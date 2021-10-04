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

.. warning:: Data tables are still far from perfect. The class is in constant
    change, because of optimizations and bug fixes. If you find a bug or have
    an improvement you want to share, take some time and share your discoveries
    with us over the main git repo.
    Any help is well appreciated.

.. warning:: In versions prior to `Kivy 2.1.0-dev0` exists an error in which is
    the table has only one row in the current page, the table will only render
    one column instead of the whole row.

.. note:: `MDDataTable` allows developers to sort the data provided by column.
    This happens thanks to the use of an external function that you can bind
    while you're defining the table columns. Be aware that the sorting function
    must return a 2 value list in the format of:
        `[Index, Sorted_Row_Data]`

    This is because the index list is needed to allow MDDataTable to keep track
    of the selected rows. and, after the data is sorted, update the row
    checkboxes.

"""

# Special thanks for the info -
# https://stackoverflow.com/questions/50219281/python-how-to-add-vertical-scroll-in-recycleview

__all__ = ("MDDataTable",)

import os
from collections import defaultdict
from typing import NoReturn, Union

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

from kivymd import uix_path
from kivymd.effects.stiffscroll import StiffScrollEffect
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tooltip import MDTooltip

with open(
    os.path.join(uix_path, "datatables", "datatables.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


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


class CellHeader(MDTooltip, BoxLayout):
    """
    Implements the label text in the column header panel from
    :attr:`~MDDataTable.column_data` data.
    """

    text = StringProperty()
    """
    Column text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    # TODO: Added example.
    sort_action = ObjectProperty()
    """
    Custom function for sorting.

    :attr:`sort_action` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    table_data = ObjectProperty()
    """
    :class:`~TableData` class.

    :attr:`table_data` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

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

    def restore_checks(self, indices: dict) -> NoReturn:
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

    def set_sort_btn(self, instance_cell_header) -> NoReturn:
        btn = instance_cell_header.ids.box.children[-1]
        if btn.opacity:
            btn.size = [dp(24), dp(0)]
            btn.opacity = 0
        else:
            btn.size = [dp(24), dp(24)]
            btn.opacity = 1

    def _sort_release(self, inst):
        inst.icon = "arrow-down" if inst.icon == "arrow-up" else "arrow-up"

        if not self.parent.parent._col_with_sort:
            c = self.parent.children
            col_with_sort = [
                each
                for each in c
                if each.ids.get("box", None) and len(each.ids.box.children) == 2
            ]
            self.parent.parent._col_with_sort = col_with_sort
        else:
            col_with_sort = self.parent.parent._col_with_sort

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


class TableHeader(ThemableBehavior, ScrollView):
    """
    Implements a panel for column heading labels -
    :attr:`~MDDataTable.column_data`.
    """

    table_data = ObjectProperty()
    """
    Class :class:`~TableData`.

    :attr:`table_data` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    column_data = ListProperty()
    """
    See :attr:`~MDDataTable.sorted_on`

    :attr:`column_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    sorted_on = StringProperty()
    """
    See :attr:`~MDDataTable.sorted_on`.
    
    :attr:`sorted_on` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    cols_minimum = DictProperty()
    """
    See :attr:`~kivy.uix.gridlayout.GridLayout.cols_minimum`.

    :attr:`cols_minimum` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{}`.
    """

    sorted_order = StringProperty()
    """
    See :attr:`~MDDataTable.sorted_order`.

    :attr:`sorted_order` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    background_color_header = ColorProperty(None)
    """
    See :attr:`~MDDataTable.background_color_header`.

    .. versionadded:: 1.0.0

    :attr:`background_color_header` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _col_with_sort = []  # store cols which contain sort functions
    _col_headings = ListProperty()  # column names list

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create cells.
        for i, col_heading in enumerate(self.column_data):
            self.cols_minimum[i] = col_heading[1] * 5
            self._col_headings.append(col_heading[0])
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

    def on_table_data(
        self, instance_table_header, instance_table_data
    ) -> NoReturn:
        """Sets the checkbox in the first cell."""

        if self.table_data.check:
            self.ids.check.size = (dp(32), dp(32))
            self.ids.check.opacity = 1
        else:
            self.ids.box.padding[0] = 0
            self.ids.box.spacing = 0


class TableData(RecycleView):
    """Implements a list of table data."""

    recycle_data = ListProperty()
    """
    See :attr:`~kivy.uix.recycleview.RecycleView.data`.

    :attr:`recycle_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    data_first_cells = ListProperty()
    """
    List of first row cells.

    :attr:`data_first_cells` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    row_data = ListProperty()
    """
    See :attr:`~MDDataTable.row_data`.

    :attr:`row_data` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    total_col_headings = NumericProperty(0)  # TableHeader._col_headings
    """
    See :attr:`~TableHeader._col_headings`.

    :attr:`total_col_headings` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    cols_minimum = DictProperty()
    """
    See :attr:`~TableHeader.cols_minimum`.

    :attr:`cols_minimum` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{}`.
    """

    table_header = ObjectProperty()
    """
    :class:`~TableHeader` class.

    :attr:`table_header` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    pagination_menu = ObjectProperty()
    """
    :class:`~kivymd.uix.menu.MDDropdownMenu` class.

    :attr:`pagination_menu` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    pagination = ObjectProperty()
    """
    :class:`~TablePagination` class.

    :attr:`pagination` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    check = ObjectProperty()
    """
    See :attr:`~MDDataTable.check`.

    :attr:`check` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    rows_num = NumericProperty()
    """
    Number of rows displayed on the table page.

    :attr:`rows_num` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    pagination_menu_open = BooleanProperty(False)
    """
    Open or close the menu for selecting the number of rows displayed
    on the table page.

    :attr:`pagination_menu_open` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    current_selection_check = DictProperty()
    """
    List of indexes of marked checkboxes.

    :attr:`current_selection_check` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{}`.
    """

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
        self.total_col_headings = len(table_header._col_headings)
        self.cols_minimum = table_header.cols_minimum
        self.set_row_data()
        self.effect_cls = self._parent.effect_cls
        Clock.schedule_once(self.set_default_first_row, 0)

    def get_select_row(self, index: int) -> NoReturn:
        """Returns the current row with all elements."""

        row = []
        for data in self.recycle_data:
            if index in data["range"]:
                row.append(data["text"])
        self._parent.dispatch("on_check_press", row)
        self._get_row_checks()  # update the dict

    def set_default_first_row(self, interval: Union[int, float]) -> NoReturn:
        """Set default first row as selected."""

        self.ids.row_controller.select_next(self)

    def set_row_data(self) -> NoReturn:
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
                            "background_color_cell": self._parent.background_color_cell,
                            "background_color_selected_cell": self._parent.background_color_selected_cell,
                        }
                    )
                else:
                    r_data = {
                        "Index": str(j),
                        "range": x[2],
                        "selectable": True,
                        "viewclass": "CellRow",
                        "table": self,
                        "background_color_cell": self._parent.background_color_cell,
                        "background_color_selected_cell": self._parent.background_color_selected_cell,
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

    def set_text_from_of(self, direction: str) -> NoReturn:
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

    def select_all(self, state: str) -> NoReturn:
        """Sets the checkboxes of all rows to the active/inactive position."""

        for i in range(0, len(self.recycle_data), self.total_col_headings):
            cell_row_obj = self.view_adapter.get_visible_view(i)
            if cell_row_obj:
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

    def check_all(self, state: str) -> NoReturn:
        """Checks if checkboxes of all rows are in the same state."""

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

    def close_pagination_menu(self, *args) -> NoReturn:
        """Called when the pagination menu window is closed."""

        self.pagination_menu_open = False

    def open_pagination_menu(self) -> NoReturn:
        """Open pagination menu window."""

        if self.pagination_menu.items:
            self.pagination_menu_open = True
            self.pagination_menu.open()

    def set_number_displayed_lines(self, text_item) -> NoReturn:
        """
        Called when the user sets the number of pages displayed
        in the table.
        """

        # self.rows_num = int(text_item)
        self.rows_num = int(text_item)
        self.set_next_row_data_parts("reset")
        self.set_text_from_of("reset")
        self.pagination_menu.caller.text = text_item

    def set_next_row_data_parts(self, direction: str) -> NoReturn:
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

    def on_mouse_select(self, instance_cell_row) -> NoReturn:
        """Called on the ``on_enter`` event of the :class:`~CellRow` class."""

        if not self.pagination_menu_open:
            if self.ids.row_controller.selected_row != instance_cell_row.index:
                self.ids.row_controller.selected_row = instance_cell_row.index
                self.ids.row_controller.select_current(self)

    def on_rows_num(self, instance_table_date, value_rows_num: int) -> NoReturn:
        if not self._to_value:
            self._to_value = value_rows_num

        self._rows_number = 0
        self._row_data_parts = list(
            self._split_list_into_equal_parts(self.row_data, value_rows_num)
        )

    def on_pagination(
        self, instance_table_date, instance_table_pagination
    ) -> NoReturn:
        if self._to_value < len(self.row_data):
            self.pagination.ids.button_forward.disabled = False

    def _split_list_into_equal_parts(self, lst, parts):
        for i in range(0, len(lst), parts):
            yield lst[i : i + parts]

    def _get_row_checks(self):
        """Returns all rows that are checked."""

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

    # def on_pagination(self, instance_table, instance_pagination):
    #    if len(self._row_data_parts) <= self._to_value:
    #        instance_pagination.ids.button_forward.disabled = True


class TablePagination(ThemableBehavior, MDBoxLayout):
    """Pagination Container."""

    table_data = ObjectProperty()
    """
    :class:`~TableData` class.

    :attr:`table_data` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """


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

        from kivymd.app import MDApp
        from kivymd.uix.datatables import MDDataTable
        from kivymd.uix.screen import MDScreen


        class Example(MDApp):
            def build(self):
                self.data_tables = MDDataTable(
                    use_pagination=True,
                    check=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Status", dp(30)),
                        ("Signal Name", dp(60), self.sort_on_signal),
                        ("Severity", dp(30)),
                        ("Stage", dp(30)),
                        ("Schedule", dp(30), self.sort_on_schedule),
                        ("Team Lead", dp(30), self.sort_on_team),
                    ],
                    row_data=[
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
                    sorted_on="Schedule",
                    sorted_order="ASC",
                    elevation=2,
                )
                self.data_tables.bind(on_row_press=self.on_row_press)
                self.data_tables.bind(on_check_press=self.on_check_press)
                screen = MDScreen()
                screen.add_widget(self.data_tables)
                return screen

            def on_row_press(self, instance_table, instance_row):
                '''Called when a table row is clicked.'''

                print(instance_table, instance_row)

            def on_check_press(self, instance_table, current_row):
                '''Called when the check box in the table row is checked.'''

                print(instance_table, current_row)

            # Sorting Methods:
            # since the https://github.com/kivymd/KivyMD/pull/914 request, the
            # sorting method requires you to sort out the indexes of each data value
            # for the support of selections.
            #
            # The most common method to do this is with the use of the builtin function
            # zip and enumerate, see the example below for more info.
            #
            # The result given by these funcitons must be a list in the format of
            # [Indexes, Sorted_Row_Data]

            def sort_on_signal(self, data):
                return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

            def sort_on_schedule(self, data):
                return zip(
                    *sorted(
                        enumerate(data),
                        key=lambda l: sum(
                            [
                                int(l[1][-2].split(":")[0]) * 60,
                                int(l[1][-2].split(":")[1]),
                            ]
                        ),
                    )
                )

            def sort_on_team(self, data):
                return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


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

    .. note:: The functions which will be called for sorting must accept a data
        argument and return the sorted data. Incoming data format will be
        similar to the provided row_data except that it'll be all list instead
        of tuple like below. Any icon provided initially will also be there in
        this data so handle accordingly.

        .. code-block:: python

            [
                [
                    "1",
                    ["icon", "No Signal"],
                    "Astrid: NE shared managed",
                    "Medium",
                    "Triaged",
                    "0:33",
                    "Chase Nguyen",
                ],
                [
                    "2",
                    "Offline",
                    "Cosmo: prod shared ares",
                    "Huge",
                    "Triaged",
                    "0:39",
                    "Brie Furman",
                ],
                [
                    "3",
                    "Online",
                    "Phoenix: prod shared lyra-lists",
                    "Minor",
                    "Not Triaged",
                    "3:12",
                    "Jeremy lake",
                ],
                [
                    "4",
                    "Online",
                    "Sirius: NW prod shared locations",
                    "Negligible",
                    "Triaged",
                    "13:18",
                    "Angelica Howards",
                ],
                [
                    "5",
                    "Online",
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma",
                ],
            ]

        You must sort inner lists in ascending order and return the sorted data
        in the same format.
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

    pagination_menu_pos = OptionProperty(
        "top", options=["center", "auto", "top"]
    )
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
    defaults to `[0, 0, 0, 0]`.
    """

    background_color_header = ColorProperty(None)
    """
    Background color for :class:`~TableHeader` class.

    .. versionadded:: 1.0.0

    .. code-block:: python

        self.data_tables = MDDataTable(
            ...,
            background_color_header=get_color_from_hex("#65275d"),
        )
        
    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-background-color-header.png
        :align: center

    :attr:`background_color_header` is a :class:`~kivy.properties.ColorProperty` and
    defaults to `None`.
    """

    background_color_cell = ColorProperty(None)
    """
    Background color for :class:`~CellRow` class.

    .. versionadded:: 1.0.0

    .. code-block:: python

        self.data_tables = MDDataTable(
            ...,
            background_color_header=get_color_from_hex("#65275d"),
            background_color_cell=get_color_from_hex("#451938"),
        )
        
    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-background-color-cell.png
        :align: center

    :attr:`background_color_cell` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    background_color_selected_cell = ColorProperty(None)
    """
    Background selected color for :class:`~CellRow` class.

    .. versionadded:: 1.0.0

    .. code-block:: python

        self.data_tables = MDDataTable(
            ...,
            background_color_header=get_color_from_hex("#65275d"),
            background_color_cell=get_color_from_hex("#451938"),
            background_color_selected_cell=get_color_from_hex("e4514f"),
        )
        
    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/data-tables-background-color-selected-cell.gif
        :align: center

    :attr:`background_color_selected_cell` is a :class:`~kivy.properties.ColorProperty` and
    defaults to `None`.
    """

    effect_cls = ObjectProperty(StiffScrollEffect)
    """
    Effect class. See ``kivy/effects`` package for more information.

    .. versionadded:: 1.0.0

    :attr:`effect_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to :class:`~kivymd.effects.stiffscroll.StiffScrollEffect`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header = TableHeader(
            column_data=self.column_data,
            sorted_on=self.sorted_on,
            sorted_order=self.sorted_order,
            background_color_header=self.background_color_header,
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

    def update_row_data(self, instance_data_table, data: list) -> NoReturn:
        """
        Called when a the widget data must be updated.

        Remember that this is a heavy function. since the whole data set must
        be updated. you can get better results calling this metod with in a
        coroutine.
        """

        self.table_data.row_data = data
        self.table_data.on_rows_num(self, self.table_data.rows_num)
        # Set cursors to 0.
        self.table_data._rows_number = 0
        self.table_data._current_value = 1

        if len(data) < self.table_data.rows_num:
            self.table_data._to_value = len(data)
            self.table_data.pagination.ids.button_forward.disabled = True
        else:
            self.table_data._to_value = self.table_data.rows_num
            self.table_data.pagination.ids.button_forward.disabled = False

        self.table_data.set_next_row_data_parts("")
        self.pagination.ids.button_back.disabled = True
        Clock.schedule_once(self.create_pagination_menu, 0.5)

    def add_row(self, data: Union[list, tuple]) -> NoReturn:
        """
        Added new row to common table.
        Argument `data` is the row data from the list :attr:`row_data`.

        .. versionadded:: 1.0.0
        """

        self.row_data.append(data)

    def remove_row(self, data: Union[list, tuple]) -> NoReturn:
        """
        Removed row from common table.
        Argument `data` is the row data from the list :attr:`row_data`.

        .. versionadded:: 1.0.0
        """

        self.row_data.remove(data)

    def on_row_press(self, instance_cell_row) -> NoReturn:
        """Called when a table row is clicked."""

    def on_check_press(self, row_data: list) -> NoReturn:
        """
        Called when the check box in the table row is checked.

        :param row_data: One of the elements from the :attr:`MDDataTable.row_data` list.
        """

    def get_row_checks(self) -> list:
        """Returns all rows that are checked."""

        return self.table_data._get_row_checks()

    def create_pagination_menu(self, interval: Union[int, float]) -> NoReturn:
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


class CellRow(
    ThemableBehavior,
    RecycleDataViewBehavior,
    HoverBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    """Implements a data row from :attr:`~MDDataTable.column_data`."""

    background_color_cell = ColorProperty(None)
    """
    See :attr:`~MDDataTable.background_color_cell.`.

    .. versionadded:: 1.0.0

    :attr:`background_color_cell` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    background_color_selected_cell = ColorProperty(None)
    """
    See :attr:`~MDDataTable.background_color_selected_cell.`.

    .. versionadded:: 1.0.0

    :attr:`background_color_selected_cell` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text = StringProperty()
    """
    Row text.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    table = ObjectProperty()
    """
    Class class:`~TableData`.

    :attr:`table` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty()
    """
    Row icon name.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_color = ColorProperty(None)
    """
    Row icon color.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    index = None
    icon_copy = icon

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.check.bind(active=self.select_check)
        self.ids.check.bind(active=self.notify_checkbox_click)

    def notify_checkbox_click(
        self, instance_check: MDCheckbox, active: bool
    ) -> NoReturn:
        """Called when the table row checkbox is activated/deactivated."""

        self.table.get_select_row(self.index)

    def refresh_view_attrs(
        self, instance_table_data: TableData, index: int, data: dict
    ):
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
        return super().refresh_view_attrs(instance_table_data, index, data)

    def apply_selection(
        self, instance_table_data: TableData, index: int, is_selected: bool
    ) -> NoReturn:
        """Called when list items of table appear on the screen."""

        self.selected = is_selected

        # Fixes cloning of icons.
        ic = instance_table_data.recycle_data[index].get("icon", None)
        cell_row_obj = instance_table_data.view_adapter.get_visible_view(index)

        if not ic:
            cell_row_obj.icon = ""
        else:
            cell_row_obj.icon = cell_row_obj.icon_copy

        # Set checkboxes.
        if instance_table_data.check:
            if self.index in instance_table_data.data_first_cells:
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
        if (
            instance_table_data._rows_number
            in instance_table_data.current_selection_check
        ):
            for index in instance_table_data.current_selection_check[
                instance_table_data._rows_number
            ]:
                if (
                    self.index
                    in instance_table_data.current_selection_check[
                        instance_table_data._rows_number
                    ]
                ):
                    self.change_check_state_no_notify("down")
                else:
                    self.change_check_state_no_notify("normal")
        else:
            self.change_check_state_no_notify("normal")

    def change_check_state_no_notify(self, new_state: str) -> NoReturn:
        checkbox = self.ids.check
        checkbox.unbind(active=self.notify_checkbox_click)
        checkbox.state = new_state
        checkbox.bind(active=self.notify_checkbox_click)

    def select_check(
        self, instance_table_data: MDDataTable, active: bool
    ) -> NoReturn:
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

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            if self.table._parent:
                self.table._parent.dispatch("on_row_press", self)
            return True

    def on_icon(self, instance_cell_row, name_icon: str) -> NoReturn:
        self.icon_copy = name_icon

    def on_table(
        self, instance_cell_row, instance_table_data: TableData
    ) -> NoReturn:
        """Sets padding/spacing to zero if no checkboxes are used for rows."""

        if not instance_table_data.check:
            self.ids.box.padding = 0
            self.ids.box.spacing = 0

    def _check_all(self, state):
        """Checks if all checkboxes are in same state."""

        if state == "down" and self.table.check_all(state):
            self.table.table_header.ids.check.state = "down"
        else:
            self.table.table_header.ids.check.state = "normal"


class SortButton(MDIconButton):
    """Implements a sort button in the :class:`~CellHeader` class."""
