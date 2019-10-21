![popupscreen.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/popupscreen.gif)

## Example of using MDPopupScreen:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch
from kivymd.popupscreen import MDPopupScreen
from kivymd.theming import ThemeManager

Builder.load_string("""
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import Window kivy.core.window.Window


###############################################################################
#
#                              EXAMPLE TO USE
#
###############################################################################

<PopupScreen>:

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'Example Popup Screen'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        StartScreen:
            id: start_screen

            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

###############################################################################
#
#                               YOUR ROOT SCREEN
#
###############################################################################

<StartScreen>:
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: 'demos/kitchen_sink/assets/tangerines-1111529_1280.jpg'
        size_hint: 1, None
        height: dp(Window.height * 35 // 100)
        allow_stretch: True
        keep_ratio: False

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5}
        on_release: root.parent.parent.show()

    Widget:

###############################################################################
#
#                            YOUR POPUP SCREEN
#
###############################################################################

<MyPopupScreen>:
    orientation: 'vertical'

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


class PopupScreen(MDPopupScreen):
    pass


class MyPopupScreen(BoxLayout):
    pass


class StartScreen(BoxLayout):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Red'

    def build(self):
        popup_screen = MyPopupScreen()
        root = PopupScreen(screen=popup_screen,
                           background_color=[.3, .3, .3, 1])
        root.max_height = root.ids.start_screen.ids.image.height + \
            root.ids.toolbar.height + dp(5)
        return root


if __name__ == "__main__":
    MyApp().run()
```