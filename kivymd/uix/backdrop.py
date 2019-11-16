"""
Backdrop
========

Tooltips display informative text when users hover over, focus on,
or tap an element.

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Menus <https://material.io/components/backdrop/>`_

Example
-------

from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

# Your layouts.
Builder.load_string(
    '''
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<ItemBackdropBackLayer>
    size_hint_y: None
    height: self.minimum_height
    spacing: "10dp"

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_dark if root.selected_item \
                else root.theme_cls.primary_color
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1


<ItemBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        size_hint: None, None
        size: "30dp", "30dp"
        active: False or self.active
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""

    MDCheckbox:
        group: "size"
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<MyBackdropFrontLayer@ScrollView>
    backdrop: None
    backlayer: None

    GridLayout:
        size_hint_y: None
        height: self.minimum_height
        cols: 1
        padding: "5dp"

        ItemBackdropFrontLayer:
            text: "Press item"
            secondary_text: "to Shop Electronics"
            icon: "monitor-star"
            on_press:
                root.backlayer.current = "second screen"
                root.backdrop.open()

        ItemBackdropFrontLayer:
            text: "Press item"
            secondary_text: "to Back"
            icon: "arrange-send-backward"
            on_press:
                root.backlayer.current = "one screen"
                root.backdrop.open()

        ItemBackdropFrontLayer:
            text: "Lower the front layer"
            secondary_text: " by 50 %"
            icon: "transfer-down"
            on_press:
                root.backdrop.open(-Window.height / 2)


<MyBackdropBackLayer@ScreenManager>
    transition: NoTransition()

    Screen:
        name: "one screen"

        ScrollView

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "5dp"

                ItemBackdropBackLayer:
                    icon: 'theater'
                    text: "TV & Home Theaters"
                ItemBackdropBackLayer:
                    icon: 'desktop-mac'
                    text: "Computers"
                ItemBackdropBackLayer:
                    icon: 'camera-plus-outline'
                    text: "Camera and Camcorders"
                ItemBackdropBackLayer:
                    icon: 'speaker'
                    text: "Speakers"
                ItemBackdropBackLayer:
                    icon: 'cellphone-iphone'
                    text: "Mobile Phones"
                ItemBackdropBackLayer:
                    icon: 'movie-outline'
                    text: "Movies"
                ItemBackdropBackLayer:
                    icon: 'gamepad-variant-outline'
                    text: "Games"
                ItemBackdropBackLayer:
                    icon: 'music-circle-outline'
                    text: "Music"

    Screen:
        name: "second screen"

        ScrollView

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "15dp"
                spacing: "10dp"

                MDLabel:
                    text: "Types of TVs Home Theater Product"
                    color: 1, 1, 1, 1

                Widget:
                    size_hint_y: None
                    height: "10dp"

                ItemBackdropBackLayerOfSecondScreen:
                    text: "Smart TV"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "4K Ultra HD TVs"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "Curved TVs"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "OLED TVs"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "LED TVs"
                ItemBackdropBackLayerOfSecondScreen:
                    text: "Home Theater Systems"

                MDSeparator:

                Widget:
                    size_hint_y: None
                    height: "15dp"

                MDLabel:
                    text: "Types of TVs Home Theater Product"
                    color: 1, 1, 1, 1

                ItemRoundBackdropBackLayerOfSecondScreen:
                    text: "TVs up to 32\\""
                ItemRoundBackdropBackLayerOfSecondScreen:
                    text: "TVs 39\\"-50\\""
                ItemRoundBackdropBackLayerOfSecondScreen:
                    text: "TVs 55\\" or larger"
'''
)

# Usage example of MDBackdrop.
Builder.load_string(
    '''
<ExampleBackdrop>

    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Example Backdrop"
        header_text: "Menu:"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
'''
)


class ExampleBackdrop(Screen):
    pass


class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "DeepPurple"

    def build(self):
        return ExampleBackdrop()


Test().run()
"""

__all__ = (
    "MDBackdropToolbar",
    "MDBackdropFrontLayer",
    "MDBackdropBackLayer",
    "MDBackdrop",
)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    BooleanProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar

Builder.load_string(
    """
<MDBackdrop>

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_color if not root.background_color \
                else root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

    MDBackdropToolbar:
        id: toolbar
        title: root.title
        elevation: 0
        md_bg_color:
            root.theme_cls.primary_color if not root.background_color \
            else root.background_color
        left_action_items: root.left_action_items
        right_action_items: root.right_action_items
        pos_hint: {'top': 1}

    _BackLayer:
        id: back_layer
        y: -toolbar.height
        padding: 0, 0, 0, "100dp"

    _FrontLayer:
        id: _front_layer
        md_bg_color: 0, 0, 0, 0
        orientation: "vertical"
        size_hint_y: None
        height: root.height - toolbar.height
        padding: root.padding

        canvas:
            Color:
                rgba: root.theme_cls.bg_normal
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: 
                    [
                    (root.radius, root.radius),
                    (0, 0),
                    (0, 0),
                    (0, 0)
                    ]

        OneLineListItem:
            id: header_button
            text: root.header_text
            divider: None
            _no_ripple_effect: True
            on_press: root.open()

        BoxLayout:
            id: front_layer
            padding: 0, 0, 0, "100dp"
"""
)


class _BackLayer(BoxLayout):
    pass


class _FrontLayer(MDCard):
    pass


class MDBackdropToolbar(MDToolbar):
    pass


class MDBackdropFrontLayer(BoxLayout):
    pass


class MDBackdropBackLayer(BoxLayout):
    pass


class MDBackdrop(ThemableBehavior, FloatLayout):
    """
    :Events:
        `on_open`
            When the front layer drops.
        `on_close`
            When the front layer rises.
    """

    padding = ListProperty([0, 0, 0, 0])
    """Padding for contents of the front layer."""

    left_action_items = ListProperty()
    """The icons and methods left of the MDToolbar in back layer.
    For more information, see the `kivymd/uix/toolbar.MDToolbar` module
    and `left_action_items` parameter.
    """

    right_action_items = ListProperty()
    """Works the same way as :attr: `left_action_items`."""

    title = StringProperty()
    """See the `kivymd/uix/toolbar.MDToolbar` module
    and `title` parameter."""

    background_color = ListProperty()
    """Background color of back layer."""

    radius = NumericProperty(25)
    """The value of the rounding radius of the upper left corner
    of the front layer.
    """

    header = BooleanProperty(True)
    """Whether to use a header above the contents of the front layer."""

    header_text = StringProperty("Header")
    """Text of header."""

    close_icon = StringProperty("close")
    """The name of the icon that will be installed on the toolbar
    on the left when opening the front layer."""

    _open_icon = ""
    _front_layer_open = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        Clock.schedule_once(
            lambda x: self.on_left_action_items(self, self.left_action_items)
        )

    def on_open(self):
        pass

    def on_close(self):
        pass

    def on_left_action_items(self, instance, value):
        if value:
            self.left_action_items = [value[0]]
        else:
            self.left_action_items = [["menu", lambda x: self.open()]]
        self._open_icon = self.left_action_items[0][0]

    def on_header(self, instance, value):
        if not value:
            self.ids._front_layer.remove_widget(self.ids.header_button)

    def open(self, open_up_to=0):
        """
        Opens the front layer.

        :open_up_to:
            the height to which the front screen will be lowered;
            if equal to zero - falls to the bottom of the screen;
        """

        self.animtion_icon_menu()
        if self._front_layer_open:
            self.close()
            return
        if open_up_to:
            y = open_up_to
        else:
            y = dp(120) - self.height
        Animation(y=y, d=0.2, t="out_quad").start(self.ids._front_layer)
        self._front_layer_open = True
        self.dispatch("on_open")

    def close(self):
        """Opens the front layer."""

        Animation(y=0, d=0.2, t="out_quad").start(self.ids._front_layer)
        self._front_layer_open = False
        self.dispatch("on_close")

    def animtion_icon_menu(self):
        icon_menu = self.ids.toolbar.ids.left_actions.children[0]
        anim = Animation(opacity=0, d=0.2, t="out_quad")
        anim.bind(on_complete=self.animtion_icon_close)
        anim.start(icon_menu)

    def animtion_icon_close(self, instance_animation, instance_icon_menu):
        instance_icon_menu.icon = (
            self.close_icon
            if instance_icon_menu.icon == self._open_icon
            else self._open_icon
        )
        Animation(opacity=1, d=0.2).start(instance_icon_menu)

    def add_widget(self, widget, index=0, canvas=None):
        if widget.__class__ in (MDBackdropToolbar, _BackLayer, _FrontLayer,):
            return super().add_widget(widget)
        else:
            if widget.__class__ is MDBackdropBackLayer:
                self.ids.back_layer.add_widget(widget)
            elif widget.__class__ is MDBackdropFrontLayer:
                self.ids.front_layer.add_widget(widget)
