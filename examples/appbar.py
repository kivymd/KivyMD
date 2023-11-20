from kivy.lang import Builder

from kivymd.app import MDApp

from examples.common_app import CommonApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.secondaryContainerColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        size_hint_x: .8
        spacing: "12dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTopAppBar:
            id: appbar
            type: "small"
    
            MDTopAppBarLeadingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "arrow-left"
    
            MDTopAppBarTitle:
                text: "AppBar small"
    
            MDTopAppBarTrailingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "attachment"
    
                MDActionTopAppBarButton:
                    icon: "calendar"
    
                MDActionTopAppBarButton:
                    icon: "dots-vertical"

        MDTopAppBar:
            id: appbar_custom
            type: "small"
    
            MDTopAppBarLeadingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "arrow-left"
                    theme_icon_color: "Custom"
                    icon_color: "green"
    
            MDTopAppBarTitle:
                text: "AppBar small"
                theme_text_color: "Custom"
                text_color: "green"
    
            MDTopAppBarTrailingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "attachment"
                    theme_icon_color: "Custom"
                    icon_color: "green"
    
                MDActionTopAppBarButton:
                    icon: "calendar"
                    theme_icon_color: "Custom"
                    icon_color: "green"
    
                MDActionTopAppBarButton:
                    icon: "dots-vertical"
                    theme_icon_color: "Custom"
                    icon_color: "green"
"""


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self):
        self.root.ids.appbar.disabled = not self.root.ids.appbar.disabled
        self.root.ids.appbar_custom.disabled = self.root.ids.appbar.disabled


Example().run()
