from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import IOSBoxLayout, MDBoxLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingIcon,
)


class DropDownRightMenu(IOSBoxLayout):
    dropdown_container = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.adaptive_height = True
        self.padding = dp(16)

        widgets = []

        top_layout = MDBoxLayout(
            MDBoxLayout(
                MDAnchorLayout(
                    Image(
                        source="images/universe.png",
                        size_hint=(None, None),
                        size=(dp(72), dp(72)),
                    ),
                    anchor_x="center",
                    anchor_y="center",
                    size_hint_y=None,
                    height=dp(72),
                ),
                MDLabel(
                    text="Classic",
                    halign="center",
                    theme_text_color="Custom",
                    text_color=[1, 1, 1, 1],
                    adaptive_size=True,
                    pos_hint={"center_x": 0.5},
                ),
                MDAnchorLayout(
                    MDListItemLeadingIcon(
                        icon="checkbox-marked-circle",
                        theme_icon_color="Custom",
                        icon_color=[0.1, 0.6, 1, 1],
                    ),
                    anchor_x="center",
                    anchor_y="center",
                    size_hint_y=None,
                    height=dp(24),
                ),
                orientation="vertical",
                size_hint=(None, None),
                width=dp(120),
                height=dp(130),
                spacing=dp(8),
            ),
            MDBoxLayout(
                MDAnchorLayout(
                    Image(
                        source="images/classic.png",
                        size_hint=(None, None),
                        size=(dp(72), dp(72)),
                    ),
                    anchor_x="center",
                    anchor_y="center",
                    size_hint_y=None,
                    height=dp(72),
                ),
                MDLabel(
                    text="Universe",
                    halign="center",
                    theme_text_color="Custom",
                    text_color=[1, 1, 1, 1],
                    adaptive_size=True,
                    pos_hint={"center_x": 0.5},
                ),
                MDAnchorLayout(
                    MDListItemLeadingIcon(
                        icon="checkbox-blank-circle-outline",
                        theme_icon_color="Custom",
                        icon_color=[0.6, 0.6, 0.6, 1],
                    ),
                    anchor_x="center",
                    anchor_y="center",
                    size_hint_y=None,
                    height=dp(24),
                ),
                orientation="vertical",
                size_hint=(None, None),
                width=dp(120),
                height=dp(130),
                spacing=dp(8),
            ),
            orientation="horizontal",
            adaptive_height=True,
            spacing=dp(16),
            padding=[0, 0, 0, dp(12)],
            pos_hint={"center_x": 0.5},
        )
        widgets.append(top_layout)
        widgets.append(
            MDDivider(
                height=dp(1),
                color=[1, 1, 1, 0.1],
            )
        )

        call_item = MDListItem(
            MDListItemLeadingIcon(
                icon="check",
                theme_icon_color="Custom",
                icon_color=[1, 1, 1, 0.9],
            ),
            MDListItemLeadingIcon(
                icon="phone-outline",
                theme_icon_color="Custom",
                icon_color=[1, 1, 1, 0.9],
            ),
            MDListItemHeadlineText(
                text="Calls",
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
            ),
            theme_bg_color="Custom",
            md_bg_color=[0, 0, 0, 0],
        )

        if self.dropdown_container:
            call_item.bind(
                on_release=lambda x: self.dropdown_container.toggle_dropdown()
            )

        widgets.append(call_item)
        widgets.append(
            MDDivider(
                height=dp(1),
                color=[1, 1, 1, 0.1],
            )
        )

        filter_item = MDListItem(
            MDListItemHeadlineText(
                text="Manage filtration",
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
            ),
            theme_bg_color="Custom",
            md_bg_color=[0, 0, 0, 0],
        )

        if self.dropdown_container:
            filter_item.bind(
                on_release=lambda x: self.dropdown_container.toggle_dropdown()
            )

        widgets.append(filter_item)

        self.widgets = widgets
