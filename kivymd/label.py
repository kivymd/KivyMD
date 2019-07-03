"""
Label
=====

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
from kivy.metrics import sp
from kivy.properties import (
    OptionProperty,
    ListProperty,
    BooleanProperty,
    StringProperty,
    AliasProperty,
)
from kivy.uix.label import Label

from kivymd.font_definitions import theme_font_styles
from kivymd.material_resources import DEVICE_TYPE
from kivymd.theming import ThemableBehavior
from kivymd.theming_dynamic_text import get_contrast_text_color

Builder.load_string(
    """
#:import md_icons kivymd.icon_definitions.md_icons


<MDLabel>
    disabled_color: self.theme_cls.disabled_hint_text_color
    text_size: (self.width, None)


<MDIcon>
    font_style: 'Icon'
    text: u'{}'.format(md_icons[self.icon])
"""
)


class MDLabel(ThemableBehavior, Label):
    font_style = OptionProperty("Body1", options=theme_font_styles)

    can_capitalize = BooleanProperty(True)
    _capitalizing = BooleanProperty(False)

    def _get_text(self):
        if self._capitalizing:
            return self._text.upper()
        return self._text

    def _set_text(self, value):
        self._text = value

    _text = StringProperty()
    text = AliasProperty(_get_text, _set_text, bind=["_text", "_capitalizing"])

    theme_text_color = OptionProperty(
        None,
        allownone=True,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
        ],
    )

    text_color = ListProperty(None, allownone=True)

    parent_background = ListProperty(None, allownone=True)

    _currently_bound_property = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            font_style=self.update_font_style, can_capitalize=self.update_font_style
        )
        self.on_theme_text_color(None, self.theme_text_color)
        self.update_font_style()
        self.on_opposite_colors(None, self.opposite_colors)

    def update_font_style(self, *args):
        font_info = self.theme_cls.font_styles[self.font_style]
        self.font_name = font_info[0]
        self.font_size = sp(font_info[1])
        if font_info[2] and self.can_capitalize:
            self._capitalizing = True
        else:
            self._capitalizing = False
        # TODO: Add letter spacing change
        # self.letter_spacing = font_info[3]

    def on_theme_text_color(self, instance, value):
        t = self.theme_cls
        op = self.opposite_colors
        setter = self.setter("color")
        t.unbind(**self._currently_bound_property)
        attr_name = {
            "Primary": "text_color" if not op else "opposite_text_color",
            "Secondary": "secondary_text_color"
            if not op
            else "opposite_secondary_text_color",
            "Hint": "disabled_hint_text_color"
            if not op
            else "opposite_disabled_hint_text_color",
            "Error": "error_color",
        }.get(value, None)
        if attr_name:
            c = {attr_name: setter}
            t.bind(**c)
            self._currently_bound_property = c
            self.color = getattr(t, attr_name)
        else:
            # 'Custom' and 'ContrastParentBackground' lead here, as well as the
            # generic None value it's not yet been set
            if value == "Custom" and self.text_color:
                self.color = self.text_color
            elif value == "ContrastParentBackground" and self.parent_background:
                self.color = get_contrast_text_color(self.parent_background)
            else:
                self.color = [0, 0, 0, 1]

    def on_text_color(self, *args):
        if self.theme_text_color == "Custom":
            self.color = self.text_color

    def on_opposite_colors(self, instance, value):
        self.on_theme_text_color(self, self.theme_text_color)


class MDIcon(MDLabel):
    icon = StringProperty("android")
