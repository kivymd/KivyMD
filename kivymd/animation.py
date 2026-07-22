"""
Components/Animation
====================

.. versionadded:: 2.0.0

Adds new transitions to the :class:`~kivy.animation.AnimationTransition` class:

- "easing_standard"
- "easing_decelerated"
- "easing_accelerated"
- "easing_linear"

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.animation import Animation
            from kivy.uix.boxlayout import BoxLayout
            from kivy.clock import Clock
            from kivy.metrics import dp
            from kivy.properties import ListProperty

            from kivymd.app import MDApp


            class AnimBox(BoxLayout):
                obj_pos = ListProperty([0, 0])


            UI = '''
            <AnimBox>:
                transition: "in_out_bounce"
                size_hint_y: None
                height: dp(100)
                obj_pos: [dp(40), self.pos[-1] + dp(40)]

                canvas:
                    Color:
                        rgba: app.theme_cls.primaryContainerColor
                    Rectangle:
                        size: [self.size[0], dp(5)]
                        pos: self.pos[0], self.pos[-1] + dp(50)
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        size: [dp(30)] * 2
                        pos: root.obj_pos

                MDLabel:
                    adaptive_height: True
                    text: root.transition
                    padding: [dp(10), 0]
                    halign: "center"

            MDGridLayout:
                orientation: "lr-tb"
                cols: 1
                md_bg_color: app.theme_cls.backgroundColor
                spacing: dp(10)
            '''


            class MotionApp(MDApp):
                def build(self):
                    return Builder.load_string(UI)

                def on_start(self):
                    for transition in [
                        "easing_linear",
                        "easing_accelerated",
                        "easing_decelerated",
                        "easing_standard",
                        "in_out_cubic"
                    ]: # add more here for comparison
                        print(transition)
                        widget = AnimBox()
                        widget.transition = transition
                        self.root.add_widget(widget)

                    Clock.schedule_once(self.run_animation, 1)

                _inverse = True

                def run_animation(self, dt):
                    x = (self.root.children[0].width - dp(30)) if self._inverse else 0

                    for widget in self.root.children:
                        Animation(
                            obj_pos=[x, widget.obj_pos[-1]], t=widget.transition, d=3
                        ).start(widget)

                    self._inverse = not self._inverse
                    Clock.schedule_once(self.run_animation, 3.1)

            MotionApp().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.core.window import Window
            from kivy.graphics import Color, Rectangle
            from kivy.animation import Animation
            from kivy.clock import Clock
            from kivy.metrics import dp
            from kivy.properties import ListProperty

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.gridlayout import MDGridLayout
            from kivymd.uix.label import MDLabel


            class AnimBox(MDBoxLayout):
                obj_pos = ListProperty([0, 0])

                def __init__(self, **kwargs):
                    super().__init__(**kwargs)

                    self.transition = "in_out_bounce"
                    self.size_hint_y = None
                    self.height = dp(100)

                    self.label = MDLabel(
                        adaptive_height=True,
                        text=self.transition,
                        padding=[dp(10), 0],
                        halign="center",
                    )
                    self.add_widget(self.label)

                    with self.canvas:
                        Color(rgba=self.theme_cls.primaryContainerColor)
                        self.background_rect = Rectangle(
                            size=(self.width, dp(5)),
                            pos=(self.x, self.y + dp(50)),
                        )

                        Color(rgba=self.theme_cls.primaryColor)
                        self.obj_rect = Rectangle(
                            size=(dp(30), dp(30)),
                            pos=(dp(40), self.y + dp(40)),
                        )

                    self.bind(
                        pos=self.update_position,
                        size=self.update_canvas,
                        y=self.update_canvas,
                        obj_pos=self.update_obj_rect,
                    )

                    Clock.schedule_once(self.set_initial_pos)

                def set_initial_pos(self, dt):
                    self.obj_pos = [
                        dp(40),
                        self.y + dp(40),
                    ]

                def update_position(self, *args):
                    self.obj_pos = [
                        self.obj_pos[0],
                        self.y + dp(40),
                    ]

                def update_canvas(self, *args):
                    self.background_rect.size = (
                        self.width,
                        dp(5),
                    )

                    self.background_rect.pos = (
                        self.x,
                        self.center_y,
                    )

                def update_obj_rect(self, *args):
                    self.obj_rect.pos = self.obj_pos


            class MotionApp(MDApp):
                def build(self):
                    layout = MDGridLayout(
                        orientation="lr-tb",
                        cols=1,
                        md_bg_color=self.theme_cls.backgroundColor,
                        spacing=dp(10),
                    )
                    Window.bind(size=layout.do_layout)

                    return layout

                def on_start(self):
                    for transition in [
                        "easing_linear",
                        "easing_accelerated",
                        "easing_decelerated",
                        "easing_standard",
                        "in_out_cubic",
                    ]:
                        widget = AnimBox()
                        widget.transition = transition
                        widget.label.text = transition
                        self.root.add_widget(widget)

                    Clock.schedule_once(self.run_animation, 1)

                _inverse = True

                def run_animation(self, dt):
                    for widget in self.root.children:
                        x = widget.width - dp(30) if self._inverse else 0
                        Animation(
                            obj_pos=[
                                x,
                                widget.y + dp(40),
                            ],
                            t=widget.transition,
                            d=3,
                        ).start(widget)

                    self._inverse = not self._inverse

                    Clock.schedule_once(self.run_animation, 3.1)


            MotionApp().run()

.. image:: https://github.com/kivymd/KivyMD/assets/68729523/21c847b0-284a-4796-b704-e4a2531fbb1b
    :align: center
"""

import kivy.animation

from kivymd.utils.cubic_bezier import CubicBezier


class MDAnimationTransition(kivy.animation.AnimationTransition):
    """KivyMD's equivalent of kivy's `AnimationTransition`."""

    easing_standard = CubicBezier(0.4, 0.0, 0.2, 1.0).t
    """
    Material Design standard easing transition.

    :data:`easing_standard` is a :class:`~typing.Callable` and defaults to
    ``CubicBezier(0.4, 0.0, 0.2, 1.0).t``.
    """

    easing_decelerated = CubicBezier(0.0, 0.0, 0.2, 1.0).t
    """
    Material Design standard easing transition.

    :data:`easing_decelerated` is a :class:`~typing.Callable` and defaults to
    ``CubicBezier(0.0, 0.0, 0.2, 1.0).t``.
    """

    easing_accelerated = CubicBezier(0.4, 0.0, 1.0, 1.0).t
    """
    Material Design standard easing transition.

    :data:`easing_accelerated` is a :class:`~typing.Callable` and defaults to
    ``CubicBezier(0.4, 0.0, 1.0, 1.0).t``.
    """

    easing_linear = CubicBezier(0.0, 0.0, 1.0, 1.0).t
    """
    Material Design standard easing transition.

    :data:`easing_linear` is a :class:`~typing.Callable` and defaults to
    ``CubicBezier(0.0, 0.0, 1.0, 1.0).t``.
    """

    # Equivalent to path(
    #     M 0,0 C 0.05,
    #     0,
    #     0.133333,
    #     0.06,
    #     0.166666,
    #     0.4 C 0.208333,
    #     0.82,
    #     0.25,
    #     1,
    #     1,
    #     1
    # )
    def easing_emphasized(t: float):
        """
        Material Design emphasized easing transition.

        :param t:
            Animation progress in the range ``0`` to ``1``.
        :returns:
            Interpolated animation progress.
        """

        if t < 0.4:
            # Normalize t: maps [0, 0.4] to [0, 1].
            t_norm = t / 0.4
            # First segment: (0.05, 0) to (0.1333, 0.06).
            return CubicBezier(0.05, 0, 0.133333, 0.06).t(t_norm) * 0.4
        else:
            # Normalize t: maps [0.4, 1.0] to [0, 1].
            t_norm = (t - 0.4) / 0.6
            # Second segment: (0.2083, 0.82) to (0.25, 1).
            # We start at 0.4 (the end of the last segment) and move toward 1.0.
            return 0.4 + CubicBezier(0.208333, 0.82, 0.25, 1).t(t_norm) * 0.6


# Monkey patch kivy's animation module.
kivy.animation.AnimationTransition = MDAnimationTransition
