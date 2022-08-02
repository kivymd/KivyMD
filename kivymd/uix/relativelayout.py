"""
Components/RelativeLayout
=========================

:class:`~kivy.uix.relativelayout.RelativeLayout` class equivalent.
Simplifies working with some widget properties. For example:

RelativeLayout
--------------

.. code-block:: kv

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

.. code-block:: kv

    MDRelativeLayout:
        radius: [25, ]
        md_bg_color: app.theme_cls.primary_color
"""

from kivy.uix.relativelayout import RelativeLayout

from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior


class MDRelativeLayout(DeclarativeBehavior, RelativeLayout, MDAdaptiveWidget):
    """
    Relative layout class. For more information, see in the
    :class:`~kivy.uix.relativelayout.RelativeLayout` class documentation.
    """
