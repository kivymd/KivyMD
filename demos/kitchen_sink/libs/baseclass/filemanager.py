import os

from kivy.uix.screenmanager import Screen


class KitchenSinkFileManager(Screen):
    manager_open = False
    file_manager = None

    def file_manager_open(self):
        from kivy.app import App

        from kivymd.uix.filemanager import MDFileManager
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton

        def open_file_manager(text_item):
            previous = False if text_item == "List" else True
            if not self.file_manager:
                self.file_manager = MDFileManager(
                    exit_manager=self.exit_manager,
                    select_path=self.select_path,
                )
            self.file_manager.previous = previous
            self.file_manager.show(App.get_running_app().user_data_dir)
            self.manager_open = True

        MDDialog(
            title="Kitchen Sink",
            size_hint=(0.8, 0.4),
            text="Open manager with 'list' or 'previous' mode?",
            buttons=[
                MDFlatButton(
                    text="List", on_release=lambda x: open_file_manager("List")
                ),
                MDFlatButton(
                    text="Previous",
                    on_release=lambda x: open_file_manager("Previous"),
                ),
            ],
        ).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;

        """

        from kivymd.toast import toast

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()
