"""
Components/TimePicker
=====================

.. seealso::

    `Material Design spec, Date picker <https://m3.material.io/components/time-pickers/overview>`_

.. rubric:: Time pickers help users select and set a specific time.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker.png
    :align: center

- Time pickers are modal and cover the main content
- Two types: dial and input
- Users can select hours, minutes, or periods of time
- Make sure time can easily be selected by hand on a mobile device

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-types.png
    :align: center

1. Vertical dial time picker
2. Horizontal dial time picker
3. Time picker input

KivyMD provides the following date pickers classes for use:

- MDTimePickerDialVertical_
- MDTimePickerDialHorizontal_
- MDTimePickerInput_

.. _MDTimePickerDialVertical:

MDTimePickerDialVertical
------------------------

Time pickers allow people to enter a specific time value. They’re displayed in
dialogs and can be used to select hours, minutes, or periods of time.

They can be used for a wide range of scenarios. Common use cases include:

- Setting an alarm
- Scheduling a meeting

Time pickers are not ideal for nuanced or granular time selection, such as
milliseconds for a stopwatch application.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/vertical-time-picker-preview.gif
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.pickers import MDTimePickerDialVertical

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_time_picker()

            MDButtonText:
                text: "Open time picker"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def show_time_picker(self):
            time_picker = MDTimePickerDialVertical()
            time_picker.open()


    Example().run()

.. _MDTimePickerDialHorizontal:

MDTimePickerDialHorizontal
--------------------------

The clock dial interface adapts to a device’s orientation. In landscape mode,
the stacked input and selection options are positioned side-by-side.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/horizontal-time-picker-preview.gif
    :align: center

.. code-block:: python

    def show_time_picker(self):
        MDTimePickerDialHorizontal().open()

.. note:: You must control the orientation of the time picker yourself.

.. code-block:: python

    from typing import Literal

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty

    from kivymd.app import MDApp
    from kivymd.theming import ThemeManager
    from kivymd.uix.pickers import (
        MDTimePickerDialHorizontal,
        MDTimePickerDialVertical,
    )

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release:
                app.open_time_picker_horizontal("1", "10") \
                if self.theme_cls.device_orientation == "landscape" else \
                app.open_time_picker_vertical("1", "10")

            MDButtonText:
                text: "Open time picker"
    '''


    class Example(MDApp):
        ORIENTATION = Literal["portrait", "landscape"]
        time_picker_horizontal: MDTimePickerDialHorizontal = ObjectProperty(
            allownone=True
        )
        time_picker_vertical: MDTimePickerDialHorizontal = ObjectProperty(
            allownone=True
        )

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.bind(device_orientation=self.check_orientation)
            return Builder.load_string(KV)

        def check_orientation(
            self, instance: ThemeManager, orientation: ORIENTATION
        ):
            if orientation == "portrait" and self.time_picker_horizontal:
                self.time_picker_horizontal.dismiss()
                hour = str(self.time_picker_horizontal.time.hour)
                minute = str(self.time_picker_horizontal.time.minute)
                Clock.schedule_once(
                    lambda x: self.open_time_picker_vertical(hour, minute),
                    0.1,
                )
            elif orientation == "landscape" and self.time_picker_vertical:
                self.time_picker_vertical.dismiss()
                hour = str(self.time_picker_vertical.time.hour)
                minute = str(self.time_picker_vertical.time.minute)
                Clock.schedule_once(
                    lambda x: self.open_time_picker_horizontal(hour, minute),
                    0.1,
                )

        def open_time_picker_horizontal(self, hour, minute):
            self.time_picker_vertical = None
            self.time_picker_horizontal = MDTimePickerDialHorizontal(
                hour=hour, minute=minute
            )
            self.time_picker_horizontal.open()

        def open_time_picker_vertical(self, hour, minute):
            self.time_picker_horizontal = None
            self.time_picker_vertical = MDTimePickerDialVertical(
                hour=hour, minute=minute
            )
            self.time_picker_vertical.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-control-orientation.gif
    :align: center

.. _MDTimePickerInput:

MDTimePickerInput
-----------------

Time input pickers allow people to specify a time using keyboard numbers.
This input option should be accessible from any other mobile time picker
interface by tapping the keyboard icon.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-time-picker-preview.gif
    :align: center

.. code-block:: python

    def show_time_picker(self):
        MDTimePickerInput().open()

Events
======

**on_edit** event
-----------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-edit.gif
    :align: center

.. code-block:: python

    from kivy.clock import Clock
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.pickers import MDTimePickerDialVertical, MDTimePickerInput

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_time_picker_vertical()

            MDButtonText:
                text: "Open time picker"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def on_edit_time_picker_input(self, time_picker_input):
            time_picker_input.dismiss()
            Clock.schedule_once(self.show_time_picker_vertical, 0.2)

        def show_time_picker_input(self, *args):
            time_picker_input = MDTimePickerInput()
            time_picker_input.bind(on_edit=self.on_edit_time_picker_input)
            time_picker_input.open()

        def on_edit_time_picker_vertical(self, time_picker_vertical):
            time_picker_vertical.dismiss()
            Clock.schedule_once(self.show_time_picker_input, 0.2)

        def show_time_picker_vertical(self, *args):
            time_picker_vertical = MDTimePickerDialVertical()
            time_picker_vertical.bind(on_edit=self.on_edit_time_picker_vertical)
            time_picker_vertical.open()


    Example().run()

**on_hour_select** event
------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-hour-select.gif
    :align: center

.. code-block:: python

    def on_hour_select(
        self, time_picker_vertical: MDTimePickerDialVertical, mode: str
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"On '{mode}' select",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_hour_select=self.on_hour_select)
        time_picker_vertical.open()

**on_minute_select** event
--------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-minute-select.gif
    :align: center

.. code-block:: python

    def on_minute_select(
        self, time_picker_vertical: MDTimePickerDialVertical, mode: str
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"On '{mode}' select",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_minute_select=self.on_minute_select)
        time_picker_vertical.open()

**on_am_pm** event
------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-am-pm.gif
    :align: center

.. code-block:: python

    def on_am_pm(
        self, time_picker_vertical: MDTimePickerDialVertical, am_pm: str
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"'{am_pm.upper()}' select",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_am_pm=self.on_am_pm)
        time_picker_vertical.open()

**on_selector_hour** event
--------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-selector-hour.gif
    :align: center

.. code-block:: python

    def on_selector_hour(
        self, time_picker_vertical: MDTimePickerDialVertical, hour: str
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The value of the hour is `{hour}` select",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_selector_hour=self.on_selector_hour)
        time_picker_vertical.open()

**on_selector_minute** event
----------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-selector-minute.gif
    :align: center

.. code-block:: python

    def on_selector_minute(
        self, time_picker_vertical: MDTimePickerDialVertical, minute: str
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The value of the hour is `{minute}` select",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_selector_minute=self.on_selector_minute)
        time_picker_vertical.open()

**on_cancel** event
-------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-cancel.gif
    :align: center

.. code-block:: python

    def on_cancel(
        self, time_picker_vertical: MDTimePickerDialVertical
    ):
        time_picker_vertical.dismiss()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_cancel=self.on_cancel)
        time_picker_vertical.open()

**on_ok** event
---------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-vertical-event-on-ok.gif
    :align: center

.. code-block:: python

    def on_ok(
        self, time_picker_vertical: MDTimePickerDialVertical
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"Time is `{time_picker_vertical.time}`",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_ok=self.on_ok)
        time_picker_vertical.open()

**on_time_input** event
-----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-input-event-on-time-input.gif
    :align: center

.. code-block:: python

    def on_time_input(
        self,
        time_picker_vertical: MDTimePickerInput,
        type_time: str,
        value: str,
    ):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=f"The {type_time} value is set to {value}",
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerInput()
        time_picker_vertical.bind(on_time_input=self.on_time_input)
        time_picker_vertical.open()

API break
=========

1.2.0 version
-------------

.. code-block:: python

    time_picker_dialog = MDTimePicker()
    time_picker_dialog.open()

2.0.0 version
-------------

.. code-block:: python

    # time_picker_dialog = MDTimePickerDialVertical()
    # time_picker_dialog = MDTimePickerDialHorizontal()

    time_picker_dialog = MDTimePickerInput()
    time_picker_dialog.open()
"""

# TODO: Implement 24h input.
#  Implement a tooltip for time picker elements.
#  Should we implement the feature to settings custom colors for the
#  time picker dialogs?

from __future__ import annotations

__all__ = (
    "MDBaseTimePicker",
    "MDTimePickerInput",
    "MDTimePickerDialVertical",
    "MDTimePickerDialHorizontal",
)

import datetime
import os
import re
import time
from typing import List

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
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
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.behaviors.motion_behavior import MotionTimePickerBehavior
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

with open(
    os.path.join(uix_path, "pickers", "timepicker", "timepicker.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDBaseTimePicker(ThemableBehavior, MotionTimePickerBehavior, BoxLayout):
    """
    Implements the base class of the time picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionTimePickerBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` and
    classes documentation.

    :Events:
        :attr:`on_cancel`
            Fired when the 'Cancel' button is pressed.
        :attr:`on_ok`
            Fired when the 'Ok' button is pressed.
        :attr:`on_dismiss`
            Fired when a date picker closes.
        :attr:`on_edit`
            Fired when you click on the date editing icon.
        :attr:`on_hour_select`
            Fired when the hour input field container is clicked.
        :attr:`on_minute_select`
            Fired when the minute input field container is clicked.
        :attr:`on_am_pm`
            Fired when the AP/PM switching elements are pressed.
        :attr:`on_selector_hour`
            Fired when switching the hour value in the clock face container.
        :attr:`on_selector_minute`
            Fired when switching the minute value in the clock face container.
    """

    hour = StringProperty("12")
    """
    Current hour.

    :attr:`hour` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'12'`.
    """

    minute = StringProperty("0")
    """
    Current minute.

    :attr:`minute` is an :class:`~kivy.properties.StringProperty`
    and defaults to `0`.
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

    headline_text = StringProperty("Select time")
    """
    Headline text.

    :attr:`headline_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Select time'`.
    """

    text_button_ok = StringProperty("Ok")
    """
    The text of the confirmation button.

    :attr:`text_button_ok` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Ok'`.
    """

    text_button_cancel = StringProperty("Cancel")
    """
    The text of the cancel button.

    :attr:`text_button_cancel` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Cancel'`.
    """

    radius = VariableListProperty([dp(16)], length=4)
    """
    Container radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(16), dp(16), dp(16), dp(16)]`.
    """

    is_open = BooleanProperty(False)
    """
    Is the date picker dialog open.

    :attr:`is_open` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    scrim_color = ColorProperty([0, 0, 0, 0.5])
    """
    Color for scrim in (r, g, b, a) or string format.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    _selector = ObjectProperty()
    _time_input = ObjectProperty()
    _am_pm_selector = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            hour=self._set_current_time,
            minute=self._set_current_time,
            am_pm=self._set_current_time,
        )
        self.register_event_type("on_dismiss")
        self.register_event_type("on_cancel")
        self.register_event_type("on_ok")
        self.register_event_type("on_edit")
        self.register_event_type("on_hour_select")
        self.register_event_type("on_minute_select")
        self.register_event_type("on_am_pm")
        self.register_event_type("on_selector_hour")
        self.register_event_type("on_selector_minute")
        self.register_event_type("on_time_input")
        Clock.schedule_once(
            lambda x: self.set_time(
                datetime.time(hour=int(self.hour), minute=int(self.minute))
            )
        )  # default time

    def set_time(self, time_obj: datetime.time) -> None:
        """Manually set time dialog with the specified time."""

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
        self._set_current_time()

    def open(self) -> None:
        """Show the dialog time picker."""

        if not self.is_open:
            if not self._scrim:
                self._scrim = MDTimePickerScrim(color=self.scrim_color)

            Window.add_widget(self._scrim)
            Window.add_widget(self)
            super().on_open()
            self.is_open = True

    def _get_dial_time(self, instance):
        mode = instance.mode
        if mode == "hour":
            self.hour = instance.selected_hour
            self.dispatch("on_selector_hour", self.hour)
        elif mode == "minute":
            self.minute = instance.selected_minute
            self.dispatch("on_selector_minute", self.minute)
        else:
            raise Exception("invalid mode for MDTimePicker: " % mode)

        self._set_time_input(self.hour, self.minute)

    def _set_dial_time(self, hour, minute):
        if self._selector:
            self._selector.selected_minute = minute
            self._selector.selected_hour = hour
        else:
            self.hour, self.minute = hour, minute
            self._set_current_time()

    def _get_time_input(self, hour, minute):
        if hour:
            self.hour = f"{int(hour):01d}"
            self.dispatch("on_time_input", "hour", self.hour)
        if minute:
            self.minute = f"{int(minute):01d}"
            self.dispatch("on_time_input", "minute", self.minute)

        self._set_dial_time(self.hour, self.minute)

    def _set_time_input(self, hour, minute):
        hour = f"{int(hour):02d}"
        minute = f"{int(minute):02d}"

        if self._time_input:
            self._time_input.set_time([hour, minute])

    def _get_am_pm(self, selected):
        self.am_pm = selected

    def _set_am_pm(self, selected: str) -> None:
        """Used by set_time() to manually set the mode to "am" or "pm"."""

        self.am_pm = selected
        self._am_pm_selector.mode = self.am_pm
        self._am_pm_selector.selected = self.am_pm

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            self.dismiss()
            return True
        super().on_touch_down(touch)
        return True

    def dismiss(self, *args) -> None:
        """Dismiss the dialog time picker."""

        super().on_dismiss()
        self.is_open = False

    def on_dismiss(self, *args) -> None:
        """Fired when a time picker closes."""

    def on_cancel(self, *args) -> None:
        """Fired when the 'Cancel' button is pressed."""

    def on_ok(self, *args) -> None:
        """Fired when the 'Ok' button is pressed."""

    def on_hour_select(self, *args) -> None:
        """Fired when the hour input field container is clicked."""

    def on_minute_select(self, *args) -> None:
        """Fired when the minute input field container is clicked."""

    def on_am_pm(self, *args) -> None:
        """Fired when the AP/PM switching elements are pressed."""

    def on_edit(self, *args) -> None:
        """Fired when you click on the time editing icon."""

    def on_selector_hour(self, *args) -> None:
        """Fired when switching the hour value in the clock face container."""

    def on_selector_minute(self, *args) -> None:
        """
        Fired when switching the minute value in the clock face container.
        """

    def on_time_input(self, *args) -> None:
        """
        Fired when switching the minute value in the clock face container.
        """

    def _get_data(self):
        try:
            if time.strftime("%p"):
                result = datetime.datetime.strptime(
                    f"{int(self.hour):02d}:{int(self.minute):02d} {self.am_pm}",
                    "%I:%M %p",
                ).time()
            else:
                result = datetime.datetime.strptime(
                    f"{int(self.hour):02d}:{int(self.minute):02d}",
                    "%I:%M",
                ).time()
            return result
        except ValueError:
            return None  # hour is zero

    def _set_current_time(self, *args):
        self.time = self._get_data()


###############################################################################
#
#                                 PICKER CLASSES
#
###############################################################################


class MDTimePickerInput(CommonElevationBehavior, MDBaseTimePicker):
    """
    Implements input time picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseTimePicker`
    classes documentation.
    """


class MDTimePickerDialVertical(CommonElevationBehavior, MDBaseTimePicker):
    """
    Implements vertical time picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseTimePicker`
    classes documentation.
    """


class MDTimePickerDialHorizontal(CommonElevationBehavior, MDBaseTimePicker):
    """
    Implements horizontal time picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseTimePicker`
    classes documentation.
    """


###############################################################################
#
#                                COMMON CLASSES
#
###############################################################################


class MDTimePickerCircularSelectorLabel(MDLabel):
    """
    Implements a label for the :class:`~MDTimePickerCircularSelector` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """


class MDTimePickerCircularSelector(ThemableBehavior, MDCircularLayout):
    """
    Implements clock face display.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ThemableBehavior` and
    :class:`~kivymd.uix.circularlayout.MDCircularLayout`
    classes documentation.
    """

    mode = OptionProperty("hour", options=["hour", "minute"])  # and military
    selected_hour = StringProperty("12")
    selected_minute = StringProperty("0")
    selector_size = NumericProperty("48dp")
    selector_pos = ListProperty([0, 0])
    font_name = StringProperty()
    scale = NumericProperty(1)
    content_scale = NumericProperty(1)
    t = StringProperty("out_quad")
    d = NumericProperty(0.2)
    scale_origin = ListProperty([100, 100])

    time_picker: MDBaseTimePicker = ObjectProperty()
    """
    Time picker object -

    :attr:`time_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _centers_pos = ListProperty()

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

    def set_selector(self, selected) -> bool:
        """Sets the selector's position towards the given text."""

        widget = None
        for wid in self.children:
            wid.text_color = self.theme_cls.onSurfaceColor
            if wid.text == selected:
                widget = wid
        if not widget:
            return False
        self.selector_pos = widget.center
        widget.text_color = self.theme_cls.onPrimaryColor
        self.dispatch("on_selector_change")
        return True

    def set_time(self, selected) -> None:
        if self.mode == "hour":
            self.selected_hour = selected
        elif self.mode == "minute":
            self.selected_minute = selected

    def update_time(self, *args) -> None:
        if self.mode == "hour":
            self.set_selector(self.selected_hour)
        elif self.mode == "minute":
            self.set_selector(self.selected_minute)

    def get_selected(self) -> str:
        return self.selected

    def switch_mode(self, mode) -> None:
        if mode != self.mode:
            self.mode = mode

        if self.mode == "hour":
            self.time_picker.dispatch("on_hour_select", self.mode)
        elif self.mode == "minute":
            self.time_picker.dispatch("on_minute_select", self.mode)

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

    def on_selector_change(self, *args):
        ...

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
            label = MDTimePickerCircularSelectorLabel(
                text=f"{x}",
            )
            if i % step != 0:
                label.opacity = 0
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


class MDTimePickerScrim(Widget):
    """
    Implements scrim for the time picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.widget.Widget` and class documentation.
    """

    color = ColorProperty(None)
    alpha = NumericProperty(0)


class MDTimePickerButtonsContainer(BoxLayout):
    """
    Implements a container with buttons for time picker dialogs.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    icon = StringProperty("keyboard")
    """
    The leading container icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'keyboard'`.
    """

    time_picker: MDBaseTimePicker = ObjectProperty()
    """
    Time picker object -

    :attr:`time_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """


class MDTimePickerAmPmSelectorLabel(ButtonBehavior, MDLabel):
    """
    Implements a label for the :class:`~MDTimePickerAmPmSelector` class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDLabel`
    classes documentation.
    """


class MDTimePickerAmPmSelector(
    ThemableBehavior, BackgroundColorBehavior, BoxLayout
):
    """
    Implements a container for AM/PM switching elements.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    selected = StringProperty()
    """
    Time type status - AM/PM.
    Real value - 'am/pm'

    :attr:`selected` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """


class MDTimePickerInputContainer(BoxLayout):
    """
    Implements a container for the hours and minutes text input fields.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    time_picker: MDBaseTimePicker = ObjectProperty()
    """
    Time picker object -

    :attr:`time_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    state = OptionProperty("hour", options=["hour", "minute"])
    """
    Container status: entering hours or minutes.
    Available options are: 'hour', 'minute'.

    :attr:`state` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'hour'`.
    """

    # State of the text fields for entering hours/minutes.
    _readonly = BooleanProperty(True)
    # MDTimePickerInputTextField objects.
    _hour = ObjectProperty()
    _minute = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_time_input")
        self.register_event_type("on_hour_select")
        self.register_event_type("on_minute_select")

    def set_time(self, time_list) -> None:
        hour, minute = time_list
        self._hour.text = hour
        self._minute.text = minute

    def get_time(self) -> List[str]:
        hour = self._hour.text.strip()
        minute = self._minute.text.strip()
        return [hour, minute]

    def on_time_input(self, *args) -> None:
        ...

    def on_minute_select(self, *args) -> None:
        pass

    def on_hour_select(self, *args) -> None:
        pass


class MDTimePickerInputTextField(MDTextField):
    """
    Implements a text field for entering hour and minute values.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.textfield.textfield.MDTextField` class documentation.
    """

    num_type = OptionProperty("hour", options=["hour", "minute"])
    hour_regx = "^[0-9]$|^0[1-9]$|^1[0-2]$"
    minute_regx = "^[0-9]$|^0[0-9]$|^[1-5][0-9]$"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_select")
        Clock.schedule_once(self._override_properties, 0)

    def validate_time(self, text) -> None | re.Match:
        reg = self.hour_regx if self.num_type == "hour" else self.minute_regx
        return re.match(reg, text)

    def insert_text(self, text, from_undo=False):
        """
        Insert new text at the current cursor position. Override this
        function in order to pre-process text for input validation.
        """

        strip_text = self.text.strip()
        current_string = "".join([strip_text, text])
        if not self.validate_time(current_string):
            text = ""
        return super().insert_text(text, from_undo=from_undo)

    def set_text(self, instance, text: str) -> None:
        """
        Just override the method since its work in this class is not needed.
        """

    def on_focus(self, *args) -> None:
        """Fired when the `focus` value changes."""

        super().on_focus(*args)
        Clock.schedule_once(self._override_properties, -1)

        if self.text.strip():
            if (
                not self.focus
                and int(self.text) == 0
                and self.num_type == "hour"
            ):
                self.text = "12"
        else:
            self.text = "12" if self.num_type == "hour" else "00"

    def on_select(self, *args) -> None:
        """Fired when the hour/minute input field container is clicked."""

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dispatch("on_select")
            return super().on_touch_down(touch)

    def _override_properties(self, *args):
        if self.readonly:
            self.canvas.before.get_group("rectangle-cursor-blink")[0].size = (
                0,
                0,
            )

        self.canvas.before.get_group("active-indicator-color")[0].rgba = (
            0,
            0,
            0,
            0,
        )
        self.canvas.before.get_group("fill-color-rounded-rectangle")[
            0
        ].radius = [
            dp(12),
        ]
