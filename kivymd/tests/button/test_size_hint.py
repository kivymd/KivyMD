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


class TestSizeHint(MDApp):
    def build(self):
        return MDScreen()

    async def generate_buttons(self):
        for button in [
            MDRaisedButton,
            MDFlatButton,
            MDRectangleFlatButton,
            MDRoundFlatButton,
            MDRoundFlatIconButton,
            MDFillRoundFlatButton,
            MDFillRoundFlatIconButton,
        ]:
            await asynckivy.sleep(0)
            button = button(size_hint=(1, 1))
            self.root.clear_widgets()
            self.root.add_widget(button)
            Clock.schedule_once(lambda x: self.check_button_size(button), 1)

        self.stop()

    def check_button_size(self, button):
        assert button.size == [800, 600]

    def on_start(self):
        asynckivy.start(self.generate_buttons())


TestSizeHint().run()
