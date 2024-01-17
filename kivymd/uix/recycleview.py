"""
Components/RecycleView
======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.recycleview.RecycleView` class equivalent. Simplifies working
with some widget properties. For example:

RecycleView
-----------

.. code-block:: kv

    RecycleView:

        canvas:
            Color:
                rgba: app.theme_cls.primaryColor
            Rectangle:
                pos: self.pos
                size: self.size

MDRecycleView
-------------

.. code-block:: kv

    MDRecycleView:
        md_bg_color: app.theme_cls.primaryColor
"""

__all__ = ("MDRecycleView",)

from kivy.uix.recycleview import RecycleView

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDRecycleView(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RecycleView,
    MDAdaptiveWidget,
):
    """
    Recycle view class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.recycleview.RecycleView` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
