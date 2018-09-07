# -*- coding: utf-8 -*-

# TODO: Add documentation and example

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty, BooleanProperty, \
    ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from kivymd.theming import ThemableBehavior

Builder.load_string("""
#:import Window kivy.core.window.Window
#:import MDSpinner kivymd.spinner.MDSpinner


<MDUpdateSpinner>:

    AnchorLayout:
        id: body_spinner
        size_hint: None, None
        size: dp(46), dp(46)
        y: Window.height
        pos_hint: {'center_x': .5}
        anchor_x: 'center'
        anchor_y: 'center'

        canvas:
            Clear
            Color:
                rgba: root.theme_cls.primary_color
            Ellipse:
                pos: self.pos
                size: self.size

        MDSpinner:
            id: spinner
            size_hint: None, None
            size: dp(30), dp(30)
            color: root.color
""")


class MDUpdateSpinner(ThemableBehavior, FloatLayout):
    _step = 0
    _spinner_work = False
    color = ListProperty([1, 1, 1, 1])
    update = BooleanProperty(False)
    event_update = ObjectProperty(lambda x: None)

    def on_touch_move(self, touch):
        if touch.grab_current is self and not self._spinner_work:
            self._step += 18
            if self._step > dp(210):
                self._spinner_work = True
                self.start_anim_spinner()
                return
            self.ids.body_spinner.y -= 18

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            if self._step > dp(210) and not self._spinner_work:
                self.start_anim_spinner()
            else:
                self.hide_anim_spinner()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)

    def start_anim_spinner(self):
        def wait_updates(interval):
            if self.update:
                self.transform_hide_anim_spinner()
                Clock.unschedule(wait_updates)
        spinner = self.ids.body_spinner
        Animation(y=spinner.y + 76, d=.8, t='out_elastic').start(spinner)
        Clock.schedule_interval(wait_updates, .1)
        self.event_update(self)

    def transform_hide_anim_spinner(self):
        spinner = self.ids.body_spinner
        Animation(size=(0, 0), opacity=0, y=Window.height,
                  d=.2, t='in_cubic').start(spinner)
        anim = Animation(opacity=0, d=.2, t='in_cubic')
        anim.bind(on_complete=self.set_spinner)
        anim.start(self.ids.spinner)

    def hide_anim_spinner(self):
        if not self._spinner_work:
            spinner = self.ids.body_spinner
            Animation(y=Window.height, d=.8, t='out_elastic').start(spinner)
            self.reset_value()

    def set_spinner(self, *args):
        body_spinner = self.ids.body_spinner
        body_spinner.size = (dp(46), dp(46))
        body_spinner.y = Window.height
        body_spinner.opacity = 1
        spinner = self.ids.spinner
        spinner.size = (dp(30), dp(30))
        spinner.opacity = 1
        self.reset_value()

    def reset_value(self):
        self._step = 0
        self._spinner_work = False
        self.update = False
