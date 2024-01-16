from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        text: "MDLabel"
        halign: "center"
        theme_text_color: "Custom"
        text_color: "red"
"""


class TestThemeTextColor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        def on_start(*args):
            assert self.root.ids.label.text_color == [1.0, 0.0, 0.0, 1.0]
            self.stop()

        super().on_start()
        Clock.schedule_once(on_start, 2)


TestThemeTextColor().run()
