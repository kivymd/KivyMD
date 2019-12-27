![textfieldrect.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/textfieldrect.gif)

## Example of using MDTextFieldRect:

```python
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window

from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image

Builder.load_string("""
<ExampleMDTextFieldRect@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(10)

    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'demos/kitchen_sink/assets/crop-blur.jpg'

    Image:
        source: 'demos/kitchen_sink/assets/twitter-red.png'
        size_hint: None, None
        size: dp(60), dp(60)
        pos_hint: {'center_x': .5}

    Label:
        text: 'Registration'
        size_hint_y: None
        height: self.texture_size[1]
        font_size: '20sp'
        bold: True

    Widget:
        size_hint_y: None
        height: dp(10)

    MDTextFieldRect:
        size_hint: None, None
        size: root.width - dp(40), dp(30)
        pos_hint: {'center_x': .5}

    MDTextFieldRect:
        size_hint: None, None
        size: root.width - dp(40), dp(30)
        pos_hint: {'center_x': .5}

    Widget:
        size_hint_y: None
        height: dp(20)

    Label:
        text: 'Enter your Login and Password'
        size_hint_y: None
        height: self.texture_size[1]

    AnchorLayout:
        anchor_y: 'bottom'
        padding: dp(10)

        MDRoundFlatButton:
            text: "Registration"
            pos_hint: {'center_x': .5}
""")


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'
    title = "Example MDTextFieldRect"
    main_widget = None

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        path_to_crop_image = \
            '{}/demos/kitchen_sink/assets/crop-blur.jpg'.format(self.directory)
        path_to_origin_image = \
            '{}/demos/kitchen_sink/assets/blur.jpg'.format(self.directory)

        if not os.path.exists(path_to_crop_image):
            crop_image((Window.width, Window.height),
                       path_to_origin_image,
                       path_to_crop_image)

    def build(self):
        self.main_widget = Factory.ExampleMDTextFieldRect()
        return self.main_widget


if __name__ == "__main__":
    Example().run()
```