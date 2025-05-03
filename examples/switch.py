from kivy.lang import Builder

from examples.common_app import KV, CommonApp
from kivymd.app import MDApp
from kivymd.uix.selectioncontrol import MDSwitch


class Example(MDApp, CommonApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.widget_box.add_widget(
            MDSwitch(
                icon_active="check",
                icon_inactive="close",
            )
        )

        self.root.ids.custom_widget_box.add_widget(
            MDSwitch(
                icon_active="check",
                icon_inactive="close",
                md_bg_color_disabled="#b5b8b166",
                thumb_color_disabled=[1, 0, 1, 0.4],
                icon_active_color="white",
                icon_inactive_color="red",
                thumb_color_active="red",
                thumb_color_inactive="white",
                track_color_active="brown",
                track_color_inactive="teal",
                line_color_disabled="darkgrey",
                theme_line_color="Custom",
                line_color="red",
            )
        )


Example().run()
