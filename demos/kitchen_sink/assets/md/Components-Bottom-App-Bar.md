![appbar.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/appbar.gif)

## Example of using MDBottomAppBar:

```python
from kivy.app import App
from kivy.lang import Builder

from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.uix.toolbar import MDBottomAppBar

kv = """
BoxLayout:
    spacing: dp(10)
    orientation: 'vertical'

    AnchorLayout:
        anchor_y: 'center'
        anchor_x: 'center'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)

            MDRaisedButton:
                text: 'Anchor center'
                pos_hint: {'center_x': .5}
                on_release:
                    app.md_app_bar.set_pos_action_button('center')
                    app.move_item_menu('center')

            MDRaisedButton:
                text: 'Anchor right'
                pos_hint: {'center_x': .5}
                on_release:
                    app.md_app_bar.set_pos_action_button('right')
                    app.move_item_menu('right')
"""


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    md_app_bar = None

    def build(self):
        root = Builder.load_string(kv)
        self.md_app_bar = MDBottomAppBar(
            md_bg_color=self.theme_cls.primary_color,
            left_action_items=[
                ['menu', lambda x: x],
                ['clock', lambda x: x],
                ['dots-vertical', lambda x: x]],
            anchor='right',
            callback=self.press_button)
        root.add_widget(self.md_app_bar)
        return root

    def move_item_menu(self, anchor):
        md_app_bar = self.md_app_bar
        if md_app_bar.anchor != anchor:
            if len(md_app_bar.right_action_items):
                md_app_bar.left_action_items.append(
                    md_app_bar.right_action_items[0])
                md_app_bar.right_action_items = []
            else:
                left_action_items = md_app_bar.left_action_items
                action_items = left_action_items[0:2]
                md_app_bar.right_action_items = [left_action_items[-1]]
                md_app_bar.left_action_items = action_items

    def press_button(self, instance):
        toast('Press Button')


if __name__ == "__main__":
    MyApp().run()
```