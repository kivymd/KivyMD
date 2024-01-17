"""
Components/Widget
=================

:class:`~kivy.uix.widget.Widget` class equivalent. Simplifies working
with some widget properties. For example:

Widget
------

.. code-block:: kv

    Widget:
        size_hint: .5, None
        height: self.width

        canvas:
            Color:
                rgba: app.theme_cls.primaryColor
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [self.height / 2,]

MDWidget
--------

.. code-block:: kv

    MDWidget:
        size_hint: .5, None
        height: self.width
        radius: self.height / 2
        md_bg_color: app.theme_cls.primaryColor
"""

__all__ = ("MDWidget",)

from kivy.uix.widget import Widget

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDWidget(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    MDAdaptiveWidget,
    Widget,
):
    """
    Widget class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivy.uix.widget.Widget` and
    classes documentation.

    .. versionadded:: 1.0.0
    """
