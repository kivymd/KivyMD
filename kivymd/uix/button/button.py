"""
Components/Button
=================

.. seealso::

    `Material Design spec, Buttons <https://m3.material.io/components/all-buttons>`_

.. rubric:: Buttons allow users to take actions, and make choices,
    with a single tap. When choosing the right button for an action, consider
    the level of emphasis each button type provides.

KivyMD provides the following button classes for use:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/buttons.png
    :align: center

1. Elevated button
2. Filled button
3. Filled tonal button
4. Outlined button
5. Text button
6. Icon button
7. Segmented button
8. Floating action button (FAB)
9. Extended FAB

Common buttons
==============

.. rubric:: Buttons help people take action, such as sending an email, sharing
    a document, or liking a comment.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/common-buttons.png
    :align: center

1. Elevated button
2. Filled button
3. Filled tonal button
4. Outlined button
5. Text button

Elevated_
Filled_
Tonal_
Outlined_
Text_

.. Elevated:

Elevated
--------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.surfaceColor

                MDButton:
                    style: "elevated"
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MDButtonIcon:
                        icon: "plus"

                    MDButtonText:
                        text: "Elevated"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Green"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Green"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonIcon(
                                    icon="plus",
                                ),
                                MDButtonText(
                                    text="Elevated",
                                ),
                                style="elevated",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            ),
                            md_bg_color=self.theme_cls.surfaceColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevated-button.gif
    :align: center

Common buttons can contain an icon or be without an icon:

.. code-block:: kv

    MDButton:
        style: "elevated"
        text: "Elevated"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevated-without-icon-button.png
    :align: center

.. Filled:

Filled
------

.. code-block:: kv

    MDButton:
        style: "filled"

        MDButtonText:
            text: "Filled"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/filled-button.gif
    :align: center

.. Tonal:

Tonal
-----

.. code-block:: kv

    MDButton:
        style: "tonal"

        MDButtonText:
            text: "Tonal"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tonal-button.gif
    :align: center

.. Outlined:

Outlined
--------

.. code-block:: kv

    MDButton:
        style: "outlined"

        MDButtonText:
            text: "Outlined"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/outlined-button.gif
    :align: center

.. Text:

Text
----

.. code-block:: kv

    MDButton:
        style: "text"

        MDButtonText:
            text: "Text"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/text-button.gif
    :align: center

Customization of buttons
========================

Text positioning and button size
--------------------------------

.. code-block:: kv

    MDButton:
        style: "tonal"
        theme_width: "Custom"
        height: "56dp"
        size_hint_x: .5

        MDButtonIcon:
            x: text.x - (self.width + dp(10))
            icon: "plus"

        MDButtonText:
            id: text
            text: "Tonal"
            pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/positioning-size-button.png
    :align: center

Font of the button text
-----------------------

.. code-block:: kv

    MDButton:
        style: "filled"

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Filled"
            font_style: "Title"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-style-button-text.png
    :align: center

.. code-block:: kv

    MDButton:
        style: "elevated"

        MDButtonText:
            text: "Elevated"
            theme_font_name: "Custom"
            font_name: "path/to/font.ttf"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-name-button-text.png
    :align: center

Custom button color
-------------------

.. code-block:: kv

    MDButton:
        style: "elevated"
        theme_shadow_color: "Custom"
        shadow_color: "red"

        MDButtonIcon:
            icon: "plus"
            theme_icon_color: "Custom"
            icon_color: "green"

        MDButtonText:
            text: "Elevated"
            theme_text_color: "Custom"
            text_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-color-button.png
    :align: center

Icon buttons
============

.. rubric:: Use icon buttons when a compact button is required, such as in a
    toolbar or image list. There are two types of icon buttons: standard and
    contained.

.. seealso::

    `Material Design spec, Icon buttons <https://m3.material.io/components/icon-buttons/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-buttons.png
    :align: center

1. Standard icon button
2. Contained icon button (including filled, filled tonal, and outlined styles)

StandardIcon_
FilledIcon_
TonalIcon_
OutlinedIcon_

.. StandardIcon:

StandardIcon
------------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "standard"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-standard.gif
    :align: center

.. FilledIcon:

FilledIcon
----------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "filled"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-filled.gif
    :align: center

.. TonalIcon:

TonalIcon
---------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "tonal"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-tonal.gif
    :align: center

.. OutlinedIcon:

OutlinedIcon
------------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "outlined"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-outlined.gif
    :align: center

Custom icon size
----------------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "tonal"
        theme_font_size: "Custom"
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "84dp", "84dp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-size.png
    :align: center

Custom button color
-------------------

.. code-block:: kv

    MDIconButton:
        icon: "heart-outline"
        style: "tonal"
        theme_bg_color: "Custom"
        md_bg_color: "brown"
        theme_icon_color: "Custom"
        icon_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-button-color.png
    :align: center

FAB buttons
===========

.. rubric:: The FAB represents the most important action on a screen.
    It puts key actions within reach.

.. seealso::

    `Material Design spec, FAB buttons <https://m3.material.io/components/floating-action-button/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-buttons.png
    :align: center

1. Standard FAB
2. Small FAB
3. Large FAB

There are three sizes of floating action buttons: FAB, small FAB, and large FAB:

Standard_
Small_
Large_

.. Standard:

Standard
--------

.. code-block:: kv

    MDFabButton:
        icon: "pencil-outline"
        style: "standard"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-button-standard.gif
    :align: center

.. Small:

Small
-----

.. code-block:: kv

    MDFabButton:
        icon: "pencil-outline"
        style: "small"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-button-small.png
    :align: center

.. Large:

Large
-----

.. code-block:: kv

    MDFabButton:
        icon: "pencil-outline"
        style: "large"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-button-large.gif
    :align: center

Additional color mappings
-------------------------

FABs can use other combinations of container and icon colors. The color
mappings below provide the same legibility and functionality as the default,
so the color mapping you use depends on style alone.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-color-mapping.png
    :align: center

1. Surface
2. Secondary
3. Tertiary

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFabButton

    KV = '''
    MDScreen:
        md_bg_color: app.theme_cls.surfaceColor

        MDBoxLayout:
            id: box
            adaptive_size: True
            spacing: "32dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            return Builder.load_string(KV)

        def on_start(self):
            styles = {
                "standard": "surface",
                "small": "secondary",
                "large": "tertiary",
            }
            for style in styles.keys():
                self.root.ids.box.add_widget(
                    MDFabButton(
                        style=style, icon="pencil-outline", color_map=styles[style]
                    )
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fab-button-color-mapping.png
    :align: center

Extended FAB
============

.. rubric::  Extended floating action buttons (extended FABs) help people take
    primary actions. They're wider than FABs to accommodate a text label and
    larger target area.

.. seealso::

    `Material Design spec, FAB extended buttons <https://m3.material.io/components/extended-fab/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/extended-fab-button.png
    :align: center

1. Extended FAB with both icon and label text
2. Extended FAB without icon

With icon
---------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: app.theme_cls.surfaceColor
        on_touch_down:
            if not btn.collide_point(*args[1].pos): \\
            btn.fab_state = "expand" \\
            if btn.fab_state == "collapse" else "collapse"

            MDExtendedFabButton:
                id: btn
                pos_hint: {"center_x": .5, "center_y": .5}

                MDExtendedFabButtonIcon:
                    icon: "pencil-outline"

                MDExtendedFabButtonText:
                    text: "Compose"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/extended-fab-button-icon.gif
    :align: center

Without icon
------------

.. code-block:: kv

    MDExtendedFabButton:
        fab_state: "expand"

        MDExtendedFabButtonText:
            text: "Compose"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/extended-fab-button-without-icon.png
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDFloatingActionButton:
        icon: "plus"

.. code-block:: kv

    MDRoundFlatButton:
        text: "Outlined"

.. code-block:: kv

    MDRoundFlatIconButton:
        text: "Outlined with icon"
        icon: "plus"

.. code-block:: kv

    MDFillRoundFlatButton
        text: "Filled"

.. code-block:: kv

    MDFillRoundFlatIconButton
        text: "Filled with icon"
        icon: "plus"

2.0.0 version
-------------

.. note:: `MDFloatingActionButtonSpeedDial` type buttons were removed
    in version `2.0.0`.

.. code-block:: kv

    MDFabButton:
        icon: "plus"

.. code-block:: kv

    MDButton:
        style: "outlined"

        MDButtonText:
            text: "Outlined"

.. code-block:: kv

    MDButton:
        style: "outlined"

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Outlined with icon"

.. code-block:: kv

    MDButton:
        style: "filled"

        MDButtonText:
            text: "Filled"

.. code-block:: kv

    MDButton:
        style: "filled"

        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Filled"
"""

from __future__ import annotations

__all__ = (
    "MDIconButton",
    "MDButtonText",
    "MDButtonIcon",
    "MDFabButton",
    "MDExtendedFabButton",
    "MDExtendedFabButtonIcon",
    "MDExtendedFabButtonText",
    "MDButton",
    "BaseButton",
    "BaseFabButton",
)

import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    CommonElevationBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.behaviors.motion_behavior import MotionExtendedFabButtonBehavior
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "button", "button.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseFabButton:
    """
    Implements the basic properties for the
    :class:`~MDExtendedFabButton` and :class:`~MDFabButton` classes.

    .. versionadded:: 2.0.0
    """

    elevation_levels = DictProperty(
        {
            0: 0,
            1: dp(4),
            2: dp(8),
            3: dp(12),
            4: dp(16),
            5: dp(18),
        }
    )
    """
    Elevation is measured as the distance between components along the z-axis
    in density-independent pixels (dps).

    .. versionadded:: 1.2.0

    :attr:`elevation_levels` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}`.
    """

    color_map = OptionProperty(
        "surface", options=("surface", "secondary", "tertiary")
    )
    """
    Additional color mappings.

    Available options are: 'surface', 'secondary', 'tertiary'.

    :attr:`color_map` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'secondary'`.
    """

    icon_color_disabled = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the list item when
    the widget item is disabled.

    :attr:`icon_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    style = OptionProperty("standard", options=("standard", "small", "large"))
    """
    Button type.

    Available options are: 'standard', 'small', 'large'.

    :attr:`style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'standard'`.
    """

    fab_state = OptionProperty("collapse", options=("collapse", "expand"))
    """
    The state of the button.

    Available options are: 'collapse' or 'expand'.

    :attr:`fab_state` is an :class:`~kivy.properties.OptionProperty`
    and defaults to "collapse".
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the list item when
    the list button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty(
        [
            dp(16),
        ],
        length=4,
    )
    """
    Canvas radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(16), dp(16), dp(16), dp(16)]`.
    """


class BaseButton(
    DeclarativeBehavior,
    BackgroundColorBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    ThemableBehavior,
    StateLayerBehavior,
):
    """
    Base button class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior`
    classes documentation.
    """

    elevation_levels = DictProperty(
        {
            0: 0,
            1: dp(4),
            2: dp(8),
            3: dp(12),
            4: dp(16),
            5: dp(18),
        }
    )
    """
    Elevation is measured as the distance between components along the z-axis
    in density-independent pixels (dps).

    .. versionadded:: 1.2.0

    :attr:`elevation_levels` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the button when
    the button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    shadow_radius = VariableListProperty([0, 0, 0, 0])
    """
    Button shadow radius.

    :attr:`shadow_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    md_bg_color = ColorProperty(None)
    """
    Button background color in (r, g, b, a) or string format.

    :attr:`md_bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color = ColorProperty(None)
    """
    Outlined color.

    :attr:`line_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_width = NumericProperty(1)
    """
    Line width for button border.

    :attr:`line_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    def on_press(self, *args) -> None:
        """Fired when the button is pressed."""

        self._on_press(args)

    def on_release(self, *args) -> None:
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        self._on_release(args)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y) and not self.disabled:
            return super().on_touch_down(touch)

    def finish_ripple(self):
        def reset_state(*args):
            self.dispatch("on_leave")
            self.hovering = False
            self.hover_visible = False

        super().finish_ripple()
        Clock.schedule_once(reset_state, 0.2)


class MDButton(BaseButton, CommonElevationBehavior, RelativeLayout):
    """
    Base class for all buttons.

    .. versionadded:: 2.2.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~BaseButton` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.
    """

    style = OptionProperty(
        "elevated", options=("elevated", "filled", "tonal", "outlined", "text")
    )
    """
    Button type.

    Available options are: 'filled', 'elevated', 'outlined', 'tonal', 'text'.

    :attr:`style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'elevated'`.
    """

    radius = VariableListProperty(
        [
            dp(20),
        ]
    )
    """
    Button radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(20), dp(20), dp(20), dp(20)]`.
    """

    # kivymd.uix.button.button.MDButtonIcon object.
    _button_icon = ObjectProperty()
    # kivymd.uix.button.button.MDButtonText object.
    _button_text = ObjectProperty()

    _icon_left_pad = dp(16)
    _spacing_between_icon_text = dp(10)
    _text_right_pad = dp(24)
    _text_left_pad = dp(24)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.adjust_width, 0.2)
        Clock.schedule_once(self.adjust_pos, 0.2)

    def adjust_pos(self, *args) -> None:
        """Adjusts the pos of the button according to the content."""

        if self._button_icon and self._button_text:
            self._button_text.x = (
                self._button_icon.x
                + self._spacing_between_icon_text
                + self._icon_left_pad
                + dp(2)
            )
        elif not self._button_icon and self._button_text:
            self._button_text.x = self._text_left_pad

    def adjust_width(self, *args) -> None:
        """Adjusts the width of the button according to the content."""

        if self._button_icon and self._button_text:
            if self.theme_width == "Primary":
                self.width = (
                    self._button_icon.texture_size[0]
                    + self._button_text.texture_size[0]
                    + self._icon_left_pad
                    + self._spacing_between_icon_text
                    + self._text_right_pad
                )
        elif not self._button_icon and self._button_text:
            if self.theme_width == "Primary":
                self.width = (
                    self._button_text.texture_size[0]
                    + self._text_left_pad
                    + self._text_right_pad
                )
        elif self._button_icon and not self._button_text:
            if self.theme_width == "Primary":
                self.width = (
                    dp(48)
                    + self._button_icon.texture_size[0]
                    - self._spacing_between_icon_text
                )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDButtonText):
            self._button_text = widget
            widget.bind(
                text=lambda x, y: Clock.schedule_once(self.adjust_width, 0.2)
            )
            widget._button = self
        elif isinstance(widget, MDButtonIcon):
            self._button_icon = widget
            widget._button = self
        if isinstance(widget, (MDButtonIcon, MDButtonText)):
            return super().add_widget(widget)

    def set_properties_widget(self) -> None:
        """Fired `on_release/on_press/on_enter/on_leave` events."""

        super().set_properties_widget()

        if (
            self._state == self.state_hover
            and self.focus_behavior
            or self._state == self.state_press
        ):
            self._elevation_level = (
                1
                if self.theme_elevation_level == "Primary"
                else self.elevation_level
            )
            self._shadow_softness = (
                0
                if self.theme_shadow_softness == "Primary"
                else self.shadow_softness
            )

            if not self.disabled:
                if self._state == self.state_hover and self.focus_behavior:
                    if self.style == "elevated":
                        self.elevation_level = 2
                        self.shadow_softness = 2
                elif self._state == self.state_press:
                    if self.style == "elevated":
                        self.elevation_level = 2
                        self.shadow_softness = 2
                elif not self._state:
                    if self.style == "elevated":
                        self.elevation_level = 1
                        self.shadow_softness = 0

    def on_disabled(self, instance, value) -> None:
        """Fired when the `disabled` value changes."""

        for element in (
            getattr(self, "_button_text", None),
            getattr(self, "_button_icon", None),
        ):
            if element:
                element.disabled = value

        super().on_disabled(instance, value)


class MDButtonText(MDLabel):
    """
    The class implements the text for the :class:`~MDButton` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    # kivymd.uix.button.button.MDButton object.
    _button = ObjectProperty()


class MDButtonIcon(MDIcon):
    """
    The class implements an icon for the :class:`~MDButton` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.
    """

    # kivymd.uix.button.button.MDButton object.
    _button = ObjectProperty()


class MDIconButton(RectangularRippleBehavior, ButtonBehavior, MDIcon):
    """
    Base class for icon buttons.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.label.label.MDIcon`
    classes documentation.
    """

    style = OptionProperty(
        "standard", options=("standard", "filled", "tonal", "outlined")
    )
    """
    Button type.

    .. versionadded:: 2.0.0

    Available options are: 'standard', 'filled', 'tonal', 'outlined'.

    :attr:`style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'standard'`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the list item when
    the list button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _line_color = ColorProperty(None)

    def on_line_color(self, instance, value) -> None:
        """Fired when the values of :attr:`line_color` change."""

        if not self.disabled and self.theme_line_color == "Custom":
            self._line_color = value


class MDFabButton(
    BaseFabButton,
    CommonElevationBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    MDIcon,
):
    """
    Base class for FAB buttons.

    For more information, see in the
    :class:`~BaseFabButton` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """

    def on_press(self, *args) -> None:
        """Fired when the button is pressed."""

        self._on_press(args)

    def on_release(self, *args) -> None:
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        self._on_release(args)

    def set_properties_widget(self) -> None:
        """Fired `on_release/on_press/on_enter/on_leave` events."""

        super().set_properties_widget()

        if (
            self._state == self.state_hover
            and self.focus_behavior
            or self._state == self.state_press
        ):
            self._elevation_level = (
                1
                if self.theme_elevation_level == "Primary"
                else self.elevation_level
            )
            self._shadow_softness = (
                0
                if self.theme_shadow_softness == "Primary"
                else self.shadow_softness
            )

        if not self.disabled:
            if self._state == self.state_hover and self.focus_behavior:
                self.elevation_level = 1
                self.shadow_softness = 0
            elif self._state == self.state_press:
                self.elevation_level = 2
                self.shadow_softness = 2
            elif not self._state:
                self.elevation_level = 1
                self.shadow_softness = 0


class MDExtendedFabButtonIcon(MDIcon):
    """
    Implements an icon for the :class:`~MDExtendedFabButton` class.

    .. versionadded:: 2.0.0
    """


class MDExtendedFabButtonText(MDLabel):
    """
    Implements the text for the class :class:`~MDExtendedFabButton` class.

    .. versionadded:: 2.0.0
    """


class MDExtendedFabButton(
    DeclarativeBehavior,
    ThemableBehavior,
    MotionExtendedFabButtonBehavior,
    CommonElevationBehavior,
    StateLayerBehavior,
    BaseFabButton,
    ButtonBehavior,
    RelativeLayout,
):
    """
    Base class for Extended FAB buttons.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionExtendedFabButtonBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~BaseFabButton` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.

    :Events:
        `on_collapse`
            Fired when the button is collapsed.
        `on_expand`
            Fired when the button is expanded.
    """

    elevation_levels = DictProperty(
        {
            0: 0,
            1: dp(4),
            2: dp(8),
            3: dp(12),
            4: dp(16),
            5: dp(18),
        }
    )
    """
    Elevation is measured as the distance between components along the z-axis
    in density-independent pixels (dps).

    .. versionadded:: 1.2.0

    :attr:`elevation_levels` is an :class:`~kivy.properties.DictProperty`
    and defaults to `{0: dp(0), 1: dp(4), 2: dp(8), 3: dp(12), 4: dp(16), 5: dp(18)}`.
    """

    _icon = ObjectProperty()
    _label = ObjectProperty()

    __events__ = ("on_collapse", "on_expand")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._set_text_pos, 0.5)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDExtendedFabButtonIcon):
            self._icon = widget
        elif isinstance(widget, MDExtendedFabButtonText):
            self._label = widget
            widget.opacity = 0

        return super().add_widget(widget)

    def on_collapse(self, *args):
        """Fired when the button is collapsed."""

    def on_expand(self, *args):
        """Fired when the button is expanded."""

    def on_fab_state(self, instance, state: str) -> None:
        """Fired when the :attr:`fab_state` value changes."""

        if state == "expand":
            Clock.schedule_once(self.expand)
            Clock.schedule_once(lambda x: self.dispatch("on_expand"))
        elif state == "collapse":
            Clock.schedule_once(self.collapse)
            Clock.schedule_once(lambda x: self.dispatch("on_collapse"))

    def on__x(self, instance, value) -> None:
        self._label.x = (
            self._icon.x + self._icon.texture_size[0] + dp(24) - value
        )

    def _set_text_pos(self, *args):
        if self._icon and self._label:
            self._label.x = self._icon.x + self._icon.texture_size[0] + dp(24)
        elif not self._icon and self._label:
            self._label.opacity = 1
            self.width = self._label.texture_size[0] + dp(32)
            self._label.pos_hint = {"center_x": 0.5}
