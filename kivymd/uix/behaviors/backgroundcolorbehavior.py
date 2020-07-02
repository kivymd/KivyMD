"""
Behaviors/Background Color
==========================

.. note:: The following classes are intended for in-house use of the library.
"""

__all__ = ("BackgroundColorBehavior", "SpecificBackgroundColorBehavior")

from kivy.lang import Builder
from kivy.properties import (
    BoundedNumericProperty,
    ListProperty,
    OptionProperty,
    ReferenceListProperty,
)
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import hue, palette, text_colors

Builder.load_string(
    """
<BackgroundColorBehavior>
    canvas:
        Color:
            rgba: self.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
"""
)


class BackgroundColorBehavior(Widget):
    r = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``red`` in the ``rgba`` palette.

    :attr:`r` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    g = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``green`` in the ``rgba`` palette.

    :attr:`g` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    b = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    """The value of ``blue`` in the ``rgba`` palette.

    :attr:`b` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `1.0`.
    """

    a = BoundedNumericProperty(0.0, min=0.0, max=1.0)
    """The value of ``alpha channel`` in the ``rgba`` palette.

    :attr:`a` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.0`.
    """

    radius = ListProperty([0, 0, 0, 0])
    """Canvas radius.

    .. code-block:: python

        # Top left corner slice.
        MDBoxLayout:
            md_bg_color: app.theme_cls.primary_color
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    md_bg_color = ReferenceListProperty(r, g, b, a)
    """The background color of the widget (:class:`~kivy.uix.widget.Widget`)
    that will be inherited from the :attr:`BackgroundColorBehavior` class.

    For example:

    .. code-block:: kv

        Widget:
            canvas:
                Color:
                    rgba: 0, 1, 1, 1
                Rectangle:
                    size: self.size
                    pos: self.pos

    similar to code:

    .. code-block:: kv

        <MyWidget@BackgroundColorBehavior>
            md_bg_color: 0, 1, 1, 1

    :attr:`md_bg_color` is an :class:`~kivy.properties.ReferenceListProperty`
    and defaults to :attr:`r`, :attr:`g`, :attr:`b`, :attr:`a`.
    """


class SpecificBackgroundColorBehavior(BackgroundColorBehavior):
    background_palette = OptionProperty(
        "Primary", options=["Primary", "Accent", *palette]
    )
    """See :attr:`kivymd.color_definitions.palette`.

    :attr:`background_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    background_hue = OptionProperty("500", options=hue)
    """See :attr:`kivymd.color_definitions.hue`.

    :attr:`background_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    specific_text_color = ListProperty([0, 0, 0, 0.87])
    """:attr:`specific_text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0.87]`.
    """

    specific_secondary_text_color = ListProperty([0, 0, 0, 0.87])
    """:attr:`specific_secondary_text_color`is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0.87]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self, "theme_cls"):
            self.theme_cls.bind(
                primary_palette=self._update_specific_text_color
            )
            self.theme_cls.bind(accent_palette=self._update_specific_text_color)
            self.theme_cls.bind(theme_style=self._update_specific_text_color)
        self.bind(background_hue=self._update_specific_text_color)
        self.bind(background_palette=self._update_specific_text_color)
        self._update_specific_text_color(None, None)

    def _update_specific_text_color(self, instance, value):
        if hasattr(self, "theme_cls"):
            palette = {
                "Primary": self.theme_cls.primary_palette,
                "Accent": self.theme_cls.accent_palette,
            }.get(self.background_palette, self.background_palette)
        else:
            palette = {"Primary": "Blue", "Accent": "Amber"}.get(
                self.background_palette, self.background_palette
            )
        color = get_color_from_hex(text_colors[palette][self.background_hue])
        secondary_color = color[:]
        # Check for black text (need to adjust opacity).
        if (color[0] + color[1] + color[2]) == 0:
            color[3] = 0.87
            secondary_color[3] = 0.54
        else:
            secondary_color[3] = 0.7
        self.specific_text_color = color
        self.specific_secondary_text_color = secondary_color
