"""
https://gist.github.com/tshirtman/a1065cf74a788434e1162e342b130df8
Write by tshirtman - https://github.com/tshirtman

Example:
=======

from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.theming import ThemeManager

KV = '''
#:import MagicBehavior kivymd.uix.behaviors.MagicBehavior


<MDIconMagicButton@MagicBehavior+MDRaisedButton>


FloatLayout:

    MDIconMagicButton:
        text: "GROW EFFECT"
        on_release: self.grow()
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)


Example().run()
"""

from kivy.animation import Animation
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string(
    """
<MagicBehavior>
    translate_x: 0
    translate_y: 0
    scale_x: 1
    scale_y: 1
    rotate: 0

    canvas.before:
        PushMatrix
        Translate:
            x: self.translate_x or 0
            y: self.translate_y or 0
        Rotate:
            origin: self.center
            angle: self.rotate or 0
        Scale:
            origin: self.center
            x: self.scale_x or 1
            y: self.scale_y or 1
    canvas.after:
        PopMatrix
"""
)


class MagicBehavior:
    def grow(self):
        Animation.stop_all(self)
        (
            Animation(scale_x=1.2, scale_y=1.2, t="out_quad", d=0.03)
            + Animation(scale_x=1, scale_y=1, t="out_elastic", d=0.4)
        ).start(self)

    def shake(self):
        Animation.stop_all(self)
        (
            Animation(translate_x=50, t="out_quad", d=0.02)
            + Animation(translate_x=0, t="out_elastic", d=0.5)
        ).start(self)

    def wobble(self):
        Animation.stop_all(self)
        (
            (
                Animation(scale_y=0.7, t="out_quad", d=0.03)
                & Animation(scale_x=1.4, t="out_quad", d=0.03)
            )
            + (
                Animation(scale_y=1, t="out_elastic", d=0.5)
                & Animation(scale_x=1, t="out_elastic", d=0.4)
            )
        ).start(self)

    def twist(self):
        Animation.stop_all(self)
        (
            Animation(rotate=25, t="out_quad", d=0.05)
            + Animation(rotate=0, t="out_elastic", d=0.5)
        ).start(self)

    def shrink(self):
        Animation.stop_all(self)
        Animation(scale_x=0.95, scale_y=0.95, t="out_quad", d=0.1).start(self)


Factory.register("MagicBehavior", cls=MagicBehavior)
