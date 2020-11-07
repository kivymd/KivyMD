![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tabs.gif)

## Example of using MDTabs:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.icon_definitions import md_icons
from kivymd.uix.tabs import MDTabsBase
from kivymd.theming import ThemeManager

demo = """
<Example@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        left_action_items: [['menu', lambda x: x]]

    MDTabs:
        id: android_tabs


<MyTab>

    FloatLayout:

        MDLabel:
            text: 'Content'
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H6'


"""

if __name__ == '__main__':
    from kivy.factory import Factory
    from kivymd.button import MDIconButton


    class MyTab(BoxLayout, MDTabsBase):
        pass


    class Example(App):
        title = 'Example Tabs'
        theme_cls = ThemeManager()
        list_name_icons = list(md_icons.keys())[0:15]

        def build(self):
            Builder.load_string(demo)
            screen = Factory.Example()

            for name_tab in self.list_name_icons:
                tab = MyTab(text=name_tab)
                screen.ids.android_tabs.add_widget(tab)
            return screen


    Example().run()
```

If you want to use text instead of icons in tabs, simply assign a text value to the **text** parameter in **MDTab**, which is not in the **md_icon** dictionary:

```python
        def build(self):

            ...

            for name_tab in self.list_name_icons:
                tab = MyTab(text=' '.join(name_tab.split('-')).capitalize())
                screen.ids.android_tabs.add_widget(tab)
```

![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tabs-text.gif)

## AndroidTabs properties

- *default_tab* - Index of the default tab. NumericProperty(0)
- *tab_bar_height* - Height of the tab bar. NumericProperty('48dp')
- *tab_indicator_anim* - Tab indicator animation. BooleanProperty(True)
- *tab_indicator_height* - Height of the tab indicator. NumeriProperty('2dp')
- *anim_duration* - Duration of the slide animation. NumericProperty(0.2)
- *anim_threshold* - Accepts 0.0 to 1.0 and directly affects indicator animation effect. BoundedNumeriProperty(0.8)

## AndroidTabsLabel properties

- *text_color_normal* - Text color of the label when it is not selected. VariableListProperty([1, 1, 1, .6])
- *text_color_active* -  Text color of the label when it is selected. VariableListProperty([1])

## Original AndroidTabs library

https://github.com/kivy-garden/garden.androidtabs