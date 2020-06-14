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
            style_name: "native"
            on_text: app.update_kv_file(self.text)
            size_hint_x: .7

        HotReloadViewer:
            size_hint_x: .3
            path: app.path_to_kv_file
            errors: True
            errors_text_color: 1, 1, 0, 1
            errors_background_color: app.theme_cls.bg_dark
    '''


    class Example(MDApp):
        path_to_kv_file = "kv_file.kv"

        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def update_kv_file(self, text):
            with open(self.path_to_kv_file, "w") as kv_file:
                kv_file.write(text)


    Example().run()

This will display the test.kv and automatically update the display when the
file changes.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/3h6B5Q9VPX0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


.. rubric:: This scripts uses watchdog to listen for file changes. To install
   watchdog.

.. code-block:: bash

   pip install watchdog
"""

import os

from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.uix.scrollview import ScrollView
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string(
    """
<HotReloadErrorText>

    MDLabel:
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color:
            root.errors_text_color if root.errors_text_color \
            else root.theme_cls.text_color
        text: root.text
"""
)


class HotReloadErrorText(ThemableBehavior, ScrollView):
    text = StringProperty()
    """Text errors.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    errors_text_color = ListProperty()
    """
    Error text color.

    :attr:`errors_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """


class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_any_event(self, event):
        self.callback()


class HotReloadViewer(ThemableBehavior, MDBoxLayout):
    """
    :Events:
        :attr:`on_error`
            Called when an error occurs in the KV-file that the user is editing.
    """

    path = StringProperty()
    """Path to KV file.

    :attr:`path` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    errors = BooleanProperty(False)
    """
    Show errors while editing KV-file.

    :attr:`errors` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    errors_background_color = ListProperty()
    """
    Error background color.

    :attr:`errors_background_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    errors_text_color = ListProperty()
    """
    Error text color.

    :attr:`errors_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    _temp_widget = None

    def __init__(self, **kwargs):
        self.observer = Observer()
        self.error_text = HotReloadErrorText()
        super().__init__(**kwargs)
        self.register_event_type("on_error")

    @mainthread
    def update(self, *args):
        """Updates and displays the KV-file that the user edits."""

        Builder.unload_file(self.path)
        self.clear_widgets()
        try:
            self.padding = (0, 0, 0, 0)
            self.md_bg_color = (0, 0, 0, 0)
            self._temp_widget = Builder.load_file(self.path)
            self.add_widget(self._temp_widget)
        except Exception as error:
            self.show_error(error)
            self.dispatch("on_error", error)

    def show_error(self, error):
        """Displays text with a current error."""

        if self._temp_widget and not self.errors:
            self.add_widget(self._temp_widget)
            return
        else:
            if self.errors_background_color:
                self.md_bg_color = self.errors_background_color
            self.padding = ("4dp", "4dp", "4dp", "4dp")
            self.error_text.text = (
                error.message
                if getattr(error, r"message", None)
                else str(error)
            )
            self.add_widget(self.error_text)

    def on_error(self, *args):
        """
        Called when an error occurs in the KV-file that the user is editing.
        """

    def on_errors_text_color(self, instance, value):
        self.error_text.errors_text_color = value

    def on_path(self, instance, value):
        self.observer.schedule(
            HotReloadHandler(self.update, value), os.path.split(value)[0]
        )
        self.observer.start()
        Clock.schedule_once(self.update, 1)
