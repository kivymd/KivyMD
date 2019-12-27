"""
Manager Swiper
==============

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

import os

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.card import MDCard
from kivymd.uix.managerswiper import MDSwiperPagination
from kivymd.theming import ThemeManager

activity = '''
#:import images_path kivymd.images_path


<MyCard>
    orientation: 'vertical'
    size_hint_y: None
    height: dp(300)
    pos_hint: {'top': 1}

    FitImage:
        source:
            f'{app.directory}/demos/kitchen_sink/assets/'\
            f'guitar-1139397_1280.png'
        size_hint: None, None
        size: root.width, dp(250)
        pos_hint: {'top': 1}

    MDLabel:
        theme_text_color: 'Custom'
        bold: True
        text_color: app.theme_cls.primary_color
        text: root.text
        size_hint_y: None
        height: dp(60)
        halign: 'center'


<ScreenOne@Screen>
    name: 'screen one'
    MyCard:
        text: 'Swipe to switch to screen one'.upper()


<ScreenTwo@Screen>
    name: 'screen two'
    MyCard:
        text: 'Swipe to switch to screen two'.upper()


<ScreenThree@Screen>
    name: 'screen three'
    MyCard:
        text: 'Swipe to switch to screen three'.upper()


<ScreenFour@Screen>
    name: 'screen four'
    MyCard:
        text: 'Swipe to switch to screen four'.upper()


<ScreenFive@Screen>
    name: 'screen five'
    MyCard:
        text: 'Swipe to switch to screen five'.upper()


<MySwiperManager>
    orientation: 'vertical'

    canvas:
        Color:
            rgba: 0, 0, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size

    MDToolbar:
        id: toolbar
        title: 'Swiper Manager'
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10
        left_action_items: [['menu', lambda x: x]]

    BoxLayout:
        padding: dp(10)
        orientation: 'vertical'

        MDSwiperManager:
            id: swiper_manager

            ScreenOne:

            ScreenTwo:

            ScreenThree:

            ScreenFour:

            ScreenFive:
'''


class MySwiperManager(BoxLayout):
    pass


class MyCard(MDCard):
    text = StringProperty('')


class Test(MDApp):
    swiper_manager = None

    def build(self):
        Builder.load_string(activity)
        start_screen = MySwiperManager()
        self.swiper_manager = start_screen.ids.swiper_manager
        paginator = MDSwiperPagination()
        paginator.screens = self.swiper_manager.screen_names
        paginator.manager = self.swiper_manager
        self.swiper_manager.paginator = paginator
        start_screen.add_widget(paginator)

        return start_screen


if __name__ == '__main__':
    Test().run()
"""

from kivy.properties import NumericProperty, ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation

from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<ItemPagination>
    size_hint: None, None
    size: dp(15), dp(15)
    pos_hint: {'center_y': .5}

    canvas:
        Color:
            rgba:
                self.theme_cls.primary_color\
                if root.current_index == 0 else root.color_round_not_active
        RoundedRectangle:
            pos: self.pos
            size: self.size


<MDSwiperPagination>
    padding: dp(5)
    size_hint: None, None
    width: self.minimum_width
    pos_hint: {'center_x': .5}
    height: dp(56)

    MDIconButton:
        icon: 'chevron-left'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        on_release: root.manager.swith_screen('right')

    BoxLayout:
        id: box
        spacing: dp(5)
        size_hint_x: None
        width: self.minimum_width

    MDIconButton:
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        icon: 'chevron-right'
        on_release: root.manager.swith_screen('left')
"""
)


class ItemPagination(ThemableBehavior, Widget):
    current_index = NumericProperty(0)
    color_round_not_active = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.color_round_not_active:
            self.color_round_not_active = self.theme_cls.primary_light


class MDSwiperPagination(ThemableBehavior, BoxLayout):
    screens = ListProperty()
    items_round_paginator = ListProperty()
    manager = ObjectProperty()

    def on_screens(self, instance, screen_names):
        self.items_round_paginator = []
        self.ids.box.clear_widgets()
        for i, screen_name in enumerate(screen_names):
            item_paginator = ItemPagination(current_index=i)
            self.ids.box.add_widget(item_paginator)
            self.items_round_paginator.append(item_paginator)

    def set_current_screen_round(self, index_screen):
        old_color = self.items_round_paginator[
            index_screen
        ].color_round_not_active
        for i, screen in enumerate(self.items_round_paginator):
            if i == index_screen:
                self.animation_set_not_active_round(
                    screen.canvas.children[0], self.theme_cls.primary_color
                )
            else:
                self.animation_set_not_active_round(
                    screen.canvas.children[0], old_color
                )

    def animation_set_not_active_round(self, instance, color):
        Animation(rgba=color, d=0.3).start(instance)


class MDSwiperManager(ScreenManager):
    swipe = False
    index_screen = NumericProperty(0)
    paginator = ObjectProperty()
    _x = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition()
        self.transition.on_complete = self.on_complete

    def on_complete(self):
        self.transition.screen_in.pos = self.pos
        self.transition.screen_out.pos = self.pos
        super(SlideTransition, self.transition).on_complete()
        self.swipe = False

    def swith_screen(self, direction):
        if direction == "right":
            if self.index_screen == 0:
                self.index_screen = len(self.screen_names) - 1
            else:
                self.index_screen -= 1
        else:
            self.index_screen += 1
        if self.index_screen >= len(self.screen_names) and direction != "right":
            self.index_screen = 0
        self.transition.direction = direction
        self.current = self.screen_names[self.index_screen]
        if self.paginator:
            self.paginator.set_current_screen_round(self.index_screen)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos) and not self.swipe:
            # When the Navigation panel is open and
            # the list of its menu is scrolled,
            # the event is also processed on the cards
            for widget in Window.children:
                if widget.__class__ is NavigationLayout:
                    if widget.state == "open":
                        return
            if touch.x < Window.width - 10:
                if self._x > touch.x:
                    direction = "left"
                else:
                    direction = "right"
                self.swipe = True
                self.swith_screen(direction)
                self._x = 0
        return super().on_touch_move(touch)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._x = touch.x
        return super().on_touch_down(touch)
