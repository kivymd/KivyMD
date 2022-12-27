import os

from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles

KV = """
MDScreen:

    MDLabel:
        id: label
        text: "Danger"
        font_style: "Danger"
        halign: "center"
        font_size: "66sp"
"""


class TestFontStyle(MDApp):
    def build(self):
        LabelBase.register(
            name="Danger",
            fn_regular=os.path.join(
                os.path.dirname(__file__).split("label")[0],
                "data",
                "danger.ttf",
            ),
        )

        theme_font_styles.append("Danger")
        self.theme_cls.font_styles["Danger"] = [
            "Danger",
            66,
            False,
            0.15,
        ]
        return Builder.load_string(KV)

    def on_start(self):
        def on_start(*args):
            assert 100 < self.root.ids.label.texture_size[1]
            self.stop()

        Clock.schedule_once(on_start, 2)


TestFontStyle().run()
