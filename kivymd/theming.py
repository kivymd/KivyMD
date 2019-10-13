"""
Theming
=======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Material theming <https://material.io/design/material-theming>`_
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import (
    OptionProperty,
    AliasProperty,
    ObjectProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    DictProperty,
)
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.atlas import Atlas

from kivymd.color_definitions import colors, palette, hue
from kivymd.font_definitions import theme_font_styles  # Fonts will be loaded
from kivymd.material_resources import DEVICE_TYPE, DEVICE_IOS
from kivymd import images_path


class ThemeManager(Widget):
    primary_palette = OptionProperty("Blue", options=palette)
    primary_hue = OptionProperty("500", options=hue)
    primary_light_hue = OptionProperty("200", options=hue)
    primary_dark_hue = OptionProperty("700", options=hue)

    def _get_primary_color(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_hue]
        )

    primary_color = AliasProperty(
        _get_primary_color, bind=("primary_palette", "primary_hue")
    )

    def _get_primary_light(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_light_hue]
        )

    primary_light = AliasProperty(
        _get_primary_light, bind=("primary_palette", "primary_light_hue")
    )

    def _get_primary_dark(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_dark_hue]
        )

    primary_dark = AliasProperty(
        _get_primary_dark, bind=("primary_palette", "primary_dark_hue")
    )

    accent_palette = OptionProperty("Amber", options=palette)
    accent_hue = OptionProperty("500", options=hue)
    accent_light_hue = OptionProperty("200", options=hue)
    accent_dark_hue = OptionProperty("700", options=hue)

    def _get_accent_color(self):
        return get_color_from_hex(colors[self.accent_palette][self.accent_hue])

    accent_color = AliasProperty(
        _get_accent_color, bind=["accent_palette", "accent_hue"]
    )

    def _get_accent_light(self):
        return get_color_from_hex(
            colors[self.accent_palette][self.accent_light_hue]
        )

    accent_light = AliasProperty(
        _get_accent_light, bind=["accent_palette", "accent_light_hue"]
    )

    def _get_accent_dark(self):
        return get_color_from_hex(
            colors[self.accent_palette][self.accent_dark_hue]
        )

    accent_dark = AliasProperty(
        _get_accent_dark, bind=["accent_palette", "accent_dark_hue"]
    )

    theme_style = OptionProperty("Light", options=["Light", "Dark"])

    def _get_theme_style(self, opposite):
        if opposite:
            return "Light" if self.theme_style == "Dark" else "Dark"
        else:
            return self.theme_style

    def _get_bg_darkest(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["StatusBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["StatusBar"])

    bg_darkest = AliasProperty(_get_bg_darkest, bind=["theme_style"])

    def _get_op_bg_darkest(self):
        return self._get_bg_darkest(True)

    opposite_bg_darkest = AliasProperty(
        _get_op_bg_darkest, bind=["theme_style"]
    )

    def _get_bg_dark(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["AppBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["AppBar"])

    bg_dark = AliasProperty(_get_bg_dark, bind=["theme_style"])

    def _get_op_bg_dark(self):
        return self._get_bg_dark(True)

    opposite_bg_dark = AliasProperty(_get_op_bg_dark, bind=["theme_style"])

    def _get_bg_normal(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["Background"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["Background"])

    bg_normal = AliasProperty(_get_bg_normal, bind=["theme_style"])

    def _get_op_bg_normal(self):
        return self._get_bg_normal(True)

    opposite_bg_normal = AliasProperty(_get_op_bg_normal, bind=["theme_style"])

    def _get_bg_light(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["CardsDialogs"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["CardsDialogs"])

    bg_light = AliasProperty(_get_bg_light, bind=["theme_style"])

    def _get_op_bg_light(self):
        return self._get_bg_light(True)

    opposite_bg_light = AliasProperty(_get_op_bg_light, bind=["theme_style"])

    def _get_divider_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        color[3] = 0.12
        return color

    divider_color = AliasProperty(_get_divider_color, bind=["theme_style"])

    def _get_op_divider_color(self):
        return self._get_divider_color(True)

    opposite_divider_color = AliasProperty(
        _get_op_divider_color, bind=["theme_style"]
    )

    def _get_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.87
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    text_color = AliasProperty(_get_text_color, bind=["theme_style"])

    def _get_op_text_color(self):
        return self._get_text_color(True)

    opposite_text_color = AliasProperty(
        _get_op_text_color, bind=["theme_style"]
    )

    def _get_secondary_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.70
        return color

    secondary_text_color = AliasProperty(
        _get_secondary_text_color, bind=["theme_style"]
    )

    def _get_op_secondary_text_color(self):
        return self._get_secondary_text_color(True)

    opposite_secondary_text_color = AliasProperty(
        _get_op_secondary_text_color, bind=["theme_style"]
    )

    def _get_icon_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    icon_color = AliasProperty(_get_icon_color, bind=["theme_style"])

    def _get_op_icon_color(self):
        return self._get_icon_color(True)

    opposite_icon_color = AliasProperty(
        _get_op_icon_color, bind=["theme_style"]
    )

    def _get_disabled_hint_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.38
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.50
        return color

    disabled_hint_text_color = AliasProperty(
        _get_disabled_hint_text_color, bind=["theme_style"]
    )

    def _get_op_disabled_hint_text_color(self):
        return self._get_disabled_hint_text_color(True)

    opposite_disabled_hint_text_color = AliasProperty(
        _get_op_disabled_hint_text_color, bind=["theme_style"]
    )

    # Hardcoded because muh standard
    def _get_error_color(self):
        return get_color_from_hex(colors["Red"]["A700"])

    error_color = AliasProperty(_get_error_color)

    def _get_ripple_color(self):
        return self._ripple_color

    def _set_ripple_color(self, value):
        self._ripple_color = value

    _ripple_color = ListProperty(get_color_from_hex(colors["Gray"]["400"]))
    ripple_color = AliasProperty(
        _get_ripple_color, _set_ripple_color, bind=["_ripple_color"]
    )

    def _determine_device_orientation(self, _, window_size):
        if window_size[0] > window_size[1]:
            self.device_orientation = "landscape"
        elif window_size[1] >= window_size[0]:
            self.device_orientation = "portrait"

    device_orientation = StringProperty("")

    def _get_standard_increment(self):
        if DEVICE_TYPE == "mobile":
            if self.device_orientation == "landscape":
                return dp(48)
            else:
                return dp(56)
        else:
            return dp(64)

    standard_increment = AliasProperty(
        _get_standard_increment, bind=["device_orientation"]
    )

    def _get_horizontal_margins(self):
        if DEVICE_TYPE == "mobile":
            return dp(16)
        else:
            return dp(24)

    horizontal_margins = AliasProperty(_get_horizontal_margins)

    def on_theme_style(self, instance, value):
        if (
            hasattr(App.get_running_app(), "theme_cls")
            and App.get_running_app().theme_cls == self
        ):
            self.set_clearcolor_by_theme_style(value)

    def set_clearcolor_by_theme_style(self, theme_style):
        if theme_style == "Light":
            Window.clearcolor = get_color_from_hex(
                colors["Light"]["Background"]
            )
        elif theme_style == "Dark":
            Window.clearcolor = get_color_from_hex(colors["Dark"]["Background"])

    # font name, size (sp), always caps, letter spacing (sp)
    font_styles = DictProperty(
        {
            "H1": ["RobotoLight", 96, False, -1.5],
            "H2": ["RobotoLight", 60, False, -0.5],
            "H3": ["Roboto", 48, False, 0],
            "H4": ["Roboto", 34, False, 0.25],
            "H5": ["Roboto", 24, False, 0],
            "H6": ["RobotoMedium", 20, False, 0.15],
            "Subtitle1": ["Roboto", 16, False, 0.15],
            "Subtitle2": ["RobotoMedium", 14, False, 0.1],
            "Body1": ["Roboto", 16, False, 0.5],
            "Body2": ["Roboto", 14, False, 0.25],
            "Button": ["RobotoMedium", 14, True, 1.25],
            "Caption": ["Roboto", 12, False, 0.4],
            "Overline": ["Roboto", 10, True, 1.5],
            "Icon": ["Icons", 24, False, 0],
        }
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rec_shadow = Atlas(f"{images_path}rec_shadow.atlas")
        self.rec_st_shadow = Atlas(f"{images_path}rec_st_shadow.atlas")
        self.quad_shadow = Atlas(f"{images_path}quad_shadow.atlas")
        self.round_shadow = Atlas(f"{images_path}round_shadow.atlas")
        Clock.schedule_once(lambda x: self.on_theme_style(0, self.theme_style))
        self._determine_device_orientation(None, Window.size)
        Window.bind(size=self._determine_device_orientation)


class ThemableBehavior(object):
    theme_cls = ObjectProperty(None)
    opposite_colors = BooleanProperty(False)
    device_ios = DEVICE_IOS

    def __init__(self, **kwargs):
        if self.theme_cls is not None:
            pass
        elif hasattr(App.get_running_app(), "theme_cls"):
            self.theme_cls = App.get_running_app().theme_cls
        else:
            self.theme_cls = ThemeManager()
        super().__init__(**kwargs)
