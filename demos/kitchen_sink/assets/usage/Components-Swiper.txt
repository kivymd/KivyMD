from kivy.lang.builder import Builder
from kivymd.app import MDApp

kv = """
<MySwiper@MDSwiperItem>

    canvas.before:
        Color:
            rgba: app.theme_cls.bg_darkest
        RoundedRectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: 'MDSwiperItem'
        halign: 'center'

MDBoxLayout:
    orientation: 'vertical'
    spacing: '8dp'

    MDToolbar:
        id: toolbar
        title: 'MDSwiper'
        elevation: 10

    MDSwiper:

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:
"""


class Example(MDApp):
    def build(self):
        return Builder.load_string(kv)


Example().run()
