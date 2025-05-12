from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemSecondary,
    MDTabsItemText,
)

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: dp(12)
        icon: "menu"

    MDBoxLayout:
        orientation: "vertical"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .6

        MDTabsPrimary:
            id: primary_tabs
            MDDivider:

            MDTabsCarousel:
                id: primary_related_content_container
                size_hint_y: None
                height: dp(140)

        MDTabsSecondary:
            id: secondary_tabs
            MDDivider:

            MDTabsCarousel:
                id: secondary_related_content_container
                size_hint_y: None
                height: dp(140)
"""


class Example(MDApp, CommonApp):
    def on_start(self):
        for type_tabs in ["primary", "secondary"]:
            if type_tabs == "primary":
                tabs = self.root.ids.primary_tabs
                content_container = (
                    self.root.ids.primary_related_content_container
                )
                item = MDTabsItem
            else:
                tabs = self.root.ids.secondary_tabs
                content_container = (
                    self.root.ids.secondary_related_content_container
                )
                item = MDTabsItemSecondary

            for tab_icon, tab_name in {
                "airplane": "Flights",
                "treasure-chest": "Trips",
                "compass-outline": "Explore",
            }.items():
                tabs.add_widget(
                    item(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
                content_container.add_widget(
                    MDLabel(
                        text=tab_name,
                        halign="center",
                        valign="center",
                    )
                )
                tabs.switch_tab(icon="airplane")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def disabled_widgets(self): ...


Example().run()
