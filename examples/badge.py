from kivy.lang import Builder

from examples.common_app import CommonApp
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDIcon:
        id: icon
        icon: "gmail"
        pos_hint: {'center_x': .5, 'center_y': .5}

        MDBadge:
            text: "12"
"""


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def disabled_widgets(self):
        self.root.ids.icon.disabled = not self.root.ids.icon.disabled


Example().run()
