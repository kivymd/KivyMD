from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.chip import MDChip, MDChipLeadingIcon, MDChipText

from examples.common_app import CommonApp, KV


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        for chip_type in ["assist", "input", "suggestion", "filter"]:
            self.root.ids.widget_box.add_widget(
                MDChip(
                    MDChipLeadingIcon(
                        icon="account",
                    ),
                    MDChipText(
                        text=chip_type.capitalize(),
                    ),
                    type=chip_type,
                )
            )

        for chip_type in ["assist", "input", "suggestion", "filter"]:
            self.root.ids.custom_widget_box.add_widget(
                MDChip(
                    MDChipLeadingIcon(
                        icon="account",
                        theme_icon_color="Custom",
                        icon_color="brown",
                        icon_color_disabled="black",
                    ),
                    MDChipText(
                        text=chip_type.capitalize(),
                        theme_text_color="Custom",
                        text_color="red",
                        text_color_disabled="black",
                    ),
                    type=chip_type,
                    theme_line_color="Custom",
                    line_color="green",
                    line_color_disabled="black",
                )
            )


Example().run()
