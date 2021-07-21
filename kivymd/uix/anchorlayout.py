"""
Components/AnchorLayout
=======================

.. versionadded:: 1.0.0

:class:`~kivy.uix.anchorlayout.AnchorLayout` class equivalent. Simplifies working
with some widget properties. For example:

AnchorLayout
------------

.. code-block::

    AnchorLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

AnchorLayout
------------

.. code-block::

    MDBoxLayout:
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
    height: self.minimum_width

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

__all__ = ("MDAnchorLayout",)

from kivy.uix.anchorlayout import AnchorLayout

from kivymd.uix import MDAdaptiveWidget


class MDAnchorLayout(AnchorLayout, MDAdaptiveWidget):
    pass
