"""
Components/Selection Controls
=============================

.. seealso::

    `Material Design spec, Selection controls <https://material.io/components/selection-controls>`_

.. rubric:: Selection controls allow the user to select options.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/selection-controll.png
    :align: center

`KivyMD` provides the following selection controls classes for use:

- MDCheckbox_
- MDSwitch_

.. MDCheckbox:
MDCheckbox
----------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp


    KV = '''
    MDFloatLayout:

        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox.gif
    :align: center

.. Note:: Be sure to specify the size of the checkbox. By default, it is
    ``(dp(48), dp(48))``, but the ripple effect takes up all the available
    space.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-no-size.gif
    :align: center

Control state
-------------

.. code-block:: kv

    MDCheckbox:
        on_active: app.on_checkbox_active(*args)

.. code-block:: python

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

MDCheckbox with group
---------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <Check@MDCheckbox>:
        group: 'group'
        size_hint: None, None
        size: dp(48), dp(48)


    MDFloatLayout:

        Check:
            active: True
            pos_hint: {'center_x': .4, 'center_y': .5}

        Check:
            pos_hint: {'center_x': .6, 'center_y': .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-group.gif
    :align: center

.. MDSwitch:
MDSwitch
--------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDFloatLayout:

        MDSwitch:
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-switch.gif
    :align: center

.. Note:: For :class:`~MDSwitch` size is not required. By default it is
    ``(dp(36), dp(48))``, but you can increase the width if you want.

.. code-block:: kv

    MDSwitch:
        width: dp(64)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-switch_width.png
    :align: center

.. Note:: Control state of :class:`~MDSwitch` same way as in
    :class:`~MDCheckbox`.
"""

__all__ = ("MDCheckbox", "MDSwitch")

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivymd.color_definitions import colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    FakeCircularElevationBehavior,
)
from kivymd.uix.label import MDIcon

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
                self._track_color_disabled if self.disabled else \
                ( \
                self._track_color_active \
                if self.active else self._track_color_normal \
                )
        RoundedRectangle:
            size:
                (self.width + dp(14), dp(28)) \
                if root.widget_style == "ios" else \
                (self.width - dp(8), dp(16))
            pos:
                (self.x - dp(2), self.center_y - dp(14)) \
                if root.widget_style == "ios" else \
                (self.x + dp(8), self.center_y - dp(8))
            radius:
                [dp(14)] if root.widget_style == "ios" else [dp(7)]
        Color:
            rgba:
                ( \
                self.theme_cls.disabled_hint_text_color[:-1] + [.2] \
                if not root.active else (0, 0, 0, 0) \
                ) \
                if root.widget_style == "ios" else (0, 0, 0, 0)
        Line:
            width: 1
            rounded_rectangle:
                ( \
                self.x - dp(2), self.center_y - dp(14), self.width + dp(14), \
                dp(28), dp(14), dp(14), dp(14), dp(14), dp(28) \
                ) \
                if root.widget_style == "ios" else \
                (1, 1, 1, 1, 1, 1, 1, 1, 1)

    Thumb:
        id: thumb
        size_hint: None, None
        size: dp(24), dp(24)
        pos: root.pos[0] + root._thumb_pos[0], root.pos[1] + root._thumb_pos[1]
        color:
            root.thumb_color_disabled if root.disabled else \
            (root.thumb_color_down if root.active else root.thumb_color)
        elevation: 8 if root.active else 5
        on_release: setattr(root, "active", not root.active)
"""
)


class MDCheckbox(CircularRippleBehavior, ToggleButtonBehavior, MDIcon):
    active = BooleanProperty(False)
    """
    Indicates if the checkbox is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    checkbox_icon_normal = StringProperty("checkbox-blank-outline")
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is not pressed.

    :attr:`checkbox_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-outline'`.
    """

    checkbox_icon_down = StringProperty("checkbox-marked")
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is pressed.

    :attr:`checkbox_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked'`.
    """

    radio_icon_normal = StringProperty("checkbox-blank-circle-outline")
    """
    Background icon (when using the ``group`` option) of the checkbox used for
    the default graphical representation when the checkbox is not pressed.

    :attr:`radio_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle-outline'`.
    """

    radio_icon_down = StringProperty("checkbox-marked-circle")
    """
    Background icon (when using the ``group`` option) of the checkbox used for
    the default graphical representation when the checkbox is pressed.

    :attr:`radio_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked-circle'`.
    """

    selected_color = ColorProperty(None)
    """
    Selected color in ``rgba`` format.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    unselected_color = ColorProperty(None)
    """
    Unelected color in ``rgba`` format.

    :attr:`unselected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    disabled_color = ColorProperty(None)
    """
    Disabled color in ``rgba`` format.

    :attr:`disabled_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _current_color = ColorProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self.check_anim_out = Animation(font_size=0, duration=0.1, t="out_quad")
        self.check_anim_in = Animation(
            font_size=sp(24), duration=0.1, t="out_quad"
        )
        super().__init__(**kwargs)
        self.selected_color = self.theme_cls.primary_color
        self.unselected_color = self.theme_cls.secondary_text_color
        self.disabled_color = self.theme_cls.divider_color
        self._current_color = self.unselected_color
        self.check_anim_out.bind(
            on_complete=lambda *x: self.check_anim_in.start(self)
        )
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
        self.theme_cls.bind(primary_color=self.update_primary_color)
        self.theme_cls.bind(theme_style=self.update_primary_color)
        self.update_icon()
        self.update_color()

    def update_primary_color(self, instance, value):
        if value in ("Dark", "Light"):
            if not self.disabled:
                self.color = self.theme_cls.primary_color
            else:
                self.color = self.disabled_color
        else:
            self.selected_color = value

    def update_icon(self, *args):
        if self.state == "down":
            self.icon = (
                self.radio_icon_down if self.group else self.checkbox_icon_down
            )
        else:
            self.icon = (
                self.radio_icon_normal
                if self.group
                else self.checkbox_icon_normal
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
            if self.group:
                self._release_group(self)
            self.active = True
        else:
            self.check_anim_in.cancel(self)
            if not self.group:
                self.check_anim_out.start(self)
            self.update_icon()
            self.active = False

    def on_active(self, *args):
        self.state = "down" if self.active else "normal"


class Thumb(
    FakeCircularElevationBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    Widget,
):
    ripple_scale = NumericProperty(2)
    """
    See :attr:`~kivymd.uix.behaviors.ripplebehavior.CommonRipple.ripple_scale`.

    :attr:`ripple_scale` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    def _set_ellipse(self, instance, value):
        self.ellipse.size = (self._ripple_rad, self._ripple_rad)
        if self.ellipse.size[0] > self.width * 1.5 and not self._fading_out:
            self.fade_out()
        self.ellipse.pos = (
            self.center_x - self._ripple_rad / 2.0,
            self.center_y - self._ripple_rad / 2.0,
        )
        self.stencil.pos = (
            self.center_x - (self.width * self.ripple_scale) / 2,
            self.center_y - (self.height * self.ripple_scale) / 2,
        )


class MDSwitch(ThemableBehavior, ButtonBehavior, FloatLayout):
    active = BooleanProperty(False)
    """
    Indicates if the switch is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _thumb_color = ColorProperty(get_color_from_hex(colors["Gray"]["50"]))

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
    """
    Get thumb color ``rgba`` format.

    :attr:`thumb_color` is an :class:`~kivy.properties.AliasProperty`
    and property is readonly.
    """

    _thumb_color_down = ColorProperty([1, 1, 1, 1])

    def _get_thumb_color_down(self):
        return self._thumb_color_down

    def _set_thumb_color_down(self, color, alpha=None):
        if len(color) == 2:
            self._thumb_color_down = get_color_from_hex(
                colors[color[0]][color[1]]
            )
            if alpha:
                self._thumb_color_down[3] = alpha
            else:
                self._thumb_color_down[3] = 1
        elif len(color) == 4:
            self._thumb_color_down = color

    _thumb_color_disabled = ColorProperty(
        get_color_from_hex(colors["Gray"]["400"])
    )

    thumb_color_disabled = get_color_from_hex(colors["Gray"]["800"])
    """
    Get thumb color disabled ``rgba`` format.

    :attr:`thumb_color_disabled` is an :class:`~kivy.properties.AliasProperty`
    and property is readonly.
    """

    def _get_thumb_color_disabled(self):
        return self._thumb_color_disabled

    def _set_thumb_color_disabled(self, color, alpha=None):
        if len(color) == 2:
            self._thumb_color_disabled = get_color_from_hex(
                colors[color[0]][color[1]]
            )
            if alpha:
                self._thumb_color_disabled[3] = alpha
        elif len(color) == 4:
            self._thumb_color_disabled = color

    thumb_color_down = AliasProperty(
        _get_thumb_color_disabled,
        _set_thumb_color_disabled,
        bind=["_thumb_color_disabled"],
    )
    """
    Get thumb color down ``rgba`` format.

    :attr:`thumb_color_down` is an :class:`~kivy.properties.AliasProperty`
    and property is readonly.
    """

    theme_thumb_color = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Thumb color scheme name

    :attr:`theme_thumb_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `Primary`.
    """

    theme_thumb_down_color = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Thumb Down color scheme name

    :attr:`theme_thumb_down_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `Primary`.
    """

    _track_color_active = ColorProperty([0, 0, 0, 0])
    _track_color_normal = ColorProperty([0, 0, 0, 0])
    _track_color_disabled = ColorProperty([0, 0, 0, 0])
    _thumb_pos = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(
            theme_style=self._set_colors,
            primary_color=self._set_colors,
            primary_palette=self._set_colors,
        )
        self.bind(active=self._update_thumb_pos)
        Clock.schedule_once(self._set_colors)
        self.size_hint = (None, None)
        self.size = (dp(36), dp(48))

    def _set_colors(self, *args):
        self._track_color_normal = self.theme_cls.disabled_hint_text_color
        if self.theme_cls.theme_style == "Dark":

            if self.theme_thumb_down_color == "Primary":
                self._track_color_active = self.theme_cls.primary_color
            else:
                self._track_color_active = self.thumb_color_down

            self._track_color_active[3] = 0.5
            self._track_color_disabled = get_color_from_hex("FFFFFF")
            self._track_color_disabled[3] = 0.1

            if self.theme_thumb_color == "Primary":
                self.thumb_color = get_color_from_hex(colors["Gray"]["400"])

            if self.theme_thumb_down_color == "Primary":
                self.thumb_color_down = get_color_from_hex(
                    colors[self.theme_cls.primary_palette]["200"]
                )
        else:
            if self.theme_thumb_down_color == "Primary":
                self._track_color_active = get_color_from_hex(
                    colors[self.theme_cls.primary_palette]["200"]
                )
            else:
                self._track_color_active = self.thumb_color_down

            self._track_color_active[3] = 0.5
            self._track_color_disabled = self.theme_cls.disabled_hint_text_color

            if self.theme_thumb_down_color == "Primary":
                self.thumb_color_down = self.theme_cls.primary_color

            if self.theme_thumb_color == "Primary":
                self.thumb_color = get_color_from_hex(colors["Gray"]["50"])

    def _update_thumb_pos(self, *args, animation=True):
        if self.active:
            _thumb_pos = (self.width - dp(14), self.height / 2 - dp(12))
        else:
            _thumb_pos = (0, self.height / 2 - dp(12))
        Animation.cancel_all(self, "_thumb_pos")
        if animation:
            Animation(_thumb_pos=_thumb_pos, duration=0.2, t="out_quad").start(
                self
            )
        else:
            self._thumb_pos = _thumb_pos

    def on_size(self, *args):
        self._update_thumb_pos(animation=False)
