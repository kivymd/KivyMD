"""
Components/DataTables
=====================

.. seealso::

    `Material Design spec, DataTables <https://material.io/components/data-tables>`_

.. rubric:: Data tables display sets of data across rows and columns.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-previous.png
    :align: center

.. warning::

    Data tables are still far from perfect. Errors are possible and we hope
    you inform us about them.
"""

# Special thanks for the info -
# https://stackoverflow.com/questions/50219281/python-how-to-add-vertical-scroll-in-recycleview

__all__ = ("MDDataTable",)

from kivy import Logger
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.scrollview import ScrollView

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE
#:import StiffScrollEffect kivymd.stiffscroll.StiffScrollEffect


<CellRow>
    orientation: "vertical"

    canvas.before:
        Color:
            rgba:
                (root.theme_cls.bg_darkest if root.theme_cls.theme_style == "Light" else root.theme_cls.bg_light) \
                if self.selected else root.theme_cls.bg_normal
        Rectangle:
            pos: self.pos
            size: self.size
    on_press: if DEVICE_TYPE != "desktop": root.table.on_mouse_select(self)
    on_enter: if DEVICE_TYPE == "desktop": root.table.on_mouse_select(self)

    MDBoxLayout:
        id: box
        padding: "8dp", "8dp", 0, "8dp"
        spacing: "16dp"

        MDCheckbox:
            id: check
            size_hint: None, None
            size: 0, 0
            opacity: 0
            on_active: root.select_check(self.active)

        MDLabel:
            id: label
            text: " " + root.text
            color: (1, 1, 1, 1) if root.theme_cls.theme_style == "Dark" else (0, 0, 0, 1)

    MDSeparator:


<CellHeader>
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height
    spacing: "4dp"
    tooltip_text: root.text

    MDLabel:
        text: " " + root.text
        size_hint_y: None
        height: self.texture_size[1]
        bold: True
        color: (1, 1, 1, 1) if root.theme_cls.theme_style == "Dark" else (0, 0, 0, 1)

    MDSeparator:
        id: separator


<TableHeader>
    bar_width: 0
    do_scroll: False
    size_hint: 1, None
    height: header.height

    MDGridLayout:
        id: header
        rows: 1
        cols_minimum: root.cols_minimum
        adaptive_size: True
        padding: 0, "8dp", 0, 0

        MDBoxLayout:
            orientation: "vertical"

            MDBoxLayout:
                id: box
                padding: "8dp", "8dp", "4dp", 0
                spacing: "16dp"

                MDCheckbox:
                    id: check
                    size_hint: None, None
                    size: 0, 0
                    opacity: 0
                    on_active: root.table_data.select_all(self.state)
                    disabled: True

                #MDIconButton:
                #    id: sort_button
                #    icon: "menu-up"
                #    pos_hint: {"center_y": 1}
                #    ripple_scale: .65
                #    on_release: root.table_data.sort_by_name()

                CellHeader:
                    id: first_cell

            MDSeparator:


<TableData>
    data: root.recycle_data
    data_first_cells: root.data_first_cells
    key_viewclass: "viewclass"
    effect_cls: StiffScrollEffect

    TableRecycleGridLayout:
        id: row_controller
        key_selection: "selectable"
        cols: root.total_col_headings
        cols_minimum: root.cols_minimum
        default_size: None, dp(52)
        default_size_hint: 1, None
        size_hint: None, None
        height: self.minimum_height
        width: self.minimum_width
        orientation: "vertical"
        multiselect: True
        touch_multiselect: True


<TablePagination>
    adaptive_height: True
    spacing: "8dp"

    Widget:

    MDLabel:
        text: "Rows per page"
        size_hint: None, 1
        width: self.texture_size[0]
        text_size: None, None
        font_style: "Caption"
        color: (1, 1, 1, 1) if root.theme_cls.theme_style == "Dark" else (0, 0, 0, 1)

    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_y': .5}
        text: str(root.table_data.rows_num)
        font_size: "14sp"
        on_release: root.table_data.open_pagination_menu()

    Widget:
        size_hint_x: None
        width: "32dp"

    MDLabel:
        id: label_rows_per_page
        text: f"1-{root.table_data.rows_num} of {len(root.table_data.row_data)}"
        size_hint: None, 1
        #width: self.texture_size[0]
        text_size: None, None
        font_style: "Caption"
        color: (1, 1, 1, 1) if root.theme_cls.theme_style == "Dark" else (0, 0, 0, 1)

    MDIconButton:
        id: button_back
        icon: "chevron-left"
        user_font_size: "20sp"
        pos_hint: {'center_y': .5}
        disabled: True
        on_release: root.table_data.set_next_row_data_parts("back")

    MDIconButton:
        id: button_forward
        icon: "chevron-right"
        user_font_size: "20sp"
        pos_hint: {'center_y': .5}
        on_release: root.table_data.set_next_row_data_parts("forward")


<MDDataTable>

    MDCard:
        id: container
        orientation: "vertical"
        elevation: 14
        md_bg_color: 0, 0, 0, 0
        padding: "24dp", "24dp", "8dp", "8dp"

        canvas:
            Color:
                rgba: root.theme_cls.bg_normal
            RoundedRectangle:
                pos: self.pos
                size: self.size
"""
)


class TableRecycleGridLayout(
    FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout
):
    selected_row = NumericProperty(0)
    table_data = ObjectProperty(None)

    def get_nodes(self):
        nodes = self.get_selectable_nodes()
        if self.nodes_order_reversed:
            nodes = nodes[::-1]
        if not nodes:
            return None, None

        selected = self.selected_nodes
        if not selected:  # nothing selected, select the first
            self.selected_row = 0
            self.select_row(nodes)
            return None, None

        if len(nodes) == 1:  # the only selectable node is selected already
            return None, None

        index = selected[-1]
        if index > len(nodes):
            last = len(nodes)
        else:
            last = nodes.index(index)
        self.clear_selection()
        return last, nodes

    def select_next(self, instance):
        """Select next row."""

        self.table_data = instance
        last, nodes = self.get_nodes()
        if not nodes:
            return

        if last == len(nodes) - 1:
            self.selected_row = nodes[0]
        else:
            self.selected_row = nodes[last + 1]

        self.selected_row += self.table_data.total_col_headings
        self.select_row(nodes)

    def select_current(self, instance):
        """Select current row."""

        self.table_data = instance
        last, nodes = self.get_nodes()
        if not nodes:
            return

        self.select_row(nodes)

    def select_row(self, nodes):
        col = self.table_data.recycle_data[self.selected_row]["range"]
        for x in range(col[0], col[1] + 1):
            self.select_node(nodes[x])


class CellRow(
    ThemableBehavior,
    RecycleDataViewBehavior,
    HoverBehavior,
    ButtonBehavior,
    BoxLayout,
):
    text = StringProperty()  # row text
    table = ObjectProperty()  # <TableData object>
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def on_table(self, instance, table):
        """Sets padding/spacing to zero if no checkboxes are used for rows."""

        if not table.check:
            self.ids.box.padding = 0
            self.ids.box.spacing = 0

    def refresh_view_attrs(self, table_data, index, data):
        """
        Called by the :class:`RecycleAdapter` when the view is initially
        populated with the values from the `data` dictionary for this item.

        Any pos or size info should be removed because they are set
        subsequently with :attr:`refresh_view_layout`.

        :Parameters:

            `table_data`: :class:`TableData` instance
                The :class:`TableData` that caused the update.
            `data`: dict
                The data dict used to populate this view.
        """

        self.index = index
        return super().refresh_view_attrs(table_data, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            if self.table._parent:
                self.table._parent.dispatch("on_row_press", self)
            return True

    def apply_selection(self, table_data, index, is_selected):
        """Called when list items of table appear on the screen."""

        self.selected = is_selected

        # Set checkboxes.
        if table_data.check:
            if self.text in table_data.data_first_cells:
                self.ids.check.size = (dp(32), dp(32))
                self.ids.check.opacity = 1
                self.ids.box.spacing = dp(16)
                self.ids.box.padding[0] = dp(8)
            else:
                self.ids.check.size = (0, 0)
                self.ids.check.opacity = 0
                self.ids.box.spacing = 0
                self.ids.box.padding[0] = 0
        # Set checkboxes state.
        if table_data._rows_number in table_data.current_selection_check:
            for index in table_data.current_selection_check[
                table_data._rows_number
            ]:
                if (
                    self.index
                    in table_data.current_selection_check[
                        table_data._rows_number
                    ]
                ):
                    self.ids.check.state = "down"
                else:
                    self.ids.check.state = "normal"
        else:
            self.ids.check.state = "normal"

    def select_check(self, active):
        """Called upon activation/deactivation of the checkbox."""

        if active and self.index not in self.table.current_selection_check:
            if (
                self.table._rows_number
                not in self.table.current_selection_check
            ):
                self.table.current_selection_check[self.table._rows_number] = []
            if (
                self.index
                not in self.table.current_selection_check[
                    self.table._rows_number
                ]
            ):
                self.table.current_selection_check[
                    self.table._rows_number
                ].append(self.index)
        else:
            if self.table._rows_number in self.table.current_selection_check:
                if (
                    self.index
                    in self.table.current_selection_check[
                        self.table._rows_number
                    ]
                    and not active
                ):
                    self.table.current_selection_check[
                        self.table._rows_number
                    ].remove(self.index)
        self.table.get_select_row(self.index)


class CellHeader(MDTooltip, BoxLayout):
    text = StringProperty()  # column text


class TableHeader(ScrollView):
    table_data = ObjectProperty()  # <TableData object>
    column_data = ListProperty()  # MDDataTable.column_data
    col_headings = ListProperty()  # column names list
    sort = BooleanProperty(False)  # MDDataTable.sort
    # kivy.uix.gridlayout.GridLayout.cols_minimum
    cols_minimum = DictProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create cells.
        for i, col_heading in enumerate(self.column_data):
            self.cols_minimum[i] = col_heading[1] * 5
            self.col_headings.append(col_heading[0])
            if i:
                self.ids.header.add_widget(
                    CellHeader(text=col_heading[0], width=self.cols_minimum[i])
                )
            else:
                # Sets the text in the first cell.
                self.ids.first_cell.text = col_heading[0]
                self.ids.first_cell.ids.separator.height = 0
                self.ids.first_cell.width = self.cols_minimum[i]

    def on_table_data(self, instance, value):
        """Sets the checkbox in the first cell."""

        if self.table_data.check:
            self.ids.check.size = (dp(32), dp(32))
            self.ids.check.opacity = 1
        else:
            self.ids.box.padding[0] = 0
            self.ids.box.spacing = 0

    def on_sort(self, instance, value):
        """Rows sorting method."""

        Logger.info("TableData: Sorting table items is not implemented")
        # if not self.sort:
        #    self.ids.sort_button.size = (0, 0)
        #    self.ids.sort_button.opacity = 0


class TableData(RecycleView):
    recycle_data = ListProperty()  # kivy.uix.recycleview.RecycleView.data
    data_first_cells = ListProperty()  # list of first row cells
    row_data = ListProperty()  # MDDataTable.row_data
    total_col_headings = NumericProperty(0)  # TableHeader.col_headings
    cols_minimum = DictProperty()  # TableHeader.cols_minimum
    table_header = ObjectProperty()  # <TableHeader object>
    pagination_menu = ObjectProperty()  # <MDDropdownMenu object>
    pagination = ObjectProperty()  # <TablePagination object>
    check = ObjectProperty()  # MDDataTable.check
    rows_num = NumericProperty()  # number of rows displayed on the table page
    # Open or close the menu for selecting the number of rows displayed
    # on the table page.
    pagination_menu_open = BooleanProperty(False)
    # List of indexes of marked checkboxes.
    current_selection_check = DictProperty()
    sort = BooleanProperty()

    _parent = ObjectProperty()
    _rows_number = NumericProperty(0)
    _rows_num = NumericProperty()
    _current_value = NumericProperty(1)
    _to_value = NumericProperty()
    _row_data_parts = ListProperty()

    def __init__(self, table_header, **kwargs):
        super().__init__(**kwargs)
        self.table_header = table_header
        self.total_col_headings = len(table_header.col_headings)
        self.cols_minimum = table_header.cols_minimum
        self.set_row_data()
        Clock.schedule_once(self.set_default_first_row, 0)

    def get_select_row(self, index):
        """Returns the current row with all elements."""

        row = []
        for data in self.recycle_data:
            if index in data["range"]:
                row.append(data["text"])
        self._parent.dispatch("on_check_press", row)

    def set_default_first_row(self, dt):
        """Set default first row as selected."""

        self.ids.row_controller.select_next(self)

    def sort_by_name(self):
        """Sorts table data."""

        # TODO: implement a rows sorting method.

    def set_row_data(self):
        data = []
        low = 0
        high = self.total_col_headings - 1
        self.recycle_data = []
        self.data_first_cells = []

        if self._row_data_parts:
            # for row in self.row_data:
            for row in self._row_data_parts[self._rows_number]:
                for i in range(len(row)):
                    data.append([row[i], row[0], [low, high]])
                low += self.total_col_headings
                high += self.total_col_headings

            for j, x in enumerate(data):
                if x[0] == x[1]:
                    self.data_first_cells.append(x[0])
                self.recycle_data.append(
                    {
                        "text": str(x[0]),
                        "Index": str(x[1]),
                        "range": x[2],
                        "selectable": True,
                        "viewclass": "CellRow",
                        "table": self,
                    }
                )
            if not self.table_header.column_data:
                raise ValueError("Set value for column_data in class TableData")
            self.data_first_cells.append(self.table_header.column_data[0][0])

    def set_text_from_of(self, direction):
        """Sets the text of the numbers of displayed pages in table."""

        if self.pagination:
            if direction == "forward":
                if (
                    len(self._row_data_parts[self._rows_number])
                    < self._to_value
                ):
                    self._current_value = self._current_value + self.rows_num
                else:
                    self._current_value = self._current_value + len(
                        self._row_data_parts[self._rows_number]
                    )
                self._to_value = self._to_value + len(
                    self._row_data_parts[self._rows_number]
                )
            if direction == "back":
                self._current_value = self._current_value - len(
                    self._row_data_parts[self._rows_number]
                )
                self._to_value = self._to_value - len(
                    self._row_data_parts[self._rows_number]
                )
            if direction == "increment":
                self._current_value = 1
                self._to_value = self.rows_num + self._current_value - 1

            self.pagination.ids.label_rows_per_page.text = f"{self._current_value}-{self._to_value} of {len(self.row_data)}"

    def select_all(self, state):
        """Sets the checkboxes of all rows to the active/inactive position."""

        # FIXME: fix the work of selecting all cells..
        for i, data in enumerate(self.recycle_data):
            opts = self.layout_manager.view_opts
            cell_row_obj = self.view_adapter.get_view(
                i, self.data[i], opts[i]["viewclass"]
            )
            cell_row_obj.ids.check.state = state
            self.on_mouse_select(cell_row_obj)
            cell_row_obj.select_check(True if state == "down" else False)

    def close_pagination_menu(self, *args):
        """Called when the pagination menu window is closed."""

        self.pagination_menu_open = False

    def open_pagination_menu(self):
        """Open pagination menu window."""

        if self.pagination_menu.items:
            self.pagination_menu_open = True
            self.pagination_menu.open()

    def set_number_displayed_lines(self, instance_menu_item):
        """
        Called when the user sets the number of pages displayed
        in the table.
        """

        self.rows_num = int(instance_menu_item.text)
        self.set_row_data()
        self.set_text_from_of("increment")

    def set_next_row_data_parts(self, direction):
        """Called when switching the pages of the table."""

        if direction == "forward":
            self._rows_number += 1
            self.pagination.ids.button_back.disabled = False
        elif direction == "back":
            self._rows_number -= 1
            self.pagination.ids.button_forward.disabled = False

        self.set_row_data()
        self.set_text_from_of(direction)

        if self._to_value == len(self.row_data):
            self.pagination.ids.button_forward.disabled = True
        if self._current_value == 1:
            self.pagination.ids.button_back.disabled = True

    def _split_list_into_equal_parts(self, lst, parts):
        for i in range(0, len(lst), parts):
            yield lst[i : i + parts]

    def on_mouse_select(self, instance):
        """Called on the ``on_enter`` event of the :class:`~CellRow` class"""

        if not self.pagination_menu_open:
            if self.ids.row_controller.selected_row != instance.index:
                self.ids.row_controller.selected_row = instance.index
                self.ids.row_controller.select_current(self)

    def on_rows_num(self, instance, value):
        if not self._to_value:
            self._to_value = value

        self._rows_number = 0
        self._row_data_parts = list(
            self._split_list_into_equal_parts(self.row_data, value)
        )

    # def on_pagination(self, instance_table, instance_pagination):
    #    if len(self._row_data_parts) <= self._to_value:
    #        instance_pagination.ids.button_forward.disabled = True


class TablePagination(ThemableBehavior, MDBoxLayout):
    """Pagination Container."""

    table_data = ObjectProperty()  # <TableData object>


class MDDataTable(BaseDialog):
    """
    :Events:
        :attr:`on_row_press`
            Called when a table row is clicked.
        :attr:`on_check_press`
            Called when the check box in the table row is checked.

    .. rubric:: Use events as follows

    .. code-block:: python

        from kivy.metrics import dp

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    use_pagination=True,
                    check=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Column 1", dp(30)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(30)),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                    ],
                    row_data=[
                        (f"{i + 1}", "2.23", "3.65", "44.1", "0.45", "62.5")
                        for i in range(50)
                    ],
                )
                self.data_tables.bind(on_row_press=self.on_row_press)
                self.data_tables.bind(on_check_press=self.on_check_press)

            def on_start(self):
                self.data_tables.open()

            def on_row_press(self, instance_table, instance_row):
                '''Called when a table row is clicked.'''

                print(instance_table, instance_row)

            def on_check_press(self, instance_table, current_row):
                '''Called when the check box in the table row is checked.'''

                print(instance_table, current_row)


        Example().run()
    """

    column_data = ListProperty()
    """
    Data for header columns.

    .. code-block:: python

        from kivy.metrics import dp

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    # name column, width column
                    column_data=[
                        ("Column 1", dp(30)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(30)),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                        ("Column 6", dp(30)),
                    ],
                )

            def on_start(self):
                self.data_tables.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-column-data.png
        :align: center

    :attr:`column_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    row_data = ListProperty()
    """
    Data for rows.

    .. code-block:: python

        from kivy.metrics import dp

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    column_data=[
                        ("Column 1", dp(30)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(30)),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                        ("Column 6", dp(30)),
                    ],
                    row_data=[
                        # The number of elements must match the length
                        # of the `column_data` list.
                        ("1", "2", "3", "4", "5", "6"),
                        ("1", "2", "3", "4", "5", "6"),
                    ],
                )

            def on_start(self):
                self.data_tables.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-row-data.png
        :align: center

    :attr:`row_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    sort = BooleanProperty(False)
    """
    Whether to display buttons for sorting table items.

    :attr:`sort` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    check = BooleanProperty(False)
    """
    Use or not use checkboxes for rows.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-check.gif
        :align: center

    :attr:`check` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    use_pagination = BooleanProperty(False)
    """
    Use page pagination for table or not.

    .. code-block:: python

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    use_pagination=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Column 1", dp(30)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(30)),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                    ],
                    row_data=[
                        (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
                    ],
                )

            def on_start(self):
                self.data_tables.open()


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-use-pagination.png
        :align: center

    :attr:`use_pagination` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    rows_num = NumericProperty(5)
    """
    The number of rows displayed on one page of the table.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-use-pagination.gif
        :align: center

    :attr:`rows_num` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `10`.
    """

    pagination_menu_pos = OptionProperty("center", options=["center", "auto"])
    """
    Menu position for selecting the number of displayed rows.
    Available options are `'center'`, `'auto'`.

    .. rubric:: Center

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-menu-pos-center.png
        :align: center

    .. rubric:: Auto

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-menu-pos-auto.png
        :align: center

    :attr:`pagination_menu_pos` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    pagination_menu_height = NumericProperty("140dp")
    """
    Menu height for selecting the number of displayed rows.

    .. rubric:: 140dp

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-menu-height-140.png
        :align: center

    .. rubric:: 240dp

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-menu-height-240.png
        :align: center

    :attr:`pagination_menu_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'140dp'`.
    """

    background_color = ListProperty([0, 0, 0, 0])
    """
    Background color in the format (r, g, b, a).
    See :attr:`~kivy.uix.modalview.ModalView.background_color`.

    :attr:`background_color` is a :class:`~kivy.properties.ListProperty` and
    defaults to [0, 0, 0, .7].
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_row_press")
        self.register_event_type("on_check_press")
        self.header = TableHeader(column_data=self.column_data, sort=self.sort)
        self.table_data = TableData(
            self.header,
            row_data=self.row_data,
            check=self.check,
            rows_num=self.rows_num,
            _parent=self,
        )
        self.pagination = TablePagination(table_data=self.table_data)
        self.table_data.pagination = self.pagination
        self.header.table_data = self.table_data
        self.table_data.fbind("scroll_x", self._scroll_with_header)
        self.ids.container.add_widget(self.header)
        self.ids.container.add_widget(self.table_data)
        if self.use_pagination:
            self.ids.container.add_widget(self.pagination)
        Clock.schedule_once(self.create_pagination_menu, 0.5)

    def on_row_press(self, *args):
        """Called when a table row is clicked."""

    def on_check_press(self, *args):
        """Called when the check box in the table row is checked."""

    def _scroll_with_header(self, instance, value):
        self.header.scroll_x = value

    def create_pagination_menu(self, interval):
        menu_items = [
            {"text": f"{i}"}
            for i in range(
                self.rows_num, len(self.row_data) // 2, self.rows_num
            )
        ]
        pagination_menu = MDDropdownMenu(
            caller=self.pagination.ids.drop_item,
            items=menu_items,
            use_icon_item=False,
            position=self.pagination_menu_pos,
            max_height=self.pagination_menu_height,
            callback=self.table_data.set_number_displayed_lines,
            width_mult=2,
        )
        pagination_menu.bind(on_dismiss=self.table_data.close_pagination_menu)
        self.table_data.pagination_menu = pagination_menu
