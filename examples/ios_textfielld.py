from kivy.metrics import dp

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import (
    IOSTextField,
    IOSTextFieldLeadingIcon,
    IOSTextFieldTrailingIcon,
)


class TestApp(MDApp, CommonApp):
    def build(self):
        bg_image = FitImage(source="https://picsum.photos/800/600?random=6")

        return MDScreen(
            bg_image,
            IOSTextField(
                IOSTextFieldLeadingIcon(
                    icon="gmail",
                    on_release=lambda x: print("Tap gmail"),
                ),
                IOSTextFieldTrailingIcon(
                    icon="account",
                    on_release=lambda x: print("Tap account"),
                ),
                target_background=bg_image,
                hint_text="Message",
                size_hint_x=0.6,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            MDIconButton(
                icon="menu",
                pos_hint={"top": 0.98},
                x=dp(12),
                on_release=lambda x: self.open_menu(x),
            ),
        )


if __name__ == "__main__":
    TestApp().run()
