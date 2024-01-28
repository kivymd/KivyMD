"""
Behaviors/Elevation
===================

.. seealso::

    `Material Design spec, Elevation <https://material.io/design/environment/elevation.html>`_

.. rubric:: Elevation is the relative distance between two surfaces along the z-axis.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevation-previous.png
    :align: center

To create an elevation effect, use the :class:`~CommonElevationBehavior` class.
For example, let's create a button with a rectangular elevation effect:

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import (
                RectangularRippleBehavior,
                BackgroundColorBehavior,
                CommonElevationBehavior,
            )

            KV = '''
            <ElevationWidget>
                size_hint: None, None
                size: "250dp", "50dp"


            MDScreen:

                # With elevation effect
                ElevationWidget:
                    pos_hint: {"center_x": .5, "center_y": .6}
                    elevation: 4
                    shadow_offset: 0, -6
                    shadow_softness: 4

                # Without elevation effect
                ElevationWidget:
                    pos_hint: {"center_x": .5, "center_y": .4}
            '''


            class ElevationWidget(
                RectangularRippleBehavior,
                CommonElevationBehavior,
                ButtonBehavior,
                BackgroundColorBehavior,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.md_bg_color = "red"


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import (
                RectangularRippleBehavior,
                BackgroundColorBehavior,
                CommonElevationBehavior,
            )
            from kivymd.uix.screen import MDScreen


            class ElevationWidget(
                RectangularRippleBehavior,
                CommonElevationBehavior,
                ButtonBehavior,
                BackgroundColorBehavior,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.md_bg_color = "red"
                    self.size_hint = (None, None)
                    self.size = ("250dp", "50dp")


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            ElevationWidget(
                                pos_hint={"center_x": .5, "center_y": .6},
                                elevation=4,
                                shadow_softness=4,
                                shadow_offset=(0, -6),
                            ),
                            ElevationWidget(
                                pos_hint={"center_x": .5, "center_y": .4},
                            ),
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-effect.png
    :align: center

.. warning::

    If before the KivyMD 1.1.0 library version you used the elevation property
    with an average value of `12` for the shadow, then starting with the KivyMD
    1.1.0 library version, the average value of the elevation property will be
    somewhere `4`.

Similarly, create a circular button:

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
            from kivymd.uix.floatlayout import MDFloatLayout

            KV = '''
            <CircularElevationButton>
                size_hint: None, None
                size: "100dp", "100dp"
                radius: self.size[0] / 2
                shadow_radius: self.radius[0]
                md_bg_color: "red"

                MDIcon:
                    icon: "hand-heart"
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size: root.size
                    pos: root.pos
                    font_size: root.size[0] * .6
                    theme_text_color: "Custom"
                    text_color: "white"


            MDScreen:

                CircularElevationButton:
                    pos_hint: {"center_x": .5, "center_y": .6}
                    elevation: 4
                    shadow_softness: 4
            '''


            class CircularElevationButton(
                CommonElevationBehavior,
                CircularRippleBehavior,
                ButtonBehavior,
                MDFloatLayout,
            ):
                pass


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.label import MDIcon
            from kivymd.uix.screen import MDScreen


            class CircularElevationButton(
                CommonElevationBehavior,
                CircularRippleBehavior,
                ButtonBehavior,
                MDFloatLayout,
            ):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.size_hint = (None, None)
                    self.size = (dp(100), dp(100))
                    self.radius = dp(100) / 2
                    self.shadow_radius = dp(100) / 2
                    self.md_bg_color = "red"
                    self.add_widget(
                        MDIcon(
                            icon="hand-heart",
                            halign="center",
                            valign="center",
                            pos_hint={"center_x": .5, "center_y": .5},
                            size=self.size,
                            theme_text_color="Custom",
                            text_color="white",
                            font_size=self.size[0] * 0.6,
                        )
                    )


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            CircularElevationButton(
                                pos_hint={"center_x": .5, "center_y": .5},
                                elevation=4,
                                shadow_softness=4,
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-elevation-effect.png
    :align: center

Animating the elevation
-----------------------

.. tabs::

    .. tab:: Declarative style with KV

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
            from kivymd.uix.widget import MDWidget

            KV = '''
            MDScreen:

                ElevatedWidget:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    size_hint: None, None
                    size: 100, 100
                    md_bg_color: 0, 0, 1, 1
                    elevation: 2
                    radius: dp(18)
            '''


            class ElevatedWidget(
                CommonElevationBehavior,
                RectangularRippleBehavior,
                ButtonBehavior,
                MDWidget,
            ):
                _elev = 0  # previous elevation value

                def on_press(self, *args):
                    if not self._elev:
                        self._elev = self.elevation
                    Animation(elevation=self.elevation + 2, d=0.4).start(self)

                def on_release(self, *args):
                    Animation.cancel_all(self, "elevation")
                    Animation(elevation=self._elev, d=0.1).start(self)


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.uix.behaviors import ButtonBehavior
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.widget import MDWidget


            class ElevatedWidget(
                CommonElevationBehavior,
                RectangularRippleBehavior,
                ButtonBehavior,
                MDWidget,
            ):
                _elev = 0  # previous elevation value

                def on_press(self, *args):
                    if not self._elev:
                        self._elev = self.elevation
                    Animation(elevation=self.elevation + 2, d=0.4).start(self)

                def on_release(self, *args):
                    Animation.cancel_all(self, "elevation")
                    Animation(elevation=self._elev, d=0.1).start(self)


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            ElevatedWidget(
                                pos_hint={'center_x': .5, 'center_y': .5},
                                size_hint=(None, None),
                                size=(100, 100),
                                md_bg_color="blue",
                                elevation=2,
                                radius=dp(18),
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-animation-effect.gif
    :align: center
"""

from __future__ import annotations

__all__ = ("CommonElevationBehavior",)

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BoundedNumericProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    VariableListProperty,
    DictProperty,
)
from kivy.uix.widget import Widget

Builder.load_string(
    """
<CommonElevationBehavior>
    canvas.before:
        PushMatrix
        Scale:
            x: self.scale_value_x
            y: self.scale_value_y
            z: self.scale_value_x
            origin:
                self.center \
                if not self.scale_value_center else \
                self.scale_value_center
        Rotate:
            angle: self.rotate_value_angle
            axis: tuple(self.rotate_value_axis)
            origin: self.center
        Color:
            rgba: root.shadow_color
        BoxShadow:
            pos: self.pos if not isinstance(self, RelativeLayout) else (0, 0)
            size: self.size
            offset: root.shadow_offset
            spread_radius: -(root.shadow_softness), -(root.shadow_softness)
            blur_radius: root.elevation_levels[root.elevation_level]
            border_radius:
                (root.radius if hasattr(self, "radius") and root.radius else [0, 0, 0, 0]) \
                if root.shadow_radius == [0.0, 0.0, 0.0, 0.0] else \
                root.shadow_radius
    canvas.after:
        PopMatrix
"""
)


class CommonElevationBehavior(Widget):
    """
    Common base class for rectangular and circular elevation behavior.

    For more information, see in the :class:`~kivy.uix.widget.Widget`
    class documentation.
    """

    elevation_level = BoundedNumericProperty(0, min=0, max=5)
    """
    Elevation level (values from 0 to 5)

    .. versionadded:: 1.2.0

    :attr:`elevation_level` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`.
    """

    elevation_levels = DictProperty(
        {
            0: 0,
            1: dp(8),
            2: dp(12),
            3: dp(16),
            4: dp(20),
            5: dp(24),
        }
    )
    """
    Elevation is measured as the distance between components along the z-axis
    in density-independent pixels (dps).

    .. versionadded:: 1.2.0

    :attr:`elevation_levels` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{0: dp(0), 1: dp(8), 2: dp(23), 3: dp(16), 4: dp(20), 5: dp(24)}`.
    """

    elevation = BoundedNumericProperty(0, min=0, errorvalue=0)
    """
    Elevation of the widget.

    :attr:`elevation` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`.
    """

    shadow_radius = VariableListProperty([0], length=4)
    """
    Radius of the corners of the shadow.

    .. versionadded:: 1.1.0

    You don't have to use this parameter.
    The radius of the elevation effect is calculated automatically one way
    or another based on the radius of the parent widget, for example:

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp

        KV = '''
        MDScreen:

            MDCard:
                radius: dp(12), dp(46), dp(12), dp(46)
                size_hint: .5, .3
                pos_hint: {"center_x": .5, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
        '''


        class Test(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Test().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-radius.png
        :align: center

    :attr:`shadow_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    shadow_softness = NumericProperty(0.0)
    """
    Softness of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior

        KV = '''
        <ElevationWidget>
            size_hint: None, None
            size: "250dp", "50dp"


        MDScreen:

            ElevationWidget:
                pos_hint: {"center_x": .5, "center_y": .6}
                elevation: 6
                shadow_softness: 6

            ElevationWidget:
                pos_hint: {"center_x": .5, "center_y": .4}
                elevation: 6
                shadow_softness: 12
        '''


        class ElevationWidget(CommonElevationBehavior, BackgroundColorBehavior):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.md_bg_color = "blue"


        class Example(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-softness.png
        :align: center

    :attr:`shadow_softness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    shadow_offset = ListProperty((0, 0))
    """
    Offset of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior

        KV = '''
        <ElevationWidget>
            size_hint: None, None
            size: "100dp", "100dp"


        MDScreen:

            ElevationWidget:
                pos_hint: {"center_x": .5, "center_y": .5}
                elevation: 6
                shadow_radius: dp(6)
                shadow_softness: 12
                shadow_offset: -12, -12
        '''


        class ElevationWidget(CommonElevationBehavior, BackgroundColorBehavior):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.md_bg_color = "blue"


        class Example(MDApp):
            def build(self):
                return Builder.load_string(KV)


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-1.png
        :align: center

    .. code-block:: kv

        ElevationWidget:
            shadow_offset: 12, -12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-2.png
        :align: center

    .. code-block:: kv

        ElevationWidget:
            shadow_offset: 12, 12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-3.png
        :align: center

    .. code-block:: kv

        ElevationWidget:
            shadow_offset: -12, 12

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-offset-4.png
        :align: center

    :attr:`shadow_offset` is an :class:`~kivy.properties.ListProperty`
    and defaults to `(0, 0)`.
    """

    shadow_color = ColorProperty([0, 0, 0, 0.6])
    """
    Offset of the shadow.

    .. versionadded:: 1.1.0

    .. code-block:: python

        ElevationWidget:
            shadow_color: 0, 0, 1, .8

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-color.png
        :align: center

    :attr:`shadow_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.6]`.
    """

    scale_value_x = NumericProperty(1)
    """
    X-axis value.

    .. versionadded:: 1.2.0

    :attr:`scale_value_x` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_y = NumericProperty(1)
    """
    Y-axis value.

    .. versionadded:: 1.2.0

    :attr:`scale_value_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_z = NumericProperty(1)
    """
    Z-axis value.

    .. versionadded:: 1.2.0

    :attr:`scale_value_z` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_center = ListProperty()
    """
    Origin of the scale.

    .. versionadded:: 1.2.0

    The format of the origin can be either (x, y) or (x, y, z).

    :attr:`scale_value_center` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `[]`.
    """

    rotate_value_angle = NumericProperty(0)
    """
    Property for getting/setting the angle of the rotation.

    .. versionadded:: 1.2.0

    :attr:`rotate_value_angle` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    rotate_value_axis = ListProperty((0, 0, 1))
    """
    Property for getting/setting the axis of the rotation.

    .. versionadded:: 1.2.0

    :attr:`rotate_value_axis` is an :class:`~kivy.properties.ListProperty`
    and defaults to `(0, 0, 1)`.
    """

    # _elevation = 0
    _elevation_level = 0
    _shadow_softness = 0
    _shadow_color = (0, 0, 0, 0)

    # def on_elevation(self, instance, value) -> None:
    #     self._elevation = value
