"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.modalview import ModalView

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import images_path kivymd.images_path


<BaseDialogForDemo>
    background: f'{images_path}/transparent.png'

    canvas.before:
        Color:
            rgba: root.canvas_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
"""
)


class BaseDialogForDemo(ThemableBehavior, ModalView):
    canvas_color = ListProperty()
    callback = ObjectProperty(lambda x: None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas_color = self.theme_cls.primary_color
        self.canvas_color[3] = 0.75
