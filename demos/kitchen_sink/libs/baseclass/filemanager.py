from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager


class KitchenSinkFileFileManagerTypeDialog(MDBoxLayout):
    """ Choose file manager type and selection type """

    allow_multiple_selection = False

    def set_selection_type(self, checkbox, value):
        self.allow_multiple_selection = value


class KitchenSinkFileManager(Screen):
    manager_open = False
    file_manager = None

    def file_manager_open(self):
        def open_file_manager(text_item):
            preview = False if text_item == "List" else True
            if not self.file_manager:
                self.file_manager = MDFileManager(
                    exit_manager=self.exit_manager,
                    select_path=self.select_path,
                    preview=preview,
                )
            self.file_manager.preview = preview

            if manager_type_dialog.allow_multiple_selection:
                self.file_manager.selector = "multi"
            else:
                self.file_manager.selector = "any"

            self.file_manager.show(MDApp.get_running_app().user_data_dir)
            self.manager_open = True

        manager_type_dialog = KitchenSinkFileFileManagerTypeDialog()

        MDDialog(
            title="Kitchen Sink",
            type="custom",
            size_hint=(0.8, 0.4),
            content_cls=manager_type_dialog,
            buttons=[
                MDFlatButton(
                    text="List", on_release=lambda x: open_file_manager("List")
                ),
                MDFlatButton(
                    text="Preview",
                    on_release=lambda x: open_file_manager("Preview"),
                ),
            ],
        ).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;

        """

        self.exit_manager()
        if type(path) == str:
            toast(path)
        else:
            toast(", ".join(path))

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()
