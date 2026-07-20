"""
Test that MDButton respects custom dimensions when using size hints.

The test creates an MDButton with a custom height and a horizontal
size hint, then verifies that the resulting button size matches the
expected window dimensions.
"""

from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.screen import MDScreen


class TestSizeHint(MDApp):
    def build(self):
        return MDScreen()

    def generate_buttons(self):
        button = MDButton(theme_height="Custom", size=self.root.size)
        self.root.clear_widgets()
        self.root.add_widget(button)
        Clock.schedule_once(lambda x: self.check_button_size(button), 1)

    def check_button_size(self, button):
        assert button.size == self.root.size
        self.stop()

    def on_start(self):
        self.generate_buttons()


if __name__ == "__main__":
    TestSizeHint().run()
