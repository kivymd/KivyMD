"""
Components/GridLayout
=====================

:class:`~kivy.uix.gridlayout.GridLayout` class equivalent. Simplifies working
with some widget properties. For example:

GridLayout
----------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            GridLayout:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.gridlayout import GridLayout
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = GridLayout()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDGridLayout
------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDGridLayout:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.gridlayout import MDGridLayout
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDGridLayout(
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

__all__ = ("MDGridLayout",)

from kivy.uix.gridlayout import GridLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior


class MDGridLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    GridLayout,
    MDAdaptiveWidget,
):
    """
    Grid layout class.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.gridlayout.GridLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
