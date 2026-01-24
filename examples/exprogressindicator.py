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
        on_active: root.dispatch("on_active", self.active)
        active: 
            root.active

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

    BoxLayout:
        spacing: "24dp"

 
        BoxLayout:
            spacing:dp(10)
            orientation:"vertical"
            padding:[dp(50), dp(80), 0, dp(20)]

            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Progress (0-100)"
                    adaptive_height: True
                MDSlider:
                    min:0
                    max:100 
                    step: 1
                    value:0 
                    on_value:
                        linear_indicator_horizontal.value = self.value
                        linear_indicator_vertical.value = self.value
                        circular_indicator.value = self.value
                    MDSliderHandle:
                    MDSliderValueLabel:


            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Amplitude (0 - 30) dp"
                    adaptive_height: True
                MDSlider:
                    min:dp(0)
                    max:dp(30)
                    step: 1
                    value:dp(3)
                    on_value:
                        linear_indicator_horizontal.amplitude = self.value
                        linear_indicator_vertical.amplitude = self.value
                        circular_indicator.amplitude = self.value
                    MDSliderHandle:
 
            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Wavelenght (0 - 100) dp"
                    adaptive_height: True
                MDSlider:
                    min:dp(0)
                    max:dp(100)
                    step: 2
                    value:dp(8)
                    on_value:
                        linear_indicator_horizontal.wave_length = self.value
                        linear_indicator_vertical.wave_length = self.value
                        circular_indicator.wave_length = self.value
                    MDSliderHandle: 

            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Wave speed (-50 - 50) dp/s"
                    adaptive_height: True
                MDSlider:
                    min:dp(-50)
                    max:dp(50)
                    step: 2
                    value:-dp(40)
                    on_value:
                        linear_indicator_horizontal.wave_speed = self.value
                        linear_indicator_vertical.wave_speed = self.value
                        circular_indicator.wave_speed = self.value
                    MDSliderHandle: 

            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Thickness (4 - 20) dp"
                    adaptive_height: True

                MDSlider:
                    min:dp(4)
                    max:dp(20)
                    step: 1
                    value:dp(4) 
                    on_value:
                        linear_indicator_horizontal.thickness = self.value
                        linear_indicator_vertical.thickness = self.value
                        circular_indicator.thickness = self.value
                    MDSliderHandle:
                    MDSliderValueLabel:

            BoxLayout:
                orientation:"vertical"
                MDLabel:
                    text: "Circular indicator size (20 - 200)dp"
                    adaptive_height: True

                MDSlider:
                    min:dp(20)
                    max:dp(240)
                    step: 2
                    value:box.size[0]
                    on_value:
                        box.size = [self.value]*2 
                    MDSliderHandle:
                    MDSliderValueLabel:

            BoxLayout:
                spacing: "12dp"
                size_hint_y:None 
                height:dp(50)

                Widget:
                MDLabel:
                    text:"Determinate"
                    adaptive_size:True
                MDSwitch:
                    active:True
                    on_active:               
                        linear_indicator_horizontal.determinate = self.active
                        linear_indicator_vertical.determinate = self.active
                        circular_indicator.determinate = self.active
                Widget:

        BoxLayout:
            spacing: "24dp"
            orientation:"vertical"
            padding:dp(20)

            MDLabel:
                id:fps
                padding:[dp(10), 0]
                halign:"center"
                text:"FPS:"
                adaptive_size:True 

            AnchorLayout:
                BoxLayout:
                    id:box
                    size_hint: None, None
                    size: [dp(50)]*2

                    MDExCircularProgressIndicator:
                        id: circular_indicator
                        active: False

            BoxLayout:
                spacing: "12dp"
                size_hint_y:None 
                height:dp(50)

                Widget:
                MDLabel:
                    text:"Retreat | Advanced"
                    adaptive_size:True
                MDSwitch:
                    on_active:               
                        circular_indicator.indeterminate_animator = "retreat" if self.active else "advanced"
                Widget:

            MDExLinearProgressIndicator: 
                color_array: [[1.0, 0.0, 0.0, 1.0], [1.0, 0.5, 0.0, 1.0], [1.0, 0.9, 0.0, 1.0], [0.0, 0.8, 0.3, 1.0], [0.0, 0.5, 1.0, 1.0], [0.6, 0.2, 0.8, 1.0]]
                id: linear_indicator_horizontal

            MDExLinearProgressIndicator:
                id: linear_indicator_vertical
                color_array: [[0.0, 0.4, 0.4, 1.0], [0.0, 0.7, 0.6, 1.0], [0.2, 0.8, 0.8, 1.0], [0.3, 0.5, 0.9, 1.0], [0.1, 0.2, 0.5, 1.0]]                
                orientation: "vertical"
                size_hint_y: None
                height: self.width

            BoxLayout:
                spacing: "12dp"
                size_hint_y:None 
                height:dp(50)

                Widget:
                MDLabel:
                    text:"Disjoint | Contiguous"
                    adaptive_size:True
                MDSwitch:
                    on_active:               
                        linear_indicator_horizontal.indeterminate_animator = "discontinuous" if self.active else ""
                        linear_indicator_vertical.indeterminate_animator = "discontinuous" if self.active else "" 
                Widget:

"""


class SelectedItem(MDBoxLayout):
    active = BooleanProperty(False)
    text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_active")

    def on_active(self, *args): ...


class Example(MDApp, CommonApp):

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_interval(self.set_fps, 0.5)

    def set_fps(self, dt):
        self.root.ids.fps.text = f"FPS: {Clock.get_rfps()}"

    def disabled_widgets(self): ...


Example().run()
