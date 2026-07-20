"""
Test that MDFabButton correctly applies Material 3 size specifications
for different button styles.

The test creates three MDFabButton instances with "standard", "small",
and "large" styles, adds them to the layout, and verifies that each
button has the expected size according to its style.

The application is stopped automatically after successful verification.
"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton

KV = """
MDScreen:

    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestFabSizeM3Style(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_size_button(self, *args):
        data = {
            "large": [dp(96.0), dp(96.0)],
            "small": [dp(40.0), dp(40.0)],
            "standard": [dp(56.0), dp(56.0)],
        }
        for button in self.root.ids.box.children:
            assert button.size == data[button.style]

        self.stop()

    def on_start(self):
        styles = ["standard", "small", "large"]
        for style in styles:
            self.root.ids.box.add_widget(
                MDFabButton(icon="pencil", style=style)
            )

        Clock.schedule_once(self.check_size_button, 1.2)


if __name__ == "__main__":
    TestFabSizeM3Style().run()
