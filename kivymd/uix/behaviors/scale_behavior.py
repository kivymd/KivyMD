"""
Behaviors/Scale
===============

.. versionadded:: 1.1.0

Base class for controlling the scale of the widget.

.. note:: See `kivy.graphics.Rotate
    <https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Scale>`_
    for more information.

Kivy
----

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.properties import NumericProperty
    from kivy.uix.button import Button
    from kivy.app import App


    KV = '''
    Screen:

        ScaleButton:
            size_hint: .5, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.change_scale(self)

            canvas.before:
                PushMatrix
                Scale:
                    x: self.scale_value_x
                    y: self.scale_value_y
                    z: self.scale_value_x
                    origin: self.center
            canvas.after:
                PopMatrix
    '''


    class ScaleButton(Button):
        scale_value_x = NumericProperty(1)
        scale_value_y = NumericProperty(1)
        scale_value_z = NumericProperty(1)


    class Test(App):
        def build(self):
            return Builder.load_string(KV)

        def change_scale(self, instance_button: Button) -> None:
            Animation(
                scale_value_x=0.5,
                scale_value_y=0.5,
                scale_value_z=0.5,
                d=0.3,
            ).start(instance_button)


    Test().run()

KivyMD
------

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import ScaleBehavior
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    MDScreen:

        ScaleBox:
            size_hint: .5, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.change_scale(self)
            md_bg_color: "red"
    '''


    class ScaleBox(ButtonBehavior, ScaleBehavior, MDBoxLayout):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def change_scale(self, instance_button: ScaleBox) -> None:
            Animation(
                scale_value_x=0.5,
                scale_value_y=0.5,
                scale_value_z=0.5,
                d=0.3,
            ).start(instance_button)


    Test().run()

.. warning:: Do not use `ScaleBehavior` class with classes that inherited`
    from `CommonElevationBehavior` class. `CommonElevationBehavior` classes
    by default contains attributes for scale widget.
"""

__all__ = ("ScaleBehavior",)

from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty

Builder.load_string(
    """
<ScaleBehavior>
    canvas.before:
        PushMatrix
        Scale:
            x: self.scale_value_x
            y: self.scale_value_y
            z: self.scale_value_z
            origin:
                self.center \
                if not self.scale_value_center else \
                self.scale_value_center
    canvas.after:
        PopMatrix
"""
)


class ScaleBehavior:
    """Base class for controlling the scale of the widget."""

    scale_value_x = NumericProperty(1)
    """
    X-axis value.

    :attr:`scale_value_x` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_y = NumericProperty(1)
    """
    Y-axis value.

    :attr:`scale_value_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    scale_value_z = NumericProperty(1)
    """
    Z-axis value.

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
