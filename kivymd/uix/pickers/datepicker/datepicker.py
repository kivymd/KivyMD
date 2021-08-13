"""
Components/DatePicker
=====================

.. seealso::

    `Material Design spec, Date picker <https://material.io/components/date-pickers>`_

.. rubric:: Includes date picker.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/picker-previous.png
    :align: center

.. warning:: The widget is under testing. Therefore, we would be grateful if
    you would let us know about the bugs found.

.. rubric:: Usage

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.pickers import MDDatePicker

    KV = '''
    MDFloatLayout:

        MDToolbar:
            title: "MDDatePicker"
            pos_hint: {"top": 1}
            elevation: 10

        MDRaisedButton:
            text: "Open time picker"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_date_picker()
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_save(self, instance, value, date_range):
            '''
            Events called when the "OK" dialog box button is clicked.

            :type instance: <kivymd.uix.picker.MDDatePicker object>;

            :param value: selected date;
            :type value: <class 'datetime.date'>;

            :param date_range: list of 'datetime.date' objects in the selected range;
            :type date_range: <class 'list'>;
            '''

            print(instance, value, date_range)

        def on_cancel(self, instance, value):
            '''Events called when the "CANCEL" dialog box button is clicked.'''

        def show_date_picker(self):
            date_dialog = MDDatePicker()
            date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
            date_dialog.open()


    Test().run()


.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDDatePicker.gif
    :align: center

Open date dialog with the specified date
----------------------------------------

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1983, month=4, day=12)
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/previous-date.png
    :align: center

You can set the time interval from and to the set date. All days of the week
that are not included in this range will have the status `disabled`.

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_date=datetime.date(2021, 2, 15),
            max_date=datetime.date(2021, 3, 27),
        )
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/range-date.gif
    :align: center

The range of available dates can be changed in the picker dialog:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/change-range-date.gif
    :align: center

Select year
-----------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/select-year-date.gif
    :align: center

.. warning:: The list of years when opening is not automatically set
    to the current year.

You can set the range of years using the :attr:`~kivymd.uix.picker.MDDatePicker.min_year` and
:attr:`~kivymd.uix.picker.MDDatePicker.max_year` attributes:

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=2021, max_year=2030)
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/min-max-year-date.png
    :align: center

Set and select a date range
---------------------------

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/set-select-range-date.gif
    :align: center
"""

__all__ = ("MDDatePicker", "BaseDialogPicker")

import calendar
import datetime
import os
from datetime import date
from typing import NoReturn, Union

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd import uix_path
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.toast import toast
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tooltip import MDTooltip

with open(
    os.path.join(uix_path, "pickers", "datepicker", "datepicker.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseDialogPicker(
    BaseDialog,
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
):
    """
    Base class for :attr:`~kivymd.uix.picker.MDDatePicker` and
    :attr:`~kivymd.uix.picker.MDTimePicker` classes.

    :Events:
        `on_save`
            Events called when the "OK" dialog box button is clicked.
        `on_cancel`
            Events called when the "CANCEL" dialog box button is clicked.
    """

    title_input = StringProperty("INPUT DATE")
    """
    Dialog title fot input date.

    :attr:`title_input` is an :class:`~kivy.properties.StringProperty`
    and defaults to `INPUT DATE`.
    """

    title = StringProperty("SELECT DATE")
    """
    Dialog title fot select date.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `SELECT DATE`.
    """

    radius = ListProperty([7, 7, 7, 7])
    """
    Radius list for the four corners of the dialog.

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    primary_color = ColorProperty(None)
    """
    Background color of toolbar.

    .. code-block:: python

        MDDatePicker(primary_color=get_color_from_hex("#72225b")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-color-date.png
        :align: center

    :attr:`primary_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    accent_color = ColorProperty(None)
    """
    Background color of calendar/clock face.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/accent-color-date.png
        :align: center

    :attr:`accent_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selector_color = ColorProperty(None)
    """
    Background color of the selected day of the month or hour.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selector-color-date.png
        :align: center

    :attr:`selector_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_toolbar_color = ColorProperty(None)
    """
    Color of labels for text on a toolbar.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-toolbar-color-date.png
        :align: center

    :attr:`text_toolbar_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Color of text labels in calendar/clock face.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-color-date.png
        :align: center

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_current_color = ColorProperty(None)
    """
    Color of the text of the current day of the month/hour.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
            text_current_color=get_color_from_hex("#e93f39"),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-current-color-date.png
        :align: center

    :attr:`text_current_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_button_color = ColorProperty(None)
    """
    Text button color.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
            text_current_color=get_color_from_hex("#e93f39"),
            text_button_color=(1, 1, 1, .5),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-button-color-date.png
        :align: center

    :attr:`text_button_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_background_color = ColorProperty(None)
    """
    Background color of input fields.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
            text_current_color=get_color_from_hex("#e93f39"),
            input_field_background_color=(1, 1, 1, 0.2),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-background-color-date.png
        :align: center

    :attr:`input_field_background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_text_color = ColorProperty(None)
    """
    Text color of input fields.

    Background color of input fields.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
            text_current_color=get_color_from_hex("#e93f39"),
            input_field_background_color=(1, 1, 1, 0.2),
            input_field_text_color=(1, 1, 1, 1),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-background-color-date.png
        :align: center

    :attr:`input_field_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty("Roboto")
    """
    Font name for dialog window text.

    .. code-block:: python

        MDDatePicker(
            primary_color=get_color_from_hex("#72225b"),
            accent_color=get_color_from_hex("#5d1a4a"),
            selector_color=get_color_from_hex("#e93f39"),
            text_toolbar_color=get_color_from_hex("#cccccc"),
            text_color=("#ffffff"),
            text_current_color=get_color_from_hex("#e93f39"),
            input_field_background_color=(1, 1, 1, 0.2),
            input_field_text_color=(1, 1, 1, 1),
            font_name="Weather.ttf",

        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-name-date.png
        :align: center

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_save")
        self.register_event_type("on_cancel")

    def on_save(self, *args) -> NoReturn:
        """Events called when the "OK" dialog box button is clicked."""

        self.dismiss()

    def on_cancel(self, *args) -> NoReturn:
        """Events called when the "CANCEL" dialog box button is clicked."""

        self.dismiss()


class DatePickerBaseTooltip(MDTooltip):
    """Implements tooltips for members of the :class:`~MDDatePicker` class."""

    owner = ObjectProperty()
    hint_text = StringProperty()


class DatePickerIconTooltipButton(MDIconButton, DatePickerBaseTooltip):
    pass


class DatePickerWeekdayLabel(MDLabel, DatePickerBaseTooltip):
    pass


class DatePickerTypeDateError(Exception):
    pass


class DatePickerEnterDataField(MDTextField):
    """Implements date input in 01/01/2021 format."""

    owner = ObjectProperty()

    _backspace = False
    _date = ""

    def isnumeric(self, value: Union[int, str]) -> bool:
        """
        We are forced to create a custom method because if we set the ``int``
        value for the ``input_filter`` parameter of the text field, then the
        ``-`` character is still available for keyboard input. Apparently, this
        is a Kivy bug.
        """

        try:
            int(value)
            return True
        except ValueError:
            return False

    def do_backspace(self, *args) -> NoReturn:
        """Prevent deleting text from the middle of a line of a text field."""

        self._backspace = True
        self.text = self.text[:-1]
        self._date = self.text
        self._backspace = False

    def input_filter(self, char: str, boolean: bool) -> Union[None, str]:
        """Date validity check in dd/mm/yyyy format."""

        cursor = self.cursor[0]
        if len(self.text) == 10:
            return
        if self.isnumeric(char):
            self._date += char
            value = int(char)
            # checking a valid value for the number of days in a month
            if cursor == 0:  # first value
                if self.owner.sel_month == 2:
                    valid_value = 2
                else:
                    valid_value = 3
                if value > valid_value:
                    self._date = self._date[:-1]
                    return
            # check there is a day number in the month
            if cursor == 1:
                days_of_month = []
                for _date in self.owner.calendar.itermonthdates(
                    self.owner.sel_year, self.owner.sel_month
                ):
                    if _date.month == self.owner.sel_month:
                        days_of_month.append(_date.day)
                if not int(self._date[:2]) in days_of_month:
                    self._date = self._date[:-1]
                    return
            # checking the allowed value of the number of months
            elif self.cursor[0] == 2:
                if int(value) > 1:
                    self._date = self._date[:-1]
                    return
            elif self.cursor[0] == 4:
                if int(self._date[-2:]) not in list(range(1, 13)):
                    self._date = self._date[:-1]
                    return
            # checking the valid year value
            elif self.cursor[0] == 6:
                if not int(value):
                    self._date = self._date[:-1]
                    return
            return str(value)

    def on_text(self, instance_field: MDTextField, text: str) -> NoReturn:
        if text != "" and not text.isspace() and not self._backspace:
            if len(text) <= 1 and instance_field.focus:
                instance_field.text = text
                self._set_pos_cursor()
            elif len(text) == 3:
                start = instance_field.text[:-1]
                end = instance_field.text[-1]
                instance_field.text = f"{start}/{end}"
                self._set_pos_cursor()
            elif len(text) == 5:
                instance_field.text += "/"
                self._set_pos_cursor()
            if not self.owner.min_date and not self.owner.max_date:
                self.owner.update_text_full_date(self._get_list_date())

    def _get_list_date(self):
        """
        Returns a list as `[dd, mm, yyyy]` from a text fied for entering a date.
        """

        return [d for d in self.text.split("/") if d]

    def _set_pos_cursor(self):
        def set_pos_cursor(pos_corsor, interval=0.5):
            self.cursor = (pos_corsor, 0)

        if self.focus:
            Clock.schedule_once(lambda x: set_pos_cursor(len(self.text)), 0.1)


class DatePickerDatePickerEnterDataFieldContainer(MDBoxLayout):
    owner = ObjectProperty()


class SelectYearList(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    """A class that implements a list for choosing a year."""


class DatePickerDaySelectableItem(
    ThemableBehavior, CircularRippleBehavior, ButtonBehavior, AnchorLayout
):
    """A class that implements a list for choosing a day."""

    text = StringProperty()
    owner = ObjectProperty()
    is_today = BooleanProperty(False)
    is_selected = BooleanProperty(False)
    current_month = NumericProperty()
    current_year = NumericProperty()
    index = NumericProperty(0)

    def check_date(self, year: int, month: int, day: int):
        try:
            return date(year, month, day) in self.owner._date_range
        except ValueError as error:
            if str(error) == "day is out of range for month":
                return False

    def on_release(self):
        if (
            self.owner.mode == "range"
            and self.owner._end_range_date
            and self.owner._start_range_date
        ):
            return
        if (
            not self.owner._input_date_dialog_open
            and not self.owner._select_year_dialog_open
        ):
            if self.owner.mode == "range" and not self.owner._start_range_date:
                self.owner._start_range_date = date(
                    self.current_year, self.current_month, int(self.text)
                )
                self.owner.min_date = self.owner._start_range_date
            elif (
                self.owner.mode == "range"
                and not self.owner._end_range_date
                and self.owner._start_range_date
            ):
                self.owner._end_range_date = date(
                    self.current_year, self.current_month, int(self.text)
                )
                if self.owner._end_range_date <= self.owner.min_date:
                    toast(self.owner.date_range_text_error)
                    Logger.error(
                        "`Data Picker: max_date` value cannot be less than "
                        "or equal to 'min_date' value."
                    )
                    self.owner._start_range_date = 0
                    self.owner._end_range_date = 0
                    return
                self.owner.max_date = self.owner._end_range_date
                self.owner.update_calendar_for_date_range()

            self.owner.set_selected_widget(self)


class DatePickerYearSelectableItem(RecycleDataViewBehavior, MDLabel):
    """Implements an item for a pick list of the year."""

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    selected_color = ColorProperty([0, 0, 0, 0])
    owner = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            self.owner.year = int(self.text)
            # self.owner.sel_year = self.owner.year
            self.owner.ids.label_full_date.text = self.owner.set_text_full_date(
                self.owner.sel_year,
                self.owner.sel_month,
                self.owner.sel_day,
                self.owner.theme_cls.device_orientation,
            )
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, table_data, index, is_selected):
        self.selected = is_selected
        if is_selected:
            self.selected_color = (
                self.owner.selector_color
                if self.owner.selector_color
                else self.theme_cls.primary_color
            )
            self.text_color = (1, 1, 1, 1)
        else:
            if int(self.text) == self.owner.sel_year:
                self.text_color = (
                    self.theme_cls.primary_color
                    if not self.owner.text_current_color
                    else self.owner.text_current_color
                )
            self.selected_color = [0, 0, 0, 0]
            self.text_color = (0, 0, 0, 1)


# TODO: Add the feature to embed the `MDDatePicker` class in other layouts
#  and not use it as a modal dialog.
class MDDatePicker(BaseDialogPicker):
    text_weekday_color = ColorProperty(None)
    """
    Text color of weekday names.

    :attr:`text_weekday_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    day = NumericProperty()
    """
    The day of the month to be opened by default. If not specified,
    the current number will be used.

    :attr:`day` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    month = NumericProperty()
    """
    The number of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`month` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    year = NumericProperty()
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    min_year = NumericProperty(1914)
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`min_year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1914`.
    """

    max_year = NumericProperty(2121)
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`max_year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2121`.
    """

    mode = OptionProperty("picker", options=["picker", "range"])
    """
    Dialog type:`'picker'` type allows you to select one date;
                 `'range'` type allows to set a range of dates from which the
                 user can select a date.
    Available options are: [`'picker'`, `'range'`].

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `picker`.
    """

    min_date = ObjectProperty()
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.

    :attr:`min_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    max_date = ObjectProperty()
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.

    :attr:`max_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    date_range_text_error = StringProperty("Error date range")
    """
    Error text that will be shown on the screen in the form of a toast if the
    minimum date range exceeds the maximum.

    :attr:`date_range_text_error` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Error date range'`.
    """

    sel_year = NumericProperty()
    sel_month = NumericProperty()
    sel_day = NumericProperty()

    _calendar_layout = ObjectProperty()
    _calendar_list = None
    _enter_data_field = None
    _enter_data_field_two = None
    _enter_data_field_container = None
    _date_range = []
    _sel_day_widget = ObjectProperty()
    _scale_calendar_layout = NumericProperty(1)
    _scale_year_layout = NumericProperty(0)
    _shift_dialog_height = NumericProperty(0)
    _input_date_dialog_open = BooleanProperty(False)
    _select_year_dialog_open = False
    _start_range_date = 0
    _end_range_date = 0

    def __init__(
        self,
        year=None,
        month=None,
        day=None,
        firstweekday=0,
        **kwargs,
    ):
        self.today = date.today()
        self.calendar = calendar.Calendar(firstweekday)
        self.sel_year = year if year else self.today.year
        self.sel_month = month if month else self.today.month
        self.sel_day = day if day else self.today.day
        self.month = self.sel_month
        self.year = self.sel_year
        self.day = self.sel_day
        self._current_selected_date = (
            self.sel_day,
            self.sel_month,
            self.sel_year,
        )
        super().__init__(**kwargs)
        self.theme_cls.bind(device_orientation=self.on_device_orientation)

        if self.max_date and self.min_date:
            if self.min_date and not isinstance(self.min_date, date):
                raise DatePickerTypeDateError(
                    "'min_date' must be of class <class 'datetime.date'>"
                )
            if self.max_date and not isinstance(self.max_date, date):
                raise DatePickerTypeDateError(
                    "'max_date' must be of class <class 'datetime.date'>"
                )
            self.compare_date_range()
            self._date_range = self.get_date_range()

        self.generate_list_widgets_days()
        self.update_calendar(self.sel_year, self.sel_month)

        if (
            not self.max_date
            and not self.min_date
            and not self._date_range
            and self.mode != "range"
        ):
            # Mark the current day.
            self.set_month_day(self.sel_day)
            self._sel_day_widget.dispatch("on_release")

    def on_device_orientation(
        self, instance_theme_manager: ThemeManager, orientation_value: str
    ) -> NoReturn:
        if self._input_date_dialog_open:
            if orientation_value == "portrait":
                self._shift_dialog_height = dp(250)
            if orientation_value == "landscape":
                self._shift_dialog_height = dp(138)

    def transformation_from_dialog_select_year(self) -> NoReturn:
        self.ids.chevron_left.disabled = False
        self.ids.chevron_right.disabled = False
        self.ids._year_layout.disabled = True
        self.ids.triangle.disabled = False
        self._select_year_dialog_open = False
        self.ids.triangle.icon = "menu-down"

        Animation(opacity=1, d=0.15).start(self.ids.chevron_left)
        Animation(opacity=1, d=0.15).start(self.ids.chevron_right)
        Animation(_scale_year_layout=0, d=0.15).start(self)
        Animation(
            _shift_dialog_height=dp(0), _scale_calendar_layout=1, d=0.15
        ).start(self)

        self._calendar_layout.clear_widgets()
        self.generate_list_widgets_days()
        self.update_calendar(self.year, self.month)

        if self.mode != "range":
            self.set_month_day(self.day)
            self._sel_day_widget.dispatch("on_release")

    def transformation_to_dialog_select_year(self) -> NoReturn:
        def disabled_chevron_buttons(*args):
            self.ids.chevron_left.disabled = True
            self.ids.chevron_right.disabled = True

        self._select_year_dialog_open = True
        self.ids._year_layout.disabled = False
        self._scale_calendar_layout = 0
        Animation(opacity=0, d=0.15).start(self.ids.chevron_left)
        Animation(opacity=0, d=0.15).start(self.ids.chevron_right)
        anim = Animation(_scale_year_layout=1, d=0.15)
        anim.bind(on_complete=disabled_chevron_buttons)
        anim.start(self)
        self.ids.triangle.icon = "menu-up"
        self.generate_list_widgets_years()
        self.set_position_to_current_year()

    def transformation_to_dialog_input_date(self) -> NoReturn:
        def set_date_to_input_field():
            if not self._enter_data_field_two:
                # Date of current day.
                self._enter_data_field.text = (
                    f"{'' if self.sel_day >= 10 else '0'}"
                    f"{self.sel_day}/"
                    f"{'' if self.sel_month >= 10 else '0'}"
                    f"{self.sel_month}/{self.sel_year}"
                )
            else:
                # Range start date.
                self._enter_data_field.text = (
                    f"{'' if self.min_date.day >= 10 else '0'}"
                    f"{self.min_date.day}/"
                    f"{'' if self.min_date.month >= 10 else '0'}"
                    f"{self.min_date.month}/{self.min_date.year}"
                )

        def set_date_to_input_field_two():
            # Range end date.
            self._enter_data_field_two.text = (
                f"{'' if self.max_date.day >= 10 else '0'}"
                f"{self.max_date.day}/"
                f"{'' if self.max_date.month >= 10 else '0'}"
                f"{self.max_date.month}/{self.max_date.year}"
            )

        self.ids.triangle.disabled = True
        if self._select_year_dialog_open:
            self.transformation_from_dialog_select_year()
        self._input_date_dialog_open = True

        self._enter_data_field_container = (
            DatePickerDatePickerEnterDataFieldContainer(owner=self)
        )
        self._enter_data_field = self.get_field()
        if self.min_date and self.max_date:
            self._enter_data_field_two = self.get_field()
            set_date_to_input_field_two()
        set_date_to_input_field()
        self._enter_data_field_container.add_widget(self._enter_data_field)
        if self._enter_data_field_two:
            self._enter_data_field_container.add_widget(
                self._enter_data_field_two
            )

        self.ids.container.add_widget(self._enter_data_field_container)
        self.ids.edit_icon.icon = "calendar"
        self.ids.label_title.text = self.title_input

        Animation(
            _shift_dialog_height=dp(250)
            if self.theme_cls.device_orientation == "portrait"
            else dp(138),
            _scale_calendar_layout=0,
            d=0.15,
        ).start(self)
        Animation(
            opacity=0,
            d=0.15 if self.theme_cls.device_orientation == "portrait" else 0,
        ).start(self.ids.chevron_left)
        Animation(
            opacity=0,
            d=0.15 if self.theme_cls.device_orientation == "portrait" else 0,
        ).start(self.ids.chevron_right)
        Animation(opacity=0, d=0.15).start(self.ids.label_month_selector)
        Animation(opacity=0, d=0.15).start(self.ids.triangle)
        Animation(opacity=1, d=0.15).start(self._enter_data_field)
        if self._enter_data_field_two:
            Animation(opacity=1, d=0.15).start(self._enter_data_field_two)
        self.ids.label_full_date.text = self.set_text_full_date(
            self.sel_year,
            self.sel_month,
            self.sel_day,
            self.theme_cls.device_orientation,
        )

    def transformation_from_dialog_input_date(
        self, interval: Union[int, float]
    ) -> NoReturn:
        self._input_date_dialog_open = False
        self.ids.label_full_date.text = self.set_text_full_date(
            self.sel_year,
            self.sel_month,
            self.sel_day,
            self.theme_cls.device_orientation,
        )
        self.ids.triangle.disabled = False
        self.ids.container.remove_widget(self._enter_data_field_container)
        Animation(
            _shift_dialog_height=dp(0), _scale_calendar_layout=1, d=0.15
        ).start(self)
        Animation(
            opacity=1,
            d=0.15 if self.theme_cls.device_orientation == "portrait" else 0.65,
        ).start(self.ids.chevron_left)
        Animation(
            opacity=1,
            d=0.15 if self.theme_cls.device_orientation == "portrait" else 0.65,
        ).start(self.ids.chevron_right)
        Animation(opacity=1, d=0.15).start(self.ids.label_month_selector)
        Animation(opacity=1, d=0.15).start(self.ids.triangle)
        Animation(opacity=0, d=0.15).start(self._enter_data_field)
        self.ids.edit_icon.icon = "pencil"
        self.ids.label_title.text = self.title

        if not self.min_date and not self.max_date:
            list_date = self._enter_data_field._get_list_date()
            if len(list_date) == 3 and len(list_date[2]) == 4:
                # self._sel_day_widget.is_selected = False
                self.update_calendar(int(list_date[2]), int(list_date[1]))
                self.set_month_day(int(list_date[0]))
                # self._sel_day_widget.dispatch("on_release")
                if self.mode != "range":
                    self._sel_day_widget.is_selected = False
                    self._sel_day_widget.dispatch("on_release")
        elif self.min_date and self.max_date:
            list_min_date = self._enter_data_field._get_list_date()
            list_max_date = self._enter_data_field_two._get_list_date()

            if len(list_min_date) == 3 and len(list_min_date[2]) == 4:
                self.min_date = date(
                    int(list_min_date[2]),
                    int(list_min_date[1]),
                    int(list_min_date[0]),
                )
            if len(list_max_date) == 3 and len(list_max_date[2]) == 4:
                self.max_date = date(
                    int(list_max_date[2]),
                    int(list_max_date[1]),
                    int(list_max_date[0]),
                )

            self.update_calendar_for_date_range()
            self.ids.label_full_date.text = self.set_text_full_date(
                int(list_max_date[2]),
                int(list_max_date[1]),
                int(list_max_date[0]),
                self.theme_cls.device_orientation,
            )

    def compare_date_range(self) -> NoReturn:
        # TODO: Add behavior if the minimum date range exceeds the maximum
        #  date range. Use toast?
        if self.max_date <= self.min_date:
            raise DatePickerTypeDateError(
                "`max_date` value cannot be less than or equal "
                "to 'min_date' value"
            )

    def update_calendar_for_date_range(self) -> NoReturn:
        # self.compare_date_range()
        self._date_range = self.get_date_range()
        self._calendar_layout.clear_widgets()
        self.generate_list_widgets_days()
        self.update_calendar(self.year, self.month)

    def update_text_full_date(self, list_date):
        """
        Updates the title of the week, month and number day name
        in an open date input dialog.
        """

        if len(list_date) == 1 and len(list_date[0]) == 2:
            self.ids.label_full_date.text = self.set_text_full_date(
                self.sel_year,
                self.sel_month,
                list_date[0],
                self.theme_cls.device_orientation,
            )
        if len(list_date) == 2 and len(list_date[1]) == 2:
            self.ids.label_full_date.text = self.set_text_full_date(
                self.sel_year,
                int(list_date[1]),
                int(list_date[0]),
                self.theme_cls.device_orientation,
            )
        if len(list_date) == 3 and len(list_date[2]) == 4:
            self.ids.label_full_date.text = self.set_text_full_date(
                int(list_date[2]),
                int(list_date[1]),
                int(list_date[0]),
                self.theme_cls.device_orientation,
            )

    def update_calendar(self, year, month):
        try:
            dates = [x for x in self.calendar.itermonthdates(year, month)]
        except ValueError as e:
            if str(e) == "year is out of range":
                pass
        else:
            self.year = year
            self.month = month
            for idx in range(len(self._calendar_list)):
                self._calendar_list[idx].current_month = int(self.month)
                self._calendar_list[idx].current_year = int(self.year)

                # Dates of the month not in the range 1-31.
                if idx >= len(dates) or dates[idx].month != month:
                    # self._calendar_list[idx].disabled = True
                    self._calendar_list[idx].text = ""
                # Dates of the month in the range 1-31.
                else:
                    self._calendar_list[idx].disabled = False
                    self._calendar_list[idx].text = str(dates[idx].day)
                    self._calendar_list[idx].is_today = dates[idx] == self.today
                # The marked date widget has a True value in the `is_selected`
                # attribute. In the KV file it is checked if the date widget
                # (DatePickerDaySelectableItem) has the `is_selected = False`
                # attribute value, then the date widget is not highlighted.
                if (
                    0
                    if not self._calendar_list[idx].text
                    else int(self._calendar_list[idx].text),
                    self._calendar_list[idx].current_month,
                    self._calendar_list[idx].current_year,
                ) == self._current_selected_date:
                    self._calendar_list[idx].is_selected = True
                else:
                    self._calendar_list[idx].is_selected = False
                # Dates outside the set range - disabled.
                if (
                    self.mode == "picker"
                    and self._date_range
                    and self._calendar_list[idx].text
                ) or (
                    self.mode == "range"
                    and self._start_range_date
                    and self._end_range_date
                    and self._calendar_list[idx].text
                ):
                    if (
                        date(
                            self._calendar_list[idx].current_year,
                            self._calendar_list[idx].current_month,
                            int(self._calendar_list[idx].text),
                        )
                        not in self._date_range
                    ):
                        self._calendar_list[idx].disabled = True

    def get_field(self):
        """Creates and returns a text field object used to enter dates."""

        field = DatePickerEnterDataField(
            owner=self, line_color_normal=self.theme_cls.divider_color
        )
        field.color_mode = "custom"
        field.line_color_focus = (
            self.theme_cls.primary_color
            if not self.input_field_text_color
            else self.input_field_text_color
        )
        field.current_hint_text_color = field.line_color_focus
        field._current_hint_text_color = field.line_color_focus
        return field

    def get_date_range(self):
        date_range = [
            self.min_date + datetime.timedelta(days=x)
            for x in range((self.max_date - self.min_date).days + 1)
        ]
        return date_range

    def set_text_full_date(self, year, month, day, orientation):
        """
        Returns a string of type "Tue, Feb 2" or "Tue,\nFeb 2" for a date
        choose and a string like "Feb 15 - Mar 23" or "Feb 15,\nMar 23" for
        a date range.
        """
        if 12 < int(month) < 0:
            raise ValueError(
                "set_text_full_date:\n\t" f"Month [{month}] out of range."
            )
        if int(day) > calendar.monthrange(int(year), (month))[1]:
            raise ValueError(
                "set_text_full_date:\n\t"
                f"Day [{day}] out of range for the month {month}"
            )
        date = datetime.date(int(year), int(month), int(day))
        separator = (
            "\n"
            if (orientation == "landscape" and not self._input_date_dialog_open)
            else " "
        )

        if self.mode == "picker":
            if not self.min_date and not self.max_date:
                return (
                    date.strftime("%a,").capitalize()
                    + separator
                    + date.strftime("%b ").capitalize()
                    + str(day).lstrip("0")
                )
            else:
                return (
                    self.min_date.strftime("%b ").capitalize()
                    + str(self.min_date.day).lstrip("0")
                    + (
                        " - "
                        if orientation == "portrait"
                        else (
                            ",\n" if not self._input_date_dialog_open else ", "
                        )
                    )
                    + self.max_date.strftime("%b ").capitalize()
                    + str(self.max_date.day).lstrip("0")
                )
        elif self.mode == "range":
            if self._start_range_date and self._end_range_date:
                if (
                    orientation == "landscape"
                    and "-" in self.ids.label_full_date.text
                ):
                    return (
                        self.ids.label_full_date.text.split("-")[0].strip()
                        + (",\n" if not self._input_date_dialog_open else " - ")
                        + date.strftime("%b ").capitalize()
                        + str(day).lstrip("0")
                    )
                else:
                    if (
                        orientation == "landscape"
                        and "," in self.ids.label_full_date.text
                    ):
                        return (
                            self.ids.label_full_date.text.split(",")[0].strip()
                            + (
                                ",\n"
                                if not self._input_date_dialog_open
                                else "-"
                            )
                            + date.strftime("%b ").capitalize()
                            + str(day).lstrip("0")
                        )
                    if (
                        orientation == "portrait"
                        and "," in self.ids.label_full_date.text
                    ):
                        return (
                            self.ids.label_full_date.text.split(",")[0].strip()
                            + "-"
                            + date.strftime("%b ").capitalize()
                            + str(day).lstrip("0")
                        )
                    if (
                        orientation == "portrait"
                        and "-" in self.ids.label_full_date.text
                    ):
                        return (
                            self.ids.label_full_date.text.split("-")[0].strip()
                            + " - "
                            + date.strftime("%b ").capitalize()
                            + str(day).lstrip("0")
                        )
            elif self._start_range_date and not self._end_range_date:
                return (
                    (
                        date.strftime("%b ").capitalize()
                        + str(day).lstrip("0")
                        + " - End"
                    )
                    if orientation != "landscape"
                    else (
                        date.strftime("%b ").capitalize()
                        + str(day).lstrip("0")
                        + "{}End".format(
                            ",\n" if not self._input_date_dialog_open else " - "
                        )
                    )
                )
            elif not self._start_range_date and not self._end_range_date:
                return (
                    "Start - End"
                    if orientation != "landscape"
                    else "Start{}End".format(
                        ",\n" if not self._input_date_dialog_open else " - "
                    )
                )

    def set_selected_widget(self, widget):
        if self._sel_day_widget:
            self._sel_day_widget.is_selected = False

        widget.is_selected = True
        self.sel_month = int(self.month)
        self.sel_year = int(self.year)
        self.sel_day = int(widget.text)
        self._current_selected_date = (
            self.sel_day,
            self.sel_month,
            self.sel_year,
        )
        self._sel_day_widget = widget

    def set_month_day(self, day):
        for idx in range(len(self._calendar_list)):
            if str(day) == str(self._calendar_list[idx].text):
                self._sel_day_widget = self._calendar_list[idx]
                self.sel_day = int(self._calendar_list[idx].text)
                if self._sel_day_widget:
                    self._sel_day_widget.is_selected = False
                self._sel_day_widget = self._calendar_list[idx]

    def set_position_to_current_year(self):
        # TODO: Add the feature to set the position of the list of years
        #  for the current year. This is not currently possible because the
        #  ``RecycleView`` class does not support this functionality.
        #  There is a solution to this problem
        #  - https://github.com/Bakterija/log_fruit/blob/dev/src/app_modules/widgets/app_recycleview/recycleview.py.
        #  But I have not been able to get it to work.
        pass

    def generate_list_widgets_years(self):
        for i, number_year in enumerate(range(self.min_year, self.max_year)):
            self.ids._year_layout.data.append(
                {
                    "owner": self,
                    "text": str(number_year),
                    "index": i,
                    "selectable": True,
                    "viewclass": "DatePickerYearSelectableItem",
                }
            )

    def generate_list_widgets_days(self):
        calendar_list = []

        for day in self.calendar.iterweekdays():
            weekday_label = DatePickerWeekdayLabel(
                text=calendar.day_name[day][0].upper(),
                owner=self,
                hint_text=calendar.day_name[day],
            )
            weekday_label.font_name = self.font_name
            self._calendar_layout.add_widget(weekday_label)
        for i, j in enumerate(range(6 * 7)):  # 6 weeks, 7 days a week
            day_selectable_item = DatePickerDaySelectableItem(
                index=i,
                owner=self,
                current_month=int(self.month),
                current_year=int(self.year),
            )
            calendar_list.append(day_selectable_item)
            self._calendar_layout.add_widget(day_selectable_item)
        self._calendar_list = calendar_list

    def change_month(self, operation):
        """
        Called when "chevron-left" and "chevron-right" buttons are pressed.
        Switches the calendar to the previous/next month.
        """

        operation = 1 if operation == "next" else -1
        month = (
            12
            if self.month + operation == 0
            else 1
            if self.month + operation == 13
            else self.month + operation
        )
        year = (
            self.year - 1
            if self.month + operation == 0
            else self.year + 1
            if self.month + operation == 13
            else self.year
        )
        self.update_calendar(year, month)
        if self.sel_day:
            x = calendar.monthrange(year, month)[1]
            if x < self.sel_day:
                self.sel_day = (
                    x if year <= self.sel_year and month <= self.sel_year else 1
                )
