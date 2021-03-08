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
    Screen:

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
            menu_items = [{"text": f"Item {i}"} for i in range(5)]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
            )
            self.menu.bind(on_release=self.menu_callback)

        def menu_callback(self, instance_menu, instance_menu_item):
            print(instance_menu, instance_menu_item)

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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-wrong.gif
    :align: center

Customization of menu item
--------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-right.gif
    :align: center

You must create a new class that inherits from the :class:`~RightContent` class:

.. code-block:: python

    class RightContentCls(RightContent):
        pass

Now in the KV rule you can create your own elements that will be displayed in
the menu item on the right:

.. code-block:: kv

    <RightContentCls>
        disabled: True

        MDIconButton:
            icon: root.icon
            user_font_size: "16sp"
            pos_hint: {"center_y": .5}

        MDLabel:
            text: root.text
            font_style: "Caption"
            size_hint_x: None
            width: self.texture_size[0]
            text_size: None, None

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-right-detail.png
    :align: center

Now create menu items as usual, but add the key ``right_content_cls`` whose
value is the class ``RightContentCls`` that you created:

.. code-block:: python

    menu_items = [
        {
            "right_content_cls": RightContentCls(
                text=f"R+{i}", icon="apple-keyboard-command",
            ),
            "icon": "git",
            "text": f"Item {i}",
        }
        for i in range(5)
    ]
    self.menu = MDDropdownMenu(
        caller=self.screen.ids.button, items=menu_items, width_mult=4
    )

Full example
------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu, RightContent

    KV = '''
    <RightContentCls>
        disabled: True

        MDIconButton:
            icon: root.icon
            user_font_size: "16sp"
            pos_hint: {"center_y": .5}

        MDLabel:
            text: root.text
            font_style: "Caption"
            size_hint_x: None
            width: self.texture_size[0]
            text_size: None, None


    Screen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class RightContentCls(RightContent):
        pass


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "right_content_cls": RightContentCls(
                        text=f"R+{i}", icon="apple-keyboard-command",
                    ),
                    "icon": "git",
                    "text": f"Item {i}",
                }
                for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button, items=menu_items, width_mult=4
            )
            self.menu.bind(on_release=self.menu_callback)

        def menu_callback(self, instance_menu, instance_menu_item):
            instance_menu.dismiss()

        def build(self):
            return self.screen


    Test().run()

Menu without icons on the left
------------------------------

If you do not want to use the icons in the menu items on the left,
then do not use the "icon" key when creating menu items:

.. code-block:: python

        menu_items = [
            {
                "right_content_cls": RightContentCls(
                    text=f"R+{i}", icon="apple-keyboard-command",
                ),
                "text": f"Item {i}",
            }
            for i in range(5)
        ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-without-icon.png
    :align: center

Item height adjustment
----------------------

.. code-block:: python

        menu_items = [
            {
                "right_content_cls": RightContentCls(
                    text=f"R+{i}", icon="apple-keyboard-command",
                ),
                "text": f"Item {i}",
                "height": "36dp",
                "top_pad": "10dp",
                "bot_pad": "10dp",
            }
            for i in range(5)
        ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-pad.png
    :align: center

Mixin items
-----------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu, RightContent

    KV = '''
    <RightContentCls>
        disabled: True

        MDIconButton:
            icon: root.icon
            user_font_size: "16sp"
            pos_hint: {"center_y": .5}

        MDLabel:
            text: root.text
            font_style: "Caption"
            size_hint_x: None
            width: self.texture_size[0]
            text_size: None, None


    Screen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class RightContentCls(RightContent):
        pass


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)

            menu_items = []
            data = [
                {"": "Open"},
                {},
                {"open-in-app": "Open in app >"},
                {"trash-can-outline": "Move to Trash"},
                {"rename-box": "Rename"},
                {"zip-box-outline": "Create zip"},
                {},
                {"": "Properties"},
            ]

            for data_item in data:
                if data_item:
                    if list(data_item.items())[0][1].endswith(">"):
                        menu_items.append(
                            {
                                "right_content_cls": RightContentCls(
                                    icon="menu-right-outline",
                                ),
                                "icon": list(data_item.items())[0][0],
                                "text": list(data_item.items())[0][1][:-2],
                                "height": "36dp",
                                "top_pad": "10dp",
                                "bot_pad": "10dp",
                                "divider": None,
                            }
                        )
                    else:
                        menu_items.append(
                            {
                                "text": list(data_item.items())[0][1],
                                "icon": list(data_item.items())[0][0],
                                "font_style": "Caption",
                                "height": "36dp",
                                "top_pad": "10dp",
                                "bot_pad": "10dp",
                                "divider": None,
                            }
                        )
                else:
                    menu_items.append(
                        {"viewclass": "MDSeparator", "height": 1}
                    )
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
            )
            self.menu.bind(on_release=self.menu_callback)

        def menu_callback(self, instance_menu, instance_menu_item):
            print(instance_menu, instance_menu_item


        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-mixin.png
    :align: center

Hover Behavior
--------------

.. code-block:: python

    self.menu = MDDropdownMenu(
        ...,
        ...,
        selected_color=self.theme_cls.primary_dark_hue,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-with-hover.gif
    :align: center

Create submenu
--------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    Screen:

        MDRaisedButton:
            id: button
            text: "PRESS ME"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.menu.open()
    '''


    class CustomDrop(MDDropdownMenu):
        def set_bg_color_items(self, instance_selected_item):
            if self.selected_color and not MDApp.get_running_app().submenu:
                for item in self.menu.ids.box.children:
                    if item is not instance_selected_item:
                        item.bg_color = (0, 0, 0, 0)
                    else:
                        instance_selected_item.bg_color = self.selected_color


    class Test(MDApp):
        submenu = None

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "icon": "git",
                    "text": f"Item {i}" if i != 3 else "Open submenu",
                }
                for i in range(5)
            ]
            self.menu = CustomDrop(
                caller=self.screen.ids.button,
                items=menu_items,
                width_mult=4,
                selected_color=self.theme_cls.bg_darkest
            )
            self.menu.bind(on_enter=self.check_item)

        def check_item(self, menu, item):
            if item.text == "Open submenu" and not self.submenu:
                menu_items = [{"text": f"Item {i}"} for i in range(5)]
                self.submenu = MDDropdownMenu(
                    caller=item,
                    items=menu_items,
                    width_mult=4,
                    selected_color=self.theme_cls.bg_darkest,
                )
                self.submenu.bind(on_dismiss=self.set_state_submenu)
                self.submenu.open()

        def set_state_submenu(self, *args):
            self.submenu = None

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-submenu.gif
    :align: center

Menu with MDToolbar
-------------------

The :class:`~MDDropdownMenu` works well with the standard
:class:`~kivymd.uix.toolbar.MDToolbar`. Since the buttons on the Toolbar are created
by the MDToolbar component, it is necessary to pass the button as an argument to
the callback using `lambda x: app.callback(x)`.

.. note::

    This example uses drop down menus for both the righthand and lefthand menus (i.e
    both the 'triple bar' and 'triple dot' menus) to illustrate that it is possible.
    A better solution for the 'triple bar' menu would probably have been
    :class:`~kivymd.uix.MDNavigationDrawer`.


.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.uix.snackbar import Snackbar

    KV = '''
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDToolbar"
            left_action_items: [["menu", lambda x: app.callback(x)]]
            right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

        MDLabel:
            text: "Content"
            halign: "center"
    '''


    class Test(MDApp):
        def build(self):
            menu_items = [{"text": f"Item {i}"} for i in range(5)]
            self.menu = MDDropdownMenu(
                items=menu_items,
                width_mult=4,
            )
            self.menu.bind(on_release=self.menu_callback)
            return Builder.load_string(KV)

        def callback(self, button):
            self.menu.caller = button
            self.menu.open()

        def menu_callback(self, menu, item):
            self.menu.dismiss()
            Snackbar(text=item.text).open()

    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-menu.gif
    :align: center

Position menu
=============

Bottom position
---------------

.. seealso::

    :attr:`~MDDropdownMenu.position`

.. code-block:: python

    from kivy.clock import Clock
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    Screen

        MDTextField:
            id: field
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint_x: None
            width: "200dp"
            hint_text: "Password"
            on_focus: if self.focus: app.menu.open()
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.field,
                items=menu_items,
                position="bottom",
                width_mult=4,
            )
            self.menu.bind(on_release=self.set_item)

        def set_item(self, instance_menu, instance_menu_item):
            def set_item(interval):
                self.screen.ids.field.text = instance_menu_item.text
                instance_menu.dismiss()
            Clock.schedule_once(set_item, 0.5)

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position.gif
    :align: center

Center position
---------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    Screen

        MDDropDownItem:
            id: drop_item
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'Item 0'
            on_release: app.menu.open()
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.drop_item,
                items=menu_items,
                position="center",
                width_mult=4,
            )
            self.menu.bind(on_release=self.set_item)

        def set_item(self, instance_menu, instance_menu_item):
            self.screen.ids.drop_item.set_item(instance_menu_item.text)
            self.menu.dismiss()

        def build(self):
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position-center.gif
    :align: center
"""

__all__ = ("MDDropdownMenu", "RightContent")

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

import kivymd.material_resources as m_res
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import FakeRectangularElevationBehavior, HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    IRightBodyTouch,
    OneLineAvatarIconListItem,
    OneLineListItem,
    OneLineRightIconListItem,
)

Builder.load_string(
    """
#:import STD_INC kivymd.material_resources.STANDARD_INCREMENT


<RightContent>
    adaptive_width: True


<MDMenuItemIcon>

    IconLeftWidget:
        id: icon_widget
        icon: root.icon


<MDMenu>
    size_hint: None, None
    width: root.width_mult * STD_INC
    bar_width: 0

    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True


<MDDropdownMenu>

    DropdownMenuFakeCard:
        id: card
        elevation: 10
        size_hint: None, None
        size: md_menu.size
        pos: md_menu.pos
        opacity: md_menu.opacity
        radius: root.radius
        md_bg_color: root.background_color if root.background_color else root.theme_cls.bg_dark

        MDMenu:
            id: md_menu
            drop_cls: root
            width_mult: root.width_mult
            size_hint: None, None
            size: 0, 0
            opacity: 0
"""
)


class DropdownMenuFakeCard(MDCard, FakeRectangularElevationBehavior):
    pass


class RightContent(IRightBodyTouch, MDBoxLayout):
    text = StringProperty()
    """
    Text item.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty()
    """
    Icon item.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """


class MDMenuItemBase(HoverBehavior):
    """
    Base class for MenuItem
    """

    def on_enter(self):
        self.parent.parent.drop_cls.set_bg_color_items(self)
        self.parent.parent.drop_cls.dispatch("on_enter", self)

    def on_leave(self):
        self.parent.parent.drop_cls.dispatch("on_leave", self)


class MDMenuItemIcon(MDMenuItemBase, OneLineAvatarIconListItem):
    icon = StringProperty()
    """
    Icon item.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """


class MDMenuItem(MDMenuItemBase, OneLineListItem):

    pass


class MDMenuItemRight(MDMenuItemBase, OneLineRightIconListItem):

    pass


class MDMenu(ScrollView):
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
        :attr:`on_enter`
            Call when mouse enter the bbox of item menu.
        :attr:`on_leave`
            Call when the mouse exit the item menu.
        :attr:`on_dismiss`
            Call when closes menu.
        :attr:`on_release`
            The method that will be called when you click menu items.
    """

    selected_color = ColorProperty(None)
    """Custom color (``rgba`` format) for list item when hover behavior occurs.

    :attr:`selected_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    items = ListProperty()
    """
    See :attr:`~kivy.uix.recycleview.RecycleView.data`.

    :attr:`items` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_mult = NumericProperty(1)
    """
    This number multiplied by the standard increment (56dp on mobile,
    64dp on desktop, determines the width of the menu items.

    If the resulting number were to be too big for the application Window,
    the multiplier will be adjusted for the biggest possible one.

    :attr:`width_mult` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    max_height = NumericProperty()
    """
    The menu will grow no bigger than this number. Set to 0 for no limit.

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    border_margin = NumericProperty("4dp")
    """
    Margin between Window border and menu.

    :attr:`border_margin` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `4dp`.
    """

    ver_growth = OptionProperty(None, allownone=True, options=["up", "down"])
    """
    Where the menu will grow vertically to when opening. Set to None to let
    the widget pick for you. Available options are: `'up'`, `'down'`.

    :attr:`ver_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    hor_growth = OptionProperty(None, allownone=True, options=["left", "right"])
    """
    Where the menu will grow horizontally to when opening. Set to None to let
    the widget pick for you. Available options are: `'left'`, `'right'`.

    :attr:`hor_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None)
    """
    Color of the background of the menu.

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
    The widget object that caller the menu window.

    :attr:`caller` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    position = OptionProperty("auto", options=["auto", "center", "bottom"])
    """
    Menu window position relative to parent element.
    Available options are: `'auto'`, `'center'`, `'bottom'`.

    :attr:`position` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'auto'`.
    """

    radius = ListProperty(
        [
            dp(7),
        ]
    )
    """
    Menu radius.

    :attr:`radius` is a :class:`~kivy.properties.ListProperty`
    and defaults to `'[dp(7),]'`.
    """

    _start_coords = []
    _calculate_complete = False
    _calculate_process = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.check_position_caller)
        Window.bind(on_maximize=self.set_menu_properties)
        Window.bind(on_restore=self.set_menu_properties)
        self.register_event_type("on_dismiss")
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")
        self.register_event_type("on_release")
        self.menu = self.ids.md_menu
        self.target_height = 0

    def check_position_caller(self, instance, width, height):
        self.set_menu_properties(0)

    def set_bg_color_items(self, instance_selected_item):
        """Called when a Hover Behavior event occurs for a list item.

        :type instance_selected_item: <kivymd.uix.menu.MDMenuItemIcon object>
        """

        if self.selected_color:
            for item in self.menu.ids.box.children:
                if item is not instance_selected_item:
                    item.bg_color = (0, 0, 0, 0)
                else:
                    instance_selected_item.bg_color = self.selected_color

    def create_menu_items(self):
        """Creates menu items."""

        for data in self.items:
            if data.get("icon") and data.get("right_content_cls", None):

                item = MDMenuItemIcon(
                    text=data.get("text", ""),
                    divider=data.get("divider", "Full"),
                    _txt_top_pad=data.get("top_pad", "20dp"),
                    _txt_bot_pad=data.get("bot_pad", "20dp"),
                )

            elif data.get("icon"):
                item = MDMenuItemIcon(
                    text=data.get("text", ""),
                    divider=data.get("divider", "Full"),
                    _txt_top_pad=data.get("top_pad", "20dp"),
                    _txt_bot_pad=data.get("bot_pad", "20dp"),
                )

            elif data.get("right_content_cls", None):
                item = MDMenuItemRight(
                    text=data.get("text", ""),
                    divider=data.get("divider", "Full"),
                    _txt_top_pad=data.get("top_pad", "20dp"),
                    _txt_bot_pad=data.get("bot_pad", "20dp"),
                )

            else:

                item = MDMenuItem(
                    text=data.get("text", ""),
                    divider=data.get("divider", "Full"),
                    _txt_top_pad=data.get("top_pad", "20dp"),
                    _txt_bot_pad=data.get("bot_pad", "20dp"),
                )

            # Set height item.
            if data.get("height", ""):
                item.height = data.get("height")
            # Compensate icon area by some left padding.
            if not data.get("icon"):
                item._txt_left_pad = data.get("left_pad", "32dp")
            # Set left icon.
            else:
                item.icon = data.get("icon", "")
            item.bind(on_release=lambda x=item: self.dispatch("on_release", x))
            right_content_cls = data.get("right_content_cls", None)
            # Set right content.
            if isinstance(right_content_cls, RightContent):
                item.ids._right_container.width = right_content_cls.width + dp(
                    20
                )
                item.ids._right_container.padding = ("10dp", 0, 0, 0)
                item.add_widget(right_content_cls)
            else:
                if "_right_container" in item.ids:
                    item.ids._right_container.width = 0
            self.menu.ids.box.add_widget(item)

    def set_menu_properties(self, interval=0):
        """Sets the size and position for the menu window."""

        if self.caller:
            if not self.menu.ids.box.children:
                self.create_menu_items()
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
            # each MDMenuItem or MDMenuItemIcon
            self.target_height = 0
            for item in self.menu.ids.box.children:
                self.target_height += item.height

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
                # Otherwise, let's pick the one with more space and adjust ourselves.
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
                # Otherwise, let's pick the one with more space and adjust ourselves.
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

    def open(self):
        """Animate the opening of a menu window."""

        def open(interval):
            if not self._calculate_complete:
                return
            if self.position == "auto":
                self.menu.pos = self._start_coords
                anim = Animation(
                    x=self.tar_x,
                    y=self.tar_y,
                    width=self.target_width,
                    height=self.target_height,
                    duration=self.opening_time,
                    opacity=1,
                    transition=self.opening_transition,
                )
                anim.start(self.menu)
            else:
                if self.position == "center":
                    self.menu.pos = (
                        self._start_coords[0] - self.target_width / 2,
                        self._start_coords[1] - self.target_height / 2,
                    )
                elif self.position == "bottom":
                    self.menu.pos = (
                        self._start_coords[0] - self.target_width / 2,
                        self.caller.pos[1] - self.target_height,
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

    def on_enter(self, instance):
        """Call when mouse enter the bbox of the item of menu."""

    def on_leave(self, instance):
        """Call when the mouse exit the item of menu."""

    def on_release(self, *args):
        """The method that will be called when you click menu items."""

    def on_dismiss(self):
        """Called when the menu is closed."""

        Window.remove_widget(self)
        self.menu.width = 0
        self.menu.height = 0
        self.menu.opacity = 0

    def dismiss(self):
        """Closes the menu."""

        self.on_dismiss()
