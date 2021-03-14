"""
Components/Pickers
==================

.. seealso::

    `Material Design spec, Time picker <https://material.io/components/time-pickers>`_

    `Material Design spec, Date picker <https://material.io/components/date-pickers>`_

.. rubric:: Includes date, time and color picker.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/picker-previous.png
    :align: center

`KivyMD` provides the following classes for use:

- MDTimePicker_
- MDDatePicker_
- MDThemePicker_

.. MDTimePicker:
MDTimePicker
------------

.. rubric:: Usage

.. code-block::

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.picker import MDTimePicker

    KV = '''
    MDFloatLayout:

        MDRaisedButton:
            text: "Open time picker"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_time_picker()
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def show_time_picker(self):
            '''Open time picker dialog.'''

            time_dialog = MDTimePicker()
            time_dialog.open()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDTimePicker.png
    :align: center

Binding method returning set time
---------------------------------

.. code-block:: python

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        '''
        The method returns the set time.

        :type instance: <kivymd.uix.picker.MDTimePicker object>
        :type time: <class 'datetime.time'>
        '''

        return time

Open time dialog with the specified time
----------------------------------------

Use the :attr:`~MDTimePicker.set_time` method of the
:class:`~MDTimePicker.` class.

.. code-block:: python

    def show_time_picker(self):
        from datetime import datetime

        # Must be a datetime object
        previous_time = datetime.strptime("03:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(previous_time)
        time_dialog.open()

.. note:: For customization of the :class:`~MDTimePicker` class, see the
    documentation in the :class:`~BaseDialogPicker` class.

.. MDDatePicker:
MDDatePicker
------------

.. warning:: The widget is under testing. Therefore, we would be grateful if
    you would let us know about the bugs found.

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.picker import MDDatePicker

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

.. MDThemePicker:
MDThemePicker
-------------

.. code-block:: python

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDThemePicker.gif
    :align: center
"""

__all__ = ("MDTimePicker", "MDDatePicker", "MDThemePicker", "BaseDialogPicker")

import calendar
import datetime
import re
from datetime import date

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.factory import Factory
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
from kivy.utils import get_color_from_hex
from kivy.vector import Vector

from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior
from kivymd.toast import toast
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tooltip import MDTooltip

Builder.load_string(
    """
#:import os os
#:import date datetime.date
#:import calendar calendar
#:import platform platform
#:import Clock kivy.clock.Clock
#:import images_path kivymd.images_path


<DatePickerBaseTooltip>
    on_enter:
        self.tooltip_text = "" if self.owner \
        and self.owner._input_date_dialog_open \
        or self.owner._select_year_dialog_open \
        else self.hint_text


<DatePickerIconTooltipButton>


<MDDatePicker>
    _calendar_layout: _calendar_layout
    size_hint: None, None
    size:
        (dp(328), dp(512) - root._shift_dialog_height) \
        if root.theme_cls.device_orientation == "portrait" \
        else (dp(528), dp(328) - root._shift_dialog_height)

    MDRelativeLayout:
        id: container
        background: os.path.join(images_path, "transparent.png")

        canvas:
            Color:
                rgb:
                    app.theme_cls.primary_color \
                    if not root.primary_color else root.primary_color
            RoundedRectangle:
                size:
                    (dp(328), dp(120)) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (dp(168), dp(328) - root._shift_dialog_height)
                pos:
                    (0, root.height - dp(120)) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (0, 0)
                radius:
                    (root.radius[0], root.radius[1], dp(0), dp(0)) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (root.radius[0], dp(0), dp(0), root.radius[3])
            Color:
                rgba:
                    app.theme_cls.bg_normal \
                    if not root.accent_color else root.accent_color
            RoundedRectangle:
                size:
                    (dp(328), dp(512) - dp(120) - root._shift_dialog_height) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (dp(360), dp(328) - root._shift_dialog_height)
                pos:
                    (0, 0) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (dp(168), 0)
                radius:
                    (dp(0), dp(0), root.radius[2], root.radius[3]) \
                    if root.theme_cls.device_orientation == "portrait" \
                    else (dp(0), root.radius[1], root.radius[2], dp(0))

        MDLabel:
            id: label_title
            font_style: "Body2"
            bold: True
            theme_text_color: "Custom"
            size_hint_x: None
            width: root.width
            adaptive_height: True
            text: root.title
            font_name: root.font_name
            pos:
                (dp(24), root.height - self.height - dp(18)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(24), root.height - self.height - dp(24))
            text_color:
                root.specific_text_color \
                if not root.text_toolbar_color else root.text_toolbar_color

        MDLabel:
            id: label_full_date
            font_style: "H4"
            theme_text_color: "Custom"
            size_hint_x: None
            width: root.width
            adaptive_height: True
            font_name: root.font_name
            markup: True
            pos:
                (dp(24), root.height - dp(120) + dp(18)) \
                if root.theme_cls.device_orientation == "portrait" \
                else \
                ( \
                dp(24) if not root._input_date_dialog_open else dp(168) + dp(24), \
                root.height - self.height - dp(96) \
                )
            text:
                root.set_text_full_date(root.sel_year, root.sel_month, root.sel_day, \
                root.theme_cls.device_orientation)
            text_color:
                ( \
                root.specific_text_color \
                if not root.text_toolbar_color else root.text_toolbar_color \
                ) \
                if root.theme_cls.device_orientation == "portrait" \
                else \
                ( \
                ( \
                self.theme_cls.primary_color \
                if not root.primary_color else root.primary_color \
                ) \
                if root._input_date_dialog_open \
                else \
                ( \
                root.specific_text_color \
                if not root.text_toolbar_color else root.text_toolbar_color \
                ) \
                )

        RecycleView:
            id: _year_layout
            key_viewclass: "viewclass"
            size_hint: None, None
            size: _calendar_layout.size
            pos: _calendar_layout.pos
            disabled: True

            canvas.before:
                PushMatrix
                Scale:
                    x: root._scale_year_layout
                    y: root._scale_year_layout
                    origin: self.center
            canvas.after:
                PopMatrix

            SelectYearList:
                cols: 3
                default_size: dp(170), dp(36)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height

        MDIconButton:
            id: edit_icon
            icon: "pencil"
            user_font_size: "24sp"
            theme_text_color: "Custom"
            on_release:
                root.transformation_to_dialog_input_date() \
                if not root._input_date_dialog_open else \
                Clock.schedule_once(root.transformation_from_dialog_input_date, .15)
            x:
                (root.width - self.width - dp(12)) \
                if root.theme_cls.device_orientation == "portrait" \
                else dp(12)
            y:
                (root.height - dp(120) + dp(12)) \
                if root.theme_cls.device_orientation == "portrait" \
                else  dp(12)
            text_color:
                root.specific_text_color \
                if not root.text_toolbar_color else root.text_toolbar_color

        MDLabel:
            id: label_month_selector
            font_style: "Body2"
            -text_size: None, None
            theme_text_color: "Custom"
            adaptive_size: True
            text: calendar.month_name[root.month].capitalize() + " " + str(root.year)
            font_name: root.font_name
            pos:
                (dp(24), root.height - dp(120) - self.height - dp(20)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(168) + dp(24), label_title.y)
            text_color:
                app.theme_cls.text_color \
                if not root.text_color else root.text_color

        DatePickerIconTooltipButton:
            id: triangle
            owner: root
            icon: "menu-down"
            ripple_scale: .5
            theme_text_color: "Custom"
            hint_text: "Choose year"
            on_release:
                root.transformation_to_dialog_select_year() \
                if not root._select_year_dialog_open else \
                root.transformation_from_dialog_select_year()
            pos:
                (label_month_selector.width + dp(14), root.height - dp(123) - self.height) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(180) + label_month_selector.width, label_title.y - dp(14))
            text_color:
                app.theme_cls.text_color \
                if not root.text_color else root.text_color
            md_bg_color_disabled: 0, 0, 0, 0

        DatePickerIconTooltipButton:
            id: chevron_left
            owner: root
            icon: "chevron-left"
            theme_text_color: "Secondary"
            on_release: root.change_month("prev")
            theme_text_color: "Custom"
            hint_text: "Previous month"
            x:
                dp(228) if root.theme_cls.device_orientation == "portrait" \
                else dp(418)
            y:
                root.height - dp(120) - self.height / 2 - dp(30) \
                if root.theme_cls.device_orientation == "portrait" \
                else dp(272)
            text_color:
                app.theme_cls.text_color \
                if not root.text_color else root.text_color

        DatePickerIconTooltipButton:
            id: chevron_right
            owner: root
            icon: "chevron-right"
            theme_text_color: "Secondary"
            on_release: root.change_month("next")
            theme_text_color: "Custom"
            hint_text: "Next month"
            x:
                dp(272) if root.theme_cls.device_orientation == "portrait" \
                else dp(464)
            y:
                root.height - dp(120) - self.height / 2 - dp(30) \
                if root.theme_cls.device_orientation == "portrait" \
                else dp(272)
            text_color:
                app.theme_cls.text_color \
                if not root.text_color else root.text_color

        # TODO: Replace the GridLayout with a RecycleView
        # if it improves performance.
        GridLayout:
            id: _calendar_layout
            cols: 7
            size_hint: None, None
            size:
                (dp(44 * 7), dp(40 * 7)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(46 * 7), dp(32 * 7))
            col_default_width:
                dp(42) if root.theme_cls.device_orientation == "portrait" \
                else dp(39)
            padding:
                (dp(2), 0) if root.theme_cls.device_orientation == "portrait" \
                else (dp(7), 0)
            spacing:
                (dp(2), 0) if root.theme_cls.device_orientation == "portrait" \
                else (dp(7), 0)
            pos:
                (dp(10), dp(56)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(168) + dp(20), dp(44))

            canvas.before:
                PushMatrix
                Scale:
                    x: root._scale_calendar_layout
                    y: root._scale_calendar_layout
                    origin: self.center
            canvas.after:
                PopMatrix

        MDFlatButton:
            id: ok_button
            width: dp(32)
            pos: root.width - self.width, dp(10)
            text: "OK"
            theme_text_color: "Custom"
            font_name: root.font_name
            text_color:
                root.theme_cls.primary_color \
                if not root.text_button_color else root.text_button_color
            on_release:
                root.dispatch(\
                "on_save", \
                date(root.sel_year, root.sel_month, root.sel_day), \
                root._date_range \
                )

        MDFlatButton:
            id: cancel_button
            text: "CANCEL"
            on_release: root.dispatch("on_cancel", None)
            theme_text_color: "Custom"
            pos: root.width - self.width - ok_button.width - dp(10), dp(10)
            font_name: root.font_name
            text_color:
                root.theme_cls.primary_color \
                if not root.text_button_color else root.text_button_color


<DatePickerDaySelectableItem>
    size_hint: None, None
    size:
        (dp(42), dp(42)) \
        if root.theme_cls.device_orientation == "portrait" \
        else (dp(32), dp(32))
    disabled: True

    canvas:
        Color:
            rgba:
                ( \
                ( \
                self.theme_cls.primary_color if not root.owner.selector_color \
                else root.owner.selector_color \
                ) \
                if root.is_selected and not self.disabled \
                else (0, 0, 0, 0) \
                ) \
                if self.owner.mode != "range" else \
                ( \
                ( \
                self.theme_cls.primary_color if not root.owner.selector_color \
                else root.owner.selector_color \
                ) \
                if root.is_selected and not self.disabled \
                and (self.owner.mode == "range" and self.owner._start_range_date) \
                else (0, 0, 0, 0) \
                )
        Ellipse:
            size:
                (dp(42), dp(42)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(32), dp(32))
            pos: self.pos

    # Fill marking the available dates of the range, if using the `range` mode
    # or use `min_date/max_date`.
    canvas.before:
        Color:
            rgba:
                (\
                self.owner.selector_color[:-1] + [.3] \
                if self.owner.selector_color \
                else self.theme_cls.primary_color[:-1] + [.3] \
                ) \
                if not self.disabled \
                and self.text \
                and self.check_date(self.owner.year, self.owner.month, int(self.text)) \
                else (0, 0, 0, 0)
        RoundedRectangle:
            size:
                (dp(44), dp(32)) \
                if root.theme_cls.device_orientation == "portrait" \
                else \
                (dp(32), dp(28)) \
                if self.index in [6, 13, 20, 27, 30] or self.owner._date_range \
                and self.text and self.owner._date_range[-1] == date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                else (dp(46), dp(28))
            pos:
                (self.x - dp(1.5), self.y + dp(5)) \
                if root.theme_cls.device_orientation == "portrait" else \
                (self.x, self.y + 1)
            radius:
                [0, 0, 0, 0] if not self.owner._date_range else \
                ( \
                [self.width / 2, 0, 0, self.width / 2] \
                if self.text and self.owner._date_range[0] == date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                or (self.index in [0, 7, 14, 21, 28] and root.is_selected) \
                else \
                ( \
                [0, 0, 0, 0] if self.text \
                and self.owner._date_range[-1] != date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                and self.index not in [6, 13, 20, 27, 30] \
                else [0, self.width / 2, self.width, 0] \
                if root.is_selected or self.text \
                and self.owner._date_range[-1] == date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                else [0, 0, 0, 0]) \
                )

        # Circle marking the beginning and end of the date range if the "range"
        # mode is used.
        Color:
            rgba:
                [0, 0, 0, 0] if not self.owner._date_range else \
                (
                ( \
                self.theme_cls.primary_color if not root.owner.selector_color \
                else root.owner.selector_color \
                ) \
                if self.text and self.owner._date_range[0] == date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                or \
                self.text and self.owner._date_range[-1] == date( \
                self.current_year, \
                self.current_month, \
                int(self.text) \
                ) \
                else (0, 0, 0, 0) \
                )
        Ellipse:
            size:
                (dp(42), dp(42)) \
                if root.theme_cls.device_orientation == "portrait" \
                else (dp(32), dp(32))
            pos: self.pos

    MDLabel:
        font_style: "Caption"
        size_hint_x: None
        halign: "center"
        text: root.text
        font_name: root.owner.font_name
        theme_text_color: "Custom"
        text_color:
            ( \
            root.theme_cls.primary_color \
            if not root.owner.text_current_color \
            else root.owner.text_current_color \
            ) \
            if root.is_today and not root.is_selected \
            else ( \
            ( \
            root.theme_cls.text_color \
            if not root.is_selected or root.owner.mode == "range" \
            else (1, 1, 1, 1) \
            ) \
            if not root.owner.text_color \
            else \
            ( \
            root.owner.text_color \
            if not root.is_selected else (1, 1, 1, 1)) \
            )


<DatePickerWeekdayLabel>
    font_style: "Caption"
    theme_text_color: "Custom"
    size_hint: None, None
    text_size: self.size
    halign: "center"
    valign:
        "middle" if root.theme_cls.device_orientation == "portrait" \
        else "center"
    size:
        (dp(40), dp(40)) if root.theme_cls.device_orientation == "portrait" \
        else (dp(32), dp(32))
    text_color:
        app.theme_cls.disabled_hint_text_color \
        if not root.owner.text_weekday_color else root.owner.text_weekday_color


<DatePickerYearSelectableItem>
    font_style: "Caption"
    size_hint_x: None
    valign: "middle"
    halign: "center"
    text: root.text
    theme_text_color: "Custom"
    on_text: root.font_name = root.owner.font_name

    canvas.before:
        Color:
            rgba:
                root.selected_color if root.selected_color \
                else self.theme_cls.primary_color
        RoundedRectangle:
            pos: self.x + dp(12), self.y
            size: self.width - dp(24), self.height
            radius: [root.height / 2, ]


<DatePickerDatePickerEnterDataFieldContainer>
    adaptive_height: True
    size_hint_x: None
    spacing: dp(8)
    width:
        self.owner.width - dp(48) \
        if root.owner.theme_cls.device_orientation == "portrait" \
        else self.owner.width - dp(168) - dp(48)
    y:
        self.owner.height - dp(123) - self.height - dp(20) \
        if root.owner.theme_cls.device_orientation == "portrait" \
        else self.owner.height - self.height - dp(24)
    x:
        dp(24) if root.owner.theme_cls.device_orientation == "portrait" \
        else dp(168) + dp(24)


<DatePickerEnterDataField>
    mode: "fill"
    opacity: 0
    hint_text: "dd/mm/yyyy"
    input_filter: root.input_filter
    do_backspace: root.do_backspace
    fill_color:
        (0, 0, 0, .15) \
        if not self.owner.input_field_background_color \
        else root.owner.input_field_background_color
"""
)


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

    def on_save(self, *args):
        """Events called when the "OK" dialog box button is clicked."""

        self.dismiss()

    def on_cancel(self, *args):
        """Events called when the "CANCEL" dialog box button is clicked."""

        self.dismiss()


class DatePickerBaseTooltip(MDTooltip):
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

    def isnumeric(self, value):
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

    def do_backspace(self, *args):
        """Prevent deleting text from the middle of a line of a text field."""

        self._backspace = True
        self.text = self.text[:-1]
        self._date = self.text
        self._backspace = False

    def input_filter(self, value, boolean):
        """Date validity check in dd/mm/yyyy format."""

        cursor = self.cursor[0]
        if len(self.text) == 10:
            return
        if self.isnumeric(value):
            self._date += value
            value = int(value)
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

    def on_text(self, instance_field, value):
        if value != "" and not value.isspace() and not self._backspace:
            if len(value) <= 1 and instance_field.focus:
                instance_field.text = value
                self._set_pos_cursor()
            elif len(value) == 3:
                start = instance_field.text[:-1]
                end = instance_field.text[-1]
                instance_field.text = f"{start}/{end}"
                self._set_pos_cursor()
            elif len(value) == 5:
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

    def check_date(self, year, month, day):
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

    def on_device_orientation(self, instance, value):
        if self._input_date_dialog_open:
            if value == "portrait":
                self._shift_dialog_height = dp(250)
            if value == "landscape":
                self._shift_dialog_height = dp(138)

    def transformation_from_dialog_select_year(self):
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

    def transformation_to_dialog_select_year(self):
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

    def transformation_to_dialog_input_date(self):
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

    def transformation_from_dialog_input_date(self, interval):
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

    def compare_date_range(self):
        # TODO: Add behavior if the minimum date range exceeds the maximum
        #  date range. Use toast?
        if self.max_date <= self.min_date:
            raise DatePickerTypeDateError(
                "`max_date` value cannot be less than or equal "
                "to 'min_date' value"
            )

    def update_calendar_for_date_range(self):
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

        field = DatePickerEnterDataField(owner=self)
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


Builder.load_string(
    """
<TimeInputLabel@MDLabel>:
    theme_text_color: "Custom"
    font_size: dp(10)
    halign: "left"
    valign: "bottom"
    adaptive_size: True


<AmPmSelectorLabel>
    halign: "center"
    valign: "center"
    theme_text_color: "Custom"


<AmPmSelector>
    size_hint: None, None

    canvas.before:
        Color:
            rgba: root.border_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [root.border_radius, ]

        #AM
        Color:
            rgba: root._am_bg_color
        RoundedRectangle:
            pos:
                [ \
                self.pos[0] + root.border_width, \
                self.pos[1] + self.height/2 + self.border_width * 0.5 \
                ] if self.orientation == "vertical" else \
                [ \
                self.pos[0] + root.border_width, \
                self.pos[1] + root.border_width \
                ]
            size:
                [ \
                self.size[0] - root.border_width * 2, \
                self.size[1] / 2 - self.border_width * 1.5 \
                ] if self.orientation == "vertical" else \
                [ \
                self.size[0] / 2 - root.border_width * 1.5, \
                self.size[1] - root.border_width * 2 \
                ]
            radius: [root.border_radius, root.border_radius, 0, 0] \
                if self.orientation == "vertical" else \
                [root.border_radius, 0, 0, root.border_radius]

        #PM
        Color:
            rgba: root._pm_bg_color
        RoundedRectangle:
            pos:
                [ \
                self.pos[0] + root.border_width, \
                self.pos[1] + self.border_width \
                ] if self.orientation == "vertical" else \
                [ \
                self.pos[0] + root.size[0] / 2 + root.border_width / 2, \
                self.pos[1] + root.border_width \
                ]
            size:
                [ \
                self.size[0] - root.border_width * 2, \
                self.size[1] / 2 - self.border_width * 1.5 \
                ] if self.orientation == "vertical" else \
                [ \
                self.size[0] / 2 - root.border_width * 1.5, \
                self.size[1] - root.border_width * 2 \
                ]
            radius: [0, 0, root.border_radius, root.border_radius] \
                if self.orientation == "vertical" else \
                [0 ,root.border_radius, root.border_radius, 0]

    # AM
    AmPmSelectorLabel:
        text: "AM"
        on_release: root.selected = "am"
        text_color: root.text_color

    AmPmSelectorLabel:
        text: "PM"
        on_release: root.selected = "pm"
        text_color: root.text_color


<TimeInputTextField>
    size_hint: None, 1
    width: dp(96)
    mode: "fill"
    active_line: False
    font_size: dp(56)
    line_color_normal: 0, 0, 0, 0
    on_text: root.on_text
    radius: [dp(10), ]


<TimeInput>
    size_hint: None, None
    _hour: hour
    _minute: minute

    TimeInputTextField:
        id: hour
        num_type: "hour"
        pos: 0, 0
        text_color: root.text_color
        disabled: root.disabled
        on_text: root.dispatch("on_time_input")
        radius: root.hour_radius
        on_select:
            root.dispatch("on_hour_select")
            root.state = "hour"
        fill_color:
            [*root.bg_color_active[:3], 0.5] \
            if root.state == "hour" else [*root.bg_color[:3], 0.5]


    MDLabel:
        text: ":"
        size_hint: None, None
        size: dp(24), dp(80)
        halign: "center"
        valign: "center"
        font_size: dp(50)
        pos: dp(96), 0
        theme_text_color: "Custom"
        text_color: root.text_color

    TimeInputTextField:
        id: minute
        num_type: "minute"
        pos: dp(120), 0
        text_color: root.text_color
        disabled: root.disabled
        on_text: root.dispatch("on_time_input")
        radius: root.minute_radius
        on_select:
            root.dispatch("on_minute_select")
            root.state = "minute"
        fill_color:
            [*root.bg_color_active[:3], 0.5] \
            if root.state == "minute" else [*root.bg_color[:3], 0.5]


<CircularSelector>
    circular_padding: dp(28)
    size_hint: None, None
    size: [dp(256), dp(256)]
    row_spacing: dp(40)

    canvas.before:
        PushMatrix
        Scale:
            origin: self.scale_origin
            x: root.scale
            y: root.scale
        Color:
            rgba: root.bg_color
        Ellipse:
            size: self.size
            pos: self.pos
        PushMatrix
        Scale:
            origin: self.center
            x: root.content_scale
            y: root.content_scale
        Color:
            rgb: root.selector_color
            a: 0 if self.selector_pos == [0, 0] else 1
        Ellipse:
            size: self.selector_size, self.selector_size
            pos:
                [self.selector_pos[0] -  self.selector_size / 2, \
                self.selector_pos[1] - self.selector_size / 2]
        Ellipse:
            size: dp(10), dp(10)
            pos: [self.center[0] - dp(5), self.center[1] - dp(5)]
        Line:
            points: [self.center, self.selector_pos]
            width: dp(1)
    canvas.after:
        PopMatrix
        PopMatrix


<SelectorLabel>
    halign: "center"
    valign: "center"
    adaptive_size: True
    theme_text_color: "Custom"


<MDTimePicker>
    auto_dismiss: True
    size_hint: None, None
    _time_input: _time_input
    _selector: _selector
    _am_pm_selector: _am_pm_selector
    _minute_label: _minute_label
    _hour_label: _hour_label

    MDRelativeLayout:
        canvas.before:
            Color:
                rgba:
                    root.primary_color \
                    if root.primary_color \
                    else root.theme_cls.bg_normal

            RoundedRectangle:
                size: self.size
                radius: root.radius

        MDLabel:
            id: label_title
            font_style: "Body2"
            bold: True
            theme_text_color: "Custom"
            size_hint_x: None
            width: root.width
            adaptive_height: True
            text: root.title
            font_name: root.font_name
            pos: (dp(24), root.height - self.height - dp(18))
            text_color:
                root.text_toolbar_color if root.text_toolbar_color \
                else root.theme_cls.text_color

        TimeInput:
            id: _time_input
            bg_color:
                root.accent_color if root.accent_color else \
                root.theme_cls.primary_light
            bg_color_active:
                root.selector_color if root.selector_color \
                else root.theme_cls.primary_color
            text_color:
                root.input_field_text_color if root.input_field_text_color else \
                root.theme_cls.text_color
            on_time_input: root._get_time_input(*self.get_time())
            on_hour_select: _selector.switch_mode("hour")
            on_minute_select: _selector.switch_mode("minute")
            minute_radius: root.minute_radius
            hour_radius: root.hour_radius

        TimeInputLabel:
            id: _hour_label
            text: "Hour"
            opacity: 0
            text_color:
                root.text_toolbar_color if root.text_toolbar_color else \
                root.theme_cls.secondary_text_color

        TimeInputLabel:
            id: _minute_label
            text: "Minute"
            opacity: 0
            text_color:
                root.text_toolbar_color if root.text_toolbar_color else \
                root.theme_cls.secondary_text_color

        AmPmSelector:
            id: _am_pm_selector
            border_color:
                root.accent_color if root.accent_color else \
                root.theme_cls.primary_color
            border_radius: root.am_pm_radius
            bg_color:
                root.primary_color if root.primary_color else \
                root.theme_cls.bg_normal
            border_width: root.am_pm_border_width
            bg_color_active:
                root.selector_color if root.selector_color else \
                root.theme_cls.primary_light
            text_color:
                root.input_field_text_color if root.input_field_text_color else \
                root.theme_cls.text_color
            on_selected: root._get_am_pm(self.selected)

        CircularSelector:
            id: _selector
            text_color:
                root.text_color if root.text_color else \
                root.theme_cls.text_color
            bg_color:
                root.accent_color if root.accent_color else \
                root.theme_cls.primary_light
            selector_color:
                root.selector_color if root.selector_color else \
                root.theme_cls.primary_color
            font_name: root.font_name
            on_selector_change: root._get_dial_time(_selector)

        MDIconButton:
            id: input_clock_switch
            icon: "keyboard"
            pos: dp(12), dp(8)
            theme_text_color: "Custom"
            user_font_size: "24dp"
            on_release: root._switch_input()
            text_color:
                root.text_toolbar_color if root.text_toolbar_color else \
                root.theme_cls.secondary_text_color

        MDFlatButton:
            id: cancel_button
            text: "CANCEL"
            on_release: root.dispatch("on_cancel", None)
            theme_text_color: "Custom"
            pos: root.width - self.width - ok_button.width - dp(10), dp(10)
            font_name: root.font_name
            text_color:
                root.theme_cls.primary_color \
                if not root.text_button_color else root.text_button_color

        MDFlatButton:
            id: ok_button
            width: dp(32)
            pos: root.width - self.width, dp(10)
            text: "OK"
            theme_text_color: "Custom"
            font_name: root.font_name
            text_color:
                root.theme_cls.primary_color \
                if not root.text_button_color else root.text_button_color
            on_release: root.dispatch("on_save", root._get_data())
""",
    filename="picker.kv",
)


class AmPmSelectorLabel(ButtonBehavior, MDLabel):
    pass


class AmPmSelector(ThemableBehavior, MDBoxLayout, EventDispatcher):
    border_radius = NumericProperty()
    border_color = ColorProperty()
    bg_color = ColorProperty()
    bg_color_active = ColorProperty()
    border_width = NumericProperty()
    am = ObjectProperty()
    pm = ObjectProperty()
    text_color = ColorProperty()
    selected = StringProperty()
    _am_bg_color = ColorProperty()
    _pm_bg_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(selected=self._upadte_color)
        Clock.schedule_once(self._upadte_color)

    def _upadte_color(self, *args):
        bg_color = self.bg_color_active
        if self.selected == "am":
            self._am_bg_color = bg_color
            self._pm_bg_color = self.bg_color
        elif self.selected == "pm":
            self._am_bg_color = self.bg_color
            self._pm_bg_color = bg_color


class TimeInputTextField(MDTextField):
    num_type = OptionProperty("hour", options=["hour", "minute"])
    hour_regx = "^[0-9]$|^0[1-9]$|^1[0-2]$"
    minute_regx = "^[0-9]$|^0[0-9]$|^[1-5][0-9]$"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.on_text)
        self.register_event_type("on_select")
        self.bind(text_color=self.setter("_current_hint_text_color"))
        self.bind(text_color=self.setter("current_hint_text_color"))

    def validate_time(self, s):
        reg = self.hour_regx if self.num_type == "hour" else self.minute_regx
        return re.match(reg, s)

    def insert_text(self, s, from_undo=False):
        text = self.text.strip()
        current_string = "".join([text, s])
        if not self.validate_time(current_string):
            s = ""
        return super().insert_text(s, from_undo=from_undo)

    def on_text(self, *args):
        """
        Texts should be center aligned. now we are setting the padding of text
        to somehow make them aligned.
        """

        if not self.text:
            self.text = " "

        self._refresh_text(self.text)
        max_size = max(self._lines_rects, key=lambda r: r.size[0]).size
        dx = (self.width - max_size[0]) / 2.0
        dy = (self.height - max_size[1]) / 2.0
        self.padding = [dx, dy, dx, dy]

        if len(self.text) > 1:
            self.text = self.text.replace(" ", "")

    def on_focus(self, *args):
        super().on_focus(*args)
        if self.text.strip():
            if (
                not self.focus
                and int(self.text) == 0
                and self.num_type == "hour"
            ):
                self.text = "12"
        else:
            self.text = " 12" if self.num_type == "hour" else " 00"

    def on_select(self, *args):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dispatch("on_select")
            super().on_touch_down(touch)


class TimeInput(MDRelativeLayout, EventDispatcher):
    bg_color = ColorProperty()
    bg_color_active = ColorProperty()
    text_color = ColorProperty()
    disabled = BooleanProperty(True)
    minute_radius = ListProperty([0, 0, 0, 0])
    hour_radius = ListProperty([0, 0, 0, 0])
    state = StringProperty("hour")
    _hour = ObjectProperty()
    _minute = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_time_input")
        self.register_event_type("on_hour_select")
        self.register_event_type("on_minute_select")

    def set_time(self, time_list):
        hour, minute = time_list
        self._hour.text = hour
        self._minute.text = minute

    def get_time(self):
        hour = self._hour.text.strip()
        minute = self._minute.text.strip()
        return [hour, minute]

    def _update_padding(self, *args):
        self._hour.on_text()
        self._minute.on_text()

    def on_time_input(self, *args):
        pass

    def on_minute_select(self, *args):
        pass

    def on_hour_select(self, *args):
        pass


class SelectorLabel(MDLabel):
    pass


class CircularSelector(MDCircularLayout, EventDispatcher):
    mode = OptionProperty("hour", options=["hour", "minute"])  # and military
    text_color = ColorProperty()
    selected_hour = StringProperty("12")
    selected_minute = StringProperty("0")
    selector_size = NumericProperty("48dp")
    selector_pos = ListProperty([0, 0])
    selector_color = ColorProperty()
    bg_color = ColorProperty()
    font_name = StringProperty()
    _centers_pos = ListProperty()
    scale = NumericProperty(1)
    content_scale = NumericProperty(1)
    t = StringProperty("out_quad")
    d = NumericProperty(0.2)
    scale_origin = ListProperty([100, 100])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            mode=self._update_labels,
            selected_hour=self.update_time,
            selected_minute=self.update_time,
        )
        Clock.schedule_once(lambda x: self._update_labels(animate=False))
        self.register_event_type("on_selector_change")

    def do_layout(self, *largs, **kwargs):
        self.update_time()
        return super().do_layout(*largs, **kwargs)

    def _update_labels(self, animate=True, *args):
        """
        This method builds the selector based on current mode which currently
        can be hour or minute.
        """

        if self.mode == "hour":
            param = (1, 12)
            self.degree_spacing = 30
            self.start_from = 60
        elif self.mode == "minute":
            param = (0, 59, 5)
            self.degree_spacing = 6
            self.start_from = 90
        elif self.mode == "military":
            param = (1, 24)
            self.degree_spacing = 30
            self.start_from = 90
        if animate:
            anim = Animation(content_scale=0, t=self.t, d=self.d)
            anim.bind(on_complete=lambda *args: self._add_items(*param))
            anim.start(self)
        else:
            self._add_items(*param)

    def _add_items(self, start, end, step=1):
        """
        Adds all number in range `[start, end + 1]` to the circular layout with
        the specified step. Step means that all widgets will be added to layout
        but sets the opacity for skipped widgets to `0` because we are using
        the label's text as a reference to the selected number so we have to
        add these to layout.
        """

        self.clear_widgets()
        i = 0
        for x in range(start, end + 1):
            label = SelectorLabel(
                text=f"{x}",
            )
            if i % step != 0:
                label.opacity = 0
            self.bind(
                text_color=label.setter("text_color"),
                font_name=label.setter("font_name"),
            )
            self.add_widget(label)
            i += 1
        Clock.schedule_once(self.update_time)
        Clock.schedule_once(self._get_centers, 0.1)
        anim = Animation(content_scale=1, t=self.t, d=self.d)
        anim.start(self)

    def _get_centers(self, *args):
        """
        Returns a list of all center. we use this for positioning the selector
        indicator.
        """

        self._centers_pos = []
        for child in self.children:
            self._centers_pos.append(child.center)

    def _get_closest_widget(self, pos):
        """
        Returns the nearest widget to the given position. we use this to create
        the magnetic effect.
        """

        distance = [Vector(pos).distance(point) for point in self._centers_pos]
        if not distance:
            return False
        index = distance.index(min(distance))
        return self.children[index]

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            closest_wid = self._get_closest_widget(touch.pos)
            self.set_time(closest_wid.text)
            return True

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            closest_wid = self._get_closest_widget(touch.pos)
            self.set_time(closest_wid.text)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            return True

    def set_selector(self, selected):
        """
        Sets the selector's position towards the given text.
        """

        widget = None
        for wid in self.children:
            wid.text_color = self.text_color
            if wid.text == selected:
                widget = wid
        if not widget:
            return False
        self.selector_pos = widget.center
        widget.text_color = [1, 1, 1, 1]
        self.dispatch("on_selector_change")
        return True

    def set_time(self, selected):
        if self.mode == "hour":
            self.selected_hour = selected
        elif self.mode == "minute":
            self.selected_minute = selected

    def update_time(self, *args):
        if self.mode == "hour":
            self.set_selector(self.selected_hour)
        elif self.mode == "minute":
            self.set_selector(self.selected_minute)

    def get_selected(self):
        return self.selected

    def on_selector_change(self, *args):
        pass

    def switch_mode(self, mode):
        if mode != self.mode:
            self.mode = mode


class MDTimePicker(BaseDialogPicker):
    hour = StringProperty("12")
    """
    Current hour

    :attr:`hour` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'12'`.
    """

    minute = StringProperty("0")
    """
    Current minute

    :attr:`minute` is an :class:`~kivy.properties.StringProperty`
    and defaults to `0`.
    """

    minute_radius = ListProperty(
        [
            dp(5),
        ]
    )
    """
    Radius of the minute input field.

    :attr:`minute_radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(5),]`.
    """

    hour_radius = ListProperty(
        [
            dp(5),
        ]
    )
    """
    Radius of the hour input field.

    :attr:`hour_radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(5),]`.
    """

    am_pm_radius = NumericProperty("5dp")
    """
    Radius of the AM/PM selector.

    :attr:`am_pm_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(5)`.
    """

    am_pm_border_width = NumericProperty("1dp")
    """
    Width of the AM/PM selector's borders.

    :attr:`am_pm_border_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(1)`.
    """

    am_pm = OptionProperty("am", options=["am", "pm"])
    """
    Current AM/PM mode.

    :attr:`am_pm` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'am'`.
    """

    animation_duration = NumericProperty(0.3)
    """
    Duration of the animations.

    :attr:`animation_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    animation_transition = StringProperty("out_quad")
    """
    Transition type of the animations.

    :attr:`animation_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    time = ObjectProperty(allownone=True)
    """
    Returns the current time object.

    :attr:`time` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _state = StringProperty()
    _selector = ObjectProperty()
    _time_input = ObjectProperty()
    _am_pm_selector = ObjectProperty()
    _hour_label = ObjectProperty()
    _minute_label = ObjectProperty()
    _anim_playing = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            hour=self._set_current_time,
            minute=self._set_current_time,
            am_pm=self._set_current_time,
        )
        self.theme_cls.bind(device_orientation=self._check_orienation)
        self.title = "SELECT TIME"
        # default time
        self.set_time(datetime.time(hour=12, minute=0))
        self._check_orienation()

    def _get_dial_time(self, instance):
        mode = instance.mode
        if mode == "hour":
            self.hour = instance.selected_hour
        elif mode == "minute":
            self.minute = instance.selected_minute
        else:
            raise Exception("invalid mode for MDTimePicker: " % mode)
        self._set_time_input(self.hour, self.minute)

    def _set_dial_time(self, hour, minute):
        self._selector.selected_minute = minute
        self._selector.selected_hour = hour

    def _get_time_input(self, hour, minute):
        if hour:
            self.hour = f"{int(hour):01d}"
        if minute:
            self.minute = f"{int(minute):01d}"
        self._set_dial_time(self.hour, self.minute)

    def _set_time_input(self, hour, minute):
        hour = f"{int(hour):02d}"
        minute = f"{int(minute):02d}"
        if self._state != "input":
            self._time_input.set_time([hour, minute])

    def _get_am_pm(self, selected):
        self.am_pm = selected

    def _set_am_pm(self, selected):
        self._am_pm_selector.mode = self.am_pm
        self._am_pm_selector.selected = self.am_pm

    def set_time(self, time_obj):
        """
        Manually set time dialog with the specified time.
        """

        hour = time_obj.hour
        minute = time_obj.minute
        if hour > 12:
            hour -= 12
            mode = "pm"
        else:
            mode = "am"
        hour = str(hour)
        minute = str(minute)
        self._set_time_input(hour, minute)
        self._set_dial_time(hour, minute)
        self._set_am_pm(mode)

    def get_state(self):
        """
        Returns the current state of TimePicker.
        Can be one of `portrait`, `landscape` or `input`.
        """

        return self._state

    def _get_data(self):
        try:
            result = datetime.datetime.strptime(
                f"{int(self.hour):02d}:{int(self.minute):02d} {self.am_pm}",
                "%I:%M %p",
            ).time()
            return result
        except ValueError:
            return None  # hour is zero

    def _check_orienation(self, *args, do_anim=False):
        orientation = self.theme_cls.device_orientation
        if self._state != "input" and orientation != self._state:
            self._update_pos_size(orientation, anim=do_anim)

    def _update_pos_size(self, orientation, anim=False):
        d = self.animation_duration
        # time input
        time_input_pos = (
            [dp(24), dp(368)]
            if orientation == "portrait"
            else (
                [dp(24), dp(178)]
                if orientation == "landscape"
                else [dp(24), dp(96)]
            )
        )
        if anim:
            _time_input = Animation(
                pos=time_input_pos,
                d=d,
                t=self.animation_transition,  # 80 - 8,
            )
            _time_input.start(self._time_input)
        else:
            self._time_input.pos = time_input_pos

        self._time_input.disabled = False if orientation == "input" else True
        self._time_input.size = (
            [dp(216), dp(62)] if orientation == "input" else [dp(216), dp(72)]
        )
        Clock.schedule_once(self._time_input._update_padding)

        # circular selector
        if orientation == "input":
            if self.theme_cls.device_orientation == "portrait":
                selector_pos = [dp(34), dp(-256)]
                self._selector.scale_origin = [dp(162), dp(200)]
            else:
                selector_pos = [dp(324), dp(-19)]
                self._selector.scale_origin = [dp(292), dp(109)]
        elif orientation == "portrait":
            self._selector.pos = selector_pos = [dp(36), dp(76)]
        else:
            self._selector.pos = selector_pos = [dp(304), dp(76)]

        Animation(
            pos=selector_pos,
            scale=0 if orientation == "input" else 1,
            opacity=0 if orientation == "input" else 1,
            d=d,
            t=self.animation_transition,
        ).start(self._selector)

        # AM/PM selector
        am_pm_pos = (
            [dp(252), dp(368)]
            if orientation == "portrait"
            else (
                [dp(24), dp(126)]
                if orientation == "landscape"
                else [dp(252), dp(96)]
            )
        )
        am_pm_size = (
            [dp(52), dp(80)]
            if orientation == "portrait"
            else (
                [dp(216), dp(40)]
                if orientation == "landscape"
                else [dp(48), dp(70)]
            )
        )
        if anim:
            Animation(
                pos=am_pm_pos,
                size=am_pm_size,
                d=d,
                t=self.animation_transition,
            ).start(self._am_pm_selector)
        else:
            self._am_pm_selector.pos = am_pm_pos
            self._am_pm_selector.size = am_pm_size

        self._am_pm_selector.orientation = (
            "horizontal" if orientation == "landscape" else "vertical"
        )

        # MDTimePicker
        time_picker_size = (
            [dp(328), dp(500)]
            if orientation == "portrait"
            else (
                [dp(584), dp(368)]
                if orientation == "landscape"
                else [dp(324), dp(218)]
            )
        )
        if anim:
            Animation(
                size=time_picker_size,
                d=d,
                t=self.animation_transition,
            ).start(self)
        else:
            self.size = time_picker_size

        # minute label
        Animation(
            pos=[dp(144), dp(76)],
            opacity=1 if orientation == "input" else 0,
            d=d,
            t=self.animation_transition,
        ).start(self._minute_label)

        # hour label
        Animation(
            pos=[dp(24), dp(76)],
            opacity=1 if orientation == "input" else 0,
            d=d,
            t=self.animation_transition,
        ).start(self._hour_label)

        self._state = orientation
        self.ids.input_clock_switch.icon = (
            "clock-time-four-outline" if orientation == "input" else "keyboard"
        )

    def _set_current_time(self, *args):
        self.time = self._get_data()

    def _switch_input(self):
        self._update_pos_size(
            self.theme_cls.device_orientation
            if self._state == "input"
            else "input",
            anim=True,
        )


Builder.load_string(
    """
<Tab@MDFloatLayout+MDTabsBase>
    md_bg_color: app.theme_cls.bg_normal


<ColorSelector>
    canvas:
        Color:
            rgba: root.rgb_hex(root.color_name)
        Ellipse:
            size: self.size
            pos: self.pos


<AccentColorSelector@ColorSelector>
    on_release: app.theme_cls.accent_palette = root.color_name


<PrimaryColorSelector@ColorSelector>
    on_release: app.theme_cls.primary_palette = root.color_name


<MDThemePicker>
    size_hint: None, None
    size: "284dp", "400dp"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Change theme"

        MDTabs:
            on_tab_switch: root.on_tab_switch(*args)

            Tab:
                id: theme_tab
                text: "Theme"

                MDGridLayout:
                    id: primary_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

            Tab:
                text: "Accent"

                MDGridLayout:
                    id: accent_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

            Tab:
                text: "Style"

                MDGridLayout:
                    adaptive_size: True
                    spacing: "8dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    cols: 2
                    rows: 1

                    MDIconButton:
                        canvas:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 1.
                                circle: (self.center_x, self.center_y, sp(62))

                        user_font_size: "100sp"
                        on_release: app.theme_cls.theme_style = "Light"

                    MDIconButton:
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos

                        on_release: app.theme_cls.theme_style = "Dark"
                        user_font_size: "100sp"

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()
"""
)


class ColorSelector(MDIconButton):
    color_name = OptionProperty("Indigo", options=palette)

    def rgb_hex(self, col):
        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class MDThemePicker(
    BaseDialog,
    SpecificBackgroundColorBehavior,
    FakeRectangularElevationBehavior,
):
    def on_open(self):
        self.on_tab_switch(None, self.ids.theme_tab, None, None)

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        if instance_tab.text == "Theme":
            if not self.ids.primary_box.children:
                for name_palette in palette:
                    self.ids.primary_box.add_widget(
                        Factory.PrimaryColorSelector(color_name=name_palette)
                    )
        if instance_tab.text == "Accent":
            if not self.ids.accent_box.children:
                for name_palette in palette:
                    self.ids.accent_box.add_widget(
                        Factory.AccentColorSelector(color_name=name_palette)
                    )
