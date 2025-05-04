"""
Components/RecycleGridLayout
============================

:class:`~kivy.uix.recyclegridlayout.RecycleGridLayout` class equivalent.
Simplifies working with some widget properties. For example:

RecycleGridLayout
-----------------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            RecycleGridLayout:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.recyclegridlayout import RecycleGridLayout
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = RecycleGridLayout()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDRecycleGridLayout
-------------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDRecycleGridLayout:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDRecycleGridLayout(
                        md_bg_color=self.theme_cls.primaryColor
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

__all__ = ("MDRecycleGridLayout",)

from kivy.uix.recyclegridlayout import RecycleGridLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior


class MDRecycleGridLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RecycleGridLayout,
    MDAdaptiveWidget,
):
    """
    Recycle grid layout class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.recyclegridlayout.RecycleGridLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
