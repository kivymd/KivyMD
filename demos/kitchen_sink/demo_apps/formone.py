"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image

from kivymd.ripplebehavior import CircularRippleBehavior
from kivymd.utils.cropimage import crop_image

if not os.path.exists("./assets/market-crop.jpg"):
    crop_image(
        (Window.width, Window.height), "./assets/market.jpg", "./assets/market-crop.jpg"
    )

registration_form_one = """
#:import images_path kivymd.images_path
#:import MDFillRoundFlatButton kivymd.button.MDFillRoundFlatButton
#:import MDLabel kivymd.label.MDLabel
#:import MDTextFieldRound kivymd.textfields.MDTextFieldRound


<ButtonRound@ButtonRoundForForm>
    size_hint: None, None
    size: dp(50), dp(50)


<CircleWidget@Widget>
    size_hint: None, None
    size: dp(20), dp(20)

    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        Ellipse:
            pos: self.pos
            size: dp(20), dp(20)


<FormOne>
    name: 'registration'

    FloatLayout:
        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                source: './assets/market-crop.jpg'

        BoxLayout:
            id: box_top
            orientation: 'vertical'
            size_hint: None, None
            size: self.minimum_size
            pos_hint: {'center_x': .5, 'top': 1}
            padding: dp(5)

            BoxLayout:
                spacing: dp(5)
                size_hint_y: None
                height: dp(20)

                CircleWidget:
                CircleWidget:
                Widget:

            Widget:
                size_hint_y: None
                height: dp(5)

            Label:
                markup: True
                text: '[size=35]MAPOGO[/size]'
                size_hint: None, None
                size: self.texture_size
                bold: True
            
            BoxLayout:
                spacing: dp(5)
                size_hint: None, None
                size: self.minimum_size

                Label:
                    markup: True
                    text: '[size=20]PREMIUM UI KIT[/size]'
                    size_hint: None, None
                    size: self.texture_size
                    bold: True

                CircleWidget:

            Widget:
                size_hint_y: None
                height: dp(20)

        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: self.minimum_size
            spacing: dp(10)
            pos_hint: {'center_x': .5}
            y: box_top.height - dp(50)

            MDTextFieldRound:
                id: field_mail
                hint_text: 'Emai'
            MDTextFieldRound:
                id: field_password
                hint_text: 'Password'
                icon: 'lock-outline'

            MDLabel:
                text: 'Forgot your Password?'
                size_hint_y: None
                height: self.texture_size[1]
                color: 1, 1, 1, 1
                halign: 'center'

            Widget:
                size_hint_y: None
                height: dp(10)

            MDFillRoundFlatButton:
                text: 'Sign In'
                pos_hint: {'center_x': .5}
                on_release: root.back_to_previous_screen()

            Widget:
                size_hint_y: None
                height: dp(15)

            MDLabel:
                text: 'OR SIGN WITH A SOCIAL ACCOUNT'
                size_hint_y: None
                height: self.texture_size[1]
                color: 1, 1, 1, 1
                halign: 'center'

            Widget:
                size_hint_y: None
                height: dp(20)

            BoxLayout:
                size_hint: None, None
                width: self.minimum_width
                height: dp(50)
                spacing: dp(5)
                pos_hint: {'center_x': .5}

                ButtonRound:
                    source: './assets/google-flat-round.png'
                ButtonRound:
                    source: './assets/facebook-flat-round.png'
                ButtonRound:
                    source: './assets/twitter-flat-round.png'

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            padding: dp(5)

            canvas:
                Color:
                    rgba: 0, 0, 0, .3
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDLabel:
                text: 'Do not have an account? Create Account'
                size_hint_y: None
                height: self.texture_size[1]
                color: 1, 1, 1, 1
                halign: 'center'
                font_style: 'Caption'
"""


class FormOne(Screen):
    def back_to_previous_screen(self):
        App.get_running_app().theme_cls.primary_palette = "BlueGray"
        App.get_running_app().main_widget.ids.scr_mngr.current = "previous"
        App.get_running_app().main_widget.ids.toolbar.height = dp(56)


class ButtonRoundForForm(CircularRippleBehavior, ButtonBehavior, Image):
    pass
