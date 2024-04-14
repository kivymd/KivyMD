from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDIcon:
        id: icon
        icon: "mail"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDBadge:
            id: badge
            text: "12"
"""


class TestMDIconBadgeColorsAfterDisabled(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def icon_undisabled(self, *args):
        self.root.ids.icon.disabled = False

    def check_badge_colors(self, *args):
        assert self.root.ids.badge.text_color == self.theme_cls.onErrorColor
        assert self.root.ids.badge.md_bg_color == self.theme_cls.errorColor

        self.stop()

    def on_start(self):
        Clock.schedule_once(self.icon_undisabled, 1)
        Clock.schedule_once(self.check_badge_colors, 2)


TestMDIconBadgeColorsAfterDisabled().run()
