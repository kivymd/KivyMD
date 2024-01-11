"""
Components/ImageList
====================

.. seealso::

    `Material Design spec, Image lists <https://material.io/components/image-lists>`_

.. rubric:: Image lists display a collection of images in an organized grid.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list.png
    :align: center

Usage
-----

.. code-block:: kv

    MDSmartTile:
        [...]

        MDSmartTileImage:
            [...]

        MDSmartTileOverlayContainer:
            [...]

            # Content
            [...]

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list-anatomy.png
    :align: center

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDSmartTile:
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: None, None
            size: "320dp", "320dp"
            overlap: False

            MDSmartTileImage:
                source: "bg.jpg"
                radius: [dp(24), dp(24), 0, 0]

            MDSmartTileOverlayContainer:
                md_bg_color: 0, 0, 0, .5
                adaptive_height: True
                padding: "8dp"
                spacing: "8dp"
                radius: [0, 0, dp(24), dp(24)]

                MDIconButton:
                    icon: "heart-outline"
                    theme_icon_color: "Custom"
                    icon_color: 1, 0, 0, 1
                    pos_hint: {"center_y": .5}
                    on_release:
                        self.icon = "heart" \\
                        if self.icon == "heart-outline" else \\
                        "heart-outline"

                MDLabel:
                    text: "Ibanez GRG121DX-BKF"
                    theme_text_color: "Custom"
                    text_color: "white"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list-example.png
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDSmartTile:
        [...]

        # Content.
        MDIconButton:
            [...]

        MDLabel:
            [...]


2.0.0 version
-------------

.. code-block:: kv

    MDSmartTile:
        [...]

        MDSmartTileImage:
            [...]

        MDSmartTileOverlayContainer:
            [...]

            # Content.
            [...]
"""

__all__ = ["MDSmartTile", "MDSmartTileOverlayContainer", "MDSmartTileImage"]

import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, OptionProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd import uix_path
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.relativelayout import MDRelativeLayout

with open(
    os.path.join(uix_path, "imagelist", "imagelist.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSmartTileImage(RectangularRippleBehavior, ButtonBehavior, FitImage):
    """
    Implements the tile image.

    .. versionchanged:: 2.0.0

        The `SmartTileImage` class has been renamed to `MDSmartTileImage`.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.fitimage.fitimage.FitImage`
    classes documentation.
    """

    _smart_tile = ObjectProperty()
    _overlay_container = ObjectProperty()


class MDSmartTileOverlayContainer(MDBoxLayout):
    """
    Implements a container for custom widgets to be added to the tile.

    .. versionchanged:: 2.0.0

        The `SmartTileOverlayBox` class has been renamed to
        `MDSmartTileOverlayContainer`.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    _smart_tile = ObjectProperty()


class MDSmartTile(MDRelativeLayout):
    """
    A tile for more complex needs.

    For more information, see in the
    :class:`~kivymd.uix.relativelayout.MDRelativeLayout`
    class documentation.

    Includes an image, a container to place overlays and a box that can act
    as a header or a footer, as described in the Material Design specs.

    :Events:
        `on_press`
            Fired when the button is pressed.
        `on_release`
            Fired when the button is released (i.e. the touch/click that
            pressed the button goes away).
    """

    overlay_mode = OptionProperty("footer", options=["footer", "header"])
    """
    Determines weather the information box acts as a header or footer to the
    image. Available are options: `'footer'`, `'header'`.

    .. versionchanged:: 2.0.0

        The `box_position` attribute has been renamed to `overlay_mode`.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list-overlay-mode.png
        :align: center

    :attr:`overlay_mode` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'footer'`.
    """

    overlap = BooleanProperty(True)
    """
    Determines if the `header/footer` overlaps on top of the image or not.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list-overlap.png
        :align: center

    :attr:`overlap` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    _no_ripple_effect = BooleanProperty(False)
    _overlay_container = ObjectProperty()
    _image = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_release")
        self.register_event_type("on_press")

    def on_release(self, *args):
        """
        Fired when the button is released (i.e. the touch/click that
        pressed the button goes away).
        """

    def on_press(self, *args):
        """Fired when the button is pressed."""

    def add_widget(self, widget, *args, **kwargs):
        def set_overlay_container(_widget):
            _widget._overlay_container = self._overlay_container

        if isinstance(widget, MDSmartTileOverlayContainer):
            widget._smart_tile = self
            self._overlay_container = widget
            return super().add_widget(widget, *args, **kwargs)
        elif isinstance(widget, MDSmartTileImage):
            self._image = widget
            widget._smart_tile = self
            widget._overlay_container = self._overlay_container
            Clock.schedule_once(lambda x: set_overlay_container(widget), 0.5)
            return super().add_widget(widget, *args, **kwargs)
