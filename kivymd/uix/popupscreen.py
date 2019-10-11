"""
MDPopupScreen
=============

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivymd.uix.popupscreen import MDPopupScreen
from kivymd.theming import ThemeManager

Builder.load_string('''
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import Window kivy.core.window.Window


<PopupScreen>

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'Example MDPopupScreen'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        UserScreen:
            id: start_screen

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size


<UserScreen@FloatLayout>

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5, 'center_y': .6}
        on_release: root.parent.parent.show()

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        spacing: dp(10)
        padding: dp(20)
        pos_hint: {'bottom': .2}

        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: 'Toggle to set custom MDPopupScreen color'
            halign: 'center'
            shorten: True

        MDSwitch:
            size_hint: None, None
            size: dp(36), dp(48)
            pos_hint: {'center_x': .5}
            on_active:
                app.root.background_image = f'{demos_assets_path}/white-texture.png' \
                if self.active else f'{images_path}/transparent.png'

        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: 'Toggle to set custom MDPopupScreen background image'
            halign: 'center'
            shorten: True

        MDSwitch:
            size_hint: None, None
            size: dp(36), dp(48)
            pos_hint: {'center_x': .5}
            on_active:
                app.root.background_color = [0, 0, 0, .8] \
                if self.active else app.theme_cls.bg_dark

    Widget:

# Your popup screen.
<ContentForPopupScreen>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {'top': 1}

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:

        MDRoundFlatButton:
            text: "Free call"
            on_press: app.callback(self.text)

        Widget:

        MDRoundFlatButton:
            text: "Free message"
            on_press: app.callback(self.text)

        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: app.callback(self.text)

        IconLeftWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: app.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)

        IconLeftWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: app.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)

        IconLeftWidget:
            icon: 'remote'
''')


class PopupScreen(MDPopupScreen):
    pass


class ContentForPopupScreen(BoxLayout):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'
    popup_screen = None
    root = None

    def open_close_callback(self, instance, value):
        print(instance, value)

    def callback(self, value):
        print(value)
        Clock.schedule_once(self.root.hide, .5)

    def build(self):
        self.popup_screen = ContentForPopupScreen()
        self.root = PopupScreen(
            screen=self.popup_screen,
            background_color=self.theme_cls.bg_dark,
        )
        self.bind(on_open=self.open_close_callback)
        self.bind(on_close=self.open_close_callback)
        return self.root


MyApp().run()
"""

from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import (
    ObjectProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import images_path kivymd.images_path


<RootScreen>
    padding: dp(15)

    canvas.before:
        Color:
            rgba:
                self.theme_cls.bg_light if not root.background_color \
                else root.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15, ]

    canvas:
        RoundedRectangle:
            pos: self.pos
            size: self.size
            source:
                f'{images_path}/transparent.png' if not root.background_image \
                else root.background_image
            radius: [15, ]
"""
)


class RootScreen(BoxLayout, ThemableBehavior):
    background_color = ListProperty()
    background_image = StringProperty()


class MDPopupScreen(FloatLayout):
    screen = ObjectProperty()
    """Screen to be added to MDPopupScreen."""

    background_color = ListProperty()
    """Background color of MDPopupScreen."""

    background_image = StringProperty()
    """Background image of MDPopupScreen."""

    padding = NumericProperty(dp(56) + dp(10))
    """Indent of list from top of screen."""

    _added_screen = False
    _open_menu = False
    _root_screen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._root_screen = RootScreen()
        self._root_screen.y = -Window.height
        self.register_event_type("on_open")
        self.register_event_type("on_close")

    def on_open(self, *args):
        pass

    def on_close(self, *args):
        pass

    def on_background_color(self, instance, value):
        if self._root_screen:
            self._root_screen.background_color = value

    def on_background_image(self, instance, value):
        if self._root_screen:
            self._root_screen.background_image = value

    def show(self):
        if not self._added_screen:
            self._root_screen.add_widget(self.screen)
            self.add_widget(self._root_screen)
            self._added_screen = True
            self._root_screen.background_color = self.background_color
        self._open_menu = True
        Animation(y=-self.padding, d=0.2, t="in_out_bounce").start(
            self._root_screen
        )
        self.dispatch("on_open", self._open_menu)

    def hide(self, *args):
        Animation(y=-Window.height, d=0.2, t="in_out_bounce").start(
            self._root_screen
        )
        self._open_menu = False
        self.dispatch("on_close", self._open_menu)

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            if Window.height - (touch.y + dp(20)) > self.padding:
                if self._open_menu:
                    self.hide()
        return super().on_touch_down(touch)
