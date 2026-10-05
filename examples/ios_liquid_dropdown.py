from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.uix.behaviors import IOSLiquidDropdownContainer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import IOSButton, IOSIconButton
from kivymd.uix.imagelist import MDSmartTile, MDSmartTileImage
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.tab import (
    IOSTabBarHorizontal,
    IOSTabBarItemIcon,
    IOSTabBarItemText,
    IOSTabBarItem,
    IOSTabBarLayout,
    IOSTabBarButton,
)

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDScrollView:
        id: scroll
        do_scroll_x: False
        size_hint: 1, 1
        pos_hint: {"top": 1}
        size_hint_y: None
        height: root.height - dp(100)

        MDGridLayout:
            id: tile_grid
            cols: 3
            adaptive_height: True
            padding: ["16dp", "80dp", "16dp", "16dp"]
            spacing: "6dp"

    BoxLayout:
        size_hint_y: None
        height: dp(64)
        padding: ["16dp", 0, "16dp", 0]
        pos_hint: {"top": .99}

        MDLabel:
            text: "Media Library"
            valign: "center"
            theme_font_size: "Custom"
            font_size: "36sp"
            bold: True
"""


class TabBarHorizontal(IOSTabBarHorizontal):
    ITEMS_DATA = (
        ("image-multiple", "Library"),
        ("file-multiple-outline", "Collection"),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._update_widgets()

    def _update_widgets(self):
        inactive_color = self.theme_cls.secondaryColor
        active_color = self.theme_cls.primaryColor
        widgets = []
        self.height = dp(65)

        for icon, text in self.ITEMS_DATA:
            item = IOSTabBarItem(
                IOSTabBarItemIcon(
                    icon=icon
                ),
                IOSTabBarItemText(
                    text=text
                ),
                inactive_color=inactive_color,
                active_color=active_color,
            )
            widgets.append(item)

        self.widgets = widgets


class ListLayout(MDBoxLayout):
    dropdown_container = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        items_data = [
            ("account-circle-outline", "My Profile", "Account settings"),
            ("message-text-outline", "Messages", "Notifications and chats"),
            ("heart-outline", "Favorites", "Saved items"),
            ("cog-outline", "Settings", "App preferences"),
            ("logout-variant", "Log Out", "End current session"),
        ]

        self.orientation = "vertical"
        self.adaptive_height = True
        self.spacing = dp(4)

        for icon, title, subtitle in items_data:
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
                MDListItemSupportingText(
                    text=subtitle,
                    theme_text_color="Custom",
                    text_color=[1, 1, 1, 0.6],
                ),
                theme_bg_color="Custom",
                md_bg_color=[0, 0, 0, 0],
            )

            if self.dropdown_container:
                item.bind(
                    on_release=lambda x: self.dropdown_container.toggle_dropdown()
                )

            self.add_widget(item)


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(KV)

        for i in range(1, 10):
            tile = MDSmartTile(
                MDSmartTileImage(
                    source=f"https://picsum.photos/800/600?random={i}",
                    radius=[dp(24)] * 4,
                ),
                size_hint_y=None,
                height="120dp",
                overlap=False,
                ripple_effect=True,
            )
            screen.ids.tile_grid.add_widget(tile)

        Clock.schedule_once(lambda dt: self.setup_dropdown(screen))
        Clock.schedule_once(lambda dt: self.setup_tabs())

        return screen

    def setup_tabs(self):
        tab_bar_icon_text = TabBarHorizontal(
            target_background=self.root.ids.scroll,
            blur_amount=10,
        )

        self.root.add_widget(
            IOSTabBarLayout(
                tab_bar_icon_text,
                IOSTabBarButton(
                    IOSIconButton(icon="magnify"),
                    size=(
                        tab_bar_icon_text.height,
                        tab_bar_icon_text.height,
                    ),
                    padding=dp(20),
                    border_radius=[tab_bar_icon_text.height / 2] * 4,
                ),
                orientation="horizontal",
                x=dp(24),
                y=dp(24),
            )
        )

    def setup_dropdown(self, screen):
        scroll_widget = screen.ids.scroll

        trigger_btn = IOSButton(
            IOSIconButton(
                icon="filter-variant",
                theme_icon_color="Custom",
                icon_color="white",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            size_hint=[None, None],
            size=[dp(56), dp(56)],
            border_radius=[dp(28)] * 4,
            target_background=scroll_widget,
            pos_hint={"right": 0.98, "top": 0.98},
        )

        dropdown_container = IOSLiquidDropdownContainer(
            direction="bottom-left",
            glass_color=get_color_from_hex("#7EACF9")[:-1] + [0.3],
            spacing=dp(8),
        )

        menu = MDBoxLayout(
            MDScrollView(
                ListLayout(dropdown_container=dropdown_container),
                do_scroll_x=False,
                bar_width=0,
            ),
            size_hint=[None, None],
            size=[dp(320), dp(240)],
            orientation="vertical",
            padding=dp(8),
        )
        menu.border_radius = [dp(24)] * 4

        trigger_btn.bind(
            on_release=lambda x: dropdown_container.toggle_dropdown()
        )

        dropdown_container.widgets = [trigger_btn, menu]
        dropdown_container.caller = trigger_btn
        dropdown_container.menu = menu

        screen.add_widget(dropdown_container)


if __name__ == "__main__":
    Example().run()
