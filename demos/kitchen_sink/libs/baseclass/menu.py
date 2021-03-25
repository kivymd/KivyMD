from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu


class RightContentCls(IRightBodyTouch, MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()


class KitchenSinkMenuRightItem(OneLineAvatarIconListItem):
    left_icon = StringProperty()
    right_icon = StringProperty()
    right_text = StringProperty()


class KitchenSinkMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "text": f"Item {i}",
                "right_text": f"R+{i}",
                "right_icon": "apple-keyboard-command",
                "left_icon": "git",
                "viewclass": "KitchenSinkMenuRightItem",
                "height": dp(54),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=menu_items,
            width_mult=4,
        )
