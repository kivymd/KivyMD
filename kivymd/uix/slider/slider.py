"""
Components/Slider
=================

.. seealso::

    `Material Design spec, Sliders <https://m3.material.io/components/sliders/overview>`_

.. rubric:: Sliders allow users to make selections from a range of values.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider.png
    :align: center

- Sliders should present the full range of choices that are available
- Two types: continuous and discrete
- The slider should immediately reflect any input made by a user

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliders-types.png
    :align: center

1. Continuous slider
2. Discrete slider

Usage
-----

.. code-block:: python

    MDSlider(
        MDSliderHandle(
        ),
        MDSliderValueLabel(
        ),
        step=10,
        value=50,
    )

.. code-block:: kv

    MDSlider:
        step: 10
        value: 50

        MDSliderHandle:

        MDSliderValueLabel:


Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider-anatomy.png
    :align: center
"""

__all__ = ("MDSlider", "MDSliderHandle", "MDSliderValueLabel")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    VariableListProperty,
    StringProperty,
    NumericProperty,
    ObjectProperty,
    ColorProperty,
)
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

from kivymd.uix.label import MDLabel
from kivymd.uix.behaviors import (
    ScaleBehavior,
    DeclarativeBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd import uix_path
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "slider", "slider.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSlider(DeclarativeBehavior, ThemableBehavior, Slider):
    """
    Slider class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.slider.Slider`
    classes documentation.
    """

    track_active_width = NumericProperty(dp(4))
    """
    Width of the active track.

    .. versionadded:: 2.0.0

    :attr:`track_active_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    track_inactive_width = NumericProperty(dp(4))
    """
    Width of the inactive track.

    .. versionadded:: 2.0.0

    :attr:`track_inactive_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    step_point_size = NumericProperty(dp(1))
    """
    Step point size.

    .. versionadded:: 2.0.0

    :attr:`step_point_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(1)`.
    """

    track_active_color = ColorProperty(None)
    """
    Color of the active track.

    .. versionadded:: 2.0.0

    .. versionchanged:: 2.0.0

        Rename from `track_color_active` to `track_active_color`

    :attr:`track_active_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    track_active_step_point_color = ColorProperty(None)
    """
    Color of step points on active track.

    .. versionadded:: 2.0.0

    :attr:`track_active_step_point_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    track_inactive_step_point_color = ColorProperty(None)
    """
    Color of step points on inactive track.

    .. versionadded:: 2.0.0

    :attr:`track_inactive_step_point_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    track_inactive_color = ColorProperty(None)
    """
    Color of the inactive track.

    .. versionadded:: 2.0.0

    .. versionchanged:: 2.0.0

        Rename from `track_color_inactive` to `track_inactive_color`

    :attr:`track_active_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    value_container_show_anim_duration = NumericProperty(0.2)
    """
    Duration of the animation opening of the label value.

    .. versionadded:: 2.0.0

    :attr:`value_container_show_anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    value_container_hide_anim_duration = NumericProperty(0.2)
    """
    Duration of closing the animation of the label value.

    .. versionadded:: 2.0.0

    :attr:`value_container_hide_anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    value_container_show_anim_transition = StringProperty("out_circ")
    """
    The type of the opening animation of the label value.

    .. versionadded:: 2.0.0

    :attr:`value_container_show_anim_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_circ'`.
    """

    value_container_hide_anim_transition = StringProperty("out_circ")
    """
    The type of the closing animation of the label value.

    .. versionadded:: 2.0.0

    :attr:`value_container_hide_anim_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_circ'`.
    """

    handle_anim_transition = StringProperty("out_circ")
    """
    Handle animation type.

    .. versionadded:: 2.0.0

    :attr:`handle_anim_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_circ'`.
    """

    handle_anim_duration = NumericProperty(0.2)
    """
    Handle animation duration.

    .. versionadded:: 2.0.0

    :attr:`handle_anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    _value_label_container_size = ListProperty([0, 0])  # value label texture
    _value_label = ObjectProperty()  # value label texture
    _value_container = ObjectProperty()  # MDSliderValueContainer object
    _value_container_y = NumericProperty(0)  # MDSliderValueContainer object
    _handle = ObjectProperty()  # MDSliderHandle object
    # List of points displayed on the slider when using the `step` for th
    # active/inactive tracks.
    _active_points = ListProperty()
    _inactive_points = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._update_state_layer_pos, 0.5)
        Clock.schedule_once(self.on_size)

    def add_widget(self, widget, index=0, canvas=None):
        def set_value_container_y(*args):
            self._value_container_y = self.ids.handle_container.y

        if isinstance(widget, MDSliderValueLabel):
            self._value_label = widget
            self._value_container = MDSliderValueContainer(_slider=self)
            self.ids.value_container.add_widget(self._value_container)
            Clock.schedule_once(set_value_container_y)
        elif isinstance(widget, MDSliderHandle):
            widget._slider = self
            self._handle = widget
            self.ids.handle_container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def update_points(self, instance, step) -> None:
        """Draws the step points on the slider."""

        def update_points(*args):
            y = (
                self.center_y
                if self.orientation == "horizontal"
                else self.center_x
            ) - self.track_active_width / 2
            slider_length = (
                self.width if self.orientation == "horizontal" else self.height
            ) - (self.padding * 2)
            slider_max_value = int(self.max)
            multiplier = slider_length / slider_max_value
            active_track_width = (
                (
                    self.width
                    if self.orientation == "horizontal"
                    else self.height
                )
                - self.padding * 2
            ) * self.value_normalized

            for i in range(0, slider_max_value + 1, step):
                x = i * multiplier

                if x < active_track_width:
                    points = self._inactive_points
                else:
                    points = self._active_points

                if self.orientation == "vertical":
                    points.append(y)

                points.append(
                    (self.x if self.orientation == "horizontal" else self.y)
                    + x
                    + self.padding
                    + (
                        (self.ids.handle_container.width / 2)
                        if i != self.max and i
                        else 0
                    )
                )
                if self.orientation == "horizontal":
                    points.append(y)

        Clock.schedule_once(update_points)

    def on_size(self, *args) -> None:
        """Fired when the widget is resized."""

        self._update_points()

    def on_touch_down(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return
        if touch.is_mouse_scrolling:
            if "down" in touch.button or "left" in touch.button:
                if self.step:
                    self.value = min(self.max, self.value + self.step)
                else:
                    self.value = min(
                        self.max, self.value + (self.max - self.min) / 20
                    )
            if "up" in touch.button or "right" in touch.button:
                if self.step:
                    self.value = max(self.min, self.value - self.step)
                else:
                    self.value = max(
                        self.min, self.value - (self.max - self.min) / 20
                    )
        elif self.sensitivity == "handle":
            if self.children[0].collide_point(*touch.pos):
                touch.grab(self)
        else:
            touch.grab(self)
            Clock.schedule_once(self._update_state_layer_pos)
            Animation(value_pos=touch.pos, d=0.2).start(self)

        return True

    def on_value_pos(self, *args) -> None:
        """
        Fired when the `value_pos` value changes.
        Sets a new value for the value label texture.
        """

        self._update_points()

        if self._value_label and self._value_container:
            # FIXME: I do not know how else I can update the texture.
            self._value_label.text = ""
            self._value_label.text = f"{int(self.value)}"
            self._value_label.texture_update()
            label_value_rect = self._value_container.canvas.get_group(
                "md-slider-label-value-rect"
            )[0]
            label_value_rect.texture = None
            label_value_rect.texture = self._value_label.texture
            label_value_rect.size = self._value_label.texture_size

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            if self._handle:
                self._handle.on_leave()
            return True

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            if self._handle:
                self._update_state_layer_pos()
            if self._handle and not self._handle._active:
                self._handle.on_enter()
        return super().on_touch_move(touch)

    def on_handle_enter(self) -> None:
        """Scales the container of the label value."""

        if self._handle and self._value_label:
            Animation(
                scale_value_x=1,
                scale_value_y=1,
                t=self.value_container_show_anim_transition,
                d=self.value_container_show_anim_duration,
            ).start(self._value_container)
            Animation(
                _value_container_y=self.ids.handle_container.y + dp(32),
                t=self.value_container_show_anim_transition,
                d=self.value_container_show_anim_duration,
            ).start(self)

    def on_handle_leave(self) -> None:
        """Scales the container of the label value."""

        if self._handle and self._value_label:
            Animation(
                scale_value_x=0,
                scale_value_y=0,
                d=self.value_container_hide_anim_duration,
                t=self.value_container_hide_anim_transition,
            ).start(self._value_container)
            Animation(
                _value_container_y=self._value_container_y - dp(24),
                t=self.value_container_hide_anim_transition,
                d=self.value_container_hide_anim_duration,
            ).start(self)

    def _update_points(self, *args) -> None:
        if self.step:
            self._active_points = []
            self._inactive_points = []
            self.update_points(self, self.step)

    def _update_state_layer_pos(self, *args):
        if self._handle:
            self._handle.ids.state_layer.scale_value_center = (
                self.ids.handle_container.center
            )


class MDSliderHandle(
    ThemableBehavior, BackgroundColorBehavior, FocusBehavior, Widget
):
    """
    Handle class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.focus_behavior.FocusBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.
    """

    radius = VariableListProperty([dp(10)], length=4)
    """
    Handle radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(10), dp(10), dp(10), dp(10)]`.
    """

    size = ListProperty([dp(20), dp(20)])
    """
    Handle size.

    :attr:`size` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(20), dp(20)]`.
    """

    state_layer_size = ListProperty([dp(40), dp(40)])
    """
    Handle state layer size.

    :attr:`state_layer_size` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(40), dp(40)]`.
    """

    state_layer_color = ColorProperty(None)
    """
    Handle state layer color.

    :attr:`state_layer_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _slider = ObjectProperty()  # MDSlider object
    _active = False  # is the layer currently displayed
    _state_layer = ObjectProperty()  # MDSliderStateLayer object

    def on_enter(self) -> None:
        """
        Fired when mouse enter the bbox of the widget.
        Animates the display of the slider handle layer.
        """

        if self._slider:
            if self._state_layer and not self._slider.disabled:
                self._active = True
                anim = Animation(scale_value_x=1, scale_value_y=1, d=0.2)
                anim.bind(on_complete=self._slider._update_state_layer_pos)
                anim.start(self._state_layer)
            if not self._slider.disabled:
                self._slider.on_handle_enter()

    def on_leave(self) -> None:
        """
        Fired when the mouse goes outside the widget border.
        Animates the hiding of the slider handle layer.
        """

        if self._slider:
            if self._state_layer and not self._slider.disabled:
                self._active = False
                anim = Animation(scale_value_x=0, scale_value_y=0, d=0.2)
                anim.bind(on_complete=self._slider._update_state_layer_pos)
                anim.start(self._state_layer)
            if not self._slider.disabled:
                self._slider.on_handle_leave()


class MDSliderHandleStateLayer(ScaleBehavior, Widget):
    """
    Slider state layer class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.
    """

    scale_value_x = NumericProperty(0)
    """
    X-axis value.

    :attr:`scale_value_x` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_y = NumericProperty(0)
    """
    Y-axis value.

    :attr:`scale_value_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """


class MDSliderValueLabel(MDLabel):
    """
    Implements the value label.

    For more information, see in the :class:`~kivymd.uix.label.label.MDLabel`
    class documentation.

    .. versionadded:: 2.0.0
    """

    size = ListProperty([dp(36), dp(36)])
    """
    Container size for the label value.

    :attr:`handle_anim_transition` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(36), dp(36)]`.
    """


class MDSliderValueContainer(ScaleBehavior, Widget):
    """
    Implements the container for value label.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.

    .. versionadded:: 2.0.0
    """

    scale_value_x = NumericProperty(0)
    """
    X-axis value.

    :attr:`scale_value_x` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_y = NumericProperty(0)
    """
    Y-axis value.

    :attr:`scale_value_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    _slider = ObjectProperty()  # MDSlider object
