from kivy.properties import BooleanProperty

from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class RallySettingsScreen(MDScreen):
    list_created = BooleanProperty(False)

    def on_pre_enter(self):
        if not self.list_created:
            items = [
                "Manage accounts",
                "Tax documents",
                "Passcode and Touch ID",
                "Notifications",
                "Personal Information",
                "Paperless settings",
                "Find ATMs",
                "Help",
                "Sign out",
            ]
            for i in items:
                list_item = OneLineListItem(
                    text=i, divider="Inset", font_style="H6"
                )
                list_item.bind(on_release=self.goto_register_screen)
                self.ids._list.add_widget(list_item)
            self.list_created = True

    def goto_register_screen(self, obj):
        self.parent.parent.parent.parent.current = "rally register screen"
        self.parent.parent.parent.ids.nav_bar.set_current(-1)
