![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/useranimationcard.gif)

## Example of using a class MDUserAnimationCard:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.toast import toast
from kivymd.theming import ThemeManager
from kivymd.uix.useranimationcard import MDUserAnimationCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch

# Your content for a contact card.
Builder.load_string("""
#:import get_hex_from_color kivy.utils.get_hex_from_color


<TestAnimationCard@BoxLayout>:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

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
        secondary_text: "[color=%s]Advantageous rates for calls[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        secondary_text: "[color=%s]Operator's tariffs apply[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'
""")


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Example Animation Card"

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        self.user_animation_card = None

    def build(self):
        def main_back_callback():
            toast('Close card')

        if not self.user_animation_card:
            self.user_animation_card = MDUserAnimationCard(
                user_name="User Name",
                path_to_avatar="path_to_avatar",
                callback=main_back_callback)
            self.user_animation_card.box_content.add_widget(
                Factory.TestAnimationCard())
        self.user_animation_card.open()


if __name__ == "__main__":
    Example().run()
```