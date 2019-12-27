from kivy.app import App
from kivy.uix.screenmanager import Screen


class KitchenSinkMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": "Example item %d" % i,
                "callback": App.get_running_app().callback_for_menu_items,
            }
            for i in range(7)
        ]
