"""
Components/NavigationRail
=========================

.. versionadded:: 1.0.0

.. seealso::

    `Material Design spec, Navigation rail <https://m3.material.io/components/navigation-rail/specs>`_

.. rubric::

    Navigation rails provide access to primary destinations in apps when using
    tablet and desktop screens.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail.png
    :align: center

Usage
=====

.. code-block:: kv

    MDNavigationRail:

        MDNavigationRailItem:

        MDNavigationRailItem:

        MDNavigationRailItem:

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDBoxLayout:

                MDNavigationRail:

                    MDNavigationRailItem:
                        text: "Python"
                        icon: "language-python"

                    MDNavigationRailItem:
                        text: "JavaScript"
                        icon: "language-javascript"

                    MDNavigationRailItem:
                        text: "CPP"
                        icon: "language-cpp"

                    MDNavigationRailItem:
                        text: "Git"
                        icon: "git"

                MDScreen:
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDNavigationRail(
                                MDNavigationRailItem(
                                    text="Python",
                                    icon="language-python",
                                ),
                                MDNavigationRailItem(
                                    text="JavaScript",
                                    icon="language-javascript",
                                ),
                                MDNavigationRailItem(
                                    text="CPP",
                                    icon="language-cpp",
                                ),
                                MDNavigationRailItem(
                                    text="Git",
                                    icon="git",
                                ),
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-usage.png
    :align: center

Example
=======

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDFillRoundFlatIconButton
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen

            KV = '''
            #:import FadeTransition kivy.uix.screenmanager.FadeTransition


            <ExtendedButton>
                elevation: 3.5
                shadow_radius: 12
                shadow_softness: 4
                -height: "56dp"


            <DrawerClickableItem@MDNavigationDrawerItem>
                focus_color: "#e7e4c0"
                unfocus_color: "#fffcf4"


            MDScreen:

                MDNavigationLayout:

                    ScreenManager:

                        MDScreen:

                            MDBoxLayout:
                                orientation: "vertical"

                                MDBoxLayout:
                                    adaptive_height: True
                                    md_bg_color: "#fffcf4"
                                    padding: "12dp"

                                    MDLabel:
                                        text: "12:00"
                                        adaptive_height: True
                                        pos_hint: {"center_y": .5}

                                MDBoxLayout:

                                    MDNavigationRail:
                                        id: navigation_rail
                                        md_bg_color: "#fffcf4"
                                        selected_color_background: "#e7e4c0"
                                        ripple_color_item: "#e7e4c0"
                                        on_item_release: app.switch_screen(*args)

                                        MDNavigationRailMenuButton:
                                            on_release: nav_drawer.set_state("open")

                                        MDNavigationRailFabButton:
                                            md_bg_color: "#b0f0d6"

                                        MDNavigationRailItem:
                                            text: "Python"
                                            icon: "language-python"

                                        MDNavigationRailItem:
                                            text: "JavaScript"
                                            icon: "language-javascript"

                                        MDNavigationRailItem:
                                            text: "CPP"
                                            icon: "language-cpp"

                                        MDNavigationRailItem:
                                            text: "Swift"
                                            icon: "language-swift"

                                    ScreenManager:
                                        id: screen_manager
                                        transition:
                                            FadeTransition(duration=.2, clearcolor=app.theme_cls.bg_dark)

                MDNavigationDrawer:
                    id: nav_drawer
                    radius: (0, 16, 16, 0)
                    md_bg_color: "#fffcf4"
                    elevation: 4
                    width: "240dp"

                    MDNavigationDrawerMenu:

                        MDBoxLayout:
                            orientation: "vertical"
                            adaptive_height: True
                            spacing: "12dp"
                            padding: "3dp", 0, 0, "12dp"

                            MDIconButton:
                                icon: "menu"

                            ExtendedButton:
                                text: "Compose"
                                icon: "pencil"

                        DrawerClickableItem:
                            text: "Python"
                            icon: "language-python"

                        DrawerClickableItem:
                            text: "JavaScript"
                            icon: "language-javascript"

                        DrawerClickableItem:
                            text: "CPP"
                            icon: "language-cpp"

                        DrawerClickableItem:
                            text: "Swift"
                            icon: "language-swift"
            '''


            class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
                '''
                Implements a button of type
                `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

                .. rubric::
                    Extended FABs help people take primary actions.
                    They're wider than FABs to accommodate a text label and larger target
                    area.

                This type of buttons is not yet implemented in the standard widget set
                of the KivyMD library, so we will implement it ourselves in this class.
                '''

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.padding = "16dp"
                    Clock.schedule_once(self.set_spacing)

                def set_spacing(self, interval):
                    self.ids.box.spacing = "12dp"

                def set_radius(self, *args):
                    if self.rounded_button:
                        self._radius = self.radius = self.height / 4


            class Example(MDApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def switch_screen(
                    self, instance_navigation_rail, instance_navigation_rail_item
                ):
                    '''
                    Called when tapping on rail menu items. Switches application screens.
                    '''

                    self.root.ids.screen_manager.current = (
                        instance_navigation_rail_item.icon.split("-")[1].lower()
                    )

                def on_start(self):
                    '''Creates application screens.'''

                    navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
                    navigation_rail_items.reverse()

                    for widget in navigation_rail_items:
                        name_screen = widget.icon.split("-")[1].lower()
                        screen = MDScreen(
                            name=name_screen,
                            md_bg_color="#edd769",
                            radius=[18, 0, 0, 0],
                        )
                        box = MDBoxLayout(padding="12dp")
                        label = MDLabel(
                            text=name_screen.capitalize(),
                            font_style="H1",
                            halign="right",
                            adaptive_height=True,
                            shorten=True,
                        )
                        box.add_widget(label)
                        screen.add_widget(box)
                        self.root.ids.screen_manager.add_widget(screen)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
            from kivymd.uix.label import MDLabel
            from kivymd.uix.navigationdrawer import (
                MDNavigationDrawerItem,
                MDNavigationLayout,
                MDNavigationDrawer,
                MDNavigationDrawerMenu,
            )
            from kivymd.uix.navigationrail import (
                MDNavigationRail,
                MDNavigationRailMenuButton,
                MDNavigationRailFabButton,
                MDNavigationRailItem,
            )
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.screenmanager import MDScreenManager


            class DrawerClickableItem(MDNavigationDrawerItem):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.focus_color = "#e7e4c0"
                    self.unfocus_color = self.theme_cls.bg_light
                    self.radius = 24


            class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.padding = "16dp"
                    self.elevation = 3.5
                    self.shadow_radius = 12
                    self.shadow_softness = 4
                    self.height = dp(56)
                    Clock.schedule_once(self.set_spacing)

                def set_spacing(self, interval):
                    self.ids.box.spacing = "12dp"

                def set_radius(self, *args):
                    if self.rounded_button:
                        self._radius = self.radius = self.height / 4


            class Example(MDApp):
                def build(self):
                    self.theme_cls.material_style = "M3"
                    self.theme_cls.primary_palette = "Orange"
                    return MDScreen(
                        MDNavigationLayout(
                            MDScreenManager(
                                MDScreen(
                                    MDBoxLayout(
                                        MDBoxLayout(
                                            MDLabel(
                                                text="12:00",
                                                adaptive_height=True,
                                                pos_hint={"center_y": 0.5},
                                            ),
                                            adaptive_height=True,
                                            md_bg_color="#fffcf4",
                                            padding="12dp",
                                        ),
                                        MDBoxLayout(
                                            MDNavigationRail(
                                                MDNavigationRailMenuButton(
                                                    on_release=self.open_nav_drawer,
                                                ),
                                                MDNavigationRailFabButton(
                                                    md_bg_color="#b0f0d6",
                                                ),
                                                MDNavigationRailItem(
                                                    text="Python",
                                                    icon="language-python",
                                                ),
                                                MDNavigationRailItem(
                                                    text="JavaScript",
                                                    icon="language-javascript",
                                                ),
                                                MDNavigationRailItem(
                                                    text="CPP",
                                                    icon="language-cpp",
                                                ),
                                                MDNavigationRailItem(
                                                    text="Swift",
                                                    icon="language-swift",
                                                ),
                                                id="navigation_rail",
                                                md_bg_color="#fffcf4",
                                                selected_color_background="#e7e4c0",
                                                ripple_color_item="#e7e4c0",
                                            ),
                                            MDScreenManager(
                                                id="screen_manager_content",
                                            ),
                                            id="root_box",
                                        ),
                                        id="box_rail",
                                        orientation="vertical",
                                    ),
                                    id="box",
                                ),
                                id="screen",
                            ),
                            id="screen_manager",
                        ),
                        MDNavigationDrawer(
                            MDNavigationDrawerMenu(
                                MDBoxLayout(
                                    MDIconButton(
                                        icon="menu",
                                    ),
                                    ExtendedButton(
                                        text="Compose",
                                        icon="pencil",
                                    ),
                                    orientation="vertical",
                                    adaptive_height=True,
                                    spacing="12dp",
                                    padding=("3dp", 0, 0, "12dp"),
                                ),
                                DrawerClickableItem(
                                    text="Python",
                                    icon="language-python",
                                ),
                                DrawerClickableItem(
                                    text="JavaScript",
                                    icon="language-javascript",
                                ),
                                DrawerClickableItem(
                                    text="CPP",
                                    icon="language-cpp",
                                ),
                                DrawerClickableItem(
                                    text="Swift",
                                    icon="language-swift",
                                ),
                            ),
                            id="nav_drawer",
                            radius=(0, 16, 16, 0),
                            elevation=4,
                            width="240dp",
                        ),
                    )

                def switch_screen(self, *args, screen_manager_content=None):
                    '''
                    Called when tapping on rail menu items. Switches application screens.
                    '''

                    instance_navigation_rail, instance_navigation_rail_item = args
                    screen_manager_content.current = (
                        instance_navigation_rail_item.icon.split("-")[1].lower()
                    )

                def open_nav_drawer(self, *args):
                    self.root.ids.nav_drawer.set_state("open")

                def on_start(self):
                    '''Creates application screens.'''

                    screen_manager = self.root.ids.screen_manager
                    root_box = screen_manager.ids.screen.ids.box.ids.box_rail.ids.root_box
                    navigation_rail = root_box.ids.navigation_rail
                    screen_manager_content = root_box.ids.screen_manager_content
                    navigation_rail_items = navigation_rail.get_items()[:]
                    navigation_rail_items.reverse()
                    navigation_rail.bind(
                        on_item_release=lambda *args: self.switch_screen(
                            *args, screen_manager_content=screen_manager_content
                        )
                    )

                    for widget in navigation_rail_items:
                        name_screen = widget.icon.split("-")[1].lower()
                        screen_manager_content.add_widget(
                            MDScreen(
                                MDBoxLayout(
                                    MDLabel(
                                        text=name_screen.capitalize(),
                                        font_style="H1",
                                        halign="right",
                                        adaptive_height=True,
                                        shorten=True,
                                    ),
                                    padding="12dp",
                                ),
                                name=name_screen,
                                md_bg_color="#edd769",
                                radius=[18, 0, 0, 0],
                            ),
                        )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-example.gif
    :align: center

"""

__all__ = (
    "MDNavigationRail",
    "MDNavigationRailItem",
    "MDNavigationRailFabButton",
    "MDNavigationRailMenuButton",
)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import ScaleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.widget import MDWidget

with open(
    os.path.join(uix_path, "navigationrail", "navigationrail.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class PanelRoot(MDFloatLayout):
    """
    Contains
    :class:`~MDNavigationRailFabButton`, :class:`~MDNavigationRailMenuButton`
    buttons and a :class:`~Paneltems` container with menu items.
    """


class PanelItems(MDBoxLayout):
    """Box for menu items."""


class RippleWidget(MDWidget, ScaleBehavior):
    """
    Implements a background color for a menu item -
    (:class:`~MDNavigationRailItem`).
    """


class MDNavigationRailFabButton(MDFloatingActionButton):
    """Implements an optional floating action button (FAB)."""

    icon = StringProperty("pencil")
    """
    Button icon name.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailFabButton:
                icon: "home"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-fab-button-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'pencil'`.
    """


class MDNavigationRailMenuButton(MDIconButton):
    """Implements a menu button."""

    icon = StringProperty("menu")
    """
    Button icon name.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailMenuButton:
                icon: "home"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-menu-button-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'menu'`.
    """


class MDNavigationRailItem(ThemableBehavior, ButtonBehavior, MDBoxLayout):
    """Implements a menu item with an icon and text."""

    navigation_rail = ObjectProperty()
    """
    :class:`~MDNavigationRail` object.

    :attr:`navigation_rail` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty("checkbox-blank-circle")
    """
    Icon item.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                icon: "language-python"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-icon.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank'`.
    """

    text = StringProperty()
    """
    Text item.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-text.png
        :align: center

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon = StringProperty()
    """
    Badge icon name.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-icon.png
        :align: center

    :attr:`badge_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon_color = ColorProperty(None)
    """
    Badge icon color in (r, g, b, a) format.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_icon_color: 0, 0, 1, 1

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-icon-color.png
        :align: center

    :attr:`badge_icon_color` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    badge_bg_color = ColorProperty(None)
    """
    Badge icon background color in (r, g, b, a) format.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_bg_color: "#b0f0d6"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-bg-color.png
        :align: center

    :attr:`badge_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_font_size = NumericProperty(0)
    """
    Badge icon font size.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"
                badge_icon: "plus"
                badge_font_size: "24sp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-item-badge-font-size.png
        :align: center

    :attr:`badge_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    active = BooleanProperty(False)
    """
    Is the element active.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _selected_region_width = NumericProperty("56dp")
    _ripple_size = ListProperty([0, 0])
    _release = BooleanProperty(False)

    def on_active(
        self, instance_navigation_rail_item, value_active: bool
    ) -> None:
        """Called when the value of `active` changes."""

        self.animation_size_ripple_area(1 if value_active else 0)

    def animation_size_ripple_area(self, value: int) -> None:
        """Animates the size/fade of the ripple area."""

        Animation(
            scale_value_x=value,
            scale_value_y=value,
            scale_value_z=value,
            opacity=value,
            d=0.25,
            t=self.navigation_rail.ripple_transition,
        ).start(self.ids.ripple_widget)

    def on_press(self) -> None:
        """Called when pressed on a panel element."""

        self._release = False
        self.active = True
        self.navigation_rail.deselect_item(self)
        self.navigation_rail.dispatch("on_item_press", self)

    def on_release(self) -> None:
        """Called when released on a panel element."""

        self._release = True
        self.animation_size_ripple_area(0)
        self.navigation_rail.dispatch("on_item_release", self)


class MDNavigationRail(MDCard):
    """
    :Events:
        :attr:`on_item_press`
            Called on the `on_press` event of menu item -
            :class:`~MDNavigationRailItem`.

        :attr:`on_item_release`
            Called on the `on_release` event of menu item -
            :class:`~MDNavigationRailItem`.
    """

    radius = VariableListProperty(0, length=4)
    """
    Rail radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    padding = VariableListProperty([0, "36dp", 0, "36dp"], length=4)
    """
    Padding between layout box and children:
    [padding_left, padding_top, padding_right, padding_bottom].

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, '36dp', 0, '36dp']`.
    """

    anchor = OptionProperty("top", options=["top", "bottom", "center"])
    """
    The position of the panel with menu items.
    Available options are: `'top'`, `'bottom'`, `'center'`.

    .. rubric:: Top

    .. code-block:: kv

        MDNavigationRail:
            anchor: "top"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-anchor-top.png
        :align: center

    .. rubric:: Center

    .. code-block:: kv

        MDNavigationRail:
            anchor: "center"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-center.png
        :align: center

    .. rubric:: Bottom

    .. code-block:: kv

        MDNavigationRail:
            anchor: "bottom"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-bottom.png
        :align: center

    :attr:`anchor` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    type = OptionProperty(
        "labeled", options=["labeled", "selected", "unselected"]
    )
    """
    Type of switching menu items.
    Available options are: `'labeled'`, `'selected'`, `'unselected'`.

    .. rubric:: Labeled

    .. code-block:: kv

        MDNavigationRail:
            type: "labeled"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-labeled.png
        :align: center

    .. rubric:: Selected

    .. code-block:: kv

        MDNavigationRail:
            type: "selected"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-selected.gif
        :align: center

    .. rubric:: Unselected

    .. code-block:: kv

        MDNavigationRail:
            type: "unselected"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-type-unselected.gif
        :align: center

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'labeled'`.
    """

    text_color_item_normal = ColorProperty(None)
    """
    The text color of the normal menu item (:class:`~MDNavigationRailItem`).

    .. code-block:: kv

        MDNavigationRail:
            text_color_item_normal: app.theme_cls.primary_color

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-text-color-item-normal.png
        :align: center

    :attr:`text_color_item_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_item_active = ColorProperty(None)
    """
    The text color of the active menu item (:class:`~MDNavigationRailItem`).

    .. code-block:: kv

        MDNavigationRail:
            text_color_item_active: app.theme_cls.primary_color

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-text-color-item-active.png
        :align: center

    :attr:`text_color_item_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_item_normal = ColorProperty(None)
    """
    The icon color of the normal menu item (:class:`~MDNavigationRailItem`).

    .. code-block:: kv

        MDNavigationRail:
            icon_color_item_normal: app.theme_cls.primary_color

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-icon-color-item-normal.png
        :align: center

    :attr:`icon_color_item_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_item_active = ColorProperty(None)
    """
    The icon color of the active menu item (:class:`~MDNavigationRailItem`).

    .. code-block:: kv

        MDNavigationRail:
            icon_color_item_active: app.theme_cls.primary_color

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-icon-color-item-active.png
        :align: center

    :attr:`icon_color_item_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    selected_color_background = ColorProperty(None)
    """
    Background color which will highlight the icon of the active menu item -
    :class:`~MDNavigationRailItem` - in (r, g, b, a) format.

    .. code-block:: kv

        MDNavigationRail:
            selected_color_background: "#e7e4c0"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-selected-color-background.png
        :align: center

    :attr:`selected_color_background` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_color_item = ColorProperty(None)
    """
    Ripple effect color of menu items (:class:`~MDNavigationRailItem`)
    in (r, g, b, a) format.

    .. code-block:: kv

        MDNavigationRail:
            ripple_color_item: "#e7e4c0"

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-ripple-color-item.png
        :align: center

    :attr:`ripple_color_item` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    ripple_transition = StringProperty("out_cubic")
    """
    Type of animation of the ripple effect when a menu item is selected.

    :attr:`ripple_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'ripple_transition'`.
    """

    current_selected_item = NumericProperty(0)
    """
    Index of the menu list item (:class:`~MDNavigationRailItem`) that will be
    active by default

    .. code-block:: kv

        MDNavigationRail:
            current_selected_item: 1

            MDNavigationRailItem:
                ...

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-current-selected-item.png
        :align: center

    :attr:`current_selected_item` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    font_name = StringProperty("Roboto")
    """
    Font path for menu item (:class:`~MDNavigationRailItem`) text.

    .. code-block:: kv

        MDNavigationRail:

            MDNavigationRailItem:
                text: "Python"
                icon: "language-python"
                font_name: "nasalization-rg.ttf"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-font-name.png
        :align: center

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_pos_menu_fab_buttons)
        Clock.schedule_once(self.set_current_selected_item)
        self.register_event_type("on_item_press")
        self.register_event_type("on_item_release")

    def on_item_press(self, *args) -> None:
        """
        Called on the `on_press` event of menu item -
        :class:`~MDNavigationRailItem`.
        """

    def on_item_release(self, *args) -> None:
        """
        Called on the `on_release` event of menu item -
        :class:`~MDNavigationRailItem`.
        """

    def deselect_item(
        self, selected_navigation_rail_item: MDNavigationRailItem
    ) -> None:
        """
        Sets the `active` value to `False` for all menu items
        (:class:`~MDNavigationRailItem`) except the selected item.
        Called when a menu item is touched.
        """

        for navigation_rail_item in self.ids.box_items.children:
            if selected_navigation_rail_item is not navigation_rail_item:
                navigation_rail_item.active = False

    def get_items(self) -> list:
        """Returns a list of :class:`~MDNavigationRailItem` objects"""

        return self.ids.box_items.children

    def set_pos_panel_items(
        self,
        instance_fab_button: Union[None, MDNavigationRailFabButton],
        instance_menu_button: Union[None, MDNavigationRailFabButton],
    ) -> None:
        """Set :class:`~Paneltems` panel position with menu items."""

        if self.anchor == "top":
            if instance_fab_button:
                self.ids.box_items.y = instance_fab_button.y - (
                    len(self.ids.box_items.children) * dp(56)
                    + self.padding[1] * 2
                    + dp(24)
                )
            else:
                if not instance_menu_button:
                    self.ids.box_items.pos_hint = {"top": 1}
                else:
                    self.ids.box_items.y = instance_menu_button.y - (
                        len(self.ids.box_items.children) * dp(56)
                        + self.padding[1] * 2
                    )
        elif self.anchor == "center":
            self.ids.box_items.pos_hint = {"center_y": 0.5}
        elif self.anchor == "bottom":
            self.ids.box_items.y = dp(12)

    def set_current_selected_item(self, interval: Union[int, float]) -> None:
        """Sets the active menu list item (:class:`~MDNavigationRailItem`)."""

        if self.ids.box_items.children:
            items = self.ids.box_items.children[:]
            items.reverse()

            if len(items) <= self.current_selected_item:
                Logger.error(
                    f"MDNavigationRail:You have "
                    f"{len(self.ids.box_items.children)} menu items, but you "
                    f"set {self.current_selected_item} as the active item. "
                    f"The very first menu item will be set active."
                )
                index = 0
            else:
                index = self.current_selected_item

            items[index].dispatch("on_press")
            items[index].dispatch("on_release")

    def set_pos_menu_fab_buttons(self, interval: Union[int, float]) -> None:
        """
        Sets the position of the :class:`~MDNavigationRailFabButton` and
        :class:`~MDNavigationRailMenuButton` buttons on the panel.
        """

        fab_button = None  # MDNavigationRailFabButton
        menu_button = None  # MDNavigationRailMenuButton

        for widget in self.ids.box_buttons.children:
            if isinstance(widget, MDNavigationRailFabButton):
                fab_button = widget
            if isinstance(widget, MDNavigationRailMenuButton):
                menu_button = widget

        if fab_button and menu_button:

            def set_fab_button_y(interval):
                fab_button.y = self.parent.height - (
                    menu_button.height
                    + fab_button.height
                    + self.padding[1]
                    + dp(18)
                )
                self.set_pos_panel_items(fab_button, menu_button)

            Clock.schedule_once(set_fab_button_y)
        elif fab_button and not menu_button:

            def set_fab_button_y(interval):
                fab_button.y = self.parent.height - (
                    self.padding[1] + fab_button.height
                )
                self.set_pos_panel_items(fab_button, menu_button)

            Clock.schedule_once(set_fab_button_y)
        else:
            Clock.schedule_once(
                lambda x: self.set_pos_panel_items(fab_button, menu_button)
            )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDNavigationRailFabButton):
            self.ids.box_buttons.add_widget(widget)
        elif isinstance(widget, MDNavigationRailMenuButton):
            self.ids.box_buttons.add_widget(widget)
        elif isinstance(widget, MDNavigationRailItem):
            widget.navigation_rail = self
            self.ids.box_items.add_widget(widget)
        elif isinstance(widget, (PanelRoot, PanelItems)):
            return super().add_widget(widget)
