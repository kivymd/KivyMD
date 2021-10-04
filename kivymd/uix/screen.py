"""
Components/Screen
=================

:class:`~kivy.uix.screenmanager.Screen` class equivalent. Simplifies working
with some widget properties. For example:

Screen
------

.. code-block::

    Screen:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

MDScreen
--------

.. code-block::

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
"""

from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

from kivymd.uix import MDAdaptiveWidget

kv = """
<MDScreen>:
    canvas.before:
        Color:
            rgba: self._md_bg_color
        Rectangle:
            pos: self.pos
            size: self.size
"""
Builder.load_string(kv, filename="MDScreen.kv")

class MDScreen(Screen, MDAdaptiveWidget):
    pass
