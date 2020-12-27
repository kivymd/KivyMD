"""
Components/Float Layout
=======================

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

.. Warning:: For a :class:`~kivy.uix.floatlayout.FloatLayout`, the
    ``minimum_size`` attributes are always 0, so you cannot use
    ``adaptive_size`` and related options.
"""

from kivy.uix.floatlayout import FloatLayout

from kivymd.uix import MDAdaptiveWidget


class MDFloatLayout(FloatLayout, MDAdaptiveWidget):
    pass
