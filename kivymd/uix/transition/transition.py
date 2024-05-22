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
    "MDSharedAxisTransition",
)

from kivy import Logger
from kivy.animation import Animation, AnimationTransition
from kivy.properties import (
    DictProperty,
    OptionProperty,
    NumericProperty,
    BooleanProperty,
)
from kivy.uix.screenmanager import (
    ScreenManagerException,
    SlideTransition,
    SwapTransition,
    TransitionBase,
)
from kivy.graphics import PopMatrix, PushMatrix, Scale
from kivy.animation import Animation, AnimationTransition
from kivy.metrics import dp

from kivymd.uix.hero import MDHeroFrom, MDHeroTo
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.animation import MDAnimationTransition


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


class MDSharedAxisTransition(MDTransitionBase):
    """
    Android default screen transition.

    .. versionadded:: 2.0.0
    """

    transition_axis = OptionProperty("x", options=["x", "y", "z"])
    """ 
    Axis of the transition. Available values "x", "y", and "z".
    
    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/transition_axis.gif
        :align: center

    :attr:`transition_axis` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `"x"`.
    """

    duration = NumericProperty(0.15)
    """
    Duration in seconds of the transition. Android recommends these intervals:

    .. list-table:: Android transition values (in seconds)
        :align: left
        :header-rows: 1

        * - Name
          - value
        * - small_1 
          - 0.075
        * - small_2 
          - 0.15
        * - medium_1
          - 0.2
        * - medium_2
          - 0.25
        * - large_1 
          - 0.3
        * - large_2
          - 0.35

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty` and
    defaults to 0.15 (= 150ms).
    """

    switch_animation = OptionProperty(
        "easing_decelerated",
        options=[
            "easing_standard",
            "easing_decelerated",
            "easing_accelerated",
            "easing_linear",
        ],
    )
    """ 
    Custom material design animation transition.
    
    :attr:`switch_animation` is a :class:`~kivy.properties.OptionProperty` and
    defaults to `"easing_decelerated"`.
    """

    slide_distance = NumericProperty(dp(15))
    """
    Distance to which it slides left, right, bottom or up depending on axis.
    
    :attr:`slide_distance` is a :class:`~kivy.properties.NumericProperty` and
    defaults to `dp(15)`.
    """

    opposite = BooleanProperty(False)
    """
    Decides Transition direction.

    :attr:`opposite` is a :class:`~kivy.properties.BooleanProperty` and
    defaults to `False`.
    """

    _s_map = {}  # scale instruction map
    _slide_diff = 0

    def start(self, manager):
        # Transition internal working (for developer only):
        # x:
        #    First half: screen_out opacity 1 ->  0, pos_x: 0 -> - slide distance
        #    Second half: screen_in opacity 0 -> 1, pos_x: slide distance -> 0
        # y:
        #    First half: screen_out opacity 1 ->  0, pos_y: 0 -> - slide distance
        #    Second half: screen_in opacity 0 -> 1, pos_y: slide distance -> 0
        # z:
        #   First half: screen_out opacity 1 -> 0, scale: 1 -> relative subtracted area
        #   Second half: screen_in opacity 0 -> 1, scale: relative subtracted area -> 1

        # Save hash of the objects
        self.ih = hash(self.screen_in)
        self.oh = hash(self.screen_out)

        # Init pos
        self.screen_in.pos = manager.pos
        self.screen_out.pos = manager.pos

        if self.transition_axis == "z":
            if self.ih not in self._s_map.keys():
                # Save scale instructions.
                with self.screen_in.canvas.before:
                    PushMatrix()
                    self._s_map[self.ih] = Scale()
                with self.screen_in.canvas.after:
                    PopMatrix()
                with self.screen_out.canvas.before:
                    PushMatrix()
                    self._s_map[self.oh] = Scale()
                with self.screen_out.canvas.after:
                    PopMatrix()

            self._s_map[self.oh].origin = [
                (manager.pos[0] + manager.width) / 2,
                (manager.pos[1] + manager.height) / 2,
            ]
            self._s_map[self.ih].origin = self._s_map[self.oh].origin
            # Relative subtracted area.
            self._slide_diff = (manager.width - self.slide_distance) * (
                manager.height - self.slide_distance
            ) / (manager.width * manager.height) - 1
        elif self.transition_axis in ["x", "y"]:
            # Slide distance with opposite logic.
            self._slide_diff = (
                (1 if self.opposite else -1) * self.slide_distance * 2
            )
        super().start(manager)

    def on_progress(self, progress):
        # This code could be simplyfied with setattr, but it's slow
        progress = getattr(MDAnimationTransition, self.switch_animation)(progress)
        progress_i = progress - 1
        progress_d = progress * 2
        # First half.
        if progress <= 0.5:
            # Screen out animation.
            if self.transition_axis == "z":
                self._s_map[self.oh].xyz = (
                    *[1 + self._slide_diff * progress_d] * 2,
                    1,
                )
            elif self.transition_axis == "x":
                self.screen_out.pos = [
                    self.manager.pos[0] + self._slide_diff * progress,
                    self.manager.pos[1],
                ]
            else:
                self.screen_out.pos = [
                    self.manager.pos[0],
                    self.manager.pos[1] - self._slide_diff * progress,
                ]
            self.screen_out.opacity = 1 - progress_d
            self.screen_in.opacity = 0
        # Second half.
        else:
            if self.transition_axis == "z":
                self._s_map[self.ih].xyz = (
                    *[1 - self._slide_diff * progress_i * 2] * 2,
                    1,
                )
            elif self.transition_axis == "x":
                self.screen_in.pos = [
                    self.manager.pos[0] + self._slide_diff * progress_i,
                    self.manager.pos[1],
                ]
            else:
                self.screen_in.pos = [
                    self.manager.pos[0],
                    self.manager.pos[1] - self._slide_diff * progress_i,
                ]
            self.screen_in.opacity = progress_d - 1
            self.screen_out.opacity = 0

    def on_complete(self):
        self.screen_in.pos = self.manager.pos
        self.screen_out.pos = self.manager.pos
        self.screen_out.opacity = 1
        self.screen_in.opacity = 1
        if self.oh in self._s_map.keys():
            self._s_map[self.oh].xyz = (1, 1, 1)
        if self.ih in self._s_map.keys():
            self._s_map[self.ih].xyz = (1, 1, 1)
        super().on_complete()
