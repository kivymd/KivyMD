"""
Behaviors/Touch
===============

.. rubric:: Provides easy access to events.

The following events are available:

- on_long_touch
- on_double_tap
- on_triple_tap

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import TouchBehavior
    from kivymd.uix.button import MDRaisedButton

    KV = '''
    MDScreen:

        MyButton:
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class MyButton(MDRaisedButton, TouchBehavior):
        def on_long_touch(self, *args):
            print("<on_long_touch> event")

        def on_double_tap(self, *args):
            print("<on_double_tap> event")

        def on_triple_tap(self, *args):
            print("<on_triple_tap> event")


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MainApp().run()
"""

__all__ = ("TouchBehavior",)

from functools import partial

from kivy.clock import Clock
from kivy.properties import NumericProperty


class TouchBehavior:
    duration_long_touch = NumericProperty(0.4)
    """
    Time for a long touch.

    :attr:`duration_long_touch` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.4`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            on_touch_down=self.create_clock, on_touch_up=self.delete_clock
        )

    def create_clock(self, widget, touch, *args):
        if self.collide_point(touch.x, touch.y):
            if "event" not in touch.ud:
                callback = partial(self.on_long_touch, touch)
                Clock.schedule_once(callback, self.duration_long_touch)
                touch.ud["event"] = callback

        if touch.is_double_tap:
            self.on_double_tap(touch, *args)
        if touch.is_triple_tap:
            self.on_triple_tap(touch, *args)

    def delete_clock(self, widget, touch, *args):
        if self.collide_point(touch.x, touch.y):
            if "event" in touch.ud:
                Clock.unschedule(touch.ud["event"])
                del touch.ud["event"]

    def on_long_touch(self, touch, *args):
        """Called when the widget is pressed for a long time."""

    def on_double_tap(self, touch, *args):
        """Called by double clicking on the widget."""

    def on_triple_tap(self, touch, *args):
        """Called by triple clicking on the widget."""
