"""
MDShrine demo
=============

.. seealso::

   `Material Design spec,
   Shrine <https://material.io/design/material-studies/shrine.html#>`

    Shrine is a retail app that uses Material Design components
    and Material Theming to express branding for a variety of
    fashion and lifestyle items.
"""

import os
import sys
from pathlib import Path

from kivy.lang import Builder

from kivymd.app import MDApp

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["SHRINE_ROOT"] = sys._MEIPASS
else:
    os.environ["SHRINE_ROOT"] = str(Path(__file__).parent)


KV_DIR = f"{os.environ['SHRINE_ROOT']}/libs/kv"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import ShrineRegisterScreen libs.baseclass.register_screen.ShrineRegisterScreen
#:import ShrineRootScreen libs.baseclass.shrine_root_screen.ShrineRootScreen


ScreenManager:
    transition: FadeTransition()

    ShrineRegisterScreen:
        name: "register screen"

    ShrineRootScreen:
        name: "shrine root screen"
"""


class MDShrine(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Shrine"
        self.icon = f"{os.environ['SHRINE_ROOT']}/assets/images/logo.png"

    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)


MDShrine().run()
