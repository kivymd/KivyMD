from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: root.width - (self.width + dp(24))
        icon: "menu"

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDButton:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: nav_drawer.set_state("toggle")

                    MDButtonText:
                        text: "Open Drawer"

        MDNavigationDrawer:
            id: nav_drawer
            radius: 0, dp(16), dp(16), 0

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    padding: "16dp", 0, "16dp", "16dp"
                    spacing: "16dp"

                    MDIcon:
                        icon: "card-account-mail-outline"
                        theme_font_size: "Custom"
                        font_size: "56sp"
                        theme_icon_color: "Custom"
                        icon_color: self.theme_cls.primaryColor

                    MDLabel:
                        text: "Gmail"
                        font_style: "Display"
                        role: "medium"
                        theme_line_height: "Custom"
                        line_height: 0
                        adaptive_height: True
                        theme_text_color: "Custom"
                        text_color: self.theme_cls.primaryColor

                MDNavigationDrawerLabel:
                    text: "accaount@gmail.com"
                    theme_text_color: "Custom"
                    text_color: self.theme_cls.primaryColor

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "inbox"

                    MDNavigationDrawerItemText:
                        text: "Inbox"

                    MDNavigationDrawerItemTrailingText:
                        text: "24"
                        theme_text_color: "Custom"
                        text_color: self.theme_cls.primaryColor

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "send-outline"

                    MDNavigationDrawerItemText:
                        text: "Outbox"

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "heart-outline"

                    MDNavigationDrawerItemText:
                        text: "Favorites"

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "trash-can-outline"

                    MDNavigationDrawerItemText:
                        text: "Trash"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Personal folders"
                    theme_text_color: "Custom"
                    text_color: self.theme_cls.primaryColor
                    padding: "16dp", "8dp", 0, 0

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "folder-outline"

                    MDNavigationDrawerItemText:
                        text: "Family"

                MDNavigationDrawerItem:

                    MDNavigationDrawerItemLeadingIcon:
                        icon: "folder-outline"

                    MDNavigationDrawerItemText:
                        text: "Wedding"
"""


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self): ...


Example().run()
