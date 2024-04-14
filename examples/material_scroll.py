import os
import sys

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy import __version__ as kv__version__
from kivymd import __version__
from kivymd.app import MDApp
from materialyoucolor import __version__ as mc__version__

from examples.common_app import CommonApp, KV

MAIN_KV = """
<Item>:
    size_hint_y:None
    height:dp(50)
    text:""
    sub_text:""
    icon:""
    spacing:dp(5)
    MDIcon:
        icon:root.icon
        size_hint:None, 1
        width:self.height
    BoxLayout:
        orientation:"vertical"
        MDLabel:
            text:root.text
        MDLabel:
            adaptive_height:True
            text:root.sub_text
            font_style:"Body"
            role:"medium"
            shorten:True
            shorten_from:"right"
            theme_text_color:"Custom"
            text_color:app.theme_cls.onSurfaceVariantColor[:-1] + [0.9]

MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    BoxLayout:
        orientation:"vertical"
        MDScrollView:
            do_scroll_x:False
            MDBoxLayout:
                spacing:dp(20)
                orientation:"vertical"
                adaptive_height:True
                id:main_scroll
                padding:[dp(10), 0]
                MDBoxLayout:
                    adaptive_height:True 
                    MDLabel:
                        theme_font_size:"Custom"
                        text:"OS Info"
                        font_size:"55sp"
                        adaptive_height:True
                        padding:[dp(10),dp(20),0,0]
                    BoxLayout:
                        orientation:"vertical"
                        size_hint_x:None
                        width:dp(70)
                        padding:[0, dp(20), dp(10),0]
                        MDIconButton:
                            on_release: app.open_menu(self)
                            size_hint: None, None
                            size:[dp(50)] * 2
                            icon: "menu"
                            pos_hint:{"center_x":0.8, "center_y":0.9}
                        Widget:
"""


class Item(BoxLayout):
    pass


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(MAIN_KV)

    def on_start(self):
        info = {
            "Name": [
                os.name,
                (
                    "microsoft"
                    if os.name == "nt"
                    else ("linux" if os.uname()[0] != "Darwin" else "apple")
                ),
            ],
            "Architecture": [os.uname().machine, "memory"],
            "Hostname": [os.uname().nodename, "account"],
            "Python Version": ["v" + sys.version, "language-python"],
            "Kivy Version": ["v" + kv__version__, "alpha-k-circle-outline"],
            "KivyMD Version": ["v" + __version__, "material-design"],
            "MaterialYouColor Version": ["v" + mc__version__, "invert-colors"],
            "Pillow Version":["Unknown", "image"],
            "Working Directory": [os.getcwd(), "folder"],
            "Home Directory": [os.path.expanduser("~"), "folder-account"],
            "Environment Variables": [os.environ, "code-json"],
        }

        try:
            from PIL import __version__ as pil__version_
            info["Pillow Version"] = ["v" + pil__version_ ,"image"] 
        except Exception:
            pass

        for info_item in info:
            widget = Item()
            widget.text = info_item
            widget.sub_text = str(info[info_item][0])
            widget.icon = info[info_item][1]
            self.root.ids.main_scroll.add_widget(widget)

        Window.size = [dp(350), dp(600)]


Example().run()
