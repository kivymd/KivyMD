"""
Progress Bar
============

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

from kivy.lang import Builder
from kivy.properties import OptionProperty, BooleanProperty

from kivymd.theming import ThemableBehavior
from kivy.uix.progressbar import ProgressBar

Builder.load_string(
    """
<MDProgressBar>
    canvas:
        Clear
        Color:
            rgba: self.theme_cls.divider_color
        Rectangle:
            size:
                (self.width , dp(4)) if self.orientation == 'horizontal'\
                else (dp(4),self.height) 
            pos:
                (self.x, self.center_y - dp(4))\
                if self.orientation == 'horizontal'\
                else (self.center_x - dp(4),self.y)
        Color:
            rgba: self.theme_cls.primary_color
        Rectangle:
            size:
                (self.width * self.value_normalized, sp(4))\
                if self.orientation == 'horizontal' else (sp(4),\
                self.height*self.value_normalized)
            pos:
                (self.width*(1 - self.value_normalized) + self.x\
                if self.reversed else self.x, self.center_y - dp(4))\
                if self.orientation == 'horizontal'\
                else (self.center_x - dp(4),self.height\
                * (1 - self.value_normalized) + self.y if self.reversed\
                else self.y)
"""
)


class MDProgressBar(ThemableBehavior, ProgressBar):
    reversed = BooleanProperty(False)
    """ Reverse the direction the progressbar moves. """

    orientation = OptionProperty("horizontal", options=["horizontal", "vertical"])
    """ Orientation of progressbar"""


if __name__ == "__main__":
    from kivy.app import App
    from kivymd.theming import ThemeManager

    class ProgressBarApp(App):
        theme_cls = ThemeManager()

        def build(self):
            return Builder.load_string(
                """
#:import MDSlider kivymd.slider.MDSlider


BoxLayout:
    orientation:'vertical'
    padding: '8dp'
    MDSlider:
        id:slider
        min:0
        max:100
        value: 40

    MDProgressBar:
        value: slider.value
    MDProgressBar:
        reversed: True
        value: slider.value
    BoxLayout:
        MDProgressBar:
            orientation:"vertical"
            reversed: True
            value: slider.value

        MDProgressBar:
            orientation:"vertical"
            value: slider.value
"""
            )

    ProgressBarApp().run()
