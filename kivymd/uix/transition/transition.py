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

from kivy import Logger
from kivy.animation import Animation, AnimationTransition
from kivy.properties import DictProperty
from kivy.uix.screenmanager import (
    ScreenManagerException,
    SlideTransition,
    SwapTransition,
    TransitionBase,
)

from kivymd.uix.hero import MDHeroFrom, MDHeroTo
from kivymd.uix.screenmanager import MDScreenManager


class MDTransitionBase(TransitionBase):
    """
    TransitionBase is used to animate 2 screens within the
    :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    For more
    information, see in the :class:`~kivy.uix.screenmanager.TransitionBase`
    class documentation.
    """

    _direction = "in"
    # Collection of child widgets of all 'MDHeroFrom' widgets that are
    # on the screen, for example:
    #
    #     MDScreen:
    #
    #         MDHeroFrom:
    #             tag: "kivymd"
    #
    #             FitImage:
    #
    #         MDHeroFrom:
    #             tag: "kivy"
    #
    #             FitImage:
    #
    # {
    #     'kivy':   <kivymd.uix.fitimage.fitimage.FitImage object>,
    #     'kivymd': <kivymd.uix.fitimage.fitimage.FitImage object>,
    # }
    _hero_from_widget_children = DictProperty()

    def start(self, instance_screen_manager: MDScreenManager) -> None:
        super().start(instance_screen_manager)

        {"in": self.animated_hero_in, "out": self.animated_hero_out}[
            self._direction
        ]()

    def animated_hero_in(self) -> None:
        """Animates the flight of heroes from screen **A** to screen **B**."""

        if self.manager._heroes_data and self.manager.current_heroes:
            for hero_from_widget in self.manager.get_hero_from_widget():
                for heroes_tag in self.manager.current_heroes:
                    if heroes_tag == hero_from_widget.tag:
                        self._check_widget_properties(hero_from_widget)

                        # Get child widget of the 'MDHeroFrom' container.
                        hero_widget = hero_from_widget.children[0]
                        self._hero_from_widget_children[
                            hero_from_widget.tag
                        ] = hero_widget

                        # Removing the child widget from the 'MDHeroFrom'
                        # container.
                        hero_from_widget.remove_widget(hero_widget)

                        # We set the size, position of the child widget of the
                        # 'MDHeroFrom' container and add this widget to the
                        # root window.
                        hero_widget.pos = self.screen_out.to_widget(
                            *hero_from_widget.to_window(*hero_from_widget.pos)
                        )
                        hero_widget.size = hero_from_widget.size
                        self.manager.get_root_window().add_widget(hero_widget)

                        # Animating widgets added to the root window.
                        if self.screen_in.heroes_to:
                            for hero_to_widget in self.screen_in.heroes_to:
                                self._check_hero_to_widget_tag(
                                    hero_to_widget, hero_from_widget
                                )
                                if hero_to_widget.tag == heroes_tag:
                                    Animation(
                                        size=hero_to_widget.size,
                                        d=self.duration,
                                        pos=hero_to_widget.pos,
                                    ).start(hero_widget)
                                    hero_from_widget.dispatch(
                                        "on_transform_in",
                                        hero_widget,
                                        self.duration,
                                    )

    def animated_hero_out(self) -> None:
        """Animates the flight of heroes from screen **B** to screen **A**."""

        if (
            self.manager._heroes_data
            and self.manager.current_heroes
            and self.screen_out.heroes_to
        ):
            for heroes_tag in self.manager.current_heroes:
                for hero_to_widget in self.screen_out.heroes_to:
                    if hero_to_widget.tag == heroes_tag:
                        hero_from_children = self._hero_from_widget_children[
                            heroes_tag
                        ]
                        hero_to_widget.remove_widget(hero_from_children)
                        self.manager.get_root_window().add_widget(
                            hero_from_children
                        )

                        for (
                            hero_from_widget
                        ) in self.manager.get_hero_from_widget():
                            hero_from_widget.dispatch(
                                "on_transform_out",
                                self._hero_from_widget_children[
                                    hero_from_widget.tag
                                ],
                                self.duration,
                            )
                            Animation(
                                pos=self.screen_in.to_widget(
                                    *hero_from_widget.to_window(
                                        *hero_from_widget.pos
                                    )
                                ),
                                size=hero_from_widget.size,
                                d=self.duration,
                            ).start(
                                self._hero_from_widget_children[
                                    hero_from_widget.tag
                                ]
                            )

    def on_complete(self) -> None:
        """
        Override method.
        See :attr:`kivy.uix.screenmanager.TransitionBase.on_complete'.
        """

        super().on_complete()

        if self.manager._heroes_data and self.manager.current_heroes:
            for hero_from_widget in self.manager.get_hero_from_widget():
                for heroes_tag in self.manager.current_heroes:
                    if heroes_tag == hero_from_widget.tag:
                        hero_from_children = self._hero_from_widget_children[
                            heroes_tag
                        ]
                        self.manager.get_root_window().remove_widget(
                            hero_from_children
                        )

                        # Adding a child widget from the 'MDHeraFrom' container
                        # to the 'MDHeroTo' container.
                        if self._direction == "in":
                            for hero_to_widget in self.screen_in.heroes_to:
                                if hero_to_widget.tag == heroes_tag:
                                    hero_to_widget.add_widget(
                                        hero_from_children
                                    )
                        # Restores the child widget for the 'MDHeraFrom'
                        # container.
                        elif self._direction == "out":
                            hero_from_widget.add_widget(hero_from_children)

        if self._direction == "out":
            self._direction = "in"
        else:
            self._direction = "out"

    # Checks the attributes for the 'self.screen_in' screen.
    # Called from the animated_hero_in method.
    def _check_widget_properties(self, hero_from_widget: MDHeroFrom):
        if not self.screen_in.heroes_to:
            raise Exception(
                f"The `heroes_to` attribute is not specified for screen "
                f"{self.screen_in}"
            )
        # The 'MDHeroFrom' widget allows you to place only one widget in
        # itself.
        if len(hero_from_widget.children) > 1:
            raise Exception(
                f"{hero_from_widget.__class__} accept only one widget"
            )

    # For new API support.
    def _check_hero_to_widget_tag(
        self, hero_to_widget: MDHeroTo, hero_from_widget: MDHeroFrom
    ) -> None:
        if not hero_to_widget.tag:
            Logger.warning(
                "KivyMD: "
                f"Set the tag '{hero_from_widget.tag}' "
                f"for the {hero_to_widget} widget to the same "
                f"as for the {hero_from_widget} widget"
            )
            hero_to_widget.tag = hero_from_widget.tag


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
