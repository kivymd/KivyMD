# Drag the image to the test application window.

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.window.window_sdl2 import WindowSDL
from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = """
<ColorCard>
    orientation: "vertical"

    MDLabel:
        text: root.text
        color: "grey"
        adaptive_height: True

    MDCard:
        theme_bg_color: "Custom"
        md_bg_color: root.bg_color


MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDRecycleView:
        id: card_list
        viewclass: "ColorCard"
        bar_width: 0

        RecycleGridLayout:
            cols: 3
            spacing: "16dp"
            padding: "16dp"
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
"""


class ColorCard(MDBoxLayout):
    text = StringProperty()
    bg_color = ColorProperty()


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self.on_drop_file)

    def on_drop_file(self, sdl: WindowSDL, path_to_file: str) -> None:
        ext = os.path.splitext(path_to_file)[1]
        if isinstance(path_to_file, bytes):
            path_to_file = path_to_file.decode()
        if isinstance(ext, bytes):
            ext = ext.decode()
        if ext in [".png", ".jpg"]:
            self.theme_cls.path_to_wallpaper = path_to_file
            Clock.schedule_once(self.generate_cards, 0.5)

    def build(self):
        self.theme_cls.dynamic_color = True
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def theme_switch(self) -> None:
        self.theme_cls.switch_theme()
        Clock.schedule_once(self.generate_cards, 0.5)

    def generate_cards(self, *args):
        self.root.ids.card_list.data = []
        for name_color in self.theme_cls.current_schemes_color_data:
            self.root.ids.card_list.data.append(
                {
                    "bg_color": getattr(self.theme_cls, name_color),
                    "text": name_color,
                }
            )

    def on_start(self):
        Clock.schedule_once(self.generate_cards)


Example().run()
