"""
Components/ScreenManager
========================

.. versionadded:: 1.0.0

:class:`~kivy.uix.screenmanager.ScreenManager` class equivalent.
If you want to use Hero animations you need to use
:class:`~kivymd.uix.screenmanager.MDScreenManager` not
:class:`~kivy.uix.screenmanager.ScreenManager` class.
"""

from kivy.clock import Clock
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.hero import MDHeroFrom


class MDScreenManager(DeclarativeBehavior, ScreenManager):
    """
    Screen manager. This is the main class that will control your
    :class:`~kivymd.uix.screen.MDScreen` stack and memory. For more
    information, see in the :class:`~kivy.uix.screenmanager.ScreenManager`
    class documentation.
    """

    current_hero = StringProperty(None)
    """
    The name of the current tag for the :class:`~kivymd.uix.hero.MDHeroFrom`
    and :class:`~kivymd.uix.hero.MDHeroTo` objects that will be animated when
    animating the transition between screens.

    See the `Hero <https://kivymd.readthedocs.io/en/latest/components/hero/>`_
    module documentation for more information about creating and using Hero
    animations.

    :attr:`current_hero` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
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

    def get_hero_from_widget(self) -> None:
        """
        Get an :class:`~kivymd.uix.hero.MDHeroTo` object with the
        :attr:`~current_hero` tag.
        """

        hero_from_widget = None

        for hero_widget in self._heroes_data:
            if isinstance(hero_widget, MDHeroFrom) or issubclass(
                hero_widget.__class__, MDHeroFrom
            ):
                if hero_widget.tag == self.current_hero:
                    hero_from_widget = hero_widget
                    break

        return hero_from_widget

    def add_widget(self, widget, *args, **kwargs):
        super().add_widget(widget, *args, **kwargs)
        Clock.schedule_once(lambda x: self._create_heroes_data(widget))

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
