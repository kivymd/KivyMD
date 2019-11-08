"""
Snackbars
=========

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Snackbars <https://material.io/design/components/snackbars.html>`_

Example
=======

from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder

from kivymd.uix.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.toast import toast

KV = '''
#:import Window kivy.core.window.Window


Screen:
    name: 'snackbar'

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)

        MDToolbar:
            title: 'Example Snackbar'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)

            Widget:

            MDRaisedButton:
                text: "Create simple snackbar"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('simple')

            MDRaisedButton:
                text: "Create snackbar with button"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('button')

            MDRaisedButton:
                text: "Create snackbar with a lot of text"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('verylong')

            MDSeparator:

            MDLabel:
                text: 'Click the MDFloatingActionButton to show the following example...'
                halign: 'center'

            Widget:

    MDFloatingActionButton:
        id: button
        md_bg_color: app.theme_cls.primary_color
        x: Window.width - self.width - dp(10)
        y: dp(10)
        on_release: app.show_example_snackbar('float')
'''


class ExampleSnackBar(MDApp):
    _interval = 0
    my_snackbar = None
    screen = None

    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def show_example_snackbar(self, snack_type):
        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.screen.ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=callback).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()
        elif snack_type == 'float':
            if not self.my_snackbar:
                self.my_snackbar = Snackbar(
                    text="This is a snackbar!", button_text='Button',
                    duration=3, button_callback=callback)
                self.my_snackbar.show()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0))
                anim.start(self.screen.ids.button)


ExampleSnackBar().run()
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.button import MDFlatButton

Builder.load_string(
    """
#:import get_color_from_hex kivy.utils.get_color_from_hex


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
            font_size: root.font_size
            theme_text_color: 'Custom'
            text_color: get_color_from_hex('ffffff')
            shorten: True
            shorten_from: 'right'
            pos_hint: {'center_y': .5}
"""
)


class Snackbar(FloatLayout):
    """A Material Design Snackbar"""

    text = StringProperty()
    """The text that will appear in the Snackbar.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` 
    and defaults to ''.
    """

    font_size = NumericProperty("15sp")
    """The font size of the text that will appear in the Snackbar.
    
    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty` and
    defaults to 15sp.
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
        if self.button_text != "":
            button = MDFlatButton(text=self.button_text)
            self.ids.box.add_widget(button)
            if self.button_callback:
                button.bind(on_release=self.button_callback)

    def show(self):
        """Show the Snackbar."""

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.duration:
                anim = Animation(y=-self.ids.box.height, d=0.2)
                anim.bind(
                    on_complete=lambda *args: Window.parent.remove_widget(self)
                )
                anim.start(self.ids.box)
                Clock.unschedule(wait_interval)
                self._interval = 0

        Window.parent.add_widget(self)
        anim = Animation(y=0, d=0.2)
        anim.bind(
            on_complete=lambda *args: Clock.schedule_interval(wait_interval, 0)
        )
        anim.start(self.ids.box)
