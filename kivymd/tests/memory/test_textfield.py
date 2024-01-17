from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)

len_callbacks = 0


class MyScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor

    def remove_widget(self, *args, **kwargs) -> None:
        global len_callbacks

        super().remove_widget(*args, **kwargs)
        len_callbacks = len(
            self.theme_cls.get_property_observers("theme_style")
        )


class TestTextFieldMemoryLeak(MDApp):
    counter = 0
    previous_len_callbacks = 0

    def build(self):
        Clock.schedule_interval(self.add_items, 0.5)
        return MyScreen()

    def add_items(self, *args):
        if len_callbacks:
            self.previous_len_callbacks = len_callbacks

        self.counter += 1
        self.root.clear_widgets()
        self.root.add_widget(
            MDTextField(
                MDTextFieldLeadingIcon(
                    icon="account",
                ),
                MDTextFieldHintText(
                    text="Hint text",
                ),
                MDTextFieldHelperText(
                    text="Helper text",
                    mode="persistent",
                ),
                MDTextFieldTrailingIcon(
                    icon="information",
                ),
                MDTextFieldMaxLengthText(
                    max_text_length=10,
                ),
            )
        )

        if self.counter > 10:
            Clock.unschedule(self.add_items)
            assert len_callbacks == self.previous_len_callbacks
            self.stop()


TestTextFieldMemoryLeak().run()
