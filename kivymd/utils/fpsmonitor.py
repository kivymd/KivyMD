"""
Monitor module
==============

The Monitor module is a toolbar that shows the activity of your current
application :

* FPS

"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label

Builder.load_string(
    """
<FpsMonitor>:
    size_hint_y: None
    height: self.texture_size[1]
    text: root._fsp_value
    pos_hint: {"top": 1}

    canvas.before:
        Color:
            rgba: app.theme_cls.primary_dark
        Rectangle:
            pos: self.pos
            size: self.size
"""
)


class FpsMonitor(Label):
    updated_interval = NumericProperty(0.5)
    """FPS refresh rate."""

    _fsp_value = StringProperty()

    def start(self):
        Clock.schedule_interval(self.update_fps, self.updated_interval)

    def update_fps(self, *args):
        self._fsp_value = "FPS: %f" % Clock.get_fps()
