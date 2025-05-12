from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = """
<SelectedItem>
    adaptive_size: True
    spacing: "12dp"

    MDCheckbox:
        group: root.group
        on_active: root.dispatch("on_active", self.active)
        active: root.active

    MDLabel:
        text: root.text
        theme_line_height: "Custom"
        adaptive_size: True
        pos_hint: {'center_y': .5}
        line_height: 1


MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: dp(12)
        icon: "menu"

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {'center_x': .5}
        size_hint_x: .5
        padding: 0, "100dp", 0, "24dp"
        spacing: "24dp"

        MDBoxLayout:
            adaptive_height: True
            spacing: "24dp"

            MDLinearProgressIndicator:
                id: linear_indicator_horizontal

            MDLinearProgressIndicator:
                id: linear_indicator_vertical
                orientation: "vertical"
                size_hint_y: None
                height: "100dp"

            MDCircularProgressIndicator:
                id: circular_indicator
                size_hint: None, None
                size: "36dp", "36dp"
                active: False

        MDButton:
            pos_hint: {'center_x': .5}
            on_release: app.run_stop_demo()

            MDButtonText:
                id: button_text
                text: "Run demo"

        Widget:

        MDLabel:
            text: "Type"
            adaptive_height: True
            pos_hint: {'center_y': .5}

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            SelectedItem:
                text: "Determinate"
                on_active: app.set_type_indicator(*args, "determinate")

            SelectedItem:
                text: "Indeterminate"
                active: True
                on_active: app.set_type_indicator(*args, "indeterminate")
"""


class SelectedItem(MDBoxLayout):
    active = BooleanProperty(False)
    text = StringProperty()
    group = StringProperty("type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_active")

    def on_active(self, *args): ...


class Example(MDApp, CommonApp):
    type_indicator = "indeterminate"
    active_indicator = False
    demo_is_run = False

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def run_stop_demo(self):
        self.demo_is_run = not self.demo_is_run
        self.root.ids.button_text.text = (
            "Stop demo" if self.demo_is_run else "Run demo"
        )
        linear_indicator_horizontal = self.root.ids.linear_indicator_horizontal
        linear_indicator_vertical = self.root.ids.linear_indicator_vertical

        if self.demo_is_run:
            self.root.ids.circular_indicator.active = True
            if self.type_indicator == "determinate":
                linear_indicator_horizontal.start()
                linear_indicator_vertical.start()
            else:
                Animation(value=80, d=0.2).start(linear_indicator_vertical)
                Animation(value=80, d=0.2).start(linear_indicator_horizontal)
        else:
            self.root.ids.circular_indicator.active = False
            if self.type_indicator == "determinate":
                linear_indicator_horizontal.stop()
                linear_indicator_vertical.stop()
            else:
                Animation(value=0, d=0.2).start(linear_indicator_vertical)
                Animation(value=0, d=0.2).start(linear_indicator_horizontal)

    def set_type_indicator(self, instance_check, active, type_indicator):
        if active and self.demo_is_run:
            self.run_stop_demo()

        self.type_indicator = type_indicator
        linear_indicator_horizontal = self.root.ids.linear_indicator_horizontal
        linear_indicator_vertical = self.root.ids.linear_indicator_vertical

        if active:
            self.root.ids.circular_indicator.determinate = (
                True if type_indicator == "determinate" else False
            )
            if type_indicator == "determinate":
                linear_indicator_horizontal.type = type_indicator
                linear_indicator_vertical.type = type_indicator

    def disabled_widgets(self): ...


Example().run()
