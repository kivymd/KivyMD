from kivy.clock import Clock
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang.builder import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        halign: "center"
        text: "MDLabel"
        allow_selection: True
        color_selection: "red"
"""


class TestColorSelection(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def check_selection(self, *args):
        assert self.root.ids.label.md_bg_color == [1.0, 0.0, 0.0, 1.0]
        self.stop()

    def on_start(self):
        touch = MouseMotionEvent("mouse", "button", self.root.ids.label.pos)
        self.root.ids.label.on_double_tap(touch, ())
        Clock.schedule_once(self.check_selection)


TestColorSelection().run()
