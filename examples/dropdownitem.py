from kivy.lang import Builder

from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp

from examples.common_app import CommonApp

KV = """
MDScreen
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDDropDownItem:
        id: drop_item
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.open_drop_item_menu(self)

        MDDropDownItemText:
            id: drop_text
            text: "Item"
"""


class Example(MDApp, CommonApp):
    drop_item_menu: MDDropdownMenu = None

    def open_drop_item_menu(self, item):
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            }
            for i in range(5)
        ]
        if not self.drop_item_menu:
            self.drop_item_menu = MDDropdownMenu(
                caller=item, items=menu_items, position="center"
            )
        self.drop_item_menu.open()

    def menu_callback(self, text_item):
        self.root.ids.drop_text.text = text_item
        self.drop_item_menu.dismiss()

    def disabled_widgets(self):
        self.root.ids.drop_item.disabled = not self.root.ids.drop_item.disabled

    def build(self):
        return Builder.load_string(KV)


Example().run()
