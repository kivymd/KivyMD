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
            if i.text == current_slide.name.upper():
                i.state = "down"
            else:
                i.state = "normal"


class CraneNavigationLabel(ToggleButtonBehavior, MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = "nav-bar"
        self.font_style = "Button"
        self.adaptive_size = True
        self.halign = "center"
        self.theme_text_color = "Custom"
        self.text_color = (1, 1, 1, 1)
        self.allow_no_selection = False


class CraneListItem(ThemableBehavior, MDBoxLayout):
    text = StringProperty()
    secondary_text = StringProperty()
    image = StringProperty()
