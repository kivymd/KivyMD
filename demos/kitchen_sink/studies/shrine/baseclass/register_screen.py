from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.theming import ThemableBehavior


class ShrineRegisterScreen(ThemableBehavior, Screen):
    """Registration screen. Opens when the application starts."""

    title = StringProperty()
