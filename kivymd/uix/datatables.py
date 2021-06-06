"""
Components/DataTables
=====================

.. seealso::

    `Material Design spec, DataTables <https://material.io/components/data-tables>`_

.. rubric:: Data tables display sets of data across rows and columns.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-previous.png
    :align: center

Warnings
---------

.. warning::

    Data tables are still far from perfect. The class is in constant change,
    because of optimizations and bug fixes.

    If you find a bug or have an improvement you want to share, take some time
    and share your discoveries with us over the main git repo.

    Any help is well appreciated.

.. warning::

    In versions prior to Kivy 2.1-dev0 exists an error in which is the table
    has only one row in the current page, the table will only render one
    column instead of the whole row.

.. note::

    MDDataTable allows developers to sort the data provided by column. This
    happens thanks to the use of an external function that you can bind while
    you're defining the table columns.

    Be aware that the sorting function must return a 2 value list in the
    format of:

    `[Index, Sorted_Row_Data]`

    This is because the index list is needed to allow MDDataTable to keep track
    of the selected rows. and, after the data is sorted, update the row
    checkboxes.

"""

# Special thanks for the info -
# https://stackoverflow.com/questions/50219281/python-how-to-add-vertical-scroll-in-recycleview

__all__ = ("MDDataTable",)

from collections import defaultdict

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
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
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE
#:import StiffScrollEffect kivymd.effects.stiffscroll.StiffScrollEffect


<CellRow>
    orientation: "vertical"

    canvas.before:
        Color:
            rgba:
                (\
                root.theme_cls.bg_darkest \
                if root.theme_cls.theme_style == "Light" else \
                root.theme_cls.bg_light \
                ) \
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

        MDBoxLayout:
            id: inner_box

            MDIcon:
                id: icon
                size_hint: None, None
                pos_hint: {"center_y": 0.5}
                size: ("24dp", "24dp") if root.icon else (0, 0)
                icon: root.icon if root.icon else ""
                theme_text_color: "Custom"
                text_color:
                    root.icon_color if root.icon_color else \
                    root.theme_cls.primary_color

            MDLabel:
                id: label
                text: " " + root.text
                markup: True
                color:
                    (1, 1, 1, 1) \
                    if root.theme_cls.theme_style == "Dark" else \
                    (0, 0, 0, 1)

    MDSeparator:


<CellHeader>
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height
    spacing: "4dp"
    tooltip_text: root.text

    BoxLayout:
        id: box
        size_hint_y: None
        height: lbl.height

        MDLabel:
            id: lbl
            text: " " + root.text
            size_hint_y: None
            height: self.texture_size[1]
            bold: True
            markup: True
            color:
                (1, 1, 1, 1) \
                if root.theme_cls.theme_style == "Dark" else \
                (0, 0, 0, 1)

    MDSeparator:
        id: separator


<SortButton>
    id: sort_btn
    icon: "arrow-up"
    pos_hint: {"center_y": 0.5}
    #ripple_scale: .65
    size: [dp(24), dp(0)]
    theme_text_color: "Custom"
    text_color: self.theme_cls.secondary_text_color
    opacity: 0


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
                    on_release: root.table_data.select_all(self.state)

                CellHeader:
                    id: first_cell

            MDSeparator:


<TableData>
    data: root.recycle_data
    data_first_cells: root.data_first_cells
    key_viewclass: "viewclass"
    # effect_cls: StiffScrollEffect

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
        multiselect: True
        touch_multiselect: True


<TablePagination>
    adaptive_height: True
    spacing: "8dp"

    MDLabel:
        text: "Rows per page"
        shorten: True
        halign: "right"
        font_style: "Caption"
        color:
            (1, 1, 1, 1) \
            if root.theme_cls.theme_style == "Dark" else \
            (0, 0, 0, 1)

    MDDropDownItem:
        id: drop_item
        pos_hint: {'center_y': .5}
        text: str(root.table_data.rows_num)
        font_size: "14sp"
        on_release: root.table_data.open_pagination_menu()

    Widget:
        size_hint_x: None
        width: "32dp" if DEVICE_TYPE != "mobile" else "8dp"

    MDLabel:
        id: label_rows_per_page
        text: f"1-{root.table_data.rows_num} of {len(root.table_data.row_data)}"
        size_hint: None, None
        size: self.texture_size
        -text_size: None, None
        pos_hint: {"center_y": .5}
        font_style: "Caption"
        color:
            (1, 1, 1, 1) \
            if root.theme_cls.theme_style == "Dark" else \
            (0, 0, 0, 1)

    MDIconButton:
        id: button_back
        icon: "chevron-left"
        user_font_size: "20sp" if DEVICE_TYPE != "mobile" else "16dp"
        ripple_scale: .5 if DEVICE_TYPE == "mobile" else 1
        pos_hint: {'center_y': .5}
        disabled: True
        md_bg_color_disabled: 0, 0, 0, 0
        on_release: root.table_data.set_next_row_data_parts("back")

    MDIconButton:
        id: button_forward
        icon: "chevron-right"
        user_font_size: "20sp" if DEVICE_TYPE != "mobile" else "16dp"
        ripple_scale: .5 if DEVICE_TYPE == "mobile" else 1
        pos_hint: {'center_y': .5}
        disabled: True
        md_bg_color_disabled: 0, 0, 0, 0
        on_release: root.table_data.set_next_row_data_parts("forward")


<MDDataTable>

    MDCard:
        id: container
        orientation: "vertical"
        elevation: root.elevation
        padding: "24dp", "24dp", "8dp", "8dp"
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
    icon = StringProperty()
    icon_copy = icon
    icon_color = ColorProperty(None)
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(CellRow, self).__init__(**kwargs)
        self.ids.check.bind(active=self.select_check)
        self.ids.check.bind(active=self.notify_checkbox_click)

    def notify_checkbox_click(self, instance, active):
        self.table.get_select_row(self.index)

    def on_icon(self, instance, value):
        self.icon_copy = value

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

        # Fixes cloning of icons.
        ic = table_data.recycle_data[index].get("icon", None)
        cell_row_obj = table_data.view_adapter.get_visible_view(index)

        if not ic:
            cell_row_obj.icon = ""
        else:
            cell_row_obj.icon = cell_row_obj.icon_copy

        # Set checkboxes.
        if table_data.check:
            if self.index in table_data.data_first_cells:
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
                    self.change_check_state_no_notif("down")
                else:
                    self.change_check_state_no_notif("normal")
        else:
            self.change_check_state_no_notif("normal")

    def change_check_state_no_notif(self, new_state):
        checkbox = self.ids.check
        checkbox.unbind(active=self.notify_checkbox_click)
        checkbox.state = new_state
        checkbox.bind(active=self.notify_checkbox_click)

    def _check_all(self, state):
        """Checks if all checkboxes are in same state"""

        if state == "down" and self.table.check_all(state):
            self.table.table_header.ids.check.state = "down"
        else:
            self.table.table_header.ids.check.state = "normal"

    def select_check(self, instance, active):
        """Called upon activation/deactivation of the checkbox."""

        if active:
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


class SortButton(MDIconButton):
    pass


class CellHeader(MDTooltip, BoxLayout):
    text = StringProperty()  # column text
    sort_action = ObjectProperty()
    table_data = ObjectProperty()
    is_sorted = BooleanProperty(False)
    sorted_order = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        if self.sort_action:
            box = self.ids.box
            ib = SortButton()
            ib.bind(on_release=self._sort_release)

            if self.is_sorted:
                ib.icon = (
                    "arrow-down" if self.sorted_order == "ASC" else "arrow-up"
                )
                ib.size = [dp(24), dp(24)]
                ib.opacity = 1
            else:
                self.bind(on_enter=self.set_sort_btn)
                self.bind(on_leave=self.set_sort_btn)

            box.add_widget(ib, index=1)

    def _sort_release(self, inst):
        inst.icon = "arrow-down" if inst.icon == "arrow-up" else "arrow-up"

        if not self.parent.parent.col_with_sort:
            c = self.parent.children
            col_with_sort = [
                each
                for each in c
                if each.ids.get("box", None) and len(each.ids.box.children) == 2
            ]
            self.parent.parent.col_with_sort = col_with_sort
        else:
            col_with_sort = self.parent.parent.col_with_sort

        for each in col_with_sort:
            if each == self:
                self.unbind(on_enter=self.set_sort_btn)
                self.unbind(on_leave=self.set_sort_btn)
            else:
                btn = each.ids.box.children[-1]
                btn.size = [dp(24), dp(0)]
                btn.opacity = 0
                each.bind(on_enter=each.set_sort_btn)
                each.bind(on_leave=each.set_sort_btn)

        if self.sort_action:
            if not self.table_data:
                th = self.parent.parent
                self.table_data = th.table_data

            indices, sorted_data = self.sort_action(self.table_data.row_data)

            if not sorted_data:
                return

            if inst.icon == "arrow-down":
                sorted_data = sorted_data[::-1]
                indices = indices[::-1]

            self.table_data.row_data = sorted_data
            self.table_data.on_rows_num(self, self.table_data.rows_num)
            self.restore_checks(dict(zip(indices, range(len(indices)))))
            self.table_data.set_next_row_data_parts("reset")
            self.table_data.cell_row_obj_dict = {}
            self.table_data.table_header.ids.check.state = "normal"

    def restore_checks(self, indices):
        curr_checks = self.table_data.current_selection_check
        rows_num = self.table_data.rows_num
        columns = self.table_data.total_col_headings

        new_checks = defaultdict(list)
        for i, x in enumerate(curr_checks):
            for j, y in enumerate(curr_checks[x]):
                new_page = (indices[y // columns + x * rows_num]) // rows_num
                new_indice = (
                    (indices[y // columns + x * rows_num]) % rows_num
                ) * columns
                new_checks[new_page].append(new_indice)
        self.table_data.current_selection_check = dict(new_checks)

    def set_sort_btn(self, instance):
        btn = instance.ids.box.children[-1]
        if btn.opacity:
            btn.size = [dp(24), dp(0)]
            btn.opacity = 0
        else:
            btn.size = [dp(24), dp(24)]
            btn.opacity = 1


class TableHeader(ScrollView):
    table_data = ObjectProperty()  # <TableData object>
    column_data = ListProperty()  # MDDataTable.column_data
    col_headings = ListProperty()  # column names list
    sorted_on = StringProperty()
    sorted_order = StringProperty()
    # kivy.uix.gridlayout.GridLayout.cols_minimum
    cols_minimum = DictProperty()
    col_with_sort = []  # store cols which contain sort functions

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create cells.
        for i, col_heading in enumerate(self.column_data):
            self.cols_minimum[i] = col_heading[1] * 5
            self.col_headings.append(col_heading[0])
            if i:
                self.ids.header.add_widget(
                    (
                        CellHeader(
                            text=col_heading[0],
                            sort_action=col_heading[2],
                            width=self.cols_minimum[i],
                            table_data=self.table_data,
                            is_sorted=(col_heading[0] == self.sorted_on),
                            sorted_order=self.sorted_order,
                        )
                        if len(col_heading) == 3
                        else CellHeader(
                            text=col_heading[0],
                            width=self.cols_minimum[i],
                            table_data=self.table_data,
                        )
                    )
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
    cell_row_obj_dict = {}

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
        self._get_row_checks()  # update the dict

    def set_default_first_row(self, dt):
        """Set default first row as selected."""

        self.ids.row_controller.select_next(self)

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
                    self.data_first_cells.append(x[2][0])
                    self.recycle_data.append(
                        {
                            "text": str(x[0]),
                            "Index": str(j),
                            "range": x[2],
                            "selectable": True,
                            "viewclass": "CellRow",
                            "table": self,
                        }
                    )
                else:
                    r_data = {
                        "Index": str(j),
                        "range": x[2],
                        "selectable": True,
                        "viewclass": "CellRow",
                        "table": self,
                    }

                    if (
                        isinstance(x[0], tuple) or isinstance(x[0], list)
                    ) and len(x[0]) == 3:
                        r_data["icon"] = x[0][0]
                        r_data["icon_color"] = x[0][1]
                        r_data["text"] = str(x[0][2])

                        self.recycle_data.append(r_data)

                    elif (
                        isinstance(x[0], tuple) or isinstance(x[0], list)
                    ) and len(x[0]) == 2:
                        r_data["icon"] = x[0][0]
                        r_data["text"] = str(x[0][1])

                        self.recycle_data.append(r_data)

                    else:
                        r_data["text"] = str(x[0])
                        self.recycle_data.append(r_data)

            if not self.table_header.column_data:
                raise ValueError("Set value for column_data in class TableData")
            self.data_first_cells.append(self.table_header.column_data[0][0])

    def set_text_from_of(self, direction):
        """Sets the text of the numbers of displayed pages in table."""

        if self.pagination:
            if direction == "reset":
                self._current_value = 1
                self._to_value = len(self._row_data_parts[self._rows_number])
            elif direction == "forward":
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
                    self._row_data_parts[self._rows_number + 1]
                )
            if direction == "increment":
                self._current_value = 1
                self._to_value = self.rows_num + self._current_value - 1

            self.pagination.ids.label_rows_per_page.text = (
                f"{self._current_value}-{self._to_value} "
                f"of {len(self.row_data)}"
            )

    def select_all(self, state):
        """Sets the checkboxes of all rows to the active/inactive position."""

        for i in range(0, len(self.recycle_data), self.total_col_headings):
            cell_row_obj = cell_row_obj = self.view_adapter.get_visible_view(i)
            self.cell_row_obj_dict[i] = cell_row_obj
            self.on_mouse_select(cell_row_obj)
            cell_row_obj.ids.check.state = state

        if state == "down":
            # select all checks on all pages
            rows_num = self.rows_num
            columns = self.total_col_headings
            full_pages = len(self.row_data) // self.rows_num
            left_over_rows = len(self.row_data) % self.rows_num

            new_checks = {}
            for page in range(full_pages):
                new_checks[page] = list(range(0, rows_num * columns, columns))

            if left_over_rows:
                new_checks[full_pages] = list(
                    range(0, left_over_rows * columns, columns)
                )

            self.current_selection_check = new_checks
            return

        # resets all checks on all pages
        self.current_selection_check = {}

    def check_all(self, state):
        """Checks if checkboxes of all rows are in the same state"""

        tmp = []
        for i in range(0, len(self.recycle_data), self.total_col_headings):
            if self.cell_row_obj_dict.get(i, None):
                cell_row_obj = self.cell_row_obj_dict[i]
            else:
                cell_row_obj = self.view_adapter.get_visible_view(i)
                if cell_row_obj:
                    self.cell_row_obj_dict[i] = cell_row_obj
            if cell_row_obj:
                tmp.append(cell_row_obj.ids.check.state == state)
        return all(tmp)

    def _get_row_checks(self):
        """
        Returns all rows that are checked
        """

        tmp = []
        for i in range(0, len(self.recycle_data), self.total_col_headings):
            if self.cell_row_obj_dict.get(i, None):
                cell_row_obj = self.cell_row_obj_dict[i]
            else:
                cell_row_obj = self.view_adapter.get_visible_view(i)
                if cell_row_obj:
                    self.cell_row_obj_dict[i] = cell_row_obj

            if cell_row_obj and cell_row_obj.ids.check.state == "down":
                idx = cell_row_obj.index
                row = []
                for data in self.recycle_data:
                    if idx in data["range"]:
                        row.append(data["text"])

                tmp.append(row)
        return tmp

    def close_pagination_menu(self, *args):
        """Called when the pagination menu window is closed."""

        self.pagination_menu_open = False

    def open_pagination_menu(self):
        """Open pagination menu window."""

        if self.pagination_menu.items:
            self.pagination_menu_open = True
            self.pagination_menu.open()

    def set_number_displayed_lines(self, text_item):
        """
        Called when the user sets the number of pages displayed
        in the table.
        """

        self.rows_num = int(text_item)
        self.set_next_row_data_parts("reset")
        self.set_text_from_of("reset")

    def set_next_row_data_parts(self, direction):
        """Called when switching the pages of the table."""

        if direction == "reset":
            self._rows_number = 0
            self.pagination.ids.button_back.disabled = True
            self.pagination.ids.button_forward.disabled = False
        elif direction == "forward":
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

    def on_mouse_select(self, instance):
        """Called on the ``on_enter`` event of the :class:`~CellRow` class."""

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

    def on_pagination(self, instance, value):
        if self._to_value < len(self.row_data):
            self.pagination.ids.button_forward.disabled = False

    def _split_list_into_equal_parts(self, lst, parts):
        for i in range(0, len(lst), parts):
            yield lst[i : i + parts]

    # def on_pagination(self, instance_table, instance_pagination):
    #    if len(self._row_data_parts) <= self._to_value:
    #        instance_pagination.ids.button_forward.disabled = True


class TablePagination(ThemableBehavior, MDBoxLayout):
    """Pagination Container."""

    table_data = ObjectProperty()  # <TableData object>


class MDDataTable(ThemableBehavior, AnchorLayout):
    """
    :Events:
        :attr:`on_row_press`
            Called when a table row is clicked.
        :attr:`on_check_press`
            Called when the check box in the table row is checked.

    .. rubric:: Use events as follows

    .. code-block:: python

        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout
        from kivy.lang import Builder
        from kivy.logger import Logger

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable

        kv = '''
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                id:button_tab
                size_hint_y:None
                height: dp(48)

                MDFlatButton:
                    text: "Hello <3"
                    on_release:
                        app.update_row_data()

            BoxLayout:
                id:body

        '''

        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    # MDDataTable allows the use of size_hint
                    size_hint=(0.8, 0.7),
                    use_pagination=True,
                    check=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Status", dp(30)),
                        ("Signal Name", dp(60), self.sort_on_signal),
                        ("Severity", dp(30)),
                        ("Stage", dp(30)),
                        ("Schedule", dp(30), self.sort_on_schedule),
                        ("Team Lead", dp(30), self.sort_on_team)
                    ],
                    row_data=[
                        ("1", ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                         "Astrid: NE shared managed", "Medium", "Triaged", "0:33",
                         "Chase Nguyen"),
                        ("2", ("alert-circle", [1, 0, 0, 1], "Offline"),
                         "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
                         "Brie Furman"),
                        ("3", (
                            "checkbox-marked-circle",
                            [39 / 256, 174 / 256, 96 / 256, 1],
                            "Online"), "Phoenix: prod shared lyra-lists", "Minor",
                         "Not Triaged", "3:12", "Jeremy lake"),
                        ("4", (
                            "checkbox-marked-circle",
                            [39 / 256, 174 / 256, 96 / 256, 1],
                            "Online"), "Sirius: NW prod shared locations",
                         "Negligible",
                         "Triaged", "13:18", "Angelica Howards"),
                        ("5", (
                            "checkbox-marked-circle",
                            [39 / 256, 174 / 256, 96 / 256, 1],
                            "Online"), "Sirius: prod independent account",
                         "Negligible",
                         "Triaged", "22:06", "Diane Okuma"),

                    ],
                    sorted_on="Schedule",
                    sorted_order="ASC",
                    elevation=2
                )
                self.data_tables.bind(on_row_press=self.on_row_press)
                self.data_tables.bind(on_check_press=self.on_check_press)
                root = Builder.load_string(kv)
                root.ids.body.add_widget(self.data_tables)
                return root

            def update_row_data(self, *dt):
                self.data_tables.row_data = [
                (
                    "21",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed",
                    "Medium",
                    "Triaged",
                    "0:33",
                    "Chase Nguyen"
                ),
                ("32", ("alert-circle", [1, 0, 0, 1], "Offline"),
                "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
                "Brie Furman"),
                ("43", (
                "checkbox-marked-circle",
                [39 / 256, 174 / 256, 96 / 256, 1],
                "Online"), "Phoenix: prod shared lyra-lists", "Minor",
                "Not Triaged", "3:12", "Jeremy lake"),
                ("54", (
                "checkbox-marked-circle",
                [39 / 256, 174 / 256, 96 / 256, 1],
                "Online"), "Sirius: NW prod shared locations",
                "Negligible",
                "Triaged", "13:18", "Angelica Howards"),
                ("85", (
                "checkbox-marked-circle",
                [39 / 256, 174 / 256, 96 / 256, 1],
                "Online"), "Sirius: prod independent account",
                "Negligible",
                "Triaged", "22:06", "Diane Okuma"),
                ("85", (
                "checkbox-marked-circle",
                [39 / 256, 174 / 256, 96 / 256, 1],
                "Online"), "Sirius: prod independent account",
                "Negligible",
                "Triaged", "22:06", "John Sakura"),
                ]


            def on_row_press(self, instance_table, instance_row):
                '''Called when a table row is clicked.'''

                print(instance_table, instance_row)

            def on_check_press(self, instance_table, current_row):
                '''Called when the check box in the table row is checked.'''

                print(instance_table, current_row)

            # Sorting Methods:
            # Since the # 914 Pull request, the sorting method requires you to sort
            # out the indexes of each data value for the support of selections

            # The most common method to do this is with the use of the bult-in function
            # zip and enimerate, see the example below for more info.

            # the result given by these funcitons must be a list in the format of
            # [Indexes, Sorted_Row_Data]


            def sort_on_signal(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: l[1][2]
                    )
                )

            def sort_on_schedule(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: sum(
                            [int(l[1][-2].split(":")[0])*60,
                            int(l[1][-2].split(":")[1])]
                        )
                    )
                )

            def sort_on_team(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: l[1][-1]
                    )
                )

        Example().run()
    """

    column_data = ListProperty()
    """
    Data for header columns.

    .. code-block:: python

        from kivy.metrics import dp

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable
        from kivy.uix.anchorlayout import AnchorLayout


        class Example(MDApp):
            def build(self):
                layout = AnchorLayout()
                self.data_tables = MDDataTable(
                    size_hint=(0.7, 0.6),
                    use_pagination=True,
                    check=True,

                    # name column, width column, sorting function column(optional)
                    column_data=[
                        ("No.", dp(30)),
                        ("Status", dp(30)),
                        ("Signal Name", dp(60)),
                        ("Severity", dp(30)),
                        ("Stage", dp(30)),
                        ("Schedule", dp(30), lambda *args: print("Sorted using Schedule")),
                        ("Team Lead", dp(30)),
                    ],
                )
                layout.add_widget(self.data_tables)
                return layout


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-column-data.png
        :align: center

    :attr:`column_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.

    .. note::
        The functions which will be called for sorting must accept a data argument and return the sorted data.

        Incoming data format will be similar to the provided row_data except that it'll be all list instead of tuple like below.
        Any icon provided initially will also be there in this data so handle accordingly.

        .. code-block:: python

            [
                ['1', ['icon', 'No Signal'], 'Astrid: NE shared managed', 'Medium', 'Triaged', '0:33', 'Chase Nguyen'],
                ['2', 'Offline', 'Cosmo: prod shared ares', 'Huge', 'Triaged', '0:39', 'Brie Furman'],
                ['3', 'Online', 'Phoenix: prod shared lyra-lists', 'Minor', 'Not Triaged', '3:12', 'Jeremy lake'],
                ['4', 'Online', 'Sirius: NW prod shared locations', 'Negligible', 'Triaged', '13:18', 'Angelica Howards'],
                ['5', 'Online', 'Sirius: prod independent account', 'Negligible', 'Triaged', '22:06', 'Diane Okuma']
            ]

        You must sort inner lists in ascending order and return the sorted data in the same format.
    """

    row_data = ListProperty()
    """
    Data for rows. To add icon in addition to a row data, include a tuple with
    This property stores the row data used to display each row in the DataTable
    To show an icon inside a column in a row, use the folowing format in the
    row's columns.

    Format:

    `("MDicon-name", [icon color in rgba], "Column Value")`

    Example:

    .. code-block:: python
        [...]
        row_data = [

            # row 1
            [
                "value 1",
                "value 2",
                # the third value will have an icon inside the box
                ["home", [128/255, 48/255, 76/255, 1], "Offie" ]
            ],

            # row 2
            [
                "value 1",
                "value 2",
                # the third value will have an icon inside the box
                ["git", [1, 0.1, 0.1, 1], "Git Repo" ]
            ]
        ]

    For a more complex example see below.

    .. code-block:: python

        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                layout = AnchorLayout()
                data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    column_data=[
                        ("Column 1", dp(20)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(50), self.sort_on_col_3),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                        ("Column 6", dp(30)),
                        ("Column 7", dp(30), self.sort_on_col_2),
                    ],
                    row_data=[
                        # The number of elements must match the length
                        # of the `column_data` list.
                        (
                            "1",
                            ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                            "Astrid: NE shared managed",
                            "Medium",
                            "Triaged",
                            "0:33",
                            "Chase Nguyen",
                        ),
                        (
                            "2",
                            ("alert-circle", [1, 0, 0, 1], "Offline"),
                            "Cosmo: prod shared ares",
                            "Huge",
                            "Triaged",
                            "0:39",
                            "Brie Furman",
                        ),
                        (
                            "3",
                            (
                                "checkbox-marked-circle",
                                [39 / 256, 174 / 256, 96 / 256, 1],
                                "Online",
                            ),
                            "Phoenix: prod shared lyra-lists",
                            "Minor",
                            "Not Triaged",
                            "3:12",
                            "Jeremy lake",
                        ),
                        (
                            "4",
                            (
                                "checkbox-marked-circle",
                                [39 / 256, 174 / 256, 96 / 256, 1],
                                "Online",
                            ),
                            "Sirius: NW prod shared locations",
                            "Negligible",
                            "Triaged",
                            "13:18",
                            "Angelica Howards",
                        ),
                        (
                            "5",
                            (
                                "checkbox-marked-circle",
                                [39 / 256, 174 / 256, 96 / 256, 1],
                                "Online",
                            ),
                            "Sirius: prod independent account",
                            "Negligible",
                            "Triaged",
                            "22:06",
                            "Diane Okuma",
                        ),
                    ],
                )
                layout.add_widget(data_tables)
                return layout

            def sort_on_col_3(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: l[1][3]
                    )
                )

            def sort_on_col_2(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: l[1][-1]
                    )
                )

        Example().run()


    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-row-data.png
        :align: center

    :attr:`row_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    sorted_on = StringProperty()
    """
    Column name upon which the data is already sorted.

    If the table data is showing an already sorted data then this can be used
    to indicate upon which column the data is sorted.

    :attr:`sorted_on` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    sorted_order = OptionProperty("ASC", options=["ASC", "DSC"])
    """
    Order of already sorted data. Must be one of `'ASC'` for ascending or
    `'DSC'` for descending order.

    :attr:`sorted_order` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'ASC'`.
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

        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                layout = AnchorLayout()
                data_tables = MDDataTable(
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
                layout.add_widget(data_tables)
                return layout


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-use-pagination.png
        :align: center

    :attr:`use_pagination` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    elevation = NumericProperty(8)
    """
    Table elevation.

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `8`.
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

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color in the format (r, g, b, a).
    See :attr:`~kivy.uix.modalview.ModalView.background_color`.

    Use markup strings
    ------------------

    .. code-block:: python

        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable


        class Example(MDApp):
            def build(self):
                layout = AnchorLayout()
                data_tables = MDDataTable(
                    size_hint=(0.9, 0.6),
                    use_pagination=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Column 1", dp(30)),
                        ("[color=#52251B]Column 2[/color]", dp(30)),
                        ("Column 3", dp(30)),
                        ("[size=24][color=#C042B8]Column 4[/color][/size]", dp(30)),
                        ("Column 5", dp(30)),
                    ],
                    row_data=[
                        (
                            f"{i + 1}",
                            "[color=#297B50]1[/color]",
                            "[color=#C552A1]2[/color]",
                            "[color=#6C9331]3[/color]",
                            "4",
                            "5",
                        )
                        for i in range(50)
                    ],
                )
                layout.add_widget(data_tables)
                return layout


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/datatables-use-markup-strings.png
        :align: center

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty` and
    defaults to [0, 0, 0, 0].
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header = TableHeader(
            column_data=self.column_data,
            sorted_on=self.sorted_on,
            sorted_order=self.sorted_order,
        )
        self.table_data = TableData(
            self.header,
            row_data=self.row_data,
            check=self.check,
            rows_num=self.rows_num,
            _parent=self,
        )
        self.register_event_type("on_row_press")
        self.register_event_type("on_check_press")
        self.pagination = TablePagination(table_data=self.table_data)
        self.table_data.pagination = self.pagination
        self.header.table_data = self.table_data
        self.table_data.fbind("scroll_x", self._scroll_with_header)
        self.ids.container.add_widget(self.header)
        self.ids.container.add_widget(self.table_data)
        if self.use_pagination:
            self.ids.container.add_widget(self.pagination)
        Clock.schedule_once(self.create_pagination_menu, 0.5)
        self.bind(row_data=self.update_row_data)

    def update_row_data(self, instance, value):
        """
        Called when a the widget data must be updated.

        Remember that this is a heavy function. since the whole data set must
        be updated. you can get better results calling this metod with in a
        coroutine.
        """

        self.table_data.row_data = value
        self.table_data.on_rows_num(self, self.table_data.rows_num)
        # Set cursors to 0
        self.table_data._rows_number = 0
        self.table_data._current_value = 1

        if len(value) < self.table_data.rows_num:
            self.table_data._to_value = len(value)
            self.table_data.pagination.ids.button_forward.disabled = True
        else:
            self.table_data._to_value = self.table_data.rows_num
            self.table_data.pagination.ids.button_forward.disabled = False

        self.table_data.set_next_row_data_parts("")
        self.pagination.ids.button_back.disabled = True
        Clock.schedule_once(self.create_pagination_menu, 0.5)

    def on_row_press(self, *args):
        """Called when a table row is clicked."""

    def on_check_press(self, *args):
        """Called when the check box in the table row is checked."""

    def get_row_checks(self):
        """Returns all rows that are checked."""

        return self.table_data._get_row_checks()

    def create_pagination_menu(self, interval):
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "on_release": lambda x=f"{i}": self.table_data.set_number_displayed_lines(
                    x
                ),
            }
            for i in range(
                self.rows_num, len(self.row_data) // 2, self.rows_num
            )
        ]
        pagination_menu = MDDropdownMenu(
            caller=self.pagination.ids.drop_item,
            items=menu_items,
            position=self.pagination_menu_pos,
            max_height=self.pagination_menu_height,
            width_mult=2,
        )
        pagination_menu.bind(
            on_dismiss=self.table_data.close_pagination_menu,
        )
        self.table_data.pagination_menu = pagination_menu

    def _scroll_with_header(self, instance, value):
        self.header.scroll_x = value
