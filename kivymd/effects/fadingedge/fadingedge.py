"""
Effects/FadingEdgeEffect
========================

.. versionadded:: 1.0.0

The `FadingEdgeEffect` class implements a fade effect for `KivyMD` widgets:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.scrollview import ScrollView

    from kivymd.app import MDApp
    from kivymd.effects.fadingedge.fadingedge import FadingEdgeEffect
    from kivymd.uix.list import OneLineListItem

    KV = '''
    MDScreen:

        FadeScrollView:
            fade_height: self.height / 2
            fade_color: root.md_bg_color

            MDList:
                id: container
    '''


    class FadeScrollView(FadingEdgeEffect, ScrollView):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(20):
                self.root.ids.container.add_widget(
                    OneLineListItem(text=f"Single-line item {i}")
                )


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fading-edge-effect-white.gif
    :align: center

.. note:: Use the same color value for the fade_color parameter as for the
    parent widget.
"""

from typing import NoReturn, Union

from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ColorProperty, NumericProperty

from kivymd.theming import ThemableBehavior

__all_ = ("FadingEdgeEffect",)


class FadingEdgeEffect(ThemableBehavior):
    """
    The class implements the fade effect.

    .. versionadded:: 1.0.0
    """

    fade_color = ColorProperty(None)
    """
    Fade color.

    :attr:`fade_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    fade_height = NumericProperty(0)
    """
    Fade height.

    :attr:`fade_height` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `0`.
    """

    edge_top = BooleanProperty(True)
    """
    Display fade edge top.

    :attr:`edge_top` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    edge_bottom = BooleanProperty(True)
    """
    Display fade edge bottom.

    :attr:`edge_bottom` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    _height_segment = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_fade)

    # TODO: Perhaps it would be better if we used a Shader for the fade effect.
    #  But, I think the canvas instructions shouldn't affect performance
    def set_fade(self, interval: Union[int, float]) -> NoReturn:
        """Draws a bottom and top fade border on the canvas."""

        fade_color = (
            self.theme_cls.primary_color
            if not self.fade_color
            else self.fade_color
        )
        height_segment = (
            self.fade_height if self.fade_height else dp(100)
        ) // self._height_segment
        alpha = 1.1

        with self.canvas:
            for i in range(self._height_segment):
                alpha -= 0.1

                Color(rgba=(fade_color[:-1] + [round(alpha, 1)]))
                rectangle_top = (
                    Rectangle(
                        pos=(self.x, self.height - (i * height_segment)),
                        size=(self.width, height_segment),
                    )
                    if self.edge_top
                    else None
                )
                rectangle_bottom = (
                    Rectangle(
                        pos=(self.x, i * height_segment),
                        size=(self.width, height_segment),
                    )
                    if self.edge_bottom
                    else None
                )
                # How I hate lambda functions because of their length :(
                # But I don’t want to call the arguments by short,
                # incomprehensible names 'a', 'b', 'c'.
                self.bind(
                    pos=lambda instance_fadind_edge_effect, window_size, rectangle_top=rectangle_top, rectangle_bottom=rectangle_bottom, index=i: self.update_canvas(
                        instance_fadind_edge_effect,
                        window_size,
                        rectangle_top,
                        rectangle_bottom,
                        index,
                    ),
                    size=lambda instance_fadind_edge_effect, window_size, rectangle_top=rectangle_top, rectangle_bottom=rectangle_bottom, index=i: self.update_canvas(
                        instance_fadind_edge_effect,
                        window_size,
                        rectangle_top,
                        rectangle_bottom,
                        index,
                    ),
                )

    def update_canvas(
        self,
        instance_fadind_edge_effect,
        size: list[int, int],
        rectangle_top: Rectangle,
        rectangle_bottom: Rectangle,
        index: int,
    ) -> NoReturn:
        """
        Updates the position and size of the fade border on the canvas.
        Called when the application screen is resized.
        """

        height_segment = (
            self.fade_height if self.fade_height else dp(100)
        ) // self._height_segment

        if rectangle_top:
            rectangle_top.pos = (
                instance_fadind_edge_effect.x,
                size[1]
                - (index * height_segment - instance_fadind_edge_effect.y),
            )
            rectangle_top.size = (size[0], height_segment)
        if rectangle_bottom:
            rectangle_bottom.pos = (
                instance_fadind_edge_effect.x,
                index * height_segment + instance_fadind_edge_effect.y,
            )
            rectangle_bottom.size = (size[0], height_segment)
