from kivy.clock import Clock
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.color_definitions import colors

KV = """
MDScreen:

    MDRaisedButton:
        id: button
        text: "Button"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestBgColorAfterChangedTheme(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        for instruction in self.root.ids.button.canvas.children:
            if isinstance(instruction, Color):
                if instruction.group == "bg-color":
                    assert instruction.rgba == get_color_from_hex(
                        colors[self.theme_cls.primary_palette]["500"]
                    )

        self.stop()

    def change_palette(self, *args):
        self.theme_cls.primary_palette = "Red"
        Clock.schedule_once(self.check_button_colors, 1.2)

    def on_start(self):
        Clock.schedule_once(self.change_palette, 1.2)


TestBgColorAfterChangedTheme().run()
