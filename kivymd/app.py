"""
App
===

This module contains :class:`MDApp` class that is inherited from
:class:`~kivy.app.App`. :class:`MDApp` has some properties needed for KivyMD
library (like :attr:`~MDApp.theme_cls`).
"""

__all__ = ("MDApp",)

from kivy.app import App
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager


class FpsMonitoring:
    """Adds a monitor to display the current FPS in the toolbar."""

    def fps_monitor_start(self):
        from kivymd.utils.fpsmonitor import FpsMonitor
        from kivy.core.window import Window

        monitor = FpsMonitor()
        monitor.start()
        Window.add_widget(monitor)


class MDApp(App, FpsMonitoring):
    theme_cls = ObjectProperty(ThemeManager())
