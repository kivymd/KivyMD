"""
Components/Tilt Parallax Card
=============================

.. versionadded:: 2.0.1

.. rubric:: A 3D parallax card widget with dynamic layer displacement for
    pop-out effects.

Features
--------

- Layered `3D Parallax Effect`: Separates the visual components into distinct
    `3D Z-layers` using `RenderContext` and dynamic matrix transformations
    based on cursor movement.
- `Pop-Out Visual Depth`: Allows foreground elements (characters, objects,
    or key visual assets) to break past the card’s physical boundary using
    configurable scale (`foreground_scale`) and depth offsets
    (`foreground_z_offset`).

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-anatomy.png
    :align: center

Base example
------------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen


            KV = '''
            <MyScreen>
                md_bg_color: "#061420"

                TiltParallaxCard:
                    card_size: dp(220), dp(320)
                    foreground_scale: 0.85
                    foreground_z_offset: dp(35)
                    text_z_offset: dp(50)
                    corner_radius: dp(24)
                    pos_hint: {"center_x": .5, "center_y": .5}
                    max_tilt_angle: 1

                    TiltBackgroundImage:
                        source: "background.png"

                    TiltForegroundImage:
                        source: "foreground.png"

                    TiltTextContainer:
                        spacing: dp(4)

                        MDLabel:
                            text: "IbaneZ"
                            font_style: "Display"
                            theme_line_height: "Custom"
                            line_height: dp(0.5)
                            role: "medium"
                            bold: True
                            adaptive_height: True
                            theme_text_color: "Custom"
                            text_color: "#F2DCB6"

                        MDLabel:
                            text:
                                "• Body: Mahogany/Poplar\\n" \
                                "• Neck: 3-pc Maple\\n" \
                                "• Fretboard: Rosewood\\n" \
                                "• Pickups: H-S-H Configuration\\n" \
                                "• Frets: 24 Jumbo"
                            bold: True
                            font_style: "Label"
                            role: "small"
                            adaptive_height: True
                            theme_text_color: "Custom"
                            text_color: "white"
            '''


            class MyScreen(MDScreen):
                ...


            class ParallaxTest(MDApp):
                def build(self):
                    Builder.load_string(KV)
                    return MyScreen()


            ParallaxTest().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.tilt import TiltParallaxCard, TiltTextContainer


            class MyScreen(MDScreen):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)

                    self.md_bg_color = "#061420"
                    self.widgets = [
                        TiltParallaxCard(
                            TiltBackgroundImage(
                                source="background.png",
                            ),
                            TiltForegroundImage(
                                source="foreground.png",
                            ),
                            TiltTextContainer(
                                MDLabel(
                                    text="IbaneZ",
                                    font_style="Display",
                                    role="medium",
                                    theme_line_height="Custom",
                                    line_height=0.5,
                                    bold=True,
                                    adaptive_height=True,
                                    theme_text_color="Custom",
                                    text_color="#F2DCB6",
                                ),
                                MDLabel(
                                    text=(
                                        "• Body: Mahogany/Poplar\n"
                                        "• Neck: 3-pc Maple\n"
                                        "• Fretboard: Rosewood\n"
                                        "• Pickups: H-S-H Configuration\n"
                                        "• Frets: 24 Jumbo"
                                    ),
                                    font_style="Label",
                                    role="small",
                                    bold=True,
                                    adaptive_height=True,
                                    theme_text_color="Custom",
                                    text_color="white",
                                ),
                                spacing="4dp",
                            ),
                            card_size=(dp(220), dp(320)),
                            foreground_scale=0.85,
                            foreground_z_offset="35dp",
                            text_z_offset="50dp",
                            corner_radius="24dp",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            max_tilt_angle=1,
                        )
                    ]


            class ParallaxTest(MDApp):
                def build(self):
                    return MyScreen()


            ParallaxTest().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-base-example.gif
    :align: center
"""

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import MatrixInstruction, RenderContext
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget

from kivymd.uix.behaviors import DeclarativeBehavior, TiltBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.tilt.tiltcard import TiltTextContainer

__all__ = (
    "TiltParallaxCard",
    "TiltBackgroundImage",
    "TiltForegroundImage",
)


class TiltBackgroundImage(AsyncImage):
    """
    Background layer widget for :class:`~TiltParallaxCard`.

    For more information, see in the :class:`~kivy.uix.image.AsyncImage`
    class documentation.
    """


class TiltForegroundImage(AsyncImage):
    """
    Foreground (pop-out) layer widget for :class:`~TiltParallaxCard`.

    For more information, see in the :class:`~kivy.uix.image.AsyncImage`
    class documentation.
    """


class TiltParallaxCard(DeclarativeBehavior, TiltBehavior, Widget):
    """
    3D Parallax Card widget with dynamic 3D depth pop-out effect.
    Renders background, foreground, and content in separated 3D Z-layers to
    create a dynamic parallax effect on mouse movement.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.tilt_behavior.TiltBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.
    """

    background_source = StringProperty("")
    """
    URL or path to the background image.

    :attr:`background_source` is a :class:`~kivy.properties.StringProperty`
    and defaults to ''.
    """

    foreground_source = StringProperty("")
    """
    URL or path to the foreground (character or pop-out object) image.

    :attr:`foreground_source` is a :class:`~kivy.properties.StringProperty`
    and defaults to ''.
    """

    foreground_scale = NumericProperty(1.25)
    """
    Scale multiplier for the foreground image relative to card dimensions.

    .. code-block:: python

        TiltParallaxCard(
            foreground_scale=1.25,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-foreground-scale-1-25.png
        :align: center

    .. code-block:: python

        TiltParallaxCard(
            foreground_scale=0.5,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-foreground-scale-0-5.png
        :align: center

    :attr:`foreground_scale` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1.25`.
    """

    foreground_z_offset = NumericProperty(dp(35))
    """
    Z-axis depth displacement for the foreground layer in 3D space.

    .. code-block:: python

        TiltParallaxCard(
            foreground_z_offset=35,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-foreground-z-offset-35.png
        :align: center

    .. code-block:: python

        TiltParallaxCard(
            foreground_z_offset=10,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-foreground-z-offset-0.png
        :align: center

    :attr:`foreground_z_offset` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(35)`.
    """

    parallax_x_offset = NumericProperty(dp(40))
    """
    Maximum horizontal displacement offset applied to foreground on mouse tilt.

    .. code-block:: python

        TiltParallaxCard(
            parallax_x_offset=dp(200),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-parallax-x-offset-200.gif
        :align: center

    .. code-block:: python

        TiltParallaxCard(
            parallax_x_offset=dp(40),
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-parallax-card-parallax-x-offset-40.gif
        :align: center

    :attr:`parallax_x_offset` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(40)`.
    """

    parallax_y_offset = NumericProperty(dp(40))
    """
    Maximum vertical displacement offset applied to foreground on mouse tilt.

    :attr:`parallax_y_offset` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(40)`.
    """

    text_z_offset = NumericProperty(dp(50))
    """
    Z-axis depth displacement for the text container layer.

    :attr:`text_z_offset` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(50)`.
    """

    container_pos = ListProperty([dp(15), dp(15)])
    """
    Position tuple `(x, y)` for placing the text container relative to
    bottom-left corner.

    :attr:`container_pos` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(15), dp(15)]`.
    """

    _bg_image = ObjectProperty(None, allownone=True)
    _fg_image = ObjectProperty(None, allownone=True)
    _text_container = ObjectProperty(None, allownone=True)

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = self.card_size

        for arg in args:
            if isinstance(arg, TiltBackgroundImage):
                self._bg_image = arg
            elif isinstance(arg, TiltForegroundImage):
                self._fg_image = arg
            elif isinstance(arg, TiltTextContainer):
                self._text_container = arg

        Clock.schedule_once(self._delayed_setup)
        self.bind(card_size=self._update_card_size)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, TiltBackgroundImage):
            self._bg_image = widget
            return
        elif isinstance(widget, TiltForegroundImage):
            self._fg_image = widget
            return
        elif isinstance(widget, TiltTextContainer):
            self._text_container = widget
            return

        super().add_widget(widget, *args, **kwargs)

    def _delayed_setup(self, *args):
        """
        Deferred callback triggered by :class:`~kivy.clock.Clock` to complete
        3D layer setup and attach mouse listeners once widget hierarchy is
        ready.
        """

        self._setup_layers()
        Window.bind(mouse_pos=self._on_mouse_pos)

    def _update_card_size(self, instance, value):
        """
        Recalculates card geometry, background placement, and foreground bounds
        when :attr:`card_size` changes.
        """

        card_w, card_h = value
        self.size = value

        if self._bg_image:
            self._bg_image.size = (card_w, card_h)
            self._bg_image.pos = (-card_w / 2.0, -card_h / 2.0)

        self._update_fg_geometry()

    def _update_fg_geometry(self):
        """
        Recalculates physical dimensions and centers the foreground image
        relative to the card's local center point based on
        :attr:`foreground_scale`.
        """

        if not self._fg_image:
            return

        card_w, card_h = self.card_size
        fg_w = card_w * self.foreground_scale
        fg_h = card_h * self.foreground_scale

        self._fg_image.size_hint = (None, None)
        self._fg_image.size = (fg_w, fg_h)
        self._fg_image.pos = (-fg_w / 2.0, -fg_h / 2.0)

    def _setup_layers(self, *args):
        """
        Constructs and appends dedicated :class:`~kivy.graphics.RenderContext`
        layers for foreground and text components to :attr:`canvas.after` to
        enable 3D depth transformations along the Z-axis.
        """

        card_w, card_h = self.card_size

        # Setup Background Layer.
        if self._bg_image and not hasattr(self, "_bg_attached"):
            self._bg_attached = True
            self._bg_image.size_hint = (None, None)
            self._bg_image.size = (card_w, card_h)
            self._bg_image.pos = (-card_w / 2.0, -card_h / 2.0)
            self.canvas.add(self._bg_image.canvas)

        # Setup Foreground Layer (3D RenderContext).
        if self._fg_image and not hasattr(self, "_fg_attached"):
            self._fg_attached = True
            self._update_fg_geometry()

            self._fg_context = RenderContext(
                use_parent_modelview=True,
                use_parent_projection=True,
            )

            with self._fg_context:
                self._fg_transform = MatrixInstruction()
                self._fg_transform.matrix = Matrix().translate(
                    0, 0, self.foreground_z_offset
                )
                self._fg_context.add(self._fg_image.canvas)

            self.canvas.after.add(self._fg_context)

        # Setup Container Layer (3D RenderContext).
        if self._text_container and not hasattr(self, "_container_attached"):
            self._container_attached = True
            max_text_width = card_w - (self.container_pos[0] * 2)

            self._text_container.size_hint = (None, None)
            self._text_container.width = max_text_width

            for child in self._text_container.children:
                if isinstance(child, MDLabel):
                    child.size_hint_x = None
                    child.width = max_text_width
                    child.text_size = (max_text_width, None)

            self._text_container.do_layout()

            self._start_x = (-card_w / 2.0) + self.container_pos[0]
            self._start_y = (-card_h / 2.0) + self.container_pos[1]
            self._text_container.pos = (0, 0)

            self._text_context = RenderContext(
                use_parent_modelview=True,
                use_parent_projection=True,
            )

            with self._text_context:
                self._text_transform = MatrixInstruction()
                self._text_transform.matrix = Matrix().translate(
                    self._start_x, self._start_y, self.text_z_offset
                )
                self._text_context.add(self._text_container.canvas)

            self.canvas.after.add(self._text_context)

    def _on_mouse_pos(self, window, pos):
        """
        Mouse motion callback that calculates normalized mouse position
        relative to the card center and applies 3D translation matrices to the
        foreground and text layers. Resets transformations when the mouse
        leaves card bounds.
        """

        if not self.get_root_window() or not hasattr(self, "_fg_transform"):
            return

        cx, cy = self.to_window(*self.center)
        w, h = self.size

        if not w or not h:
            return

        rel_x = max(-1.0, min(1.0, (pos[0] - cx) / (w / 2.0)))
        rel_y = max(-1.0, min(1.0, (pos[1] - cy) / (h / 2.0)))

        if self.collide_point(*pos):
            fg_shift_x = rel_x * self.parallax_x_offset
            fg_shift_y = rel_y * self.parallax_y_offset

            self._fg_transform.matrix = Matrix().translate(
                fg_shift_x, fg_shift_y, self.foreground_z_offset
            )

            if hasattr(self, "_text_transform"):
                text_shift_x = self._start_x + (
                    rel_x * self.parallax_x_offset * 0.4
                )
                text_shift_y = self._start_y + (
                    rel_y * self.parallax_y_offset * 0.4
                )

                self._text_transform.matrix = Matrix().translate(
                    text_shift_x, text_shift_y, self.text_z_offset
                )
        else:
            self._fg_transform.matrix = Matrix().translate(
                0, 0, self.foreground_z_offset
            )

            if hasattr(self, "_text_transform"):
                self._text_transform.matrix = Matrix().translate(
                    self._start_x, self._start_y, self.text_z_offset
                )
