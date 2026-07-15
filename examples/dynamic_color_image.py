# Drag the image to the test application window.

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = """
<ColorCard>:
    orientation: "vertical"
    size_hint_y: None
    height: dp(80)
    radius:[dp(20), dp(20), dp(20), dp(20)]

    MDLabel:
        text: root.text
        color: (1 - root.md_bg_color[0], 1 - root.md_bg_color[1], 1 - root.md_bg_color[2], 1)
        adaptive_height: True
        padding:[dp(10), 0]


MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    MDScrollView:
        do_scroll_x:False
        MDGridLayout:
            id: card_list
            cols: 3
            spacing: "16dp"
            padding: "16dp"
            size_hint_y: None
            height: self.minimum_height
"""


class ColorCard(MDBoxLayout):
    text = StringProperty()


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self.on_drop_file)

    def on_drop_file(self, sdl: Window, path_to_file: str) -> None:
        ext = os.path.splitext(path_to_file)[1]

        if isinstance(path_to_file, bytes):
            path_to_file = path_to_file.decode()
        if isinstance(ext, bytes):
            ext = ext.decode()
        if ext in [".png", ".jpg"]:
            self.theme_cls.path_to_wallpaper = path_to_file

    def build(self):
        self.theme_cls.dynamic_color = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.on_colors = lambda: Clock.schedule_once(self.refresh)
        return Builder.load_string(KV)

    def theme_switch(self) -> None:
        self.theme_cls.switch_theme()

    def generate_cards(self, *args):
        grid = self.root.ids.card_list
        if grid.children:
            return
        for name_color in self.theme_cls.current_schemes_color_data:
            grid.add_widget(
                ColorCard(
                    md_bg_color=getattr(self.theme_cls, name_color),
                    text=name_color,
                )
            )

    def refresh(self, *args):
        grid = self.root.ids.card_list
        for card, name_color in zip(
            grid.children[::-1], self.theme_cls.current_schemes_color_data
        ):
            card.md_bg_color = getattr(self.theme_cls, name_color)

    def on_start(self):
        Clock.schedule_once(self.generate_cards)


Example().run()
