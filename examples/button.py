from kivy.clock import Clock
from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.button import (
    MDButton,
    MDButtonIcon,
    MDButtonText,
    MDExtendedFabButton,
    MDExtendedFabButtonIcon,
    MDExtendedFabButtonText,
    MDFabButton,
    MDIconButton,
)

KV = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    ScrollView:
        size_hint_y: None
        height: root.height - dp(68)

        MDBoxLayout:
            orientation: "vertical"
            padding: "24dp", 0, "24dp", 0
            adaptive_height: True

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"

                MDLabel:
                    text: "MDIconButton"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: icon_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"
                md_bg_color: app.theme_cls.secondaryContainerColor
                radius: "12dp"

                MDLabel:
                    text: "MDIconButton (custom color)"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: custom_icon_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"

                MDLabel:
                    text: "MDFabButton"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: fab_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"
                md_bg_color: app.theme_cls.secondaryContainerColor
                radius: "12dp"

                MDLabel:
                    text: "MDFabButton (custom color)"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: custom_fab_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"

                MDLabel:
                    text: "MDButton"
                    adaptive_height: True
                    bold: True

                MDBoxLayout:
                    id: md_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp", 0, "24dp", "24dp"

                MDLabel:
                    text: "MDButton (with icon)"
                    adaptive_height: True
                    bold: True

                MDBoxLayout:
                    id: md_button_icon_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"
                md_bg_color: app.theme_cls.secondaryContainerColor
                radius: "12dp"

                MDLabel:
                    text: "MDButton (custom color)"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: custom_md_button_box
                    adaptive_height: True
                    spacing: "12dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "24dp"
                padding: "24dp"
                radius: "12dp"

                MDLabel:
                    text: "MDExtendedFabButton"
                    bold: True
                    adaptive_height: True

                MDBoxLayout:
                    id: extended_fab_button_box
                    adaptive_height: True
                    spacing: "12dp"

                    Widget:
"""


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self):
        for button in (
            self.root.ids.fab_button_box.children
            + self.root.ids.custom_fab_button_box.children
            + self.root.ids.custom_icon_button_box.children
            + self.root.ids.md_button_box.children
            + self.root.ids.icon_button_box.children
            + self.root.ids.md_button_icon_box.children
            + self.root.ids.custom_md_button_box.children
            + self.root.ids.extended_fab_button_box.children
        ):
            button.disabled = not button.disabled

    def on_start(self):
        styles = ["standard", "filled", "outlined", "tonal"]
        color_disabled = [
            0.4627450980392157,
            0.47058823529411764,
            0.07450980392156863,
            0.38,
        ]

        for style in styles:
            self.root.ids.icon_button_box.add_widget(
                MDIconButton(style=style, icon="heart")
            )
            if style in ["filled", "tonal"]:
                self.root.ids.custom_icon_button_box.add_widget(
                    MDIconButton(
                        style=style,
                        icon="heart",
                        theme_bg_color="Custom",
                        theme_icon_color="Custom",
                        md_bg_color={"filled": "brown", "tonal": "green"}[
                            style
                        ],
                        icon_color={"filled": "green", "tonal": "brown"}[style],
                        icon_color_disabled="black",
                        md_bg_color_disabled=color_disabled,
                    )
                )
            elif style == "outlined":
                self.root.ids.custom_icon_button_box.add_widget(
                    MDIconButton(
                        style=style,
                        icon="heart",
                        theme_icon_color="Custom",
                        theme_line_color="Custom",
                        line_color="brown",
                        icon_color="green",
                        icon_color_disabled="black",
                        md_bg_color_disabled=color_disabled,
                    )
                )
            elif style == "standard":
                self.root.ids.custom_icon_button_box.add_widget(
                    MDIconButton(
                        style=style,
                        icon="heart",
                        theme_icon_color="Custom",
                        icon_color="green",
                        icon_color_disabled="black",
                        md_bg_color_disabled=color_disabled,
                    )
                )

        styles = ["filled", "outlined", "tonal", "elevated", "text"]
        for style in styles:
            text = style.capitalize()
            self.root.ids.md_button_box.add_widget(
                MDButton(
                    MDButtonText(
                        text=text,
                    ),
                    style=style,
                )
            )
            self.root.ids.md_button_icon_box.add_widget(
                MDButton(
                    MDButtonIcon(
                        icon="heart",
                    ),
                    MDButtonText(
                        text=text,
                    ),
                    style=style,
                )
            )
            self.root.ids.custom_md_button_box.add_widget(
                MDButton(
                    MDButtonIcon(
                        icon="heart",
                        theme_icon_color="Custom",
                        icon_color="yellow",
                        icon_color_disabled="black",
                    ),
                    MDButtonText(
                        text=text,
                        theme_text_color="Custom",
                        text_color={
                            "filled": "white",
                            "tonal": "white",
                            "outlined": "green",
                            "text": "green",
                            "elevated": "white",
                        }[style],
                    ),
                    style=style,
                    theme_bg_color="Custom",
                    theme_line_color=(
                        "Custom" if style == "outlined" else "Primary"
                    ),
                    md_bg_color={
                        "filled": "brown",
                        "tonal": "brown",
                        "outlined": self.theme_cls.transparentColor,
                        "text": self.theme_cls.transparentColor,
                        "elevated": "red",
                    }[style],
                    line_color="green",
                    md_bg_color_disabled=color_disabled,
                )
            )

        styles = {
            "standard": "surface",
            "small": "secondary",
            "large": "tertiary",
        }
        for style in styles.keys():
            self.root.ids.fab_button_box.add_widget(
                MDFabButton(
                    style=style, icon="pencil-outline", color_map=styles[style]
                )
            )
            self.root.ids.custom_fab_button_box.add_widget(
                MDFabButton(
                    style=style,
                    icon="heart",
                    theme_bg_color="Custom",
                    md_bg_color="brown",
                    theme_icon_color="Custom",
                    icon_color="yellow",
                    icon_color_disabled="lightgrey",
                    md_bg_color_disabled=color_disabled,
                )
            )
        button = MDExtendedFabButton(
            MDExtendedFabButtonIcon(
                icon="pencil-outline",
            ),
            MDExtendedFabButtonText(
                text="Compose",
            ),
            fab_state="expand",
        )
        button.bind(on_release=self.fab_button_expand)
        self.root.ids.extended_fab_button_box.add_widget(
            MDExtendedFabButton(
                MDExtendedFabButtonText(
                    text="Compose",
                    theme_text_color="Custom",
                    text_color="red",
                ),
                fab_state="expand",
            )
        )
        self.root.ids.extended_fab_button_box.add_widget(button)

    def fab_button_expand(self, instance):
        def fab_button_expand(*args):
            instance.fab_state = (
                "expand" if instance.fab_state == "collapse" else "collapse"
            )

        Clock.schedule_once(fab_button_expand, 0.3)


Example().run()
