"""
Components/ProgressIndicator
============================

.. seealso::

    `Material Design spec, ProgressIndicator <https://m3.material.io/components/progress-indicators/overview>`_

.. rubric:: Progress indicators show the status of a process in real time.

- Use the same progress indicator for all instances of a process (like loading)
- Two types: linear and circular
- Never use them as decoration
- They capture attention through motion

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-indicator-types.png
    :align: center

1. Linear progress indicator
2. Circular progress indicator

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDLinearProgressIndicator:
            size_hint_x: .5
            value: 50
            pos_hint: {'center_x': .5, 'center_y': .4}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/linear-progress-indicator-usage.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDCircularProgressIndicator:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-progress-indicator-usage.gif
    :align: center

Linear progress indicators can be determinate or indeterminate.

Determinate linear progress indicator
-------------------------------------

Determinate operations display the indicator increasing from 0 to 100% of the
track, in sync with the process’s progress.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDLinearProgressIndicator:
            id: progress
            size_hint_x: .5
            type: "determinate"
            pos_hint: {'center_x': .5, 'center_y': .4}
    '''


    class Example(MDApp):
        def on_start(self):
            self.root.ids.progress.start()

        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/determinate-linear-progress-indicator.gif
    :align: center

Circular progress indicators can be determinate or indeterminate.

Indeterminate circular progress indicator
-----------------------------------------

Indeterminate operations display the indicator continually growing and
shrinking along the track until the process is complete..

.. code-block:: kv

    MDCircularProgressIndicator:
        size_hint: None, None
        size: "48dp", "48dp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-progress-indicator-usage.gif
    :align: center

Determinate circular progress indicator
---------------------------------------

.. code-block:: kv

    MDCircularProgressIndicator:
        size_hint: None, None
        size: "48dp", "48dp"
        determinate: True
        on_determinate_complete: print(args)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/determinate-circular-progress-indicator.gif
    :align: center

API break
=========

1.1.1 version
-------------

.. code-block:: kv

    MDProgressBar:
        value: 50
        color: app.theme_cls.accent_color

.. code-block:: kv

    MDSpinner:
        size_hint: None, None
        size: dp(48), dp(48)

2.0.0 version
-------------

.. code-block:: kv

    MDLinearProgressIndicator:
        value: 50
        indicator_color: app.theme_cls.errorColor

.. code-block:: kv

    MDCircularProgressIndicator:
        size_hint: None, None
        size: dp(48), dp(48)
"""

__all__ = ("MDCircularProgressIndicator", "MDLinearProgressIndicator")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    VariableListProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import DeclarativeBehavior

with open(
    os.path.join(uix_path, "progressindicator", "progressindicator.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDLinearProgressIndicator(DeclarativeBehavior, ThemableBehavior, ProgressBar):
    """
    Implementation of the linear progress indicator.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.progressbar.ProgressBar`
    classes documentation.
    """

    radius = VariableListProperty([0], length=4)
    """
    Progress line radius.

    .. versionadded:: 1.2.0

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    reversed = BooleanProperty(False)
    """
    Reverse the direction the progressbar moves.

    :attr:`reversed` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    orientation = OptionProperty(
        "horizontal", options=["horizontal", "vertical"]
    )
    """
    Orientation of progressbar. Available options are: `'horizontal '`,
    `'vertical'`.

    :attr:`orientation` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'horizontal'`.
    """

    indicator_color = ColorProperty(None)
    """
    Color of the active track.

    .. versionchanged:: 2.0.0

        Rename from `color` to `indicator_color` attribute.

    :attr:`indicator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    track_color = ColorProperty(None)
    """
    Progress bar back color in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    .. versionchanged:: 2.0.0

        Rename from `back_color` to `track_color` attribute.

    :attr:`track_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    running_determinate_transition = StringProperty("out_quart")
    """
    Running transition.

    .. versionchanged:: 2.0.0

        Rename from `running_transition` to `running_determinate_transition`
        attribute.

    :attr:`running_determinate_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quart'`.
    """

    catching_determinate_transition = StringProperty("out_quart")
    """
    Catching transition.

    .. versionchanged:: 2.0.0

        Rename from `catching_transition` to `catching_determinate_transition`
        attribute.

    :attr:`catching_determinate_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quart'`.
    """

    running_determinate_duration = NumericProperty(2.5)
    """
    Running duration.

    .. versionchanged:: 2.0.0

        Rename from `running_duration` to `running_determinate_duration`
        attribute.

    :attr:`running_determinate_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.5`.
    """

    catching_determinate_duration = NumericProperty(0.8)
    """
    Catching duration.

    :attr:`running_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    type = OptionProperty(
        None, options=["indeterminate", "determinate"], allownone=True
    )
    """
    Type of progressbar. Available options are: `'indeterminate '`,
    `'determinate'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    running_indeterminate_transition = StringProperty("in_cubic")
    """
    Running transition.

    :attr:`running_indeterminate_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'in_cubic'`.
    """

    catching_indeterminate_transition = StringProperty("out_quart")
    """
    Catching transition.

    :attr:`catching_indeterminate_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quart'`.
    """

    running_indeterminate_duration = NumericProperty(0.5)
    """
    Running duration.

    :attr:`running_indeterminate_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    catching_indeterminate_duration = NumericProperty(0.8)
    """
    Catching duration.

    :attr:`catching_indeterminate_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    _x = NumericProperty(0)

    def __init__(self, **kwargs):
        self.catching_anim = None
        self.running_anim = None
        super().__init__(**kwargs)
        Clock.schedule_once(self.check_size)

    def check_size(self, *args) -> None:
        if self.height == 100:
            if self.orientation == "horizontal":
                self.size_hint_y = None
                self.height = dp(4)
            elif self.orientation == "vertical":
                self.size_hint_x = None
                self.width = dp(4)

    def start(self) -> None:
        """Start animation."""

        if self.type in ("indeterminate", "determinate"):
            Clock.schedule_once(self._set_default_value)
            if not self.catching_anim and not self.running_anim:
                if self.type == "indeterminate":
                    self._create_indeterminate_animations()
                else:
                    self._create_determinate_animations()
            self.running_away()

    def stop(self) -> None:
        """Stop animation."""

        Animation.cancel_all(self)
        self._set_default_value(0)

    def running_away(self, *args) -> None:
        self._set_default_value(0)
        self.running_anim.start(self)

    def catching_up(self, *args) -> None:
        if self.type == "indeterminate":
            self.reversed = True
        self.catching_anim.start(self)

    # FIXME: This method fixes a bug: the indicator values are not set to 0.
    def on_value(self, instance, value):
        if not value:
            self.value = 0.01

    def _create_determinate_animations(self):
        self.running_anim = Animation(
            value=100,
            opacity=1,
            t=self.running_determinate_transition,
            d=self.running_determinate_duration,
        )
        self.running_anim.bind(on_complete=self.catching_up)
        self.catching_anim = Animation(
            opacity=0,
            t=self.catching_determinate_transition,
            d=self.catching_determinate_duration,
        )
        self.catching_anim.bind(on_complete=self.running_away)

    def _create_indeterminate_animations(self):
        self.running_anim = Animation(
            _x=self.width / 2,
            value=50,
            t=self.running_indeterminate_transition,
            d=self.running_indeterminate_duration,
        )
        self.running_anim.bind(on_complete=self.catching_up)
        self.catching_anim = Animation(
            value=0,
            t=self.catching_indeterminate_transition,
            d=self.catching_indeterminate_duration,
        )
        self.catching_anim.bind(on_complete=self.running_away)

    def _set_default_value(self, interval):
        self._x = 0
        self.opacity = 1
        self.value = 0
        self.reversed = False


class MDCircularProgressIndicator(ThemableBehavior, Widget):
    """
    Implementation of the circular progress indicator.

    .. versionchanged:: 2.0.0

        Rename `MDSpinner` to `MDCircularProgressIndicator` class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.widget.Widget`
    classes documentation.

    It can be used either as an indeterminate indicator that loops while
    the user waits for something to happen, or as a determinate indicator.

    Set :attr:`determinate` to **True** to activate determinate mode, and
    :attr:`determinate_time` to set the duration of the animation.

    :Events:
        `on_determinate_complete`
            The event is called at the end of the indicator loop in the
            `determinate = True` mode.
    """

    determinate = BooleanProperty(False)
    """
    Determinate value.

    :attr:`determinate` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    determinate_time = NumericProperty(2)
    """
    Determinate time value.

    :attr:`determinate_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    line_width = NumericProperty(dp(2.25))
    """
    Progress line width of indicator.

    :attr:`line_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(2.25)`.
    """

    active = BooleanProperty(True)
    """
    Use :attr:`active` to start or stop the indicator.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    color = ColorProperty(None)
    """
    Indicator color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    palette = ListProperty()
    """
    A set of colors. Changes with each completed indicator cycle.

    :attr:`palette` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    _alpha = NumericProperty(0)
    _rotation_angle = NumericProperty(360)
    _angle_start = NumericProperty(0)
    _angle_end = NumericProperty(0)
    _palette = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._alpha_anim_in = Animation(_alpha=1, duration=0.8, t="out_quad")
        self._alpha_anim_out = Animation(_alpha=0, duration=0.3, t="out_quad")
        self._alpha_anim_out.bind(
            on_complete=self._reset,
            on_progress=self._on_determinate_progress,
        )
        self.register_event_type("on_determinate_complete")
        Clock.schedule_once(self.check_determinate)

    def on__rotation_angle(self, *args):
        if self._rotation_angle == 0:
            self._rotation_angle = 360
            if not self.determinate:
                _rot_anim = Animation(_rotation_angle=0, duration=2)
                _rot_anim.start(self)
        elif self._rotation_angle == 360:
            if self._palette:
                try:
                    Animation(color=next(self._palette), duration=2).start(self)
                except StopIteration:
                    self._palette = iter(self.palette)
                    Animation(color=next(self._palette), duration=2).start(self)

    def on_palette(self, instance, palette_list: list) -> None:
        """Fired when the `palette` value changes."""

        self._palette = iter(palette_list)

    def on_active(self, instance, value) -> None:
        """Fired when the `active` value changes."""

        self._reset()
        if self.active:
            self.check_determinate()

    def on_determinate_complete(self, *args) -> None:
        """
        The event is fired at the end of the indicator loop in the
        `determinate = True` mode.
        """

        self._angle_start = 0
        self._angle_end = 0
        self._rotation_angle = 360
        self._alpha = 0
        Clock.schedule_once(self._start_determinate)

    def check_determinate(self, *args) -> None:
        """Fired when the class is initialized."""

        if self.active:
            if self.determinate:
                self._start_determinate()
            else:
                self._start_loop()

    def _update_color(self, *args):
        self.color = self.theme_cls.primaryColor

    def _start_determinate(self, *args):
        self._alpha_anim_in.start(self)
        Animation(
            _rotation_angle=0,
            duration=self.determinate_time * 0.7,
            t="out_quad",
        ).start(self)

        _angle_start_anim = Animation(
            _angle_end=360, duration=self.determinate_time, t="in_out_quad"
        )
        _angle_start_anim.bind(
            on_complete=lambda *x: self._alpha_anim_out.start(self)
        )
        _angle_start_anim.start(self)

    def _start_loop(self, *args):
        if self._alpha == 0:
            _rot_anim = Animation(_rotation_angle=0, duration=2, t="linear")
            _rot_anim.start(self)

        self._alpha = 1
        self._alpha_anim_in.start(self)
        _angle_start_anim = Animation(
            _angle_end=self._angle_end + 270, duration=0.6, t="in_out_cubic"
        )
        _angle_start_anim.bind(on_complete=self._anim_back)
        _angle_start_anim.start(self)

    def _anim_back(self, *args):
        _angle_back_anim = Animation(
            _angle_start=self._angle_end - 8, duration=0.6, t="in_out_cubic"
        )
        _angle_back_anim.bind(on_complete=self._start_loop)

        _angle_back_anim.start(self)

    def _reset(self, *args):
        Animation.cancel_all(
            self,
            "_angle_start",
            "_rotation_angle",
            "_angle_end",
            "_alpha",
            "color",
        )
        self._angle_start = 0
        self._angle_end = 0
        self._rotation_angle = 360
        self._alpha = 0

    def _on_determinate_progress(self, animation, instance, value):
        if value == 1:
            self.dispatch("on_determinate_complete")
