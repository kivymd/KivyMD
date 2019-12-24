from kivy.animation import Animation
from kivy.uix.screenmanager import Screen


class Home(Screen):
    def closing_animation_backdrop_components(
        self, instance_backdrop, instance_backlayer
    ):
        Animation(scale_x=0, scale_y=0, d=0.2).start(instance_backlayer)
        anim = Animation(opacity=0, d=0.2)
        anim.bind(on_complete=self.set_instance_backdrop_title)
        anim.start(instance_backdrop.ids.toolbar.ids.label_title)

    def opening_animation_backdrop_components(
        self, instance_backdrop, instance_backlayer
    ):
        Animation(scale_x=1, scale_y=1, d=0.2).start(instance_backlayer)
        anim = Animation(opacity=0, d=0.2)
        anim.bind(on_complete=self.set_instance_backdrop_title)
        anim.start(instance_backdrop.ids.toolbar.ids.label_title)

    def set_instance_backdrop_title(
        self, instance_animation, instance_backdrop
    ):
        instance_backdrop.text = (
            "Menu"
            if instance_backdrop.text == "Kitchen Sink"
            else "Kitchen Sink"
        )
        Animation(opacity=1, d=0.2).start(instance_backdrop)
