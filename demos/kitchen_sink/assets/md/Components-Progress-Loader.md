![useranimationcard.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/progressloader.gif)

## Example of using a class MDProgressLoader:

```python
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.uix.progressloader import MDProgressLoader
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string(
'''
<Root@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        id: box

        MDRoundFlatIconButton:
            text: "Download file"
            icon: "download"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            on_release: app.show_example_download_file()
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Progress Loader"

    def build(self):
        self.main_widget = Factory.Root()
        return self.main_widget

    def set_chevron_back_screen(self):
        '''Sets the return chevron to the previous screen in ToolBar.'''

        self.main_widget.ids.toolbar.right_action_items = []

    def download_progress_hide(self, instance_progress, value):
        '''Hides progress progress.'''

        self.main_widget.ids.toolbar.right_action_items = \
            [['download',
                lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self):
        link = 'https://www.python.org/ftp/python/3.5.1/python-3.5.1-embed-win32.zip'
        progress = MDProgressLoader(
            url_on_image=link,
            path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
            download_complete=self.download_complete,
            download_hide=self.download_progress_hide
        )
        progress.start(self.main_widget.ids.box)

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')


if __name__ == "__main__":
    Example().run()
```