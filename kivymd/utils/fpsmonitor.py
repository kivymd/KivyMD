"""
Monitor module
==============

The Monitor module is a toolbar that shows the activity of your current
application :

* FPS

"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty, OptionProperty, StringProperty
from kivy.uix.label import Label

Builder.load_string(
    """
<FpsMonitor>:
    size_hint_y: None
    height: self.texture_size[1]
    text: root._fsp_value
    pos_hint: {root.anchor: 1}
    color: app.theme_cls.surfaceColor

    canvas.before:
        Color:
            rgba: app.theme_cls.onBackgroundColor
        Rectangle:
            pos: self.pos
            size: self.size
"""
)


class FpsMonitor(Label):
    """
    Fps monitor class.

    For more information, see in the
    :class:`~kivy.uix.label.Label` class documentation.
    """

    updated_interval = NumericProperty(0.5)
    """
    FPS refresh rate.

    :attr:`updated_interval` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    anchor = OptionProperty("top", options=["top", "bottom"])
    """
    Monitor position.
    Available option are: 'top', 'bottom'.

    :attr:`anchor` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    _fsp_value = StringProperty()

    def start(self) -> None:
        """Monitor starting."""

        Clock.schedule_interval(self.update_fps, self.updated_interval)

    def update_fps(self, *args) -> None:
        self._fsp_value = "FPS: %f" % Clock.get_fps()
