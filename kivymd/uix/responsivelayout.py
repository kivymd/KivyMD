# TODO: Add doc string.

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

from kivymd.uix.controllers import WindowController


class MDResponsiveLayout(EventDispatcher, WindowController):
    mobile_view = ObjectProperty()
    tablet_view = ObjectProperty()
    desktop_view = ObjectProperty()

    _current_device_type = ""

    def on_size(self, *args) -> None:
        super().on_size(*args)
        self.set_screen()

        if self._current_device_type != self.real_device_type:
            self._current_device_type = self.real_device_type

    def set_screen(self) -> None:
        if self.real_device_type != self._current_device_type:
            self.clear_widgets()

            if self.real_device_type == "mobile":
                self.add_widget(self.mobile_view)
            elif self.real_device_type == "tablet":
                self.add_widget(self.tablet_view)
            elif self.real_device_type == "desktop":
                self.add_widget(self.desktop_view)
