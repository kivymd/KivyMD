from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDRectangleFlatIconButton:
        id: button
        icon: "android"
        text: "Button"
        icon_size: "56sp"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestMDRectangleFlatIconButtonIconSize(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_icon_size(self, *args):
        assert self.root.ids.button.height > 50.0
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_icon_size, 1.2)


TestMDRectangleFlatIconButtonIconSize().run()
