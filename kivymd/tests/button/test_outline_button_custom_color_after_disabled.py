from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDButton:
        id: button
        theme_line_color: "Custom"
        line_color: "red"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDButtonText:
            text: "Button"
"""


class TestOutlineButtonCustomColorsAfterDisabled(MDApp):
    state_button = "unchecked"

    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        def check_button_colors_control(dt):
            button.disabled = False
            self.state_button = "checked"
            Clock.schedule_once(self.check_button_colors, 1.2)

        button = self.root.ids.button
        assert button.line_color == [1.0, 0.0, 0.0, 1.0]

        if self.state_button == "checked":
            self.stop()
        elif self.state_button == "unchecked":
            button.disabled = True
            Clock.schedule_once(check_button_colors_control, 1.2)

    def on_start(self):
        Clock.schedule_once(self.check_button_colors, 1.2)


TestOutlineButtonCustomColorsAfterDisabled().run()
