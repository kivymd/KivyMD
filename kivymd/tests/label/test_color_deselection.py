from kivy.clock import Clock
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang.builder import Builder

from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        id: label
        halign: "center"
        text: "MDLabel"
        allow_selection: True
"""


class TestColorDeselection(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_selection(self, *args):
        self.root.ids.label.cancel_selection()
        assert self.root.ids.label.md_bg_color == self.theme_cls.backgroundColor
        self.stop()

    def on_start(self):
        super().on_start()
        self.touch = MouseMotionEvent(
            "mouse", "button", self.root.ids.label.pos
        )
        self.root.ids.label.on_double_tap(self.touch, ())
        Clock.schedule_once(self.check_selection)


TestColorDeselection().run()
