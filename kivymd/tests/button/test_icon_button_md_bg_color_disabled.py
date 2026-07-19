"""
Test that MDIconButton correctly applies the disabled background color.

The test creates a disabled MDIconButton with a custom
``md_bg_color_disabled`` value, adds it to the screen, and verifies that
the background color of the button's canvas matches the specified color.

The application is stopped automatically after the verification is complete.
"""

from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen


class TestMdIconButtonMdBgColorDisabled(MDApp):
    def build(self):
        return MDScreen()

    def generate_buttons(self):
        button = MDIconButton(
            disabled=True,
            md_bg_color_disabled="red",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.root.clear_widgets()
        self.root.add_widget(button)

        Clock.schedule_once(
            lambda y, x=button: self.check_button_md_bg_color_disabled(x), 1
        )
        Clock.schedule_once(lambda x: self.stop(), 2)

    def check_button_md_bg_color_disabled(self, button):
        assert button.canvas.before.get_group("md-icon-button-bg-color")[
            0
        ].rgba == [1.0, 0.0, 0.0, 1.0]

    def on_start(self):
        self.generate_buttons()


if __name__ == "__main__":
    TestMdIconButtonMdBgColorDisabled().run()
