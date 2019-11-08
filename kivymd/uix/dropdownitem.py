"""
MDDropDownItem
==============

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.theming import ThemeManager

Builder.load_string(
    '''
#:import toast kivymd.toast.toast


<MyRoot@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: "Test MDDropDownItem"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['menu', lambda x: x]]

    FloatLayout:

        MDDropDownItem:
            id: dropdown_item
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            items: app.items
            dropdown_bg: [1, 1, 1, 1]

        MDRaisedButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            text: 'Chek Item'
            on_release: toast(dropdown_item.current_item)
''')


class Test(MDApp):

    def build(self):
        self.items = [f"Item {i}" for i in range(50)]
        return Factory.MyRoot()


Test().run()
"""

from kivy.lang import Builder
from kivy.properties import (
    ListProperty,
    StringProperty,
    NumericProperty,
    BooleanProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<_Triangle>:
    canvas:
        Color:
            rgba: root.theme_cls.text_color
        Triangle:
            points:
                [\
                self.right-14, self.y+7, \
                self.right-7, self.y+7, \
                self.right-7, self.y+14 \
                ]


<MDDropDownItem>
    orientation: 'vertical'
    size_hint: None, None
    size: self.minimum_size
    spacing: '5dp'

    BoxLayout:
        size_hint: None, None
        size: self.minimum_size
        spacing: '10dp'

        Label:
            id: label_item
            size_hint: None, None
            size: self.texture_size
            color: root.theme_cls.text_color
        

        _Triangle:
            size_hint: None, None
            size: '20dp', '20dp'

    MDSeparator:
"""
)


class _Triangle(ThemableBehavior, Widget):
    pass


class MDDropDownItem(ThemableBehavior, BoxLayout):
    items = ListProperty()
    """String list of items for a drop-down list."""

    dropdown_bg = ListProperty()
    """Color of the background of the menu."""

    dropdown_max_height = NumericProperty()
    """The menu will grow no bigger than this number."""

    dropdown_width_mult = NumericProperty(2)
    """This number multiplied by the standard increment (56dp on mobile,
    64dp on desktop, determines the width of the menu items.

    If the resulting number were to be too big for the application Window,
    the multiplier will be adjusted for the biggest possible one.
    """

    current_item = StringProperty()
    """Current label of item MDDropDownItem class."""

    _center = BooleanProperty(True)

    _drop_list = None

    _list_menu = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.dropdown_bg:
            self.dropdown_bg = self.theme_cls.primary_color

    def on_items(self, instance, value):
        _list_menu = []
        for name_item in value:
            _list_menu.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name_item,
                    "text_color": self.theme_cls.text_color,
                    "theme_text_color": "Custom",
                    "on_release": lambda x=name_item: self.set_item(x),
                }
            )
        self._list_menu = _list_menu
        self.ids.label_item.text = (
            self.current_item if self.current_item else value[0]
        )
        self.current_item = self.ids.label_item.text

    def set_item(self, name_item):
        self.ids.label_item.text = name_item
        self.current_item = name_item
        self._drop_list.dismiss()

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y) and self._list_menu:
            self._drop_list = MDDropdownMenu(
                _center=self._center,
                items=self._list_menu,
                background_color=self.dropdown_bg,
                max_height=self.dropdown_max_height,
                width_mult=self.dropdown_width_mult,
                width_rectangle=1,
            )
            self._drop_list.open(self)
