![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/navdrawer.gif)

## Example of using a class MDNavigationDrawer:

## Using MDNavigationDrawer has changed!

You should now use this markup structure:

```python
Root:

    NavigationLayout:

        ScreenManager:

            ...
            ...

        MDNavigationDrawer:

            UserContentNavigationDrawer:
```

`MDNavigationDrawer` is an empty `MDCard` class into which you add your own content.

```python
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarListItem

KV = '''
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path


<NavigationItem>
    theme_text_color: 'Custom'
    divider: None

    IconLeftWidget:
        icon: root.icon


<ContentNavigationDrawer>

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            size_hint_y: None
            height: "200dp"

            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size

            BoxLayout:
                id: top_box
                size_hint_y: None
                height: "200dp"
                #padding: "10dp"
                x: root.parent.x
                pos_hint: {"top": 1}

                FitImage:
                    source: f"{images_path}kivymd_alpha.png"

            MDIconButton:
                icon: "close"
                x: root.parent.x + dp(10)
                pos_hint: {"top": 1}
                on_release: root.parent.toggle_nav_drawer()

            MDLabel:
                markup: True
                text: "[b]KivyMD[/b]\\nVersion: 0.102.1"
                #pos_hint: {'center_y': .5}
                x: root.parent.x + dp(10)
                y: root.height - top_box.height + dp(10)
                size_hint_y: None
                height: self.texture_size[1]

        ScrollView:
            pos_hint: {"top": 1}

            GridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        md_bg_color: app.theme_cls.primary_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    pass


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for items in {
            "home-circle-outline": "Home",
            "update": "Check for Update",
            "settings-outline": "Settings",
            "exit-to-app": "Exit",
        }.items():
            self.root.ids.content_drawer.ids.box_item.add_widget(
                NavigationItem(
                    text=items[1],
                    icon=items[0],
                )
            )


TestNavigationDrawer().run()
```