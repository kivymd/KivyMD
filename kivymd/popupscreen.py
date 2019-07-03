"""
Popup Screen
============

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout

from kivymd.button import MDIconButton
from kivymd.list import ILeftBodyTouch
from kivymd.popupscreen import MDPopupScreen
from kivymd.theming import ThemeManager

Builder.load_string('''
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import Window kivy.core.window.Window


###############################################################################
#
#                              EXAMPLE TO USE
#
###############################################################################

<PopupScreen>

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'Example Popup Screen'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        StartScreen:
            id: start_screen

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

###############################################################################
#
#                               YOUR ROOT SCREEN
#
###############################################################################

<StartScreen>
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: 'demos/kitchen_sink/assets/tangerines-1111529_1280.jpg'
        size_hint: 1, None
        height: dp(Window.height * 35 // 100)
        allow_stretch: True
        keep_ratio: False

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5}
        on_release: root.parent.parent.show()

    Widget:

###############################################################################
#
#                            YOUR POPUP SCREEN
#
###############################################################################

<MyPopupScreen>
    orientation: 'vertical'

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


class PopupScreen(MDPopupScreen):
    pass


class MyPopupScreen(BoxLayout):
    pass


class StartScreen(BoxLayout):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'

    def build(self):
        popup_screen = MyPopupScreen()
        root = PopupScreen(screen=popup_screen,
                           background_color=[.3, .3, .3, 1])
        root.max_height = root.ids.start_screen.ids.image.height\
            + root.ids.toolbar.height + dp(5)
        return root


MyApp().run()
"""

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<RootScreen>
    padding: dp(15)

    canvas:
        Color:
            rgba:
                self.theme_cls.bg_light if not len(root.background_color)\
                else root.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15, ]
"""
)


class RootScreen(BoxLayout, ThemableBehavior):
    background_color = ListProperty()


class MDPopupScreen(FloatLayout):
    screen = ObjectProperty()
    background_color = ListProperty()
    added_screen = False
    max_height = dp(100)
    open_menu = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_screen = RootScreen()
        self.root_screen.y = -Window.height

    def show(self):
        if not self.added_screen:
            self.root_screen.add_widget(self.screen)
            self.add_widget(self.root_screen)
            self.added_screen = True
            self.root_screen.background_color = self.background_color
        self.open_menu = True
        Animation(y=-self.max_height, d=0.2, t="in_out_bounce").start(self.root_screen)

    def hide(self, interval):
        Animation(y=-Window.height, d=0.2, t="in_out_bounce").start(self.root_screen)
        self.open_menu = False

    def on_touch_down(self, touch):
        if touch.button == "scrollup" or touch.button == "scrolldown":
            return
        if self.open_menu:
            Clock.schedule_once(self.hide, 0.3)
        return super().on_touch_down(touch)
