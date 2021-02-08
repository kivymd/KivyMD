from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CircularElevationBehavior


class KitchenSinkElevationScreen(MDScreen):
    pass


class KitchenSinkElevationExampleCircle(
    CircularElevationBehavior, MDBoxLayout
):
    def on_size(self, *dt):
        self.radius = [self.size[0] / 2]
