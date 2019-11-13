![banner.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/banner.gif)

## Example of using MDBottomAppBar:

```python
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.app import MDApp

Builder.load_string("""
<ExampleBanner@Screen>

    MDBanner:
        id: banner
        over_widget: scroll

    MDToolbar:
        id: toolbar
        title: "Example Banners"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]
        pos_hint: {'top': 1}

    ScrollView:
        id: scroll
        size_hint_y: None
        height: Window.height - toolbar.height

        GridLayout:
            id: box
            size_hint_y: None
            height: self.minimum_height
            cols: 1
            padding: "10dp"
            spacing: "10dp"

            OneLineListItem:
                text: "ThreeLineBanner"
                on_release:
                    banner.type = "three-line"
                    banner.text = \
                    [\
                    "Three line string text example with two actions.", \
                    "This is the second line of the banner message,", \
                    "and this is the third line of the banner message.",
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "TwoLineBanner"
                on_release:
                    banner.type = "two-line"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "OneLineBanner"
                on_release:
                    banner.type = "one-line"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "ThreeLineIconBanner"
                on_release:
                    banner.type = "three-line-icon"
                    banner.text = \
                    [\
                    "Three line string text example with two actions.", \
                    "This is the second line of the banner message,", \
                    "and this is the third line of the banner message.",
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "TwoLineIconBanner"
                on_release:
                    banner.type = "two-line-icon"
                    banner.text = \
                    [\
                    "One line string text example with two actions.", \
                    "This is the second line of the banner message.", \
                    ]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "OneLineIconBanner"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example with two actions."]
                    banner.left_action = ["CANCEL", lambda x: None]
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()

            OneLineListItem:
                text: "Banner without actions"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = []
                    banner.show()

            OneLineListItem:
                text: "Banner with one actions"
                on_release:
                    banner.type = "one-line-icon"
                    banner.text = ["One line string text example without actions."]
                    banner.left_action = []
                    banner.right_action = ["CLOSE", lambda x: banner.hide()]
                    banner.show()
""")


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "DeepPurple"

    def build(self):
        return Factory.ExampleBanner()


Test().run()
```