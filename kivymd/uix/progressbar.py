"""
Components/Progress Bar
=======================

.. seealso::

    `Material Design spec, Progress indicators <https://material.io/components/progress-indicators>`_

.. rubric:: Progress indicators express an unspecified wait time or display
    the length of a process.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar-preview.png
    :align: center

`KivyMD` provides the following bars classes for use:

- MDProgressBar_
- Determinate_
- Indeterminate_

.. MDProgressBar:
MDProgressBar
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    BoxLayout:
        padding: "10dp"

        MDProgressBar:
            value: 50
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar.png
    :align: center

Vertical orientation
--------------------

.. code-block:: kv

    MDProgressBar:
        orientation: "vertical"
        value: 50

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar-vertical.png
    :align: center

With custom color
-----------------

.. code-block:: kv

    MDProgressBar:
        value: 50
        color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar-custom-color.png
    :align: center

.. Indeterminate:
Indeterminate
-------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp

    KV = '''
    Screen:

        MDProgressBar:
            id: progress
            pos_hint: {"center_y": .6}
            type: "indeterminate"

        MDRaisedButton:
            text: "STOP" if app.state == "start" else "START"
            pos_hint: {"center_x": .5, "center_y": .45}
            on_press: app.state = "stop" if app.state == "start" else "start"
    '''


    class Test(MDApp):
        state = StringProperty("stop")

        def build(self):
            return Builder.load_string(KV)

        def on_state(self, instance, value):
            {
                "start": self.root.ids.progress.start,
                "stop": self.root.ids.progress.stop,
            }.get(value)()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/indeterminate-progress-bar.gif
    :align: center

.. Determinate:
Determinate
-----------

.. code-block:: kv

    MDProgressBar:
        type: "determinate"
        running_duration: 1
        catching_duration: 1.5

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/determinate-progress-bar.gif
    :align: center
"""

__all__ = ("MDProgressBar",)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.progressbar import ProgressBar

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<MDProgressBar>
    canvas:
        Clear
        Color:
            rgba: self.theme_cls.divider_color
        Rectangle:
            size:
                (self.width, dp(4)) \
                if self.orientation == "horizontal" \
                else (dp(4), self.height)
            pos:
                (self.x, self.center_y - dp(4)) \
                if self.orientation == "horizontal" \
                else (self.center_x - dp(4),self.y)
        Color:
            rgba:
                self.theme_cls.primary_color if not self.color else self.color
        Rectangle:
            size:
                (self.width * self.value_normalized, sp(4)) \
                if self.orientation == "horizontal" \
                else (sp(4), self.height * self.value_normalized)
            pos:
                (self.width * (1 - self.value_normalized) + self.x \
                if self.reversed else self.x + self._x, self.center_y - dp(4)) \
                if self.orientation == "horizontal" \
                else (self.center_x - dp(4),self.height \
                * (1 - self.value_normalized) + self.y if self.reversed \
                else self.y)
"""
)


class MDProgressBar(ThemableBehavior, ProgressBar):
    reversed = BooleanProperty(False)
    """Reverse the direction the progressbar moves.

    :attr:`reversed` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    orientation = OptionProperty(
        "horizontal", options=["horizontal", "vertical"]
    )
    """Orientation of progressbar. Available options are: `'horizontal '`,
    `'vertical'`.

    :attr:`orientation` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'horizontal'`.
    """

    color = ColorProperty(None)
    """
    Progress bar color in ``rgba`` format.

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    running_transition = StringProperty("in_cubic")
    """Running transition.

    :attr:`running_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'in_cubic'`.
    """

    catching_transition = StringProperty("out_quart")
    """Catching transition.

    :attr:`catching_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quart'`.
    """

    running_duration = NumericProperty(0.5)
    """Running duration.

    :attr:`running_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.5`.
    """

    catching_duration = NumericProperty(0.8)
    """Catching duration.

    :attr:`running_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    type = OptionProperty(
        None, options=["indeterminate", "determinate"], allownone=True
    )
    """Type of progressbar. Available options are: `'indeterminate '`,
    `'determinate'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    _x = NumericProperty(0)

    def __init__(self, **kwargs):
        self.catching_anim = None
        self.running_anim = None
        super().__init__(**kwargs)

    def start(self):
        """Start animation."""

        if self.type in ("indeterminate", "determinate"):
            Clock.schedule_once(self._set_default_value)
            if not self.catching_anim and not self.running_anim:
                if self.type == "indeterminate":
                    self._create_indeterminate_animations()
                else:
                    self._create_determinate_animations()
            self.running_away()

    def stop(self):
        """Stop animation."""

        Animation.cancel_all(self)
        self._set_default_value(0)

    def running_away(self, *args):
        self._set_default_value(0)
        self.running_anim.start(self)

    def catching_up(self, *args):
        if self.type == "indeterminate":
            self.reversed = True
        self.catching_anim.start(self)

    def _create_determinate_animations(self):
        self.running_anim = Animation(
            value=100,
            opacity=1,
            t=self.running_transition,
            d=self.running_duration,
        )
        self.running_anim.bind(on_complete=self.catching_up)
        self.catching_anim = Animation(
            opacity=0,
            t=self.catching_transition,
            d=self.catching_duration,
        )
        self.catching_anim.bind(on_complete=self.running_away)

    def _create_indeterminate_animations(self):
        self.running_anim = Animation(
            _x=self.width / 2,
            value=50,
            t=self.running_transition,
            d=self.running_duration,
        )
        self.running_anim.bind(on_complete=self.catching_up)
        self.catching_anim = Animation(
            value=0, t=self.catching_transition, d=self.catching_duration
        )
        self.catching_anim.bind(on_complete=self.running_away)

    def _set_default_value(self, interval):
        self._x = 0
        self.value = 0
        self.reversed = False
