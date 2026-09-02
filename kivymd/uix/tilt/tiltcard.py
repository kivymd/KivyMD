"""
Components/Tilt card
====================

.. versionadded:: 2.0.1

.. rubric:: The :class:`~TiltCard` widget is a ready-to-use 3D interactive card
    that combines background image loading, custom 3D projection, and floating
    text layers into a single component powered by
    :class:`~kivymd.uix.behaviors.tilt_behavior.TiltBehavior`.

Features
--------

- Asynchronous Image Loading with Aspect Ratio Support: Uses :class:`~kivymd.uix.fitimage.FitImage`
  to fetch, scale, and cover card background spaces seamlessly.
- Floating Parallax Text Container: Supports a specialized
  :class:`~TiltTextContainer` that automatically positions and floats text
  content above the card using 3D translation matrices.
- Responsive Text Wrapping: Automatically calculates available dimensions and wraps
  inner :class:`~kivymd.uix.label.label.MDLabel` instances to prevent text
  overflowing the card boundaries.

Base example
------------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen

            KV = '''
            <MyScreen>:
                md_bg_color: self.theme_cls.backgroundColor

                TiltCard:
                    source: "bg.png"
                    card_size: dp(200), dp(340)
                    container_pos: dp(15), dp(15)
                    corner_radius: 24
                    pos_hint: {"center_x": .5, "center_y": .5}

                    TiltTextContainer:
                        spacing: dp(4)

                        MDLabel:
                            text: "Grey-winged\\nBlackbird"
                            font_style: "Title"
                            role: "small"
                            bold: True
                            adaptive_height: True
                            theme_text_color: "Custom"
                            text_color: "white"

                        MDLabel:
                            text: "Turdus boulboul • Himalayas"
                            font_style: "Body"
                            role: "small"
                            adaptive_height: True
                            theme_text_color: "Custom"
                            text_color: "white"
            '''


            class MyScreen(MDScreen):
                pass


            class TiltTest(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    Builder.load_string(KV)

                    return MyScreen()


            TiltTest().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.tilt import TiltCard, TiltTextContainer


            class MyScreen(MDScreen):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    self.md_bg_color = self.theme_cls.backgroundColor
                    self.widgets = [
                        TiltCard(
                            TiltTextContainer(
                                MDLabel(
                                    text="Grey-winged\\nBlackbird",
                                    font_style="Title",
                                    role="small",
                                    bold=True,
                                    adaptive_height=True,
                                    theme_text_color="Custom",
                                    text_color="white",
                                ),
                                MDLabel(
                                    text="Turdus boulboul • Himalayas",
                                    font_style="Body",
                                    role="small",
                                    adaptive_height=True,
                                    theme_text_color="Custom",
                                    text_color="white",
                                ),
                                spacing=dp(4)
                            ),
                            source='bg.png',
                            card_size=(dp(200), dp(340)),
                            container_pos=(dp(15), dp(15)),
                            corner_radius=24,
                            pos_hint={"center_x": .5, "center_y": .5}
                        )
                    ]


            class TiltTest(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return MyScreen()


            TiltTest().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-card-base-example.gif
    :align: center
"""

from kivy.clock import Clock
from kivy.graphics import MatrixInstruction, RenderContext
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from kivymd.uix.behaviors import DeclarativeBehavior, TiltBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel

__all__ = (
    "TiltTextContainer",
    "TiltCard",
)


class TiltTextContainer(MDBoxLayout):
    """
    A vertical layout container specifically designed to hold text elements
    inside a :class:`~TiltCard`.
    It automatically adapts its height to its children.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout`
    class documentation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"
        self.adaptive_height = True


class TiltCard(DeclarativeBehavior, TiltBehavior, Widget):
    """
    A 3D interactive card widget.

    Inherits from :class:`~kivymd.uix.behaviors.tilt_behavior.TiltBehavior`
    (providing the 3D projection, glare, and parallax shaders) and the standard
    Kivy :class:`~kivy.uix.widget.Widget`. Uses :class:`~kivymd.uix.fitimage.FitImage`
    to render aspect-ratio corrected background images.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.tilt_behavior.TiltBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.
    """

    source = StringProperty("")
    """
    URL or path to the background image.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `""`.
    """

    container = ObjectProperty(None, allownone=True)
    """
    Reference to the child text container.

    :attr:`container` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    container_pos = ListProperty([dp(15), dp(15)])
    """
    X and Y padding/offset for the text container from the bottom-left corner.

    :attr:`container_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(15), dp(15)]`.
    """

    def __init__(self, container=None, **kwargs):
        self._fit_image = FitImage()

        passed_container = container

        super().__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = self.card_size

        if passed_container:
            self.container = passed_container

        card_w, card_h = self.card_size
        self._fit_image.size_hint = (None, None)
        self._fit_image.size = (card_w, card_h)
        self._fit_image.pos = (-card_w / 2.0, -card_h / 2.0)

        # We attach the FitImage canvas to the card's main canvas.
        self.canvas.add(self._fit_image.canvas)

        if self.source:
            self._fit_image.source = self.source

        if self.container and not hasattr(self, "_container_attached"):
            Clock.schedule_once(self._setup_container)

        self.bind(
            source=self._update_source,
            card_size=self._update_rect_size,
        )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, TiltTextContainer):
            self.container = widget
            Clock.schedule_once(self._setup_container)

            return

        super().add_widget(widget, *args, **kwargs)

    def _update_source(self, instance, value):
        """Updates the FitImage source property."""

        if value:
            self._fit_image.source = value

    def _update_rect_size(self, instance, value):
        """Synchronizes widget dimensions and FitImage geometry."""

        card_w, card_h = value
        self.size = value
        self._fit_image.size = (card_w, card_h)
        self._fit_image.pos = (-card_w / 2.0, -card_h / 2.0)

    def _setup_container(self, *args):
        """
        Calculates the available width for the text, forces child MDLabels to
        wrap properly, and applies a translation matrix to float the text above
        the card in an isolated RenderContext.
        """

        if not self.container:
            return

        card_w, card_h = self.card_size
        max_text_width = card_w - (self.container_pos[0] * 2)

        self.container.size_hint = (None, None)
        self.container.width = max_text_width

        for child in self.container.children:
            if isinstance(child, MDLabel):
                child.size_hint_x = None
                child.width = max_text_width
                child.text_size = (max_text_width, None)

        self.container.do_layout()

        start_x = (-card_w / 2.0) + self.container_pos[0]
        start_y = (-card_h / 2.0) + self.container_pos[1]
        self.container.pos = (0, 0)

        if not hasattr(self, "_container_attached"):
            self._container_attached = True
            self._text_context = RenderContext(
                use_parent_modelview=True,
                use_parent_projection=True,
            )

            with self._text_context:
                self._text_transform = MatrixInstruction()
                self._text_transform.matrix = Matrix().translate(
                    start_x, start_y, self.text_z_offset
                )
                self._text_context.add(self.container.canvas)

            self.canvas.after.add(self._text_context)
        else:
            self._text_transform.matrix = Matrix().translate(
                start_x, start_y, self.text_z_offset
            )
