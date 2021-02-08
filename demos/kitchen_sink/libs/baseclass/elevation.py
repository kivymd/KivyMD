from kivymd.uix.behaviors import CircularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class KitchenSinkElevationScreen(MDScreen):
    pass


class KitchenSinkElevationExampleCircle(CircularElevationBehavior, MDBoxLayout):
    def on_size(self, *dt):
        self.radius = [self.size[0] / 2]
