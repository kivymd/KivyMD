"""
Components/Menu
===============

.. seealso::

    `Material Design spec, Menus <https://material.io/components/menus>`_

.. rubric:: Menus display a list of choices on temporary surfaces.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-previous.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    MDScreen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-usage.gif
    :align: center

.. Warning:: Do not create the :class:`~MDDropdownMenu` object when you open
    the menu window. Because on a mobile device this one will be very slow!

Wrong
-----

.. code-block:: python

    menu = MDDropdownMenu(caller=self.screen.ids.button, items=menu_items)
    menu.open()

Customization of menu item
--------------------------

Menu items are created in the same way as items for the
:class:`~kivy.uix.recycleview.RecycleView` class.

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    <RightContentCls>
        disabled: True
        adaptive_size: True
        pos_hint: {"center_y": .5}

        MDIconButton:
            icon: root.icon
            user_font_size: "16sp"
            md_bg_color_disabled: 0, 0, 0, 0

        MDLabel:
            text: root.text
            font_style: "Caption"
            adaptive_size: True
            pos_hint: {"center_y": .5}


    <Item>

        IconLeftWidget:
            icon: root.left_icon

        RightContentCls:
            id: container
            icon: root.right_icon
            text: root.right_text


    MDScreen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class RightContentCls(IRightBodyTouch, MDBoxLayout):
        icon = StringProperty()
        text = StringProperty()


    class Item(OneLineAvatarIconListItem):
        left_icon = StringProperty()
        right_icon = StringProperty()
        right_text = StringProperty()


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "right_text": f"R+{i}",
                    "right_icon": "apple-keyboard-command",
                    "left_icon": "git",
                    "viewclass": "Item",
                    "height": dp(54),
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Test().run()


.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-right.gif
    :align: center

.. Header:
Header
------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    <MenuHeader>
        orientation: "vertical"
        adaptive_size: True
        padding: "4dp"

        MDBoxLayout:
            spacing: "12dp"
            adaptive_size: True

            MDIconButton:
                icon: "gesture-tap-button"
                pos_hint: {"center_y": .5}

            MDLabel:
                text: "Actions"
                adaptive_size: True
                pos_hint: {"center_y": .5}


    MDScreen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class MenuHeader(MDBoxLayout):
        '''An instance of the class that will be added to the menu header.'''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                header_cls=MenuHeader(),
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-header.png
    :align: center

Menu with MDTopAppBar
---------------------

The :class:`~MDDropdownMenu` works well with the standard
:class:`~kivymd.uix.toolbar.MDTopAppBar`. Since the buttons on the Toolbar are created
by the MDTopAppBar component, it is necessary to pass the button as an argument to
the callback using `lambda x: app.callback(x)`.

.. note:: This example uses drop down menus for both the righthand and
    lefthand menus (i.e both the 'triple bar' and 'triple dot' menus) to
    illustrate that it is possible. A better solution for the 'triple bar' menu
    would probably have been :class:`~kivymd.uix.MDNavigationDrawer`.


.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.uix.snackbar import Snackbar

    KV = '''
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "MDTopAppBar"
            left_action_items: [["menu", lambda x: app.callback(x)]]
            right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Test(MDApp):
        def build(self):
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "text": f"Item {i}",
                    "height": dp(56),
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                 } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                items=menu_items,
                width_mult=4,
            )
            return Builder.load_string(KV)

        def callback(self, button):
            self.menu.caller = button
            self.menu.open()

        def menu_callback(self, text_item):
            self.menu.dismiss()
            Snackbar(text=text_item).open()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-menu.gif
    :align: center

.. Position:
Position
========

Bottom position
---------------

.. seealso::

    :attr:`~MDDropdownMenu.position`

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.properties import StringProperty

    from kivymd.uix.list import OneLineIconListItem
    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    <IconListItem>

        IconLeftWidget:
            icon: root.icon


    MDScreen

        MDTextField:
            id: field
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: None
            width: "200dp"
            hint_text: "Password"
            on_focus: if self.focus: app.menu.open()
    '''


    class IconListItem(OneLineIconListItem):
        icon = StringProperty()


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "viewclass": "IconListItem",
                    "icon": "git",
                    "height": dp(56),
                    "text": f"Item {i}",
                    "on_release": lambda x=f"Item {i}": self.set_item(x),
                } for i in range(5)]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.field,
                items=menu_items,
                position="bottom",
                width_mult=4,
            )

        def set_item(self, text__item):
            self.screen.ids.field.text = text__item
            self.menu.dismiss()

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position.gif
    :align: center

Center position
---------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.properties import StringProperty

    from kivymd.uix.list import OneLineIconListItem
    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    <IconListItem>

        IconLeftWidget:
            icon: root.icon


    MDScreen

        MDDropDownItem:
            id: drop_item
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'Item 0'
            on_release: app.menu.open()
    '''


    class IconListItem(OneLineIconListItem):
        icon = StringProperty()


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "viewclass": "IconListItem",
                    "icon": "git",
                    "text": f"Item {i}",
                    "height": dp(56),
                    "on_release": lambda x=f"Item {i}": self.set_item(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.drop_item,
                items=menu_items,
                position="center",
                width_mult=4,
            )
            self.menu.bind()

        def set_item(self, text_item):
            self.screen.ids.drop_item.set_item(text_item)
            self.menu.dismiss()

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position-center.gif
    :align: center
"""

__all__ = ("MDDropdownMenu",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.window.window_sdl2 import WindowSDL
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView

import kivymd.material_resources as m_res
from kivymd import uix_path
from kivymd.theming import ThemableBehavior

with open(
    os.path.join(uix_path, "menu", "menu.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDMenu(RecycleView):
    width_mult = NumericProperty(1)
    """
    See :attr:`~MDDropdownMenu.width_mult`.
    """

    drop_cls = ObjectProperty()
    """
    See :class:`~MDDropdownMenu` class.
    """


class MDDropdownMenu(ThemableBehavior, FloatLayout):
    """
    :Events:
        `on_release`
            The method that will be called when you click menu items.
    """

    header_cls = ObjectProperty()
    """
    An instance of the class (`Kivy` or `KivyMD` widget) that will be added
    to the menu header.

    .. versionadded:: 0.104.2

    See Header_ for more information.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-header-cls.png
        :align: center

    :attr:`header_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    items = ListProperty()
    """
    See :attr:`~kivy.uix.recycleview.RecycleView.data`.

    .. code-block:: python

        items = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Item {i}",
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=items,
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-items.png
        :align: center

    :attr:`items` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_mult = NumericProperty(1)
    """
    This number multiplied by the standard increment ('56dp' on mobile, '64dp'
    on desktop), determines the width of the menu items.

    If the resulting number were to be too big for the application Window,
    the multiplier will be adjusted for the biggest possible one.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            width_mult=4,
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-width-mult-4.png
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            width_mult=8,
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-width-mult-8.png
        :align: center

    :attr:`width_mult` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    max_height = NumericProperty()
    """
    The menu will grow no bigger than this number. Set to 0 for no limit.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            max_height=dp(112),
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-max-height-112.png
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            max_height=dp(224),
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-max-height-224.png
        :align: center

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    border_margin = NumericProperty("4dp")
    """
    Margin between Window border and menu.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            border_margin=dp(4),
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-border-margin-4.png
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            border_margin=dp(24),
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-border-margin-24.png
        :align: center

    :attr:`border_margin` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `4dp`.
    """

    ver_growth = OptionProperty(None, allownone=True, options=["up", "down"])
    """
    Where the menu will grow vertically to when opening. Set to `None` to let
    the widget pick for you. Available options are: `'up'`, `'down'`.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            ver_growth="up",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-up.gif
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            ver_growth="down",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-down.gif
        :align: center

    :attr:`ver_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    hor_growth = OptionProperty(None, allownone=True, options=["left", "right"])
    """
    Where the menu will grow horizontally to when opening. Set to `None` to let
    the widget pick for you. Available options are: `'left'`, `'right'`.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            hor_growth="left",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-left.gif
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            hor_growth="right",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-right.gif
        :align: center

    :attr:`hor_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None)
    """
    Color of the background of the menu.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            background_color=self.theme_cls.primary_light,
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-background-color.png
        :align: center

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    opening_transition = StringProperty("out_cubic")
    """
    Type of animation for opening a menu window.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.2)
    """
    Menu window opening animation time and you can set it to 0
    if you don't want animation of menu opening.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    caller = ObjectProperty()
    """
    The widget object that calls the menu window.

    :attr:`caller` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    position = OptionProperty(
        "auto", options=["top", "auto", "center", "bottom"]
    )
    """
    Menu window position relative to parent element.
    Available options are: `'auto'`, `'center'`, `'bottom'`.

    See Position_ for more information.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position.png
        :align: center

    :attr:`position` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'auto'`.
    """

    radius = VariableListProperty([dp(7)])
    """
    Menu radius.

    .. code-block:: python

        self.menu = MDDropdownMenu(
            radius=[24, 0, 24, 0],
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-radius.png
        :align: center

    :attr:`radius` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `'[dp(7)]'`.
    """

    elevation = NumericProperty(4)
    """
    Elevation value of menu dialog.

    .. versionadded:: 1.0.0

    .. code-block:: python

        self.menu = MDDropdownMenu(
            elevation=4,
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-elevation.png
        :align: center

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `4`.
    """

    _start_coords = []
    _calculate_complete = False
    _calculate_process = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.check_position_caller)
        Window.bind(on_maximize=self.set_menu_properties)
        Window.bind(on_restore=self.set_menu_properties)
        Clock.schedule_once(self.ajust_radius)
        self.register_event_type("on_dismiss")
        self.menu = self.ids.md_menu
        self.target_height = 0

    def check_position_caller(
        self, instance_window: WindowSDL, width: int, height: int
    ) -> None:
        """Called when the application root window is resized."""

        # FIXME: Menu position is not recalculated when changing the size of
        #  the root application window.
        self.set_menu_properties(0)

    def set_menu_properties(self, interval: Union[int, float] = 0) -> None:
        """Sets the size and position for the menu window."""

        if self.caller:
            self.ids.md_menu.data = self.items
            # We need to pick a starting point, see how big we need to be,
            # and where to grow to.
            self._start_coords = self.caller.to_window(
                self.caller.center_x, self.caller.center_y
            )
            self.target_width = self.width_mult * m_res.STANDARD_INCREMENT

            # If we're wider than the Window...
            if self.target_width > Window.width:
                # ...reduce our multiplier to max allowed.
                self.target_width = (
                    int(Window.width / m_res.STANDARD_INCREMENT)
                    * m_res.STANDARD_INCREMENT
                )

            # Set the target_height of the menu depending on the size of
            # each MDMenuItem or MDMenuItemIcon.
            self.target_height = 0
            for item in self.ids.md_menu.data:
                self.target_height += item.get("height", dp(72))

            # If we're over max_height...
            if 0 < self.max_height < self.target_height:
                self.target_height = self.max_height

            # Establish vertical growth direction.
            if self.ver_growth is not None:
                ver_growth = self.ver_growth
            else:
                # If there's enough space below us:
                if (
                    self.target_height
                    <= self._start_coords[1] - self.border_margin
                ):
                    ver_growth = "down"
                # if there's enough space above us:
                elif (
                    self.target_height
                    < Window.height - self._start_coords[1] - self.border_margin
                ):
                    ver_growth = "up"
                # Otherwise, let's pick the one with more space and adjust
                # ourselves.
                else:
                    # If there"s more space below us:
                    if (
                        self._start_coords[1]
                        >= Window.height - self._start_coords[1]
                    ):
                        ver_growth = "down"
                        self.target_height = (
                            self._start_coords[1] - self.border_margin
                        )
                    # If there's more space above us:
                    else:
                        ver_growth = "up"
                        self.target_height = (
                            Window.height
                            - self._start_coords[1]
                            - self.border_margin
                        )

            if self.hor_growth is not None:
                hor_growth = self.hor_growth
            else:
                # If there's enough space to the right:
                if (
                    self.target_width
                    <= Window.width - self._start_coords[0] - self.border_margin
                ):
                    hor_growth = "right"
                # if there's enough space to the left:
                elif (
                    self.target_width
                    < self._start_coords[0] - self.border_margin
                ):
                    hor_growth = "left"
                # Otherwise, let's pick the one with more space and adjust
                # ourselves.
                else:
                    # if there"s more space to the right:
                    if (
                        Window.width - self._start_coords[0]
                        >= self._start_coords[0]
                    ):
                        hor_growth = "right"
                        self.target_width = (
                            Window.width
                            - self._start_coords[0]
                            - self.border_margin
                        )
                    # if there"s more space to the left:
                    else:
                        hor_growth = "left"
                        self.target_width = (
                            self._start_coords[0] - self.border_margin
                        )

            if ver_growth == "down":
                self.tar_y = self._start_coords[1] - self.target_height
            else:  # should always be "up"
                self.tar_y = self._start_coords[1]

            if hor_growth == "right":
                self.tar_x = self._start_coords[0]
            else:  # should always be "left"
                self.tar_x = self._start_coords[0] - self.target_width
            self._calculate_complete = True

    def ajust_radius(self, interval: Union[int, float]) -> None:
        """
        Adjusts the radius of the first and last items in the menu list
        according to the radius that is set for the menu.
        """

        if self.items:
            radius_for_firt_item = self.radius[:2]
            radius_for_last_item = self.radius[2:]

            firt_data_item = self.items[0]
            last_data_item = self.items[-1]

            firt_data_item["radius"] = radius_for_firt_item + [0, 0]
            last_data_item["radius"] = [0, 0] + radius_for_last_item
            last_data_item["divider"] = None

            self.items[0] = firt_data_item
            self.items[-1] = last_data_item

            # For all other elements of the list, except for the first and
            # last, we set the value of the radius to `0`.
            for i, data_item in enumerate(self.items):
                if "radius" not in data_item:
                    data_item["radius"] = 0
                    self.items[i] = data_item

    def adjust_position(self) -> str:
        """
        Returns value 'auto' for the menu position if the menu position is out
        of screen.
        """

        target_width = self.target_width
        target_height = self.target_height
        caller = self.caller
        position = self.position

        if (
            caller.x < target_width
            or caller.x + target_width > Window.width
            or caller.y + target_height > Window.height
            or (caller.y < target_height and position == "center")
        ):
            position = "auto"
            if self.hor_growth or self.ver_growth:
                self.hor_growth = None
                self.ver_growth = None
                self.set_menu_properties()
        return position

    def open(self) -> None:
        """Animate the opening of a menu window."""

        def open(interval):
            if not self._calculate_complete:
                return

            position = self.adjust_position()

            if position == "auto":
                self.menu.pos = self._start_coords
                anim = Animation(
                    x=self.tar_x,
                    y=self.tar_y
                    - (self.header_cls.height if self.header_cls else 0),
                    width=self.target_width,
                    height=self.target_height,
                    duration=self.opening_time,
                    opacity=1,
                    transition=self.opening_transition,
                )
                anim.start(self.menu)
            else:
                if position == "center":
                    self.menu.pos = (
                        self._start_coords[0] - self.target_width / 2,
                        self._start_coords[1] - self.target_height / 2,
                    )
                elif position == "bottom":
                    self.menu.pos = (
                        self._start_coords[0] - self.target_width / 2,
                        self.caller.pos[1] - self.target_height,
                    )
                elif position == "top":
                    self.menu.pos = (
                        self._start_coords[0] - self.target_width / 2,
                        self.caller.pos[1] + self.caller.height,
                    )
                anim = Animation(
                    width=self.target_width,
                    height=self.target_height,
                    duration=self.opening_time,
                    opacity=1,
                    transition=self.opening_transition,
                )
            anim.start(self.menu)
            Window.add_widget(self)
            Clock.unschedule(open)
            self._calculate_process = False

        self.set_menu_properties()
        if not self._calculate_process:
            self._calculate_process = True
            Clock.schedule_interval(open, 0)

    def on_header_cls(
        self, instance_dropdown_menu, instance_user_menu_header
    ) -> None:
        """Called when a value is set to the :attr:`header_cls` parameter."""

        def add_content_header_cls(interval):
            self.ids.content_header.clear_widgets()
            self.ids.content_header.add_widget(instance_user_menu_header)

        Clock.schedule_once(add_content_header_cls, 1)

    def on_touch_down(self, touch):
        if not self.menu.collide_point(*touch.pos):
            self.dispatch("on_dismiss")
            return True
        super().on_touch_down(touch)
        return True

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        return True

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        return True

    def on_dismiss(self) -> None:
        """Called when the menu is closed."""

        Window.remove_widget(self)
        self.menu.width = 0
        self.menu.height = 0
        self.menu.opacity = 0

    def dismiss(self, *args) -> None:
        """Closes the menu."""

        self.on_dismiss()


if __name__ == "__main__":
    # To test the correct menu position.
    from kivy.lang import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.button import MDRaisedButton
    from kivymd.uix.screen import MDScreen

    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = MDScreen()
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Item {i}",
                }
                for i in range(5)
            ]
            self.menu = MDDropdownMenu(items=menu_items, width_mult=4)

        def open_menu(self, caller):
            self.menu.caller = caller
            self.menu.open()

        def on_start(self):
            pos_hints = [
                {"top": 1, "left": 0.1},
                {"top": 1, "center_x": 0.5},
                {"top": 1, "right": 1},
                {"center_y": 0.5, "left": 1},
                {"bottom": 1, "left": 1},
                {"bottom": 1, "center_x": 0.5},
                {"bottom": 1, "right": 1},
                {"center_y": 0.5, "right": 1},
                {"center_y": 0.5, "center_x": 0.5},
            ]
            for pos_hint in pos_hints:
                self.screen.add_widget(
                    MDRaisedButton(pos_hint=pos_hint, on_release=self.open_menu)
                )

        def build(self):
            return self.screen

    Test().run()
