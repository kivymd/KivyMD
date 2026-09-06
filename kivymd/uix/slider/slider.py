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

.. tabs::

    .. tab:: Declarative Python style

        .. code-block:: python

            MDSlider(
                MDSliderHandle(
                    ...
                ),
                MDSliderValueLabel(
                    ...
                ),
                step=10,
                value=50,
            )

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDSlider:
                step: 10
                value: 50

                MDSliderHandle:
                    ...

                MDSliderValueLabel:
                    ....

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider-anatomy.png
    :align: center

IOS Slider
----------

.. seealso::

    `Human Interface Guidelines, Sliders <https://developer.apple.com/design/human-interface-guidelines/sliders>`_

.. rubric:: A slider is a horizontal track with a control, called a thumb,
    that people can adjust between a minimum and maximum value.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ios-components-slider-intro.png
    :align: center

IOS Usage
---------

.. tabs::

    .. tab:: Declarative Python style

        .. code-block:: python

            bg_image = FitImage(source="bg.png")
            MDScreen(
                bg_image,
                IOSSlider(
                    min=0,
                    max=100,
                    value=45,
                    target_background=bg_image,
                ),
            )

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDScreen:

                FitImage:
                    id: bg_image
                    source: "bg.png"

                IOSSlider:
                    min: 0
                    max: 100
                    value: 45
                    target_background: bg_image
"""

__all__ = (
    # MD.
    "MDSlider",
    "MDSliderHandle",
    "MDSliderValueLabel",
    # IOS.
    "IOSSlider",
)

import os

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
    VariableListProperty,
)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
    IOSGlassBehavior,
    ScaleBehavior,
)
from kivymd.uix.behaviors.focus_behavior import StateFocusBehavior
from kivymd.uix.label import MDLabel

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
            ) - self.padding * 2
            slider_max_value = int(self.max)
            multiplier = (
                slider_length / slider_max_value if slider_max_value > 0 else 0
            )
            active_track_width = (
                (
                    self.width
                    if self.orientation == "horizontal"
                    else self.height
                )
                - self.padding * 2
            ) * self.value_normalized

            step_int = max(1, int(step)) if step > 0 else 1

            for i in range(0, slider_max_value + 1, step_int):
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
                        self.ids.handle_container.width / 2
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
    ThemableBehavior, BackgroundColorBehavior, StateFocusBehavior, Widget
):
    """
    Handle class.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.focus_behavior.StateFocusBehavior` and
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


# ------------------------------------ IOS ------------------------------------


class IOSSliderThumb(IOSGlassBehavior, ThemableBehavior, FloatLayout):
    """
    Thumb widget with glassmorphism visual effect for :class:`~IOSSlider`.

    .. versionadded:: 2.0.1
    """

    _color = ColorProperty(None)  # internal color of the thumb
    # Press factor controlling glass refraction adjustments
    # (0.0 for released, 1.0 for pressed).
    _press_factor = NumericProperty(0.0)

    def on_pos(self, *args) -> None:
        """
        Position change event handler. Updates corner radius and syncs shader
        FBO.
        """

        self.border_radius = [self.height / 2.0] * 4
        self._sync_glass()

    def on_size(self, *args) -> None:
        """
        Size change event handler. Recalculates border radius to maintain
        circular/oval shape.
        """

        self.border_radius = [self.height / 2.0] * 4
        self._sync_glass()

    def _sync_glass(self):
        """Forces an update of the FBO blur shader matrix and texture."""

        if hasattr(self, "_on_bg_update"):
            self._on_bg_update()


class IOSSlider(DeclarativeBehavior, ThemableBehavior, FloatLayout):
    """
    iOS-style Liquid Glass Slider with animated thumb expansion on touch
    interaction.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.floatLayout.FloatLayout`
    classes documentation.
    """

    min = NumericProperty(0.0)
    """
    Minimum value of the slider.

    :attr:`min` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    max = NumericProperty(100.0)
    """
    Maximum value of the slider.

    :attr:`max` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `100.0`.
    """

    value = NumericProperty(0.0)
    """
    Current value of the slider.

    :attr:`value` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    step = NumericProperty(0.0)
    """
    Step size for value increments. If `0`, value changes continuously.

    :attr:`step` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    orientation = OptionProperty(
        "horizontal", options=["horizontal", "vertical"]
    )
    """
    Slider orientation. Available options are: `'horizontal'`, `'vertical'`.

    :attr:`orientation` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'horizontal'`.
    """

    disabled = BooleanProperty(False)
    """
    Disables touch interaction with the slider when set to `True`.

    :attr:`disabled` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    disable_animation = BooleanProperty(False)
    """
    Disables thumb expansion animations on press.

    :attr:`disable_animation` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    target_background = ObjectProperty(None)
    """
    Target widget captured for background sampling and glass effect rendering.

    :attr:`target_background` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    track_height = NumericProperty(dp(6))
    """
    Thickness of the slider track line.

    :attr:`track_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(6)`.
    """

    padding = NumericProperty(dp(16))
    """
    Padding along the slider track edges to keep the thumb within bounds.

    :attr:`padding` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(16)`.
    """

    thumb_width = NumericProperty(dp(42))
    """
    Default width of the thumb in idle state.

    :attr:`thumb_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(28)`.
    """

    thumb_height = NumericProperty(dp(28))
    """
    Default height of the thumb in idle state.

    :attr:`thumb_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(28)`.
    """

    pressed_expansion_width = NumericProperty(dp(10))
    """
    Delta increase in thumb width when pressed.

    :attr:`pressed_expansion_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(10)`.
    """

    pressed_expansion_height = NumericProperty(dp(4))
    """
    Delta increase in thumb height when pressed.

    :attr:`pressed_expansion_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    track_active_color = ColorProperty(None)
    """
    Color of the active (filled) section of the track.

    :attr:`track_active_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    track_inactive_color = ColorProperty(None)
    """
    Color of the inactive (unfilled) section of the track.

    :attr:`track_inactive_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    thumb_color = ColorProperty(None)
    """
    Base color tint of the thumb.

    :attr:`thumb_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    thumb_color_disabled = ColorProperty(None)
    """
    Color tint of the thumb when disabled (`disabled=True`).

    :attr:`thumb_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    value_normalized = NumericProperty(0.0)
    """
    Normalized slider value in range `0.0` to `1.0`.

    :attr:`value_normalized` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    value_pos = ObjectProperty((0, 0))
    """
    Absolute coordinates `(x, y)` of the thumb center in canvas space.

    :attr:`value_pos` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `(0, 0)`.
    """

    lens_power = NumericProperty(0.08)
    """
    Thumb magnification power at the center of the lens.

    :attr:`lens_power` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.08`.
    """

    bevel_power = NumericProperty(0.15)
    """
    Thumb light refraction power at the bevel/edges.

    :attr:`bevel_power` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    glass_color = ColorProperty([1.0, 1.0, 1.0, 0.15])
    """
    Thumb tint color of the glass in (r, g, b, a) format.

    :attr:`glass_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1.0, 1.0, 1.0, 0.15]`.
    """

    blur_amount = NumericProperty(3.0)
    """
    Thumb amount of background blur applied inside the glass widget.

    :attr:`blur_amount` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `14.0`.
    """

    _thumb_w = NumericProperty(dp(42))
    _thumb_h = NumericProperty(dp(28))
    _thumb_x = NumericProperty(0)
    _thumb_y = NumericProperty(0)

    def __init__(self, **kwargs):
        self._touch_dragging = False
        super().__init__(**kwargs)

        self.bind(
            value=self._update_value_normalized,
            min=self._update_value_normalized,
            max=self._update_value_normalized,
            value_normalized=self._update_value_pos,
            size=self._update_value_pos,
            pos=self._update_value_pos,
            padding=self._update_value_pos,
            value_pos=self._update_thumb_layout,
            lens_power=self._apply_thumb_properties,
            bevel_power=self._apply_thumb_properties,
            blur_amount=self._apply_thumb_properties,
            glass_color=self._apply_thumb_properties,
            _thumb_w=self._update_thumb_layout,
            _thumb_h=self._update_thumb_layout,
        )

        Clock.schedule_once(lambda dt: self._apply_thumb_properties())
        Clock.schedule_once(lambda dt: self._sync_thumb())

    def on_touch_down(self, touch):
        if self.disabled or not self.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        touch.grab(self)
        self._touch_dragging = True
        self._update_touch_value(touch)

        if not self.disable_animation:
            self._animate_press()
        else:
            self._sync_thumb_dimensions(pressed=True)

        return True

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self._update_touch_value(touch)

            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self._touch_dragging = False

            if not self.disable_animation:
                self._animate_release()
            else:
                self._sync_thumb_dimensions(pressed=False)

            return True

        return super().on_touch_up(touch)

    def _update_touch_value(self, touch):
        """
        Calculates normalized and discrete slider values based on touch
        coordinates.
        """

        if self.orientation == "horizontal":
            padded_width = self.width - self.padding * 2

            if padded_width <= 0:
                return

            val_norm = (touch.x - (self.x + self.padding)) / padded_width
        else:
            padded_height = self.height - self.padding * 2

            if padded_height <= 0:
                return

            val_norm = (touch.y - (self.y + self.padding)) / padded_height

        self.value_normalized = max(0.0, min(1.0, val_norm))
        val = self.min + self.value_normalized * (self.max - self.min)

        if self.step > 0:
            val = round((val - self.min) / self.step) * self.step + self.min

        self.value = max(self.min, min(self.max, val))

    def _update_value_normalized(self, *args):
        """
        Recalculates normalized value on `value`, `min`, or `max` changes.
        """

        if self.max == self.min:
            self.value_normalized = 0
        else:
            val = max(self.min, min(self.max, self.value))
            self.value_normalized = (val - self.min) / (self.max - self.min)

    def _update_value_pos(self, *args):
        """
        Updates central coordinates (`value_pos`) based on normalized value.
        """

        if self.orientation == "horizontal":
            x = (
                self.x
                + self.padding
                + (self.width - self.padding * 2) * self.value_normalized
            )
            y = self.y + self.height / 2.0
        else:
            x = self.x + self.width / 2.0
            y = (
                self.y
                + self.padding
                + (self.height - self.padding * 2) * self.value_normalized
            )

        self.value_pos = (x, y)

    def _update_thumb_layout(self, *args):
        """
        Updates bottom-left corner offset of thumb and triggers glass
        re-render.
        """

        self._thumb_x = self.value_pos[0] - self._thumb_w / 2.0
        self._thumb_y = self.value_pos[1] - self._thumb_h / 2.0

        thumb = self.ids.get("ios_thumb")

        if thumb:
            thumb._sync_glass()

    def _get_normal_size(self):
        """Returns `(width, height)` tuple for idle state."""

        return self.thumb_width, self.thumb_height

    def _get_expanded_size(self):
        """Returns `(width, height)` tuple for pressed state."""

        norm_w, norm_h = self._get_normal_size()
        return (
            norm_w + self.pressed_expansion_width,
            norm_h + self.pressed_expansion_height,
        )

    def _animate_press(self):
        """
        Triggers parallel animations for thumb dimension expansion and glass
        refraction factor.
        """

        thumb = self.ids.get("ios_thumb")

        if not thumb:
            return

        Animation.stop_all(self, "_thumb_w", "_thumb_h")
        Animation.stop_all(thumb, "_press_factor")

        exp_w, exp_h = self._get_expanded_size()

        anim_slider = Animation(
            _thumb_w=exp_w, _thumb_h=exp_h, d=0.14, t="out_quad"
        )
        anim_glass = Animation(_press_factor=1.0, d=0.14, t="out_quad")

        anim_slider.bind(on_progress=lambda *a: thumb._sync_glass())

        anim_slider.start(self)
        anim_glass.start(thumb)

    def _animate_release(self):
        """
        Triggers smooth restoration of thumb dimensions back to idle state.
        """

        thumb = self.ids.get("ios_thumb")

        if not thumb:
            return

        Animation.stop_all(self, "_thumb_w", "_thumb_h")
        Animation.stop_all(thumb, "_press_factor")

        norm_w, norm_h = self._get_normal_size()

        anim_slider = Animation(
            _thumb_w=norm_w, _thumb_h=norm_h, d=0.2, t="out_quad"
        )
        anim_glass = Animation(_press_factor=0.0, d=0.2, t="out_quad")

        anim_slider.bind(on_progress=lambda *a: thumb._sync_glass())

        anim_slider.start(self)
        anim_glass.start(thumb)

    def _sync_thumb(self):
        """Synchronizes initial thumb dimensions without animation."""

        self._sync_thumb_dimensions(pressed=False)

    def _sync_thumb_dimensions(self, pressed=False):
        """
        Instantly updates thumb dimensions and `_press_factor` without
        animating.
        """

        thumb = self.ids.get("ios_thumb")

        if not thumb:
            return

        Animation.stop_all(self, "_thumb_w", "_thumb_h")
        Animation.stop_all(thumb, "_press_factor")

        w, h = self._get_expanded_size() if pressed else self._get_normal_size()
        self._thumb_w = w
        self._thumb_h = h

        thumb._press_factor = 1.0 if pressed else 0.0
        thumb._sync_glass()

    def _apply_thumb_properties(self, *args):
        """
        Passes custom lens and glass refraction kwargs to the
        :class:`~IOSSliderThumb` instance."""

        thumb = self.ids.get("ios_thumb")

        if thumb:
            thumb.lens_power = self.lens_power
            thumb.bevel_power = self.bevel_power
            thumb.blur_amount = self.blur_amount
            thumb.glass_color = self.glass_color
            thumb._sync_glass()
