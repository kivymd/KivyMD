"""
Components/Relative Layout
==========================

:class:`~kivy.uix.relativelayout.RelativeLayout` class equivalent. Simplifies working
with some widget properties. For example:

RelativeLayout
--------------

.. code-block::

    RelativeLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: (0, 0)
                size: self.size
                radius: [25, ]

MDRelativeLayout
----------------

.. code-block::

    MDRelativeLayout:
        radius: [25, ]
        md_bg_color: app.theme_cls.primary_color
"""

from kivy.uix.relativelayout import RelativeLayout

from kivymd.uix import MDAdaptiveWidget


class MDRelativeLayout(RelativeLayout, MDAdaptiveWidget):
    pass
