"""
Components/Slider
=================

.. seealso::

    `Material Design spec, Sliders <https://material.io/components/sliders>`_

.. rubric:: Sliders allow users to make selections from a range of values.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider.png
    :align: center

With value hint
---------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen

        MDSlider:
            min: 0
            max: 100
            value: 40
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider-1.gif
    :align: center

Without value hint
------------------

.. code-block:: kv

    MDSlider:
        min: 0
        max: 100
        value: 40
        hint: False

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider-2.gif
    :align: center

Without custom color
--------------------

.. code-block:: kv

    MDSlider:
        min: 0
        max: 100
        value: 40
        hint: False
        color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/slider-3.png
    :align: center
"""

__all__ = ("MDSlider",)

import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    VariableListProperty,
)
from kivy.uix.slider import Slider
from kivy.utils import get_color_from_hex

from kivymd import uix_path
from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "slider", "slider.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSlider(ThemableBehavior, Slider):
    active = BooleanProperty(False)
    """
    If the slider is clicked.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    hint = BooleanProperty(True)
    """
    If True, then the current value is displayed above the slider.

    :attr:`hint` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    hint_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Hint rectangle color in ``rgba`` format.

    :attr:`hint_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    hint_text_color = ColorProperty(None)
    """
    Hint text color in ``rgba`` format.

    :attr:`hint_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_radius = VariableListProperty([dp(4), dp(4), dp(4), dp(4)])
    """
    Hint radius.

    :attr:`hint_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(4), dp(4), dp(4), dp(4)]`.
    """

    show_off = BooleanProperty(True)
    """
    Show the `'off'` ring when set to minimum value.

    :attr:`show_off` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    color = ColorProperty([0, 0, 0, 0])
    """
    Color slider in ``rgba`` format.

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _track_color_active = ColorProperty([0, 0, 0, 0])
    _track_color_normal = ColorProperty([0, 0, 0, 0])
    _track_color_disabled = ColorProperty([0, 0, 0, 0])
    _thumb_pos = ListProperty([0, 0])
    _thumb_color_disabled = ColorProperty(
        get_color_from_hex(colors["Gray"]["400"])
    )
    # Internal state of ring
    _is_off = BooleanProperty(False)
    # Internal adjustment to reposition sliders for ring
    _offset = ListProperty((0, 0))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(
            theme_style=self._set_colors,
            primary_color=self._set_colors,
            primary_palette=self._set_colors,
        )
        self._set_colors()

    def on_hint(self, instance, value):
        if not value:
            self.remove_widget(self.ids.hint_box)

    def on_value_normalized(self, *args):
        """
        When the ``value == min`` set it to `'off'` state and make slider
        a ring.
        """

        self._update_is_off()

    def on_show_off(self, *args):
        self._update_is_off()

    def on__is_off(self, *args):
        self._update_offset()

    def on_active(self, *args):
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

    def _set_colors(self, *args):
        if self.theme_cls.theme_style == "Dark":
            self._track_color_normal = get_color_from_hex("FFFFFF")
            self._track_color_normal[3] = 0.3
            self._track_color_active = self._track_color_normal
            self._track_color_disabled = self._track_color_normal
            if self.color == [0, 0, 0, 0]:
                self.color = get_color_from_hex(
                    colors[self.theme_cls.primary_palette]["200"]
                )
            self.thumb_color_disabled = get_color_from_hex(
                colors["Gray"]["800"]
            )
        else:
            self._track_color_normal = get_color_from_hex("000000")
            self._track_color_normal[3] = 0.26
            self._track_color_active = get_color_from_hex("000000")
            self._track_color_active[3] = 0.38
            self._track_color_disabled = get_color_from_hex("000000")
            self._track_color_disabled[3] = 0.26
            if self.color == [0, 0, 0, 0]:
                self.color = self.theme_cls.primary_color
