"""
Test that MDLabel applies the correct font size when configured
programmatically in Python code.

The test creates an MDLabel with a custom font style and role assigned
during widget initialization and verifies that the resulting font size
matches the expected value.
"""

# Test for https://github.com/kivymd/KivyMD/issues/1435:

from kivy.clock import Clock
from kivy.metrics import sp

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class TestFontSizeInPythonCode(MDApp):
    def check_font_size(self, *args):
        assert self.root.get_ids().label.font_size == sp(57)
        self.stop()

    def build(self):
        return MDBoxLayout(
            MDLabel(
                id="label",
                text="MDLabel",
                font_style="Display",
                role="large",
            ),
        )

    def on_start(self):
        Clock.schedule_once(self.check_font_size, 1.2)


if __name__ == "__main__":
    TestFontSizeInPythonCode().run()
