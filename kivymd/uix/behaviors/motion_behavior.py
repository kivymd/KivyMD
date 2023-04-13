"""
Behaviors/Motion
================

.. rubric:: Use motion to make a UI expressive and easy to use.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/motion.png
    :align: center

.. versionadded:: 1.2.0

Classes of the `Motion` type implement the display behavior of widgets such
as dialogs, dropdown menu, snack bars, and so on.
"""

__all__ = (
    "MotionBase",
    "MotionDropDownMenuBehavior",
    "MotionDialogBehavior",
    "MotionShackBehavior",
)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty

from kivymd.uix.behaviors.stencil_behavior import StencilBehavior


class MotionBase:
    """Base class for widget display movement behavior."""

    show_transition = StringProperty("linear")
    """
    The type of transition of the widget opening.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    show_duration = NumericProperty(0.2)
    """
    Duration of widget display transition.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    hide_transition = StringProperty("linear")
    """
    The type of transition of the widget closing.

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    hide_duration = NumericProperty(0.2)
    """
    Duration of widget closing transition.

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """


class MotionDropDownMenuBehavior(MotionBase):
    """
    Base class for the dropdown menu movement behavior.

    For more information, see in the :class:`~MotionBase` class documentation.
    """

    show_transition = StringProperty("out_back")
    """
    The type of transition of the widget opening.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_back'`.
    """

    show_duration = NumericProperty(0.4)
    """
    Duration of widget display transition.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    hide_transition = StringProperty("out_cubic")
    """
    The type of transition of the widget closing.

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    _scale_x = NumericProperty(None)
    """
    Default X-axis scaling values.

    :attr:`_scale_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    _scale_y = NumericProperty(None)
    """
    Default Y-axis scaling values.

    :attr:`_scale_y` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    _opacity = NumericProperty(None)
    """
    Menu transparency values.

    :attr:`_opacity` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_scale()
        # self.set_opacity()

    def set_opacity(self) -> None:
        self._opacity = 0

    def set_scale(self) -> None:
        self._scale_x = 0
        self._scale_y = 0

    def on_dismiss(self) -> None:
        anim = Animation(
            _scale_x=0,
            _scale_y=0,
            # _opacity=0,
            duration=self.hide_duration,
            transition=self.hide_transition,
        )
        anim.bind(on_complete=lambda *args: Window.remove_widget(self))
        anim.start(self)

    def on_open(self, *args):
        anim = Animation(
            _scale_y=1,
            # _opacity=1,
            duration=self.show_duration,
            transition=self.show_transition,
        )
        anim &= Animation(
            _scale_x=1,
            duration=self.show_duration - 0.3,
            transition="out_quad",
        )
        anim.start(self)

    def on__opacity(self, instance, value):
        self.opacity = value

    def on__scale_x(self, instance, value):
        self.scale_value_x = value

    def on__scale_y(self, instance, value):
        self.scale_value_y = value


class MotionDialogBehavior(MotionBase):
    """
    Base class for dialog movement behavior.

    For more information, see in the :class:`~MotionBase` class documentation.
    """

    show_duration = NumericProperty(0.1)
    """
    Duration of widget display transition.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.1`.
    """

    scale_x = NumericProperty(1.5)
    """
    Default X-axis scaling values.

    :attr:`scale_x` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1.5`.
    """

    scale_y = NumericProperty(1.5)
    """
    Default Y-axis scaling values.

    :attr:`scale_y` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1.5`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_default_values()

    def set_default_values(self):
        """Sets default scaled and transparency values."""

        self.scale_value_x = self.scale_x
        self.scale_value_y = self.scale_y
        self.opacity = 0

    def on_dismiss(self, *args):
        """Called when a dialog closed."""

        self.set_default_values()

    def on_open(self, *args):
        """Called when a dialog opened."""

        Animation(
            opacity=1,
            scale_value_x=1,
            scale_value_y=1,
            t=self.show_transition,
            d=self.show_duration,
        ).start(self)


class MotionShackBehavior(StencilBehavior, MotionBase):
    """
    The base class for the behavior of the movement of snack bars.

    For more information, see in the
    :class:`~MotionBase` class and
    :class:`~kivy.uix.behaviors.stencil_behavior.StencilBehavior` class
    documentation.
    """

    _interval = 0
    _height = 0

    def on_dismiss(self, *args):
        """Called when a snackbar closed."""

        def remove_snackbar(*args):
            Window.parent.remove_widget(self)
            self.height = self._height
            self.dispatch("on_dismiss")

        Clock.unschedule(self._wait_interval)
        anim = Animation(
            opacity=0,
            height=0,
            t=self.hide_transition,
            d=self.hide_duration,
        )
        anim.bind(on_complete=remove_snackbar)
        anim.start(self)

    def on_open(self, *args):
        """Called when a snackbar opened."""

        def open(*args):
            self._height = self.height
            self.height = 0
            anim = Animation(
                opacity=1,
                height=self._height,
                t=self.show_transition,
                d=self.show_duration,
            )
            anim.bind(
                on_complete=lambda *args: Clock.schedule_interval(
                    self._wait_interval, 1
                )
            )
            anim.start(self)

        Clock.schedule_once(open)
        self.dispatch("on_open")

    def _wait_interval(self, interval):
        self._interval += interval
        if self._interval > self.duration:
            self.dismiss()
            self._interval = 0
