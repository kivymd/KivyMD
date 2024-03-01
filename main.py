from glob import glob
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp

from examples.common_app import CommonApp, KV

MAIN_KV = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    BoxLayout:
        orientation:"vertical"
        padding:[dp(16),0]
        MDCarousel:
            id:carousel
            size_hint_y:None
            height:dp(200)
        MDSlider:
            step: 20
            value: 50   
            MDSliderHandle:
            MDSliderValueLabel:
        Widget:

"""

class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Mediumspringgreen"
        return Builder.load_string(MAIN_KV)

    def on_start(self):
        super().on_start()
        self.root.ids.carousel.data = [
        #    {"source":path} for path in glob("/home/tdynamos/Pictures/Screenshots/*")[:20]
           {"text":str(_+1)} for _ in range(20)
        ] 

Example().run()
