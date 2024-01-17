from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDButton:
        id: button
        pos_hint: {"center_x": .5, "center_y": .5}

        MDButtonText:
            id: button_text
            text: "Button"
"""


class TestBgColorAfterChangedTheme(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        assert self.root.ids.button.md_bg_color == [
            1.0,
            0.9411764705882353,
            0.9294117647058824,
            1,
        ]
        assert self.root.ids.button_text.text_color == [
            0.7568627450980392,
            0.0,
            0.0,
            1,
        ]
        self.stop()

    def change_palette(self, *args):
        self.theme_cls.primary_palette = "Red"
        Clock.schedule_once(self.check_button_colors, 1.2)

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.change_palette, 1.2)


TestBgColorAfterChangedTheme().run()
