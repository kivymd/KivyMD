from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDListItem
from examples.common_app import CommonApp
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons

class IconItem(MDListItem):
    icon = StringProperty()
    text = StringProperty()

MAIN_KV = """
#: import images_path kivymd.images_path

<IconItem>
    theme_bg_color:"Custom"
    md_bg_color:[0,0,0,0]
    MDListItemLeadingIcon:
        icon: root.icon

    MDListItemSupportingText:
        text: root.text

MDScreen:
    md_bg_color:app.theme_cls.backgroundColor
    BoxLayout:
        padding:[dp(10), dp(30), dp(10), dp(10)]
        orientation:"vertical"
        
        MDSearchBar:
            id: search_bar
            supporting_text: "Search in text"
            view_root: root
            on_text: app.set_list_md_icons(text=args[-1], search=True)
            
            # Search Bar items
            MDSearchBarLeadingContainer:
                MDSearchLeadingIcon:
                    icon: "menu"
                    on_release: app.open_menu(self)

            MDSearchBarTrailingContainer:
                MDSearchTrailingIcon:
                    icon:"microphone"
                MDSearchTrailingAvatar:
                    source:f"{images_path}/logo/kivymd-icon-128.png"
            
            # Search View
            MDSearchViewLeadingContainer:
                MDSearchLeadingIcon:
                    icon:"arrow-left"
                    on_release: search_bar.close_view()

            MDSearchViewTrailingContainer:
                MDSearchTrailingIcon:
                    icon:"window-close"
                    on_release: search_bar.text = ""

            MDSearchViewContainer:
                RecycleView:
                    id: rv
                    key_viewclass: 'viewclass'
                    key_size: 'height'

                    RecycleBoxLayout:
                        default_size: None, dp(48)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
        Widget:

        BoxLayout:
            size_hint_y:None
            height:dp(30)
            padding:[dp(50), 0]
            spacing:dp(10)
            MDLabel:
                text:"Bar dock"
                halign:"right"
            MDSwitch:
                on_active:search_bar.docked = args[-1]
"""

class Example(MDApp, CommonApp):

    def build(self):
        return Builder.load_string(MAIN_KV)

    def on_start(self):
        self.set_list_md_icons()    

    def set_list_md_icons(self, text="", search=False):
        def add_icon_item(name_icon):
            self.root.ids.rv.data.append(
                {
                    "viewclass": "IconItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.root.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

Example().run()
