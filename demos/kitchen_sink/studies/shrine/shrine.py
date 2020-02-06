"""
MDShrine demo
=============

.. seealso::

   `Material Design spec, Shrine <https://material.io/design/material-studies/shrine.html#>`

Shrine is a retail app that uses Material Design components
and Material Theming to express branding for a variety of fashion and lifestyle items.
"""

import os

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager

from kivymd.theming import ThemableBehavior


Builder.load_string(
    """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import ShrineRegisterScreen studies.shrine.baseclass.register_screen.ShrineRegisterScreen
#:import ShrineRootScreen studies.shrine.baseclass.shrine_root_screen.ShrineRootScreen


<MDShrine>
    transition: FadeTransition()

    ShrineRegisterScreen:
        title: root.title

    ShrineRootScreen:
        title: root.title
"""
)

KV_DIR = f"{os.path.dirname(__file__)}/kv"
for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())


class MDShrine(ThemableBehavior, ScreenManager):
    title = StringProperty("SHRINE")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
