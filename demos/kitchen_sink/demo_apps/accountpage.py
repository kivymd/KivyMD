"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.utils.cropimage import crop_image, crop_round_image

if not os.path.exists('./assets/sasha-round.png'):
    crop_round_image(
        (int(dp(Window.width * 30 / 100)), int(dp(Window.width * 30 / 100))),
        './assets/sasha-grey.jpg',
        './assets/sasha-round.png')
if not os.path.exists('./assets/account-background-crop.png'):
    crop_image(
        (Window.width, Window.height),
        './assets/account-background.jpeg',
        './assets/account-background-crop.png')

screen_account_page = '''
#:import Window kivy.core.window.Window
#:import MDLabel kivymd.label.MDLabel
#:import MDFillRoundFlatButton kivymd.button.MDFillRoundFlatButton
#:import MDCustomRoundIconButton kivymd.button.MDCustomRoundIconButton


<LabelAccountPage@Label>
    size_hint: None, None
    size: self.texture_size
    pos_hint: {'center_x': .5}


<BoxMinimumHeight@BoxLayout>
    size_hint_y: None
    height: self.minimum_height


<AccountPage>
    name: 'account page'

    FloatLayout:
        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                source: './assets/account-background-crop.png'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(30)

            BoxMinimumHeight:
                orientation: 'vertical'
                padding: 0, dp(50), 0, 0
                spacing: dp(30)
                pos_hint: {'top': 1}

                Image:
                    size_hint: None, None
                    size: self.size
                    source: './assets/sasha-round.png'
                    pos_hint: {'center_x': .5}

                LabelAccountPage:
                    text: 'Sasha Grey'
                    halign: 'center'
                    font_size: '30sp'
                    bold: True

                LabelAccountPage:
                    id: info
                    halign: 'center'
                    font_size: '13sp'

                LabelAccountPage:
                    id: status
                    halign: 'center'
                    opacity: 0
                    font_size: '11sp'
                    text: 'Sex without love, like food without taste...'

                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, .7
                        RoundedRectangle:
                            size: self.texture_size[0] + 20, self.texture_size[1] + 20
                            pos: self.pos[0] - 10, self.pos[1] - 10
                            radius: [25,]

            BoxLayout:
                id: box
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                opacity: 0

                canvas.before:
                    Color:
                        rgba: 1, 1, 1, .7
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos

                BoxMinimumHeight:
                    spacing: dp(10)
                    padding: 10, 0, 10, 0

                    MDFillRoundFlatButton:
                        id: button
                        text: 'MESSAGE'
                        size_hint_x: None
                        theme_text_color: 'Custom'
                        text_color: .2, .2, .2, 1
                        md_bg_color: 1, 1, 1, 1
                        pos_hint: {'center_y': .5}
            
                    MDCustomRoundIconButton:
                        size_hint: None, None
                        size: button.height, button.height
                        source: './assets/add-friend.png'

                ScrollView:

                    GridLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        cols: 1
                        padding: dp(10)
                        spacing: dp(10)

                        AnchorLayout:
                            anchor_x: 'center'
                            size_hint_y: None
                            height: box_2.height

                            canvas:
                                Color:
                                    rgba: 1, 1, 1, 1
                                RoundedRectangle:
                                    size: self.size
                                    pos: self.pos

                            BoxLayout:
                                id: box_2
                                size_hint: None, None
                                size: self.minimum_size
                                spacing: dp(40)
                                padding: dp(50), dp(10), dp(50), dp(10)

                                LabelAccountPage:
                                    text: '[size=30]368[/size]\\n[color=#ed9249][b]Friends[/b][/color]'
                                    color: .2, .2, .2, 1
                                    markup: True

                                Widget:
                                    size_hint_x: .2

                                LabelAccountPage:
                                    text: '[size=30]4368[/size]\\n[color=#ed9249][b]Followers[/b][/color]'
                                    color: .2, .2, .2, 1
                                    markup: True

                        LabelAccountPage
                            color: .2, .2, .2, 1
                            text:
                                '[color=#ed9249][b]\\n  Date of Birth[/b][/color]\\n  14.03.1988\\n\\n' \
                                '[color=#ed9249][b]\\n  Place of residence[/b][/color]\\n  SACRAMENTO, LOS ANGELES\\n\\n' \
                                '[color=#ed9249][b]\\n  Place of work[/b][/color]\\n  TOP MODEL\\n'
                            text_size: Window.width - dp(40), None
                            markup: True

                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, 1
                                RoundedRectangle:
                                    size: self.size
                                    pos: self.pos
'''


class AccountPage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Window.bind(on_keyboard=self.events_program)

    def on_enter(self, *args):
        Clock.schedule_interval(self.set_button_width, 0)
        self.l = iter(list('Former porn actress'))
        Clock.schedule_interval(self.set_label_info, 0)
        Animation(opacity=1, d=.5).start(self.ids.status)
        Animation(opacity=1, d=.5).start(self.ids.box)

    def on_leave(self, *args):
        self.ids.info.text = ''

    def set_label_info(self, interval):
        try:
            self.ids.info.text += next(self.l)
        except StopIteration:
            Clock.unschedule(self.set_label_info)

    def set_button_width(self, interval):
        self.ids.button.width = \
            Window.width - (dp(50) + self.ids.button.height)

    def events_program(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            from kivy.app import App

            App.get_running_app().main_widget.ids.scr_mngr.current = 'previous'
            App.get_running_app().main_widget.ids.toolbar.height = dp(56)
