from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDFlatButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
)
from kivymd.uix.screen import MDScreen
from kivymd.utils import asynckivy


class TestTextHalignValign(MDApp):
    data = {
        "halign": {
            "left": {
                "MDRaisedButton": 16.0,
                "MDFlatButton": 8.0,
                "MDFillRoundFlatButton": 16.0,
                "MDFillRoundFlatIconButton": 26.0,
                "MDRectangleFlatButton": 16.0,
                "MDRoundFlatButton": 16.0,
                "MDRoundFlatIconButton": 26.0,
            },
            "right": {
                "MDRaisedButton": 741.0,
                "MDFlatButton": 749.0,
                "MDFillRoundFlatButton": 741.0,
                "MDFillRoundFlatIconButton": 741.0,
                "MDRectangleFlatButton": 741.0,
                "MDRoundFlatButton": 741.0,
                "MDRoundFlatIconButton": 741.0,
            },
            "center": {
                "MDRaisedButton": 378.5,
                "MDFlatButton": 378.5,
                "MDFillRoundFlatButton": 378.5,
                "MDFillRoundFlatIconButton": 383.5,
                "MDRectangleFlatButton": 378.5,
                "MDRoundFlatButton": 378.5,
                "MDRoundFlatIconButton": 383.5,
            },
        },
        "valign": {
            "top": {
                "MDRaisedButton": 575.0,
                "MDFlatButton": 575.0,
                "MDFillRoundFlatButton": 575.0,
                "MDFillRoundFlatIconButton": 574.5,
                "MDRectangleFlatButton": 575.0,
                "MDRoundFlatButton": 575.0,
                "MDRoundFlatIconButton": 574.5,
            },
            "bottom": {
                "MDRaisedButton": 8.0,
                "MDFlatButton": 8.0,
                "MDFillRoundFlatButton": 8.0,
                "MDFillRoundFlatIconButton": 8.5,
                "MDRectangleFlatButton": 8.0,
                "MDRoundFlatButton": 8.0,
                "MDRoundFlatIconButton": 8.5,
            },
            "center": {
                "MDRaisedButton": 291.5,
                "MDFlatButton": 291.5,
                "MDFillRoundFlatButton": 291.5,
                "MDFillRoundFlatIconButton": 291.5,
                "MDRectangleFlatButton": 291.5,
                "MDRoundFlatButton": 291.5,
                "MDRoundFlatIconButton": 291.5,
            },
        },
    }
    exit_flag = 0

    def build(self):
        return MDScreen()

    async def generate_buttons(self, halign, valign):
        self.exit_flag += 1
        for button in [
            MDRaisedButton,
            MDFlatButton,
            MDFillRoundFlatButton,
            MDFillRoundFlatIconButton,
            MDRectangleFlatButton,
            MDRoundFlatButton,
            MDRoundFlatIconButton,
        ]:
            await asynckivy.sleep(0)
            button = button(
                text="Button",
                size_hint=[1, 1],
                halign=halign,
                valign=valign,
            )
            self.root.add_widget(button)
            Clock.schedule_once(
                lambda y, x=button: self.check_button_text_pos(x), 2
            )

    def check_button_text_pos(self, button):
        button_name = button.__class__.__name__
        assert (
            self.data["halign"][button.halign][button_name]
            == button.ids.lbl_txt.x
        )
        assert (
            self.data["valign"][button.valign][button_name]
            == button.ids.lbl_txt.y
        )

        self.root.clear_widgets()
        self.exit_flag += 1
        if self.exit_flag == 48:
            self.stop()

    def on_start(self):
        asynckivy.start(self.generate_buttons(halign="left", valign="top"))
        asynckivy.start(self.generate_buttons(halign="right", valign="top"))
        asynckivy.start(self.generate_buttons(halign="center", valign="top"))
        asynckivy.start(self.generate_buttons(halign="left", valign="bottom"))
        asynckivy.start(self.generate_buttons(halign="right", valign="bottom"))
        asynckivy.start(self.generate_buttons(halign="right", valign="center"))


TestTextHalignValign().run()
