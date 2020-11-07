![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/bottom-navigation.gif)

## Example of using MDBottomNavigation:

```python
from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager


class Test(App):
    theme_cls = ThemeManager()

    def build(self):
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id: toolbar
        title: 'Test MDBottomNavigation'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    MDBottomNavigation:
        id: panel

        MDBottomNavigationItem:
            name: 'files1'
            text: 'Python'
            icon: 'language-python'

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                pos_hint: {'center_x': .5, 'center_y': .5}

                MDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Primary'
                    text: 'Toggle to set custom panel color'
                    halign: 'center'

                MDSwitch:
                    size_hint: None, None
                    size: dp(36), dp(48)
                    pos_hint: {'center_x': .5}
                    on_active:
                        panel.panel_color = \
                        [0.2980392156862745, 0.2823529411764706, 0.32941176470588235, 1] \
                        if self.active else app.theme_cls.bg_dark

        MDBottomNavigationItem:
            name: 'files2'
            text: 'C++'
            icon: 'language-cpp'

            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'files3'
            text: 'JS'
            icon: 'language-javascript'

            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: 'Oh god JS again'
                halign: 'center'
''')


if __name__ == "__main__":
    Test().run()
```

Or MDBottomNavigation with custom of panel color:

![bottom-navigation-with-custom-color-panel.png](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/bottom-navigation-with-custom-color-panel.png)

```
    MDBottomNavigation:
        panel_color:
            [0.2980392156862745, 0.2823529411764706, 0.32941176470588235, 1]
```