"""
Components/ExProgressIndicator
==============================

.. seealso::

    `Material Design spec, Progress indicators <https://m3.material.io/components/progress-indicators/overview>`_

.. rubric:: Expressive progress indicators with wave-style animation.

- Adds wave amplitude, speed, and wavelength controls.
- Supports determinate and indeterminate modes.
- Circular indeterminate mode features retreat and advance animation styles.
- Linear indeterminate mode offers contiguous and discontinuous visual options.
- Linear and circular variants.

.. image:: https://github.com/user-attachments/assets/e58e0274-d8c4-42c2-aae8-211907f95788
    :align: center
    :alt: Linear and circular expressive progress indicator variants.


Terminologies
-------------

.. image:: https://github.com/user-attachments/assets/181298fc-0751-4b42-9b59-7ed7150ff0a8
    :align: center
    :alt: Linear and circular expressive progress indicator variants.
    :width: 400px
- *Amplitude* measures from the center of the resting position to the center of the peak

.. image:: https://github.com/user-attachments/assets/04519538-9e7f-4b11-a434-1eab03fad560
    :align: center
    :alt: Linear and circular expressive progress indicator variants.
    :width: 400px

- *Wavelength* measures the distance between two adjacent peaks

Usage
-----

Linear
~~~~~~~~

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDExLinearProgressIndicator:
                    id: linear_indicator
                    size_hint_x: .7
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    amplitude: dp(3)
                    wave_length: dp(40)
                    wave_speed: dp(20)
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.exprogressindicator import MDExLinearProgressIndicator
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDExLinearProgressIndicator(
                                size_hint_x=.7,
                                amplitude="3dp",
                                wave_length="40dp",
                                wave_speed="20dp",
                                pos_hint={"center_x": .5, "center_y": .5},
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/user-attachments/assets/d433c88a-24ea-46ce-acd5-4dd2f901d578
    :align: center
    :alt: Example of a linear expressive progress indicator in use.

Circular
~~~~~~~~

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDExCircularProgressIndicator:
                    size_hint: None, None
                    size: "48dp", "48dp"
                    pos_hint: {'center_x': .5, 'center_y': .5}
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.exprogressindicator import MDExCircularProgressIndicator
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDExCircularProgressIndicator(
                                size_hint=(None, None),
                                size=("48dp", "48dp"),
                                pos_hint={"center_x": .5, "center_y": .5},
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/user-attachments/assets/8c8da3a6-cb70-422b-8be7-cfc29cb40034
    :align: center
    :alt: Example of a circular expressive progress indicator in use.


Determinate and indeterminate modes
-----------------------------------

Both linear and circular indicators support determinate and indeterminate
variants. Set :attr:`MDExBaseProgressBar.determinate` to toggle modes.

Determinate with animated progress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To improve the visual flow of your progress bars, favor the ``easing_emphasized``
transition over linear movement when using :class:`kivy.animation.Animation`.

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.clock import Clock
            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDExLinearProgressIndicator:
                    id: progress
                    size_hint_x: .7
                    determinate: True
                    pos_hint: {'center_x': .5, 'center_y': .5}
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    root = Builder.load_string(KV)
                    Clock.schedule_once(self.animate, 0)
                    return root

                def animate(self, *_):
                    anim = Animation(
                        value=100,
                        d=1.6,
                        t="easing_emphasized",
                    )
                    anim.start(self.root.ids.progress)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.animation import Animation
            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.exprogressindicator import MDExLinearProgressIndicator
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.progress = MDExLinearProgressIndicator(
                        size_hint_x=.7,
                        determinate=True,
                        pos_hint={"center_x": .5, "center_y": .5},
                    )
                    root = MDScreen(
                        self.progress,
                        md_bg_color=self.theme_cls.backgroundColor,
                    )
                    Clock.schedule_once(self.animate, 0)
                    return root

                def animate(self, *_):
                    anim = Animation(
                        value=100,
                        d=1.6,
                        t="easing_emphasized",
                    )
                    anim.start(self.progress)


            Example().run()

.. image:: https://github.com/user-attachments/assets/c0468075-0f63-43b4-9d78-6324de3dd643
    :align: center
    :alt: Determinate expressive progress indicator animation.



.. image:: https://github.com/user-attachments/assets/f68c5cdb-d691-4b6f-b17d-05a4b57724e0
    :align: center
    :alt: Indeterminate expressive progress indicator animation.

Indeterminate animation modes
-----------------------------

Linear indeterminate modes
~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``contiguous``: a single bar that flows continuously across the track.
- ``discontinuous``: two separate bars with gaps between them.

Set the mode with :attr:`MDExLinearProgressIndicator.indeterminate_animator`.

.. code-block:: python

    MDExLinearProgressIndicator(
        indeterminate_animator="contiguous",
    )

.. image:: https://github.com/user-attachments/assets/5f4fbc91-8507-4098-a388-a85ba90afc30
    :align: center
    :alt: Linear contiguous indeterminate animation.

.. code-block:: python

    MDExLinearProgressIndicator(
        indeterminate_animator="discontinuous",
    )

.. image:: https://github.com/user-attachments/assets/c93a29c4-4ce9-4a18-9836-e40df8ae9554
    :align: center
    :alt: Linear discontinuous indeterminate animation.

Circular indeterminate modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``advanced``: multi-phase expansion/collapse with smooth color transitions.
- ``retreat``: a single arc that grows and shrinks with rotating emphasis.

Set the mode with :attr:`MDExCircularProgressIndicator.indeterminate_animator`.

.. code-block:: python

    MDExCircularProgressIndicator(
        indeterminate_animator="advanced",
    )

.. image:: https://github.com/user-attachments/assets/61be6cf2-d98e-46d5-aab9-c824a54e3d16
    :align: center
    :alt: Circular advanced indeterminate animation with color transitions.


.. code-block:: python

    MDExCircularProgressIndicator(
        indeterminate_animator="retreat",
    )

.. image:: https://github.com/user-attachments/assets/1ba0b5de-3824-4209-abe3-e3c5dfeef705
    :align: center
    :alt: Circular retreat indeterminate animation with a single arc.

.. note::

    A comprehensive interactive demo is available in
    :file:`examples/exprogressindicator.py`.
"""

__all__ = (
    "MDExBaseProgressBar",
    "MDExCircularProgressIndicator",
    "MDExLinearProgressIndicator",
)

import math
import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import DeclarativeBehavior

from .animators import (
    LinearIndeterminateDisjointAnimator,
    LinearIndeterminateContiguousAnimator,
    CircularIndeterminateRetreatAnimator,
    CircularIndeterminateAdvancedAnimator,
)


with open(
    os.path.join(uix_path, "exprogressindicator", "exprogressindicator.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDExBaseProgressBar(Widget, DeclarativeBehavior, ThemableBehavior):
    """
    Base class for extended progress indicators.

    Handles shared properties, frame context caching, and wave rendering hooks
    used by both linear and circular indicators.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    classes documentation.
    """

    _value = 0

    def _get_value(self):
        return self._value

    def _set_value(self, value):
        value = max(0, min(self.max, value))
        if value != self._value:
            self._value = value
            return True

    value = AliasProperty(_get_value, _set_value)
    """Current value used for the slider.

    :attr:`value` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the progress bar. If the value is < 0 or >
    :attr:`max`, it will be normalized to those boundaries.
    """

    def get_norm_value(self):
        d = self.max
        if d == 0:
            return 0
        return self.value / float(d)

    def set_norm_value(self, value):
        self.value = value * self.max

    value_normalized = AliasProperty(
        get_norm_value, set_norm_value, bind=("value", "max"), cache=True
    )
    """Normalized value inside the range 0-1::

        >>> pb = ProgressBar(value=50, max=100)
        >>> pb.value
        50
        >>> pb.value_normalized
        0.5

    :attr:`value_normalized` is an :class:`~kivy.properties.AliasProperty`.
    """

    max = NumericProperty(100.0)
    """Maximum value allowed for :attr:`value`.

    :attr:`max` is a :class:`~kivy.properties.NumericProperty` and defaults to
    100.
    """

    active_track_color = ColorProperty([0, 0, 0, 0])
    """Color of active track

    :attr:`active_track_color` is a :class:`~kivy.properties.ColorProperty` and defaults to
    None.
    """

    inactive_track_color = ColorProperty([0, 0, 0, 0])
    """Color of inactive track

    :attr:`inactive_track_color` is a :class:`~kivy.properties.ColorProperty` and defaults to
    None.
    """

    thickness = NumericProperty(dp(4))
    """
    Thickness of tracks

    :attr:`thickness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    spacing = NumericProperty(dp(4))
    """Spacing between tracks/segments.

    :attr:`spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(4)`.
    """

    # wave params
    amplitude = NumericProperty(dp(3))
    """Amplitude of the wave effect.

    :attr:`amplitude` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(3)`.
    """

    wave_speed = NumericProperty(-dp(40))
    """Speed of the wave effect.

    :attr:`wave_speed` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `-dp(40)` per second.
    """

    wave_length = NumericProperty(dp(8))
    """Wavelength of the wave effect.

    :attr:`wave_length` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(40)`.
    """

    # type
    determinate = BooleanProperty(True)
    """Switch between determinate and indeterminate modes.

    :attr:`determinate` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    # each with colors
    color_array = ListProperty([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]])
    """List of RGBA colors used by indeterminate animations.

    :attr:`color_array` is an :class:`~kivy.properties.ListProperty`
    and defaults to three RGBA colors.
    """

    # internal props
    _fctx = {}
    _time = 0
    _ctx_deps = ["center", "spacing", "thickness"]

    _active_line_objs = []
    _inactive_line_objs = []
    _active_names = ["active_track"]
    _inactive_names = ["inactive_track"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._fctx = {}
        self._time = 0
        Clock.schedule_once(self._start, 0)

    _init = False

    def _start(self, *args):
        if self.canvas is None:
            return Clock.schedule_once(self._start, 0)

        self._init = True
        self._active_line_objs = []
        self._inactive_line_objs = []

        self.on_determinate(self, self.determinate)
        self.save_frame_context()

        Clock.schedule_interval(self._render_wave, 0)
        self.bind(**dict.fromkeys(self._ctx_deps, self.save_frame_context))

    def color_obj(self, line_name):
        """Get color object from line."""
        return self.canvas.get_group(line_name + "_color")[0]

    def reset_colors(self):
        # active lines
        for line in self._active_names:
            self.color_obj(line).rgba = self.active_track_color
        # inactive lines
        for line in self._inactive_names:
            self.color_obj(line).rgba = self.inactive_track_color

    def refresh_lines(self, line_list):
        """Clears points and returns a reusable queue."""
        for line in line_list:
            line.points = []
        return line_list[:]

    def setup_lines(self, *args):
        """init line objs"""
        self._active_line_objs = [
            self.canvas.get_group(name)[0] for name in self._active_names
        ]
        self._inactive_line_objs = [
            self.canvas.get_group(name)[0] for name in self._inactive_names
        ]
        self.refresh_lines(self._active_line_objs)
        self.refresh_lines(self._inactive_line_objs)

    def _render_wave(self, dt):
        self._time += dt
        if self.determinate:
            return self.render_determinate_wave()
        else:
            return self.render_indeterminate_wave()

    def render_determinate_wave(self): ...

    def render_indeterminate_wave(self): ...

    def save_frame_context(self, *args): ...

    def on_determinate(self, instance, value):
        if not self._init:
            return False
        self.setup_lines()
        self.reset_colors()
        self._time = 0
        return True

    def get_amplitude(self, A, t):
        """fade in/out for amplitude using quadratic easing."""
        if t < 0.05:
            # fade-in: (t/0.05)^2
            return A * (400.0 * t * t)

        if t > 0.95:
            # fade-out: ((1-t)/0.05)^2
            inv_t = 1.0 - t
            return A * (400.0 * inv_t * inv_t)

        return A


class MDExLinearProgressIndicator(MDExBaseProgressBar):
    """
    Implementation of the linear progress indicator.

    For more information, see in the
    :class:`~kivymd.uix.exprogressindicator.MDExBaseProgressBar` and
    classes documentation.
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

    # options
    # discontinuous and contiguous
    indeterminate_animator = StringProperty("discontinuous")
    """
    Name of the indeterminate animator to use for linear mode.
    Available options are: `'contiguous'`, `'discontinuous'`.

    :attr:`indeterminate_animator` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    `'discontinuous'`.
    """

    _discts_animator = None
    _cont_animator = None

    _active_line_objs = []
    _inactive_line_objs = []
    _active_names = ["active_track", "active_track_1"]
    _inactive_names = ["inactive_track", "inactive_track_1"]

    def _start(self, *args):
        super()._start(*args)

        self._discts_animator = LinearIndeterminateDisjointAnimator()
        self._cont_animator = LinearIndeterminateContiguousAnimator()
        self._cont_animator.len_palette = 3
        # bind to some values
        self.bind(
            **dict.fromkeys(["thickness", "amplitude"], self.on_orientation)
        )
        # run it once
        Clock.schedule_once(self.on_orientation)

    def save_frame_context(self, *args):
        """Pre-calculate geometry and spacing factors for the current frame."""
        is_horizontal = self.orientation == "horizontal"
        if is_horizontal:
            ax_s = self.x
            ax_size = self.width
            center = self.center_y
            inv = None
        else:
            ax_s = self.y
            ax_size = self.height
            center = self.center_x
            inv = -1

        thickness = self.thickness
        t_h = thickness * 0.5
        track_l = ax_size - thickness - 1.0

        spacing = self.spacing
        total_g = spacing + thickness
        self._fctx = {
            "origin": ax_s + t_h,
            "track_l": track_l,
            "center": center,
            "inv": inv,
            "t_h": t_h,
            "spacing": spacing,
            "gap_p": total_g * 0.5,
            "fade": total_g * 2.0 - t_h,
        }

    def on_color_array(self, instance, value):
        if self._cont_animator is not None:
            self._cont_animator.len_palette = len(value)

    def reset_colors(self, *args):
        super().reset_colors(*args)
        dot = self.canvas.get_group("dot")[0]
        dot.rgba = self.active_track_color[:-1] + [int(self.determinate)]

    def on_indeterminate_animator(self, instance, value):
        if value == "discontinuous" and not self.determinate:
            self.on_determinate(instance, False)

    def on_orientation(self, *args):
        if self.orientation == "vertical":
            self.size_hint_x = None
            self.size_hint_y = 1
            self.width = self.amplitude * 2 + self.thickness
        else:
            self.size_hint_y = None
            self.size_hint_x = 1
            self.height = self.amplitude * 2 + self.thickness
        self.save_frame_context()

    def w_seg(self, start, end) -> list:
        """High-performance wave point generator."""
        fctx = self._fctx
        amplitude = self.amplitude
        if self.determinate:
            amplitude = self.get_amplitude(amplitude, self.value_normalized)

        k = 2 * math.pi / max(0.01, self.wave_length)
        phase = self.wave_speed * self._time

        points = []
        _sin = math.sin

        if fctx["inv"] is None:  # horizontal
            cy = fctx["center"]
            for x in range(int(start), int(end), 1):
                points.extend((x, cy + amplitude * _sin(k * (x - phase))))
        else:
            cx = fctx["center"]
            for y in range(int(start), int(end), 1):
                points.extend((cx + amplitude * _sin(k * (y - phase)), y))

        return points

    def cleanup_lines(self, line_groups):
        for group in line_groups:
            self.canvas.get_group(group)[0].points = []
        return line_groups

    def compute_inactive_segments(self, active_bars):
        # filter noise and sort
        valid = sorted(
            [(s, e) for s, e in active_bars if (e - s) > 0.001],
            key=lambda x: x[0],
        )

        if not valid:
            return [(0.0, 1.0)]

        inactive = []
        cur = 0.0
        for s, e in valid:
            if s > cur:
                inactive.append((cur, s))
            cur = max(cur, e)

        if cur < 1.0:
            inactive.append((cur, 1.0))
        return inactive

    def render_determinate_wave(self):
        ctx = self._fctx
        v_n = self.value_normalized

        # active line
        s, e = self.get_segment_coords(0.0, v_n)
        dot_size = dp(2)

        # dot when progress is 0
        if e - s <= ctx["spacing"]:
            e = s + dot_size

        self._active_line_objs[0].points = self.w_seg(s, e)

        # inactive Line
        s_i, e_i = self.get_segment_coords(v_n, 1.0, do_fade=False)

        # setup dot at starting
        _dist = ctx["origin"] + ctx["track_l"]
        s_i = max(
            ctx["origin"] + ctx["gap_p"] * 2 + dot_size,
            min(s_i, _dist - ctx["t_h"] / 2),
        )
        e_i = min(_dist, e_i)

        center = ctx["center"]
        inv = ctx["inv"]
        self._inactive_line_objs[0].points = [
            [s_i, center][::inv],
            [e_i, center][::inv],
        ]

    def get_segment_coords(self, s_f, e_f, do_fade=True):
        """Calculates points ensuring consistent visual gaps."""
        fctx = self._fctx
        origin = fctx["origin"]
        track_l = fctx["track_l"]
        gap_p = fctx["gap_p"]
        fade = fctx["fade"] if do_fade else 1

        # calculate distance from edges for the "fade" effect
        dist_s = s_f * track_l
        dist_e = (1.0 - e_f) * track_l

        # compute stretch factors (0.0 at wall, 1.0 in middle)
        s_fac = dist_s / fade if dist_s < fade else 1.0
        e_fac = dist_e / fade if dist_e < fade else 1.0

        # we add gap_p to the start and subtract from the end
        start = origin + dist_s + (gap_p * s_fac)
        end = origin + (e_f * track_l) - (gap_p * e_fac)

        return start, end

    def render_discts_wave(self):
        act_bars = self._discts_animator.bars(self._time)
        inact_bars = self.compute_inactive_segments(act_bars)
        ctx = self._fctx
        center = ctx["center"]
        inv = ctx["inv"]

        # active
        pool = self.refresh_lines(self._active_line_objs)
        for s_f, e_f in act_bars:
            s, e = self.get_segment_coords(s_f, e_f)
            if e < s:
                continue
            pool.pop(0).points = self.w_seg(s, e)

        # inactive
        pool = self.refresh_lines(self._inactive_line_objs)
        for s_f, e_f in inact_bars:
            s, e = self.get_segment_coords(s_f, e_f)
            if e < s:
                continue
            pool.pop(0).points = [
                [s, center][::inv],
                [e, center][::inv],
            ]

    def render_cont_wave(self):
        act_bars = self._cont_animator.bars(self._time)
        ctx = self._fctx
        center = ctx["center"]
        inv = ctx["inv"]

        # active
        pool = self.refresh_lines(
            self._inactive_line_objs + self._active_line_objs
        )
        for s_f, e_f, c_i in act_bars:
            s, e = self.get_segment_coords(s_f, e_f)
            if e < s:
                continue

            line = pool.pop(0)
            line.points = [
                [s, center][::inv],
                [e, center][::inv],
            ]
            self.color_obj(line.group).rgba = self.color_array[c_i]

    def render_indeterminate_wave(self):
        if self.indeterminate_animator == "discontinuous":
            return self.render_discts_wave()
        else:
            # contiguous
            return self.render_cont_wave()


class MDExCircularProgressIndicator(MDExBaseProgressBar):
    """
    Implementation of the circular progress indicator.

    For more information, see in the
    :class:`~kivymd.uix.exprogressindicator.MDExBaseProgressBar` and
    classes documentation.
    """

    # retreat, advanced
    indeterminate_animator = StringProperty("retreat")
    """
    Name of the indeterminate animator to use for circular mode.
    Available options are: `'advanced'`, `'retreat'`.

    :attr:`indeterminate_animator` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    `'retreat'`.
    """
    use_color_array = BooleanProperty(False)
    """
    Whether to use :attr:`color_array` for circular active track colors.

    :attr:`use_color_array` is an
    :class:`~kivy.properties.BooleanProperty` and defaults to `True`.
    """

    _retreat_animator = None
    _advanced_animator = None
    _ctx_deps = [
        "center",
        "spacing",
        "thickness",
        # as we want stuff in angular form
        "wave_length",
        "wave_speed",
    ]

    def _start(self, *args):
        super()._start(*args)
        self._retreat_animator = CircularIndeterminateRetreatAnimator()
        self._retreat_animator.len_palette = 3
        self._advanced_animator = CircularIndeterminateAdvancedAnimator()
        self._advanced_animator.len_palette = 3

    def on_color_array(self, instance, value):
        self._retreat_animator.len_palette = len(value)
        self._advanced_animator.len_palette = len(value)

    def save_frame_context(self, *args):
        # step size for rendering
        # currently set to maximum quality
        step = 1 / self.width

        # radius of the circle
        thickness = self.thickness
        radius = (self.width - thickness) / 2

        # angular wave lenght
        if self.wave_length > 0:
            mode_number = 2 * (math.pi * radius) / self.wave_length
        else:
            # technically at zero should be infinity!
            mode_number = 0

        # angluar wave speed
        ang_wave_speed = (2 * math.pi * self.wave_speed) / radius
        # spacing in degree
        spacing = (self.spacing + thickness + dp(1)) / radius

        self._fctx = {
            "radius": radius,
            "mode_number": mode_number,
            "ang_wave_speed": ang_wave_speed,
            "spacing": spacing,
            "step": step,
            "cx": self.center_x,
            "cy": self.center_y,
        }

    def w_seg(self, start, end) -> list:
        ctx = self._fctx
        _sin, _cos = math.sin, math.cos

        if self.determinate:
            amplitude = self.get_amplitude(
                self.amplitude, self.value_normalized
            )
            ang_wave_speed = ctx["ang_wave_speed"]
        else:
            amplitude = self.amplitude
            ang_wave_speed = 0

        num_steps = int((end - start) / ctx["step"]) + 1

        return [
            coord
            for i in range(num_steps)
            for pt in [start + i * ctx["step"]]
            for r in [
                ctx["radius"]
                + amplitude
                * _sin(ctx["mode_number"] * pt - ang_wave_speed * self._time)
            ]
            for coord in (ctx["cx"] + r * _sin(pt), ctx["cy"] + r * _cos(pt))
        ]

    def get_arc_points(self, start_rad, end_rad) -> list:
        ctx = self._fctx
        num_steps = int((end_rad - start_rad) / ctx["step"]) + 1
        cx, cy, r = ctx["cx"], ctx["cy"], ctx["radius"]
        _sin, _cos = math.sin, math.cos
        return [
            coord
            for i in range(num_steps)
            for pt in [start_rad + i * ctx["step"]]
            for coord in (cx + r * _sin(pt), cy + r * _cos(pt))
        ]

    def get_start_and_end(self, init_rad, s_f, e_f):
        full_angle = 2 * math.pi
        s = init_rad + (s_f * full_angle)
        e = init_rad + (e_f * full_angle)
        return s, e

    def render_retreat_wave(self):
        ctx = self._fctx
        rot_rad, (s_f, e_f, c_idx) = self._retreat_animator.bars(self._time)
        a_s, a_e = self.get_start_and_end(rot_rad, s_f, e_f)
        spacing = ctx["spacing"]

        # active line
        self._active_line_objs[0].points = self.w_seg(a_s, a_e)

        # active line color
        color = self.color_obj(self._active_line_objs[0].group)
        if self.use_color_array:
            color.rgba = self.color_array[c_idx]
        else:
            color.rgba = self.active_track_color

        # inactive line
        i_s = a_e + spacing
        i_e = a_s + (2 * math.pi) - spacing
        if i_e - i_s <= 0:
            i_e = i_s
        self._inactive_line_objs[0].points = self.get_arc_points(i_s, i_e)

    def render_indeterminate_wave(self):
        if self.indeterminate_animator == "retreat":
            return self.render_retreat_wave()
        else:
            return self.render_advanced_wave()

    def render_advanced_wave(self):
        ctx = self._fctx
        rot_rad, (s_f, e_f, color_data) = self._advanced_animator.bars(
            self._time
        )
        a_s, a_e = self.get_start_and_end(rot_rad, s_f, e_f)
        spacing = ctx["spacing"]

        # active line
        self._active_line_objs[0].points = self.w_seg(a_s, a_e)

        # active line color
        color = self.color_obj(self._active_line_objs[0].group)
        if self.use_color_array:
            idx_from, idx_to, mix = color_data
            c1 = self.color_array[idx_from]
            c2 = self.color_array[idx_to]
            # linear mixing
            mixed_color = [c1[i] + (c2[i] - c1[i]) * mix for i in range(4)]
            color.rgba = mixed_color
        else:
            color.rgba = self.active_track_color

        # inacitve line
        i_s = a_e + spacing
        i_e = a_s + (2 * math.pi) - spacing
        self._inactive_line_objs[0].points = self.get_arc_points(i_s, i_e)

    def render_determinate_wave(self):
        ctx = self._fctx
        spacing = ctx["spacing"]
        a_s, a_e = self.get_start_and_end(0, 0, self.value_normalized)

        # persistant inital dot
        a_e = max(math.radians(2), a_e)
        # active line
        self._active_line_objs[0].points = self.w_seg(a_s, a_e)

        # inactive line
        i_s = a_e + spacing
        i_e = (2 * math.pi) - spacing
        self._inactive_line_objs[0].points = self.get_arc_points(i_s, i_e)
