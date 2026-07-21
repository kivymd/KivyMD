"""
Test that MDTextField applies the correct disabled colors to all
internal components.

The test creates a disabled MDTextField with hint text, helper text,
leading and trailing icons, and maximum length text. It verifies that
all disabled elements use the expected disabled text color with the
correct opacity.
"""

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
        field = self.root.ids.field
        field._set_disabled_colors()
        Clock.tick()

        for group_name in [
            "helper-text-color",
            "leading-icons-color",
            "trailing-icons-color",
            "max-length-color",
        ]:
            group = field.canvas.before.get_group(group_name)[0]
            expected = self.theme_cls.onSurfaceVariantColor

            assert group.rgba == expected

        group = field.canvas.after.get_group("hint-text-color")[0]
        expected_rgb = self.theme_cls.primaryColor[:-1]
        actual_rgb = group.rgba[:-1]

        assert actual_rgb == expected_rgb

        self.stop()

    def on_start(self):
        Clock.schedule_once(self.check_colors, 0.5)


if __name__ == "__main__":
    TestDisabledTextColor().run()
