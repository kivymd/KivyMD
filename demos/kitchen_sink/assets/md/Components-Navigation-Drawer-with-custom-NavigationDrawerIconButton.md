![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/custom-navigation-drawer-icon-button.gif)

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.image import Image

from kivymd.uix.list import ILeftBody, OneLineAvatarListItem
from kivymd.theming import ThemeManager
from kivymd.toast import toast

main_kv = """
<ContentNavigationDrawer@MDNavigationDrawer>
    drawer_logo: 'demos/kitchen_sink/assets/drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu:"


<CustomNavigationDrawerIconButton>

    AvatarSampleWidget:
        source: root.source


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


class AvatarSampleWidget(ILeftBody, Image):
    pass


class CustomNavigationDrawerIconButton(OneLineAvatarListItem):
    source = StringProperty()

    def _set_active(self, active, nav_drawer):
        pass


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Navigation Drawer"
    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget

    def callback(self, instance, value):
        toast("Pressed item menu %d" % value)

    def on_start(self):
        for i in range(15):
            self.main_widget.ids.nav_drawer.add_widget(
                CustomNavigationDrawerIconButton(
                    text=f"Item {i}",
                    source="data/logo/kivy-icon-128.png",
                    on_press=lambda x, y=i: self.callback(x, y)
                )
            )


if __name__ == "__main__":
    Example().run()
```