"""
Test that MDLabel supports copying text to the clipboard when the
allow_copy property is enabled.

The test creates an MDLabel with text copying enabled, simulates a
double-tap event on the label, and verifies that the copied clipboard
content matches the label text.
"""

from kivy.clock import Clock
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
        on_copy: app.check_clipboard()
"""


class TestAllowCopy(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_clipboard(self):
        assert self.root.ids.label.text == Clipboard.paste()
        self.stop()

    def on_start(self):
        def on_start(*args):
            touch = MouseMotionEvent("mouse", "button", self.root.ids.label.pos)
            self.root.ids.label.on_double_tap(touch, ())

        Clock.schedule_once(on_start, 1)


if __name__ == "__main__":
    TestAllowCopy().run()
