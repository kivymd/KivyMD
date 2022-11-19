from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDIcon:
        id: icon
        icon: "mail"
        badge_icon: "numeric-10"
        badge_icon_color: "red"
        badge_bg_color: "black"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestMDIconBadgeColors(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_badge_colors(self, *args):
        assert self.root.ids.icon.badge_icon_color == [1.0, 0.0, 0.0, 1.0]
        assert self.root.ids.icon.badge_bg_color == [0.0, 0.0, 0.0, 1.0]

        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_badge_colors, 2)


TestMDIconBadgeColors().run()
