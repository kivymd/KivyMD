"""
Test that MDBadge restores its theme colors after the parent MDIcon
is enabled again.

The test creates an MDIcon with an attached MDBadge, enables the icon
after the initial disabled state, and verifies that the badge text color
and background color remain equal to the current theme error colors.
"""

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


if __name__ == "__main__":
    TestMDIconBadgeColorsAfterDisabled().run()
