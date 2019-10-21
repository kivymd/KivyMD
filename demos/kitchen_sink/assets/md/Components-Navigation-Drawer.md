![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/navdrawer.gif)

## Example of using a class MDNavigationDrawer:

```python
from kivy.app import App
from kivy.lang import Builder

from kivymd.uix.navigationdrawer import NavigationDrawerIconButton
from kivymd.theming import ThemeManager
from kivymd.toast import toast

main_kv = """
<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: 'demos/kitchen_sink/assets/drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu:"


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'KivyMD Kitchen Sink'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            elevation: 10
            left_action_items:
                [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]

        Widget:
"""


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget

    def callback(self, instance, value):
        toast("Pressed item menu %d" % value)

    def on_start(self):
        for i in range(15):
            self.main_widget.ids.nav_drawer.add_widget(
                NavigationDrawerIconButton(
                    icon='checkbox-blank-circle', text="Item menu %d" % i,
                    on_release=lambda x, y=i: self.callback(x, y)))


Example().run()
```