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

__all__ = (
    "MDFadeSlideTransition",
    "MDSlideTransition",
    "MDSwapTransition",
    "MDTransitionBase",
)

from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import (
    ScreenManagerException,
    SlideTransition,
    SwapTransition,
    TransitionBase,
)

from kivymd.uix.screenmanager import MDScreenManager


class MDTransitionBase(TransitionBase):
    _direction = "in"
    hero_widget = None
    hero_from_widget = None  # kivymd.uix.hero.MDHeroFrom object

    def start(self, instance_screen_manager: MDScreenManager) -> None:
        super().start(instance_screen_manager)

        {"in": self.animated_hero_in, "out": self.animated_hero_out}[
            self._direction
        ]()

    def animated_hero_in(self) -> None:
        if self.manager._heroes_data and self.manager.current_hero:
            self.hero_from_widget = self.manager.get_hero_from_widget()
            self._check_widget_properties()
            self.hero_widget = self.hero_from_widget.children[0]
            self.hero_from_widget.remove_widget(self.hero_widget)

            self.hero_widget.pos = self.screen_out.to_widget(
                *self.hero_from_widget.to_window(*self.hero_from_widget.pos)
            )
            self.hero_widget.size = self.hero_from_widget.size
            self.manager.get_root_window().add_widget(self.hero_widget)

            Animation(
                size=self.screen_in.hero_to.size,
                d=self.duration,
                pos=self.screen_in.hero_to.pos,
            ).start(self.hero_widget)
            self.hero_from_widget.dispatch(
                "on_transform_in", self.hero_widget, self.duration
            )

    def animated_hero_out(self) -> None:
        if self.manager._heroes_data and self.manager.current_hero:
            self.screen_out.hero_to.remove_widget(self.hero_widget)
            self.manager.get_root_window().add_widget(self.hero_widget)

            self.hero_from_widget.dispatch(
                "on_transform_out", self.hero_widget, self.duration
            )
            Animation(
                pos=self.screen_in.to_widget(
                    *self.hero_from_widget.to_window(*self.hero_from_widget.pos)
                ),
                size=self.hero_from_widget.size,
                d=self.duration,
            ).start(self.hero_widget)

    def on_complete(self) -> None:
        super().on_complete()

        if self._direction == "out":
            self._direction = "in"
            if self.manager._heroes_data and self.manager.current_hero:
                self.manager.get_root_window().remove_widget(self.hero_widget)
                self.hero_from_widget.add_widget(self.hero_widget)
        else:
            self._direction = "out"
            if self.manager._heroes_data and self.manager.current_hero:
                self.manager.get_root_window().remove_widget(self.hero_widget)
                self.screen_in.hero_to.add_widget(self.hero_widget)

    def _check_widget_properties(self):
        if not self.screen_in.hero_to:
            raise Exception(
                f"The `hero_to` attribute is not specified for screen {self.screen_in}"
            )
        if len(self.hero_from_widget.children) > 1:
            raise Exception(
                f"{self.hero_from_widget.__class__} accept only one widget"
            )


class MDSwapTransition(SwapTransition, MDTransitionBase):
    pass


class MDSlideTransition(SlideTransition, MDTransitionBase):
    pass


class MDFadeSlideTransition(MDSlideTransition):
    def start(self, instance_screen_manager: MDScreenManager) -> None:
        if self.is_active:
            raise ScreenManagerException("start() is called twice!")

        self.manager = instance_screen_manager
        self._anim = Animation(d=self.duration, s=0)
        self._anim.bind(
            on_progress=self._on_progress, on_complete=self._on_complete
        )

        if self._direction == "in":
            self.add_screen(self.screen_in)
            self.animated_hero_in()
        else:
            self.animated_hero_out()
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

        if self._direction == "in":
            self.screen_in.y = 0
            self.screen_in.opacity = 0

    def on_progress(self, progression: float) -> None:
        progression = AnimationTransition.out_quad(progression)

        if self._direction == "in":
            self.screen_in.y = (
                self.manager.y + self.manager.height * progression
            ) - self.screen_in.height
            self.screen_in.opacity = progression
        if self._direction == "out":
            self.screen_out.y = (
                self.manager.y - self.manager.height * progression
            )
            self.screen_out.opacity = 1 - progression
