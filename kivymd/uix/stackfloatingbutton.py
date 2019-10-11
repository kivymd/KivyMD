"""
Stack Floating Buttons
======================

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.toast import toast
from kivymd.theming import ThemeManager
from kivymd.uix.stackfloatingbuttons import MDStackFloatingButtons


Builder.load_string('''
<ExampleFloatingButtons@BoxLayout>:
    orientation: 'vertical'

    MDToolbar:
        title: 'Stack Floating Buttons'
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['menu', lambda x: None]]

''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Example Stack Floating Buttons"
    create_stack_floating_buttons = False
    floating_data = {
        'Python': 'language-python',
        'Php': 'language-php',
        'C++': 'language-cpp'}

    def set_my_language(self, instance_button):
        toast(instance_button.icon)

    def build(self):
        screen = Factory.ExampleFloatingButtons()
        # Use this condition otherwise the stack will be created each time.
        if not self.create_stack_floating_buttons:
            screen.add_widget(MDStackFloatingButtons(
                icon='lead-pencil',
                floating_data=self.floating_data,
                callback=self.set_my_language))
            self.create_stack_floating_buttons = True
        return screen


Example().run()
"""

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import (
    StringProperty,
    DictProperty,
    ObjectProperty,
    ListProperty,
)
from kivy.metrics import dp

from kivymd.uix.card import MDCard


Builder.load_string(
    """
#:import Window kivy.core.window.Window


<FloatingButton@MDFloatingActionButton>
    x: Window.width - (self.width + dp(21))
    y: dp(25)
    size_hint: None, None
    size: dp(46), dp(46)
    elevation: 5
    md_bg_color: app.theme_cls.primary_color
    text_color: root.parent.text_color
    on_release: self.parent.callback(self)


<MDFloatingLabel>
    size_hint: None, None
    height: dp(20)
    width: label.texture_size[0]
    border_color_a: .5
    md_bg_color: app.theme_cls.primary_color
    x: -self.width

    Label:
        id: label
        color: root.parent.text_color
        bold: True
        markup: True
        text: '  %s  ' % root.text


<MDStackFloatingButtons>
    FloatingButton:
        id: f_btn_1
        icon: list(root.floating_data.values())[0]
    FloatingButton:
        id: f_btn_2
        icon: list(root.floating_data.values())[1]
    FloatingButton:
        id: f_btn_3
        icon: list(root.floating_data.values())[2]

    MDFloatingLabel:
        id: f_lbl_1
        text: list(root.floating_data.keys())[0]
        y: dp(117)
    MDFloatingLabel:
        id: f_lbl_2
        text: list(root.floating_data.keys())[1]
        y: dp(170)
    MDFloatingLabel:
        id: f_lbl_3
        text: list(root.floating_data.keys())[2]
        y: dp(226)

    MDFloatingActionButton:
        icon: root.icon
        size: dp(56), dp(56)
        x: Window.width - (self.width + dp(15))
        md_bg_color: app.theme_cls.primary_color
        text_color: root.text_color
        y: dp(15)
        on_release: root.show_floating_buttons()
"""
)


class MDFloatingLabel(MDCard):
    text = StringProperty()
    text_color = ListProperty([0, 0, 0, 1])


class MDStackFloatingButtons(FloatLayout):
    icon = StringProperty("checkbox-blank-circle")
    callback = ObjectProperty(lambda x: None)
    text_color = ListProperty([0, 0, 0, 1])
    floating_data = DictProperty()
    show = False
    in_progress = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lbl_list = [self.ids.f_lbl_1, self.ids.f_lbl_2, self.ids.f_lbl_3]
        self.btn_list = [self.ids.f_btn_1, self.ids.f_btn_2, self.ids.f_btn_3]

    def set_in_progress(self, instance_anim, instance):
        if instance is self.ids.f_btn_3:
            self.in_progress = False

    def show_floating_buttons(self):
        step = dp(46)
        if self.in_progress:
            return
        self.in_progress = True
        for i, btn in enumerate(self.btn_list):
            step += dp(56)
            anim = Animation(y=step, d=0.5, t="out_elastic")
            anim.bind(on_complete=self.set_in_progress)
            anim.start(btn)

        self.show = True if not self.show else False
        self.show_floating_labels() if self.show else self.hide_floating_labels()

    def show_floating_labels(self):
        i = 0
        for lbl in self.lbl_list:
            i += 0.3
            pos_x = Window.width - (lbl.width + dp(46 + 21 * 1.5))
            Animation(x=pos_x, d=i, t="out_elastic").start(lbl)

    def hide_floating_buttons(self):
        for btn in self.btn_list:
            Animation(y=25, d=0.5, t="in_elastic").start(btn)

    def hide_floating_labels(self):
        i = 1
        for lbl in self.lbl_list:
            i -= 0.3
            Animation(x=-lbl.width, d=i, t="out_elastic").start(lbl)
        self.hide_floating_buttons()
