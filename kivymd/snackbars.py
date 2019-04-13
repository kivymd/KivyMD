# -*- coding: utf-8 -*-

"""
Snackbars
=========

Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Snackbars <https://material.io/design/components/snackbars.html>`
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout

from kivymd.button import MDFlatButton

Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import MDLabel kivymd.label.MDLabel


<Snackbar>:

    BoxLayout:
        id: box
        size_hint_y: None
        height: dp(58)
        spacing: dp(5)
        padding: dp(10)
        y: -self.height

        canvas:
            Color:
                rgba: get_color_from_hex('323232')
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            id: text_bar
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            theme_text_color: 'Custom'
            text_color: get_color_from_hex('ffffff')
            shorten: True
            shorten_from: 'right'
            pos_hint: {'center_y': .5}
''')


class Snackbar(FloatLayout):
    """A Material Design Snackbar"""

    text = StringProperty()
    """The text that will appear in the Snackbar.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` 
    and defaults to ''.
    """

    button_text = StringProperty()
    """The text that will appear in the Snackbar's button.

    .. note::
        If this variable is None, the Snackbar will have no button.

    :attr:`button_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to ''.
    """

    button_callback = ObjectProperty()
    """The callback that will be triggered when the Snackbar's
    button is pressed.

    .. note::
        If this variable is None, the Snackbar will have no button.

    :attr:`button_callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to None.
    """

    duration = NumericProperty(3)
    """The amount of time that the Snackbar will stay on screen for.

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to 3.
    """

    _interval = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.button_text != '':
            button = MDFlatButton(text=self.button_text)
            self.ids.box.add_widget(button)
            if self.button_callback:
                button.bind(on_release=self.button_callback)

    def show(self):
        """Show the Snackbar."""

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.duration:
                anim = Animation(y=-self.ids.box.height, d=.2)
                anim.bind(on_complete=lambda *args: Window.parent.remove_widget(self))
                anim.start(self.ids.box)
                Clock.unschedule(wait_interval)
                self._interval = 0

        Window.parent.add_widget(self)
        anim = Animation(y=0, d=.2)
        anim.bind(on_complete=lambda *args: Clock.schedule_interval(wait_interval, 0))
        anim.start(self.ids.box)
