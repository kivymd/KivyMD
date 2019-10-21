![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/list-item-with-checkbox.gif)

## Example of using OneLineAvatarIconListItem with Checkbox:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.image import Image

from kivymd.theming import ThemeManager
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox

Builder.load_string(
'''
<ListItemWithCheckbox@OneLineAvatarIconListItem>:
    MyAvatar:
        source: 'data/logo/kivy-icon-128.png'
    MyCheckbox:


<Lists@BoxLayout>
    name: 'lists'
    orientation: 'vertical'

    MDToolbar:
        title:'List item with Checkbox'
        md_bg_color: app.theme_cls.primary_color
        elevation: 10

    ScrollView:

        MDList:
            id: scroll
''')


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class MyAvatar(ILeftBody, Image):
    pass


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        list = Factory.Lists()
        for i in range(30):
            list.ids.scroll.add_widget(
                Factory.ListItemWithCheckbox(text='Item %d' % i))
        return list


if __name__ == "__main__":
    Example().run()
```