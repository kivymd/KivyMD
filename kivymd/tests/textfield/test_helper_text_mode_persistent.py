from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDTextField:
        id: field
        text: "Text"
        helper_text: "Helper text"
        helper_text_mode: "persistent"
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestHelperTextModePersistent(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_helper_text_without_focus(self, *args):
        if self.root.ids.field.focus:
            self.stop()

        assert self.root.ids.field._helper_text_label.texture_size != [0, 0]

        for instruction in self.root.ids.field.canvas.before.children:
            if instruction.group == "helper-text-color":
                assert (
                    instruction.rgba == self.theme_cls.disabled_hint_text_color
                )

        self.root.ids.field.focus = True
        Clock.schedule_once(self.check_helper_text_without_focus, 5)

    def on_start(self):
        Clock.schedule_once(self.check_helper_text_without_focus, 2)


TestHelperTextModePersistent().run()
