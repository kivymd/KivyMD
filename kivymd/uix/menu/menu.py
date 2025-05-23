"""
Components/Menu
===============

.. seealso::

    `Material Design spec, Menus <https://m3.material.io/components/menus/overview>`_

.. rubric:: Menus display a list of choices on temporary surfaces.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-preview.png
    :align: center

- Menus should be easy to open, close, and interact with
- Menu content should be suited to user needs
- Menu items should be easy to scan

Usage
-----

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    id: button
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.menu_open()

                    MDButtonText:
                        text: "Press me"
            '''


            class Example(MDApp):
                def menu_open(self):
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(
                        caller=self.root.ids.button, items=menu_items
                    ).open()

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def menu_open(self, button_press_me):
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(caller=button_press_me, items=menu_items).open()

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Press me"
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=self.menu_open,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-usage.gif
    :align: center

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-anatomy.png
    :align: center

You can combine the following parameters:
-----------------------------------------

- leading_icon
- text
- trailing_icon
- trailing_text

...to create the necessary types of menu items:

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_icon": "apple-keyboard-command",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "trailing_text": "Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_text": "Shift+X",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-leading-icon-trailing-text.png
    :align: center

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-text.png
    :align: center

You can use the following parameters to customize the menu items:
-----------------------------------------------------------------

- text_color
- leading_icon_color
- trailing_icon_color
- trailing_text_color

.. code-block:: python

    menu_items = [
        {
            "text": "Strikethrough",
            "leading_icon": "check",
            "trailing_icon": "apple-keyboard-command",
            "trailing_text": "+Shift+X",
            "leading_icon_color": "orange",
            "trailing_icon_color": "green",
            "trailing_text_color": "red",
        }
    ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-item-customize.png
    :align: center

.. Header:

Header
------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.boxlayout import MDBoxLayout

            KV = '''
            <MenuHeader>
                spacing: "12dp"
                padding: "4dp"
                adaptive_height: True

                MDIconButton:
                    icon: "gesture-tap-button"
                    pos_hint: {"center_y": .5}

                MDLabel:
                    text: "Actions"
                    adaptive_size: True
                    pos_hint: {"center_y": .5}


            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    id: button
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.menu.open()

                    MDButtonText:
                        text: "Press me"
            '''


            class MenuHeader(MDBoxLayout):
                '''An instance of the class that will be added to the menu header.'''


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.screen = Builder.load_string(KV)
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    self.menu = MDDropdownMenu(
                        header_cls=MenuHeader(),
                        caller=self.screen.ids.button,
                        items=menu_items,
                    )

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return self.screen


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButtonText, MDButton, MDIconButton
            from kivymd.uix.label import MDLabel
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.screen import MDScreen


            class MenuHeader(MDBoxLayout):
                '''An instance of the class that will be added to the menu header.'''


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    self.menu = MDDropdownMenu(
                        header_cls=MenuHeader(
                            MDIconButton(
                                icon="gesture-tap-button",
                                pos_hint={"center_y": .5},
                            ),
                            MDLabel(
                                text="Actions",
                                adaptive_size=True,
                                pos_hint={"center_y": .5},
                            ),
                            spacing="12dp",
                            padding="4dp",
                            adaptive_height=True,
                        ),
                        items=menu_items,
                    )
                    self.screen = (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Press me"
                                ),
                                id="button_press_me",
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=lambda x: self.menu.open(),
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )
                    self.menu.caller = self.screen.get_ids().button_press_me

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return self.screen


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-header.png
    :align: center

Menu with MDTopAppBar
---------------------

The :class:`~MDDropdownMenu` works well with the standard
:class:`~kivymd.uix.toolbar.MDTopAppBar`. Since the buttons on the Toolbar are created
by the MDTopAppBar component, it is necessary to pass the button as an argument to
the callback using `lambda x: app.callback(x)`. This example uses drop down menus
for both the righthand and lefthand menus.

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

            KV = '''
            MDBoxLayout:
                orientation: "vertical"
                md_bg_color: self.theme_cls.backgroundColor

                MDTopAppBar:

                    MDTopAppBarLeadingButtonContainer:

                        MDActionTopAppBarButton:
                            icon: "menu"
                            on_release: app.callback(self)

                    MDTopAppBarTitle:
                        text: "MDTopAppBar"
                        pos_hint: {"center_x": .5}

                    MDTopAppBarTrailingButtonContainer:

                        MDActionTopAppBarButton:
                            icon: "dots-vertical"
                            on_release: app.callback(self)

                MDLabel:
                    text: "Content"
                    halign: "center"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    self.menu = MDDropdownMenu(items=menu_items)
                    return Builder.load_string(KV)

                def callback(self, button):
                    self.menu.caller = button
                    self.menu.open()

                def menu_callback(self, text_item):
                    self.menu.dismiss()
                    MDSnackbar(
                        MDSnackbarText(
                            text=text_item,
                        ),
                        y=dp(24),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                    ).open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.appbar import (
                MDTopAppBar,
                MDTopAppBarLeadingButtonContainer,
                MDActionTopAppBarButton,
                MDTopAppBarTitle,
                MDTopAppBarTrailingButtonContainer,
            )
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.label import MDLabel
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    self.menu = MDDropdownMenu(items=menu_items)
                    return (
                        MDBoxLayout(
                            MDTopAppBar(
                                MDTopAppBarLeadingButtonContainer(
                                    MDActionTopAppBarButton(
                                        icon="menu",
                                        on_release=self.callback,
                                    )
                                ),
                                MDTopAppBarTitle(
                                    text="MDTopAppBar",
                                    pos_hint={"center_x": .5},
                                ),
                                MDTopAppBarTrailingButtonContainer(
                                    MDActionTopAppBarButton(
                                        icon="dots-vertical",
                                        on_release=self.callback,
                                    )
                                )
                            ),
                            MDLabel(
                                text="Content",
                                halign="center",
                            ),
                            orientation="vertical",
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )

                def callback(self, button):
                    self.menu.caller = button
                    self.menu.open()

                def menu_callback(self, text_item):
                    self.menu.dismiss()
                    MDSnackbar(
                        MDSnackbarText(
                            text=text_item,
                        ),
                        y=dp(24),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                    ).open()


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toolbar-menu.png
    :align: center

.. Position:

Position
========

Bottom position
---------------

.. seealso::

    :attr:`~MDDropdownMenu.position`

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDTextField:
                    id: field
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    size_hint_x: None
                    width: "200dp"
                    on_focus: if self.focus: app.menu.open()

                    MDTextFieldHintText:
                        text: "Password"
            '''


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.screen = Builder.load_string(KV)
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.set_item(x),
                        } for i in range(5)]
                    self.menu = MDDropdownMenu(
                        caller=self.screen.ids.field,
                        items=menu_items,
                        position="bottom",
                    )

                def set_item(self, text_item):
                    self.screen.ids.field.text = text_item
                    self.menu.dismiss()

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return self.screen


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.textfield import MDTextField, MDTextFieldHintText


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.set_item(x),
                        }
                        for i in range(5)
                    ]
                    self.menu = MDDropdownMenu(items=menu_items, position="bottom")
                    self.screen = MDScreen(
                        MDTextField(
                            MDTextFieldHintText(text="Password"),
                            id="field",
                            pos_hint={"center_x": 0.5, "center_y": 0.6},
                            size_hint_x=None,
                            width="200dp",
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )
                    field = self.screen.get_ids().field
                    self.menu.caller = field
                    field.bind(
                        focus=lambda instance, value: self.menu.open() if value else None
                    )

                def set_item(self, text_item):
                    self.screen.get_ids().field.text = text_item
                    self.menu.dismiss()

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return self.screen


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position.png
    :align: center

Center position
---------------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.app import MDApp

            KV = '''
            MDScreen
                md_bg_color: self.theme_cls.backgroundColor

                MDDropDownItem:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.open_drop_item_menu(self)

                    MDDropDownItemText:
                        id: drop_text
                        text: "Item"
            '''


            class Example(MDApp):
                drop_item_menu: MDDropdownMenu = None

                def open_drop_item_menu(self, item):
                    menu_items = [
                        {
                            "text": f"{i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    if not self.drop_item_menu:
                        self.drop_item_menu = MDDropdownMenu(
                            caller=item, items=menu_items, position="center"
                        )
                        self.drop_item_menu.open()

                def menu_callback(self, text_item):
                    self.root.ids.drop_text.text = text_item
                    self.drop_item_menu.dismiss()

                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.uix.dropdownitem import MDDropDownItemText, MDDropDownItem
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                drop_item_menu: MDDropdownMenu = None

                def open_drop_item_menu(self, item):
                    menu_items = [
                        {
                            "text": f"{i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    if not self.drop_item_menu:
                        self.drop_item_menu = MDDropdownMenu(
                            caller=item, items=menu_items, position="center"
                        )
                        self.drop_item_menu.open()

                def menu_callback(self, text_item):
                    self.root.get_ids().drop_text.text = text_item
                    self.drop_item_menu.dismiss()

                def build(self):
                    return (
                        MDScreen(
                            MDDropDownItem(
                                MDDropDownItemText(
                                    id="drop_text",
                                    text="Item",
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=self.open_drop_item_menu,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-position-center.gif
    :align: center

API break
=========

1.1.1 version
-------------

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
            icon_size: "16sp"
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


    class Example(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "right_text": "+Shift+X",
                    "right_icon": "apple-keyboard-command",
                    "left_icon": "web",
                    "viewclass": "Item",
                    "height": dp(54),
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                caller=self.screen.ids.button,
                items=menu_items,
                bg_color="#bdc6b0",
                width_mult=4,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Example().run()

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.metrics import dp

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


    class Example(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
            menu_items = [
                {
                    "text": f"Item {i}",
                    "leading_icon": "web",
                    "trailing_icon": "apple-keyboard-command",
                    "trailing_text": "+Shift+X",
                    "trailing_icon_color": "grey",
                    "trailing_text_color": "grey",
                    "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                } for i in range(5)
            ]
            self.menu = MDDropdownMenu(
                md_bg_color="#bdc6b0",
                caller=self.screen.ids.button,
                items=menu_items,
            )

        def menu_callback(self, text_item):
            print(text_item)

        def build(self):
            return self.screen


    Example().run()

2.0.0 version
-------------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.menu import MDDropdownMenu

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    id: button
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.menu_open()

                    MDButtonText:
                        text: "Press me"
            '''


            class Example(MDApp):
                def menu_open(self):
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(
                        caller=self.root.ids.button, items=menu_items
                    ).open()

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def menu_open(self, button_press_me):
                    menu_items = [
                        {
                            "text": f"Item {i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(caller=button_press_me, items=menu_items).open()

                def menu_callback(self, text_item):
                    print(text_item)

                def build(self):
                    self.theme_cls.primary_palette = "Orange"
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Press me"
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=self.menu_open,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )


            Example().run()
"""

from __future__ import annotations

__all__ = (
    "BaseDropdownItem",
    "MDDropdownMenu",
    "MDDropdownTextItem",
    "MDDropdownLeadingIconItem",
    "MDDropdownTrailingIconItem",
    "MDDropdownTrailingIconTextItem",
    "MDDropdownTrailingTextItem",
    "MDDropdownLeadingTrailingIconTextItem",
    "MDDropdownLeadingIconTrailingTextItem",
)

import os

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
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.recycleview import RecycleView

from kivymd import uix_path
from kivymd.uix.behaviors import RectangularRippleBehavior, StencilBehavior
from kivymd.uix.behaviors.motion_behavior import MotionDropDownMenuBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

# from kivymd.uix.list import IRightBody

with open(
    os.path.join(uix_path, "menu", "menu.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDMenu(RecycleView):
    width_mult = NumericProperty(1)
    """
    See :attr:`~MDDropdownMenu.width_mult`.

    .. deprecated:: 1.2.0
    """

    drop_cls = ObjectProperty()
    """
    See :class:`~MDDropdownMenu` class.
    """


class BaseDropdownItem(RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    """
    Base class for menu items.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` classes.
    """

    text = StringProperty()
    """
    The text of the menu item.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    leading_icon = StringProperty()
    """
    The leading icon of the menu item.

    :attr:`leading_icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    trailing_icon = StringProperty()
    """
    The trailing icon of the menu item.

    :attr:`trailing_icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    trailing_text = StringProperty()
    """
    The trailing text of the menu item.

    :attr:`trailing_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the text of the
    menu item.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    leading_icon_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the leading icon
    of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    trailing_icon_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the trailing
    icon of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    trailing_text_color = ColorProperty(None)
    """
    The color of the text in (r, g, b, a) or string format for the trailing
    text of the menu item.

    :attr:`leading_icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    divider = OptionProperty("Full", options=["Full", None], allownone=True)
    """
    Divider mode. Available options are: `'Full'`, `None`
    and default to `'Full'`.

    :attr:`divider` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Full'`.
    """

    divider_color = ColorProperty(None)
    """
    Divider color in (r, g, b, a) or string format.

    :attr:`divider_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDTrailingTextContainer(BaseDropdownItem, MDLabel):
    """
    Implements a container for trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~BaseDropdownItem` and
    :class:`~kivymd.uix.list.IRightBody` and
    :class:`~kivymd.uix.label.MDLabel` classes.
    """


class MDTrailingIconTextContainer(BaseDropdownItem, MDBoxLayout):
    """
    Implements a container for trailing icons and trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~BaseDropdownItem` and
    :class:`~kivymd.uix.list.IRightBody` and
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` classes.
    """


class MDDropdownTextItem(BaseDropdownItem):
    """
    Implements a menu item with text without leading and trailing icons.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownLeadingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, leading icon and without trailing icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownTrailingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon and with trailing
    icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownTrailingIconTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon, with trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownTrailingTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, without leading icon, without trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownLeadingIconTrailingTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, leading icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownLeadingTrailingIconTextItem(BaseDropdownItem):
    """
    Implements a menu item with text, with leading icon, with trailing
    icon and with trailing text.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownLeadingTrailingIconItem(BaseDropdownItem):
    """
    Implements a menu item with text, with leading icon, with trailing icon.

    .. versionadded:: 1.2.0

    For more information, see in the :class:`~BaseDropdownItem` class.
    """


class MDDropdownMenu(MotionDropDownMenuBehavior, StencilBehavior, MDCard):
    """
    Dropdown menu class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionDropDownMenuBehavior` and
    :class:`~kivymd.uix.behaviors.stencil_behavior.StencilBehavior` and
    :class:`~kivymd.uix.card.card.MDCard`
    classes documentation.

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

    :attr:`header_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    items = ListProperty()
    """
    List of dictionaries with properties for menu items.

    :attr:`items` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    width_mult = NumericProperty(1, deprecated=True)
    """
    This number multiplied by the standard increment ('56dp' on mobile, '64dp'
    on desktop), determines the width of the menu items.

    If the resulting number were to be too big for the application Window,
    the multiplier will be adjusted for the biggest possible one.

    .. deprecated:: 1.2.0

        Use `width` instead.

        .. code-block:: python

            self.menu = MDDropdownMenu(
                width=dp(240),
                ...,
            )

    :attr:`width_mult` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    min_height = NumericProperty(dp(48))

    max_height = NumericProperty()
    """
    The menu will grow no bigger than this number. Set to 0 for no limit.

    :attr:`max_height` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    border_margin = NumericProperty("4dp")
    """
    Margin between Window border and menu.

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

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-up.png
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            ver_growth="down",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-ver-growth-down.png
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

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-left.png
        :align: center

    .. code-block:: python

        self.menu = MDDropdownMenu(
            hor_growth="right",
            ...,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/menu-hor-growth-right.png
        :align: center

    :attr:`hor_growth` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None, deprecated=True)
    """
    Color in (r, g, b, a) or string format of the background of the menu.

    .. deprecated:: 1.2.0

        Use `md_bg_color` instead.

    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
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
    Available options are: `'auto'`, `'top'`, `'center'`, `'bottom'`.

    See Position_ for more information.

    :attr:`position` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'auto'`.
    """

    radius = VariableListProperty([dp(7)])
    """
    Menu radius.

    :attr:`radius` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to `'[dp(7)]'`.
    """

    _items = []
    _start_coords = []
    _tar_x = 0
    _tar_y = 0

    __events__ = ("on_dismiss",)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(
            on_resize=self._remove_menu,
            on_maximize=self._remove_menu,
            on_restore=self._remove_menu,
        )
        self.menu = self.ids.md_menu
        self.target_height = 0

    def adjust_width(self) -> None:
        """
        Adjust the width of the menu if the width of the menu goes beyond
        the boundaries of the parent window from  starting point.
        """

        if self._start_coords[0] >= Window.width / 2:
            if self.width > self._start_coords[0]:
                self.width = (
                    self._start_coords[0]
                    - self.border_margin
                    - (
                        (self.caller.width / 2 + self.border_margin)
                        if self.position in ["right", "left"]
                        else 0
                    )
                )
        else:
            if Window.width - self._start_coords[0] < self.width:
                self.width = (
                    Window.width - self._start_coords[0] - self.border_margin
                )

    def check_ver_growth(self) -> None:
        """
        Checks whether the height of the lower/upper borders of the menu
        exceeds the limits borders of the parent window.
        """

        if self.target_height > self._start_coords[1] - self.border_margin:
            self.ver_growth = "up"
        else:
            if self._start_coords[1] > Window.height - self._start_coords[1]:
                self.ver_growth = "down"

    def check_hor_growth(self) -> None:
        """
        Checks whether the width of the left/right menu borders exceeds the
        boundaries of the parent window.
        """

        if (
            Window.width - (self._start_coords[0] + self.border_margin)
            <= self.width
        ):
            self.hor_growth = "left"
        elif self.width >= self._start_coords[0] + self.border_margin:
            self.hor_growth = "right"

    def get_target_pos(self) -> [float, float]:
        self._tar_x, self._tar_y = self._start_coords

        if self.ver_growth == "up":
            self._tar_y = self._start_coords[1] + self.height
        else:
            self._tar_y = self._start_coords[1]

        if self.hor_growth == "left":
            self._tar_x = self._start_coords[0] - self.width
        else:
            self._tar_x = self._start_coords[0]

        return self._tar_x, self._tar_y

    def set_target_height(self) -> None:
        """
        Set the target height of the menu depending on the size of each item.
        """

        self.target_height = 0
        for item in self.menu.data:
            self.target_height += item.get("height", self.min_height)

        if 0 < self.max_height < self.target_height:
            self.target_height = self.max_height

        if self._start_coords[1] >= Window.height / 2:
            if self.target_height > self._start_coords[1]:
                self.target_height = (
                    self._start_coords[1]
                    - self.border_margin
                    - (
                        (self.caller.height / 2 + self.border_margin)
                        if self.position in ["top", "bottom"]
                        else 0
                    )
                )
        else:
            if Window.height - self._start_coords[1] < self.target_height:
                self.target_height = (
                    Window.height - self._start_coords[1] - self.border_margin
                )

    def set_menu_properties(self, *args) -> None:
        """Sets the size and position for the menu window."""

        if self.caller:
            self.menu.data = self._items
            # We need to pick a starting point, see how big we need to be,
            # and where to grow to.
            self._start_coords = self.caller.to_window(*self.caller.center)

            self.adjust_width()
            self.set_target_height()
            self.check_ver_growth()
            self.check_hor_growth()

    def set_menu_pos(self, *args) -> None:
        if self.position == "auto":
            self.menu.x = self._tar_x
            self.menu.y = self._tar_y - (
                self.header_cls.height if self.header_cls else 0
            )
        else:
            if self.position == "center":
                self.pos = (
                    self._start_coords[0] - self.width / 2,
                    self._start_coords[1] - self.height / 2,
                )
            elif self.position == "bottom":
                self.pos = (
                    (
                        (self._start_coords[0] - self.width / 2)
                        if not self.hor_growth
                        else (
                            (self._start_coords[0] - self.width)
                            if self.hor_growth == "left"
                            else (self._start_coords[0])
                        )
                    ),
                    self._start_coords[1]
                    - (
                        self.height
                        + self.border_margin
                        + self.caller.height / 2
                    ),
                )
            elif self.position == "top":
                self.pos = (
                    (
                        (self._start_coords[0] - self.width / 2)
                        if not self.hor_growth
                        else (
                            (self._start_coords[0] - self.width)
                            if self.hor_growth == "left"
                            else (self._start_coords[0])
                        )
                    ),
                    self._start_coords[1]
                    + self.caller.height / 2
                    + self.border_margin,
                )

    def adjust_position(self) -> str:
        """
        Return value 'auto' for the menu position if the menu position is out
        of screen.
        """

        position = self.position

        if position == "bottom":
            if (
                self._start_coords[1]
                - (self.height + self.border_margin + self.caller.height / 2)
                < 0
            ):
                position = "auto"
        elif position == "top":
            if (
                self._start_coords[1]
                + self.caller.height / 2
                + self.border_margin
                > Window.height
            ):
                position = "auto"
        elif position == "center":
            if (
                (
                    self._start_coords[1] + self.height / 2 > Window.height
                    or self._start_coords[1] - self.height / 2 < 0
                )
                or Window.width - (self._start_coords[0] + self.border_margin)
                < self.width / 2
                or self._start_coords[0] + self.border_margin < self.width / 2
            ):
                position = "auto"

        return position

    def open(self) -> None:
        """Animate the opening of a menu window."""

        self.set_menu_properties()
        Window.add_widget(self)
        self.position = self.adjust_position()

        if self.width <= 100:
            self.width = dp(240)

        self.height = self.target_height
        self._tar_x, self._tar_y = self.get_target_pos()
        self.x = self._tar_x
        self.y = self._tar_y - self.target_height
        self.scale_value_center = self.caller.center
        self.set_menu_pos()
        self.on_open()

    def on_items(self, instance, value: list) -> None:
        """
        The method sets the class that will be used to create the menu item.
        """

        items = []
        viewclass = "MDDropdownTextItem"

        for data in value:
            if "viewclass" not in data:
                if (
                    "leading_icon" not in data
                    and "trailing_icon" not in data
                    and "trailing_text" not in data
                ):
                    viewclass = "MDDropdownTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" not in data
                    and "trailing_text" not in data
                ):
                    viewclass = "MDDropdownLeadingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" in data
                    and "trailing_text" not in data
                ):
                    viewclass = "MDDropdownTrailingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" in data
                    and "trailing_text" in data
                ):
                    viewclass = "MDDropdownTrailingIconTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" in data
                    and "trailing_text" in data
                ):
                    viewclass = "MDDropdownLeadingTrailingIconTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" in data
                    and "trailing_text" not in data
                ):
                    viewclass = "MDDropdownLeadingTrailingIconItem"
                elif (
                    "leading_icon" not in data
                    and "trailing_icon" not in data
                    and "trailing_text" in data
                ):
                    viewclass = "MDDropdownTrailingTextItem"
                elif (
                    "leading_icon" in data
                    and "trailing_icon" not in data
                    and "trailing_text" in data
                ):
                    viewclass = "MDDropdownLeadingIconTrailingTextItem"

                data["viewclass"] = viewclass

            if "height" not in data:
                data["height"] = dp(48)

            items.append(data)

        self._items = items
        # Update items in view
        if hasattr(self, "menu"):
            self.menu.data = self._items

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

    def dismiss(self, *args) -> None:
        """Closes the menu."""

        self.on_dismiss()

    def _remove_menu(self, *args):
        Window.remove_widget(self)
        self.set_scale()


if __name__ == "__main__":
    # To test the correct menu position.
    from kivy.lang import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.button import MDButton, MDButtonText
    from kivymd.uix.screen import MDScreen

    class Example(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = MDScreen(md_bg_color=self.theme_cls.backgroundColor)
            menu_items = [{"text": f"Item {i}"} for i in range(55)]
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
                    MDButton(
                        MDButtonText(
                            text="Press me",
                        ),
                        pos_hint=pos_hint,
                        on_release=self.open_menu,
                    )
                )

        def build(self):
            return self.screen

    Example().run()
