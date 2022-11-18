from kivy.clock import Clock
from kivy.graphics import Color
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDRectangleFlatIconButton:
        id: button
        icon: "android"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        text_color: "yellow"
        line_color: "red"
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestMDRectangleFlatIconButtonCustomColors(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        button = self.root.ids.button

        assert button.ids.lbl_ic.color == [1.0, 0.6470588235294118, 0.0, 1.0]
        assert button.ids.lbl_txt.color == [1.0, 1.0, 0.0, 1.0]

        for instruction in button.canvas.children:
            if isinstance(instruction, Color):
                if instruction.group == "outline-color":
                    assert instruction.rgba == [1.0, 0.0, 0.0, 1.0]
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_button_colors, 1.2)


TestMDRectangleFlatIconButtonCustomColors().run()
