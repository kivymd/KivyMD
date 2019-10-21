![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/filemanager.gif)

## Example of using a class MDFileManager:

```python
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.modalview import ModalView

from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string(
'''
<ExampleFileManager@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color


    FloatLayout:

        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.file_manager_open()
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "File Manager"

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.manager = None

    def build(self):
        return Factory.ExampleFileManager()

    def file_manager_open(self):
        if not self.manager:
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
        self.manager.open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;

        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


if __name__ == "__main__":
    Example().run()
```

## Example of using a class MDFileManager with previous mode:
(uses threads to create previews and does not slow down user interface)

![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/filemanager_previous.gif)

```python
file_manager = MDFileManager(previous=True)
```