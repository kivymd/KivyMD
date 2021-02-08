from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.behaviors import (ButtonBehavior)
from kivymd.uix.behaviors import (
    RectangularElevationBehavior,
    CircularElevationBehavior,
    RoundedRectangularElevationBehavior,
    CircularRippleBehavior,
    SpecificBackgroundColorBehavior
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import  Clock
class ElevationScreen(Screen):
    Filled=BooleanProperty(False)
    clean_event=ObjectProperty()

    def on_enter(self,*dt):
        # optimized code to allow a faster comeback
        if self.clean_event:
            self.clean_event.cancel()
        if self.Filled is False:
            for i in range(32):
                self.ids.container_box_1.add_widget(
                    Elevation_Example_Box(
                        elevation=i,
                        size=[60,60],
                        size_hint=[None,None]
                    )
                )
                self.ids.container_box_2.add_widget(
                    Elevation_Example_Circle(
                        elevation=i,
                        size=[60,60],
                        size_hint=[None,None]
                    )
                )
                self.ids.container_box_3.add_widget(
                    Elevation_Example_Rounded(
                        elevation=i,
                        size=[70,40],
                        size_hint=[None,None]
                    )
                )
            self.Filled=True

    def on_leave(self,*dt):
        self.clean_event = Clock.schedule_once(self.clear_screen,10)

    def clear_screen(self,*dt):
        self.ids.container_box_1.clear_widgets()
        self.ids.container_box_2.clear_widgets()
        self.ids.container_box_3.clear_widgets()
        self.Filled=False

    pass

class Elevation_Example_Box(
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    ButtonBehavior,
    BoxLayout,
    # BoxLayout
):
    animation=ObjectProperty()
    md_bg_color=[1]*4

class Elevation_Example_Circle(
    CircularElevationBehavior,
    CircularRippleBehavior,
    SpecificBackgroundColorBehavior,
    ButtonBehavior,
    BoxLayout,
):
    animation=ObjectProperty()
    md_bg_color=[1]*4
    def on_size(self, *dt):
        self.radius=[self.size[0]/2]

class Elevation_Example_Rounded(
    RoundedRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    ButtonBehavior,
    BoxLayout,
):
    animation=ObjectProperty()
    md_bg_color=[1]*4
