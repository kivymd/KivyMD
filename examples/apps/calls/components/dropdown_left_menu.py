from kivy.metrics import dp
from kivy.properties import ObjectProperty

from kivymd.uix.boxlayout import IOSBoxLayout
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingIcon,
)


class DropDownLeftMenu(IOSBoxLayout):
    dropdown_container = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        items_data = [
            ("account-circle-outline", "Name setting"),
            ("check-outline", "Select"),
        ]

        self.orientation = "vertical"
        self.adaptive_height = True
        self.spacing = dp(4)
        widgets = []

        for icon, title in items_data:
            item = MDListItem(
                MDListItemLeadingIcon(
                    icon=icon,
                    theme_icon_color="Custom",
                    icon_color=[1, 1, 1, 0.9],
                ),
                MDListItemHeadlineText(
                    text=title,
                    theme_text_color="Custom",
                    text_color=[1, 1, 1, 1],
                ),
                theme_bg_color="Custom",
                md_bg_color=[0, 0, 0, 0],
            )

            if self.dropdown_container:
                item.bind(
                    on_release=lambda x: self.dropdown_container.toggle_dropdown()
                )

            widgets.append(item)

        self.widgets = widgets
