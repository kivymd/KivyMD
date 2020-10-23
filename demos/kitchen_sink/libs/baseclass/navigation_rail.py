import os

from kivy.factory import Factory

from kivymd.uix.screen import MDScreen


class KitchenSinkNavigationRail(MDScreen):
    data = (
        ("dog-side", "african-lion-951778_1280.png"),
        ("human", "beautiful-931152_1280.png"),
        ("human", "guitar-1139397_1280.png"),
        ("dog-side", "kitten-1049129_1280.png"),
        ("head-lightbulb", "light-bulb-1042480_1280.png"),
        ("dog-side", "robin-944887_1280.png"),
    )

    def on_enter(self):
        if not self.ids.box.children:
            self.create_tiles()

    def create_tiles(self, sort=""):
        assets_dir = os.environ["KITCHEN_SINK_ASSETS"]
        for data in self.data:
            if not sort:
                tile = Factory.KitchenSinkNavigationRailTile(
                    source=os.path.join(assets_dir, data[1])
                )
            else:
                if sort in data:
                    tile = Factory.KitchenSinkNavigationRailTile(
                        source=os.path.join(assets_dir, data[1])
                    )
                else:
                    continue
            tile.stars = 3
            self.ids.box.add_widget(tile)

    def sort_tiles(self, instance_rail, instance_item):
        self.ids.box.clear_widgets()
        self.create_tiles(instance_item.icon)
