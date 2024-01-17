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
    "MotionExtendedFabButtonBehavior",
    "MotionDropDownMenuBehavior",
    "MotionDialogBehavior",
    "MotionShackBehavior",
    "MotionDatePickerBehavior",
    "MotionTimePickerBehavior",
)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivymd.uix.behaviors.scale_behavior import ScaleBehavior


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


class MotionExtendedFabButtonBehavior(MotionBase):
    """
    Base class for extended Fab button movement behavior.

    For more information, see in the :class:`~MotionBase` class documentation.
    """

    show_transition = StringProperty("out_circ")
    """
    The type of transition of the widget opening.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_circ'`.
    """

    shift_transition = StringProperty("out_sine")
    """
    Text label transition.

    :attr:`shift_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    show_duration = NumericProperty(0.3)
    """
    Duration of widget display transition.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.3`.
    """

    hide_transition = StringProperty("out_sine")
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

    _x = NumericProperty(0)
    _anim_opacity = None

    def collapse(self, *args) -> None:
        """Collapses the button."""

        def collapse(*args):
            if self._label and self._icon:
                Animation(_x=0, d=self.hide_duration).start(self)
                anim = Animation(
                    width=dp(56), d=self.hide_duration, t=self.hide_transition
                )
                anim.bind(on_progress=self._check_collapse_progress)
                anim.start(self)

        Clock.schedule_once(collapse)

    def expand(self, *args) -> None:
        """Expands the button."""

        def expand(*args):
            if self._label and self._icon:
                anim = Animation(
                    width=self.width
                    + self._label.texture_size[0]
                    + (dp(18) if self._icon else 0),
                    d=self.show_duration,
                    t=self.show_transition,
                )
                anim.bind(on_progress=self._check_expand_progress)
                anim.start(self)
                Animation(
                    _x=dp(12), d=self.show_duration, t=self.shift_transition
                ).start(self)

        Clock.schedule_once(expand)

    def set_opacity_text_button(self, value: int) -> None:
        if self._label:
            self._anim_opacity = Animation(
                opacity=value,
                d=self.show_duration * 16.666666666666668 / 100
                if value
                else self.show_duration * 1.6666666666666667 / 100,
            )
            self._anim_opacity.bind(
                on_complete=lambda *x: setattr(self, "_anim_opacity", None)
            )
            self._anim_opacity.start(self._label)

    def _check_collapse_progress(self, animation, instance, progress) -> None:
        if progress > 0.1:
            if not self._anim_opacity:
                self.set_opacity_text_button(0)

    def _check_expand_progress(self, animation, instance, progress) -> None:
        if progress > 0.3:
            if not self._anim_opacity:
                self.set_opacity_text_button(1)


class MotionDialogBehavior(ScaleBehavior, MotionBase):
    """
    Base class for dialog movement behavior.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior`
    :class:`~MotionBase`
    classes documentation.
    """

    show_transition = StringProperty("out_expo")
    """
    The type of transition of the widget opening.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_expo'`.
    """

    show_button_container_transition = StringProperty("out_circ")
    """
    The type of transition of the widget opening.

    :attr:`show_button_container_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_circ'`.
    """

    hide_transition = StringProperty("out_circ")
    """
    The type of transition of the widget opening.

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'hide_transition'`.
    """

    show_duration = NumericProperty(0.4)
    """
    Duration of widget display transition.

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    def on_dismiss(self, *args):
        """Fired when a dialog closed."""

        def remove_dialog(*args):
            Window.remove_widget(self)
            if self._scrim:
                Window.remove_widget(self._scrim)

        if self._scrim:
            Animation(alpha=0, d=self.hide_duration).start(self._scrim)

        Animation(
            y=self.ids.content_container.y,
            t=self.hide_transition,
            d=self.hide_duration,
        ).start(self.ids.button_container)

        anim = Animation(
            opacity=0,
            scale_value_y=0,
            t=self.hide_transition,
            d=self.hide_duration,
        )
        anim.bind(on_complete=remove_dialog)
        anim.start(self)

    def on_open(self, *args):
        """Fired when a dialog opened."""

        def open(*args):
            self.scale_value_y = 0
            self.scale_value_center = (0, self.center[1] + self.height / 2)
            Animation(
                opacity=1,
                scale_value_y=1,
                t=self.show_transition,
                d=self.show_duration,
            ).start(self)

            Animation(
                y=dp(24),
                t=self.show_button_container_transition,
                d=self.show_duration + 0.15,
            ).start(self.ids.button_container)

            if self._scrim:
                Animation(alpha=0.4, d=self.show_duration).start(self._scrim)

        Clock.schedule_once(open)


class MotionPickerBehavior(MotionDialogBehavior):
    """
    Base class for date/time pickers movement behavior.

    For more information, see in the
    :class:`~MotionDialogBehavior` class documentation.
    """

    _scrim = ObjectProperty()

    def on_open(self, *args):
        """Fired when a dialog opened."""

        def open(*args):
            self.scale_value_y = 0
            self.scale_value_center = (0, self.center[1] + self.height / 2)
            Animation(
                opacity=1,
                scale_value_y=1,
                t=self.show_transition,
                d=self.show_duration,
            ).start(self)

            if self._scrim:
                Animation(alpha=0.4, d=self.show_duration).start(self._scrim)

        Clock.schedule_once(open)

    def on_dismiss(self, *args):
        """Fired when a dialog closed."""

        def remove_dialog(*args):
            Window.remove_widget(self)
            if self._scrim:
                Window.remove_widget(self._scrim)
            self.dispatch("on_dismiss")

        if self._scrim:
            Animation(alpha=0, d=self.hide_duration).start(self._scrim)

        anim = Animation(
            opacity=0,
            scale_value_y=0,
            t=self.hide_transition,
            d=self.hide_duration,
        )
        anim.bind(on_complete=remove_dialog)
        anim.start(self)


class MotionTimePickerBehavior(MotionPickerBehavior):
    """
    Base class for time picker movement behavior.

    For more information, see in the
    :class:`~MotionPickerBehavior` class documentation.
    """


class MotionDatePickerBehavior(MotionPickerBehavior):
    """
    Base class for date picker movement behavior.

    For more information, see in the
    :class:`~MotionPickerBehavior` class documentation.
    """


class MotionShackBehavior(MotionBase):
    """
    The base class for the behavior of the movement of snack bars.

    For more information, see in the
    :class:`~MotionBase` class documentation.
    """

    _interval = 0
    _height = 0

    def on_dismiss(self, *args):
        """Fired when a snackbar closed."""

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
        """Fired when a snackbar opened."""

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
            self.dispatch("on_open")

        Clock.schedule_once(open, 0.2)

    def _wait_interval(self, interval):
        self._interval += interval
        if self._interval > self.duration:
            self.dismiss()
            self._interval = 0
