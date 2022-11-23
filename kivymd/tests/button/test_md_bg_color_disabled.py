from kivy.clock import Clock
from kivy.graphics import Color

from kivymd.app import MDApp
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDFlatButton,
    MDFloatingActionButton,
    MDIconButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
)
from kivymd.uix.screen import MDScreen
from kivymd.utils import asynckivy


class TestMdBgColorDisabled(MDApp):
    def build(self):
        return MDScreen()

    async def generate_buttons(self):
        for button in [
            MDRaisedButton,
            MDFlatButton,
            MDFillRoundFlatButton,
            MDFillRoundFlatIconButton,
            MDFloatingActionButton,
            MDRectangleFlatButton,
            MDRoundFlatButton,
            MDRoundFlatIconButton,
            MDIconButton,
        ]:
            await asynckivy.sleep(0)
            button = button(
                disabled=True,
                md_bg_color_disabled="red",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.root.clear_widgets()
            self.root.add_widget(button)
            Clock.schedule_once(
                lambda y, x=button: self.check_button_md_bg_color_disabled(x), 1
            )

        Clock.schedule_once(lambda x: self.stop(), 2)

    def check_button_md_bg_color_disabled(self, button):
        for instruction in button.canvas.children:
            if isinstance(instruction, Color):
                if instruction.group == "bg-color":
                    assert instruction.rgba == [1.0, 0.0, 0.0, 1.0]

    def on_start(self):
        asynckivy.start(self.generate_buttons())


TestMdBgColorDisabled().run()
