"""
Components/FitImage
===================

Example
=======

.. tabs::

    .. tab:: Imperative Python Styles

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


    .. tab:: Declarative Python Styles

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
from materialshapes.kivy_widget import MaterialShape

from kivymd.uix.behaviors import DeclarativeBehavior, StencilBehavior


class FitImage(DeclarativeBehavior, StencilBehavior, MaterialShape, AsyncImage):
    """
    Fit image class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.stencil_behavior.StencilBehavior` and
    :class:`~materialshapes.kivy_widget.MaterialShape` and
    :class:`~kivy.uix.image.AsyncImage` and
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

    shape = OptionProperty(
        None,
        options=[
            "circle",
            "square",
            "slanted",
            "arch",
            "semiCircle",
            "oval",
            "pill",
            "triangle",
            "arrow",
            "fan",
            "diamond",
            "clamShell",
            "pentagon",
            "gem",
            "sunny",
            "verySunny",
            "cookie4Sided",
            "cookie6Sided",
            "cookie7Sided",
            "cookie9Sided",
            "cookie12Sided",
            "clover4Leaf",
            "clover8Leaf",
            "burst",
            "softBurst",
            "boom",
            "softBoom",
            "flower",
            "puffy",
            "puffyDiamond",
            "ghostish",
            "pixelCircle",
            "pixelTriangle",
            "bun",
            "heart",
        ],
    )
    """
    The Material shape style applied to the image clipping mask.

    .. versionadded:: 2.0.1

    Available shape options are: `'circle'`, `'square'`, `'slanted'`, `'arch'`,
    `'semiCircle'`, `'oval'`, `'pill'`, `'triangle'`, `'arrow'`, `'fan'`,
    `'diamond'`, `'clamShell'`, `'pentagon'`, `'gem'`, `'sunny'`,
    `'verySunny'`, `'cookie4Sided'`, `'cookie6Sided'`, `'cookie7Sided'`,
    `'cookie9Sided'`, `'cookie12Sided'`, `'clover4Leaf'`, `'clover8Leaf'`,
    `'burst'`, `'softBurst'`, `'boom'`, `'softBoom'`, `'flower'`, `'puffy'`,
    `'puffyDiamond'`, `'ghostish'`, `'pixelCircle'`, `'pixelTriangle'`,
    `'bun'`, `'heart'`.

    If set to ``None``, the image will be rendered as a standard rectangle.

    :attr:`shape` is an :class:`~kivy.properties.OptionProperty` and
    defaults to `None`.

    .. tabs::

        .. tab:: Imperative Python Styles

            .. code-block:: python

                from kivy.lang import Builder
                from kivy.metrics import dp

                from kivymd.app import MDApp
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.fitimage import FitImage
                from kivymd.uix.label import MDLabel

                KV = '''
                MDScreen:
                    md_bg_color: app.theme_cls.surfaceColor

                    MDScrollView:

                        MDGridLayout:
                            id: shape_grid
                            cols: 6
                            adaptive_height: True
                            padding: dp(16)
                            spacing: dp(16)
                '''


                class ExampleApp(MDApp):
                    SHAPES = [
                        "circle",
                        "square",
                        "slanted",
                        "arch",
                        "semiCircle",
                        "oval",
                        "pill",
                        "triangle",
                        "arrow",
                        "fan",
                        "diamond",
                        "clamShell",
                        "pentagon",
                        "gem",
                        "sunny",
                        "verySunny",
                        "cookie4Sided",
                        "cookie6Sided",
                        "cookie7Sided",
                        "cookie9Sided",
                        "cookie12Sided",
                        "clover4Leaf",
                        "clover8Leaf",
                        "burst",
                        "softBurst",
                        "boom",
                        "softBoom",
                        "flower",
                        "puffy",
                        "puffyDiamond",
                        "ghostish",
                        "pixelCircle",
                        "pixelTriangle",
                        "bun",
                        "heart",
                    ]
                    IMAGE_PATH = "bg.jpg"

                    def build(self):
                        return Builder.load_string(KV)

                    def on_start(self):
                        grid = self.root.ids.shape_grid

                        for shape_name in self.SHAPES:
                            item_box = MDBoxLayout(
                                orientation="vertical",
                                adaptive_height=True,
                                spacing=dp(8),
                            )

                            shape_widget = FitImage(
                                size_hint=(None, None),
                                size=(dp(90), dp(90)),
                                pos_hint={"center_x": 0.5},
                                shape=shape_name,
                                source=self.IMAGE_PATH,
                            )

                            label = MDLabel(
                                text=shape_name,
                                halign="center",
                                adaptive_height=True,
                                font_style="Label",
                                role="medium",
                            )

                            item_box.add_widget(shape_widget)
                            item_box.add_widget(label)
                            grid.add_widget(item_box)


                if __name__ == "__main__":
                    ExampleApp().run()

        .. tab:: Declarative Python Styles

            .. code-block:: python

                from kivy.metrics import dp

                from kivymd.app import MDApp
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.fitimage import FitImage
                from kivymd.uix.gridlayout import MDGridLayout
                from kivymd.uix.label import MDLabel
                from kivymd.uix.scrollview import MDScrollView
                from kivymd.uix.screen import MDScreen


                class ExampleApp(MDApp):
                    SHAPES = [
                        "circle",
                        "square",
                        "slanted",
                        "arch",
                        "semiCircle",
                        "oval",
                        "pill",
                        "triangle",
                        "arrow",
                        "fan",
                        "diamond",
                        "clamShell",
                        "pentagon",
                        "gem",
                        "sunny",
                        "verySunny",
                        "cookie4Sided",
                        "cookie6Sided",
                        "cookie7Sided",
                        "cookie9Sided",
                        "cookie12Sided",
                        "clover4Leaf",
                        "clover8Leaf",
                        "burst",
                        "softBurst",
                        "boom",
                        "softBoom",
                        "flower",
                        "puffy",
                        "puffyDiamond",
                        "ghostish",
                        "pixelCircle",
                        "pixelTriangle",
                        "bun",
                        "heart",
                    ]
                    IMAGE_PATH = "bg.jpg"

                    def build(self):
                        return MDScreen(
                            MDScrollView(
                                MDGridLayout(
                                    *[
                                        MDBoxLayout(
                                            FitImage(
                                                size_hint=(None, None),
                                                size=(dp(90), dp(90)),
                                                pos_hint={"center_x": 0.5},
                                                shape=shape_name,
                                                source=self.IMAGE_PATH,
                                            ),
                                            MDLabel(
                                                text=shape_name,
                                                halign="center",
                                                adaptive_height=True,
                                                font_style="Label",
                                                role="medium",
                                            ),
                                            orientation="vertical",
                                            adaptive_height=True,
                                            spacing=dp(8),
                                        )
                                        for shape_name in self.SHAPES
                                    ],
                                    cols=6,
                                    adaptive_height=True,
                                    padding=dp(16),
                                    spacing=dp(16),
                                )
                            ),
                            md_bg_color=self.theme_cls.surfaceColor,
                        )


                if __name__ == "__main__":
                    ExampleApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fitimage-shapes.png
        :align: center
    """

    def on_source(self, instance, value):
        """Fired when the :attr:`source` value changes."""

        # Redirecting the path from `source` directly to `MaterialShape.image`.
        self.image = value

    def update_texture(self, *args):
        """
        Updates the widget texture.

        If a custom Material :attr:`shape` is set, delegates texture generation
        to :meth:`materialshapes.kivy_widget.MaterialShape.update_texture`.
        This builds a Cairo surface based on the target shape dimensions,
        applies the image pattern (or fill color), and renders the resulting
        vector mask directly to the Kivy :attr:`texture`.

        If :attr:`shape` is ``None``, execution falls back to standard GPU
        texture rendering via :class:`~kivy.uix.image.AsyncImage`.
        """

        # If the Material shape is specified, we use the MaterialShape logic.
        if self.shape:
            super().update_texture(*args)
            return

    def _get_shape_path(self, ctx):
        # If the shape is not specified (shape=None), we fill the entire
        # context with a rectangle.
        if not self.shape:
            ctx.rectangle(0, 0, 1, 1)
            return

        super()._get_shape_path(ctx)

    def _load_source(self, *args):
        # Block the standard loading of AsyncImage so that it doesn't create
        # self.texture or draw a rectangle.
        if self.shape:
            return

        super()._load_source(*args)
