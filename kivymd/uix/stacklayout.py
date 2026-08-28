"""
Components/StackLayout
======================

:class:`~kivy.uix.stacklayout.StackLayout` class equivalent. Simplifies working
with some widget properties. For example:

StackLayout
-----------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            StackLayout:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.stacklayout import StackLayout
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = StackLayout()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDStackLayout
-------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDStackLayout:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.stacklayout import MDStackLayout
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDStackLayout(
                        md_bg_color=self.theme_cls.primaryColor
                    )

            MyApp().run()

IOSStackLayout
--------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            IOSStackLayout:
                bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.stacklayout import IOSStackLayout
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return IOSStackLayout(
                        bg_color=self.theme_cls.primaryColor
                    )

            MyApp().run()

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:

adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:

adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    width: self.minimum_width

.. adaptive_size:

adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

__all__ = (
    "MDStackLayout",
    "IOSStackLayout",
)

from kivy.uix.stacklayout import StackLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
    IOSBackgroundColorBehavior,
)


class MDStackLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    StackLayout,
    MDAdaptiveWidget,
):
    """
    Stack layout class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.stacklayout.StackLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """


class IOSStackLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    IOSBackgroundColorBehavior,
    StackLayout,
    MDAdaptiveWidget,
):
    """
    iOS Stack layout class.

    .. versionadded:: 2.0.1

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.ios.backgroundcolor_behavior.IOSBackgroundColorBehavior` and
    :class:`~kivy.uix.stacklayout.StackLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
