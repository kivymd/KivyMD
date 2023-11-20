"""
Components/ScrollView
=====================

.. versionadded:: 1.0.0

:class:`~kivy.uix.scrollview.ScrollView` class equivalent. Simplifies working
with some widget properties. For example:

ScrollView
----------

.. code-block:: kv

    ScrollView:

        canvas:
            Color:
                rgba: app.theme_cls.primaryColor
            Rectangle:
                pos: self.pos
                size: self.size

MDScrollView
------------

.. code-block:: kv

    MDScrollView:
        md_bg_color: app.theme_cls.primaryColor
"""

from __future__ import annotations

__all__ = ("MDScrollView",)

from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.uix.scrollview import ScrollView

from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDScrollViewEffect(DampedScrollEffect):
    """
    This class is simply based on DampedScrollEffect.
    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """

    def on_overscroll(self, instance, overscroll: int | float) -> None:
        ...


class MDScrollView(DeclarativeBehavior, BackgroundColorBehavior, ScrollView):
    """
    ScrollView class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.scrollview.ScrollView`
    classes documentation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.effect_cls = MDScrollViewEffect
