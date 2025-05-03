from kivy.lang import Builder
from kivy.properties import StringProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.navigationrail import MDNavigationRailItem

KV = """
<CommonNavigationRailItem>

    MDNavigationRailItemIcon:
        icon: root.icon

    MDNavigationRailItemLabel:
        text: root.text


MDBoxLayout:

    MDNavigationRail:
        id: rail

        MDNavigationRailMenuButton:
            icon: "menu"
            on_release: app.open_menu(self)

        MDNavigationRailFabButton:
            icon: "home"

        CommonNavigationRailItem:
            icon: "folder-outline"
            text: "Files"

        CommonNavigationRailItem:
            icon: "bookmark-outline"
            text: "Bookmark"

        CommonNavigationRailItem:
            icon: "library-outline"
            text: "Library"

    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor
"""


class CommonNavigationRailItem(MDNavigationRailItem):
    text = StringProperty()
    icon = StringProperty()


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self):
        self.root.ids.rail.disabled = not self.root.ids.rail.disabled


Example().run()
