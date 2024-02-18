from kivy.utils import hex_colormap

from materialyoucolor.utils.platform_utils import SCHEMES
from kivymd.uix.menu import MDDropdownMenu

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        id: root_box
        orientation: "vertical"
        spacing: "12dp"
        padding: "12dp"

        MDIconButton:
            on_release: app.open_menu(self)
            icon: "menu"
    
        ScrollView:
    
            MDBoxLayout:
                orientation: "vertical"
                padding: "32dp", 0, "32dp", "32dp"
                spacing: "24dp"
                adaptive_height: True
        
                MDLabel:
                    adaptive_height: True
                    text: "Standard widget"
        
                MDBoxLayout:
                    id: widget_box
                    adaptive_height: True
                    spacing: "24dp"
        
                Widget:
                    size_hint_y: None
                    height: "12dp"
        
                MDLabel:
                    adaptive_height: True
                    text: "Custom widget"

                MDBoxLayout:
                    id: custom_widget_box
                    adaptive_height: True
                    spacing: "24dp"
"""


class CommonApp:
    menu: MDDropdownMenu = None

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Set palette": lambda: self.set_palette(),
            "Switch theme style": lambda: self.switch_theme(),
            "Switch scheme type": lambda: self.set_scheme_type(),
            "Disabled widgets": lambda: self.disabled_widgets(),
        }.items():
            menu_items.append(
                {
                    "text": item,
                    "on_release": method,
                }
            )
        self.menu = MDDropdownMenu(
            caller=menu_button,
            items=menu_items,
        )
        self.menu.open()

    def switch_palette(self, selected_palette):
        self.theme_cls.primary_palette = selected_palette
    
    def switch_theme(self):
        self.theme_cls.switch_theme()

    def set_palette(self):
        instance_from_menu = self.get_instance_from_menu("Set palette")
        available_palettes = [
            name_color.capitalize() for name_color in hex_colormap.keys()
        ]

        menu_items = []
        for name_palette in available_palettes:
            menu_items.append(
                {
                    "text": name_palette,
                    "on_release": lambda x=name_palette: self.switch_palette(x),
                }
            )
        MDDropdownMenu(
            caller=instance_from_menu,
            items=menu_items,
        ).open()

    def set_scheme_type(self):
        instance_from_menu = self.get_instance_from_menu("Switch scheme type")

        menu_items = []
        for scheme_name in SCHEMES.keys():
            menu_items.append(
                {
                    "text": scheme_name,
                    "on_release": lambda x=scheme_name: self.update_scheme_name(x),
                }
            )
        MDDropdownMenu(
            caller=instance_from_menu,
            items=menu_items,
        ).open()
    
    def update_scheme_name(self, scheme_name):
        self.theme_cls.dynamic_scheme_name = scheme_name

    def get_instance_from_menu(self, name_item):
        index = 0
        rv = self.menu.ids.md_menu
        opts = rv.layout_manager.view_opts
        datas = rv.data[0]

        for data in rv.data:
            if data["text"] == name_item:
                index = rv.data.index(data)
                break

        instance = rv.view_adapter.get_view(
            index, datas, opts[index]["viewclass"]
        )
        return instance

    def disabled_widgets(self):
        for widget in self.root.ids.widget_box.children:
            widget.disabled = not widget.disabled

        for widget in self.root.ids.custom_widget_box.children:
            widget.disabled = not widget.disabled
