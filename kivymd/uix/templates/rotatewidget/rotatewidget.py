"""
Templates/RotateWidget
======================

.. versionadded:: 1.0.0

Base class for controlling the rotate of the widget.

.. note:: See `kivy.graphics.Rotate
    <https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Rotate>`_
    for more information.

Kivy
----

.. code-block:: python

    from typing import NoReturn

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.app import App
    from kivy.properties import NumericProperty
    from kivy.uix.button import Button

    KV = '''
    Screen:

        RotateButton:
            size_hint: .5, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.change_rotate(self)

            canvas.before:
                PushMatrix
                Rotate:
                    angle: self.rotate_value_angle
                    axis: 0, 0, 1
                    origin: self.center
            canvas.after:
                PopMatrix
    '''


    class RotateButton(Button):
        rotate_value_angle = NumericProperty(0)


    class Test(App):
        def build(self):
            return Builder.load_string(KV)

        def change_rotate(self, instance_button: Button) -> NoReturn:
            Animation(rotate_value_angle=45, d=0.3).start(instance_button)


    Test().run()

KivyMD
------

.. code-block:: python

    from typing import NoReturn

    from kivy.animation import Animation
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDRaisedButton
    from kivymd.uix.templates import RotateWidget

    KV = '''
    MDScreen:

        RotateButton:
            size_hint: .5, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.change_rotate(self)
            elevation:0
    '''


    class RotateButton(MDRaisedButton, RotateWidget):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def change_rotate(self, instance_button: MDRaisedButton) -> NoReturn:
            Animation(rotate_value_angle=45, d=0.3).start(instance_button)


    Test().run()
"""

__all__ = ("RotateWidget",)

import os

from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty

from kivymd import uix_path

with open(
    os.path.join(uix_path, "templates", "rotatewidget", "rotatewidget.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class RotateWidget:
    """Base class for controlling the rotate of the widget."""

    rotate_value_angle = NumericProperty(0)
    """
    Property for getting/setting the angle of the rotation.

    :attr:`rotate_value_angle` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    rotate_value_axis = ListProperty((0, 0, 1))
    """
    Property for getting/setting the axis of the rotation.

    :attr:`rotate_value_axis` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `(0, 0, 1)`.
    """
