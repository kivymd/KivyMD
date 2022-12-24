"""
Components/DatePicker
=====================

.. seealso::

    `Material Design spec, Date picker <https://material.io/components/date-pickers>`_

.. rubric:: Includes date picker.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/picker-previous.png
    :align: center

.. rubric:: Usage

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDDatePicker

            KV = '''
            MDFloatLayout:

                MDRaisedButton:
                    text: "Open date picker"
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_date_picker()
            '''


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
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

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDRaisedButton
            from kivymd.uix.pickers import MDDatePicker
            from kivymd.uix.screen import MDScreen


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDRaisedButton(
                                text="Open data picker",
                                pos_hint={'center_x': .5, 'center_y': .5},
                                on_release=self.show_date_picker,
                            )
                        )
                    )

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

                def show_date_picker(self, *args):
                    date_dialog = MDDatePicker()
                    date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
                    date_dialog.open()


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDDatePicker.png
    :align: center

Open date dialog with the specified date
----------------------------------------

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1983, month=4, day=12)
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/specified-date.png
    :align: center

Interval date
-------------

You can set the time interval from and to the set date. All days of the week
that are not included in this range will have the status `disabled`.

.. code-block:: python

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_date=datetime.date.today(),
            max_date=datetime.date(
                datetime.date.today().year,
                datetime.date.today().month,
                datetime.date.today().day + 2,
            ),
        )
        date_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/range-date.png
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
        date_dialog = MDDatePicker(min_year=2022, max_year=2030)
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

from __future__ import annotations

__all__ = ("MDDatePicker", "BaseDialogPicker", "DatePickerInputField")

import calendar
import datetime
import math
import os
import time
from datetime import date
from itertools import zip_longest
from typing import Union

from kivy.animation import Animation
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
    CommonElevationBehavior,
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
    CommonElevationBehavior,
    SpecificBackgroundColorBehavior,
):
    """
    Base class for :class:`~kivymd.uix.picker.MDDatePicker` and
    :class:`~kivymd.uix.picker.MDTimePicker` classes.

    For more information, see in the
    :class:`~kivymd.uix.dialog.BaseDialog` and
    :class:`~kivymd.uix.behaviors.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.SpecificBackgroundColorBehavior`
    classes documentation.

    :Events:
        `on_save`
            Events called when the "OK" dialog box button is clicked.
        `on_cancel`
            Events called when the "CANCEL" dialog box button is clicked.
    """

    title_input = StringProperty("INPUT DATE")
    """
    Dialog title fot input date.

    .. code-block:: python

        MDDatePicker(title_input="INPUT DATE")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-date-picker-input-date.png
        :align: center

    :attr:`title_input` is an :class:`~kivy.properties.StringProperty`
    and defaults to `INPUT DATE`.
    """

    title = StringProperty("SELECT DATE")
    """
    Dialog title fot select date.

    .. code-block:: python

        MDDatePicker(title="SELECT DATE")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-date-picker-select-date.png
        :align: center

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `SELECT DATE`.
    """

    radius = ListProperty([7, 7, 7, 7])
    """
    Radius list for the four corners of the dialog.

    .. code-block:: python

        MDDatePicker(radius=[7, 7, 7, 26])

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-date-picker-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[7, 7, 7, 7]`.
    """

    primary_color = ColorProperty(None)
    """
    Background color of toolbar in (r, g, b, a) or string format.

    .. code-block:: python

        MDDatePicker(primary_color="brown")

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-color-date.png
        :align: center

    :attr:`primary_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    accent_color = ColorProperty(None)
    """
    Background color of calendar/clock face in (r, g, b, a) or string format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/accent-color-date.png
        :align: center

    :attr:`accent_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selector_color = ColorProperty(None)
    """
    Background color of the selected day of the month or hour in (r, g, b, a)
    or string format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selector-color-date.png
        :align: center

    :attr:`selector_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_toolbar_color = ColorProperty(None)
    """
    Color of labels for text on a toolbar in (r, g, b, a) or string format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-toolbar-color-date.png
        :align: center

    :attr:`text_toolbar_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Color of text labels in calendar/clock face in (r, g, b, a) or string format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-color-date.png
        :align: center

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_current_color = ColorProperty(None)
    """
    Color of the text of the current day of the month/hour in (r, g, b, a)
    or string format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-current-color-date.png
        :align: center

    :attr:`text_current_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_button_color = ColorProperty(None)
    """
    Text button color in (r, g, b, a) format.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-button-color-date.png
        :align: center

    :attr:`text_button_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_background_color_normal = ColorProperty(None)
    """
    Background color normal of input fields in (r, g, b, a) or string format.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
            input_field_background_color_normal="coral",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-background-color-date.png
        :align: center

    :attr:`input_field_background_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_background_color_focus = ColorProperty(None)
    """
    Background color normal of input fields in (r, g, b, a) or string format.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
            input_field_background_color_normal="coral",
            input_field_background_color_focus="red",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-background-color-focus-date.png
        :align: center

    :attr:`input_field_background_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_background_color = ColorProperty(None)
    """
    .. deprecated:: 1.1.0
        Use :attr:`input_field_background_color_normal` instead.
    """

    input_field_text_color = ColorProperty(None)
    """
    .. deprecated:: 1.1.0
        Use :attr:`input_field_text_color_normal` instead.
    """

    input_field_text_color_normal = ColorProperty(None)
    """
    Text color normal of input fields in (r, g, b, a) or string format.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
            input_field_background_color_normal="brown",
            input_field_background_color_focus="red",
            input_field_text_color_normal="white",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-text-color-normal-date.png
        :align: center

    :attr:`input_field_text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    input_field_text_color_focus = ColorProperty(None)
    """
    Text color focus of input fields in (r, g, b, a) or string format.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
            input_field_background_color_normal="brown",
            input_field_background_color_focus="red",
            input_field_text_color_normal="white",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-field-text-color-normal-date.png
        :align: center

    :attr:`input_field_text_color_focus` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty("Roboto")
    """
    Font name for dialog window text.

    .. code-block:: python

        MDDatePicker(
            primary_color="brown",
            accent_color="darkred",
            selector_color="red",
            text_toolbar_color="lightgrey",
            text_color="orange",
            text_current_color="white",
            text_button_color="lightgrey",
            input_field_background_color_normal="brown",
            input_field_background_color_focus="red",
            input_field_text_color_normal="white",
            input_field_text_color_focus="lightgrey",
            font_name="nasalization.ttf",
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

    def on_input_field_background_color(
        self, instance, value: str | list | tuple
    ) -> None:
        """For supported of current API."""

        self.input_field_background_color_normal = value

    def on_input_field_text_color(
        self, instance, value: str | list | tuple
    ) -> None:
        """For supported of current API."""

        self.input_field_text_color_normal = value

    def on_save(self, *args) -> None:
        """Events called when the "OK" dialog box button is clicked."""

        self.dismiss()

    def on_cancel(self, *args) -> None:
        """Events called when the "CANCEL" dialog box button is clicked."""

        self.dismiss()


class DatePickerBaseTooltip(MDTooltip):
    """Implements tooltips for members of the :class:`~MDDatePicker` class."""

    owner = ObjectProperty()  # MDDatePicker object
    hint_text = StringProperty()


class DatePickerIconTooltipButton(MDIconButton, DatePickerBaseTooltip):
    pass


class DatePickerWeekdayLabel(MDLabel, DatePickerBaseTooltip):
    pass


class DatePickerTypeDateError(Exception):
    pass


class DatePickerInputField(MDTextField):
    """
    Implements date input in dd/mm/yyyy format.

    For more information, see in the
    :class:`~kivymd.uix.textfield.MDTextField` class documentation.
    """

    helper_text_mode = StringProperty("on_error")
    owner = ObjectProperty()  # MDDatePicker object

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(text=self._on_text_check_errors)

    def _on_text_check_errors(self, widget, text):
        if text == "":
            self.error = False
            return
        try:
            datetime.datetime.strptime(text, "%d/%m/%Y")
            self.error = False
        except ValueError:
            self.error = True

    def set_error(self):
        """Sets a text field to an error state."""

        self.error = True

    def input_filter(self, value: str, boolean: bool) -> Union[str, None]:
        """Filters the input according to the specified mode."""

        if self.is_numeric(value):
            return value

    def is_numeric(self, value: str) -> bool:
        """
        Returns true if the value of the `value` argument can be converted
        to an integer, or if the value of the `value` argument is '/'.
        """

        try:
            if value == "/":
                return True
            int(value)
            return True
        except ValueError:
            return False

    def get_list_date(self) -> list:
        """
        Returns a list as `[dd, mm, yyyy]` from a text fied for entering a date.
        """

        return [d for d in self.text.split("/") if d]


class DatePickerInputFieldContainer(MDBoxLayout):
    owner = ObjectProperty()  # MDDatePicker object


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
    is_in_range = BooleanProperty(False)
    is_range_start = BooleanProperty(False)
    is_range_end = BooleanProperty(False)
    is_month_end = BooleanProperty(False)
    is_week_end = BooleanProperty(False)

    def on_release(self):
        self.owner.set_selected_widget(self)

    def on_touch_down(self, touch):
        # If year_layout is active don't dispatch on_touch_down events,
        # so date items don't consume touch.
        if not self.owner.ids._year_layout.disabled:
            return
        super().on_touch_down(touch)


class DatePickerYearSelectableItem(RecycleDataViewBehavior, MDLabel):
    """Implements an item for a pick list of the year."""

    index = None
    selected = BooleanProperty(False)
    owner = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            self.owner.year = int(self.text)
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, table_data, index, is_selected):
        self.selected = is_selected


# TODO: Add the feature to embed the `MDDatePicker` class in other layouts
#  and not use it as a modal dialog.
#  Add a date input mask. Currently, the date is entered in the format
#  'dd/mm/yy'. In some countries, the date is formatted as 'mm/dd/yy'.
class MDDatePicker(BaseDialogPicker):
    text_weekday_color = ColorProperty(None)
    """
    Text color of weekday names in (r, g, b, a) or string format.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-date-picker-text-weekday-color.png
        :align: center

    :attr:`text_weekday_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    helper_text = StringProperty("Wrong date")
    """
    Helper text when entering an invalid date.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-date-picker-helper-text.png
        :align: center

    :attr:`helper_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Wrong date'`.
    """

    day = NumericProperty()
    """
    The day of the month to be opened by default. If not specified,
    the current number will be used.

    See `Open date dialog with the specified date <https://kivymd.readthedocs.io/en/latest/components/datepicker/#open-date-dialog-with-the-specified-date>`_ for more information.

    :attr:`day` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    month = NumericProperty()
    """
    The number of month to be opened by default. If not specified,
    the current number will be used.

    See `Open date dialog with the specified date <https://kivymd.readthedocs.io/en/latest/components/datepicker/#open-date-dialog-with-the-specified-date>`_ for more information.

    :attr:`month` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    year = NumericProperty()
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    See `Open date dialog with the specified date <https://kivymd.readthedocs.io/en/latest/components/datepicker/#open-date-dialog-with-the-specified-date>`_ for more information.

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

    min_date = ObjectProperty(allownone=True)
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.

    See `Open date dialog with the specified date <https://kivymd.readthedocs.io/en/latest/components/datepicker/#interval-date>`_ for more information.

    :attr:`min_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    max_date = ObjectProperty(allownone=True)
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.

    See `Open date dialog with the specified date <https://kivymd.readthedocs.io/en/latest/components/datepicker/#interval-date>`_ for more information.

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

    input_field_cls = ObjectProperty(DatePickerInputField)
    """
    A class that will implement date input in the format dd/mm/yyyy.
    See :class:`~DatePickerInputField` class for more information.

    .. code-block:: python

        class CustomInputField(MDTextField):
            owner = ObjectProperty()  # required attribute

            # Required method.
            def set_error(self):
                [...]

            # Required method.
            def get_list_date(self):
                [...]

            # Required method.
            def input_filter(self):
                [...]

        def show_date_picker(self):
            date_dialog = MDDatePicker(input_field_cls=CustomInputField)

    :attr:`input_field_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to :class:`~DatePickerInputField`.
    """

    sel_year = NumericProperty()
    sel_month = NumericProperty()
    sel_day = NumericProperty()

    _calendar_layout = ObjectProperty()
    _calendar_list = None
    _fields_container = None
    _scale_calendar_layout = NumericProperty(1)
    _scale_year_layout = NumericProperty(0)
    _shift_dialog_height = NumericProperty(0)
    _input_date_dialog_open = BooleanProperty(False)
    _select_year_dialog_open = False
    _date_label_text = StringProperty()

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

        self.generate_list_widgets_days()
        self.update_calendar(self.sel_year, self.sel_month)

    def on_device_orientation(
        self, instance_theme_manager: ThemeManager, orientation_value: str
    ) -> None:
        """Called when the device's screen orientation changes."""

        # Separators of the label text depend on the orientation.
        self._update_date_label_text()
        if self._input_date_dialog_open:
            if orientation_value == "portrait":
                self._shift_dialog_height = dp(250)
            if orientation_value == "landscape":
                self._shift_dialog_height = dp(138)

    def on_ok_button_pressed(self) -> None:
        """
        Called when the 'OK' button is pressed to confirm the date entered.
        """

        if self._input_date_dialog_open and not self._try_apply_input():
            return
        self.dispatch(
            "on_save",
            date(self.sel_year, self.sel_month, self.sel_day),
            self.get_date_range(),
        )

    def is_date_valaid(self, date: str) -> bool:
        """Checks the valid of the currently entered date."""

        try:
            time.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def transformation_from_dialog_select_year(self) -> None:
        self.ids.chevron_left.disabled = False
        self.ids.chevron_right.disabled = False
        self.ids._year_layout.disabled = True
        self.ids.triangle.disabled = False
        self._select_year_dialog_open = False
        self.ids.triangle.icon = "menu-down"

        Animation(opacity=1, d=0.15).start(self.ids.chevron_left)
        Animation(opacity=1, d=0.15).start(self.ids.chevron_right)
        Animation(_scale_year_layout=0, d=0.15).start(self)
        Animation(_scale_calendar_layout=1, d=0.15).start(self)

        # Move selection to the same day and month of the selected year.
        self.sel_year = self.year
        last_day = calendar.monthrange(self.year, self.sel_month)[1]
        self.sel_day = min(self.sel_day, last_day)
        self.update_calendar(self.year, self.month)

    def transformation_to_dialog_select_year(self) -> None:
        def disabled_chevron_buttons(*args):
            self.ids.chevron_left.disabled = True
            self.ids.chevron_right.disabled = True

        self._select_year_dialog_open = True
        self.ids._year_layout.disabled = False
        Animation(opacity=0, d=0.15).start(self.ids.chevron_left)
        Animation(opacity=0, d=0.15).start(self.ids.chevron_right)
        Animation(_scale_calendar_layout=0, d=0.15).start(self)
        anim = Animation(_scale_year_layout=1, d=0.15)
        anim.bind(on_complete=disabled_chevron_buttons)
        anim.start(self)
        self.ids.triangle.icon = "menu-up"
        self.generate_list_widgets_years()
        self.set_position_to_current_year()
        if self.min_year <= self.year < self.max_year:
            index = self.year - self.min_year
            self.ids._year_layout.children[0].select_node(index)
        else:
            self.ids._year_layout.children[0].clear_selection()

    def transformation_to_dialog_input_date(self) -> None:
        self.ids.triangle.disabled = True
        if self._select_year_dialog_open:
            self.transformation_from_dialog_select_year()
        self._input_date_dialog_open = True
        self.ids.edit_icon.icon = "calendar"
        self.ids.label_title.text = self.title_input

        self._fields_container = DatePickerInputFieldContainer(owner=self)
        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            selected_dates = [selected_date]
        else:
            selected_dates = [self.min_date, self.max_date]
        for selected_date in selected_dates:
            field = self.get_field(selected_date)
            field.bind(text=self._on_date_field_text_changes)
            self._fields_container.add_widget(field)
        self.ids.container.add_widget(self._fields_container)

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
        Animation(opacity=1, d=0.15).start(self._fields_container)
        # The label text separator in landscape orientation depends on the
        # open dialog.
        self._update_date_label_text()

    def transformation_from_dialog_input_date(
        self, interval: Union[int, float]
    ) -> None:
        if not self._try_apply_input():
            return
        self._input_date_dialog_open = False
        self.ids.triangle.disabled = False
        self.ids.edit_icon.icon = "pencil"
        self.ids.label_title.text = self.title
        self.ids.container.remove_widget(self._fields_container)
        self._fields_container = None
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
        # The label text separator in landscape orientation depends on the
        # open dialog.
        self._update_date_label_text()

    def _get_dates_from_fields(self):
        """
        Return a list of dates entered by the user in the input fields.

        If there is an error in the field or the field is empty, None will be
        in its place in the list. The length of the list will be 0 if the input
        dialog is closed, otherwise 1 in picker mode or 2 in range mode.
        """

        if not self._fields_container:
            return []

        dates = []
        # Widgets are arranged in the reverse order of their addition.
        for field in reversed(self._fields_container.children):
            try:
                date = datetime.datetime.strptime(field.text, "%d/%m/%Y").date()
            except ValueError:
                date = None
            dates.append(date)

        return dates

    def _try_apply_input(self) -> bool:
        """
        Apply the dates entered by the user, update the calendar and return
        True. If there are errors in the fields, do nothing and return False.
        """

        dates = self._get_dates_from_fields()
        if not dates:
            return True

        # Widgets are arranged in the reverse order of their addition.
        fields = reversed(self._fields_container.children)
        if any(d is None and f.text for f, d in zip(fields, dates)):
            return False

        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            selected_date = dates[0] or selected_date
            self.sel_year = selected_date.year
            self.sel_month = selected_date.month
            self.sel_day = selected_date.day
            self.update_calendar(self.sel_year, self.sel_month)
        elif self.mode == "range":
            date1, date2 = dates[0] or self.min_date, dates[1] or self.max_date
            ends = list(filter(bool, [date1, date2]))
            if ends:
                self.min_date = min(ends)
                self.max_date = max(ends)
                self.update_calendar(self.year, self.month)

        return True

    def _on_date_field_text_changes(self, *args):
        self._update_date_label_text()

    def compare_date_range(self) -> None:
        # TODO: Add behavior if the minimum date range exceeds the maximum
        #  date range. Use toast?
        if self.max_date <= self.min_date:
            raise DatePickerTypeDateError(
                "`max_date` value cannot be less than or equal "
                "to 'min_date' value"
            )

    def update_calendar_for_date_range(self) -> None:
        # This method is no longer used, use update_calendar instead.
        self.update_calendar(self.year, self.month)

    def update_text_full_date(self, list_date) -> None:
        """
        Updates the title of the week, month and number day name
        in an open date input dialog.
        """

        # This method no longer used, use update_calendar instead.
        year = int(list_date[2]) if len(list_date) > 2 else self.sel_year
        month = int(list_date[1]) if len(list_date) > 1 else self.sel_month
        day = int(list_date[0]) if len(list_date) > 0 else self.sel_day
        day = min(day, calendar.monthrange(year, month)[1])
        self.sel_year, self.sel_month, self.sel_day = year, month, day
        self.update_calendar(year, month)

    def update_calendar(self, year, month) -> None:
        self.year, self.month = year, month
        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            selected_dates = {selected_date}
        else:
            selected_dates = {self.min_date, self.max_date}
        # The label text depends on the selected date or date range.
        self._update_date_label_text()
        month_end = date(year, month, calendar.monthrange(year, month)[1])
        dates = self.calendar.itermonthdates(year, month)
        for widget, widget_date in zip_longest(self._calendar_list, dates):
            # Only widgets whose dates are in the displayed month are visible.
            visible = (
                widget_date is not None
                and widget_date.month == month
                and widget_date.year == year
            )
            widget.text = str(widget_date.day) if visible else ""
            widget.is_today = visible and widget_date == self.today
            widget.is_selected = visible and widget_date in selected_dates
            # I don't understand why, but this line is important. Without this
            # line, some widgets that we are trying to disable remain enabled.
            widget.disabled = False
            widget.disabled = not visible
            widget.is_in_range = (
                visible
                and self.min_date is not None
                and self.max_date is not None
                and self.min_date <= widget_date <= self.max_date
            )
            widget.is_range_start = (
                visible
                and self.min_date is not None
                and widget_date == self.min_date
            )
            widget.is_range_end = (
                visible
                and self.max_date is not None
                and widget_date == self.max_date
            )
            widget.is_month_end = widget_date == month_end

    def get_field(self, date=None) -> MDTextField:
        """Creates and returns a text field object used to enter dates."""

        if issubclass(self.input_field_cls, MDTextField):
            text_color_focus = (
                self.input_field_text_color_focus
                if self.input_field_text_color_focus
                else self.theme_cls.primary_color
            )
            text_color_normal = (
                self.input_field_text_color_normal
                if self.input_field_text_color_normal
                else self.theme_cls.disabled_hint_text_color
            )
            fill_color_focus = (
                self.input_field_background_color_focus
                if self.input_field_background_color_focus
                else self.theme_cls.bg_dark
            )
            fill_color_normal = (
                self.input_field_background_color_normal
                if self.input_field_background_color_normal
                else self.theme_cls.bg_darkest
            )

            field = self.input_field_cls(
                owner=self,
                text=date.strftime("%d/%m/%Y") if date else "",
                helper_text=self.helper_text,
                fill_color_normal=fill_color_normal,
                fill_color_focus=fill_color_focus,
                hint_text_color_normal=text_color_normal,
                hint_text_color_focus=text_color_focus,
                text_color_normal=text_color_normal,
                text_color_focus=text_color_focus,
                line_color_focus=text_color_focus,
                line_color_normal=text_color_normal,
            )
            return field
        else:
            raise TypeError(
                "The `input_field_cls` parameter must be an object of the "
                "`kivymd.uix.textfield.MDTextField class`"
            )

    def get_date_range(self) -> list:
        if not self.min_date or not self.max_date:
            return []
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

        # In portrait orientation, the label is stretched in width, so we
        # should not insert line breaks. When the input dialog is open, the
        # label moves to the right and also stretches in width.
        horizontal = orientation == "portrait" or self._input_date_dialog_open

        def date_repr(date):
            return date.strftime("%b").capitalize() + " " + str(date.day)

        input_dates = self._get_dates_from_fields()
        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            if input_dates:
                selected_date = input_dates[0] or selected_date
            weekday_repr = selected_date.strftime("%a").capitalize()
            separator = ", " if horizontal else ",\n"
            return weekday_repr + separator + date_repr(selected_date)
        elif self.mode == "range":
            start, end = self.min_date, self.max_date
            if input_dates:
                start, end = input_dates[0] or start, input_dates[1] or end
            ends = [end for end in (start, end) if end]
            if len(ends) == 0:
                start_repr, end_repr = "Start", "End"
            else:
                start, end = min(ends), max(ends)
                start_repr, end_repr = date_repr(start), date_repr(end)
            separator = " — " if horizontal else ",\n"
            return start_repr + separator + end_repr

    def _update_date_label_text(self):
        self._date_label_text = self.set_text_full_date(
            self.sel_year,
            self.sel_month,
            self.sel_day,
            self.theme_cls.device_orientation,
        )

    def set_selected_widget(self, widget) -> None:
        if self._select_year_dialog_open or self._input_date_dialog_open:
            return
        try:
            widget_date = date(self.year, self.month, int(widget.text))
        except ValueError:
            return
        if self.mode == "picker":
            self.sel_year = widget_date.year
            self.sel_month = widget_date.month
            self.sel_day = widget_date.day
            self.update_calendar(self.sel_year, self.sel_month)
        elif self.mode == "range":
            ends = [end for end in (self.min_date, self.max_date) if end]
            if widget_date in ends:
                ends = [end for end in ends if end != widget_date]
            elif len(ends) < 2:
                ends.append(widget_date)
            else:
                start, end = min(ends), max(ends)
                if abs(widget_date - start).days < abs(widget_date - end).days:
                    start = widget_date
                else:
                    end = widget_date
                ends = [start, end]
            if len(ends) == 0:
                self.min_date, self.max_date = None, None
            else:
                self.min_date, self.max_date = min(ends), max(ends)
            self.update_calendar(self.year, self.month)

    def set_month_day(self, day) -> None:
        # This method is no longer used. The code bellow repeats the behavior
        # that was previously required of it for backward compatibility
        # reasons.
        self.sel_day = day
        self.update_calendar(self.sel_year, self.sel_month)

    def set_position_to_current_year(self) -> None:
        year_layout = self.ids._year_layout
        # When this method is called for the first time, RecycleView has not
        # yet added widgets to the year list, so we use the default height.
        widget_height = year_layout.children[0].default_size[1]
        cols_amount = year_layout.children[0].cols
        rows_amount = math.ceil((self.max_year - self.min_year) / cols_amount)
        row_index = (self.year - self.min_year) // cols_amount
        # To find the middle of the current year widget, we add the height of
        # the rows under this widget with half the widget height.
        widget_center_y = (rows_amount - row_index - 1 + 0.5) * widget_height
        viewport_height = year_layout.height
        year_list_height = rows_amount * widget_height
        # If there are too few years in the list to fill the entire viewport,
        # RecycleView displays additional empty space outside the list.
        # We have to move the viewport up so that this space is displayed
        # under the years list. Also, this guard condition protects against
        # the division by zero error below.
        if viewport_height >= year_list_height:
            year_layout.scroll_y = 1
            return
        viewport_bottom = widget_center_y - 0.5 * viewport_height
        # We set scroll_y property to the ratio of the actual lifting height
        # of the viewport to the maximum possible, and clamp this ratio in the
        # range from 0 to 1 so that the viewport still is in a valid position
        # if it is impossible to show the widget in the middle.
        scroll_y = viewport_bottom / (year_list_height - viewport_height)
        year_layout.scroll_y = min(1, max(0, scroll_y))

    def generate_list_widgets_years(self) -> None:
        self.ids._year_layout.data = []
        for i, number_year in enumerate(range(self.min_year, self.max_year)):
            self.ids._year_layout.data.append(
                {
                    "owner": self,
                    "text": str(number_year),
                    "index": i,
                    "viewclass": "DatePickerYearSelectableItem",
                }
            )

    def generate_list_widgets_days(self) -> None:
        calendar_list = []

        for day in self.calendar.iterweekdays():
            weekday_label = DatePickerWeekdayLabel(
                text=calendar.day_name[day][0].upper(),
                owner=self,
                hint_text=calendar.day_name[day],
            )
            weekday_label.font_name = self.font_name
            self._calendar_layout.add_widget(weekday_label)
        for i in range(6 * 7):  # 6 weeks, 7 days a week
            day_selectable_item = DatePickerDaySelectableItem(
                is_week_end=i % 7 == 6,
                owner=self,
            )
            calendar_list.append(day_selectable_item)
            self._calendar_layout.add_widget(day_selectable_item)
        self._calendar_list = calendar_list

    def change_month(self, operation: str) -> None:
        """
        Called when "chevron-left" and "chevron-right" buttons are pressed.
        Switches the calendar to the previous/next month.
        """

        month_delta = 1 if operation == "next" else -1
        year = self.year + (self.month - 1 + month_delta) // 12
        month = (self.month - 1 + month_delta) % 12 + 1

        if year <= 0:
            year, month = 1, 1
        self.update_calendar(year, month)
