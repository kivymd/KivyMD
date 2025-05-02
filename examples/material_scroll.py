import os
import sys

from kivy import __version__ as kv__version__
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from materialyoucolor import __version__ as mc__version__

from examples.common_app import CommonApp
from kivymd import __version__
from kivymd.app import MDApp
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)

MAIN_KV = """
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDScrollView:
        do_scroll_x: False

        MDBoxLayout:
            id: main_scroll
            orientation: "vertical"
            adaptive_height: True

            MDBoxLayout:
                adaptive_height: True

                MDLabel:
                    theme_font_size: "Custom"
                    text: "OS Info"
                    font_size: "55sp"
                    adaptive_height: True
                    padding: "10dp", "20dp", 0, 0

                MDIconButton:
                    icon: "menu"
                    on_release: app.open_menu(self)
                    pos_hint: {"center_y": .5}
"""


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
            "Pillow Version": ["Unknown", "image"],
            "Working Directory": [os.getcwd(), "folder"],
            "Home Directory": [os.path.expanduser("~"), "folder-account"],
            "Environment Variables": [os.environ, "code-json"],
        }

        try:
            from PIL import __version__ as pil__version_

            info["Pillow Version"] = ["v" + pil__version_, "image"]
        except Exception:
            pass

        for info_item in info:
            self.root.ids.main_scroll.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        icon=info[info_item][1],
                    ),
                    MDListItemHeadlineText(
                        text=info_item,
                    ),
                    MDListItemSupportingText(
                        text=str(info[info_item][0]),
                    ),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )

        Window.size = [dp(350), dp(600)]


Example().run()
