from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.screen import MDScreen


class TestSizeHint(MDApp):
    def build(self):
        return MDScreen()

    def generate_buttons(self):
        button = MDButton(
            size_hint_x=1, theme_width="Custom", height=self.root.height
        )
        self.root.clear_widgets()
        self.root.add_widget(button)
        Clock.schedule_once(lambda x: self.check_button_size(button), 1)

    def check_button_size(self, button):
        assert button.size == [800, 600]
        self.stop()

    def on_start(self):
        self.generate_buttons()


TestSizeHint().run()
