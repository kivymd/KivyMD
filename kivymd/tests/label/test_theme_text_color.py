"""
Test that MDLabel applies a custom text color when using the custom
theme text color option.

The test creates an MDLabel with a custom text color and verifies that
the label text color property matches the specified RGBA value.
"""

from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        text: "MDLabel"
        halign: "center"
        theme_text_color: "Custom"
        text_color: "red"
"""


class TestThemeTextColor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        def on_start(*args):
            assert self.root.ids.label.text_color == [1.0, 0.0, 0.0, 1.0]
            self.stop()

        Clock.schedule_once(on_start, 2)


if __name__ == "__main__":
    TestThemeTextColor().run()
