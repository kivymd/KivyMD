from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTextField:
        id: field
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .6
        disabled: True

        MDTextFieldLeadingIcon:
            icon: "account"

        MDTextFieldHintText:
            text: "Hint text"

        MDTextFieldHelperText:
            text: "Helper text"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "information"

        MDTextFieldMaxLengthText:
            max_text_length: 10
"""


class TestDisabledTextColor(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_colors(self, *args):
        for group_name in [
            "helper-text-color",
            "leading-icons-color",
            "trailing-icons-color",
            "max-length-color",
        ]:
            group = self.root.ids.field.canvas.before.get_group(group_name)[0]
            assert group.rgba == self.theme_cls.disabledTextColor[:-1] + [0.60]

        group = self.root.ids.field.canvas.after.get_group("hint-text-color")[0]
        assert group.rgba == self.theme_cls.disabledTextColor[:-1] + [0.60]
        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_colors, 2)


TestDisabledTextColor().run()
