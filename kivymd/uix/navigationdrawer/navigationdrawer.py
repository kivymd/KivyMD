"""
Components/NavigationDrawer
===========================

.. seealso::

    `Material Design, Navigation drawer <https://m3.material.io/components/navigation-drawer/overview>`_

.. rubric:: Navigation drawers provide access to destinations in your app.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer.png
    :align: center

- Use navigation drawers in expanded layouts and modal navigation drawers in compact and medium layouts
- Can be open or closed by default
- Two types: standard and modal

When using the class :class:`~MDNavigationDrawer` skeleton of your `KV` markup
should look like this:

Usage
-----

.. code-block:: kv

    Root:

        MDNavigationLayout:

            MDScreenManager:

                Screen_1:

                Screen_2:

            MDNavigationDrawer:

                # This custom rule should implement what will be displayed in
                # your MDNavigationDrawer.
                ContentNavigationDrawer:

A simple example
----------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDNavigationLayout:

                    MDScreenManager:

                        MDScreen:

                            MDButton:
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_release: nav_drawer.set_state("toggle")

                                MDButtonText:
                                    text: "Open Drawer"

                    MDNavigationDrawer:
                        id: nav_drawer
                        radius: 0, dp(16), dp(16), 0

                        MDNavigationDrawerMenu:

                            MDNavigationDrawerLabel:
                                text: "Mail"

                            MDNavigationDrawerItem:

                                MDNavigationDrawerItemLeadingIcon:
                                    icon: "account"

                                MDNavigationDrawerItemText:
                                    text: "Inbox"

                                MDNavigationDrawerItemTrailingText:
                                    text: "24"

                            MDNavigationDrawerDivider:
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.screenmanager import MDScreenManager
            from kivymd.uix.navigationdrawer import (
                MDNavigationLayout,
                MDNavigationDrawer,
                MDNavigationDrawerMenu,
                MDNavigationDrawerLabel,
                MDNavigationDrawerItem,
                MDNavigationDrawerItemLeadingIcon,
                MDNavigationDrawerItemText,
                MDNavigationDrawerItemTrailingText,
                MDNavigationDrawerDivider,
            )
            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp


            class Example(MDApp):
                def build(self):
                    return MDScreen(
                        MDNavigationLayout(
                            MDScreenManager(
                                MDScreen(
                                    MDButton(
                                        MDButtonText(
                                            text="Open Drawer",
                                        ),
                                        on_release=lambda x: self.root.get_ids().nav_drawer.set_state(
                                            "toggle"
                                        ),
                                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    ),
                                ),
                            ),
                            MDNavigationDrawer(
                                MDNavigationDrawerMenu(
                                    MDNavigationDrawerLabel(
                                        text="Mail",
                                    ),
                                    MDNavigationDrawerItem(
                                        MDNavigationDrawerItemLeadingIcon(
                                            icon="account",
                                        ),
                                        MDNavigationDrawerItemText(
                                            text="Inbox",
                                        ),
                                        MDNavigationDrawerItemTrailingText(
                                            text="24",
                                        ),
                                    ),
                                    MDNavigationDrawerDivider(
                                    ),
                                ),
                                id="nav_drawer",
                                radius=(0, dp(16), dp(16), 0),
                            ),
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


            Example().run()

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-anatomy.png
    :align: center

.. Note:: :class:`~MDNavigationDrawer` is an empty
    :class:`~kivymd.uix.card.MDCard` panel.

Item anatomy
------------

.. code-block:: kv

    MDNavigationDrawerItem:

        MDNavigationDrawerItemLeadingIcon:
            icon: "account"

        MDNavigationDrawerItemText:
            text: "Inbox"

        MDNavigationDrawerItemTrailingText:
            text: "24"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-item-anatomy.png
    :align: center

Type drawer
===========

Standard
--------

.. code-block:: kv

    MDNavigationDrawer:
        drawer_type: "standard"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-type-standard.gif
    :align: center

Modal
-----

.. code-block:: kv

    MDNavigationDrawer:
        drawer_type: "modal"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-type-modal.gif
    :align: center

Anchoring screen edge for drawer
================================

    Left
    ----

    .. code-block:: kv

        MDNavigationDrawer:
            anchor: "left"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-ancjor-left.png
        :align: center

    Right
    -----

    .. code-block:: kv

        MDNavigationDrawer:
            anchor: "right"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-ancjor-right.png
        :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <DrawerClickableItem@MDNavigationDrawerItem>
        focus_color: "#e7e4c0"
        text_color: "#4a4939"
        icon_color: "#4a4939"
        ripple_color: "#c5bdd2"
        selected_color: "#0c6c4d"


    <DrawerLabelItem@MDNavigationDrawerItem>
        text_color: "#4a4939"
        icon_color: "#4a4939"
        focus_behavior: False
        selected_color: "#4a4939"
        _no_ripple_effect: True


    MDScreen:

        MDNavigationLayout:

            MDScreenManager:

                MDScreen:

                    MDRaisedButton:
                        text: "Open Drawer"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: nav_drawer.set_state("toggle")

            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, dp(16), dp(16), 0)

                MDNavigationDrawerMenu:

                    MDNavigationDrawerHeader:
                        title: "Header title"
                        title_color: "#4a4939"
                        text: "Header text"
                        spacing: "4dp"
                        padding: "12dp", 0, 0, "56dp"

                    MDNavigationDrawerLabel:
                        text: "Mail"

                    DrawerClickableItem:
                        icon: "gmail"
                        right_text: "+99"
                        text_right_color: "#4a4939"
                        text: "Inbox"

                    DrawerClickableItem:
                        icon: "send"
                        text: "Outbox"

                    MDNavigationDrawerDivider:

                    MDNavigationDrawerLabel:
                        text: "Labels"

                    DrawerLabelItem:
                        icon: "information-outline"
                        text: "Label"

                    DrawerLabelItem:
                        icon: "information-outline"
                        text: "Label"
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

2.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty, ColorProperty

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.navigationdrawer import (
        MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
    )

    KV = '''
    <DrawerItem>
        active_indicator_color: "#e7e4c0"

        MDNavigationDrawerItemLeadingIcon:
            icon: root.icon
            theme_icon_color: "Custom"
            icon_color: "#4a4939"

        MDNavigationDrawerItemText:
            text: root.text
            theme_text_color: "Custom"
            text_color: "#4a4939"


    <DrawerLabel>
        adaptive_height: True
        padding: "18dp", 0, 0, "12dp"

        MDNavigationDrawerItemLeadingIcon:
            icon: root.icon
            theme_icon_color: "Custom"
            icon_color: "#4a4939"
            pos_hint: {"center_y": .5}

        MDNavigationDrawerLabel:
            text: root.text
            theme_text_color: "Custom"
            text_color: "#4a4939"
            pos_hint: {"center_y": .5}
            padding: "6dp", 0, "16dp", 0
            theme_line_height: "Custom"
            line_height: 0


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDNavigationLayout:

            MDScreenManager:

                MDScreen:

                    MDButton:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: nav_drawer.set_state("toggle")

                        MDButtonText:
                            text: "Open Drawer"

            MDNavigationDrawer:
                id: nav_drawer
                radius: 0, dp(16), dp(16), 0

                MDNavigationDrawerMenu:

                    MDNavigationDrawerHeader:
                        orientation: "vertical"
                        padding: 0, 0, 0, "12dp"
                        adaptive_height: True

                        MDLabel:
                            text: "Header title"
                            theme_text_color: "Custom"
                            theme_line_height: "Custom"
                            line_height: 0
                            text_color: "#4a4939"
                            adaptive_height: True
                            padding_x: "16dp"
                            font_style: "Display"
                            role: "small"

                        MDLabel:
                            text: "Header text"
                            padding_x: "18dp"
                            adaptive_height: True
                            font_style: "Title"
                            role: "large"

                    MDNavigationDrawerDivider:

                    DrawerItem:
                        icon: "gmail"
                        text: "Inbox"
                        trailing_text: "+99"
                        trailing_text_color: "#4a4939"

                    DrawerItem:
                        icon: "send"
                        text: "Outbox"

                    MDNavigationDrawerDivider:

                    MDNavigationDrawerLabel:
                        text: "Labels"
                        padding_y: "12dp"

                    DrawerLabel:
                        icon: "information-outline"
                        text: "Label"

                    DrawerLabel:
                        icon: "information-outline"
                        text: "Label"
    '''


    class DrawerLabel(MDBoxLayout):
        icon = StringProperty()
        text = StringProperty()


    class DrawerItem(MDNavigationDrawerItem):
        icon = StringProperty()
        text = StringProperty()
        trailing_text = StringProperty()
        trailing_text_color = ColorProperty()

        _trailing_text_obj = None

        def on_trailing_text(self, instance, value):
            self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
                text=value,
                theme_text_color="Custom",
                text_color=self.trailing_text_color,
            )
            self.add_widget(self._trailing_text_obj)

        def on_trailing_text_color(self, instance, value):
            self._trailing_text_obj.text_color = value


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()
"""

__all__ = (
    "MDNavigationLayout",
    "MDNavigationDrawer",
    "MDNavigationDrawerItem",
    "MDNavigationDrawerItemLeadingIcon",
    "MDNavigationDrawerItemTrailingText",
    "MDNavigationDrawerItemText",
    "MDNavigationDrawerMenu",
    "MDNavigationDrawerHeader",
    "MDNavigationDrawerLabel",
    "MDNavigationDrawerDivider",
    "BaseNavigationDrawerItem",
)

import os

from kivy.animation import Animation, AnimationTransition
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.appbar import MDTopAppBar
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDLabel
from kivymd import uix_path
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
    MDListItemTrailingSupportingText,
)
from kivymd.uix.scrollview import MDScrollView

with open(
    os.path.join(uix_path, "navigationdrawer", "navigationdrawer.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class NavigationDrawerContentError(Exception):
    pass


class BaseNavigationDrawerItem:
    """
    Implement the base class for the menu list item.

    .. versionadded:: 2.0.0
    """

    selected = BooleanProperty(False)
    """
    Is the item selected.

    :attr:`selected` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    # kivymd.uix.navigationdrawer.MDNavigationDrawerMenu object.
    _drawer_menu = ObjectProperty()
    # kivymd.uix.navigationdrawer.MDNavigationDrawerItem object.
    _drawer_item = ObjectProperty()


class MDNavigationLayout(DeclarativeBehavior, FloatLayout):
    """
    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    classes documentation.
    """

    _scrim_color = ObjectProperty(None)
    _scrim_rectangle = ObjectProperty(None)
    _screen_manager = ObjectProperty(None)
    _navigation_drawer = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(width=self.update_pos)

    def update_pos(self, instance_navigation_drawer, pos_x: float) -> None:
        drawer = self._navigation_drawer
        manager = self._screen_manager
        if not drawer or not manager:
            return
        if drawer.drawer_type == "standard":
            manager.size_hint_x = None
            if drawer.anchor == "left":
                if (
                    self._navigation_drawer.__class__.__name__
                    != "MDBottomSheet"
                ):
                    manager.x = drawer.width + drawer.x
                    manager.width = self.width - manager.x
                else:
                    manager.width = self.width - manager.x
            else:
                manager.x = 0
                manager.width = drawer.x
        elif drawer.drawer_type == "modal":
            manager.size_hint_x = None
            manager.x = 0
            if drawer.anchor == "left":
                manager.width = self.width - manager.x
            else:
                manager.width = self.width

    def add_scrim(self, instance_manager: ScreenManager) -> None:
        with instance_manager.canvas.after:
            self._scrim_color = Color(rgba=[0, 0, 0, 0])
            self._scrim_rectangle = Rectangle(
                pos=instance_manager.pos, size=instance_manager.size
            )
            instance_manager.bind(
                pos=self.update_scrim_rectangle,
                size=self.update_scrim_rectangle,
            )

    def update_scrim_rectangle(
        self, instance_manager: ScreenManager, size: list
    ) -> None:
        self._scrim_rectangle.pos = self.pos
        self._scrim_rectangle.size = self.size

    def add_widget(self, widget, index=0, canvas=None):
        """
        Only two layouts are allowed:
        :class:`~kivy.uix.screenmanager.ScreenManager` and
        :class:`~MDNavigationDrawer`.
        """

        if not isinstance(
            widget,
            (MDNavigationDrawer, ScreenManager, MDTopAppBar),
        ):
            raise NavigationDrawerContentError(
                "The MDNavigationLayout must contain "
                "only `MDNavigationDrawer` and `ScreenManager`"
            )
        if isinstance(widget, ScreenManager):
            self._screen_manager = widget
            self.add_scrim(widget)
        if isinstance(widget, MDNavigationDrawer):
            self._navigation_drawer = widget
            widget.bind(
                x=self.update_pos, width=self.update_pos, anchor=self.update_pos
            )
        if len(self.children) > 3:
            raise NavigationDrawerContentError(
                "The MDNavigationLayout must contain "
                "only `MDNavigationDrawer` and `ScreenManager`"
            )
        return super().add_widget(widget)


class MDNavigationDrawerLabel(MDLabel):
    """
    Implements a label class.

    For more information, see in the :class:`~kivymd.uix.label.label.MDLabel`
    class documentation.

    .. versionadded:: 1.0.0
    """


class MDNavigationDrawerDivider(BoxLayout):
    """
    Implements a divider class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.

    .. versionadded:: 1.0.0
    """


class MDNavigationDrawerHeader(DeclarativeBehavior, BoxLayout):
    """
    Implements a header class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.

    .. versionadded:: 1.0.0
    """


class MDNavigationDrawerItem(
    MDListItem, FocusBehavior, BaseNavigationDrawerItem
):
    """
    Implements an item for the :class:`~MDNavigationDrawer` menu list.

    For more information, see in the
    :class:`~kivymd.uix.list.list.MDListItem` and
    :class:`~kivymd.uix.behaviors.focus_behavior.FocusBehavior` and
    :class:`~BaseNavigationDrawerItem`
    classes documentation.

    .. versionadded:: 1.0.0
    """

    active_indicator_color = ColorProperty(None)
    """
    The active indicator color in (r, g, b, a) or string format.

    .. versionadded:: 2.0.0

    :attr:`active_indicator_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    inactive_indicator_color = ColorProperty(None)
    """
    The inactive indicator color in (r, g, b, a) or string format.

    .. versionadded:: 2.0.0

    :attr:`inactive_indicator_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(
            widget,
            (
                MDNavigationDrawerItemLeadingIcon,
                MDNavigationDrawerItemText,
                MDNavigationDrawerItemTrailingText,
            ),
        ):
            widget._drawer_item = self
        return super().add_widget(widget)

    def on_release(self, *args) -> None:
        """
        Fired when the item is released
        (i.e. the touch/click that pressed the item goes away).
        """

        self.selected = not self.selected
        self._drawer_menu.update_items_color(self)


class MDNavigationDrawerItemLeadingIcon(
    MDListItemLeadingIcon, BaseNavigationDrawerItem
):
    """
    Implements the leading icon for the menu list item.

    For more information, see in the
    :class:`~kivymd.uix.list.list.MDListItemLeadingIcon` and
    :class:`~BaseNavigationDrawerItem`
    classes documentation.

    .. versionadded:: 2.0.0
    """


class MDNavigationDrawerItemText(
    MDListItemSupportingText, BaseNavigationDrawerItem
):
    """
    Implements the text for the menu list item.

    For more information, see in the
    :class:`~kivymd.uix.list.list.MDListItemSupportingText` and
    :class:`~BaseNavigationDrawerItem`
    classes documentation.

    .. versionadded:: 2.0.0
    """


class MDNavigationDrawerItemTrailingText(
    MDListItemTrailingSupportingText, BaseNavigationDrawerItem
):
    """
    Implements the supporting text for the menu list item.

    For more information, see in the
    :class:`~kivymd.uix.list.list.MDListItemTrailingSupportingText` and
    :class:`~BaseNavigationDrawerItem`
    classes documentation.

    .. versionadded:: 2.0.0
    """


class MDNavigationDrawerMenu(MDScrollView):
    """
    Implements a scrollable list for menu items of the
    :class:`~MDNavigationDrawer` class.

    For more information, see in the
    :class:`~kivymd.uix.scrollview.MDScrollView` class documentation.

    .. versionadded:: 1.0.0

    .. code-block:: kv

        MDNavigationDrawer:

            MDNavigationDrawerMenu:

                # Your menu items.
                ...
    """

    spacing = NumericProperty(0)
    """
    Spacing between children, in pixels.

    :attr:`spacing` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, GridLayout):
            return super().add_widget(widget, *args, **kwargs)
        else:
            if isinstance(widget, MDNavigationDrawerItem):
                widget._drawer_menu = self
            self.ids.menu.add_widget(widget)

    def update_items_color(self, item: MDNavigationDrawerItem) -> None:
        for widget in self.ids.menu.children:
            if issubclass(widget.__class__, MDNavigationDrawerItem):
                if widget is not item:
                    widget.md_bg_color = (
                        widget.theme_cls.surfaceContainerLowColor
                        if not widget.inactive_indicator_color
                        else widget.inactive_indicator_color
                    )
                else:
                    widget.md_bg_color = (
                        widget.theme_cls.secondaryContainerColor
                        if not widget.active_indicator_color
                        else widget.active_indicator_color
                    )


class MDNavigationDrawer(MDCard):
    """
    Navigation drawer class.

    For more information, see in the :class:`~kivymd.uix.card.card.MDCard`
    class documentation.

    :Events:

        .. versionadded:: 2.0.0

        `on_open`:
            Fired when the navigation drawer is opened.
        `on_close`:
            Fired when the navigation drawer is closed.
    """

    drawer_type = OptionProperty("modal", options=("standard", "modal"))
    """
    Type of drawer. Modal type will be on top of screen. Standard type will be
    at left or right of screen. Also it automatically disables
    :attr:`close_on_click` and :attr:`enable_swiping` to prevent closing
    drawer for standard type.

    .. versionchanged:: 2.0.0

        Rename from `type` to `drawer_type`.

    :attr:`drawer_type` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'modal'`.
    """

    anchor = OptionProperty("left", options=("left", "right"))
    """
    Anchoring screen edge for drawer. Set it to `'right'` for right-to-left
    languages. Available options are: `'left'`, `'right'`.

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'left'`.
    """

    # FIXME: Doesn't work in Kivy v2.1.0.
    scrim_color = ColorProperty([0, 0, 0, 0.5])
    """
    Color for scrim in (r, g, b, a) or string format. Alpha channel will be
    multiplied with :attr:`_scrim_alpha`. Set fourth channel to 0 if you want
    to disable scrim.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    padding = VariableListProperty([dp(16), dp(16), dp(12), dp(16)])
    """
    Padding between layout box and children: [padding_left, padding_top,
    padding_right, padding_bottom].

    Padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionchanged:: 1.0.0

    .. code-block:: kv

        MDNavigationDrawer:
            padding: "56dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer-padding.png
        :align: center

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty` and
    defaults to '[dp(16), dp(16), dp(12), dp(16)]'.
    """

    close_on_click = BooleanProperty(True)
    """
    Close when click on scrim or keyboard escape. It automatically sets to
    False for "standard" type.

    :attr:`close_on_click` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    state = OptionProperty("close", options=("close", "open"))
    """
    Indicates if panel closed or opened. Sets after :attr:`status` change.
    Available options are: `'close'`, `'open'`.

    :attr:`state` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    status = OptionProperty(
        "closed",
        options=(
            "closed",
            "opening_with_swipe",
            "opening_with_animation",
            "opened",
            "closing_with_swipe",
            "closing_with_animation",
        ),
    )
    """
    Detailed state. Sets before :attr:`state`. Bind to :attr:`state` instead
    of :attr:`status`. Available options are: `'closed'`,
    `'opening_with_swipe'`, `'opening_with_animation'`, `'opened'`,
    `'closing_with_swipe'`, `'closing_with_animation'`.

    :attr:`status` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'closed'`.
    """

    open_progress = NumericProperty(0.0)
    """
    Percent of visible part of side panel. The percent is specified as a
    floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if
    panel is opened.

    :attr:`open_progress` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    enable_swiping = BooleanProperty(True)
    """
    Allow to open or close navigation drawer with swipe. It automatically
    sets to False for "standard" type.

    :attr:`enable_swiping` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    swipe_distance = NumericProperty(10)
    """
    The distance of the swipe with which the movement of navigation drawer
    begins.

    :attr:`swipe_distance` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `10`.
    """

    swipe_edge_width = NumericProperty(20)
    """
    The size of the area in px inside which should start swipe to drag
    navigation drawer.

    :attr:`swipe_edge_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `20`.
    """

    def _get_scrim_alpha(self):
        _scrim_alpha = 0
        if self.drawer_type == "modal":
            _scrim_alpha = self._scrim_alpha_transition(self.open_progress)
        if (
            isinstance(self.parent, MDNavigationLayout)
            and self.parent._scrim_color
        ):
            self.parent._scrim_color.rgba = self.scrim_color[:3] + [
                self.scrim_color[3] * _scrim_alpha
            ]
        return _scrim_alpha

    _scrim_alpha = AliasProperty(
        _get_scrim_alpha,
        None,
        bind=("_scrim_alpha_transition", "open_progress", "scrim_color"),
    )
    """
    Multiplier for alpha channel of :attr:`scrim_color`. For internal
    usage only.
    """

    scrim_alpha_transition = StringProperty("linear")
    """
    The name of the animation transition type to use for changing
    :attr:`scrim_alpha`.

    :attr:`scrim_alpha_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    def _get_scrim_alpha_transition(self):
        return getattr(AnimationTransition, self.scrim_alpha_transition)

    _scrim_alpha_transition = AliasProperty(
        _get_scrim_alpha_transition,
        None,
        bind=("scrim_alpha_transition",),
        cache=True,
    )

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    closing_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'close'`.

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    background_color = ColorProperty(None)
    """
    The drawer background color in (r, g, b, a) or string format.

    .. versionadded:: 2.0.0

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    theme_elevation_level = "Custom"
    """
    Drawer elevation level scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_elevation_level` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Custom'`.
    """

    elevation_level = 1
    """
    Drawer elevation level (values from 0 to 5)

    .. versionadded:: 2.2.0

    :attr:`elevation_level` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `2`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        self.bind(
            open_progress=self.update_status,
            status=self.update_status,
            state=self.update_status,
        )
        Window.bind(on_keyboard=self._handle_keyboard)

    def set_properties_widget(self) -> None:
        pass

    def set_state(self, new_state="toggle", animation=True) -> None:
        """
        Change state of the side panel.
        New_state can be one of `"toggle"`, `"open"` or `"close"`.
        """

        if new_state == "toggle":
            new_state = "close" if self.state == "open" else "open"

        if new_state == "open":
            Animation.cancel_all(self, "open_progress")
            self.status = "opening_with_animation"
            if animation:
                anim = Animation(
                    open_progress=1.0,
                    d=self.opening_time * (1 - self.open_progress),
                    t=self.opening_transition,
                )
                anim.bind(on_complete=self._check_state)
                anim.start(self)
            else:
                self.open_progress = 1
        else:  # "close"
            Animation.cancel_all(self, "open_progress")
            self.status = "closing_with_animation"
            if animation:
                anim = Animation(
                    open_progress=0.0,
                    d=self.closing_time * self.open_progress,
                    t=self.closing_transition,
                )
                anim.bind(on_complete=self._check_state)
                anim.start(self)
            else:
                self.open_progress = 0

    def update_status(self, *args) -> None:
        status = self.status
        if status == "closed":
            self.state = "close"
        elif status == "opened":
            self.state = "open"
        elif self.open_progress == 1 and status == "opening_with_animation":
            self.status = "opened"
            self.state = "open"
        elif self.open_progress == 0 and status == "closing_with_animation":
            self.status = "closed"
            self.state = "close"
        elif status in (
            "opening_with_swipe",
            "opening_with_animation",
            "closing_with_swipe",
            "closing_with_animation",
        ):
            pass
        if self.status == "closed":
            self.opacity = 0
        else:
            self.opacity = 1

    def get_dist_from_side(self, x: float) -> float:
        if self.anchor == "left":
            return 0 if x < 0 else x
        return 0 if x > Window.width else Window.width - x

    def on_touch_down(self, touch):
        if self.status == "closed":
            return False
        elif self.status == "opened":
            for child in self.children[:]:
                if child.dispatch("on_touch_down", touch):
                    return True
        if self.drawer_type == "standard" and not self.collide_point(
            touch.ox, touch.oy
        ):
            return False
        return True

    def on_touch_move(self, touch):
        if self.enable_swiping:
            if self.status == "closed":
                if (
                    self.get_dist_from_side(touch.ox) <= self.swipe_edge_width
                    and abs(touch.x - touch.ox) > self.swipe_distance
                ):
                    self.status = "opening_with_swipe"
            elif self.status == "opened":
                if abs(touch.x - touch.ox) > self.swipe_distance:
                    self.status = "closing_with_swipe"

        if self.status in ("opening_with_swipe", "closing_with_swipe"):
            self.open_progress = max(
                min(
                    self.open_progress
                    + (touch.dx if self.anchor == "left" else -touch.dx)
                    / self.width,
                    1,
                ),
                0,
            )
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.status == "opening_with_swipe":
            if self.open_progress > 0.5:
                self.set_state("open", animation=True)
            else:
                self.set_state("close", animation=True)
        elif self.status == "closing_with_swipe":
            if self.open_progress < 0.5:
                self.set_state("close", animation=True)
            else:
                self.set_state("open", animation=True)
        elif self.status == "opened":
            if self.close_on_click and not self.collide_point(
                touch.ox, touch.oy
            ):
                self.set_state("close", animation=True)
            elif self.drawer_type == "standard" and not self.collide_point(
                touch.ox, touch.oy
            ):
                return False
        elif self.status == "closed":
            return False
        return True

    def on_radius(self, instance_navigation_drawer, radius_value: list) -> None:
        """Fired when the :attr:`radius` value changes."""

        self._radius = radius_value

    def on_drawer_type(
        self, instance_navigation_drawer, drawer_type: str
    ) -> None:
        """Fired when the :attr:`drawer_type` value changes."""

        if self.drawer_type == "standard":
            self.enable_swiping = False
            self.close_on_click = False
        else:
            self.enable_swiping = True
            self.close_on_click = True

    def on_open(self, *args) -> None:
        """Fired when the navigation drawer is opened."""

    def on_close(self, *args) -> None:
        """Fired when the navigation drawer is closed."""

    def _handle_keyboard(self, window, key, *largs):
        if key == 27 and self.status == "opened" and self.close_on_click:
            self.set_state("close")
            return True

    def _check_state(self, *args):
        if self.state == "open":
            self.dispatch("on_open")
        elif self.state == "close":
            self.dispatch("on_close")
