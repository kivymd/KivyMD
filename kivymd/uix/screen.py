"""
Components/Screen
=================

:class:`~kivy.uix.screenmanager.Screen` class equivalent. Simplifies working
with some widget properties. For example:

Screen
------

.. tabs::

    .. tab:: KV

        .. code-block:: kv

            Screen:
                canvas:
                    Color:
                        rgba: app.theme_cls.primaryColor
                    Rectangle:
                        pos: self.pos
                        size: self.size

    .. tab:: Python

        .. code-block:: python

            from kivy.uix.screenmanager import Screen
            from kivy.graphics import Color, Rectangle
            from kivy.app import App

            class MyApp(App):
                def build(self):
                    layout = Screen()

                    with layout.canvas:
                        Color(*self.theme_cls.primary_color)
                        self.rect = Rectangle(pos=layout.pos, size=layout.size)

                    return layout

            MyApp().run()

MDScreen
--------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: kv

            MDScreen:
                md_bg_color: app.theme_cls.primaryColor

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp

            class MyApp(App):
                def build(self):
                    return MDScreen(
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

__all__ = ("MDScreen",)

from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import Screen

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior
from kivymd.uix.hero import MDHeroTo


class MDScreen(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    Screen,
    MDAdaptiveWidget,
):
    """
    Screen is an element intended to be used with a
    :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.screenmanager.Screen` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """

    hero_to = ObjectProperty(deprecated=True)
    """
    Must be a :class:`~kivymd.uix.hero.MDHeroTo` class.

    See the documentation of the
    `MDHeroTo <https://kivymd.readthedocs.io/en/latest/components/hero/>`_
    widget for more detailed information.

    .. deprecated:: 1.0.0
        Use attr:`heroes_to` attribute instead.

    :attr:`hero_to` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    heroes_to = ListProperty()
    """
    Must be a list of :class:`~kivymd.uix.hero.MDHeroTo` class.

    .. versionadded:: 1.0.0

    :attr:`heroes_to` is an :class:`~kivy.properties.LiatProperty`
    and defaults to `[]`.
    """

    def on_hero_to(self, screen, widget: MDHeroTo) -> None:
        """Fired when the value of the :attr:`hero_to` attribute changes."""

        if not isinstance(widget, MDHeroTo) or not issubclass(
            widget.__class__, MDHeroTo
        ):
            raise TypeError(
                f"The `{widget}` widget must be an `kivymd.uix.hero.MDHeroTo` "
                f"class or inherited from this class"
            )
        self.heroes_to = [widget]
