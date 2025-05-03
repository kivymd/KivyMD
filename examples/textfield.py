from kivy.lang import Builder

from examples.common_app import KV, CommonApp
from kivymd.app import MDApp
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldHelperText,
    MDTextFieldHintText,
    MDTextFieldLeadingIcon,
    MDTextFieldMaxLengthText,
    MDTextFieldTrailingIcon,
)


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for mode in ["outlined", "filled", "required"]:
            self.root.ids.widget_box.add_widget(
                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="account",
                    ),
                    MDTextFieldHintText(
                        text="Hint text",
                    ),
                    MDTextFieldHelperText(
                        text="Helper text",
                        mode="persistent",
                    ),
                    MDTextFieldTrailingIcon(
                        icon="information",
                    ),
                    MDTextFieldMaxLengthText(
                        max_text_length=10,
                    ),
                    mode="filled" if mode == "required" else mode,
                    text=mode.capitalize() if mode != "required" else "",
                    required=mode == "required",
                )
            )
        for mode in ["outlined", "filled", "required"]:
            self.root.ids.custom_widget_box.add_widget(
                MDTextField(
                    MDTextFieldLeadingIcon(
                        icon="account",
                        theme_icon_color="Custom",
                        icon_color_normal="mediumaquamarine",
                        icon_color_focus="tan",
                    ),
                    MDTextFieldHintText(
                        text="Hint text",
                        text_color_normal="mediumaquamarine",
                        text_color_focus="tan",
                    ),
                    MDTextFieldHelperText(
                        text="Helper text",
                        mode="persistent",
                        text_color_normal="mediumaquamarine",
                        text_color_focus="tan",
                    ),
                    MDTextFieldTrailingIcon(
                        icon="information",
                        theme_icon_color="Custom",
                        icon_color_normal="mediumaquamarine",
                        icon_color_focus="tan",
                    ),
                    MDTextFieldMaxLengthText(
                        max_text_length=10,
                        text_color_normal="mediumaquamarine",
                        text_color_focus="tan",
                    ),
                    mode="filled" if mode == "required" else mode,
                    text=mode.capitalize() if mode != "required" else "DDDD",
                    required=mode == "required",
                    theme_bg_color="Custom",
                    fill_color_normal="lightcyan",
                    fill_color_focus="lightsteelblue",
                    theme_line_color="Custom",
                    line_color_normal="mediumaquamarine",
                    line_color_focus="tan",
                )
            )


Example().run()
