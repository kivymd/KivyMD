"""
Components/FloatLayout
======================

:class:`~kivy.uix.floatlayout.FloatLayout` class equivalent. Simplifies working
with some widget properties. For example:

FloatLayout
-----------

.. code-block:: kv

    FloatLayout:
        canvas:
            Color:
                rgba: app.theme_cls.primaryColor
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

MDFloatLayout
-------------

.. code-block:: kv

    MDFloatLayout:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primaryColor

.. Warning:: For a :class:`~kivy.uix.floatlayout.FloatLayout`, the
    ``minimum_size`` attributes are always 0, so you cannot use
    ``adaptive_size`` and related options.
"""

from kivy.uix.floatlayout import FloatLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, BackgroundColorBehavior


class MDFloatLayout(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    FloatLayout,
    MDAdaptiveWidget,
):
    """
    Float layout class.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    classes documentation.
    """
