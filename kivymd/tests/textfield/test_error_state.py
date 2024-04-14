# Test task:
#
# The text field is in an error state due to the fact that the length
# of the text exceeds the set value in the `max_text_length` parameter.
#
# - set the focus on the text field;
# - delete text characters up to the set value in the `max_text_length`
#   parameter;
# - check the color of the text;
# - check the color of the hint text;
# - check the color of the helper text;
# - check the color of the right icon;
# - check the color of the text max length;

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
            max_text_length: 3
"""


class TestErrorState(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_colors(self, *args):
        for group_name in [
            "helper-text-color",
            "trailing-icons-color",
            "max-length-color",
        ]:
            group = self.root.ids.field.canvas.before.get_group(group_name)[0]
            assert group.rgba == self.theme_cls.errorColor

        group = self.root.ids.field.canvas.before.get_group(
            "leading-icons-color"
        )[0]
        assert group.rgba == self.theme_cls.onSurfaceVariantColor
        group = self.root.ids.field.canvas.after.get_group("hint-text-color")[0]
        assert group.rgba == self.theme_cls.errorColor
        self.stop()

    def set_max_text_length(self, *args):
        field = self.root.ids.field
        field.focus = True
        field.text = "Text"
        Clock.schedule_once(self.check_colors, 2)

    def on_start(self):
        Clock.schedule_once(self.set_max_text_length, 2)


TestErrorState().run()
