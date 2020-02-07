"""
Components/Context Menu
=======================

Example
-------

.. code-block:: python

    from kivymd.app import MDApp
    from kivy.lang import Builder

    from kivymd.theming import ThemeManager

    kv = '''
    FloatLayout:

        MDContextMenu:
            menu: app.menu
            pos_hint: {'top': 1}
            on_enter: app.on_enter(*args)

            MDContextMenuItem:
                text: 'File'

            MDContextMenuItem:
                text: 'Edit'
    '''


    MENU = [
        [
            "File",
            [
                {"Item 1": []},
                {
                    "Item 2": [
                        "Item 1",
                        "Item 2",
                        "Separator",
                        ["language-python", "Item 3"],
                    ]
                },
                "Separator",
                {"Item 3": []},
                {
                    "Item 4": [
                        ["language-python", "Item 1"],
                        ["language-cpp", "Item 2"],
                        "Separator",
                        ["language-swift", "Item 3"],
                    ]
                },
                "Separator",
                {"Item 5": []},
            ],
        ],

        [
            "Edit",
            [
                {"Item 1": []},
                ["language-swift", "Item 3"]
            ]
        ]

    ]


    class Test(MDApp):
        context_menu = None
        menu = MENU

        def on_enter(self, instance):
            '''
            :type instance: <kivymd.context_menu.MDContextMenu object>

            '''

            print(instance.current_selected_menu.text)

        def build(self):
            root = Builder.load_string(kv)
            return root


    Test().run()
"""

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    StringProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
import kivymd.material_resources as m_res


Builder.load_string(
    """
<MDContextMenu>
    size_hint_y: None
    height: self.minimum_height

    canvas:
        Color:
            rgba:
                root.background_color_menu_header \
                if root.background_color_menu_header \
                else root.theme_cls.primary_dark
        Rectangle:
            pos: self.pos
            size: self.size


<MDContextMenuItem>
    orientation: "vertical"
    size_hint: None, None
    size: self.minimum_size
    padding: "5dp"

    Label:
        text: root.text
        color: root.text_color
        size_hint: None, None
        size: self.texture_size

    MDSeparator:
        color: root._color_active
        size_hint_y: None
        height: "2dp"


<MenuIconItem>
    padding: 0, 0, "5dp", 0

    canvas:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon: root.icon
        disabled: True
        theme_text_color: "Custom"
        text_color: root.icon_color
        pos_hint: {"center_y": .5}
        user_font_size: root.icon_size

    Label:
        id: label_item
        text: root.text
        size_hint_x: None
        width: self.texture_size[0]
        shorten: True
        color:
            root.color_text_item_menu_header \
            if root.color_text_item_menu_header \
            else root.theme_cls.text_color


<MenuItem>
    padding: "25dp", 0, "5dp", 0

    canvas:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: label_item
        text: root.text
        size_hint_x: None
        width: self.texture_size[0]
        shorten: True
        color:
            root.color_text_item_menu_header \
            if root.color_text_item_menu_header \
            else root.theme_cls.text_color

    Widget:

    MDLabel:
        text: root.arrow_right
        pos_hint: {"center_y": .5}
        halign: "right"
        color: label_item.color
        bold: True
"""
)


class MDContextDropdownMenu(MDDropdownMenu):
    menu_item = ObjectProperty()

    def display_menu(self, caller):
        c = caller.to_window(caller.center_x, caller.center_y)
        target_width = self.width_mult * m_res.STANDARD_INCREMENT
        if target_width > Window.width:
            target_width = (
                int(Window.width / m_res.STANDARD_INCREMENT)
                * m_res.STANDARD_INCREMENT
            )

        target_height = sum([dp(48) for i in self.items])
        if 0 < self.max_height < target_height:
            target_height = self.max_height

        if self.ver_growth is not None:
            ver_growth = self.ver_growth
        else:
            if target_height <= c[1] - self.border_margin:
                ver_growth = "down"
            elif target_height < Window.height - c[1] - self.border_margin:
                ver_growth = "up"
            else:
                if c[1] >= Window.height - c[1]:
                    ver_growth = "down"
                    target_height = c[1] - self.border_margin
                else:
                    ver_growth = "up"
                    target_height = Window.height - c[1] - self.border_margin

        if not self.hor_growth:
            if target_width <= Window.width - c[0] - self.border_margin:
                pass
            elif target_width < c[0] - self.border_margin:
                pass
            else:
                if Window.width - c[0] >= c[0]:
                    target_width = Window.width - c[0] - self.border_margin
                else:
                    target_width = c[0] - self.border_margin

        if ver_growth == "down":
            tar_y = c[1] - target_height
        else:
            tar_y = c[1]

        menu = self.ids.md_menu
        if not self._center:
            x = self.menu_item.x
            y = caller.y - target_height
        else:
            x = target_width
            y = tar_y
        anim = Animation(
            x=x,
            y=y,
            width=target_width,
            height=target_height,
            duration=0.3,
            transition="out_quint",
        )
        menu.pos = c
        anim.start(menu)


class BasedMenuItem(BoxLayout, HoverBehavior, ThemableBehavior):
    """List item for toolbar context menu."""

    text = StringProperty()
    """Text of Item."""

    background_color = ListProperty()
    """Background color of Item."""

    selected_color = ListProperty()
    """Selected color of Item."""

    arrow_right = StringProperty()
    """The path to the image of the right arrow."""

    color_text_item_menu_header = ListProperty()
    """Header color for context menu items."""

    context_menu = ObjectProperty()
    """<kivymd.context_menu.MDContextMenu object>."""

    name_item_menu = StringProperty()
    """The currently selected context menu header item."""

    _background_color = []

    def on_enter(self):
        if (
            self.context_menu.current_selected_item
            and self.context_menu.current_selected_item != self.text
            and self.context_menu.context_submenu_open
            and self.parent.parent.parent.parent != self.context_menu.sub_menu
        ):
            self.context_menu.sub_menu.on_dismiss()
            self.context_menu.context_submenu_open = False
        self.context_menu.current_selected_item = self.text

        if not self._background_color:
            self._background_color = self.background_color
        self.background_color = self.selected_color

        if self.arrow_right:
            if self.context_menu.context_submenu_open:
                return
            self.context_menu.generates_context_submenu(
                self, self.name_item_menu, self.text
            )

    def on_leave(self):
        self.background_color = self._background_color


class MenuItem(BasedMenuItem):
    pass


class MenuIconItem(BasedMenuItem, ThemableBehavior):
    icon = StringProperty("circle-outline")
    icon_color = ListProperty()
    icon_size = NumericProperty()


class MDContextMenuItem(BoxLayout, ThemableBehavior, HoverBehavior):
    """An item inside the context menu header."""

    text = StringProperty()
    """Text item"""

    color_active = ListProperty()
    """Color of the item when it is selected."""

    text_color = ListProperty()
    """Color of the item."""

    _color_active = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.text_color:
            self.text_color = self.theme_cls.text_color

    def on_enter(self):
        """Called when the mouse cursor hovers over one of the items
        in the header of the context menu."""

        def context_menu_open():
            self.parent.open(self, self.text)
            self._color_active = (
                self.color_active
                if self.color_active
                else self.theme_cls.primary_color
            )

        if not self.parent.context_menu_open:
            context_menu_open()
        else:
            if self.parent.current_selected_menu.text != self.text:
                # FIXME:  MDContextMenu.context_previous_menu_dismiss
                # of <kivymd.context_menu.MDContextMenu> method
                # is not called on a menu close event.
                self.parent.context_menu.on_dismiss()
                if self.parent.sub_menu:
                    self.parent.sub_menu.on_dismiss()
                self.parent.context_previous_menu_dismiss()
                context_menu_open()

        self.parent._on_enter()

    def diactivate_item(self):
        self._color_active = [0, 0, 0, 0]


class MDContextMenu(BoxLayout, ThemableBehavior):
    """MDContextMenu.

    :Events:
        `on_enter`
            Called when an item is selected in the context menu header
        `on_leave`
            Called when the context menu is closed
    """

    menu = ListProperty()

    background_color_context_menu = ListProperty()
    """Context menu background color."""

    selected_color_item_context_menu = ListProperty()
    """The highlight color of the current item in the context menu."""

    background_color_menu_header = ListProperty()
    """Header color for context menu items."""

    color_text_item_menu_header = ListProperty()
    """Header color for context menu items."""

    icon_color = ListProperty()
    """The color of the icons used for menu items."""

    icon_size = NumericProperty("15sp")
    """The size of the icons used for menu items."""

    separator_height = NumericProperty(1)
    """Line separator height."""

    context_menu_open = False
    """Open or close context menu."""

    context_submenu_open = False
    """Open or close context sub menu."""

    current_selected_menu = None
    """Object of the selected item in the context menu header."""

    current_selected_item = ""
    """Name of the selected item in the context menu."""

    sub_menu = None
    """Submenu object."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")

        if not self.background_color_context_menu:
            self.background_color_context_menu = self.theme_cls.primary_dark
        if not self.selected_color_item_context_menu:
            self.selected_color_item_context_menu = self.theme_cls.primary_color
        if not self.icon_color:
            self.icon_color = self.theme_cls.text_color

        # Creating menu objects and submenus.
        self.context_menu = MDContextDropdownMenu(
            width_mult=3,
            background_color=self.background_color_context_menu,
            width_rectangle=1,
            max_height=dp(200),
        )
        self.context_menu.bind(on_dismiss=self.context_previous_menu_dismiss)

    def on_enter(self):
        """Called when an item is selected in the context menu header."""

        pass

    def on_leave(self):
        """Called when the context menu is closed."""

        pass

    def _on_enter(self):
        self.dispatch("on_enter")

    def add_separator(self, list_menu):
        list_menu.append(
            {"viewclass": "MDSeparator", "height": self.separator_height}
        )

    def add_icon_item(self, list_menu, data):
        list_menu.append(
            {
                "viewclass": "MenuIconItem",
                "text": data[1],
                "icon": data[0],
                "icon_color": self.icon_color,
                "icon_size": self.icon_size,
                "background_color": self.background_color_context_menu,
                "selected_color": self.selected_color_item_context_menu,
                "context_menu": self,
                "height": dp(32),
            }
        )

    def generates_context_submenu(
        self, instance_menu_item, name_item_menu, text
    ):
        """Generates a sub menu."""

        sub_menu = []
        self.sub_menu = MDContextDropdownMenu(
            width_mult=3,
            background_color=self.background_color_context_menu,
            width_rectangle=1,
            max_height=dp(200),
            _center=True,
        )

        for data_item in self.menu:
            if data_item[0] == name_item_menu:
                if data_item[0] == name_item_menu:
                    for data_item in data_item[1]:
                        if isinstance(data_item, dict):
                            if text in list(data_item.keys()):
                                for item_text in data_item[text]:
                                    if isinstance(item_text, str):
                                        if item_text == "Separator":
                                            self.add_separator(sub_menu)
                                        else:
                                            sub_menu.append(
                                                {
                                                    "viewclass": "MenuItem",
                                                    "text": item_text,
                                                    "background_color": self.background_color_context_menu,
                                                    "selected_color": self.selected_color_item_context_menu,
                                                    "context_menu": self,
                                                    "height": dp(32),
                                                }
                                            )
                                    if isinstance(item_text, list):
                                        self.add_icon_item(sub_menu, item_text)
        self.sub_menu.items = sub_menu
        self.sub_menu.open(instance_menu_item)
        self.context_submenu_open = True

    def generates_context_menu(self, instance, name_item_menu):
        """Generates a menu."""

        menu_list = []
        for data_item in self.menu:
            if data_item[0] == name_item_menu:
                for data_item in data_item[1]:
                    if isinstance(data_item, str) and data_item == "Separator":
                        self.add_separator(menu_list)
                    elif isinstance(data_item, dict):
                        name_item = list(data_item.keys())[0]
                        if not data_item[name_item]:
                            arrow_right = ""
                        else:
                            arrow_right = ">"
                        menu_list.append(
                            {
                                "viewclass": "MenuItem",
                                "text": name_item,
                                "background_color": self.background_color_context_menu,
                                "selected_color": self.selected_color_item_context_menu,
                                "color_text_item_menu_header": self.color_text_item_menu_header,
                                "arrow_right": arrow_right,
                                "name_item_menu": name_item_menu,
                                "context_menu": self,
                                "height": dp(32),
                            }
                        )
                    elif isinstance(data_item, list):
                        self.add_icon_item(menu_list, data_item)
                break
        return menu_list

    def open(self, instance, name_item_menu):
        menu_list = self.generates_context_menu(instance, name_item_menu)
        self.open_menu(instance, menu_list)

    def open_menu(self, instance, menu_list):
        if menu_list:
            self.current_selected_menu = instance
            self.context_menu.items = menu_list
            self.context_menu.menu_item = instance
            self.context_menu.open(instance)
            self.context_menu_open = True

    def context_previous_menu_dismiss(self, *args):
        """Called when closing the context menu."""

        self.context_menu_open = False
        self.context_submenu_open = False
        self.current_selected_menu.diactivate_item()
        self.current_selected_menu = None
        self.dispatch("on_leave")
