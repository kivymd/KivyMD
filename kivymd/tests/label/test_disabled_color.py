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
        assert (
            self.root.ids.label.disabled_color
            == self.theme_cls.onSurfaceColor[:-1]
            + [self.root.ids.label.label_opacity_value_disabled_text]
        )
        self.stop()

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.check_disabled_color, 1)


TestDisabledColor().run()
