from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


class DropListItem(OneLineAvatarIconListItem):
    icon = StringProperty()


class MDDropItem(MDScreen):
    menu = None

    def on_enter(self):
        menu_items = [
            {
                "viewclass": "DropListItem",
                "icon": "git",
                "height": dp(56),
                "text": f"Item {i}",
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.dropdown_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )

    def set_item(self, text_item):
        self.ids.dropdown_item.set_item(text_item)
        self.menu.dismiss()
