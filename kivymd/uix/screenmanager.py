"""
Components/ScreenManager
========================

.. versionadded:: 1.0.0

:class:`~kivy.uix.screenmanager.ScreenManager` class equivalent.
If you want to use Hero animations you need to use
:class:`~kivymd.uix.screenmanager.MDScreenManager` not
:class:`~kivy.uix.screenmanager.ScreenManager` class.

Transition
----------

:class:`~kivymd.uix.screenmanager.MDScreenManager` class supports the following
transitions:

- :class:`~kivymd.uix.transition.MDFadeSlideTransition`
- :class:`~kivymd.uix.transition.MDSlideTransition`
- :class:`~kivymd.uix.transition.MDSwapTransition`

You need to use the :class:`~kivymd.uix.screenmanager.MDScreenManager` class
when you want to use hero animations on your screens. If you don't need hero
animation use the :class:`~kivy.uix.screenmanager.ScreenManager` class.
"""

from kivy import Logger
from kivy.clock import Clock
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.hero import MDHeroFrom


class MDScreenManager(DeclarativeBehavior, ScreenManager):
    """
    Screen manager. This is the main class that will control your
    :class:`~kivymd.uix.screen.MDScreen` stack and memory.

    For more
    information, see in the :class:`~kivy.uix.screenmanager.ScreenManager`
    class documentation.
    """

    current_hero = StringProperty(None, deprecated=True)
    """
    The name of the current tag for the :class:`~kivymd.uix.hero.MDHeroFrom`
    and :class:`~kivymd.uix.hero.MDHeroTo` objects that will be animated when
    animating the transition between screens.

    .. deprecated:: 1.1.0
        Use :attr:`current_heroes` attribute instead.

    See the `Hero <https://kivymd.readthedocs.io/en/latest/components/hero/>`_
    module documentation for more information about creating and using Hero
    animations.

    :attr:`current_hero` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    current_heroes = ListProperty()
    """
    A list of names (tags) of heroes that need to be animated when moving
    to the next screen.

    .. versionadded:: 1.1.0

    :attr:`current_heroes` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    # Collection of `MDHeroFrom` objects on all screens of the current
    # screen manager.
    _heroes_data = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.check_transition)

    def check_transition(self, *args) -> None:
        """Sets the default type transition."""

        from kivymd.uix.transition.transition import MDTransitionBase

        if not issubclass(self.transition.__class__, MDTransitionBase):
            from kivymd.uix.transition import MDSlideTransition

            self.transition = MDSlideTransition()

    def get_hero_from_widget(self) -> list:
        """
        Get a list of :class:`~kivymd.uix.hero.MDHeroFrom` objects according
        to the tag names specified in the :attr:`~current_heroes` list.
        """

        hero_from_widget = []

        for name_hero in self.current_heroes:
            for hero_widget in self._heroes_data:
                if isinstance(hero_widget, MDHeroFrom) or issubclass(
                    hero_widget.__class__, MDHeroFrom
                ):
                    if hero_widget.tag == name_hero:
                        hero_from_widget.append(hero_widget)

        return hero_from_widget

    def on_current_hero(self, instance, value: str) -> None:
        """
        Called when the value of the :attr:`current_hero` attribute changes.
        """

        Logger.warning(
            "KivyMD: "
            "`kivymd/uix/screenmanager.MDScreenManager.current_hero` "
            "attribute is deprecated. "
            "Use `kivymd/uix/screenmanager.MDScreenManager.current_heroes` "
            "attribute instead."
        )
        if value:
            self.current_heroes = [value]
        else:
            self.current_heroes = []

    def add_widget(self, widget, *args, **kwargs):
        super().add_widget(widget, *args, **kwargs)
        Clock.schedule_once(lambda x: self._create_heroes_data(widget))

    # TODO: Add a method to delete an object from the arrt:`_heroes_data`
    #  collection when deleting an object using the `remove_widget` method.

    def _create_heroes_data(self, widget):
        def find_hero_widget(child_widget):
            widget_hero = None

            for w in child_widget.children:
                if isinstance(w, MDHeroFrom) or issubclass(
                    w.__class__, MDHeroFrom
                ):
                    self._heroes_data.append(w)
                find_hero_widget(w)

            return widget_hero

        for child in widget.children:
            if isinstance(child, MDHeroFrom) or issubclass(
                child.__class__, MDHeroFrom
            ):
                self._heroes_data.append(child)
            else:
                find_hero_widget(child)
