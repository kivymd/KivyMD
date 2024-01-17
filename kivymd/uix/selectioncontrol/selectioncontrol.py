"""
Components/SelectionControls
============================

.. seealso::

    `Material Design spec, Checkbox <https://m3.material.io/components/checkbox/overview>`_

    `Material Design spec, Switch <https://m3.material.io/components/switch/overview>`_

.. rubric:: Selection controls allow the user to select options.

`KivyMD` provides the following selection controls classes for use:

- MDCheckbox_
- MDSwitch_

.. MDCheckbox:

MDCheckbox
----------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox.png
    :align: center

Usage
-----

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


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox.gif
    :align: center

.. Note:: Be sure to specify the size of the checkbox. By default, it is
    `(dp(48), dp(48))`, but the ripple effect takes up all the available
    space.

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


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-group.gif
    :align: center

Parent and child checkboxes
---------------------------

Checkboxes can have a parent-child relationship with other checkboxes. When
the parent checkbox is checked, all child checkboxes are checked. If a parent
checkbox is unchecked, all child checkboxes are unchecked. If some, but not all,
child checkboxes are checked, the parent checkbox becomes an indeterminate
checkbox.

Usage
-----

.. code-block:: kv

    MDCheckbox:
        group: "root"  # this is a required name for the parent checkbox group

    MDCheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

    MDCheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

Example
-------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    <CheckItem>
        adaptive_height: True

        MDCheckbox:
            group: root.group

        MDLabel:
            text: root.text
            adaptive_height: True
            padding_x: "12dp"
            pos_hint: {"center_y": .5}


    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: self.theme_cls.backgroundColor

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: "12dp", "36dp", 0, 0
            spacing: "12dp"

            CheckItem:
                text: "Recieve emails"
                group: "root"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "24dp", 0, 0, 0
                spacing: "12dp"

                CheckItem:
                    text: "Daily"
                    group: "child"

                CheckItem:
                    text: "Weekly"
                    group: "child"

                CheckItem:
                    text: "Monthly"
                    group: "child"

        MDWidget:
    '''


    class CheckItem(MDBoxLayout):
        text = StringProperty()
        group = StringProperty()


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Teal"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-parent-child.gif
    :align: center

.. MDSwitch:

MDSwitch
--------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDFloatLayout:

        MDSwitch:
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-switch.gif
    :align: center

.. Note:: Control state of :class:`~MDSwitch` same way as in
    :class:`~MDCheckbox`.
"""

__all__ = ("MDCheckbox", "MDSwitch")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    StringProperty,
)
from kivy.uix.behaviors import ToggleButtonBehavior

from kivymd import uix_path
from kivymd.uix.behaviors import CircularRippleBehavior, ScaleBehavior
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDIcon

with open(
    os.path.join(uix_path, "selectioncontrol", "selectioncontrol.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDCheckbox(
    CircularRippleBehavior,
    ScaleBehavior,
    ToggleButtonBehavior,
    MDIcon,
):
    """
    Checkbox class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.behaviors.ToggleButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """

    __allow_child_checkboxes_active = True
    __allow_root_checkbox_active = True

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
    Background icon (when using the `group` option) of the checkbox used for
    the default graphical representation when the checkbox is not pressed.

    :attr:`radio_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle-outline'`.
    """

    radio_icon_down = StringProperty("checkbox-marked-circle")
    """
    Background icon (when using the `group` option) of the checkbox used for
    the default graphical representation when the checkbox is pressed.

    :attr:`radio_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked-circle'`.
    """

    color_active = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the active state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDCheckbox:
            color_active: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-color-active.png
        :align: center

    :attr:`color_active` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_inactive = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the inactive state.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDCheckbox:
            color_inactive: "blue"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-color-inactive.png
        :align: center

    :attr:`color_inactive` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_disabled = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the disabled state.

    .. versionadded:: 2.0.0
        Use :attr:`color_disabled` instead.

    :attr:`color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Deprecated property.

    disabled_color = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the disabled state.

    .. deprecated:: 2.0.0
        Use :attr:`color_disabled` instead.

    :attr:`disabled_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selected_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the active state.

    .. deprecated:: 1.0.0
        Use :attr:`color_active` instead.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    unselected_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format when the checkbox is in the inactive state.

    .. deprecated:: 1.0.0
        Use :attr:`color_inactive` instead.

    :attr:`unselected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _current_color = ColorProperty([0.0, 0.0, 0.0, 0.0])

    def __init__(self, **kwargs):
        self.check_anim_out = Animation(
            scale_value_x=0, scale_value_y=0, duration=0.1, t="out_quad"
        )
        self.check_anim_in = Animation(
            scale_value_x=1, scale_value_y=1, duration=0.1, t="out_quad"
        )
        super().__init__(**kwargs)
        self.check_anim_out.bind(
            on_complete=lambda *x: self.check_anim_in.start(self)
        )
        self.bind(
            checkbox_icon_normal=self.update_icon,
            checkbox_icon_down=self.update_icon,
            radio_icon_normal=self.update_icon,
            radio_icon_down=self.update_icon,
            group=self.update_icon,
        )
        self.update_icon()

    def update_icon(self, *args) -> None:
        """
        Fired when the values of
        :attr:`checkbox_icon_normal` and
        :attr:`checkbox_icon_down` and
        :attr:`radio_icon_normal` and
        :attr:`group`
        change.
        """

        if self.state == "down":
            self.icon = (
                self.radio_icon_down
                if self.group and self.group not in ["root", "child"]
                else self.checkbox_icon_down
                if self.group != "root"
                else "minus-box"
            )
        else:
            self.icon = (
                self.radio_icon_normal
                if self.group and self.group not in ["root", "child"]
                else self.checkbox_icon_normal
            )

    def set_root_active(self) -> None:
        root_checkbox = self.get_widgets("root")
        if root_checkbox:
            MDCheckbox.__allow_root_checkbox_active = False
            root_checkbox[0].active = True in [
                child.active for child in self.get_widgets("child")
            ]
            MDCheckbox.__allow_root_checkbox_active = True

    def set_child_active(self, active: bool):
        for child in self.get_widgets("child"):
            child.active = active
        MDCheckbox.__allow_child_checkboxes_active = True

    def on_state(self, *args) -> None:
        """Fired when the values of :attr:`state` change."""

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

    def on_active(self, *args) -> None:
        """Fired when the values of :attr:`active` change."""

        self.state = "down" if self.active else "normal"

        if (
            self.group
            and self.group == "root"
            and MDCheckbox.__allow_root_checkbox_active
        ):
            self.set_child_active(self.active)
        elif self.group and self.group == "child":
            if MDCheckbox.__allow_child_checkboxes_active:
                self.set_root_active()

    # FIXME: https://github.com/kivymd/KivyMD/issues/1574
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if self.group and self.group == "root":
                MDCheckbox.__allow_child_checkboxes_active = False
        return super().on_touch_down(touch)

    def _release_group(self, current):
        if self.group and self.group in ["root", "child"]:
            return
        super()._release_group(current)


class ThumbIcon(MDIcon):
    """
    Implements icon for the :class:`~Thumb` widget.

    .. versionadded:: 1.0.0
    """


class Thumb(CircularRippleBehavior, MDFloatLayout):
    """Implements a thumb for the :class:`~MDSwitch` widget."""

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


class MDSwitch(StateLayerBehavior, MDFloatLayout):
    """
    Switch class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivymd.uix.floatlayout.MDFloatLayout`
    classes documentation.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the switch when
    the switch is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_effect = BooleanProperty(True)
    """
    Allows or does not allow the ripple effect when activating/deactivating
    the switch.

    .. versionadded:: 2.0.0

    :attr:`ripple_effect` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    active = BooleanProperty(False)
    """
    Indicates if the switch is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    icon_active = StringProperty()
    """
    Thumb icon when the switch is in the active state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            active: True
            icon_active: "check"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-icon-active.png
        :align: center

    :attr:`icon_active` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_inactive = StringProperty()
    """
    Thumb icon when the switch is in an inactive state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            icon_inactive: "close"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-icon-inactive.png
        :align: center

    :attr:`icon_inactive` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_active_color = ColorProperty(None)
    """
    Thumb icon color in (r, g, b, a) or string format when the switch is in the
    active state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            active: True
            icon_active: "check"
            icon_active_color: "white"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-icon-active-color.png
        :align: center

    :attr:`icon_active_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_inactive_color = ColorProperty(None)
    """
    Thumb icon color in (r, g, b, a) or string format when the switch is in an
    inactive state (only M3 style).

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            icon_inactive: "close"
            icon_inactive_color: "grey"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-icon-inactive-color.png
        :align: center

    :attr:`icon_inactive_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    thumb_color_active = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the thumb when the switch is active.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            active: True
            thumb_color_active: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-thumb-color-active.png
        :align: center

    :attr:`thumb_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    thumb_color_inactive = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the thumb when the switch is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            thumb_color_inactive: "brown"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-thumb-color-inactive.png
        :align: center

    :attr:`thumb_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    thumb_color_disabled = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the thumb when the switch is
    in the disabled state.

    .. code-block:: kv

        MDSwitch:
            active: True
            thumb_color_disabled: "brown"
            disabled: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-thumb-color-disabled.png
        :align: center

    :attr:`thumb_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_active = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is active.

    .. code-block:: kv

        MDSwitch:
            active: True
            track_color_active: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-track-color-active.png
        :align: center

    :attr:`track_color_active` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_inactive = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is inactive.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDSwitch:
            track_color_inactive: "red"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-track-color-inactive.png
        :align: center

    :attr:`track_color_inactive` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    track_color_disabled = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the track when the switch is
    in the disabled state.

    .. code-block:: kv

        MDSwitch:
            track_color_disabled: "lightgrey"
            disabled: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch-track-color-disabled.png
        :align: center

    :attr:`track_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and default to `None`.
    """

    line_color_disabled = ColorProperty(None)
    """
    The color of the outline in the disabled state

    .. versionadded:: 2.0.0

    :attr:`line_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _thumb_pos = ListProperty([0, 0])
    _line_color = ColorProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(icon_active=self.set_icon, icon_inactive=self.set_icon)
        Clock.schedule_once(lambda x: self.on_active(self, self.active))

    def set_icon(self, instance_switch, icon_value: str) -> None:
        """
        Fired when the values of
        :attr:`icon_active` and :attr:`icon_inactive` change.
        """

        def set_icon(*args):
            icon = icon_value if icon_value else "blank"
            self.ids.thumb.ids.icon.icon = icon

        Clock.schedule_once(set_icon, 0.2)

    def on_line_color(self, instance, value) -> None:
        """Fired when the values of :attr:`line_color` change."""

        if not self.disabled:
            self._line_color = value

    def on_active(self, instance_switch, active_value: bool) -> None:
        """Fired when the values of :attr:`active` change."""

        size = (
            ((dp(16), dp(16)) if not self.icon_inactive else (dp(24), dp(24)))
            if not active_value
            else (dp(24), dp(24))
        )
        icon = "blank"

        if self.icon_active and active_value:
            icon = self.icon_active
        elif self.icon_inactive and not active_value:
            icon = self.icon_inactive

        Animation(size=size, t="out_quad", d=0.2).start(self.ids.thumb)
        self.set_icon(self, icon)
        self._update_thumb_pos()

    # FIXME: If you move the cursor from the switch during the
    #  `on_touch_down` event, the animation of returning the thumb to
    #  the previous size does not work. The following code fixes this.
    def on_thumb_down(self) -> None:
        """
        Fired at the on_touch_down event of the :class:`~Thumb` object.
        Indicates the state of the switch "on/off" by an animation of
        increasing the size of the thumb.
        """

        if self.active:
            size = (dp(28), dp(28))
        else:
            size = (dp(24), dp(24))

        Animation(size=size, t="out_quad", d=0.2).start(self.ids.thumb)

    def _update_thumb_pos(self, *args, animation=True):
        if self.active:
            _thumb_pos = (
                self.width - dp(46 if self.icon_inactive else 40),
                self.height / 2 - dp(16),
            )
        else:
            _thumb_pos = (
                0 if not self.icon_inactive else dp(-14),
                self.height / 2 - dp(16),
            )
        Animation.cancel_all(self, "_thumb_pos")

        if animation:
            Animation(_thumb_pos=_thumb_pos, duration=0.2, t="out_quad").start(
                self
            )
        else:
            self._thumb_pos = _thumb_pos
