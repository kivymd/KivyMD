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
                rgba: app.theme_cls.primaryColor
            Rectangle:
                pos: self.pos
                size: self.size

MDAnchorLayout
--------------

.. code-block:: kv

    MDAnchorLayout:
        md_bg_color: app.theme_cls.primaryColor
"""

__all__ = ("MDAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDAnchorLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    AnchorLayout,
    MDAdaptiveWidget,
):
    """
    Anchor layout class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
