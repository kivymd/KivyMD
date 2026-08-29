from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import IOSButton, IOSButtonText, IOSIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        bg_image = FitImage(source="https://picsum.photos/800/600?random=2")

        return MDScreen(
            bg_image,
            MDBoxLayout(
                IOSButton(
                    IOSIconButton(
                        icon="account",
                    ),
                    size=(dp(56), dp(56)),
                    adaptive_size=False,
                    border_radius=[dp(28)] * 4,
                    target_background=bg_image,
                    pos_hint={"center_x": 0.5},
                ),
                IOSButton(
                    IOSIconButton(
                        icon="account",
                    ),
                    IOSButtonText(
                        text="iOS Button",
                    ),
                    target_background=bg_image,
                    pos_hint={"center_x": 0.5},
                    border_radius=[dp(20)] * 4,
                ),
                IOSButton(
                    IOSIconButton(
                        icon="account",
                    ),
                    IOSButtonText(
                        text="iOS Button",
                    ),
                    orientation="vertical",
                    target_background=bg_image,
                    pos_hint={"center_x": 0.5},
                    border_radius=[dp(20)] * 4,
                ),
                IOSButton(
                    IOSButtonText(
                        text="IOS Button",
                    ),
                    target_background=bg_image,
                    pos_hint={"center_x": 0.5},
                    border_radius=[dp(22)] * 4,
                ),
                orientation="vertical",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                adaptive_size=True,
                spacing=dp(12),
            ),
        )


Example().run()
