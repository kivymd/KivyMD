from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()

        MDButtonText:
            text: "Show dialog"
"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="refresh",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Reset settings?",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="This will reset your app preferences back to their "
                "default settings. The following accounts will also "
                "be signed out:",
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="gmail",
                    ),
                    MDListItemSupportingText(
                        text="KivyMD-library@yandex.com",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="gmail",
                    ),
                    MDListItemSupportingText(
                        text="kivydevelopment@gmail.com",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                ),
                MDButton(
                    MDButtonText(text="Accept"),
                    style="text",
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        ).open()


Example().run()
