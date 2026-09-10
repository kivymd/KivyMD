from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(24)
        padding: dp(48)

        MDBoxLayout:
            md_bg_color: self.theme_cls.primaryContainerColor
            radius: dp(56)
            size_hint_y: None
            height: dp(200)

            MDLabel:
                text:
                    "This is a standard MDBoxLayout\\nwith background color" \
                    "but\\nregular rectangular corners."
                halign: "center"
                theme_text_color: "Custom"
                text_color: self.theme_cls.onPrimaryContainerColor

        IOSBoxLayout:
            bg_color: self.theme_cls.primaryContainerColor
            radius: [dp(56)] * 4
            size_hint_y: None
            height: dp(200)

            MDLabel:
                text:
                    "This is an IOSBoxLayout\\nwith background color " \
                    "and\\nsquircl/iOS-style rounded corners."
                halign: "center"
                theme_text_color: "Custom"
                text_color: self.theme_cls.onPrimaryContainerColor

        Widget:

    MDIconButton:
        icon: "menu"
        pos_hint: {"top": 0.98}
        x: dp(12)
        on_release: app.get_running_app().open_menu(self)
"""


class IOSBoxLayoutExampleApp(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)


IOSBoxLayoutExampleApp().run()
