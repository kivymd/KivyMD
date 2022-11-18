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
"""


class TestDisabledColor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_disabled_color(self, *args):
        assert self.root.ids.label._label.options["color"] == getattr(
            self.theme_cls, "disabled_hint_text_color"
        )
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_disabled_color, 1)


TestDisabledColor().run()
