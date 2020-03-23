"""
Components/FloatLayout
======================

:class:`~kivy.uix.floatlayout.FloatLayout` class equivalent. Simplifies working
with some widget properties. For example:

FloatLayout
-----------

.. code-block::

    FloatLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

MDFloatLayout
-------------

.. code-block::

    MDFloatLayout:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
"""

from kivy.uix.floatlayout import FloatLayout

from kivymd.uix import MDAdaptiveWidget


class MDFloatLayout(FloatLayout, MDAdaptiveWidget):
    pass
