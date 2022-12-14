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

    MDTextField:
        id: field
        text: "Text"
        icon_right: "gmail"
        hint_text: "Hint text"
        helper_text: "Helper text"
        helper_text_mode: "on_focus"
        max_text_length: 3
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestErrorState(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_field_color(self, *args):
        for instruction in self.root.ids.field.canvas.before.children:
            if instruction.group in ["helper-text-color", "max-length-color"]:
                assert (
                    instruction.rgba == self.theme_cls.disabled_hint_text_color
                )
            elif instruction.group in [
                "active-underline-color",
                "text-color",
                "hint-text-color",
            ]:
                assert instruction.rgba == self.theme_cls.primary_color

        self.stop()

    def set_max_text_length(self, *args):
        field = self.root.ids.field
        field.focus = True
        field.text = "Tex"
        Clock.schedule_once(self.check_field_color, 2)

    def on_start(self):
        Clock.schedule_once(self.set_max_text_length, 2)


TestErrorState().run()
