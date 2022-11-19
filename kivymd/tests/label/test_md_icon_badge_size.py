from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDIcon:
        id: icon
        icon: "mail"
        badge_icon: "numeric-10"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestMDIconBadgeSize(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_badge_size(self, *args):
        for instruction in self.root.ids.icon.ids.badge.canvas.before.children:
            if instruction.group == "badge":
                assert instruction.size == (16.0, 16.0)

        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_badge_size, 2)


TestMDIconBadgeSize().run()
