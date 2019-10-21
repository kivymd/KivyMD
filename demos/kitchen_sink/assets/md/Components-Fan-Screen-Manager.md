> Attention! This is an experimental widget.
> Perhaps the wrong positioning of the screens with a large number of them.

![fansceernmanager.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/fansceernmanager.gif)

## Example of using MDFanScreenManager:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDIconButton
from kivymd.uix.fanscreenmanager import MDFanScreen
from kivymd.uix.list import ILeftBodyTouch
from kivymd.theming import ThemeManager


Builder.load_string("""
#:import get_hex_from_color kivy.utils.get_hex_from_color


<TestFanScreenManager>:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: 'Screen Tree'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: fan_screen_manager.open_fan()]]
        background_palette: 'Primary'

    MDFanScreenManager:
        id: fan_screen_manager

        canvas:
            Color:
                rgba: 0, 0, 0, .2
            Rectangle:
                pos: self.pos
                size: self.size

        ScreenOne:
            name: 'Screen One'
            on_enter: toolbar.title = self.name

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        ScreenTwo:
            name: 'Screen Two'
            on_enter: toolbar.title = self.name

        ScreenTree:
            name: 'Screen Tree'
            on_enter: toolbar.title = self.name

            canvas.before:
                Color:
                    rgba: .9, .9, .8, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

###############################################################################
#
#                                SCREEN WIDGETS
#
###############################################################################

<ScreenTwo>:
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


<ScreenOne>:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    Image:
        size_hint_y: None
        source: 'data/logo/kivy-icon-512.png'

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:
        MDRoundFlatButton:
            text: "Free call"
        Widget:
        MDRoundFlatButton:
            text: "Free message"
        Widget:

    OneLineIconListItem:
        text: "Video call"
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'

    Widget:
""")


class TestFanScreenManager(BoxLayout):
    pass


class ScreenOne(MDFanScreen):
    pass


class ScreenTwo(MDFanScreen):
    pass


class ScreenTree(ScreenOne):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'

    def build(self):
        return TestFanScreenManager()


if __name__ == "__main__":
    MyApp().run()
```