from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.modalview import ModalView

from kivymd.theming import ThemableBehavior

Builder.load_string("""
#:import images_path kivymd.images_path


<BaseDialog>
    background: '{}/transparent.png'.format(images_path)

    canvas.before:
        Color:
            rgba: root.canvas_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
""")


class BaseDialog(ThemableBehavior, ModalView):
    canvas_color = ListProperty()
    callback = ObjectProperty(lambda x: None)

    def __init__(self, **kwargs):
        super(BaseDialog, self).__init__(**kwargs)
        self.canvas_color = self.theme_cls.primary_color
        self.canvas_color[3] = .75
