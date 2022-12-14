from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
MDScreen:

    MDTextField:
        id: field
        text: "Text"
        hint_text: "Hint text"
        helper_text: "Helper text"
        helper_text_mode: "persistent"
        icon_right: "gmail"
        size_hint_x: .5
        max_text_length: 3
        pos_hint: {"center_x": .5, "center_y": .5}
        disabled: True
"""


class TestDisabledTextColorSwitchTheme(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_colors(self, *args):
        for instruction in self.root.ids.field.canvas.before.children:
            if instruction.group in [
                "hint-text-color",
                "max-length-color",
                "right-left-icons-color",
                "helper-text-color",
            ]:
                assert (
                    instruction.rgba == self.theme_cls.disabled_hint_text_color
                )

        self.stop()

    def change_theme(self, *args):
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_once(self.check_colors, 3)

    def on_start(self):
        Clock.schedule_once(self.change_theme, 2)


TestDisabledTextColorSwitchTheme().run()
