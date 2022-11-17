from kivy.core.clipboard import Clipboard
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang.builder import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        halign: "center"
        text: "MDLabel"
        allow_copy: True
        on_copy: app.check_selection()
"""


class TestLabelAllowCopy(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_selection(self, *args):
        assert self.root.ids.label.text == Clipboard.paste()
        self.stop()

    def on_start(self):
        touch = MouseMotionEvent("mouse", "button", self.root.ids.label.pos)
        self.root.ids.label.on_double_tap(touch, ())


TestLabelAllowCopy().run()
