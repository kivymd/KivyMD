"""
MDFortnightly demo
=============

.. seealso::

   `Material Design spec,
   Fortnightly <https://material.io/design/material-studies/fortnightly.html#>`

    Fortnightly is an app that covers the news on a variety of topics.
    The app’s focus is on content, specifically article copy and photography.
"""

import os
import sys
from pathlib import Path

from kivy.lang import Builder

from kivymd.app import MDApp

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["FORTNIGHTLY_ROOT"] = sys._MEIPASS
else:
    os.environ["FORTNIGHTLY_ROOT"] = str(Path(__file__).parent)


KV_DIR = f"{os.environ['FORTNIGHTLY_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import FortnightlyRootScreen libs.baseclass.root_screen.FortnightlyRootScreen


ScreenManager:
    transition: FadeTransition()

    FortnightlyRootScreen:
        name: "fortnightly root screen"
"""


class MDFortnightly(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Fortnightly"
        self.icon = f"{os.environ['FORTNIGHTLY_ROOT']}/assets/images/logo.png"

    def build(self):
        FONT_PATH = f"{os.environ['FORTNIGHTLY_ROOT']}/assets/fonts/"

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "Merriweather-BlackItalic", 96, False, -1.5],
                "H2": [FONT_PATH + "LibreFranklin-Light", 60, False, -0.5],
                "H3": [FONT_PATH + "Merriweather-BlackItalic", 48, False, 0],
                "H4": [FONT_PATH + "LibreFranklin-Regular", 34, False, 0.25],
                "H5": [FONT_PATH + "LibreFranklin-Regular", 24, False, 0],
                "H6": [FONT_PATH + "Merriweather-BoldItalic", 20, False, 0.15],
                "Subtitle1": [
                    FONT_PATH + "LibreFranklin-Medium",
                    16,
                    False,
                    0.15,
                ],
                "Subtitle2": [
                    FONT_PATH + "Merriweather-Regular",
                    14,
                    False,
                    0.1,
                ],
                "Body1": [FONT_PATH + "Merriweather-Regular", 16, False, 0.5],
                "Body2": [FONT_PATH + "LibreFranklin-Regular", 14, False, 0.25],
                "Button": [FONT_PATH + "LibreFranklin-Bold", 14, True, 1.25],
                "Caption": [
                    FONT_PATH + "Merriweather-BlackItalic",
                    12,
                    False,
                    0.4,
                ],
                "Overline": [
                    FONT_PATH + "LibreFranklin-Bold",
                    10,
                    True,
                    1.5,
                ],
            }
        )
        return Builder.load_string(KV)


MDFortnightly().run()
