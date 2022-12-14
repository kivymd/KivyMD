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

    MDTextField:
        id: field
        text: "Text"
        helper_text: "Helper text"
        helper_text_mode: "on_focus"
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestHelperTextModeOnFocus(MDApp):
    state = "unchecked"

    def build(self):
        return Builder.load_string(KV)

    def check_helper_text_focus(self, *args):
        field = self.root.ids.field
        focus = field.focus

        for instruction in self.root.ids.field.canvas.before.children:
            if instruction.group == "helper-text-color":
                assert instruction.rgba == (
                    [0.0, 0.0, 0.0, 0.0]
                    if not focus
                    else self.theme_cls.disabled_hint_text_color
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
        Clock.schedule_once(self.check_helper_text_focus, 2)


TestHelperTextModeOnFocus().run()
