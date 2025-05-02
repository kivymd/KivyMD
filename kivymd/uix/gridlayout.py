"""
Components/GridLayout
=====================

:class:`~kivy.uix.gridlayout.GridLayout` class equivalent. Simplifies working
with some widget properties. For example:

GridLayout
----------

.. code-block::

    GridLayout:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primaryColor
            Rectangle:
                pos: self.pos
                size: self.size

MDGridLayout
------------

.. code-block::

    MDGridLayout:
        adaptive_height: True
        md_bg_color: app.theme_cls.primaryColor

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
