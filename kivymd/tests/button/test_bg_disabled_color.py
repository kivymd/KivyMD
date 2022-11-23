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


class TestBgDisabledColor(MDApp):
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
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.root.clear_widgets()
            self.root.add_widget(button)
            Clock.schedule_once(
                lambda y, x=button: self.check_button_bg_disabled_color(x), 1
            )

        Clock.schedule_once(lambda x: self.stop(), 2)

    def check_button_bg_disabled_color(self, button):
        if isinstance(
            button,
            (
                MDRectangleFlatButton,
                MDRoundFlatButton,
                MDRoundFlatIconButton,
            ),
        ):
            for instruction in button.canvas.children:
                if isinstance(instruction, Color):
                    if instruction.group == "outline-color":
                        assert (
                            instruction.rgba
                            == self.theme_cls.disabled_primary_color
                        )
            return

        for instruction in button.canvas.children:
            if isinstance(instruction, Color):
                if instruction.group == "bg-color":
                    if isinstance(
                        button,
                        (
                            MDRaisedButton,
                            MDFillRoundFlatButton,
                            MDFillRoundFlatIconButton,
                            MDFloatingActionButton,
                        ),
                    ):
                        assert (
                            instruction.rgba
                            == self.theme_cls.disabled_primary_color
                        )
                    elif isinstance(button, (MDFlatButton, MDIconButton)):
                        assert instruction.rgba == [
                            0.0,
                            0.0,
                            0.0,
                            0.0,
                        ]

    def on_start(self):
        asynckivy.start(self.generate_buttons())


TestBgDisabledColor().run()
