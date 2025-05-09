"""
Components/AnchorLayout
=======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.anchorlayout.AnchorLayout` class equivalent. Simplifies working
with some widget properties. For example:

AnchorLayout
------------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            AnchorLayout:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.anchorlayout import AnchorLayout
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = AnchorLayout()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDAnchorLayout
--------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDAnchorLayout:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.anchorlayout import MDAnchorLayout
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDAnchorLayout(
                        md_bg_color=self.theme_cls.primaryColor
                    )

            MyApp().run()
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
