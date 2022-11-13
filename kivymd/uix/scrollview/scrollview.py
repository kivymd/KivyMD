"""
Components/ScrollView
=====================

:class:`~kivy.uix.scrollview.ScrollView` class equivalent. Simplifies working
with some widget properties. For example:

ScrollView
----------

.. code-block::

    ScrollView:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDScrollView
------------

.. code-block::

    MDScrollView:
        adaptive_height: True
        md_bg_color: app.theme_cls.primary_color

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

__all__ = "MDScrollView"

import os

from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivymd import uix_path
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior

with open(
    os.path.join(uix_path, "scrollview", "scrollview.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDScrollView(DeclarativeBehavior, ScrollView, MDAdaptiveWidget):
    """
    Scroll view class. For more information, see in the
    :class:`~kivy.uix.scrollview.ScrollView` class documentation.
    """

    bar_radius = ListProperty([dp(0), dp(0), dp(0), dp(0)])
    """
    `MDScrollView` scroll bar radius.

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(0), dp(0), dp(0), dp(0)]`.
    """
