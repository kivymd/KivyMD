from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivymd.uix.behaviors import (
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.taptargetview import MDTapTargetView


class CustomToolbar(
    RectangularElevationBehavior, SpecificBackgroundColorBehavior, BoxLayout
):
    pass


class KitchenSinkTapTargetView(Screen):
    app = ObjectProperty()
    _complete = False

    def on_enter(self):
        self.ids.lbl.opacity = 0
        self.ids.logo.opacity = 1
        self._complete = False

        ttv4 = MDTapTargetView(
            widget=self.ids.add_btn,
            outer_radius=dp(320),
            cancelable=True,
            outer_circle_color=self.app.theme_cls.primary_color[:-1],
            outer_circle_alpha=0.9,
            title_text="This is an add button",
            description_text="You can cancel it by clicking outside",
            widget_position="left_bottom",
        )
        ttv4.bind(on_close=self.complete)

        ttv3 = MDTapTargetView(
            widget=self.ids.info_btn,
            outer_radius=dp(440),
            outer_circle_color=self.app.theme_cls.primary_color[:-1],
            outer_circle_alpha=0.8,
            target_circle_color=[255 / 255, 34 / 255, 212 / 255],
            title_text="This is the info button",
            description_text="No information available yet!",
            widget_position="center",
            title_position="left_bottom",
        )
        ttv3.bind(on_close=ttv4.start)

        ttv2 = MDTapTargetView(
            widget=self.ids.search_btn,
            outer_circle_color=[155 / 255, 89 / 255, 182 / 255],
            target_circle_color=[0.2, 0.2, 0.2],
            title_text="This is the search button",
            description_text="It won't search anything for now.",
            widget_position="center",
            title_position="left_bottom",
        )
        ttv2.bind(on_close=ttv3.start)

        ttv1 = MDTapTargetView(
            widget=self.ids.menu_btn,
            outer_circle_color=self.app.theme_cls.primary_color[:-1],
            outer_circle_alpha=0.85,
            title_text="Menu Button",
            description_text="Opens up the drawer",
            widget_position="center",
            title_position="right_bottom",
        )
        ttv1.bind(on_close=ttv2.start)
        ttv1.start()

    def complete(self, *args):
        Animation(opacity=0.3, d=0.2).start(self.ids.logo)
        Animation(opacity=0.3, d=0.2).start(self.ids.lbl)
        self._complete = True
