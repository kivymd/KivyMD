from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

len_callbacks = 0


class LabelPotentialMemoryLeak(MDLabel):
    def dec_disabled(self, *args, **kwargs) -> None:
        global len_callbacks

        super().dec_disabled()
        len_callbacks = len(
            self.theme_cls.get_property_observers("theme_style")
        )


class TestLabelMemoryLeak(MDApp):
    counter = 0
    previous_len_callbacks = 0

    def build(self):
        Clock.schedule_interval(self.add_items, 1)
        return MDScreen()

    def add_items(self, *args):
        if len_callbacks:
            self.previous_len_callbacks = len_callbacks

        self.counter += 1
        self.root.clear_widgets()
        self.root.add_widget(
            LabelPotentialMemoryLeak(
                text=f"Count {self.counter}", halign="center"
            )
        )

        if self.counter > 10:
            Clock.unschedule(self.add_items)
            assert len_callbacks == self.previous_len_callbacks
            self.stop()


TestLabelMemoryLeak().run()
