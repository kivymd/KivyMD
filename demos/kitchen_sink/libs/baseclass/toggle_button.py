from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDRectangleFlatButton,
    MDFillRoundFlatIconButton,
)


class KitchenSinkToggleButtons(Screen):
    pass


class FillRoundFlatToggleButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.primary_dark
        super().__init__(**kwargs)


class RectangleFlatButtonToggleButton(MDRectangleFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.primary_light
        super().__init__(**kwargs)


class RoundFlatIconToggleButton(MDFillRoundFlatIconButton, MDToggleButton):
    def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.accent_color
        super().__init__(**kwargs)
