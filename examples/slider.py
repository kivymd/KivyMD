from kivy.lang import Builder

from kivymd.uix.slider import MDSlider, MDSliderHandle, MDSliderValueLabel
from kivymd.app import MDApp

from examples.common_app import CommonApp, KV


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        self.root.ids.widget_box.add_widget(
            MDSlider(
                MDSliderHandle(),
                MDSliderValueLabel(),
                step=10,
                value=50,
            )
        )
        self.root.ids.custom_widget_box.add_widget(
            MDSlider(
                MDSliderHandle(
                    theme_bg_color="Custom",
                    md_bg_color="teal",
                    state_layer_color="black",
                ),
                step=10,
                value=50,
                track_active_color="green",
                track_inactive_color="lightgreen",
                track_active_step_point_color="white",
                track_inactive_step_point_color="green",
            )
        )


Example().run()
