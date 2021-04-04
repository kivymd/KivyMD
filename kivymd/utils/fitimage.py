"""
Fit Image
=========

Feature to automatically crop a `Kivy` image to fit your layout
Write by Benedikt Zwölfer

Referene - https://gist.github.com/benni12er/95a45eb168fc33a4fcd2d545af692dad


Example:
========

.. code-block:: kv

    BoxLayout:
        size_hint_y: None
        height: "200dp"
        orientation: 'vertical'

        FitImage:
            size_hint_y: 3
            source: 'images/img1.jpg'

        FitImage:
            size_hint_y: 1
            source: 'images/img2.jpg'

Example with round corners:
===========================

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fitimage-round-corners.png
    :align: center

.. code-block:: python

    from kivy.uix.modalview import ModalView
    from kivy.lang import Builder

    from kivymd import images_path
    from kivymd.app import MDApp
    from kivymd.uix.card import MDCard

    Builder.load_string(
        '''
    <Card>:
        elevation: 10
        radius: [36, ]

        FitImage:
            id: bg_image
            source: "images/bg.png"
            size_hint_y: .35
            pos_hint: {"top": 1}
            radius: [36, 36, 0, 0, ]
    ''')


    class Card(MDCard):
        pass


    class Example(MDApp):
        def build(self):
            modal = ModalView(
                size_hint=(0.4, 0.8),
                background=f"{images_path}/transparent.png",
                overlay_color=(0, 0, 0, 0),
            )
            modal.add_widget(Card())
            modal.open()


    Example().run()
"""

__all__ = ("FitImage",)

from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget

Builder.load_string(
    """
<FitImage>
    canvas.before:
        StencilPush
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        StencilUse

    canvas.after:
        StencilUnUse
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        StencilPop
"""
)


class FitImage(BoxLayout):
    source = ObjectProperty()
    container = ObjectProperty()
    radius = ListProperty([0, 0, 0, 0])
    mipmap = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, *args):
        self.container = Container(self.source, self.mipmap)
        self.bind(source=self.container.setter("source"))
        self.add_widget(self.container)

    def reload(self):
        self.container.image.reload()


class Container(Widget):
    source = ObjectProperty()
    image = ObjectProperty()

    def __init__(self, source, mipmap, **kwargs):
        super().__init__(**kwargs)
        self.image = AsyncImage(mipmap=mipmap)
        self.image.bind(on_load=self.adjust_size)
        self.source = source
        self.bind(size=self.adjust_size, pos=self.adjust_size)

    def on_source(self, instance, value):
        if isinstance(value, str):
            self.image.source = value
        else:
            self.image.texture = value
        self.adjust_size()

    def adjust_size(self, *args):
        if not self.parent or not self.image.texture:
            return

        (par_x, par_y) = self.parent.size

        if par_x == 0 or par_y == 0:
            with self.canvas:
                self.canvas.clear()
            return

        par_scale = par_x / par_y
        (img_x, img_y) = self.image.texture.size
        img_scale = img_x / img_y

        if par_scale > img_scale:
            (img_x_new, img_y_new) = (img_x, img_x / par_scale)
        else:
            (img_x_new, img_y_new) = (img_y * par_scale, img_y)

        crop_pos_x = (img_x - img_x_new) / 2
        crop_pos_y = (img_y - img_y_new) / 2

        subtexture = self.image.texture.get_region(
            crop_pos_x, crop_pos_y, img_x_new, img_y_new
        )

        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1)
            Rectangle(texture=subtexture, pos=self.pos, size=(par_x, par_y))
