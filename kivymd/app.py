"""
App
===

This module contains :class:`MDApp` class that is inherited from
:class:`~kivy.app.App`. :class:`MDApp` has some properties needed for KivyMD
library (like :attr:`~MDApp.theme_cls`).
"""

__all__ = ("MDApp",)

from kivy.app import App
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager


class MDApp(App):
    theme_cls = ObjectProperty(ThemeManager())
