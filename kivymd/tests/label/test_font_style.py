import os

from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.metrics import sp

from kivymd.app import MDApp

KV = """
MDScreen:

    MDLabel:
        id: label
        text: "Danger"
        font_style: "Danger"
        role: "large"
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

        self.theme_cls.font_styles["Danger"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "Danger",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "Danger",
                "font-size": sp(45),
            },
            "small": {
                "line-height": 1.44,
                "font-name": "Danger",
                "font-size": sp(36),
            },
        }
        return Builder.load_string(KV)

    def on_start(self):
        def on_start(*args):
            assert (
                sp(57)
                == self.theme_cls.font_styles["Danger"][
                    self.root.ids.label.role
                ]["font-size"]
            )
            self.stop()

        super().on_start()
        Clock.schedule_once(on_start, 2)


TestFontStyle().run()
