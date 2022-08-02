"""
Components/AnchorLayout
=======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.anchorlayout.AnchorLayout` class equivalent. Simplifies working
with some widget properties. For example:

AnchorLayout
------------

.. code-block:: kv

    AnchorLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDAnchorLayout
--------------

.. code-block:: kv

    MDAnchorLayout:
        md_bg_color: app.theme_cls.primary_color
"""

__all__ = ("MDAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior


class MDAnchorLayout(DeclarativeBehavior, AnchorLayout, MDAdaptiveWidget):
    """
    Anchor layout class. For more information, see in the
    :class:`~kivy.uix.anchorlayout.AnchorLayout` class documentation.
    """
