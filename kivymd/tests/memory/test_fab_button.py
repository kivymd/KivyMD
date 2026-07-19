"""
Test that MDFabButton does not leak theme observers when widgets are
created and removed repeatedly.

The test continuously replaces the chip widget on a screen, tracks
the number of theme style observers, and verifies that removing old
MDFabButton instances does not increase the number of registered callbacks.
"""

from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton
from kivymd.uix.screen import MDScreen

len_callbacks = 0


class MyScreen(MDScreen):
    def remove_widget(self, *args, **kwargs) -> None:
        global len_callbacks

        super().remove_widget(*args, **kwargs)
        len_callbacks = len(
            self.theme_cls.get_property_observers("theme_style")
        )


class TestButtonMemoryLeak(MDApp):
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
        self.root.add_widget(MDFabButton(icon="plus"))

        if self.counter > 10:
            Clock.unschedule(self.add_items)
            assert len_callbacks == self.previous_len_callbacks
            self.stop()


if __name__ == "__main__":
    TestButtonMemoryLeak().run()
