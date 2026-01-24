"""
Animation
=========

.. versionadded:: 2.0.0

Adds new transitions to the :class:`~kivy.animation.AnimationTransition` class:
- "easing_standard"
- "easing_decelerated"
- "easing_accelerated"
- "easing_linear"


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
        transition:"in_out_bounce"
        size_hint_y:None
        height:dp(100)
        obj_pos:[dp(40), self.pos[-1] + dp(40)]
        canvas:
            Color:
                rgba:app.theme_cls.primaryContainerColor
            Rectangle:
                size:[self.size[0], dp(5)]
                pos:self.pos[0], self.pos[-1] + dp(50)
            Color:
                rgba:app.theme_cls.primaryColor
            Rectangle:
                size:[dp(30)] * 2
                pos:root.obj_pos
        MDLabel:
            adaptive_height:True
            text:root.transition
            padding:[dp(10), 0]
            halign:"center"

    MDGridLayout:
        orientation:"lr-tb"
        cols:1
        md_bg_color:app.theme_cls.backgroundColor
        spacing:dp(10)
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
            ]: # Add more here for comparison
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

.. image:: https://github.com/kivymd/KivyMD/assets/68729523/21c847b0-284a-4796-b704-e4a2531fbb1b
    :align: center
"""

import kivy.animation

from kivymd.utils.cubic_bezier import CubicBezier
import time


class MDAnimationTransition(kivy.animation.AnimationTransition):
    """KivyMD's equivalent of kivy's `AnimationTransition`"""

    easing_standard = CubicBezier(0.4, 0.0, 0.2, 1.0).t
    easing_decelerated = CubicBezier(0.0, 0.0, 0.2, 1.0).t
    easing_accelerated = CubicBezier(0.4, 0.0, 1.0, 1.0).t
    easing_linear = CubicBezier(0.0, 0.0, 1.0, 1.0).t

    # equivalent to
    # path(M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1)
    def easing_emphasized(t: float):
        if t < 0.4:
            # Normalize t: maps [0, 0.4] to [0, 1]
            t_norm = t / 0.4
            # First segment: (0.05, 0) to (0.1333, 0.06)
            return CubicBezier(0.05, 0, 0.133333, 0.06).t(t_norm) * 0.4
        else:
            # Normalize t: maps [0.4, 1.0] to [0, 1]
            t_norm = (t - 0.4) / 0.6
            # Second segment: (0.2083, 0.82) to (0.25, 1)
            # We start at 0.4 (the end of the last segment) and move toward 1.0
            return 0.4 + CubicBezier(0.208333, 0.82, 0.25, 1).t(t_norm) * 0.6


# Monkey patch kivy's animation module
kivy.animation.AnimationTransition = MDAnimationTransition
