![appbar.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/appbar.gif)

## Example of using MDBottomAppBar:

```python
from kivy.factory import Factory

from kivymd.app import MDApp
from kivy.lang import Builder


Builder.load_string(
    """
<StyleLabel@MDLabel>:
    size_hint_y: None
    height: self.texture_size[1]


<StyleItemCheck@BoxLayout>:
    group: ""
    text: ""
    active: False
    size_hint_y: None
    height: self.minimum_height

    MDCheckbox:
        group: root.group
        active: root.active
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {"center_y": .5}
        on_active: app.callback(root.text, self.active)

    StyleLabel:
        text: root.text
        pos_hint: {"center_y": .5}


<BottomAppBar@Screen>
    name: 'bottom app bar'

    BoxLayout:
        spacing: dp(10)
        orientation: 'vertical'

        MDToolbar:
            title: "Title"
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]

        ScrollView:

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "10dp"
                spacing: "10dp"

                MDSeparator:

                StyleLabel:
                    text: "Notch"

                StyleItemCheck:
                    group: 'notch'
                    text: "On"
                    active: True

                StyleItemCheck:
                    group: 'notch'
                    text: "Off"

                MDSeparator:

                StyleLabel:
                    text: "Position"

                StyleItemCheck:
                    group: 'pos'
                    text: "Attached - Center"
                    active: True

                StyleItemCheck:
                    group: 'pos'
                    text: "Attached - End"

                StyleItemCheck:
                    group: 'pos'
                    text: "Free - Center"

                StyleItemCheck:
                    group: 'pos'
                    text: "Free - End"

        MDBottomAppBar

            MDToolbar:
                id: toolbar
                title: "Title"
                icon: "git"
                type: "bottom"
                left_action_items: [["menu", lambda x: x]]
"""
)


class BottomAppBarTest(MDApp):
    def callback(self, text, value):
        if value and self.root:
            if text == "Off":
                self.root.ids.toolbar.remove_notch()
            elif text == "On":
                self.root.ids.toolbar.set_notch()
            elif text == "Attached - End":
                self.root.ids.toolbar.mode = "end"
            elif text == "Attached - Center":
                self.root.ids.toolbar.mode = "center"
            elif text == "Free - End":
                self.root.ids.toolbar.mode = "free-end"
            elif text == "Free - Center":
                self.root.ids.toolbar.mode = "free-center"

    def build(self):
        return Factory.BottomAppBar()


BottomAppBarTest().run()
```