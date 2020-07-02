"""
Behaviors/Elevation
===================

.. rubric:: Classes implements a circular and rectangular elevation effects.

To create a widget with rectangular or circular elevation effect,
you must create a new class that inherits from the
:class:`~RectangularElevationBehavior` or :class:`~CircularElevationBehavior`
class.

For example, let's create an button with a rectangular elevation effect:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import (
        RectangularRippleBehavior,
        BackgroundColorBehavior,
        RectangularElevationBehavior,
    )

    KV = '''
    <RectangularElevationButton>:
        size_hint: None, None
        size: "250dp", "50dp"


    Screen:

        # With elevation effect
        RectangularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .6}
            elevation: 11

        # Without elevation effect
        RectangularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .4}
    '''


    class RectangularElevationButton(
        RectangularRippleBehavior,
        RectangularElevationBehavior,
        ButtonBehavior,
        BackgroundColorBehavior,
    ):
        md_bg_color = [0, 0, 1, 1]


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-effect.gif
    :align: center

Similarly, create a button with a circular elevation effect:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.image import Image
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import (
        CircularRippleBehavior,
        CircularElevationBehavior,
    )

    KV = '''
    #:import images_path kivymd.images_path


    <CircularElevationButton>:
        size_hint: None, None
        size: "100dp", "100dp"
        source: f"{images_path}/kivymd_logo.png"


    Screen:

        # With elevation effect
        CircularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .6}
            elevation: 5

        # Without elevation effect
        CircularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .4}
            elevation: 0
    '''


    class CircularElevationButton(
        CircularRippleBehavior,
        CircularElevationBehavior,
        ButtonBehavior,
        Image,
    ):
        md_bg_color = [0, 0, 1, 1]


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-elevation-effect.gif
    :align: center
"""

__all__ = (
    "CommonElevationBehavior",
    "RectangularElevationBehavior",
    "CircularElevationBehavior",
)

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, NumericProperty, ObjectProperty

from kivymd.app import MDApp

Builder.load_string(
    """
<RectangularElevationBehavior>
    canvas.before:
        Color:
            a: self._soft_shadow_a
        Rectangle:
            texture: self._soft_shadow_texture
            size: self._soft_shadow_size
            pos: self._soft_shadow_pos
        Color:
            a: self._hard_shadow_a
        Rectangle:
            texture: self._hard_shadow_texture
            size: self._hard_shadow_size
            pos: self._hard_shadow_pos
        Color:
            a: 1


<CircularElevationBehavior>
    canvas.before:
        Color:
            a: self._soft_shadow_a
        Rectangle:
            texture: self._soft_shadow_texture
            size: self._soft_shadow_size
            pos: self._soft_shadow_pos
        Color:
            a: self._hard_shadow_a
        Rectangle:
            texture: self._hard_shadow_texture
            size: self._hard_shadow_size
            pos: self._hard_shadow_pos
        Color:
            a: 1
"""
)


class CommonElevationBehavior(object):
    """Common base class for rectangular and circular elevation behavior."""

    elevation = NumericProperty(1)
    """
    Elevation value.

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to 1.
    """

    _elevation = NumericProperty(0)
    _soft_shadow_texture = ObjectProperty()
    _soft_shadow_size = ListProperty((0, 0))
    _soft_shadow_pos = ListProperty((0, 0))
    _soft_shadow_a = NumericProperty(0)
    _hard_shadow_texture = ObjectProperty()
    _hard_shadow_size = ListProperty((0, 0))
    _hard_shadow_pos = ListProperty((0, 0))
    _hard_shadow_a = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            elevation=self._update_elevation,
            pos=self._update_shadow,
            size=self._update_shadow,
        )

    def _update_shadow(self, *args):
        raise NotImplementedError

    def _update_elevation(self, instance, value):
        if not self._elevation:
            self._elevation = value
            self._update_shadow(instance, value)


class RectangularElevationBehavior(CommonElevationBehavior):
    """Base class for rectangular elevation behavior.
    Controls the size and position of the shadow."""

    def _update_shadow(self, *args):
        if self._elevation > 0:
            # Set shadow size.
            ratio = self.width / (self.height if self.height != 0 else 1)
            if -2 < ratio < 2:
                self._shadow = MDApp.get_running_app().theme_cls.quad_shadow
                width = soft_width = self.width * 1.9
                height = soft_height = self.height * 1.9
            elif ratio <= -2:
                self._shadow = MDApp.get_running_app().theme_cls.rec_st_shadow
                ratio = abs(ratio)
                if ratio > 5:
                    ratio = ratio * 22
                else:
                    ratio = ratio * 11.5
                width = soft_width = self.width * 1.9
                height = self.height + dp(ratio)
                soft_height = (
                    self.height + dp(ratio) + dp(self._elevation) * 0.5
                )
            else:
                self._shadow = MDApp.get_running_app().theme_cls.quad_shadow
                width = soft_width = self.width * 1.8
                height = soft_height = self.height * 1.8

            self._soft_shadow_size = (soft_width, soft_height)
            self._hard_shadow_size = (width, height)
            # Set ``soft_shadow`` parameters.
            self._soft_shadow_pos = (
                self.center_x - soft_width / 2,
                self.center_y
                - soft_height / 2
                - dp(0.1 * 1.5 ** self._elevation),
            )
            self._soft_shadow_a = 0.1 * 1.1 ** self._elevation
            self._soft_shadow_texture = self._shadow.textures[
                str(int(round(self._elevation)))
            ]
            # Set ``hard_shadow`` parameters.
            self._hard_shadow_pos = (
                self.center_x - width / 2,
                self.center_y - height / 2 - dp(0.5 * 1.18 ** self._elevation),
            )
            self._hard_shadow_a = 0.4 * 0.9 ** self._elevation
            self._hard_shadow_texture = self._shadow.textures[
                str(int(round(self._elevation)))
            ]
        else:
            self._soft_shadow_a = 0
            self._hard_shadow_a = 0


class CircularElevationBehavior(CommonElevationBehavior):
    """Base class for circular elevation behavior.
    Controls the size and position of the shadow."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._shadow = MDApp.get_running_app().theme_cls.round_shadow

    def _update_shadow(self, *args):
        if self.elevation > 0:
            # Set shadow size.
            width = self.width * 2
            height = self.height * 2

            x = self.center_x - width / 2
            self._soft_shadow_size = (width, height)
            self._hard_shadow_size = (width, height)
            # Set ``soft_shadow`` parameters.
            y = self.center_y - height / 2 - dp(0.1 * 1.5 ** self._elevation)
            self._soft_shadow_pos = (x, y)
            self._soft_shadow_a = 0.1 * 1.1 ** self._elevation
            self._soft_shadow_texture = self._shadow.textures[
                str(int(round(self._elevation)))
            ]
            # Set ``hard_shadow`` parameters.
            y = self.center_y - height / 2 - dp(0.5 * 1.18 ** self._elevation)
            self._hard_shadow_pos = (x, y)
            self._hard_shadow_a = 0.4 * 0.9 ** self._elevation
            self._hard_shadow_texture = self._shadow.textures[
                str(int(round(self._elevation)))
            ]
        else:
            self._soft_shadow_a = 0
            self._hard_shadow_a = 0
