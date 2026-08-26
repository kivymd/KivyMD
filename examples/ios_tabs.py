from kivy.metrics import dp
from kivy.properties import OptionProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.button import IOSIconButton, MDIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import (
    IOSTabBarButton,
    IOSTabBarHorizontal,
    IOSTabBarItem,
    IOSTabBarItemIcon,
    IOSTabBarItemText,
    IOSTabBarLayout,
    IOSTabBarVertical,
)


class TabBarVertical(IOSTabBarVertical):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        items_data = [
            "home",
            "compass",
            "bell",
            "account",
        ]

        self.widgets = [
            IOSTabBarItem(
                IOSTabBarItemIcon(
                    icon=icon,
                ),
                inactive_color=self.theme_cls.secondaryColor,
                active_color=self.theme_cls.primaryColor,
            )
            for icon in items_data
        ]


class TabBarHorizontal(IOSTabBarHorizontal):
    display_mode = OptionProperty("both", options=["both", "icon", "text"])

    ITEMS_DATA = (
        ("home", "Home"),
        ("compass", "View"),
        ("bell", "Message"),
        ("account", "Account"),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._update_widgets()

    def on_display_mode(self, instance, value):
        if hasattr(self, "items_box"):
            self._update_widgets()

    def _update_widgets(self):
        inactive_color = self.theme_cls.secondaryColor
        active_color = self.theme_cls.primaryColor
        mode = self.display_mode
        widgets = []

        self.height = (
            dp(40) if mode == "text" else (dp(48) if mode == "icon" else dp(65))
        )

        for icon, text in self.ITEMS_DATA:
            children = []

            if mode in ("both", "icon"):
                children.append(IOSTabBarItemIcon(icon=icon))

                if mode == "icon":
                    self.padding = [dp(-4), dp(4), dp(-4), dp(4)]

            if mode in ("both", "text"):
                children.append(IOSTabBarItemText(text=text))

                if mode == "text":
                    self.padding = [dp(4), dp(4), dp(4), dp(4)]

            item = IOSTabBarItem(
                *children,
                inactive_color=inactive_color,
                active_color=active_color,
            )
            widgets.append(item)

            if mode == "text":
                item.padding = [0, dp(6), 0, dp(8)]

        self.widgets = widgets


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        image = FitImage(
            source="bg.jpg",
            opacity=0.3,
        )

        self.tab_bar_icon_text = TabBarHorizontal(
            target_background=image,
            blur_amount=20,
            display_mode="both",
        )

        self.tab_bar_icon = TabBarHorizontal(
            target_background=image,
            blur_amount=20,
            display_mode="icon",
        )

        self.tab_bar_text = TabBarHorizontal(
            target_background=image,
            blur_amount=20,
            display_mode="text",
        )

        self.tab_bar_vertical = TabBarVertical(
            target_background=image,
            blur_amount=20,
        )

        self.widgets = [
            image,
            MDIconButton(
                icon="menu",
                pos_hint={"top": 0.98},
                x=dp(12),
                on_release=lambda x: MDApp.get_running_app().open_menu(x),
            ),
            IOSTabBarLayout(
                self.tab_bar_vertical,
                IOSTabBarButton(
                    IOSIconButton(icon="magnify"),
                    size=(
                        self.tab_bar_vertical.width,
                        self.tab_bar_vertical.width,
                    ),
                    border_radius=[self.tab_bar_vertical.width / 2] * 4,
                    on_release=lambda btn: print("Search pressed!"),
                ),
                orientation="horizontal",
                pos_hint={"center_x": 0.1, "center_y": 0.5},
            ),
            IOSTabBarLayout(
                self.tab_bar_icon_text,
                IOSTabBarButton(
                    IOSIconButton(icon="magnify"),
                    size=(
                        self.tab_bar_icon_text.height,
                        self.tab_bar_icon_text.height,
                    ),
                    border_radius=[self.tab_bar_icon_text.height / 2] * 4,
                    on_release=lambda btn: print("Search pressed!"),
                ),
                orientation="horizontal",
                pos_hint={"center_x": 0.5, "center_y": 0.8},
            ),
            IOSTabBarLayout(
                self.tab_bar_icon,
                orientation="horizontal",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            IOSTabBarLayout(
                self.tab_bar_text,
                orientation="horizontal",
                pos_hint={"center_x": 0.5, "center_y": 0.3},
            ),
        ]


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"

        return HomeScreen()


Example().run()
