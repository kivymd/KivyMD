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
                rgba: app.theme_cls.primaryColor
            RoundedRectangle:
                pos: (0, 0)
                size: self.size
                radius: [25, ]

MDRelativeLayout
----------------

.. code-block:: kv

    MDRelativeLayout:
        radius: [25, ]
        md_bg_color: app.theme_cls.primaryColor
"""

__all__ = ("MDRelativeLayout",)

from kivy.uix.relativelayout import RelativeLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDRelativeLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RelativeLayout,
    MDAdaptiveWidget,
):
    """
    Relative layout class.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
