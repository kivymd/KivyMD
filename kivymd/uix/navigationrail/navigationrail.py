"""
Components/NavigationRail
=========================

.. versionadded:: 1.0.0

.. seealso::

    `Material Design spec, Navigation rail <https://m3.material.io/components/navigation-rail/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail.png
    :align: center

.. rubric:: Navigation rails let people switch between UI views on mid-sized
    devices.

- Can contain 3-7 destinations plus an optional FAB
- Always put the rail in the same place, even on different screens of an app

Example
-------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.navigationrail import MDNavigationRailItem

            KV = '''
            <CommonNavigationRailItem>

                MDNavigationRailItemIcon:
                    icon: root.icon

                MDNavigationRailItemLabel:
                    text: root.text


            MDBoxLayout:

                MDNavigationRail:
                    type: "selected"

                    MDNavigationRailMenuButton:
                        icon: "menu"

                    MDNavigationRailFabButton:
                        icon: "home"

                    CommonNavigationRailItem:
                        icon: "folder-outline"
                        text: "Files"

                    CommonNavigationRailItem:
                        icon: "bookmark-outline"
                        text: "Bookmark"

                    CommonNavigationRailItem:
                        icon: "library-outline"
                        text: "Library"

                MDScreen:
                    md_bg_color: self.theme_cls.secondaryContainerColor
            '''


            class CommonNavigationRailItem(MDNavigationRailItem):
                text = StringProperty()
                icon = StringProperty()


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.navigationrail import (
                MDNavigationRailItem,
                MDNavigationRail,
                MDNavigationRailMenuButton,
                MDNavigationRailFabButton,
                MDNavigationRailItemIcon,
                MDNavigationRailItemLabel,
            )
            from kivymd.uix.screen import MDScreen


            class CommonNavigationRailItem(MDNavigationRailItem):
                text = StringProperty()
                icon = StringProperty()

                def on_icon(self, instance, value):
                    def on_icon(*ars):
                        self.add_widget(MDNavigationRailItemIcon(icon=value))
                    Clock.schedule_once(on_icon)

                def on_text(self, instance, value):
                    def on_text(*ars):
                        self.add_widget(MDNavigationRailItemLabel(text=value))
                    Clock.schedule_once(on_text)


            class Example(MDApp):
                def build(self):
                    return MDBoxLayout(
                        MDNavigationRail(
                            MDNavigationRailMenuButton(
                                icon="menu",
                            ),
                            MDNavigationRailFabButton(
                                icon="home",
                            ),
                            CommonNavigationRailItem(
                                icon="bookmark-outline",
                                text="Files",
                            ),
                            CommonNavigationRailItem(
                                icon="folder-outline",
                                text="Bookmark",
                            ),
                            CommonNavigationRailItem(
                                icon="library-outline",
                                text="Library",
                            ),
                            type="selected",
                        ),
                        MDScreen(
                            md_bg_color=self.theme_cls.secondaryContainerColor,
                        ),
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-usage.png
    :align: center

Anatomy
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDNavigationRail:

                # Optional.
                MDNavigationRailMenuButton:
                    icon: "menu"

                # Optional.
                MDNavigationRailFabButton:
                    icon: "home"

                MDNavigationRailItem

                    MDNavigationRailItemIcon:
                        icon: icon

                    MDNavigationRailItemLabel:
                        text: text

    .. tab:: Declarative Python style

        .. code-block:: python

            MDNavigationRail(
                # Optional.
                MDNavigationRailMenuButton(
                    icon="menu"
                ),
                # Optional.
                MDNavigationRailFabButton(
                    icon="home"
                ),
                MDNavigationRailItem(
                    MDNavigationRailItemIcon(
                        icon=icon
                    ),
                    MDNavigationRailItemLabel(
                        text=text
                    ),
                )
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anatomy.png
    :align: center

Anatomy item
------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDNavigationRailItem

                MDNavigationRailItemIcon:
                    icon: icon

                MDNavigationRailItemLabel:
                    text: text

    .. tab:: Declarative Python style

        .. code-block:: python

            MDNavigationRailItem(
                MDNavigationRailItemIcon(
                    icon=icon
                ),
                MDNavigationRailItemLabel(
                    text=text
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anatomy-item.png
    :align: center

Configurations
==============

Rail types
----------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type.png
    :align: center

1. Selected
2. Unselected
3. Labeled

Selected
--------

.. code-block:: kv

    MDNavigationRail:
        type: "selected"  # default

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-selected.gif
    :align: center

Unselected
----------

.. code-block:: kv

    MDNavigationRail:
        type: "unselected"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-unselected.gif
    :align: center

Labeled
-------

.. code-block:: kv

    MDNavigationRail:
        type: "labeled"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-labeled.gif
    :align: center

Rail anchored
-------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anchored.png
    :align: center

1. Top
2. Center
3. Bottom

Top
---

.. code-block:: kv

    MDNavigationRail:
        anchor: "top"

Center
------

.. code-block:: kv

    MDNavigationRail:
        anchor: "center"  # default

Bottom
------

.. code-block:: kv

    MDNavigationRail:
        anchor: "bottom"

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDNavigationRail:

        MDNavigationRailMenuButton:
            icon: "menu"

        MDNavigationRailFabButton:
            icon: "home"

        MDNavigationRailItem:
            icon: icon
            text: text

2.2.0 version
-------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDNavigationRail:

                # Optional.
                MDNavigationRailMenuButton:
                    icon: "menu"

                # Optional.
                MDNavigationRailFabButton:
                    icon: "home"

                MDNavigationRailItem

                    MDNavigationRailItemIcon:
                        icon: icon

                    MDNavigationRailItemLabel:
                        text: text

    .. tab:: Declarative Python style

        .. code-block:: python

            MDNavigationRail(
                # Optional.
                MDNavigationRailMenuButton(
                    icon="menu"
                ),
                # Optional.
                MDNavigationRailFabButton(
                    icon="home"
                ),
                MDNavigationRailItem(
                    MDNavigationRailItemIcon(
                        icon=icon
                    ),
                    MDNavigationRailItemLabel(
                        text=text
                    ),
                )
            )
"""

__all__ = (
    "MDNavigationRail",
    "MDNavigationRailItem",
    "MDNavigationRailItemIcon",
    "MDNavigationRailItemLabel",
    "MDNavigationRailFabButton",
    "MDNavigationRailMenuButton",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import (
    Color,
    Ellipse,
    RoundedRectangle,
    StencilPop,
    StencilPush,
    StencilUnUse,
    StencilUse,
)
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
    ScaleBehavior,
)
from kivymd.uix.behaviors.focus_behavior import StateFocusBehavior
from kivymd.uix.button import MDFabButton, MDIconButton
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "navigationrail", "navigationrail.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDNavigationRailFabButton(MDFabButton):
    """
    Implements a floating action button (FAB).

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDFabButton`
    class documentation.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the switch when
    the widget is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDNavigationRailMenuButton(MDIconButton):
    """
    Implements a menu button.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDIconButton` class documentation.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the switch when
    the widget is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDNavigationRailItemIcon(RectangularRippleBehavior, MDIcon):
    """
    Implements an icon for the :class:`~MDNavigationRailItem` class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.

    .. versionchanged:: 2.0.0
    """

    active_indicator_color = ColorProperty(None)
    """
    Background color of the active indicator in (r, g, b, a) or string format.

    :attr:`active_indicator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _alpha = NumericProperty(0)
    _active = BooleanProperty(False)
    _navigation_rail = ObjectProperty()
    _navigation_item = ObjectProperty()
    _layer_color = ColorProperty([0, 0, 0, 0])
    _selected_region_width = NumericProperty(dp(0))

    def anim_complete(self, *args):
        super().anim_complete()
        self._navigation_rail.set_active_item(self._navigation_item)

    def lay_canvas_instructions(self) -> None:
        if not self.ripple_effect:
            return

        canvas_rectangle = self.canvas.before.get_group(
            "navigation-rail-rounded-rectangle"
        )[0]

        with (
            self.canvas.after
            if self.ripple_canvas_after
            else self.canvas.before
        ):
            if hasattr(self, "radius"):
                self.radius = [
                    canvas_rectangle.radius[0][0],
                ]
                self._round_rad = self.radius
            StencilPush(group="rectangular_ripple_behavior")
            RoundedRectangle(
                pos=canvas_rectangle.pos,
                size=canvas_rectangle.size,
                radius=self._round_rad,
                group="rectangular_ripple_behavior",
            )
            StencilUse(group="rectangular_ripple_behavior")
            self.col_instruction = Color(
                rgba=self.ripple_color, group="rectangular_ripple_behavior"
            )
            self.ellipse = Ellipse(
                size=(self._ripple_rad, self._ripple_rad),
                pos=(
                    self.ripple_pos[0] - self._ripple_rad / 2.0,
                    self.ripple_pos[1] - self._ripple_rad / 2.0,
                ),
                group="rectangular_ripple_behavior",
            )
            StencilUnUse(group="rectangular_ripple_behavior")
            RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=self._round_rad,
                group="rectangular_ripple_behavior",
            )
            StencilPop(group="rectangular_ripple_behavior")
        self.bind(ripple_color=self._set_color, _ripple_rad=self._set_ellipse)


class MDNavigationRailItemLabel(ScaleBehavior, MDLabel):
    """
    Implements an label for the :class:`~MDNavigationRailItem` class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivymd.uix.label.label.MDLabel`
    classes documentation.

    .. versionchanged:: 2.0.0
    """

    scale_value_y = NumericProperty(0)
    """
    Y-axis value.

    :attr:`scale_value_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    _active = BooleanProperty(False)

    def on__active(self, instance, value) -> None:
        """Fired when the :attr:`_active` value changes."""

        self.text_color = (
            self.theme_cls.onSurfaceColor
            if value
            else self.theme_cls.onSurfaceVariantColor
        )


class MDNavigationRailItem(
    DeclarativeBehavior,
    ButtonBehavior,
    ThemableBehavior,
    StateFocusBehavior,
    BoxLayout,
):
    """
    Implements a menu item with an icon and text.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.focus_behavior.StateFocusBehavior`
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    active = BooleanProperty(False)
    """
    Is the element active.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    radius = VariableListProperty(0, length=4)
    """
    Item radius.

    .. versionchanged:: 2.0.0

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    _navigation_rail = ObjectProperty()
    _icon_item = ObjectProperty()

    def on_active(self, instance, value) -> None:
        """Fired when the :attr:`active` value changes."""

        if value:
            Clock.schedule_once(self.on_leave)

    def on_enter(self, *args) -> None:
        """Fired when mouse enter the bbox of the widget."""

        if not self.active:
            # FIXME: Move layer creation to
            #  kivymd/uix/behaviors/state_layer_behavior.py module.
            self._icon_item._layer_color = self.theme_cls.onSurfaceColor[
                :-1
            ] + [0.12]
            Animation(
                _selected_region_width=self._icon_item.width + dp(32),
                d=0.2,
            ).start(self._icon_item)

    def on_leave(self, *args) -> None:
        """Fired when the mouse goes outside the widget border."""

        self._icon_item._layer_color = self.theme_cls.transparentColor

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDNavigationRailItemLabel):
            Clock.schedule_once(lambda x: self._check_type_rail(widget))
        elif isinstance(widget, MDNavigationRailItemIcon):
            widget._navigation_rail = self._navigation_rail
            widget._navigation_item = self
            self._icon_item = widget
        return super().add_widget(widget)

    def _check_type_rail(self, instance: MDNavigationRailItemLabel):
        if self._navigation_rail.type == "labeled":
            instance.scale_value_y = 1


class MDNavigationRail(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    RelativeLayout,
):
    """
    Navigation rail class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.
    """

    radius = VariableListProperty(0, length=4)
    """
    Rail radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    anchor = OptionProperty("center", options=["top", "bottom", "center"])
    """
    The position of the panel with menu items.
    Available options are: `'top'`, `'bottom'`, `'center'`.

    :attr:`anchor` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    type = OptionProperty(
        "selected", options=["labeled", "selected", "unselected"]
    )
    """
    Type of switching menu items.
    Available options are: `'labeled'`, `'selected'`, `'unselected'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'labeled'`.
    """

    fab_button: MDNavigationRailFabButton = ObjectProperty()
    menu_button: MDNavigationRailFabButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._check_anchor)

    def on_size(self, *args) -> None:
        """Fired when the application screen size changes."""

        Clock.schedule_once(self._set_pos_menu_fab_buttons)
        Clock.schedule_once(self._check_anchor)

    def get_items(self) -> list:
        """Returns a list of :class:`~MDNavigationRailItem` objects."""

        return self.ids.box_items.children

    def set_active_item(self, item: MDNavigationRailItem) -> None:
        """Sets the active menu list item."""

        for widget in self.ids.box_items.children:
            if item is widget:
                widget.active = not widget.active

                for widget_item in item.children:
                    if isinstance(widget_item, MDNavigationRailItemLabel):
                        widget_item._active = widget.active
                        if self.type == "selected":
                            Animation(
                                scale_value_y=1 if widget.active else 0,
                                height=(
                                    widget_item.texture_size[1]
                                    if widget.active
                                    else 0
                                ),
                                d=0.2,
                            ).start(widget_item)
                    if isinstance(widget_item, MDNavigationRailItemIcon):
                        widget_item._active = widget.active
                        widget_item._alpha = 1 if widget.active else 0
                        widget_item._selected_region_width = 0
                        Animation(
                            _selected_region_width=(
                                widget_item.width + dp(32)
                                if widget.active
                                else 0
                            ),
                            d=0.2,
                        ).start(widget_item)
            else:
                widget.active = False
                for widget_item in widget.children:
                    widget_item._active = widget.active
                    if isinstance(widget_item, MDNavigationRailItemLabel):
                        if self.type == "selected":
                            Animation(scale_value_y=0, height=0, d=0.2).start(
                                widget_item
                            )
                    if isinstance(widget_item, MDNavigationRailItemIcon):
                        Animation(
                            _selected_region_width=0,
                            _alpha=0,
                            d=0.2,
                        ).start(widget_item)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDNavigationRailFabButton):
            self.fab_button = widget
            super().add_widget(widget)
        elif isinstance(widget, MDNavigationRailMenuButton):
            self.menu_button = widget
            super().add_widget(widget)
        elif isinstance(widget, MDNavigationRailItem):
            self.ids.box_items.add_widget(widget)
            widget._navigation_rail = self
            widget._navigation_item = widget
            widget.bind(on_release=self.set_active_item)
        else:
            return super().add_widget(widget)

    def _set_pos_menu_fab_buttons(self, *args):
        def set_pos_menu_fab_buttons(*args):
            if self.fab_button and not self.menu_button:
                self.fab_button.y = self.height - (
                    self.fab_button.height + dp(48)
                )
            elif self.menu_button and not self.fab_button:
                self.menu_button.y = self.height - (
                    self.menu_button.height + dp(38)
                )
            elif self.fab_button and self.menu_button:
                self.menu_button.y = self.height - (
                    self.menu_button.height + dp(38)
                )
                self.fab_button.y = self.height - (
                    self.fab_button.height + dp(48) + dp(48)
                )

        Clock.schedule_once(set_pos_menu_fab_buttons)

    def _check_anchor(self, *args):
        def set_top_pos(*args):
            anchor_button = None
            if (
                self.fab_button
                and not self.menu_button
                or self.fab_button
                and self.menu_button
            ):
                anchor_button = self.fab_button
            elif self.menu_button and not self.fab_button:
                anchor_button = self.menu_button

            if anchor_button:
                self.ids.box_items.y = (
                    anchor_button.y
                    - (len(self.ids.box_items.children) * dp(56))
                    - dp(56)
                )
            else:
                self.ids.box_items.y = self.height - (
                    len(self.ids.box_items.children) * dp(48)
                )

        if self.anchor == "center":
            self.ids.box_items.pos_hint = {"center_y": 0.5}
        elif self.anchor == "top":
            Clock.schedule_once(set_top_pos)
        elif self.anchor == "bottom":
            self.ids.box_items.y = dp(56)
