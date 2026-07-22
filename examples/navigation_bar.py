from kivy.lang import Builder
from kivy.metrics import dp

from examples.common_app import KV, CommonApp
from kivymd.app import MDApp
from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
    MDNavigationItemIcon,
    MDNavigationItemLabel,
)


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ): ...

    def on_start(self):
        self.root.ids.widget_box.height = dp(80)
        self.root.ids.widget_box.add_widget(
            MDNavigationBar(
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="gmail",
                    ),
                    MDNavigationItemLabel(
                        text="Mail",
                    ),
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="twitter",
                    ),
                    MDNavigationItemLabel(
                        text="Twitter",
                    ),
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="linkedin",
                    ),
                    MDNavigationItemLabel(
                        text="LinkedIN",
                    ),
                ),
                on_switch_tabs=self.on_switch_tabs,
            )
        )

        self.root.ids.custom_widget_box.add_widget(
            MDNavigationBar(
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="gmail",
                        theme_icon_color="Custom",
                        icon_color_normal="brown",
                        icon_color_active="white",
                    ),
                    MDNavigationItemLabel(
                        text="Mail",
                        theme_text_color="Custom",
                        text_color_active="white",
                    ),
                    indicator_color="grey",
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="twitter",
                        theme_icon_color="Custom",
                        icon_color_normal="brown",
                        icon_color_active="white",
                    ),
                    MDNavigationItemLabel(
                        text="Twitter",
                        theme_text_color="Custom",
                        text_color_active="white",
                    ),
                    indicator_color="grey",
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="linkedin",
                        theme_icon_color="Custom",
                        icon_color_normal="brown",
                        icon_color_active="white",
                    ),
                    MDNavigationItemLabel(
                        text="LinkedIN",
                        theme_text_color="Custom",
                        text_color_active="white",
                    ),
                    indicator_color="grey",
                ),
                theme_bg_color="Custom",
                md_bg_color="silver",
                on_switch_tabs=self.on_switch_tabs,
            )
        )


Example().run()
