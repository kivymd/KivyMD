"""
Selection Controls
==================

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Selection controls <https://material.io/design/components/selection-controls.html>`_
"""

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import AliasProperty, BooleanProperty
from kivy.metrics import dp, sp
from kivy.animation import Animation
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import colors
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.elevation import CircularElevationBehavior
from kivymd.ripplebehavior import CircularRippleBehavior
from kivymd.label import MDLabel, MDIcon
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget

Builder.load_string(
    """
<MDCheckbox>
    canvas:
        Clear
        Color:
            rgba: self.color
        Rectangle:
            texture: self.texture
            size: self.texture_size
            pos:
                int(self.center_x - self.texture_size[0] / 2.),\
                int(self.center_y - self.texture_size[1] / 2.)

    color: self._current_color
    halign: 'center'
    valign: 'middle'


<Thumb>
    color: 1, 1, 1, 1
    canvas:
        Color:
            rgba: self.color
        Ellipse:
            size: self.size
            pos: self.pos


<MDSwitch>
    canvas.before:
        Color:
            rgba:
                self._track_color_disabled if self.disabled else\
                (self._track_color_active if self.active\
                else self._track_color_normal)
        Ellipse:
            size: dp(16), dp(16)
            pos: self.x, self.center_y - dp(8)
            angle_start: 180
            angle_end: 360
        Rectangle:
            size: self.width - dp(16), dp(16)
            pos: self.x + dp(8), self.center_y - dp(8)
        Ellipse:
            size: dp(16), dp(16)
            pos: self.right - dp(16), self.center_y - dp(8)
            angle_start: 0
            angle_end: 180

    on_release: thumb.trigger_action()

    Thumb:
        id: thumb
        size_hint: None, None
        size: dp(24), dp(24)
        pos: root._thumb_pos
        color:
            root.thumb_color_disabled if root.disabled else\
            (root.thumb_color_down if root.active else root.thumb_color)
        elevation:    4 if root.active else 2
        on_release: setattr(root, 'active', not root.active)
"""
)


class MDCheckbox(CircularRippleBehavior, ToggleButtonBehavior, MDIcon):
    active = BooleanProperty(False)

    checkbox_icon_normal = StringProperty("checkbox-blank-outline")
    checkbox_icon_down = StringProperty("checkbox-marked-outline")
    radio_icon_normal = StringProperty("checkbox-blank-circle-outline")
    radio_icon_down = StringProperty("checkbox-marked-circle-outline")

    selected_color = ListProperty()
    unselected_color = ListProperty()
    disabled_color = ListProperty()
    _current_color = ListProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self.check_anim_out = Animation(font_size=0, duration=0.1, t="out_quad")
        self.check_anim_in = Animation(font_size=sp(24), duration=0.1, t="out_quad")
        super().__init__(**kwargs)
        self.selected_color = self.theme_cls.primary_color
        self.unselected_color = self.theme_cls.secondary_text_color
        self.disabled_color = self.theme_cls.divider_color
        self._current_color = self.unselected_color
        self.check_anim_out.bind(on_complete=lambda *x: self.check_anim_in.start(self))
        self.bind(
            checkbox_icon_normal=self.update_icon,
            checkbox_icon_down=self.update_icon,
            radio_icon_normal=self.update_icon,
            radio_icon_down=self.update_icon,
            group=self.update_icon,
            selected_color=self.update_color,
            unselected_color=self.update_color,
            disabled_color=self.update_color,
            disabled=self.update_color,
            state=self.update_color,
        )
        self.update_icon()
        self.update_color()

    def update_icon(self, *args):
        if self.state == "down":
            self.icon = self.radio_icon_down if self.group else self.checkbox_icon_down
        else:
            self.icon = (
                self.radio_icon_normal if self.group else self.checkbox_icon_normal
            )

    def update_color(self, *args):
        if self.disabled:
            self._current_color = self.disabled_color
        elif self.state == "down":
            self._current_color = self.selected_color
        else:
            self._current_color = self.unselected_color

    def on_state(self, *args):
        if self.state == "down":
            self.check_anim_in.cancel(self)
            self.check_anim_out.start(self)
            self.update_icon()
            self.active = True
        else:
            self.check_anim_in.cancel(self)
            self.check_anim_out.start(self)
            self.update_icon()
            self.active = False

    def on_active(self, *args):
        self.state = "down" if self.active else "normal"


class Thumb(CircularElevationBehavior, CircularRippleBehavior, ButtonBehavior, Widget):
    ripple_scale = NumericProperty(2)

    def _set_ellipse(self, instance, value):
        self.ellipse.size = (self.ripple_rad, self.ripple_rad)
        if self.ellipse.size[0] > self.width * 1.5 and not self.fading_out:
            self.fade_out()
        self.ellipse.pos = (
            self.center_x - self.ripple_rad / 2.0,
            self.center_y - self.ripple_rad / 2.0,
        )
        self.stencil.pos = (
            self.center_x - (self.width * self.ripple_scale) / 2,
            self.center_y - (self.height * self.ripple_scale) / 2,
        )


class MDSwitch(ThemableBehavior, ButtonBehavior, FloatLayout):
    active = BooleanProperty(False)

    _thumb_color = ListProperty(get_color_from_hex(colors["Gray"]["50"]))

    def _get_thumb_color(self):
        return self._thumb_color

    def _set_thumb_color(self, color, alpha=None):
        if len(color) == 2:
            self._thumb_color = get_color_from_hex(colors[color[0]][color[1]])
            if alpha:
                self._thumb_color[3] = alpha
        elif len(color) == 4:
            self._thumb_color = color

    thumb_color = AliasProperty(
        _get_thumb_color, _set_thumb_color, bind=["_thumb_color"]
    )

    _thumb_color_down = ListProperty([1, 1, 1, 1])

    def _get_thumb_color_down(self):
        return self._thumb_color_down

    def _set_thumb_color_down(self, color, alpha=None):
        if len(color) == 2:
            self._thumb_color_down = get_color_from_hex(colors[color[0]][color[1]])
            if alpha:
                self._thumb_color_down[3] = alpha
            else:
                self._thumb_color_down[3] = 1
        elif len(color) == 4:
            self._thumb_color_down = color

    thumb_color_down = AliasProperty(
        _get_thumb_color_down, _set_thumb_color_down, bind=["_thumb_color_down"]
    )

    _thumb_color_disabled = ListProperty(get_color_from_hex(colors["Gray"]["400"]))

    thumb_color_disabled = get_color_from_hex(colors["Gray"]["800"])

    def _get_thumb_color_disabled(self):
        return self._thumb_color_disabled

    def _set_thumb_color_disabled(self, color, alpha=None):
        if len(color) == 2:
            self._thumb_color_disabled = get_color_from_hex(colors[color[0]][color[1]])
            if alpha:
                self._thumb_color_disabled[3] = alpha
        elif len(color) == 4:
            self._thumb_color_disabled = color

    thumb_color_down = AliasProperty(
        _get_thumb_color_disabled,
        _set_thumb_color_disabled,
        bind=["_thumb_color_disabled"],
    )

    _track_color_active = ListProperty()
    _track_color_normal = ListProperty()
    _track_color_disabled = ListProperty()
    _thumb_pos = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(
            theme_style=self._set_colors,
            primary_color=self._set_colors,
            primary_palette=self._set_colors,
        )
        self._set_colors()

    def _set_colors(self, *args):
        self._track_color_normal = self.theme_cls.disabled_hint_text_color
        if self.theme_cls.theme_style == "Dark":
            self._track_color_active = self.theme_cls.primary_color
            self._track_color_active[3] = 0.5
            self._track_color_disabled = get_color_from_hex("FFFFFF")
            self._track_color_disabled[3] = 0.1
            self.thumb_color = get_color_from_hex(colors["Gray"]["400"])
            self.thumb_color_down = get_color_from_hex(
                colors[self.theme_cls.primary_palette]["200"]
            )
        else:
            self._track_color_active = get_color_from_hex(
                colors[self.theme_cls.primary_palette]["200"]
            )
            self._track_color_active[3] = 0.5
            self._track_color_disabled = self.theme_cls.disabled_hint_text_color
            self.thumb_color_down = self.theme_cls.primary_color

    def on_pos(self, *args):
        if self.active:
            self._thumb_pos = (self.right - dp(12), self.center_y - dp(12))
        else:
            self._thumb_pos = (self.x - dp(12), self.center_y - dp(12))
        self.bind(active=self._update_thumb)

    def _update_thumb(self, *args):
        if self.active:
            Animation.cancel_all(self, "_thumb_pos")
            anim = Animation(
                _thumb_pos=(self.right - dp(12), self.center_y - dp(12)),
                duration=0.2,
                t="out_quad",
            )
        else:
            Animation.cancel_all(self, "_thumb_pos")
            anim = Animation(
                _thumb_pos=(self.x - dp(12), self.center_y - dp(12)),
                duration=0.2,
                t="out_quad",
            )
        anim.start(self)
