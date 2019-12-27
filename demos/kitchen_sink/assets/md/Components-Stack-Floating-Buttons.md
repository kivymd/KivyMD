![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/stackfloatingbuttons.gif)

## Example of using a class MDStackFloatingButtons:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.toast import toast
from kivymd.theming import ThemeManager
from kivymd.uix.stackfloatingbutton import MDStackFloatingButtons


Builder.load_string("""
<ExampleFloatingButtons@BoxLayout>:
    orientation: 'vertical'

    MDToolbar:
        title: 'Stack Floating Buttons'
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['menu', lambda x: None]]

""")


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Example Stack Floating Buttons"
    create_stack_floating_buttons = False
    floating_data = {
        'Python': 'language-python',
        'Php': 'language-php',
        'C++': 'language-cpp'}

    def set_my_language(self, instance_button):
        toast(instance_button.icon)

    def build(self):
        screen = Factory.ExampleFloatingButtons()
        # Use this condition otherwise the stack will be created each time.
        if not self.create_stack_floating_buttons:
            screen.add_widget(MDStackFloatingButtons(
                icon='lead-pencil',
                floating_data=self.floating_data,
                callback=self.set_my_language))
            self.create_stack_floating_buttons = True
        return screen


if __name__ == "__main__":
    Example().run()
```