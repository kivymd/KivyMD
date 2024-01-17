from kivy.lang import Builder

from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.app import MDApp

from examples.common_app import CommonApp, KV


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        self.root.ids.widget_box.add_widget(MDCheckbox())
        self.root.ids.custom_widget_box.add_widget(
            MDCheckbox(
                color_active="lightgreen",
                color_inactive="red",
                color_disabled="brown",
            )
        )


Example().run()
