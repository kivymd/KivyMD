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


class TestMDRectangleFlatIconButtonCustomColorsAfterDisabled(MDApp):
    state_button = "unchecked"

    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        def check_button_colors_control(*args):
            button.disabled = False
            self.state_button = "checked"
            Clock.schedule_once(self.check_button_colors, 1.2)

        button = self.root.ids.button

        assert button.ids.lbl_ic.color == [1.0, 0.6470588235294118, 0.0, 1.0]
        assert button.ids.lbl_txt.color == [1.0, 1.0, 0.0, 1.0]

        for instruction in button.canvas.children:
            if isinstance(instruction, Color):
                if instruction.group == "outline-color":
                    assert instruction.rgba == [1.0, 0.0, 0.0, 1.0]

        if self.state_button == "checked":
            self.stop()
        elif self.state_button == "unchecked":
            button.disabled = True
            Clock.schedule_once(check_button_colors_control, 1.2)

    def on_start(self):
        Clock.schedule_once(self.check_button_colors, 1.2)


TestMDRectangleFlatIconButtonCustomColorsAfterDisabled().run()
