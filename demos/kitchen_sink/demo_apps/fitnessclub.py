"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image

from kivymd.ripplebehavior import CircularRippleBehavior
from kivymd.utils.cropimage import crop_image

if not os.path.exists("./assets/crossfit-crop.png"):
    crop_image(
        (Window.width, Window.height),
        "./assets/crossfit.png",
        "./assets/crossfit-crop.png",
    )

screen_fitness_club = """
#:import MDBottomNavigation kivymd.bottomnavigation.MDBottomNavigation
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDLabel kivymd.label.MDLabel
#:import MDIconButton kivymd.button.MDIconButton


<InputField@MDTextFieldRect>:
    size_hint: None, None
    multiline: False
    size_hint: None, None
    size: app.Window.width - dp(50), dp(30)
    pos_hint: {'center_y': .5, 'center_x': .5}
    cursor_color: 0, 0, 0, 1


<ItemFitnessClubMenu@OneLineAvatarListItem>
    callback: None
    theme_text_color: 'Custom'
    text_color: 1, 1, 1, 1

    canvas.before:
        Color:
            rgba: 0, 0, 0, .7
        Rectangle:
            size: self.size
            pos: self.pos

    AvatarSampleWidget:
        source: './assets/arrow-right.png'

<ItemLabel@MDLabel>
    color: 1, 1, 1, 1
    font_size: '18'
    bold: True
    size_hint_y: None
    height: self.texture_size[1]


<CallUs@BoxLayout>
    orientation: 'vertical'

    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos

    Toolbar:
        text: 'Call Us'

    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(5)

        MDLabel:
            text: 'Join Us'
            color: 1, 1, 1, 1
            font_size: '20'
            bold: True
            size_hint_y: None
            height: self.texture_size[1]

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(5)
            padding: dp(10)
    
            canvas:
                Color:
                    rgba: .2, .2, .2, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [15,]

            MDTextField:
                id: name_field
                hint_text: 'Full Name'
            MDTextField:
                hint_text: 'Email Address'
            MDTextField:
                hint_text: 'Phone Number'
            MDTextField:
                hint_text: 'My Goal'
            ItemLabel:
                text: 'Comments'
            InputField:
                multiline: True
                height: dp(100)
            Widget:


<CustomToolbarForFitness@BoxLayout>
    size_hint_y: None
    height: dp(56)
    spacing: dp(20)
    padding: dp(10)

    canvas:
        Color:
            rgba: 0, 0, 0, .7
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        font_name: './assets/ua_scroonge.ttf'
        text: 'Fitness Club'
        color: 1, 1, 1, 1
        font_size: '36sp'
        shorten: True
        halign: 'center'


<MainScreen@FloatLayout>
    Button:
        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                source: './assets/crossfit-crop.png'


<Toolbar@FloatLayout>
    size_hint_y: None
    height: dp(56)
    text: ''

    Button:
        size_hint_y: None
        height: dp(56)
        pos_hint: {'top': 1}

        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                source: './assets/gradient.png'
        
    Label:
        text: root.text
        bold: True
        font_size: '26sp'
        pos_hint: {'top': 1}

    MDIconButton:
        icon: 'arrow-left'
        text: 'Back'
        pos_hint: {'top': 1}


<AboutUs@BoxLayout>
    orientation: 'vertical'
    text: ''

    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos

    Toolbar:
        text: 'About Us'

    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        Image:
            id: about_girl
            size_hint: None, None
            size: app.Window.width - dp(20), dp(200)
            source: './assets/about-us-girl-crop.png'

        ScrollView:

            Label:
                id: about_label
                text: root.text
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]
                halign: 'center'


<FitnessClub>
    name: 'fitness club'
    on_enter:
        root.set_item_menu()
        root.set_item_reg()
    #on_leave:
    #    root.set_chevron_back_screen()

    MDBottomNavigation:

        MDBottomNavigationItem:
            id: main
            name: 'main'
            text: 'Main'
            icon: 'home-variant'

            MainScreen:

                ItemMenuForFitness:
                    id: facebook
                    source: './assets/facebook-round.png'
                    size_hint: None, None
                    size: dp(50), dp(50)
                    x: -60
                    y: 50

                ItemMenuForFitness:
                    id: twitter
                    source: './assets/twitter-round.png'
                    size_hint: None, None
                    size: dp(50), dp(50)
                    x: app.Window.width
                    y: 50

                CustomToolbarForFitness:
                    id: toolbar
                    pos_hint: {'top': 1}
                
                ItemFitnessClubMenu:
                    id: exercises
                    x: app.Window.width
                    y: app.Window.height - dp(200)
                    text: 'Exercises'

                ItemFitnessClubMenu:
                    id: nutrition
                    x: app.Window.width
                    y: app.Window.height - dp(200) - dp(64)
                    text: 'Nutrition'

                ItemFitnessClubMenu:
                    id: motivation
                    x: app.Window.width
                    y: app.Window.height - dp(200) - dp(64) * 2
                    text: 'Motivation'

                ItemFitnessClubMenu:
                    id: about
                    x: app.Window.width
                    y: app.Window.height - dp(200) - dp(64) * 3
                    text: 'Back'
                    on_release:  root.back_to_previous_screen()

        MDBottomNavigationItem:
            name: 'about us'
            text: 'About Us'
            icon: 'information'
            on_tab_press:
                root.set_image(\
                './assets/about-us-girl', \
                (int(app.Window.width - dp(20)), int(dp(200))), \
                20, \
                'png')

            AboutUs:
                id: about_us
                text: root.about_text

        MDBottomNavigationItem:
            name: 'call us'
            text: 'Call Us'
            icon: 'phone'
            on_tab_press: root.set_focus(call_us.ids.name_field)
            
            CallUs:
                id: call_us
"""


class FitnessClub(Screen):
    about_text = (
        "Gym and Fitness was founded in 2002 as a family owned and operated "
        "business. The Gym and Fitness founders didn’t want it to be just "
        "another gym equipment retailer - they wanted to be the best in the "
        "industry and set their minds to doing so! Since its birth, Gym and "
        "Fitness has grown into one of Australia’s largest online fitness "
        "equipment retailers having helped over 50,000 customers live "
        "longer, happier and healthier lives"
    )

    def set_focus(self, inctanse_field):
        def set_focus(interval):
            inctanse_field.focus = True

        Clock.schedule_once(set_focus, 0.5)

    def set_image(self, path_to_image, size, corner=False, ext="png"):
        prefix = "crop"
        path_to_crop = f"{path_to_image}-{prefix}.{ext}"
        if not os.path.exists(path_to_crop):
            crop_image(size, f"{path_to_image}.{ext}", path_to_crop, corner=corner)
            self.ids.about_us.ids.about_girl.source = path_to_crop
            self.ids.about_us.ids.about_girl.reload()

    def set_item_reg(self):
        Animation(
            x=(App.get_running_app().Window.width // 2) - dp(60),
            d=0.15,
            t="in_out_bounce",
        ).start(self.ids.facebook)
        Animation(
            x=App.get_running_app().Window.width // 2, d=0.15, t="in_out_bounce"
        ).start(self.ids.twitter)

    def set_item_menu(self):
        def anim_item(*args):
            instance_item = args[0]
            Animation(
                x=(App.get_running_app().Window.width // 2) - dp(30),
                d=0.15,
                t="in_out_bounce",
            ).start(instance_item)

        Clock.schedule_once(lambda x: anim_item(self.ids.exercises), 0.1)
        Clock.schedule_once(lambda x: anim_item(self.ids.nutrition), 0.15)
        Clock.schedule_once(lambda x: anim_item(self.ids.motivation), 0.2)
        Clock.schedule_once(lambda x: anim_item(self.ids.about), 0.25)

    def back_to_previous_screen(self):
        App.get_running_app().main_widget.ids.scr_mngr.current = "previous"
        App.get_running_app().main_widget.ids.toolbar.height = dp(56)


class ItemMenuForFitness(CircularRippleBehavior, ButtonBehavior, Image):
    pass
