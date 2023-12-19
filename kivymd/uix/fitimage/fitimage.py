"""
Components/FitImage
===================

Example:
========

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDBoxLayout:
                size_hint_y: None
                height: "200dp"
                orientation: 'vertical'

                FitImage:
                    size_hint_y: 3
                    source: 'images/img1.jpg'

                FitImage:
                    size_hint_y: 1
                    source: 'images/img2.jpg'

    .. tab:: Declarative python styles

        .. code-block:: python

            MDBoxLayout(
                FitImage(
                    size_hint_y=0.3,
                    source='images/img1.jpg',
                ),
                FitImage(
                    size_hint_y=0.7,
                    source='images/img2.jpg',
                ),
                size_hint_y=None,
                height="200dp",
                orientation='vertical',
            )

Example with round corners:
===========================

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fitimage-round-corners.png
    :align: center

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDCard:
                    radius: dp(36)
                    md_bg_color: "grey"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: .4, .8

                    FitImage:
                        source: "bg.jpg"
                        size_hint_y: .35
                        pos_hint: {"top": 1}
                        radius: dp(36), dp(36), 0, 0
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.card import MDCard
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDCard(
                                FitImage(
                                    source="bg.jpg",
                                    size_hint_y=0.35,
                                    pos_hint={"top": 1},
                                    radius=(dp(36), dp(36), 0, 0),
                                ),
                                radius=dp(36),
                                md_bg_color="grey",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                size_hint=(0.4, 0.8),
                            ),
                        )
                    )


            Example().run()
"""

__all__ = ("FitImage",)

from kivy.properties import OptionProperty
from kivy.uix.image import AsyncImage

from kivymd.uix.behaviors import StencilBehavior


class FitImage(AsyncImage, StencilBehavior):
    """
    Fit image class.

    For more information, see in the
    :class:`~kivy.uix.image.AsyncImage` and
    :class:`~kivymd.uix.behaviors.stencil_behavior.StencilBehavior`
    classes documentation.
    """

    fit_mode = OptionProperty(
        "cover", options=["scale-down", "fill", "contain", "cover"]
    )
    """
    Image will be stretched horizontally or vertically to fill the widget box,
    **maintaining its aspect ratio**. If the image has a different aspect ratio
    than the widget, then the image will be clipped to fit.

    :attr:`fit_mode` is a :class:`~kivy.properties.OptionProperty` and
    defaults to `'cover'`.
    """
