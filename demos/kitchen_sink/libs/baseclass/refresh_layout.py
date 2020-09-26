from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from libs.baseclass.list_items import KitchenSinkOneLineLeftIconItem

from kivymd.icon_definitions import md_icons
from kivymd.utils import asynckivy


class KitchenSinkRefreshLayout(Screen):
    tick = 0
    start = 0
    end = 25

    def on_enter(self):
        if not len(self.ids.box.children):
            self.set_list_for_refresh_layout()

    def set_list_for_refresh_layout(self):
        async def set_list_for_refresh_layout():
            names_icons_list = list(md_icons.keys())[self.start : self.end]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.ids.box.add_widget(
                    KitchenSinkOneLineLeftIconItem(
                        icon=name_icon, text=name_icon
                    )
                )
            self.ids.refresh_layout.refresh_done()

        asynckivy.start(set_list_for_refresh_layout())

    def refresh_callback(self, *args):
        """A method that updates the state of your application
        while the spinner remains on the screen."""

        def refresh_callback(interval):
            self.ids.box.clear_widgets()
            if self.start == 0:
                self.start, self.end = 25, 50
            else:
                self.start, self.end = 0, 25
            self.set_list_for_refresh_layout()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)
