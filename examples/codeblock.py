from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


appkv = """
MDScreen:
    MDStackLayout:
        size_hint: 1, 1
        
        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: [dp(20), dp(20), dp(20), dp(20)]
            
            MDCodeBlock:
                size_hint: 1, None
                adaptive_height: True
                text: "import os"
"""


class MyApp(MDApp):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        Window.clearcolor = self.theme_cls.surfaceColor

    def build(self) -> MDScreen:
        screen = Builder.load_string(appkv)
        return screen

if __name__=="__main__":
    MyApp().run()