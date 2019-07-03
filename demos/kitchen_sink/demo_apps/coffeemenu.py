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

from .basedialog import BaseDialogForDemo

if not os.path.exists("./assets/coffee_crop.jpg"):
    crop_image(
        (Window.width, Window.height), "./assets/coffee.jpg", "./assets/coffee_crop.jpg"
    )

screen_coffee_menu = """
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDLabel kivymd.label.MDLabel
#:import MDCard kivymd.cards.MDCard
#:import MDFlatButton kivymd.button.MDFlatButton

#:set coffee_color [.33725490196078434, .16862745098039217, .0392156862745098, .7]
#:set item_color [.3333333333333333, .1411764705882353, .06666666666666667, 1]


<PreviousDialogCoffee>
    size_hint: None, None
    size: dp(280), dp(420)

    BoxLayout:
        spacing: dp(10)
        orientation: 'vertical'

        Image:
            id: previous_image
            size_hint: None, None
            size: dp(280), dp(222)
            source: './assets/Latte-crop.jpg'

        BoxLayout:
            padding: dp(10)

            MDLabel:
                text:
                    "[b]Latte[/b] - is a coffee drink originally from Italy, " \
                    "consisting of milk and espresso coffee."
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                color: 1, 1, 1, 1

        BoxLayout:

            Widget:

            MDFlatButton:
                text: 'Ok'
                theme_text_color: 'Custom'
                text_color: [1, 1, 1, 1]
                on_release: root.dismiss()


<MenuDialog>
    orientation: 'vertical'
    size_hint: None, None
    size: app.Window.width - dp(45), app.Window.height - dp(85)
    spacing: dp(5)
    padding: dp(5)
    pos_hint: {'center_x': .5}

    canvas.before:
        RoundedRectangle:
            size: self.size
            pos: self.pos
            source: './assets/texture-menu.png'
            radius: [10,]

    MDLabel:
        font_name: './assets/Pollywog.ttf'
        text: 'Coffee Menu'
        color: item_color
        font_size: '20sp'
        halign: 'center'
        size_hint_y: None
        height: self.texture_size[1]

    Image:
        source: './assets/sep.png'
        size_hint_y: None
        height: dp(40)

    RecycleView:
        id: rv
        key_viewclass: 'viewclass'
        key_size: 'height'
        bar_color: coffee_color

        RecycleBoxLayout:
            padding: dp(10)
            spacing: dp(10)
            default_size: None, dp(48)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'


<ItemCoffeeMenu@OneLineAvatarListItem>
    callback: None
    theme_text_color: 'Custom'
    text_color: item_color
    on_release: root.callback()

    AvatarSampleWidget:
        source: './assets/coffee-icon-brown.png'


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
            y: app.Window.height

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
                on_release: root.show_menu_list_animation()

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
                on_release:
                    root.hide_menu_animation()
                    root.hide_toolbar_animation()

        MenuDialog:
            id: menu_dialog
            y: app.Window.height
"""


class CoffeeMenu(Screen):
    coffees_list = [
        "Americano",
        "Affogato",
        "Bicherin",
        "Vietnamese ice coffee",
        "Gallon (drink)",
        "Glace",
        "Ipoh White Coffee",
        "Cappuccino",
        "Carahillo",
        "Cortado",
        "Irish Coffee",
        "Coffee Liège",
        "Turkish coffee",
        "Coffee with liqueur",
        "Coffee with milk",
        "Coffee Tuba",
        "Coffee frappe",
        "Coffee cocktail",
        "Cuban coffee",
        "Latte",
        "Latte Macchiato",
        "Long black",
        "Lungo",
        "Macchiato",
        "Melange (coffee)",
        "Mokkachino",
        "Mocha",
        "Postum (drink)",
        "Raf-coffee",
        "Ristretto",
        "Red ah",
        "Pharisee (drink)",
        "Flat white",
        "Frappe (cocktail)",
        "Frappuccino",
        "Cold coffee",
        "Uh",
        "Espresso",
        "Espresso martini",
    ]
    menu_open = False

    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_keyboard=self.events_program)

    def on_enter(self, *args):
        self.add_custom_toolbar()
        self.show_menu_animation()
        self.set_items_menu()

    def set_items_menu(self):
        self.ids.menu_dialog.ids.rv.data = []
        for name_item in self.coffees_list:
            self.ids.menu_dialog.ids.rv.data.append(
                {
                    "viewclass": "ItemCoffeeMenu",
                    "text": str(name_item),
                    "callback": self.open_previous_coffee_info,
                }
            )

    def add_custom_toolbar(self):
        toolbar = self.ids.toolbar
        Animation(y=Window.height - toolbar.height, d=0.3).start(toolbar)

    def show_menu_animation(self):
        Animation(x=0, d=0.2).start(self.ids.top_menu)
        Animation(x=Window.width - self.ids.bottom_menu.width, d=0.2).start(
            self.ids.bottom_menu
        )

    def show_menu_list_animation(self):
        Animation(y=dp(60), d=0.6, t="out_elastic").start(self.ids.menu_dialog)
        self.menu_open = True

    def hide_menu_list_animation(self):
        Animation(y=Window.height, d=0.6, t="in_elastic").start(self.ids.menu_dialog)
        self.menu_open = False

    def hide_menu_animation(self):
        Animation(x=Window.width, d=0.2).start(self.ids.top_menu)
        anim = Animation(x=-Window.width, d=0.2)
        anim.bind(on_complete=self.back_to_previous_screen)
        anim.start(self.ids.bottom_menu)

    def hide_toolbar_animation(self):
        Animation(y=Window.height, d=0.2).start(self.ids.toolbar)

    def back_to_previous_screen(self, *args):
        if self.menu_open:
            self.menu_open = False
            self.hide_menu_list_animation()
        App.get_running_app().main_widget.ids.scr_mngr.current = "previous"
        App.get_running_app().main_widget.ids.toolbar.height = dp(56)

    def open_previous_coffee_info(self):
        PreviousDialogCoffee().open()

    def events_program(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.menu_open:
                self.hide_menu_list_animation()


class ItemMenu(CircularRippleBehavior, ButtonBehavior, BoxLayout):
    name_item = StringProperty()
    icon_item = StringProperty()


class MenuDialog(BoxLayout):
    background = StringProperty()


class PreviousDialogCoffee(BaseDialogForDemo):
    icon = StringProperty()

    def on_open(self):
        if not os.path.exists("./assets/Latte-crop.jpg"):
            crop_image(
                (int(dp(280)), int(dp(222))),
                "./assets/Latte.jpg",
                "./assets/Latte-crop.jpg",
            )
            self.ids.previous_image.reload()
