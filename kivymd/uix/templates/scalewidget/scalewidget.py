"""
Templates/ScaleWidget
=====================

.. versionadded:: 1.0.0

Base class for controlling the scale of the widget.

.. note:: See `kivy.graphics.Scale
    <https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Scale>`_
    for more information.

Kivy
----

.. code-block:: python

    from typing import NoReturn

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

        def change_scale(self, instance_button: Button) -> NoReturn:
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

    from typing import NoReturn

    from kivy.animation import Animation
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDRaisedButton
    from kivymd.uix.templates import ScaleWidget

    KV = '''
    MDScreen:

        ScaleButton:
            size_hint: .5, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.change_scale(self)
            elevation:0
    '''


    class ScaleButton(MDRaisedButton, ScaleWidget):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def change_scale(self, instance_button: MDRaisedButton) -> NoReturn:
            Animation(
                scale_value_x=0.5,
                scale_value_y=0.5,
                scale_value_z=0.5,
                d=0.3,
            ).start(instance_button)


    Test().run()
"""

__all__ = ("ScaleWidget",)

import os

from kivy.lang import Builder
from kivy.properties import NumericProperty

from kivymd import uix_path

with open(
    os.path.join(uix_path, "templates", "scalewidget", "scalewidget.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class ScaleWidget:
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
