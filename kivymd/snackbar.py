# -*- coding: utf-8 -*-
'''
Snackbar
========

`Material Design spec page <https://material.io/guidelines/components/snackbars-toasts.html>`_

API
---
'''

from collections import deque
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivymd.material_resources import DEVICE_TYPE

Builder.load_string('''
#:import Window kivy.core.window.Window
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDLabel kivymd.label.MDLabel
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE
<_SnackbarWidget>
    canvas:
        Color:
            rgb: get_color_from_hex('323232')
        Rectangle:
            size: self.size
    size_hint_y: None
    size_hint_x: 1 if DEVICE_TYPE == 'mobile' else None
    height: dp(48) if _label.texture_size[1] < dp(30) else dp(80)
    width: dp(24) + _label.width + _spacer.width + root.padding_right if root.button_text == '' else dp(24) + \
        _label.width + _spacer.width + _button.width + root.padding_right
    top: 0
    x: 0 if DEVICE_TYPE == 'mobile' else Window.width/2 - self.width/2
    BoxLayout:
        width: Window.width - root.padding_right - _spacer.width - dp(24) if DEVICE_TYPE == 'mobile' and \
            root.button_text == '' else Window.width - root.padding_right - _button.width - _spacer.width - dp(24) \
            if DEVICE_TYPE == 'mobile' else _label.texture_size[0] if (dp(568) - root.padding_right - _button.width - \
            _spacer.width - _label.texture_size[0] - dp(24)) >= 0 else (dp(568) - root.padding_right - _button.width - \
            _spacer.width - dp(24))
        size_hint_x: None
        x: dp(24)
        MDLabel:
            id: _label
            text: root.text
            theme_text_color: 'Custom'
            text_color: get_color_from_hex('ffffff')
            size: self.texture_size
    BoxLayout:
        id: _spacer
        size_hint_x: None
        x: _label.right
        width: 0
    MDFlatButton:
        id: _button
        text: root.button_text
        theme_text_color: 'Custom'
        text_color: get_color_from_hex('ffffff')
        size_hint_x: None
        x: _spacer.right if root.button_text != '' else root.right
        center_y: root.height/2
        on_release: root.button_callback()
''')


class SnackbarManager:
    playing = False
    queue = deque()

    def _play_next(self, dying_widget=None):
        if (dying_widget or not self.playing) and len(self.queue) > 0:
            self.playing = True
            self.queue.popleft().begin()
        elif len(self.queue) == 0:
            self.playing = False

    def make(self, text, button_text=None, button_callback=None, duration=3):
        if button_text is not None and button_callback is not None:
            self.queue.append(_SnackbarWidget(text=text, button_text=button_text, button_callback=button_callback,
                                              duration=duration))
        else:
            self.queue.append(_SnackbarWidget(text=text, duration=duration))
        self._play_next()


class Snackbar(EventDispatcher):
    '''
    A Material Design Snackbar
    '''
    text = StringProperty("")
    '''The text that will appear in the Snackbar.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to ''.
    '''
    button_text = StringProperty(None, allownone=True)
    '''The text that will appear in the Snackbar's button.

    .. note::
        If this variable is None, the Snackbar will have no button.

    :attr:`button_text` is a :class:`~kivy.properties.StringProperty` and defaults to None.
    '''
    button_callback = ObjectProperty(None, allownone=True)
    '''The callback that will be triggered when the Snackbar's button is pressed.

    .. note::
        If this variable is None, the Snackbar will have no button.

    :attr:`button_callback` is a :class:`~kivy.properties.ObjectProperty` and defaults to None.
    '''
    duration = NumericProperty(3)
    '''The amount of time that the Snackbar will stay on screen for.

    :attr:`duration` is a :class:`~kivy.properties.NumericProperty` and defaults to 3.
    '''

    def __init__(self, text, button_text=None, button_callback=None, duration=None):
        self.text = text
        self.button_text = button_text
        self.button_callback = button_callback
        self.duration = duration or self.duration

    def show(self):
        '''Show the Snackbar'''
        manager.make(text=self.text, button_text=self.button_text, button_callback=self.button_callback,
                     duration=self.duration)


class _SnackbarWidget(RelativeLayout):
    text = StringProperty()
    button_text = StringProperty()
    button_callback = ObjectProperty()
    duration = NumericProperty()
    padding_right = NumericProperty(dp(24))

    def __init__(self, text, duration, button_text='', button_callback=None,
                 **kwargs):
        super(_SnackbarWidget, self).__init__(**kwargs)
        self.text = text
        self.button_text = button_text
        self.button_callback = button_callback
        self.duration = duration
        self.ids['_label'].text_size = (None, None)

    def begin(self):
        if self.button_text == '':
            self.remove_widget(self.ids['_button'])
        else:
            self.ids['_spacer'].width = dp(16) if DEVICE_TYPE == "mobile" else dp(40)
            self.padding_right = dp(16)
        Window.add_widget(self)
        anim = Animation(y=0, duration=.3, t='out_quad')
        anim.start(self)
        Clock.schedule_once(lambda dt: self.die(), self.duration)

    def die(self):
        anim = Animation(top=0, duration=.3, t='out_quad')
        anim.bind(on_complete=lambda *args: manager._play_next(self))
        anim.bind(on_complete=lambda *args: Window.remove_widget(self))
        anim.start(self)

manager = SnackbarManager()
