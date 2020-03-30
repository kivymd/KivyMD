from kivy.uix.screenmanager import Screen

from kivymd.uix.menu import MDDropdownMenu


class MDDropItem(Screen):
    menu = None

    def on_enter(self):
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.ids.dropdown_item,
            items=menu_items,
            position="center",
            callback=self.set_item,
            width_mult=4,
        )

    def set_item(self, instance):
        self.ids.dropdown_item.set_item(instance.text)
