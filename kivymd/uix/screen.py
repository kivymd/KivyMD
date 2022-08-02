"""
Components/Screen
=================

:class:`~kivy.uix.screenmanager.Screen` class equivalent. Simplifies working
with some widget properties. For example:

Screen
------

.. code-block:: kv

    Screen:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

MDScreen
--------

.. code-block:: kv

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
"""

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.hero import MDHeroTo


class MDScreen(DeclarativeBehavior, Screen, MDAdaptiveWidget):
    """
    Screen is an element intended to be used with a
    :class:`~kivymd.uix.screenmanager.MDScreenManager`. For more information,
    see in the :class:`~kivy.uix.screenmanager.Screen` class documentation.
    """

    hero_to = ObjectProperty()
    """
    Must be a  :class:`~kivymd.uix.hero.MDHeroTo` class.
    See the documentation of the
    `MDHeroTo <https://kivymd.readthedocs.io/en/latest/components/hero/>`_
    widget for more detailed information.

    .. versionchanged:: 1.0.0

    :attr:`hero_to` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def on_hero_to(self, screen, widget) -> None:
        if not isinstance(widget, MDHeroTo) or not issubclass(
            widget.__class__, MDHeroTo
        ):
            raise TypeError(
                f"The `{widget}` widget must be an `kivymd.uix.hero.MDHeroTo` "
                f"class or inherited from this class"
            )
