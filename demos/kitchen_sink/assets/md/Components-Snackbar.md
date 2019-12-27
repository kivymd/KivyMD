![chips.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/snackbar.gif)

## Example of using Snackbars:

```python
from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder

from kivymd.uix.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.toast import toast

KV = """
#:import Window kivy.core.window.Window


Screen:
    name: 'snackbar'

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)

        MDToolbar:
            title: 'Example Snackbar'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)

            Widget:

            MDRaisedButton:
                text: "Create simple snackbar"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('simple')

            MDRaisedButton:
                text: "Create snackbar with button"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('button')

            MDRaisedButton:
                text: "Create snackbar with a lot of text"
                pos_hint: {'center_x': .5}
                on_release: app.show_example_snackbar('verylong')

            MDSeparator:

            MDLabel:
                text: 'Click the MDFloatingActionButton to show the following example...'
                halign: 'center'

            Widget:

    MDFloatingActionButton:
        id: button
        md_bg_color: app.theme_cls.primary_color
        x: Window.width - self.width - dp(10)
        y: dp(10)
        on_release: app.show_example_snackbar('float')
"""


class ExampleSnackBar(App):
    theme_cls = ThemeManager()
    _interval = 0
    my_snackbar = None
    screen = None

    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def show_example_snackbar(self, snack_type):
        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.screen.ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=callback).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()
        elif snack_type == 'float':
            if not self.my_snackbar:
                self.my_snackbar = Snackbar(
                    text="This is a snackbar!", button_text='Button',
                    duration=3, button_callback=callback)
                self.my_snackbar.show()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0))
                anim.start(self.screen.ids.button)


if __name__ == "__main__":
    ExampleSnackBar().run()
```

## Example of using MDFloatingActionButton with Snackbars:

![chips.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/snackbar-2.gif)

```python
from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder

from kivymd.uix.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.toast import toast

KV = """
#:import Window kivy.core.window.Window


Screen:
    name: 'snackbar'

    Toolbar:
        title: 'Example Snackbar'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: x]]
        pos_hint: {'top': 1}

    MDFloatingActionButton:
        id: button
        md_bg_color: app.theme_cls.primary_color
        x: Window.width - self.width - dp(10)
        y: dp(10)
        on_release: app.show_example_snackbar('float')
"""


class ExampleSnackBar(App):
    theme_cls = ThemeManager()
    _interval = 0
    my_snackbar = None
    screen = None

    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def show_example_snackbar(self, snack_type):
        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.screen.ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        if not self.my_snackbar:
            self.my_snackbar = Snackbar(
                text="This is a snackbar!", button_text='Button',
                duration=3, button_callback=callback)
            self.my_snackbar.show()
            anim = Animation(y=dp(72), d=.2)
            anim.bind(on_complete=lambda *args: Clock.schedule_interval(wait_interval, 0))
            anim.start(self.screen.ids.button)


if __name__ == "__main__":
    ExampleSnackBar().run()
```