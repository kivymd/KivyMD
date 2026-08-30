from kivy.metrics import dp
from kivy.properties import ColorProperty, StringProperty

from kivymd.app import MDApp
from kivymd.uix.button import IOSButton, IOSButtonText
from kivymd.uix.dialog import (
    IOSDialog,
    IOSDialogButton,
    IOSDialogButtonContainer,
    IOSDialogButtonText,
    IOSDialogMessage,
    IOSDialogTitle,
)
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen


class CommonIOSDialogButton(IOSDialogButton):
    text = StringProperty()
    color = ColorProperty("white")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widgets = [
            IOSDialogButtonText(
                text=self.text,
                theme_text_color="Custom",
                text_color=self.color,
            )
        ]


class Example(MDApp):
    dialog = IOSDialog

    def build(self):
        image = FitImage(source="https://picsum.photos/800/600?random=2")

        return MDScreen(
            image,
            IOSButton(
                IOSButtonText(
                    text="Open iOS Dialog",
                ),
                target_background=image,
                adaptive_width=True,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                border_radius=[dp(22)] * 4,
                on_release=lambda x: self.show_dialog(),
            ),
        )

    def dialog_dismiss(self, *args):
        self.dialog.dismiss()

    def show_dialog(self, *args):
        self.dialog = IOSDialog(
            IOSDialogTitle(
                text="Delete application?",
                bold=True,
            ),
            IOSDialogMessage(
                text=(
                    "This will also result in the deletion of all data "
                    "associated with it."
                )
            ),
            IOSDialogButtonContainer(
                CommonIOSDialogButton(
                    text="Cancel",
                    on_release=lambda x: self.dialog_dismiss(),
                ),
                CommonIOSDialogButton(
                    text="Delete",
                    color="red",
                    on_release=lambda x: self.dialog_dismiss(),
                ),
                orientation="vertical",
            ),
            target_background=self.root,
        )
        self.dialog.open()


if __name__ == "__main__":
    Example().run()
