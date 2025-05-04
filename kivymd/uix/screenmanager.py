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

:class:`~kivy.uix.screenmanager.ScreenManager` class equivalent. Simplifies
working with some widget properties. For example:

ScreenManager
-------------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            ScreenManager:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.screenmanager import ScreenManager
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = ScreenManager()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDScreenManager
---------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDScreenManager:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.sreenmanager import MDScreenManager
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDScreenManager(
                        md_bg_color=self.theme_cls.primaryColor
                    )

            MyApp().run()

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:

adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:

adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    height: self.minimum_width

.. adaptive_size:

adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

__all__ = ("MDScreenManager",)

from kivy import Logger
from kivy.clock import Clock
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior
from kivymd.uix.hero import MDHeroFrom


class MDScreenManager(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    ScreenManager,
    MDAdaptiveWidget,
):
    """
    Screen manager. This is the main class that will control your
    :class:`~kivymd.uix.screen.MDScreen` stack and memory.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.screenmanager.ScreenManager` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
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
            from kivymd.uix.transition import MDSharedAxisTransition

            self.transition = MDSharedAxisTransition()

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
        Fired when the value of the :attr:`current_hero` attribute changes.
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

    # TODO: Add a method to delete an object from the attr:`_heroes_data`
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
