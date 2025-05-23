"""
Behaviors/Ripple
================

.. rubric:: Classes implements a circular and rectangular ripple effects.

To create a widget with сircular ripple effect, you must create a new class
that inherits from the :class:`~CircularRippleBehavior` class.

For example, let's create an image button with a circular ripple effect:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior
    from kivy.uix.image import Image

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import CircularRippleBehavior

    KV = '''
    MDScreen:

        CircularRippleButton:
            source: "data/logo/kivy-icon-256.png"
            size_hint: None, None
            size: "250dp", "250dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
        def __init__(self, **kwargs):
            self.ripple_scale = 0.85
            super().__init__(**kwargs)


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-ripple-effect.gif
    :align: center

To create a widget with rectangular ripple effect, you must create a new class
that inherits from the :class:`~RectangularRippleBehavior` class:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior

    KV = '''
    MDScreen:

        RectangularRippleButton:
            size_hint: None, None
            size: "250dp", "50dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class RectangularRippleButton(
        RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior
    ):
        md_bg_color = [0, 0, 1, 1]


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-ripple-effect.gif
    :align: center
"""

__all__ = (
    "CommonRipple",
    "RectangularRippleBehavior",
    "CircularRippleBehavior",
)

from typing import NoReturn

from kivy.animation import Animation
from kivy.graphics import (
    Color,
    Ellipse,
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.behaviors import ToggleButtonBehavior


class CommonRipple:
    """Base class for ripple effect."""

    ripple_rad_default = NumericProperty(1)
    """
    The starting value of the radius of the ripple effect.

    .. code-block:: kv

        CircularRippleButton:
            ripple_rad_default: 100

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-rad-default.gif
       :align: center

    :attr:`ripple_rad_default` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    ripple_color = ColorProperty(None)
    """
    Ripple color in (r, g, b, a) format.

    .. code-block:: kv

        CircularRippleButton:
            ripple_color: app.theme_cls.primary_color

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-color.gif
       :align: center

    :attr:`ripple_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_alpha = NumericProperty(0.5)
    """
    Alpha channel values for ripple effect.

    .. code-block:: kv

        CircularRippleButton:
            ripple_alpha: .9
            ripple_color: app.theme_cls.primary_color

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-alpha.gif
       :align: center

    :attr:`ripple_alpha` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    ripple_scale = NumericProperty(None)
    """
    Ripple effect scale.

    .. code-block:: kv

        CircularRippleButton:
            ripple_scale: .5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-scale-05.gif
       :align: center

    .. code-block:: kv

        CircularRippleButton:
            ripple_scale: 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-scale-1.gif
       :align: center

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    ripple_duration_in_fast = NumericProperty(0.3)
    """
    Ripple duration when touching to widget.

    .. code-block:: kv

        CircularRippleButton:
            ripple_duration_in_fast: .1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-duration-in-fast.gif
       :align: center

    :attr:`ripple_duration_in_fast` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    ripple_duration_in_slow = NumericProperty(2)
    """
    Ripple duration when long touching to widget.

    .. code-block:: kv

        CircularRippleButton:
            ripple_duration_in_slow: 5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-duration-in-slow.gif
       :align: center

    :attr:`ripple_duration_in_slow` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    ripple_duration_out = NumericProperty(0.3)
    """
    The duration of the disappearance of the wave effect.

    .. code-block:: kv

        CircularRippleButton:
            ripple_duration_out: 5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-duration-out.gif
       :align: center

    :attr:`ripple_duration_out` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    ripple_canvas_after = BooleanProperty(True)
    """
    The ripple effect is drawn above/below the content.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDIconButton:
            ripple_canvas_after: True
            icon: "android"
            ripple_alpha: .8
            ripple_color: app.theme_cls.primary_color
            icon_size: "100sp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-canvas-after-true.gif
       :align: center

    .. code-block:: kv

        MDIconButton:
            ripple_canvas_after: False
            icon: "android"
            ripple_alpha: .8
            ripple_color: app.theme_cls.primary_color
            icon_size: "100sp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-canvas-after-false.gif
       :align: center

    :attr:`ripple_canvas_after` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    ripple_func_in = StringProperty("out_quad")
    """
    Type of animation for ripple in effect.

    :attr:`ripple_func_in` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    ripple_func_out = StringProperty("out_quad")
    """
    Type of animation for ripple out effect.

    :attr:`ripple_func_out` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'ripple_func_out'`.
    """

    ripple_effect = BooleanProperty(True)
    """
    Should I use the ripple effect.

    :attr:`ripple_effect` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    _ripple_rad = NumericProperty()
    _doing_ripple = BooleanProperty(False)
    _finishing_ripple = BooleanProperty(False)
    _fading_out = BooleanProperty(False)
    _round_rad = ListProperty([0, 0, 0, 0])

    def lay_canvas_instructions(self) -> NoReturn:
        raise NotImplementedError

    def start_ripple(self) -> None:
        if not self._doing_ripple:
            self._doing_ripple = True
            anim = Animation(
                _ripple_rad=self.finish_rad,
                t="linear",
                duration=self.ripple_duration_in_slow,
            )
            anim.bind(on_complete=self.fade_out)
            anim.start(self)

    def finish_ripple(self) -> None:
        if self._doing_ripple and not self._finishing_ripple:
            self._finishing_ripple = True
            self._doing_ripple = False
            Animation.cancel_all(self, "_ripple_rad")
            anim = Animation(
                _ripple_rad=self.finish_rad,
                t=self.ripple_func_in,
                duration=self.ripple_duration_in_fast,
            )
            anim.bind(on_complete=self.fade_out)
            anim.start(self)

    def fade_out(self, *args) -> None:
        rc = self.ripple_color
        if not self._fading_out:
            self._fading_out = True
            Animation.cancel_all(self, "ripple_color")
            anim = Animation(
                ripple_color=[rc[0], rc[1], rc[2], 0.0],
                t=self.ripple_func_out,
                duration=self.ripple_duration_out,
            )
            anim.bind(on_complete=self.anim_complete)
            anim.start(self)

    def anim_complete(self, *args) -> None:
        """Fired when the "fade_out" animation complete."""

        self._doing_ripple = False
        self._finishing_ripple = False
        self._fading_out = False

        if not self.ripple_canvas_after:
            canvas = self.canvas.before
        else:
            canvas = self.canvas.after

        canvas.remove_group("circular_ripple_behavior")
        canvas.remove_group("rectangular_ripple_behavior")

    def on_touch_down(self, touch):
        # FIXME: in fact, the output of the super method is extra.
        #  But without this, the list (`ScrollView`) placed in the `MDCard`
        #  widget will not scroll.
        super().on_touch_down(touch)
        if touch.is_mouse_scrolling:
            return False
        if not self.collide_point(touch.x, touch.y):
            return False
        if not self.disabled:
            self.call_ripple_animation_methods(touch)
            # FIXME: this check is needed for the `MDTabsLabel` object.
            #  With the normal `return True`, events for tabs from the `MDTabs`
            #  class are not processed.
            #  There may be problems with other widgets.
            #  Status: requires check.
            if isinstance(self, ToggleButtonBehavior):
                return super().on_touch_down(touch)
            else:
                return True

    def call_ripple_animation_methods(self, touch) -> None:
        if self._doing_ripple:
            Animation.cancel_all(
                self, "_ripple_rad", "ripple_color", "rect_color"
            )
            self.anim_complete()
        self._ripple_rad = self.ripple_rad_default
        self.ripple_pos = (touch.x, touch.y)

        if self.ripple_color:
            pass
        elif hasattr(self, "theme_cls"):
            self.ripple_color = self.theme_cls.rippleColor
        else:
            # If no theme, set Gray 300.
            self.ripple_color = [
                0.8784313725490196,
                0.8784313725490196,
                0.8784313725490196,
                self.ripple_alpha,
            ]
        self.ripple_color[3] = self.ripple_alpha
        self.lay_canvas_instructions()
        self.finish_rad = max(self.width, self.height) * self.ripple_scale
        self.start_ripple()

    def on_touch_move(self, touch, *args):
        if not self.collide_point(touch.x, touch.y):
            if not self._finishing_ripple and self._doing_ripple:
                self.finish_ripple()
        return super().on_touch_move(touch, *args)

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y) and self._doing_ripple:
            self.finish_ripple()
        return super().on_touch_up(touch)

    def _set_ellipse(self, instance, value):
        self.ellipse.size = (self._ripple_rad, self._ripple_rad)

    # Adjust ellipse pos here

    def _set_color(self, instance, value):
        self.col_instruction.a = value[3]


class RectangularRippleBehavior(CommonRipple):
    """
    Class implements a rectangular ripple effect.

    For more information, see in the :class:`~kivymd.uix.behavior.CommonRipple`
    class documentation.
    """

    ripple_scale = NumericProperty(2.75)
    """
    See :class:`~CommonRipple.ripple_scale`.

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.75`.
    """

    def lay_canvas_instructions(self) -> None:
        """
        Adds graphic instructions to the canvas to implement ripple animation.
        """

        if not self.ripple_effect:
            return

        with (
            self.canvas.after
            if self.ripple_canvas_after
            else self.canvas.before
        ):
            if hasattr(self, "radius"):
                if isinstance(self.radius, (float, int)):
                    self.radius = [
                        self.radius,
                    ]
                self._round_rad = self.radius
            StencilPush(group="rectangular_ripple_behavior")
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=self._round_rad,
                group="rectangular_ripple_behavior",
            )
            StencilUse(group="rectangular_ripple_behavior")
            self.col_instruction = Color(
                rgba=self.ripple_color, group="rectangular_ripple_behavior"
            )
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.ripple_pos[0] - self._ripple_rad / 2.0,
                    self.ripple_pos[1] - self._ripple_rad / 2.0,
                ),
                group="rectangular_ripple_behavior",
            )
            StencilUnUse(group="rectangular_ripple_behavior")
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=self._round_rad,
                group="rectangular_ripple_behavior",
            )
            StencilPop(group="rectangular_ripple_behavior")
        self.bind(ripple_color=self._set_color, _ripple_rad=self._set_ellipse)

    def _set_ellipse(self, instance, value):
        super()._set_ellipse(instance, value)
        self.ellipse.pos = (
            self.ripple_pos[0] - self._ripple_rad / 2.0,
            self.ripple_pos[1] - self._ripple_rad / 2.0,
        )


class CircularRippleBehavior(CommonRipple):
    """
    Class implements a circular ripple effect.

    For more information, see in the :class:`~kivymd.uix.behavior.CommonRipple`
    class documentation.
    """

    ripple_scale = NumericProperty(1)
    """
    See :class:`~CommonRipple.ripple_scale`.

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def lay_canvas_instructions(self) -> None:
        if not self.ripple_effect:
            return

        with (
            self.canvas.after
            if self.ripple_canvas_after
            else self.canvas.before
        ):
            StencilPush(group="circular_ripple_behavior")
            self.stencil = Ellipse(
                size=(
                    self.width * self.ripple_scale,
                    self.height * self.ripple_scale,
                ),
                pos=(
                    self.center_x - (self.width * self.ripple_scale) / 2,
                    self.center_y - (self.height * self.ripple_scale) / 2,
                ),
                group="circular_ripple_behavior",
            )
            StencilUse(group="circular_ripple_behavior")
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.center_x - self._ripple_rad / 2.0,
                    self.center_y - self._ripple_rad / 2.0,
                ),
                group="circular_ripple_behavior",
            )
            StencilUnUse(group="circular_ripple_behavior")
            Ellipse(
                pos=self.pos, size=self.size, group="circular_ripple_behavior"
            )
            StencilPop(group="circular_ripple_behavior")
            self.bind(
                ripple_color=self._set_color, _ripple_rad=self._set_ellipse
            )

    def _set_ellipse(self, instance, value):
        super()._set_ellipse(instance, value)
        if self.ellipse.size[0] > self.width * 0.6 and not self._fading_out:
            self.fade_out()
        self.ellipse.pos = (
            self.center_x - self._ripple_rad / 2.0,
            self.center_y - self._ripple_rad / 2.0,
        )
