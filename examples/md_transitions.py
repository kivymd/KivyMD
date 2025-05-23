from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp


class AnimBox(BoxLayout):
    obj_pos = ListProperty([0, 0])


UI = """
<AnimBox>:
    transition:"in_out_bounce"
    size_hint_y:None
    height:dp(100)
    obj_pos:[dp(40), self.pos[-1] + dp(40)]
    canvas:
        Color:
            rgba:app.theme_cls.primaryContainerColor
        Rectangle:
            size:[self.size[0], dp(5)]
            pos:self.pos[0], self.pos[-1] + dp(50)
        Color:
            rgba:app.theme_cls.primaryColor
        Rectangle:
            size:[dp(30)] * 2
            pos:root.obj_pos
    MDLabel:
        adaptive_height:True
        text:root.transition
        padding:[dp(10), 0]
        halign:"center"

MDGridLayout:
    orientation:"lr-tb"
    cols:1
    md_bg_color:app.theme_cls.backgroundColor
    spacing:dp(10)
"""


class MotionApp(MDApp):
    def build(self):
        return Builder.load_string(UI)

    def on_start(self):
        for transition in [
            "easing_linear",
            "easing_accelerated",
            "easing_decelerated",
            "easing_standard",
            "in_out_cubic",
        ]:  # Add more here for comparison
            print(transition)
            widget = AnimBox()
            widget.transition = transition
            self.root.add_widget(widget)
        Clock.schedule_once(self.run_animation, 1)

    _inverse = True

    def run_animation(self, dt):
        x = (self.root.children[0].width - dp(30)) if self._inverse else 0
        for widget in self.root.children:
            Animation(
                obj_pos=[x, widget.obj_pos[-1]], t=widget.transition, d=3
            ).start(widget)
        self._inverse = not self._inverse
        Clock.schedule_once(self.run_animation, 3.1)


MotionApp().run()
