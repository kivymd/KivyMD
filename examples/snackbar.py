from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.widget import Widget

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.snackbar import (
    MDSnackbar,
    MDSnackbarActionButton,
    MDSnackbarActionButtonText,
    MDSnackbarButtonContainer,
    MDSnackbarCloseButton,
    MDSnackbarSupportingText,
    MDSnackbarText,
)

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDBoxLayout:
        id: box
        orientation: "vertical"
        adaptive_size: True
        spacing: "8dp"
        pos_hint: {'center_x': .5, 'center_y': .5}
"""


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self): ...

    def on_start(self):
        data = {
            "Single-line snackbar": self.show_snack_single_line,
            "Single-line snackbar with action": self.show_snack_single_line_with_action,
            "Single-line snackbar with action and close buttons": self.show_snack_single_line_with_action_and_close_button,
            "Two-line snackbar with action and close buttons at the bottom": self.show_snack_two_line_with_action_and_close_button_at_botton,
        }

        for text_button, function in data.items():
            self.root.ids.box.add_widget(
                MDButton(
                    MDButtonText(
                        text=text_button,
                    ),
                    on_release=lambda x, f=function: f(),
                )
            )

    def show_snack_single_line(self):
        MDSnackbar(
            MDSnackbarText(
                text="Single-line snackbar",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_snack_single_line_with_action(self):
        MDSnackbar(
            MDSnackbarSupportingText(
                text="Single-line snackbar with action",
            ),
            MDSnackbarButtonContainer(
                MDSnackbarActionButton(
                    MDSnackbarActionButtonText(text="Action button"),
                ),
                pos_hint={"center_y": 0.5},
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_snack_single_line_with_action_and_close_button(self):
        MDSnackbar(
            MDSnackbarSupportingText(
                text="Single-line snackbar with action and close buttons",
            ),
            MDSnackbarButtonContainer(
                MDSnackbarActionButton(
                    MDSnackbarActionButtonText(
                        text="Action button",
                    ),
                ),
                MDSnackbarCloseButton(
                    icon="close",
                ),
                pos_hint={"center_y": 0.5},
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        ).open()

    def show_snack_two_line_with_action_and_close_button(self):
        MDSnackbar(
            MDSnackbarText(
                text="Single-line snackbar",
            ),
            MDSnackbarSupportingText(
                text="with action and close buttons",
            ),
            MDSnackbarButtonContainer(
                MDSnackbarActionButton(
                    MDSnackbarActionButtonText(text="Action button"),
                ),
                MDSnackbarCloseButton(
                    icon="close",
                ),
                pos_hint={"center_y": 0.5},
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def show_snack_two_line_with_action_and_close_button_at_botton(self):
        MDSnackbar(
            MDSnackbarText(
                text="Single-line snackbar with action",
            ),
            MDSnackbarSupportingText(
                text="and close buttons at the bottom",
                padding=[0, 0, 0, dp(56)],
            ),
            MDSnackbarButtonContainer(
                Widget(),
                MDSnackbarActionButton(
                    MDSnackbarActionButtonText(text="Action button"),
                ),
                MDSnackbarCloseButton(
                    icon="close",
                ),
            ),
            y=dp(124),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            padding=[0, 0, "8dp", "8dp"],
        ).open()


Example().run()
