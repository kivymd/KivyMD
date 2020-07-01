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
    #:import images_path kivymd.images_path


    Screen:

        CircularRippleButton:
            source: f"{images_path}/kivymd_logo.png"
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
            self.theme_cls.theme_style = "Dark"
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
    Screen:

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
            self.theme_cls.theme_style = "Dark"
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

from kivy.animation import Animation
from kivy.graphics import (
    Color,
    Ellipse,
    Rectangle,
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)


class CommonRipple(object):
    """Base class for ripple effect."""

    ripple_rad_default = NumericProperty(1)
    """
    Default value of the ripple effect radius.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-rad-default.gif
       :align: center

    :attr:`ripple_rad_default` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    ripple_color = ListProperty()
    """
    Ripple color in ``rgba`` format.

    :attr:`ripple_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    ripple_alpha = NumericProperty(0.5)
    """
    Alpha channel values for ripple effect.

    :attr:`ripple_alpha` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    ripple_scale = NumericProperty(None)
    """
    Ripple effect scale.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-scale-1.gif
       :align: center

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    ripple_duration_in_fast = NumericProperty(0.3)
    """
    Ripple duration when touching to widget.

    :attr:`ripple_duration_in_fast` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    ripple_duration_in_slow = NumericProperty(2)
    """
    Ripple duration when long touching to widget.

    :attr:`ripple_duration_in_slow` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    ripple_duration_out = NumericProperty(0.3)
    """
    The duration of the disappearance of the wave effect.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ripple-duration-out.gif
       :align: center

    :attr:`ripple_duration_out` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
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

    :attr:`ripple_func_in` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'ripple_func_out'`.
    """

    _ripple_rad = NumericProperty()
    _doing_ripple = BooleanProperty(False)
    _finishing_ripple = BooleanProperty(False)
    _fading_out = BooleanProperty(False)
    _no_ripple_effect = BooleanProperty(False)

    def lay_canvas_instructions(self):
        raise NotImplementedError

    def start_ripple(self):
        if not self._doing_ripple:
            self._doing_ripple = True
            anim = Animation(
                _ripple_rad=self.finish_rad,
                t="linear",
                duration=self.ripple_duration_in_slow,
            )
            anim.bind(on_complete=self.fade_out)

            anim.start(self)

    def finish_ripple(self):
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

    def fade_out(self, *args):
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

    def anim_complete(self, *args):
        self._doing_ripple = False
        self._finishing_ripple = False
        self._fading_out = False
        self.canvas.after.clear()

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return False
        if not self.collide_point(touch.x, touch.y):
            return False

        if not self.disabled:
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
                self.ripple_color = self.theme_cls.ripple_color
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
        return super().on_touch_down(touch)

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
    """Class implements a rectangular ripple effect."""

    ripple_scale = NumericProperty(2.75)
    """
    See :class:`~CommonRipple.ripple_scale`.

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.75`.
    """

    def lay_canvas_instructions(self):
        if self._no_ripple_effect:
            return
        with self.canvas.after:
            StencilPush()
            Rectangle(pos=self.pos, size=self.size)
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.ripple_pos[0] - self._ripple_rad / 2.0,
                    self.ripple_pos[1] - self._ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            Rectangle(pos=self.pos, size=self.size)
            StencilPop()
        self.bind(ripple_color=self._set_color, _ripple_rad=self._set_ellipse)

    def _set_ellipse(self, instance, value):
        super()._set_ellipse(instance, value)
        self.ellipse.pos = (
            self.ripple_pos[0] - self._ripple_rad / 2.0,
            self.ripple_pos[1] - self._ripple_rad / 2.0,
        )


class CircularRippleBehavior(CommonRipple):
    """Class implements a circular ripple effect."""

    ripple_scale = NumericProperty(1)
    """
    See :class:`~CommonRipple.ripple_scale`.

    :attr:`ripple_scale` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def lay_canvas_instructions(self):
        with self.canvas.after:
            StencilPush()
            self.stencil = Ellipse(
                size=(
                    self.width * self.ripple_scale,
                    self.height * self.ripple_scale,
                ),
                pos=(
                    self.center_x - (self.width * self.ripple_scale) / 2,
                    self.center_y - (self.height * self.ripple_scale) / 2,
                ),
            )
            StencilUse()
            self.col_instruction = Color(rgba=self.ripple_color)
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.center_x - self._ripple_rad / 2.0,
                    self.center_y - self._ripple_rad / 2.0,
                ),
            )
            StencilUnUse()
            Ellipse(pos=self.pos, size=self.size)
            StencilPop()
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
