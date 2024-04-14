# Test for https://github.com/kivymd/KivyMD/issues/1403 issue.

from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

UI = """
MDScreenManager:

    MDScreen:
        name: "screen one"

        MDLabel:
            text: "This is MDLabel"
            halign: "center"

    MDScreen:
        name: "screen two"
        on_enter: app.callback_change_theme()

        MDLabel:
            id: label_two
            text: "This is MDLabel"
            halign: "center"
"""


class TestSwitchTheme(MDApp):
    def check_label_color(self, *args):
        assert self.root.ids.label_two.color == self.theme_cls.onSurfaceColor
        self.stop()

    def callback_change_theme(self):
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_once(self.check_label_color, 1.2)

    def switch_screen_two(self, *args):
        self.root.current = "screen two"

    def on_start(self):
        Clock.schedule_once(self.switch_screen_two, 1)

    def build(self):
        return Builder.load_string(UI)


TestSwitchTheme().run()
