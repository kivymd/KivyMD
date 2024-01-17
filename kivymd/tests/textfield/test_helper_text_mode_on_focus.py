# Test task:
#
# - helper text is not displayed (text fields without focus);
# - helper text is displayed (text fields with focus);
# - helper text is not displayed (text fields without focus);

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


class TestHelperTextModeOnFocus(MDApp):
    state = "unchecked"

    def build(self):
        return Builder.load_string(KV)

    def check_helper_text_focus(self, *args):
        field = self.root.ids.field
        focus = field.focus

        instruction = self.root.ids.field.canvas.before.get_group(
            "helper-text-color"
        )[0]
        assert instruction.rgba == (
            [0.0, 0.0, 0.0, 0.0]
            if not focus
            else self.theme_cls.onSurfaceVariantColor
        )

        if self.state == "checked":
            self.stop()

        if field.focus:
            field.focus = False
            self.state = "checked"
            Clock.schedule_once(self.check_helper_text_focus, 2)
            return

        field.focus = True
        Clock.schedule_once(self.check_helper_text_focus, 2)

    def on_start(self):
        super().on_start()
        Clock.schedule_once(self.check_helper_text_focus, 2)


TestHelperTextModeOnFocus().run()
