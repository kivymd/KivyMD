"""
Test that the MDButton background color and text color are updated correctly
after changing the application theme palette.

The test starts the application with the default theme, changes the primary
palette to "Red", waits for the theme update animation and verifies that the
button colors match the expected values.

The application is stopped automatically after successful verification.
"""

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
            0.9333333333333333,
            1,
        ]
        assert self.root.ids.button_text.text_color == [
            0.5647058823529412,
            0.29411764705882354,
            0.25098039215686274,
            1.0,
        ]
        self.stop()

    def change_palette(self, *args):
        self.theme_cls.primary_palette = "Red"
        Clock.schedule_once(self.check_button_colors, 1.2)

    def on_start(self):
        Clock.schedule_once(self.change_palette, 1.2)


if __name__ == "__main__":
    TestBgColorAfterChangedTheme().run()
