"""
Controllers/WindowController
============================
"""

from kivy.core.window import Window
from kivy.core.window.window_sdl2 import WindowSDL


class WindowController:
    def __init__(self):
        self.window_resizing_direction = "unknown"
        self.__width = Window.width
        Window.bind(on_resize=self._on_resize)

    def get_window_width_resizing_direction(self) -> str:
        return self.window_resizing_direction

    def _set_window_width_resizing_direction(self, width: int) -> None:
        if self.__width > width:
            self.window_resizing_direction = "left"
        elif self.__width < width:
            self.window_resizing_direction = "right"

    def _on_resize(self, window_sdl2: WindowSDL, width: int, height: int) -> None:
        self._set_window_width_resizing_direction(width)
        self.__width = width
