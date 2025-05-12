"""
Components/FitImage
===================

Example
=======

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDBoxLayout:
                    radius: "36dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint: .4, .8
                    md_bg_color: self.theme_cls.onSurfaceVariantColor

                    FitImage:
                        source: "image.png"
                        size_hint_y: .35
                        pos_hint: {"top": 1}
                        radius: "36dp", "36dp", 0, 0
            '''


            class Example(MDApp):
                def build(self):
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
                    return (
                        MDScreen(
                            MDBoxLayout(
                                FitImage(
                                    source="image.png",
                                    size_hint_y=0.35,
                                    pos_hint={"top": 1},
                                    radius=(dp(36), dp(36), 0, 0),
                                ),
                                radius=dp(36),
                                md_bg_color=self.theme_cls.onSurfaceVariantColor,
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                size_hint=(0.4, 0.8),
                            ),
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fitimage-round-corners.png
    :align: center
"""

__all__ = ("FitImage",)

from kivy.properties import OptionProperty
from kivy.uix.image import AsyncImage

from kivymd.uix.behaviors import DeclarativeBehavior, StencilBehavior


class FitImage(DeclarativeBehavior, StencilBehavior, AsyncImage):
    """
    Fit image class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
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
