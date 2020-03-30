from kivy.uix.screenmanager import Screen

from kivymd.uix.menu import MDDropdownMenu, RightContent


class RightContentCls(RightContent):
    pass


class KitchenSinkMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [
            {
                "right_content_cls": RightContentCls(
                    text=f"R+{i}", icon="apple-keyboard-command",
                ),
                "icon": "git",
                "text": f"Item {i}",
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button, items=menu_items, width_mult=4
        )
