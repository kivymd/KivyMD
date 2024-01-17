from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty

from kivymd.app import MDApp

KV = """
MDScreen:

    MDButton:
        id: button
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.flag = True

        MDButtonText:
            text: "Text"
"""


class TestOnRelease(MDApp):
    flag = BooleanProperty(False)

    def build(self):
        return Builder.load_string(KV)

    def check_release_flag(self, *args):
        assert self.flag is True
        self.stop()

    def press_button(self, *args):
        self.root.ids.button.dispatch("on_release")
        Clock.schedule_once(self.check_release_flag, 2)

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.press_button, 1)


TestOnRelease().run()
