from kivy.clock import Clock
from kivy.lang.builder import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        halign: "center"
        text: "MDLabel"
        disabled: True
        disabled_color: "red"
"""


class TestDisabledCustomColor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_disabled_color(self, *args):
        assert self.root.ids.label._label.options["color"] == [
            1.0,
            0.0,
            0.0,
            1.0,
        ]
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_disabled_color, 1)


TestDisabledCustomColor().run()
