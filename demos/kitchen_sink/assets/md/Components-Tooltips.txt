![chips.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tooltips.gif)

## Example of using MDTooltips:

```python
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.app import MDApp

Builder.load_string("""
#:import random random
#:import hex_colormap kivy.utils.hex_colormap
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import md_icons kivymd.icon_definitions.md_icons

#:set ICONS list(md_icons.keys())


<IconButtonTooltips@MDIconButton+MDTooltip>


<ExampleTooltips@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        title: "Example Tooltips"
        md_bg_color: get_color_from_hex(hex_colormap["crimson"])
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]
        tooltip_text: "MDToolbar"

    Screen:

        BoxLayout:
            size_hint: None, None
            size: self.minimum_size
            padding: "10dp"
            spacing: "10dp"
            pos_hint: {'center_x': .5, "center_y": .9}

            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
            IconButtonTooltips:
                icon: random.choice(ICONS)
                tooltip_text: "MDIconButton"
""")


class Test(MDApp):
    def build(self):
        return Factory.ExampleTooltips()


Test().run()
```

## MDTooltip Behavior on Mobile:

![chips.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tooltips-on-mobile.gif)

