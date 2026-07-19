"""
Test that MDButton applies a custom line color when using the custom
line color theme option.

The test creates an MDButton with a custom line color and verifies
that the line color property is set to the expected RGBA value.
"""

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


class TestOutlineButtonCustomColors(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_button_colors(self, *args):
        assert self.root.ids.button.line_color == [1.0, 0.0, 0.0, 1.0]
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_button_colors, 1.2)


if __name__ == "__main__":
    TestOutlineButtonCustomColors().run()
