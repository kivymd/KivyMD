from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex


<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"


MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDNavigationRail"
        md_bg_color: rail.md_bg_color

    MDBoxLayout:

        MDNavigationRail:
            id: rail
            md_bg_color: get_color_from_hex("#344954")
            color_normal: get_color_from_hex("#718089")
            color_active: get_color_from_hex("#f3ab44")

            MDNavigationRailItem:
                icon: "language-cpp"
                text: "C++"

            MDNavigationRailItem:
                icon: "language-python"
                text: "Python"

            MDNavigationRailItem:
                icon: "language-swift"
                text: "Swift"

        MDBoxLayout:
            padding: "24dp"

            ScrollView:

                MDList:
                    id: box
                    cols: 3
                    spacing: "12dp"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(9):
            tile = Factory.MyTile(source="cpp.png")
            tile.stars = 5
            self.root.ids.box.add_widget(tile)


Test().run()