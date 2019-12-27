![sliders.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/sliders.gif)

## Example of using MDSlider and MDProgressBar:

```python
from kivy.app import App
from kivymd.theming import ThemeManager

class SliderApp(App):
    theme_cls = ThemeManager()

    def build(self):
        return Builder.load_string(
            """
Screen
name: 'progress bar'

BoxLayout:
    orientation:'vertical'
    padding: '8dp'

    MDLabel:
        text: "Slider with [b]hint = True[/b]"
        markup: True
        halign: "center"

    MDSlider:
        id: progress_slider
        min: 0
        max: 100
        value: 40

    MDLabel:
        text: "Slider with [b]hint = False[/b]"
        markup: True
        halign: "center"

    MDSlider:
        id: progress_slider
        min: 0
        max: 100
        value: 40
        hint: False

    MDLabel:
        text: "Examples [b]MDProgressBar[/b]"
        markup: True
        halign: "center"

    MDProgressBar:
        value: progress_slider.value

    MDProgressBar:
        reversed: True
        value: progress_slider.value

    BoxLayout:
        MDProgressBar:
            orientation: "vertical"
            reversed: True
            value: progress_slider.value

        MDProgressBar:
            orientation: "vertical"
            value: progress_slider.value
"""
        )

SliderApp().run()
```