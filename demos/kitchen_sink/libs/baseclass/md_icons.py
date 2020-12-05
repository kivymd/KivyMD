from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons


class KitchenSinkMDIcons(Screen):
    def set_list_md_icons(self, text="", search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "KitchenSinkOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)
