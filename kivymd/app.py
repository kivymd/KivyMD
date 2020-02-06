"""
Themes/Material App
===================

This module contains :class:`MDApp` class that is inherited from
:class:`~kivy.app.App`. :class:`MDApp` has some properties needed for ``KivyMD``
library (like :attr:`~MDApp.theme_cls`).

You can turn on the monitor displaying the current ``FPS`` value in your application:

.. code-block:: python

    KV = '''
    Screen:

        MDLabel:
            text: "Hello, World!"
            halign: "center"
    '''

    from kivy.lang import Builder

    from kivymd.app import MDApp


    class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.fps_monitor_start()


    MainApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fps-monitor.png
    :width: 350 px
    :align: center

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
    """
    Instance of :class:`~ThemeManager` class.

    :attr:`theme_cls` is an :class:`~kivy.properties.ObjectProperty`.
    """
