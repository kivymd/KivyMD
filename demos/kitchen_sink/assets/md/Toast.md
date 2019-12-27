![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivy-toast.gif)

## Example of using Kivy Toast:

```python
from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.toast.kivytoast.kivytoast import toast


class Test(App):
    theme_cls = ThemeManager()

    def show_toast(self):
        toast('Test Kivy Toast')
        # toast('Test Kivy Toast', duration=3)  # toast with user duration

    def build(self):
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id: toolbar
        title: 'Test Toast'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    FloatLayout:

        MDRaisedButton:
            text: 'TEST KIVY TOAST'
            on_release: app.show_toast()
            pos_hint: {'center_x': .5, 'center_y': .5}

'''
        )


if __name__ == "__main__":
    Test().run()
```