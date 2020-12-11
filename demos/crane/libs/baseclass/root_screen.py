from kivy.properties import StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class CraneRootScreen(ThemableBehavior, MDScreen):
    def on_slide_complete(
        self, instance_carousel, previous_slide, current_slide, next_slide
    ):
        for i in self.ids.tab.children:
            if i.text == current_slide.name:
                i.state = "down"
            else:
                i.state = "normal"


class CraneNavigationLabel(ToggleButtonBehavior, MDLabel):
    pass


class CraneListItem(ThemableBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    image = StringProperty()
