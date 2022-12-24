"""
Components/Spinner
==================

.. seealso::

    `Material Design spec, Menus <https://material.io/components/progress-indicators#circular-progress-indicators>`_

.. rubric:: Circular progress indicator in Google's Material Design.

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDSpinner:
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .5}
            active: True if check.active else False

        MDCheckbox:
            id: check
            size_hint: None, None
            size: dp(48), dp(48)
            pos_hint: {'center_x': .5, 'center_y': .4}
            active: True
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/spinner.gif
    :align: center

Spinner palette
---------------

.. code-block:: kv

    MDSpinner:
        # The number of color values ​​can be any.
        palette:
            [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1], \
            [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1], \
            [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1], \
            [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],

.. code-block:: python

    MDSpinner(
        size_hint=(None, None),
        size=(dp(46), dp(46)),
        pos_hint={'center_x': .5, 'center_y': .5},
        active=True,
        palette=[
            [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
            [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
            [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
            [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
        ]
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/spinner-palette.gif
    :align: center

Determinate mode
----------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDSpinner:
            size_hint: None, None
            size: dp(48), dp(48)
            pos_hint: {'center_x': .5, 'center_y': .5}
            determinate: True
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/spinner-determinate.gif
    :align: center
"""

__all__ = ("MDSpinner",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
)
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "spinner", "spinner.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSpinner(ThemableBehavior, Widget):
    """
    :class:`MDSpinner` is an implementation of the circular progress
    indicator in `Google's Material Design`.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.widget.Widget` classes documentation.

    It can be used either as an indeterminate indicator that loops while
    the user waits for something to happen, or as a determinate indicator.

    Set :attr:`determinate` to **True** to activate determinate mode, and
    :attr:`determinate_time` to set the duration of the animation.

    :Events:
        `on_determinate_complete`
            The event is called at the end of the spinner loop in the
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
    Progress line width of spinner.

    :attr:`line_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(2.25)`.
    """

    active = BooleanProperty(True)
    """
    Use :attr:`active` to start or stop the spinner.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    color = ColorProperty(None, allownone=True)
    """
    Spinner color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    palette = ListProperty()
    """
    A set of colors. Changes with each completed spinner cycle.

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
        if not self.color:
            self.color = self.theme_cls.primary_color
        if self.color == self.theme_cls.primary_color:
            self.theme_cls.bind(primary_color=self._update_color)

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

    def on_palette(self, instance_spinner, palette_list: list) -> None:
        self._palette = iter(palette_list)

    def on_active(self, instance_spinner, active_value: bool) -> None:
        self._reset()
        if self.active:
            self.check_determinate()

    def on_determinate_complete(self, *args):
        """
        The event is called at the end of the spinner loop in the
        `determinate = True` mode.
        """

    def check_determinate(self, interval: Union[float, int] = 0) -> None:
        if self.active:
            if self.determinate:
                self._start_determinate()
            else:
                self._start_loop()

    def _update_color(self, *args):
        self.color = self.theme_cls.primary_color

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

    def _on_determinate_progress(
        self, instance_animation, instance_spinner, value
    ):
        if value == 1:
            self.dispatch("on_determinate_complete")
