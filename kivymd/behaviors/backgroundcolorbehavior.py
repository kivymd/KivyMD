"""
Background Color Behavior
=========================

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

from kivy.lang import Builder
from kivy.properties import BoundedNumericProperty, ReferenceListProperty
from kivy.properties import OptionProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import palette, hue, text_colors

Builder.load_string(
    """
<BackgroundColorBehavior>
    canvas:
        Color:
            rgba: self.md_bg_color
        Rectangle:
            size: self.size
            pos: self.pos
"""
)


class BackgroundColorBehavior(Widget):
    r = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    g = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    b = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    a = BoundedNumericProperty(0.0, min=0.0, max=1.0)

    md_bg_color = ReferenceListProperty(r, g, b, a)


class SpecificBackgroundColorBehavior(BackgroundColorBehavior):
    background_palette = OptionProperty(
        "Primary", options=["Primary", "Accent", *palette]
    )
    background_hue = OptionProperty("500", options=hue)

    specific_text_color = ListProperty([0, 0, 0, 0.87])
    specific_secondary_text_color = ListProperty([0, 0, 0, 0.87])

    def _update_specific_text_color(self, instance, value):
        if hasattr(self, "theme_cls"):
            palette = {
                "Primary": self.theme_cls.primary_palette,
                "Accent": self.theme_cls.accent_palette,
            }.get(self.background_palette, self.background_palette)
        else:
            palette = {"Primary": "Blue", "Accent": "Amber"}.get(
                self.background_palette, self.background_palette
            )
        color = get_color_from_hex(text_colors[palette][self.background_hue])
        secondary_color = color[:]
        # Check for black text (need to adjust opacity)
        if (color[0] + color[1] + color[2]) == 0:
            color[3] = 0.87
            secondary_color[3] = 0.54
        else:
            secondary_color[3] = 0.7
        self.specific_text_color = color
        self.specific_secondary_text_color = secondary_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self, "theme_cls"):
            self.theme_cls.bind(primary_palette=self._update_specific_text_color)
            self.theme_cls.bind(accent_palette=self._update_specific_text_color)
            self.theme_cls.bind(theme_style=self._update_specific_text_color)
        self.bind(background_hue=self._update_specific_text_color)
        self.bind(background_palette=self._update_specific_text_color)
        self._update_specific_text_color(None, None)
