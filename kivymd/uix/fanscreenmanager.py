"""
Fan Screen Manager
==================

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Attention! This is an experimental widget.
Perhaps the wrong positioning of the screens with a large number of them.

Thanks for reply - https://groups.google.com/forum/#!topic/kivy-users/ReAVg8eDrDo

Example
-------

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.button import MDIconButton
from kivymd.fanscreenmanager import MDFanScreen
from kivymd.list import ILeftBodyTouch
from kivymd.theming import ThemeManager


Builder.load_string('''
#:import get_hex_from_color kivy.utils.get_hex_from_color


<TestFanScreenManager>
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: 'Screen Tree'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: fan_screen_manager.open_fan()]]
        background_palette: 'Primary'

    MDFanScreenManager:
        id: fan_screen_manager

        canvas:
            Color:
                rgba: 0, 0, 0, .2
            Rectangle:
                pos: self.pos
                size: self.size

        ScreenOne:
            name: 'Screen One'
            on_enter: toolbar.title = self.name

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        ScreenTwo:
            name: 'Screen Two'
            on_enter: toolbar.title = self.name

        ScreenTree:
            name: 'Screen Tree'
            on_enter: toolbar.title = self.name

            canvas.before:
                Color:
                    rgba: .9, .9, .8, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

###############################################################################
#
#                              SCREEN WIDGETS
#
###############################################################################

<ScreenTwo>
    orientation: 'vertical'
    spacing: dp(10)

    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'demos/kitchen_sink/assets/crop-blur.jpg'

    Image:
        source: 'demos/kitchen_sink/assets/twitter-red.png'
        size_hint: None, None
        size: dp(60), dp(60)
        pos_hint: {'center_x': .5}

    Label:
        text: 'Registration'
        size_hint_y: None
        height: self.texture_size[1]
        font_size: '20sp'
        bold: True

    Widget:
        size_hint_y: None
        height: dp(10)

    MDTextFieldRect:
        size_hint: None, None
        size: root.width - dp(40), dp(30)
        pos_hint: {'center_x': .5}

    MDTextFieldRect:
        size_hint: None, None
        size: root.width - dp(40), dp(30)
        pos_hint: {'center_x': .5}

    Widget:
        size_hint_y: None
        height: dp(20)

    Label:
        text: 'Enter your Login and Password'
        size_hint_y: None
        height: self.texture_size[1]

    AnchorLayout:
        anchor_y: 'bottom'
        padding: dp(10)

        MDRoundFlatButton:
            text: "Registration"
            pos_hint: {'center_x': .5}


<ScreenOne>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    Image:
        size_hint_y: None
        source: 'data/logo/kivy-icon-512.png'

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:
        MDRoundFlatButton:
            text: "Free call"
        Widget:
        MDRoundFlatButton:
            text: "Free message"
        Widget:

    OneLineIconListItem:
        text: "Video call"
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'

    Widget:
''')


class TestFanScreenManager(BoxLayout):
    pass


class ScreenOne(MDFanScreen):
    pass


class ScreenTwo(MDFanScreen):
    pass


class ScreenTree(ScreenOne):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class MyApp(MDApp):

    def build(self):
        return TestFanScreenManager()


MyApp().run()
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.metrics import dp


class MDFanScreenManager(FloatLayout):
    shift_x = 0
    shift_y = 0
    count_screens = 0
    selected_screen = None
    fan = "close"

    def open_fan(self):
        list_screens = self.children
        self.shift_x = len(list_screens) * 20 + 20
        self.shift_y = len(list_screens) * 30 + 40

        if self.fan == "open":
            self.close_fan(list_screens[0])
            return

        for screen in list_screens:
            self.shift_x -= 20
            self.shift_y -= 40
            Animation(x=dp(self.shift_x), y=-dp(self.shift_y), d=0.05).start(
                screen
            )
        self.fan = "open"

    def close_fan(self, instance_selected_screen):
        self.selected_screen = instance_selected_screen
        for screen in self.children:
            if screen is not instance_selected_screen:
                anim = Animation(x=self.width, y=0, d=0.15)
                anim.bind(on_complete=self.check_screens_closed)
                anim.start(screen)
        self.fan = "close"

    def check_screens_closed(self, animation_instance, screen_instnce):
        self.count_screens += 1
        if len(self.children) - 1 == self.count_screens:
            self.count_screens = 0
            self.set_selected_screen()

    def set_selected_screen(self):
        anim = Animation(x=0, y=0, d=0.1)
        anim.bind(on_complete=self.set_default_screens_position)
        anim.start(self.selected_screen)

    def set_default_screens_position(self, animation_instance, screen_instnce):
        for screen in self.children:
            if screen is not self.selected_screen:
                screen.x = 0
        self.remove_widget(self.selected_screen)
        self.add_widget(self.selected_screen)


class MDFanScreen(BoxLayout):
    name = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_enter")

    def on_enter(self, *args):
        pass

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.parent.fan == "open":
                self.parent.close_fan(self)
                self.dispatch("on_enter")
                return True
            else:
                return super().on_touch_down(touch)
