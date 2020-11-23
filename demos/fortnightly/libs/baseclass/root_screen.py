from kivy.properties import StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class FortnightlyRootScreen(MDScreen):
    pass


class FortnightlyListItem(ThemableBehavior, MDBoxLayout):
    title = StringProperty()
    secondary_text = StringProperty()
    image = StringProperty()
