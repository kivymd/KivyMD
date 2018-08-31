# -*- coding: utf-8 -*-

''' 
Разработано специально для проекта VKGroups -
https://github.com/HeaTTheatR/VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по услолвиям той же лицензии,
что и фреймворк Kivy.

'''

from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.metrics import dp


class Toast(ModalView):
    def __init__(self, **kwargs):
        super(Toast, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.pos_hint = {'center_x': .5, 'center_y': .1}
        self.background_color = [0, 0, 0, 0]
        self.background = 'atlas://data/images/defaulttheme/modalview-background'
        self.opacity = 0
        self.auto_dismiss = False
        self.label_toast = Label(size_hint=(None, None), opacity=0)
        self.label_toast.bind(texture_size=self.label_check_texture_size)
        self.add_widget(self.label_toast)

    def label_check_texture_size(self, instance, texture_size):
        texture_width, texture_height = texture_size
        if texture_width > Window.width:
           instance.text_size = (Window.width - dp(10), None)
           instance.texture_update()
           texture_width, texture_height = instance.texture_size
        self.size = (texture_width + 15, texture_height + 15)

    def toast(self, text_toast):
        self.label_toast.text = text_toast
        self.open()

    def on_open(self):
        self.fade_in()
        Clock.schedule_once(self.fade_out, 2.5)

    def fade_in(self):
        anim_label = Animation(opacity=0, duration=.4)
        anim_label += Animation(opacity=.1, duration=.4)
        anim_label += Animation(opacity=1, duration=.4)

        anim_body = Animation(opacity=0, duration=.4)
        anim_body += Animation(opacity=.1, duration=.4)
        anim_body += Animation(opacity=1, duration=.4)

        anim_label.start(self.label_toast)
        anim_body.start(self)

    def fade_out(self, interval):
        anim_label = Animation(opacity=1, duration=.4)
        anim_label += Animation(opacity=0, duration=.4)

        anim_body = Animation(opacity=1, duration=.4)
        anim_body += Animation(opacity=0, duration=.4)
        anim_body.bind(on_complete=lambda *x: self.dismiss())

        anim_label.start(self.label_toast)
        anim_body.start(self)


def toast(text, length_long=False):
    Toast().toast(text)

