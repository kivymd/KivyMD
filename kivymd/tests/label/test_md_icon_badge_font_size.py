from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDIcon:
        id: icon
        icon: "mail"
        badge_icon: "numeric-10"
        badge_font_size: "56sp"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestMDIconBadgeFontSize(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_badge_font_size(self, *args):
        assert self.root.ids.icon.ids.badge.texture_size[0] > 50
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_badge_font_size, 2)


TestMDIconBadgeFontSize().run()
