"""
Themes/Material App
===================

This module contains :class:`MDApp` class that is inherited from
:class:`~kivy.app.App`. :class:`MDApp` has some properties needed for ``KivyMD``
library (like :attr:`~MDApp.theme_cls`). You can turn on the monitor displaying
the current ``FPS`` value in your application:

.. code-block:: python

    KV = '''
    MDScreen:

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

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import ObjectProperty, StringProperty

from kivymd.theming import ThemeManager


class FpsMonitoring:
    """Implements a monitor to display the current FPS in the toolbar."""

    def fps_monitor_start(self) -> None:
        """Adds a monitor to the main application window."""

        def add_monitor(*args):
            from kivy.core.window import Window

            from kivymd.utils.fpsmonitor import FpsMonitor

            monitor = FpsMonitor()
            monitor.start()
            Window.add_widget(monitor)

        Clock.schedule_once(add_monitor)


class MDApp(App, FpsMonitoring):
    """
    Application class, see :class:`~kivy.app.App` class documentation for more
    information.
    """

    icon = StringProperty("kivymd/images/logo/kivymd-icon-512.png")
    """
    See :attr:`~kivy.app.App.icon` attribute for more information.

    .. versionadded:: 1.1.0

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    adn default to `kivymd/images/logo/kivymd-icon-512.png`.
    """

    theme_cls = ObjectProperty()
    """
    Instance of :class:`~ThemeManager` class.

    .. Warning:: The :attr:`~theme_cls` attribute is already available
        in a class that is inherited from the :class:`~MDApp` class.
        The following code will result in an error!

    .. code-block:: python

        class MainApp(MDApp):
            theme_cls = ThemeManager()
            theme_cls.primary_palette = "Teal"

    .. Note:: Correctly do as shown below!

    .. code-block:: python

        class MainApp(MDApp):
            def build(self):
                self.theme_cls.primary_palette = "Teal"

    :attr:`theme_cls` is an :class:`~kivy.properties.ObjectProperty`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()

    def load_all_kv_files(self, path_to_directory: str) -> None:
        """
        Recursively loads KV files from the selected directory.

        .. versionadded:: 1.0.0
        """

        for path_to_dir, dirs, files in os.walk(path_to_directory):
            # When using the `load_all_kv_files` method, all KV files
            # from the `KivyMD` library were loaded twice, which leads to
            # failures when using application built using `PyInstaller`.
            if "kivymd" in path_to_directory:
                Logger.critical(
                    "KivyMD: "
                    "Do not use the word 'kivymd' in the name of the directory "
                    "from where you download KV files"
                )
            if (
                "venv" in path_to_dir
                or ".buildozer" in path_to_dir
                or os.path.join("kivymd") in path_to_dir
            ):
                continue
            for name_file in files:
                if (
                    os.path.splitext(name_file)[1] == ".kv"
                    and name_file != "style.kv"  # if use PyInstaller
                    and "__MACOS" not in path_to_dir  # if use Mac OS
                ):
                    path_to_kv_file = os.path.join(path_to_dir, name_file)
                    Builder.load_file(path_to_kv_file)
