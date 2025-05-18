"""
Components/ScrollView
=====================

.. versionadded:: 1.0.0

:class:`~kivy.uix.scrollview.ScrollView` class equivalent.
It implements Material Design's overscorll effect and
simplifies working with some widget properties. For example:

ScrollView
----------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            ScrollView:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.scrollview import ScrollView
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = ScrollView()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDScrollView
------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDScrollView:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.scrollview import MDScrollView
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDScrollView(
                        md_bg_color=self.theme_cls.primaryColor
                    )

            MyApp().run()

The stretching effect
---------------------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            import os
            import sys

            from kivy.core.window import Window
            from kivy import __version__ as kv__version__
            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd import __version__
            from kivymd.uix.list import (
                MDListItem,
                MDListItemHeadlineText,
                MDListItemSupportingText,
                MDListItemLeadingIcon,
            )

            from materialyoucolor import __version__ as mc__version__


            MAIN_KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.backgroundColor

                MDScrollView:
                    do_scroll_x: False

                    MDBoxLayout:
                        id: main_scroll
                        orientation: "vertical"
                        adaptive_height: True

                        MDBoxLayout:
                            adaptive_height: True

                            MDLabel:
                                theme_font_size: "Custom"
                                text: "OS Info"
                                font_size: "55sp"
                                adaptive_height: True
                                padding: "10dp", "20dp", 0, 0

                            MDIconButton:
                                icon: "menu"
                                pos_hint: {"center_y": .5}
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(MAIN_KV)

                def on_start(self):
                    info = {
                        "Name": [
                            os.name,
                            (
                                "microsoft"
                                if os.name == "nt"
                                else ("linux" if os.uname()[0] != "Darwin" else "apple")
                            ),
                        ],
                        "Architecture": [os.uname().machine, "memory"],
                        "Hostname": [os.uname().nodename, "account"],
                        "Python Version": ["v" + sys.version, "language-python"],
                        "Kivy Version": ["v" + kv__version__, "alpha-k-circle-outline"],
                        "KivyMD Version": ["v" + __version__, "material-design"],
                        "MaterialYouColor Version": ["v" + mc__version__, "invert-colors"],
                        "Pillow Version": ["Unknown", "image"],
                        "Working Directory": [os.getcwd(), "folder"],
                        "Home Directory": [os.path.expanduser("~"), "folder-account"],
                        "Environment Variables": [os.environ, "code-json"],
                    }

                    try:
                        from PIL import __version__ as pil__version_

                        info["Pillow Version"] = ["v" + pil__version_, "image"]
                    except Exception:
                        pass

                    for info_item in info:
                        self.root.ids.main_scroll.add_widget(
                            MDListItem(
                                MDListItemLeadingIcon(
                                    icon=info[info_item][1],
                                ),
                                MDListItemHeadlineText(
                                    text=info_item,
                                ),
                                MDListItemSupportingText(
                                    text=str(info[info_item][0]),
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                            )
                        )

                    Window.size = [dp(350), dp(600)]


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            import os
            import sys

            from kivy.core.window import Window
            from kivy import __version__ as kv__version__
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd import __version__
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.label import MDLabel
            from kivymd.uix.list import (
                MDListItem,
                MDListItemHeadlineText,
                MDListItemSupportingText,
                MDListItemLeadingIcon,
            )

            from materialyoucolor import __version__ as mc__version__

            from kivymd.uix.screen import MDScreen
            from kivymd.uix.scrollview import MDScrollView


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDScrollView(
                                MDBoxLayout(
                                    MDBoxLayout(
                                        MDLabel(
                                            theme_font_size="Custom",
                                            text="OS Info",
                                            font_size="55sp",
                                            adaptive_height=True,
                                            padding=("10dp", "20dp", 0, 0),
                                        ),
                                        MDIconButton(
                                            icon="menu",
                                            pos_hint={"center_y": .5},
                                        ),
                                        adaptive_height=True
                                    ),
                                    id="main_scroll",
                                    orientation="vertical",
                                    adaptive_height=True,
                                ),
                                do_scroll_x=False
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def on_start(self):
                    info = {
                        "Name": [
                            os.name,
                            (
                                "microsoft"
                                if os.name == "nt"
                                else ("linux" if os.uname()[0] != "Darwin" else "apple")
                            ),
                        ],
                        "Architecture": [os.uname().machine, "memory"],
                        "Hostname": [os.uname().nodename, "account"],
                        "Python Version": ["v" + sys.version, "language-python"],
                        "Kivy Version": ["v" + kv__version__, "alpha-k-circle-outline"],
                        "KivyMD Version": ["v" + __version__, "material-design"],
                        "MaterialYouColor Version": ["v" + mc__version__, "invert-colors"],
                        "Pillow Version": ["Unknown", "image"],
                        "Working Directory": [os.getcwd(), "folder"],
                        "Home Directory": [os.path.expanduser("~"), "folder-account"],
                        "Environment Variables": [os.environ, "code-json"],
                    }

                    try:
                        from PIL import __version__ as pil__version_

                        info["Pillow Version"] = ["v" + pil__version_, "image"]
                    except Exception:
                        pass

                    for info_item in info:
                        self.root.get_ids().main_scroll.add_widget(
                            MDListItem(
                                MDListItemLeadingIcon(
                                    icon=info[info_item][1],
                                ),
                                MDListItemHeadlineText(
                                    text=info_item,
                                ),
                                MDListItemSupportingText(
                                    text=str(info[info_item][0]),
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                            )
                        )

                    Window.size = [dp(350), dp(600)]


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/stretch_over_scroll_stencil.gif
    :align: center
"""

from __future__ import annotations

__all__ = ("MDScrollView", "StretchOverScrollStencil")

import math

from kivy.animation import Animation
from kivy.effects.scroll import ScrollEffect
from kivy.graphics import Color, PopMatrix, PushMatrix, Scale
from kivy.uix.scrollview import ScrollView

from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior


class StretchOverScrollStencil(ScrollEffect):
    """
    Stretches the view on overscroll and absorbs
    velocity at start and end to convert to stretch.

    .. versionadded:: 2.0.0

    .. note:: This effect only works with
        :class:`kivymd.uix.scrollview.MDScrollView`.

    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """

    # Android constants.
    minimum_absorbed_velocity = 0
    maximum_velocity = 10000
    stretch_intensity = 0.016
    exponential_scalar = math.e / (1 / 3)
    scroll_friction = 0.015
    # Used in `absorb_impact` but for now it's not compatible with kivy so we
    # using are approx value.
    # fling_friction = 1.01
    approx_normailzer = 2e5

    # Duration to normalize scale
    # when touch up is received and view is stretched.
    duration_normailzer = 10

    scroll_view = None  # scroll view instance
    scroll_scale = None  # Scale instruction instance

    scale_axis = "y"  # axis of effect
    last_touch_pos = None  # used to calculate distance

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.friction = self.scroll_friction

    def clamp(self, value, min_val=0, max_val=0):
        return min(max(value, min_val), max_val)

    def is_top_or_bottom(self):
        return getattr(self.scroll_view, "scroll_" + self.scale_axis) in [1, 0]

    _should_absorb = True

    def on_value(self, stencil, scroll_distance):
        super().on_value(stencil, scroll_distance)
        if self.target_widget:
            if not all([self.scroll_view, self.scroll_scale]):
                self.scroll_view = self.target_widget.parent
                self.scroll_scale = self.scroll_view._internal_scale

            if self.is_top_or_bottom():
                if (
                    abs(self.velocity) > self.minimum_absorbed_velocity
                    and self._should_absorb  # only first time when reaches
                    # top or bottom
                ):
                    self.absorb_impact()
                self._should_absorb = False
            else:
                self._should_absorb = True

    def get_hw(self):
        return "height" if self.scale_axis == "y" else "width"

    def set_scale_origin(self):
        # Check if target size is small than scrollview
        # if yes don't stretch scroll view.
        if getattr(self.target_widget, self.get_hw()) < getattr(
            self.scroll_view, self.get_hw()
        ):
            return False

        self.scroll_scale.origin = [
            0 if self.scroll_view.scroll_x <= 0.5 else self.scroll_view.width,
            0 if self.scroll_view.scroll_y <= 0.5 else self.scroll_view.height,
        ]
        return True

    def absorb_impact(self):
        self.set_scale_origin()
        sanitized_velocity = self.clamp(
            abs(self.velocity), 1, self.maximum_velocity
        )
        # Approx implementation.
        new_scale = 1 + min(
            (sanitized_velocity / self.approx_normailzer),
            1 / 3,
        )
        init_anim = Animation(
            **{self.scale_axis: new_scale},
            d=(sanitized_velocity * 4) / 1e6,
        )
        init_anim.bind(on_complete=self.reset_scale)
        init_anim.start(self.scroll_scale)

    def get_component(self, pos):
        return pos[-1 if self.scale_axis == "y" else 1]

    def convert_overscroll(self, touch):
        if (
            self.scroll_view
            and self.scroll_view.collide_point(*touch.pos)
            and self.is_top_or_bottom()
            and getattr(self.scroll_view, "do_scroll_" + self.scale_axis)
            and self.velocity == 0
            and self.set_scale_origin()  # sets stretch direction
        ):
            # Distance travelled by touch divided by size of scrollview.
            distance = (
                abs(
                    self.get_component(touch.pos)
                    - self.get_component(self.last_touch_pos)
                )
                / self.scroll_view.height
            )
            # Constant scale due to distance.
            linear_intensity = self.stretch_intensity * distance
            # Far the touch -> less it stretches.
            exponential_intensity = self.stretch_intensity * (
                1 - math.exp(-distance * self.exponential_scalar)
            )
            new_scale = 1 + exponential_intensity + linear_intensity
            setattr(self.scroll_scale, self.scale_axis, new_scale)

    def reset_scale(self, *arg):
        if not self.scroll_scale:
            return
        _scale = getattr(self.scroll_scale, self.scale_axis)
        if _scale > 1:
            anim = Animation(
                **{self.scale_axis: 1},
                d=0.2,
            )
            anim.start(self.scroll_scale)


class MDScrollView(DeclarativeBehavior, BackgroundColorBehavior, ScrollView):
    """
    An approximate implementation to Material Design's overscorll effect.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.scrollview.ScrollView`
    classes documentation.
    """

    _internal_scale = None

    def __init__(self, *args, **kwargs):
        self.effect_cls = StretchOverScrollStencil
        super().__init__(*args, **kwargs)
        with self.canvas.before:
            Color(rgba=self.md_bg_color)
            PushMatrix()
            self._internal_scale = Scale()
        with self.canvas.after:
            PopMatrix()
        self.effect_y.scale_axis = "y"
        self.effect_x.scale_axis = "x"

    def on_touch_down(self, touch):
        self.effect_x.last_touch_pos = touch.pos
        self.effect_y.last_touch_pos = touch.pos
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        try:
            self.effect_x.convert_overscroll(touch)
            self.effect_y.convert_overscroll(touch)
        except AttributeError:
            pass

        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        try:
            self.effect_x.reset_scale()
            self.effect_y.reset_scale()
        except AttributeError:
            pass

        super().on_touch_up(touch)
