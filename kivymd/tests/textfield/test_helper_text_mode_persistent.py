from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTextField:
        id: field
        pos_hint: {"center_x": .5, "center_y": .5}
        text: "Text"
        size_hint_x: .6

        MDTextFieldLeadingIcon:
            icon: "account"

        MDTextFieldHintText:
            text: "Hint text"

        MDTextFieldHelperText:
            text: "Helper text"
            mode: "on_focus"

        MDTextFieldTrailingIcon:
            icon: "information"

        MDTextFieldMaxLengthText:
            max_text_length: 10
"""


class TestHelperTextModePersistent(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_helper_text_without_focus(self, *args):
        if self.root.ids.field.focus:
            self.stop()

        assert self.root.ids.field._helper_text_label.texture_size != [0, 0]

        instruction = self.root.ids.field.canvas.before.get_group(
            "helper-text-color"
        )[0]
        if self.root.ids.field.focus:
            assert instruction.rgba == self.theme_cls.onSurfaceVariantColor
        self.root.ids.field.focus = True
        Clock.schedule_once(self.check_helper_text_without_focus, 5)

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.check_helper_text_without_focus, 2)


TestHelperTextModePersistent().run()
