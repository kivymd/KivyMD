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
    FloatLayout:

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


    FloatLayout:

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
    FloatLayout:

        MDSwitch:
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-switch.gif
    :align: center

.. Note:: For :class:`~MDCheckbox` size is not required. By default it is
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
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
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
    CircularElevationBehavior,
    CircularRippleBehavior,
)
from kivymd.uix.button import MDIconButton

Builder.load_string(
    """
<MDCheckbox>:

<Thumb>
    color: 1, 1, 1, 1
    canvas:
        Color:
            rgba: self.color
        Ellipse:
            size: self.size
            pos: self.pos


<MDSwitch>:
    canvas.before:
        Color:
            rgba:
                self._track_color_disabled if self.disabled else\
                (self._track_color_active if self.active\
                else self._track_color_normal)
        RoundedRectangle:
            size: self.width - dp(8), dp(16)
            pos: self.x + dp(8), self.center_y - dp(8)
            radius: [dp(7)]

    on_release: thumb.trigger_action()

    Thumb:
        id: thumb
        size_hint: None, None
        size: dp(24), dp(24)
        pos: root.pos[0] + root._thumb_pos[0], root.pos[1] + root._thumb_pos[1]
        color:
            root.thumb_color_disabled if root.disabled else\
            (root.thumb_color_down if root.active else root.thumb_color)
        elevation: 4 if root.active else 2
        on_release: setattr(root, 'active', not root.active)
"""
)


class MDCheckbox(ToggleButtonBehavior, MDIconButton):

    # Deprecated properties ====================================================
    checkbox_icon_normal = StringProperty(None, deprecated=True)
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is not pressed.

    :attr:`checkbox_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-outline'`.

    .. warning:: Deprecated
    This property is now deprecated, use selection_normal instead.
    """
    checkbox_icon_down = StringProperty(None, deprecated=True)
    """
    Background icon of the checkbox used for the default graphical
    representation when the checkbox is pressed.

    :attr:`checkbox_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked-outline'`.

    .. warning:: Deprecated
    This property is now deprecated, use selection_normal instead.
    """
    radio_icon_normal = StringProperty(None, deprecated=True)
    """
    Background icon (when using the ``group`` option) of the checkbox used for
    the default graphical representation when the checkbox is not pressed.

    :attr:`radio_icon_normal` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle-outline'`.

    .. warning:: Deprecated
    This property is now deprecated, use selection_normal instead.
    """
    radio_icon_down = StringProperty(None, deprecated=True)
    """
    Background icon (when using the ``group`` option) of the checkbox used for
    the default graphical representation when the checkbox is pressed.

    :attr:`radio_icon_down` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-marked-circle-outline'`.

    .. warning:: Deprecated
    This property is now deprecated, use selection_normal instead.
    """
    # Active properties ========================================================
    selection_normal = StringProperty(None, allownone=False)
    """
    Selection Checkbox displayed icon, used as the indicator when the checkbox is
    not pressed.

    This value is used when the MDCheckbox is on selection mode
    (whe group is None).

    This value can either be a listed icon, or a image path.

    .. note:: unexpected Loading time.
    keep in mind that if the image is not already in memory there might be some
    delay as the interpreter loads the image in memory.
    """
    selection_down = StringProperty(None, allownone=False)
    """
    Selection Checkbox displayed icon, used as the indicator when the checkbox is
    pressed.

    This value is used when the MDCheckbox is on selection mode
    (whe group is None).

    This value can either be a listed icon, or a image path.

    .. note:: unexpected Loading time.
    keep in mind that if the image is not already in memory there might be some
    delay as the interpreter loads the image in memory.
    """
    group_normal = StringProperty(None, allownone=False)
    """
    Group Checkbox displayed icon, used as the indicator when the checkbox is
    not pressed.

    This value is used when the MDCheckbox is on group mode
    (whe group is not None).

    This value can either be a listed icon, or a image path.

    .. note:: unexpected Loading time.
    keep in mind that if the image is not already in memory there might be some
    delay as the interpreter loads the image in memory.
    """
    group_down = StringProperty(None, allownone=False)
    """
    Group Checkbox displayed icon, used as the indicator when the checkbox is
    pressed.

    This value is used when the MDCheckbox is on group mode
    (whe group is not None).

    This value can either be a listed icon, or a image path.

    .. note:: unexpected Loading time.
    keep in mind that if the image is not already in memory there might be some
    delay as the interpreter loads the image in memory.
    """
    #
    color_normal = ListProperty(None, allownone=False)
    """
    This property sets the text color when the button is not pressed.
    it only works when the `theme_color_normal` is set to `"Custom"`.

    :attr:`color_normal` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
    If you set this property inside a widget definition in kvlang or as a kwarg
    in python code, it will make the class to change `theme_color_normal` to
    `"Custom"`.

    after the new instance is created this property won't affect
    `theme_color_normal` property.
    """

    theme_color_normal = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )
    """
    This property will be set to the icon when the state of the MDCheckbox
    `state` is set to `"normal"` (`active` is `False`).

    :attr:`theme_color_normal` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
    If you don't set this property inside a widget definition in kvlang or as a kwarg
    in python code, it will be settled to "Primary"

    """

    color_down = ListProperty(None, allownone=False)
    """
    This property sets the text color when the button is pressed.
    it only works when the `theme_color_down` is set to `"Custom"`.

    :attr:`color_down` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
    If you set this property inside a widget definition in kvlang or as a kwarg
    in python code, it will make the class to change `theme_color_down` to
    `"Custom"`.

    after the new instance is created this property won't affect
    `theme_color_down` property.
    """

    theme_color_down = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )
    """
    This property will be set to the icon when the state of the MDCheckbox
    `state` is set to `"down"` (`active` is `True`).

    :attr:`theme_color_down` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
    If you don't set this property inside a widget definition in kvlang or as a kwarg
    in python code, it will be settled to "Primary_color"

    """

    disabled_color = ListProperty(None)
    """
    Disabled color in ``rgba`` format.

    :attr:`disabled_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    selected_color = ListProperty(None, deprecated=True)
    """
    Selected color in ``rgba`` format.

    :attr:`selected_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.

    .. warning:: Deprecated
    This property is now deprecated, use `color_down` instead.
    """

    unselected_color = ListProperty(None, deprecated=True)
    """
    Unelected color in ``rgba`` format.

    :attr:`unselected_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.

    .. warning:: Deprecated
    This property is now deprecated, use `color_normal` instead.
    """
    _font_size_normal = NumericProperty("24sp")
    """
    This property stores the actual size to animate the label
    and regain it's actual size once the animation has ended.

    .. warning:: Internal use Only.
    This property is intended for interla use only.
    """
    # Animations
    animate = BooleanProperty(True)
    """
    This property allows the widget to play an animation every time the Widget
    changes state.

    This is for performance purposes only.

    :attr:`animate` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    animate
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.__after_init__)

    def __after_init__(self, *dt):
        # updates icon states
        if self.selection_normal is None:
            self.selection_normal = "checkbox-blank-outline"
        if self.selection_down is None:
            self.selection_down = "checkbox-marked-outline"
        if self.group_normal is None:
            self.group_normal = "checkbox-blank-circle-outline"
        if self.group_down is None:
            self.group_down = "checkbox-marked-circle-outline"
        if self.icon is None:
            if self.active is True:
                self.icon = (
                    self.selection_down
                    if self.group is None
                    else self.group_down
                )
            else:
                self.icon = (
                    self.selection_normal
                    if self.group is None
                    else self.group_normal
                )
        # check if the developer gave a custom color input
        if self.color_normal is not None:
            self.theme_color_normal = "Custom"
        if self.color_down is not None:
            self.theme_color_down = "Custom"
        # Check if the developer gave a custom color theme
        if self.theme_color_normal is None:
            self.theme_color_normal = "Primary"
        if self.theme_color_down is None:
            self.theme_color_down = "Primary_color"
        #
        if self.disabled_text_color is None:
            self.disabled_text_color = self.theme_cls.disabled_hint_text_color
        #
        if self.active is None:
            self.active = False
        #
        self.update_state(skip=True)
        self.bind(
            state=self.update_state,
            group_normal=self.update_state,
            group_down=self.update_state,
            selection_normal=self.update_state,
            selection_down=self.update_state,
            theme_color_down=self.toggle_theme,
            theme_color_normal=self.toggle_theme,
            color_down=self.toggle_theme,
            color_normal=self.toggle_theme,
        )
        # complement
        self.bind(
            state=self.toggle_theme,
        )
        super().__after_init__(*dt)
        if self.state == "down":
            self._release_group(self)
        self.toggle_theme()
        self.Update_Container_size()

    def on_font_size(self, instance, value):
        super().on_font_size(instance, value)
        if value:
            self._font_size_normal = value

    def toggle_theme(self, *dt):
        """
        This function is in charge to update the colors and themes of the
        displayed MDIcon.
        """
        if self.state == "down":
            self.theme_icon_color = self.theme_color_down
            if self.theme_color_down == "Custom":
                self.text_color = self.color_down
        else:
            self.theme_icon_color = self.theme_color_normal
            if self.theme_color_normal == "Custom":
                self.text_color = self.color_normal

    def update_state(self, *dt, skip=False):
        """
        This funciton is in charge of updating the icon when it's needed.
        it will force the update of the icon to the respective behavior
        either be as a group icon or as a selection icon.
        """
        if self.group is None:
            self.selection_update(skip=skip)
        else:
            self.group_update(skip=skip)

    # @property
    def get_active(self):
        return True if self.state == "down" else False

    # @active.setter
    def set_active(self, value):
        if value is True:
            self.state = "down"
        elif value is False:
            self.state = "normal"
        else:
            raise ValueError(f"Active is a bool property, got {type(value)}")
        return True

    active = AliasProperty(get_active, set_active, bind=["state"], cache=True)
    """
    Indicates if the checkbox is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.AliasProperty` that acts as a
    common BooleanProperty and by default is set to `False` .
    it uses get_active as a getter and set_active as a setter.
    its binded to the ToggleButtonBehavior.state and it's cached.
    """

    def on_group(self, instance, value):
        """
        This function ensures that the toggle button group updates every time a
        button group is pressed.

        it also ensures that the icon shown inside the button is the correct
        type.
        """
        super().on_group(instance, value)
        self.update_state()

    def selection_update(self, *dt, skip=False):
        """
        This function is called uppon an state update of the button
        It will change the icon to the respective selection icon.
        """
        if self.group is None:
            if (
                self.zoom_in_animation
                and self.animate is True
                and skip is False
            ):
                self.zoom_in_animation(
                    next_icon=self.selection_down
                    if self.state == "down"
                    else self.selection_normal
                )
            else:
                if self.state == "down":
                    self.next_icon = self.selection_down
                else:
                    self.next_icon = self.selection_normal

    def group_update(self, *dt, skip=False):
        """
        This function is called uppon an state update of the button
        It will change the icon to the respective group icon.
        """
        if self.group is not None:
            if (
                self.zoom_in_animation
                and self.animate is True
                and skip is False
            ):
                self.zoom_in_animation(
                    next_icon=self.group_down
                    if self.state == "down"
                    else self.group_normal
                )
            else:
                if self.state == "down":
                    self.icon = self.group_down
                else:
                    self.icon = self.group_normal

    # Backward compatibility:
    #   This section will be removed in future versions
    # TODO remove this in nex release!

    def on_checkbox_icon_normal(self, instance, value):
        # TODO remove this in nex release!
        Logger.info(
            "checkbox_icon_normal is now a Deprecated property please use "
            "`'selection_normal'` instead."
        )
        self.selection_normal = value

    def on_checkbox_icon_down(self, instance, value):
        # TODO remove this in nex release!
        Logger.info(
            "checkbox_icon_down is now a Deprecated property please use "
            "`'selection_down'` instead."
        )
        self.selection_down = value

    def on_radio_icon_normal(self, instance, value):
        # TODO remove this in nex release!
        Logger.info(
            "radio_icon_normal is now a Deprecated property please use "
            "`'group_normal'` instead."
        )
        self.group_normal = value

    def on_radio_icon_down(self, instance, value):
        # TODO remove this in nex release!
        Logger.info(
            "radio_icon_down is now a Deprecated property please use "
            "`'group_down'` instead."
        )
        self.group_down = value

    def on_selected_color(self, instance, value):
        # TODO remove this in nex release!
        Logger.debug(
            "radio_icon_down is now a Deprecated property please use "
            "`'color_down'` instead."
        )
        self.color_down = value

    def on_unselected_color(self, instance, value):
        # TODO remove this in nex release!
        Logger.debug(
            "radio_icon_down is now a Deprecated property please use "
            "`'color_normal'` instead."
        )
        self.color_normal = value


class Thumb(
    CircularElevationBehavior, CircularRippleBehavior, ButtonBehavior, Widget
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
    """
    Get thumb color ``rgba`` format.

    :attr:`thumb_color` is an :class:`~kivy.properties.AliasProperty`
    and property is readonly.
    """

    _thumb_color_down = ListProperty([1, 1, 1, 1])

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

    _thumb_color_disabled = ListProperty(
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
        self.bind(active=self._update_thumb_pos)
        self._set_colors()
        self.size_hint = (None, None)
        self.size = (dp(36), dp(48))

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

    def _update_thumb_pos(self, *args, animation=True):
        if self.active:
            _thumb_pos = (self.width - dp(12), self.height / 2 - dp(12))
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
