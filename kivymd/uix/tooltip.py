"""
Tooltip
=======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Menus <https://material.io/components/tooltips/>`_

Example
-------

from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.app import MDApp

Builder.load_string('''
#:import hex_colormap kivy.utils.hex_colormap
#:import get_color_from_hex kivy.utils.get_color_from_hex


<IconButtonTooltips@MDIconButton+MDTooltip>

<RoundImageButtonTooltips@MDRoundImageButton+MDTooltip>

<ToolbarTooltips@MDToolbar+MDTooltip>


<ExampleTooltips@BoxLayout>
    orientation: "vertical"

    ToolbarTooltips:
        title: "Example Tooltips"
        md_bg_color: get_color_from_hex(hex_colormap["crimson"])
        elevation: 10
        left_action_items: [["dots-vertical", lambda x: None]]
        tooltip_text: "MDToolbar"

    Screen:

        BoxLayout:
            size_hint: None, None
            size: self.minimum_size
            padding: "10dp"
            pos_hint: {"center_x": .5, "center_y": .9}

            IconButtonTooltips:
                icon: "cart"
                tooltip_text_color: 1, 0, 0, 1
                tooltip_text: "MDIconButton"

            RoundImageButtonTooltips:
                source: "data/logo/kivy-icon-512.png"
                tooltip_bg_color: 1, 0, 0, 1
                tooltip_text: "MDRoundImageButton"
                pos_hint: {"center_x": .5, "center_y": .5}
''')


class Test(MDApp):
    def build(self):
        return Factory.ExampleTooltips()


Test().run()
"""

__all__ = (
    "MDTooltip",
    "MDTooltipViewClass",
)

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE


<MDTooltipViewClass>
    size_hint: None, None
    width: self.minimum_width
    height:
        dp(24) + root.padding[1] * 2 if DEVICE_TYPE == "desktop" \
        else dp(32) + root.padding[1] * 2

    padding:
        dp(8) if DEVICE_TYPE == "desktop" else dp(16), \
        dp(4), \
        dp(8) if DEVICE_TYPE == "desktop" else dp(16), \
        dp(4)

    canvas:
        Color:
            rgba:
                root.theme_cls.opposite_bg_dark if not root.tooltip_bg_color \
                else root.tooltip_bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10]

    Label:
        id: label_tooltip
        text: root.tooltip_text
        size_hint: None, None
        size: self.texture_size
        bold: True
        color:
            ([0, 0, 0, 1] if not root.tooltip_text_color else root.tooltip_text_color) \
            if root.theme_cls.theme_style == "Dark" else \
            ([1, 1, 1, 1] if not root.tooltip_text_color else root.tooltip_text_color)
        pos_hint: {"center_y": .5}
"""
)


class MDTooltipViewClass(ThemableBehavior, BoxLayout):
    tooltip_bg_color = ListProperty()
    tooltip_text_color = ListProperty()
    tooltip_text = StringProperty()


class MDTooltip(ThemableBehavior, HoverBehavior, BoxLayout):
    tooltip_bg_color = ListProperty()
    """Tooltip background color."""

    tooltip_text_color = ListProperty()
    """Tooltip text color."""

    tooltip_text = StringProperty()
    """Tooltip text."""

    _tooltip = None
    _pos = []

    def on_enter(self):
        if not self.tooltip_text:
            return
        self._tooltip = MDTooltipViewClass(
                tooltip_bg_color=self.tooltip_bg_color,
                tooltip_text_color=self.tooltip_text_color,
                tooltip_text=self.tooltip_text,
            )
        Clock.schedule_once(self.display_tooltip, -1)

    def display_tooltip(self, interval):
        # TODO: Add tooltip animation.
        Window.add_widget(self._tooltip)
        pos = self.to_window(self.center_x, self.center_y)
        self._tooltip.pos = (
            pos[0] - self._tooltip.width / 2,
            pos[1] - self._tooltip.height / 2 - self.height / 2 - dp(20),
        )

    def on_leave(self):
        Window.remove_widget(self._tooltip)
