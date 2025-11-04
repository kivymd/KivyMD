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

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDSmartTile:
                [...]

                MDSmartTileImage:
                    [...]

                MDSmartTileOverlayContainer:
                    [...]

                    # Content
                    [...]

    .. tab:: Declarative Python style

        .. code-block:: python

            MDSmartTile(
                MDSmartTileImage(
                ),
                MDSmartTileOverlayContainer(
                    # Content
                )
            )

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list-anatomy.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative python style with KV

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

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.imagelist import (
                MDSmartTile,
                MDSmartTileImage,
                MDSmartTileOverlayContainer,
            )
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def set_icon(self, heart_outline):
                    heart_outline.icon = (
                        "heart"
                        if heart_outline.icon == "heart-outline"
                        else "heart-outline"
                    )

                def on_start(self):
                    self.root.get_ids().heart_outline.bind(on_release=self.set_icon)

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return MDScreen(
                        MDSmartTile(
                            MDSmartTileImage(
                                source="bg.jpg",
                                radius=[dp(24), dp(24), 0, 0],
                            ),
                            MDSmartTileOverlayContainer(
                                MDIconButton(
                                    id="heart_outline",
                                    icon="heart-outline",
                                    theme_icon_color="Custom",
                                    icon_color=(1, 0, 0, 1),
                                    pos_hint={"center_y": 0.5},
                                ),
                                MDLabel(
                                    text="Ibanez GRG121DX-BKF",
                                    theme_text_color="Custom",
                                    text_color="white",
                                ),
                                md_bg_color=(0, 0, 0, 0.5),
                                adaptive_height=True,
                                padding="8dp",
                                spacing="8dp",
                                radius=[0, 0, dp(24), dp(24)],
                            ),
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            size_hint=(None, None),
                            size=("320dp", "320dp"),
                            overlap=False,
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


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
from kivy.properties import BooleanProperty, ObjectProperty, OptionProperty
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

    def on_touch_down(self, touch):
        if (
            self.collide_point(touch.x, touch.y)
            and self._overlay_container._touch_on_container
        ):
            return False
        elif (
            self.collide_point(touch.x, touch.y)
            and not self._overlay_container._touch_on_container
        ):
            return super().on_touch_down(touch)


class MDSmartTileOverlayContainer(MDBoxLayout):
    """
    Implements a container for custom widgets to be added to the tile.

    .. versionchanged:: 2.0.0

        The `SmartTileOverlayBox` class has been renamed to
        `MDSmartTileOverlayContainer`.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    # If True, a touch event has occurred on one of the container's widgets.
    _touch_on_container = BooleanProperty(False)
    # kivymd.uix.imagelist.imagelist.MDSmartTile object.
    _smart_tile = ObjectProperty()

    def add_widget(self, widget, *args, **kwargs):
        widget.bind(
            on_touch_down=self._child_on_touch_down,
            on_touch_up=self._child_on_touch_up,
        )
        return super().add_widget(widget, *args, **kwargs)

    def _child_on_touch_down(self, instance, touch):
        if self.collide_point(touch.x, touch.y):
            self._touch_on_container = True

    def _child_on_touch_up(self, instance, touch):
        if self.collide_point(touch.x, touch.y):
            self._touch_on_container = False


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

    ripple_effect = BooleanProperty(False)

    _overlay_container = ObjectProperty()
    _image = ObjectProperty()

    __events__ = ("on_release", "on_press")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_release(self, *args):
        """
        Fired when the button is released (i.e. the touch/click that
        pressed the button goes away).
        """

    def on_press(self, *args):
        """Fired when the button is pressed."""

    def add_widget(self, widget, *args, **kwargs):
        def set_ripple_effect(_widget):
            _widget.ripple_effect = self.ripple_effect

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
            Clock.schedule_once(lambda x: set_ripple_effect(widget), 0.5)
            return super().add_widget(widget, *args, **kwargs)
