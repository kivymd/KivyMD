from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from examples.common_app import CommonApp, KV

Builder.load_string(
    """
<MyCard>
    padding: "4dp"
    size_hint_y: None
    height: "100dp"

    MDRelativeLayout:

        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}
            focus_behavior: False

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True
"""
)


class MyCustomCard(MDCard):
    text = StringProperty()


class MyCard(MDCard):
    text = StringProperty()


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def on_start(self):
        super().on_start()
        color_disabled = [
            0.4627450980392157,
            0.47058823529411764,
            0.07450980392156863,
            0.38,
        ]
        for style in ("elevated", "filled", "outlined"):
            self.root.ids.widget_box.add_widget(
                MyCard(
                    style=style,
                    text=style.capitalize(),
                    ripple_behavior=True,
                )
            )
            if style == "elevated":
                card = MyCard(
                    style=style,
                    text=style.capitalize(),
                    theme_shadow_color="Custom",
                    shadow_color="red",
                    theme_bg_color="Custom",
                    md_bg_color="white",
                    md_bg_color_disabled=color_disabled,
                    theme_shadow_offset="Custom",
                    shadow_offset=(1, -2),
                    theme_focus_color="Custom",
                    focus_color=[1, 0, 0, 0.2],
                    theme_shadow_softness="Custom",
                    shadow_softness=1,
                    theme_elevation_level="Custom",
                    elevation_level=2,
                    ripple_behavior=True,
                )
                self.root.ids.custom_widget_box.add_widget(card)
            elif style == "filled":
                self.root.ids.custom_widget_box.add_widget(
                    MyCard(
                        style=style,
                        text=style.capitalize(),
                        ripple_behavior=True,
                        theme_bg_color="Custom",
                        md_bg_color="brown",
                    )
                )
            elif style == "outlined":
                self.root.ids.custom_widget_box.add_widget(
                    MyCard(
                        style=style,
                        text=style.capitalize(),
                        ripple_behavior=True,
                        theme_line_color="Custom",
                        line_color="brown",
                        md_bg_color_disabled=color_disabled,
                    )
                )


Example().run()
