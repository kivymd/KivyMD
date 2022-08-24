"""
Components/Slider
=================

.. seealso::

    `Material Design spec, Sliders <https://material.io/components/sliders>`_

.. rubric:: Sliders allow users to make selections from a range of values.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider.png
    :align: center
"""

__all__ = ("MDSlider",)

import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    VariableListProperty,
)
from kivy.uix.slider import Slider

from kivymd import uix_path
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "slider", "slider.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSlider(ThemableBehavior, Slider):
    """
    Class for creating a Slider widget. See in the
    :class:`~kivy.uix.slider.Slider` class documentation.
    """

    active = BooleanProperty(False)
    """
    If the slider is clicked.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    color = ColorProperty(None)
    """
    Color slider.

    .. code-block:: kv

        MDSlider
            color: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-color.png
        :align: center

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint = BooleanProperty(True)
    """
    If True, then the current value is displayed above the slider.

    .. code-block:: kv

        MDSlider
            hint: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-hint.png
        :align: center

    :attr:`hint` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    hint_bg_color = ColorProperty(None)
    """
    Hint rectangle color in (r.g.b.a) format.

    .. code-block:: kv

        MDSlider
            hint: True
            hint_bg_color: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-hint-bg-color.png
        :align: center

    :attr:`hint_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    hint_text_color = ColorProperty(None)
    """
    Hint text color in (r.g.b.a) format.

    .. code-block:: kv

        MDSlider
            hint: True
            hint_bg_color: "red"
            hint_text_color: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-hint-text-color.png
        :align: center

    :attr:`hint_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_radius = VariableListProperty([dp(4), dp(4), dp(4), dp(4)])
    """
    Hint radius.

    .. code-block:: kv

        MDSlider
            hint: True
            hint_bg_color: "red"
            hint_text_color: "white"
            hint_radius: [6, 0, 6, 0]

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-hint-radius.png
        :align: center

    :attr:`hint_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(4), dp(4), dp(4), dp(4)]`.
    """

    thumb_color_active = ColorProperty(None)
    """
    The color of the thumb when the slider is active.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            thumb_color_active: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-thumb-color-active.png
        :align: center

    :attr:`thumb_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    thumb_color_inactive = ColorProperty(None)
    """
    The color of the thumb when the slider is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            thumb_color_inactive: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-thumb-color-inactive.png
        :align: center

    :attr:`thumb_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    thumb_color_disabled = ColorProperty(None)
    """
    The color of the thumb when the slider is in the disabled state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            value: 55
            disabled: True
            thumb_color_disabled: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-thumb-color-disabled.png
        :align: center

    :attr:`thumb_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_active = ColorProperty(None)
    """
    The color of the track when the slider is active.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            track_color_active: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-track-color-active.png
        :align: center

    :attr:`track_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_inactive = ColorProperty(None)
    """
    The color of the track when the slider is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            track_color_inactive: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-track-color-inactive.png
        :align: center

    :attr:`track_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_disabled = ColorProperty(None)
    """
    The color of the track when the slider is in the disabled state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSlider
            disabled: True
            track_color_disabled: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slide-track-color-disabled.png
        :align: center

    :attr:`track_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    show_off = BooleanProperty(True)
    """
    Show the `'off'` ring when set to minimum value.

    :attr:`show_off` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    _thumb_pos = ListProperty([0, 0])
    # Internal state of ring.
    _is_off = BooleanProperty(False)
    # Internal adjustment to reposition sliders for ring.
    _offset = ListProperty((0, 0))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_thumb_icon)

    def set_thumb_icon(self, *args) -> None:
        self.ids.thumb.ids.icon.icon = "blank"

    def on_hint(self, instance, value) -> None:
        def on_hint(*args):
            if not value:
                self.remove_widget(self.ids.hint_box)

        # Schedule using for declarative style.
        # Otherwise get AttributeError exception.
        Clock.schedule_once(on_hint)

    def on_value_normalized(self, *args) -> None:
        """
        When the ``value == min`` set it to `'off'` state and make slider
        a ring.
        """

        self._update_is_off()

    def on_show_off(self, *args) -> None:
        self._update_is_off()

    def on__is_off(self, *args) -> None:
        self._update_offset()

    def on_active(self, *args) -> None:
        self._update_offset()

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            self.active = True

    def on_touch_up(self, touch):
        if super().on_touch_up(touch):
            self.active = False

    def _update_offset(self):
        """
        Offset is used to shift the sliders so the background color
        shows through the off circle.
        """

        d = 2 if self.active else 0
        self._offset = (dp(11 + d), dp(11 + d)) if self._is_off else (0, 0)

    def _update_is_off(self):
        self._is_off = self.show_off and (self.value_normalized == 0)
