> MDExpansionPanel will be added in KivyMD v0.101.0

![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/accordionlistitem.gif)

## Example of using MDExpansionPanel:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch
from kivymd.theming import ThemeManager
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.toast import toast

Builder.load_string('''
#:import get_hex_from_color kivy.utils.get_hex_from_color


<ContentForAnimCard>
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
            on_press: root.callback(self.text)
        Widget:
        MDRoundFlatButton:
            text: "Free message"
            on_press: root.callback(self.text)
        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: root.callback(self.text)
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'


<ExampleExpansionPanel@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]

    Screen:

        ScrollView:

            GridLayout:
                id: anim_list
                cols: 1
                size_hint_y: None
                height: self.minimum_height
''')


class ContentForAnimCard(BoxLayout):
    callback = ObjectProperty(lambda x: None)


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Example Expansion Panel"
    main_widget = None

    def build(self):
        self.main_widget = Factory.ExampleExpansionPanel()
        return self.main_widget

    def on_start(self):
        def callback(text):
            toast(f'{text} to {content.name_item}')

        content = ContentForAnimCard(callback=callback)
        names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko')

        for name_contact in names_contacts:
            self.main_widget.ids.anim_list.add_widget(
                MDExpansionPanel(content=content,
                                 icon='data/logo/kivy-icon-128.png',
                                 title=name_contact))


if __name__ == "__main__":
    Example().run()
```