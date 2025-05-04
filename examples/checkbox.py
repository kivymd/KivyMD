from kivy.lang import Builder

from examples.common_app import KV, CommonApp
from kivymd.app import MDApp
from kivymd.uix.selectioncontrol import MDCheckbox


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.widget_box.add_widget(MDCheckbox())
        self.root.ids.custom_widget_box.add_widget(
            MDCheckbox(
                color_active="lightgreen",
                color_inactive="red",
                color_disabled="brown",
            )
        )


Example().run()
