![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/custom-navigation-drawer.gif)

[CustomNavigationDrawer](https://github.com/HeaTTheatR/CustomNavigationDrawer)

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

from kivymd.uix.list import ILeftBody, OneLineAvatarListItem
from kivymd.theming import ThemableBehavior, ThemeManager

Builder.load_string("""
#:import Window kivy.core.window.Window
#:import get_hex_from_color kivy.utils.get_hex_from_color

#:set color_lilac_very_light [0.5215686274509804, 0.37254901960784315, 0.9450980392156862, 1]
#:set color_grey_dark [0.18823529411764706, 0.19215686274509805, 0.30980392156862746, 1]
#:set color_grey [.29411764705882354, .3215686274509804, .4196078431372549, 1]
#:set hex_color_grey get_hex_from_color([.29411764705882354, .3215686274509804, .4196078431372549, 1])


<MyLabel@Label>
    size_hint: None, None
    size: self.texture_size
    pos_hint: {'center_x': .5}


<MyBoxLayout@BoxLayout>
    size_hint_y: None
    height: self.minimum_height


<CustomNavigationDrawerIconButton>
    theme_text_color: 'Custom'
    text_color: color_grey
    divider: None

    AvatarSampleWidget:
        source: root.source


<CustomNavigationDrawer@BoxLayout>
    size_hint: None, None
    width: '360dp'
    height: Window.height
    x: Window.width

    canvas:
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'data/shadow-profile-items.png'

    BoxLayout:
        id: box_content
        orientation: 'vertical'
        width: '320dp'
        pos_hint: {'right': 1}
        padding: '60dp', '10dp', '30dp', 0
        spacing: '30dp'

        MDIconButton:
            icon: 'close'
            theme_text_color: 'Custom'
            text_color: color_grey
            on_release: root.parent.hide_navigation_drawer()

        MyBoxLayout:

            Image:
                source: 'data/users/user.png'

            MyLabel:
                id: label_user_name_mail
                markup: True
                text:
                    f"[color={hex_color_grey}][size=20]HeaTTeatR" \
                    f"[/size][/color]\\nkivydevelopment@gmail.com"
                color: color_grey_dark
                pos_hint: {'center_y': .5}

        MyBoxLayout:
            spacing: '5dp'
            padding: '10dp'

            MyBoxLayout:
                orientation: 'vertical'
                spacing: '5dp'

                MyLabel:
                    id: label_plain
                    markup: True
                    text: 'My Plain'
                    color: color_grey
                    pos_hint: {'center_y': .5}

                MyBoxLayout:
                    spacing: '5dp'

                    Widget:
                        size_hint: None, None
                        size: '10dp', '10dp'
                        pos_hint: {'center_y': .5}

                        canvas.before:
                            Color:
                                rgba: color_lilac_very_light
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos

                    MyLabel:
                        id: label_basic
                        markup: True
                        text: 'Basic $5/mo'
                        color: color_grey_dark

            MDRoundFlatButton:
                text: 'Upgrade'
                pos_hint: {'right': 1}

        ScrollView:

            GridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height


<RootScreen>
    name: 'custom navigation drawer'
    on_kv_post: root.set_navigation_drawer_icons()

    FloatLayout:

        BoxLayout:
            orientation: 'vertical'

            MDToolbar:
                title: app.title
                md_bg_color: app.theme_cls.primary_color
                elevation: 10
                left_action_items:
                    [['menu', lambda x: root.show_navigation_drawer()]]

            Widget:

    CustomNavigationDrawer:
        id: navigation_drawer
""")


class AvatarSampleWidget(ILeftBody, Image):
    pass


class CustomNavigationDrawerIconButton(OneLineAvatarListItem):
    source = StringProperty()


class RootScreen(ThemableBehavior, Screen):
    def hide_navigation_drawer(self):
        Animation(x=Window.width, d=0.2).start(self.ids.navigation_drawer)

    def show_navigation_drawer(self):
        Animation(x=Window.width - self.ids.navigation_drawer.width, d=0.2).start(
            self.ids.navigation_drawer
        )

    def set_navigation_drawer_icons(self):
        for items in {
            "home": "Home",
            "about": "About",
            "update": "Check for Update",
            "preferences": "Preferences",
            "promo": "Promo",
            "report": "Send Report",
            "out": "Sign Out",
            "quit": "Quit",
        }.items():
            self.ids.navigation_drawer.ids.box_item.add_widget(
                CustomNavigationDrawerIconButton(
                    text=items[1],
                    source=f"data/profile/{items[0]}.png",
                )
            )


class TestCustomNavigationDrawer(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Indigo"
    root_screen = None
    title = "Test CustomNavigationDrawer"

    def build(self):
        self.root_screen = RootScreen()
        return self.root_screen


if __name__ == "__main__":
    TestCustomNavigationDrawer().run()
```