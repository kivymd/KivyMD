"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from kivymd.utils.cropimage import crop_image
from kivymd.ripplebehavior import CircularRippleBehavior


if not os.path.exists('./assets/coffee_crop.jpg'):
    crop_image(
        (Window.width, Window.height),
        './assets/coffee.jpg',
        './assets/coffee_crop.jpg')

screen_coffee_menu = '''
#:set coffee_color [0.33725490196078434, 0.16862745098039217, 0.0392156862745098, .7]


<CustomToolbar@BoxLayout>
    size_hint_y: None
    height: dp(56)
    spacing: dp(20)
    padding: dp(10)

    canvas:
        Color:
            rgba: coffee_color
        Rectangle:
            size: self.size
            pos: self.pos

    Image:
        source: './assets/coffee-icon.png'
        size_hint: None, None
        size: dp(46), dp(46)

    MDLabel:
        font_name: './assets/Pollywog.ttf'
        text: 'Coffee House'
        color: 1, 1, 1, 1
        font_size: '30sp'
        shorten: True


<ItemMenu>
    canvas.before:
        Color:
            rgba: coffee_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(5)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_y': .5}

        Image:
            source: root.icon_item
            size_hint: None, None
            height: root.height // 2.5
            width: self.height
            pos_hint: {'center_x': .5}

        MDLabel:
            text: root.name_item
            color: 1, 1, 1, 1
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'


<CoffeeMenu>
    name: 'coffee menu'

    FloatLayout:
        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                source: './assets/coffee_crop.jpg'

        CustomToolbar:
            id: toolbar
            y: root.app.Window.height

        BoxLayout:
            id: top_menu
            spacing: dp(5)
            padding: dp(5)
            size_hint_y: None
            height: dp(100)
            y: dp(95)
            x: Window.width

            ItemMenu:
                icon_item: './assets/menu.png'
                name_item: 'Menu'

            ItemMenu:
                icon_item: './assets/about-us.png'
                name_item: 'About Us'

            ItemMenu:
                icon_item: './assets/facebook.png'
                name_item: 'Facebook'

        BoxLayout:
            id: bottom_menu
            spacing: dp(5)
            padding: dp(5)
            size_hint_y: None
            height: dp(100)
            x: -Window.width

            ItemMenu:
                icon_item: './assets/events.png'
                name_item: 'Events'

            ItemMenu:
                icon_item: './assets/coffees.png'
                name_item: 'Coffees'

            ItemMenu:
                icon_item: './assets/back.png'
                name_item: 'Back'
                on_release: root.hide_menu_animation()
'''


class CoffeeMenu(Screen):
    app = App.get_running_app()

    def on_enter(self, *args):
        self.add_custom_toolbar()
        self.show_menu_animation()

    def add_custom_toolbar(self):
        toolbar = self.ids.toolbar
        Animation(y=Window.height - toolbar.height, d=.3).start(toolbar)

    def show_menu_animation(self):
        Animation(x=0, d=.2).start(self.ids.top_menu)
        Animation(x=Window.width - self.ids.bottom_menu.width, d=.2).start(
            self.ids.bottom_menu)

    def hide_menu_animation(self):
        Animation(x=Window.width, d=.2).start(self.ids.top_menu)
        Animation(y=Window.height, d=.2).start(self.ids.toolbar)
        anim = Animation(x=-Window.width, d=.2)
        anim.bind(on_complete=self.back_to_previous_screen)
        anim.start(self.ids.bottom_menu)

    def back_to_previous_screen(self, *args):
        self.app.main_widget.ids.scr_mngr.current = 'previous'
        self.app.main_widget.ids.toolbar.height = dp(56)


class ItemMenu(CircularRippleBehavior, ButtonBehavior, BoxLayout):
    name_item = StringProperty()
    icon_item = StringProperty()
