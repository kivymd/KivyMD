"""
Components/Transition
=====================

.. rubric::
    A set of classes for implementing transitions between application screens.

.. versionadded:: 1.0.0

Changing transitions
--------------------

You have multiple transitions available by default, such as:

- :class:`MDFadeSlideTransition`
    state one: the new screen closes the previous screen by lifting from the
    bottom of the screen and changing from transparent to non-transparent;

    state two: the current screen goes down to the bottom of the screen,
    passing from a non-transparent state to a transparent one, thus opening the
    previous screen;

.. note::
    You cannot control the direction of a slide using the direction attribute.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/transition-md-fade-slide-transition.gif
    :align: center

"""

__all__ = ("MDFadeSlideTransition",)

from typing import NoReturn

from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import (
    ScreenManager,
    ScreenManagerException,
    SlideTransition,
)


class MDFadeSlideTransition(SlideTransition):
    _direction = "up"

    def start(self, instance_screen_manager: ScreenManager) -> NoReturn:
        """
        Starts the transition. This is automatically called by the
        :class:`ScreenManager`.
        """

        if self.is_active:
            raise ScreenManagerException("start() is called twice!")

        self.manager = instance_screen_manager
        self._anim = Animation(d=self.duration, s=0)
        self._anim.bind(
            on_progress=self._on_progress, on_complete=self._on_complete
        )
        if self._direction == "up":
            self.add_screen(self.screen_in)
        else:
            self.add_screen(self.screen_in)
            self.add_screen(self.screen_out)
        self.screen_in.transition_progress = 0.0
        self.screen_in.transition_state = "in"
        self.screen_out.transition_progress = 0.0
        self.screen_out.transition_state = "out"
        self.screen_in.dispatch("on_pre_enter")
        self.screen_out.dispatch("on_pre_leave")

        self.is_active = True
        self._anim.start(self)
        self.dispatch("on_progress", 0)
        if self._direction == "up":
            self.screen_in.y = 0
            self.screen_in.opacity = 0

    def on_progress(self, progression: float) -> NoReturn:
        progression = AnimationTransition.out_quad(progression)

        if self._direction == "up":
            self.screen_in.y = (
                self.manager.y + self.manager.height * progression
            ) - self.screen_in.height
            self.screen_in.opacity = progression
        if self._direction == "down":
            self.screen_out.y = (
                self.manager.y - self.manager.height * progression
            )
            self.screen_out.opacity = 1 - progression

    def on_complete(self) -> NoReturn:
        if self._direction == "down":
            self._direction = "up"
        else:
            self._direction = "down"
        super().on_complete()
