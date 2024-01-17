"""
Components/Divider
==================

.. versionadded:: 2.0.0

.. seealso::

    `Material Design 3 spec, Divider <https://m3.material.io/components/divider/overview>`_

.. rubric:: Dividers are thin lines that group content in lists or other containers.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/divider.png
    :align: center

- Make dividers visible but not bold
- Only use dividers if items can’t be grouped with open space
- Use dividers to group things, not separate individual items

`KivyMD` provides the following bar positions for use:

- HorizontalDivider_
- VerticalDivider_

.. HorizontalDivider:

HorizontalDivider
-----------------

Dividers are one way to visually group components and create hierarchy.
They can also be used to imply nested parent/child relationships.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/divider-horizontal-desc.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDDivider:
            size_hint_x: .5
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/divider-horizontal.png
    :align: center

.. VerticalDivider:

VerticalDivider
---------------

A vertical divider can be used to arrange content on a larger screen, such as
separating paragraph text from video or imagery media.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/divider-vertical-desc.png
    :align: center

.. code-block:: kv

    MDDivider:
        size_hint_y: .5
        orientation: "vertical"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/divider-vertical.png
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDSeparator:
        [...]

2.0.0 version
-------------

.. code-block:: kv

    MDDivider:
        [...]
"""

__all__ = ("MDDivider",)

import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path

with open(
    os.path.join(uix_path, "divider", "divider.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDDivider(BoxLayout):
    """
    A divider line.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    color = ColorProperty(None)
    """
    Divider color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    divider_width = NumericProperty(dp(1))
    """
    Divider width.

    :attr:`divider_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(1)`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.on_orientation)

    def on_orientation(self, *args) -> None:
        """Fired when the values of :attr:`orientation` change."""

        if self.orientation == "vertical":
            self.size_hint_x = None
            self.width = self.divider_width
        elif self.orientation == "horizontal":
            self.size_hint_y = None
            self.height = self.divider_width
