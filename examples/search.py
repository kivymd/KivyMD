from kivy.lang import Builder
from kivymd.app import MDApp
from examples.common_app import CommonApp
from faker import Faker

MAIN_KV = """
#: import images_path kivymd.images_path

MDScreen:
    md_bg_color:app.theme_cls.backgroundColor
    BoxLayout:
        padding:[dp(10), dp(50)]
        orientation:"vertical"
        
        MDSearchBar:
            id: search_bar
            supporting_text: "Search in text"
            view_root: root
            
            # Search Bar
            MDSearchBarLeadingContainer:
                MDSearchLeadingIcon:
                    icon:"magnify"

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

            MDSearchViewContainer:
                MDLabel:
                    text:"Hello World!"

        Widget:
        MDSwitch:
            on_active:app.theme_cls.theme_style = "Dark" if app.theme_cls.theme_style == "Light" else "Light"
        Widget:
    

"""

class Example(MDApp, CommonApp):
    fake = Faker()
    def build(self):
        return Builder.load_string(MAIN_KV)

Example().run()
