from kivy.lang import Builder

from examples.common_app import KV, CommonApp
from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingAvatar,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
    MDListItemTertiaryText,
    MDListItemTrailingCheckbox,
)


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_tap_list_item(self, list_item: MDListItem):
        print("on_tap_list_item")

    def on_start(self):
        self.root.ids.widget_box.orientation = "vertical"
        self.root.ids.widget_box.add_widget(
            MDListItem(
                MDListItemLeadingIcon(
                    icon="account-outline",
                ),
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
                MDListItemTertiaryText(
                    text="Tertiary text",
                ),
                MDListItemTrailingCheckbox(),
                on_release=self.on_tap_list_item,
            )
        )
        # Custom.
        self.root.ids.custom_widget_box.add_widget(
            MDListItem(
                MDListItemLeadingAvatar(
                    source=f"{images_path}/logo/kivymd-icon-256.png",
                ),
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemTrailingCheckbox(
                    color_disabled="red",
                ),
                divider=True,
                theme_divider_color="Custom",
                divider_color="red",
                theme_bg_color="Custom",
                md_bg_color=[1, 1, 0, 0.3],
            )
        )


Example().run()
