"""
Components/TimePicker
=====================

.. seealso::

    `Material Design spec, Time picker <https://material.io/components/time-pickers>`_

.. rubric:: Includes time picker.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/picker-previous.png
    :align: center

.. warning:: The widget is under testing. Therefore, we would be grateful if
    you would let us know about the bugs found.

.. rubric:: Usage

.. code-block::

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.pickers import MDTimePicker

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
    documentation in the :class:`~kivymd.uix.pickers.datepicker.datepicker.BaseDialogPicker` class.

.. code-block:: python

    time_dialog = MDTimePicker(
        primary_color=get_color_from_hex("#72225b"),
        accent_color=get_color_from_hex("#5d1a4a"),
        text_button_color=(1, 1, 1, 1),
    )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-customization.png
        :align: center
"""

__all__ = ("MDTimePicker",)

import datetime
import os
import re
import time
from typing import List, Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.event import EventDispatcher
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
from kivy.vector import Vector

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers.datepicker import BaseDialogPicker
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField

with open(
    os.path.join(uix_path, "pickers", "timepicker", "timepicker.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class AmPmSelectorLabel(ButtonBehavior, MDLabel):
    pass


class AmPmSelector(ThemableBehavior, MDBoxLayout):
    border_radius = NumericProperty()
    border_color = ColorProperty()
    bg_color = ColorProperty()
    bg_color_active = ColorProperty()
    border_width = NumericProperty()
    am = ObjectProperty()
    am = ObjectProperty()
    owner = ObjectProperty()
    text_color = ColorProperty()
    selected = StringProperty()

    _am_bg_color = ColorProperty()
    _pm_bg_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(selected=self._upadte_color)
        Clock.schedule_once(self._upadte_color)

    def _upadte_color(self, *args):
        bg_color = (
            self.owner.accent_color
            if self.owner.accent_color
            else self.bg_color_active
        )
        if self.selected == "am":
            self._am_bg_color = bg_color
            self._pm_bg_color = (
                self.owner.primary_color
                if self.owner.accent_color
                else self.bg_color
            )
        elif self.selected == "pm":
            self._am_bg_color = (
                self.owner.primary_color
                if self.owner.accent_color
                else self.bg_color
            )
            self._pm_bg_color = bg_color


class TimeInputTextField(MDTextField):
    num_type = OptionProperty("hour", options=["hour", "minute"])
    hour_regx = "^[0-9]$|^0[1-9]$|^1[0-2]$"
    minute_regx = "^[0-9]$|^0[0-9]$|^[1-5][0-9]$"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_text)
        self.register_event_type("on_select")
        self.bind(text_color_focus=self.setter("hint_text_color_normal"))

    def validate_time(self, text) -> Union[None, re.Match]:
        reg = self.hour_regx if self.num_type == "hour" else self.minute_regx
        return re.match(reg, text)

    def insert_text(self, text, from_undo=False):
        strip_text = self.text.strip()
        current_string = "".join([strip_text, text])
        if not self.validate_time(current_string):
            text = ""
        return super().insert_text(text, from_undo=from_undo)

    def set_text(self, *args) -> None:
        """
        Texts should be center aligned. Now we are setting the padding of text
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

    def on_focus(self, *args) -> None:
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

    def on_select(self, *args) -> None:
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dispatch("on_select")
            super().on_touch_down(touch)


class TimeInput(MDRelativeLayout):
    """Implements two text fields for displaying and entering a time value."""

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

    def set_time(self, time_list) -> None:
        hour, minute = time_list
        self._hour.text = hour
        self._minute.text = minute

    def get_time(self) -> List[str]:
        hour = self._hour.text.strip()
        minute = self._minute.text.strip()
        return [hour, minute]

    def on_time_input(self, *args) -> None:
        pass

    def on_minute_select(self, *args) -> None:
        pass

    def on_hour_select(self, *args) -> None:
        pass

    def _update_padding(self, *args):
        self._hour.set_text()
        self._minute.set_text()


class SelectorLabel(MDLabel):
    pass


class CircularSelector(MDCircularLayout, EventDispatcher):
    """Implements clock face display."""

    mode = OptionProperty("hour", options=["hour", "minute"])  # and military
    text_color = ColorProperty()
    selected_hour = StringProperty("12")
    selected_minute = StringProperty("0")
    selector_size = NumericProperty("48dp")
    selector_pos = ListProperty([0, 0])
    selector_color = ColorProperty()
    bg_color = ColorProperty()
    font_name = StringProperty()
    scale = NumericProperty(1)
    content_scale = NumericProperty(1)
    t = StringProperty("out_quad")
    d = NumericProperty(0.2)
    scale_origin = ListProperty([100, 100])

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
            wid.text_color = self.text_color
            if wid.text == selected:
                widget = wid
        if not widget:
            return False
        self.selector_pos = widget.center
        widget.text_color = [1, 1, 1, 1]
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
        pass

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


class MDTimePicker(BaseDialogPicker):
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

    minute_radius = VariableListProperty(dp(5), length=4)
    """
    Radius of the minute input field.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-minute-radius.png
        :align: center

    :attr:`minute_radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(5), dp(5), dp(5), dp(5)]`.
    """

    hour_radius = VariableListProperty(dp(5), length=4)
    """
    Radius of the hour input field.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-hour-radius.png
        :align: center

    :attr:`hour_radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(5), dp(5), dp(5), dp(5)]`.
    """

    am_pm_radius = NumericProperty("5dp")
    """
    Radius of the AM/PM selector.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-am-pm-radius.png
        :align: center

    :attr:`am_pm_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(5)`.
    """

    am_pm_border_width = NumericProperty("1dp")
    """
    Width of the AM/PM selector's borders.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/time-picker-am-pm-border-width.png
        :align: center

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
        if self.title == "SELECT DATE":
            self.title = "SELECT TIME"
        self.set_time(datetime.time(hour=12, minute=0))  # default time
        self._check_orienation()

    def set_time(self, time_obj) -> None:
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

    def get_state(self) -> str:
        """
        Returns the current state of TimePicker.
        Can be one of `portrait`, `landscape` or `input`.
        """

        return self._state

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

    def _set_am_pm(self, selected: str) -> None:
        """Used by set_time() to manually set the mode to "am" or "pm"."""
        self.am_pm = selected
        self._am_pm_selector.mode = self.am_pm
        self._am_pm_selector.selected = self.am_pm

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

        # Circular selector.
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

        # AM/PM selector.
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

        # MDTimePicker.
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

        # Minute label.
        Animation(
            pos=[dp(144), dp(76)],
            opacity=1 if orientation == "input" else 0,
            d=d,
            t=self.animation_transition,
        ).start(self._minute_label)

        # Hour label.
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
