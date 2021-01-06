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
    Screen

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

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
)
from kivy.uix.slider import Slider
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import Thumb kivymd.uix.selectioncontrol.Thumb


<MDSlider>
    id: slider
    canvas:
        Clear
        Color:
            rgba:
                self._track_color_disabled if self.disabled \
                else (self._track_color_active if self.active \
                else self._track_color_normal)
        Rectangle:
            size:
                (self.width - self.padding * 2 - self._offset[0], dp(4)) if \
                self.orientation == "horizontal" \
                else (dp(4),self.height - self.padding*2 - self._offset[1])
            pos:
                (self.x + self.padding + self._offset[0], self.center_y - dp(4)) \
                if self.orientation == "horizontal" else \
                (self.center_x - dp(4), self.y + self.padding + self._offset[1])

        # If 0 draw circle
        Color:
            rgba:
                (0, 0, 0, 0) if not self._is_off \
                else (self._track_color_disabled if self.disabled \
                else (self._track_color_active \
                if self.active else self._track_color_normal))
        Line:
            width: 2
            circle:
                (self.x + self.padding + dp(3), self.center_y - dp(2), 8 \
                if self.active else 6 ) if self.orientation == "horizontal" \
                else (self.center_x - dp(2), self.y + self.padding + dp(3), 8 \
                if self.active else 6)

        Color:
            rgba:
                (0, 0, 0, 0) if self._is_off \
                else (self.color if not self.disabled \
                else self._track_color_disabled)
        Rectangle:
            size:
                ((self.width - self.padding * 2) * self.value_normalized, sp(4)) \
                if slider.orientation == "horizontal" else (sp(4), \
                (self.height - self.padding * 2) * self.value_normalized)
            pos:
                (self.x + self.padding, self.center_y - dp(4)) \
                if self.orientation == "horizontal" \
                else (self.center_x - dp(4), self.y + self.padding)

    Thumb:
        id: thumb
        size_hint: None, None
        size:
            (dp(12), dp(12)) if root.disabled else ((dp(24), dp(24)) \
            if root.active else (dp(16), dp(16)))
        pos:
            (slider.value_pos[0] - dp(8), slider.center_y - thumb.height / 2 - dp(2)) \
            if slider.orientation == "horizontal" \
            else (slider.center_x - thumb.width / 2 - dp(2), \
            slider.value_pos[1] - dp(8))
        color:
            (0, 0, 0, 0) if slider._is_off else (root._track_color_disabled \
            if root.disabled else root.color)
        elevation:
            0 if slider._is_off else (4 if root.active else 2)

    MDCard:
        id: hint_box
        size_hint: None, None
        md_bg_color: (1, 1, 1, 1) if not root.hint_bg_color else slider.hint_bg_color
        elevation: 0
        opacity: 1 if slider.active else 0
        background: f"{images_path}transparent.png"
        radius: [slider.hint_radius,]
        size:
            (dp(12), dp(12)) if root.disabled else ((dp(28), dp(28)) \
            if root.active else (dp(20), dp(20)))
        pos:
            (slider.value_pos[0] - dp(9), slider.center_y - hint_box.height / 2 + dp(30)) \
            if slider.orientation == "horizontal" \
            else (slider.center_x - hint_box.width / 2 + dp(30), \
            slider.value_pos[1] - dp(8))

        MDLabel:
            text: str(int(slider.value))
            font_style: "Caption"
            halign: "center"
            theme_text_color: "Custom"
            text_color:
                (root.color if root.active else (0, 0, 0, 0)) \
                if not slider.hint_text_color else slider.hint_text_color
"""
)


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

    hint_bg_color = ColorProperty(None)
    """
    Hint rectangle color in ``rgba`` format.

    :attr:`hint_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_text_color = ColorProperty(None)
    """
    Hint text color in ``rgba`` format.

    :attr:`hint_text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    hint_radius = NumericProperty(4)
    """
    Hint radius.

    :attr:`hint_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `4`.
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
        """When the ``value == min`` set it to `'off'` state and make slider
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
        """Offset is used to shift the sliders so the background color
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
