"""
HotReloadViewer
===============

.. Note:: The :class:`~HotReloadViewer` class is based on
    the `KvViewerApp <https://github.com/kivy/kivy/blob/master/kivy/tools/kviewer.py>`_ class

:class:`~HotReloadViewer`, for KV-Viewer, is a simple tool allowing you to
dynamically display a KV file, taking its changes into account
(thanks to watchdog). The idea is to facilitate design using the KV language.

Usage
-----

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp

        KV = '''
        #:import KivyLexer kivy.extras.highlight.KivyLexer
        #:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


        BoxLayout:

            CodeInput:
                lexer: KivyLexer()
                on_text: app.update_kv_file(self.text)
                size_hint_x: .6

            HotReloadViewer:
                size_hint_x: .4
                path: app.path_to_kv_file
        '''


        class Example(MDApp):
            path_to_kv_file = "kv_file.kv"

            def build(self):
                return Builder.load_string(KV)

            def update_kv_file(self, text):
                with open(self.path_to_kv_file, "w") as kv_file:
                    kv_file.write(text)


        Example().run()

This will display the test.kv and automatically update the display when the
file changes.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/AV-D73RynoA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

.. note: This scripts uses watchdog to listen for file changes. To install
   watchdog::

   pip install watchdog
"""

import os

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock, mainthread

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from kivymd.uix.label import MDLabel


class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_any_event(self, event):
        self.callback()


class HotReloadViewer(BoxLayout):
    path = StringProperty()
    """Path to KV file.

    :attr:`path` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def __init__(self, **kwargs):
        self.observer = Observer()
        self.error_label = MDLabel()
        super().__init__(**kwargs)

    def on_path(self, instance, value):
        self.observer.schedule(
            HotReloadHandler(self.update, value), os.path.split(value)[0]
        )
        self.observer.start()
        Clock.schedule_once(self.update, 1)

    @mainthread
    def update(self, *args):
        Builder.unload_file(self.path)
        self.clear_widgets()
        try:
            self.add_widget(Builder.load_file(self.path))
            self.padding = (0, 0, 0, 0)
        except Exception as error:
            self.padding = ("4dp", "4dp", "4dp", "4dp")
            self.error_label.text = (
                error.message
                if getattr(error, r"message", None)
                else str(error)
            )
            self.add_widget(self.error_label)
