from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFabButton

KV = """
MDScreen:

    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class TestFabSizeM3Style(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def check_size_button(self, *args):
        data = {
            "large": [96.0, 96.0],
            "small": [40.0, 40.0],
            "standard": [56.0, 56.0],
        }
        for button in self.root.ids.box.children:
            assert button.size == data[button.style]

        self.stop()

    def on_start(self):
        styles = ["standard", "small", "large"]
        for style in styles:
            self.root.ids.box.add_widget(
                MDFabButton(icon="pencil", style=style)
            )

        Clock.schedule_once(self.check_size_button, 1.2)


TestFabSizeM3Style().run()
