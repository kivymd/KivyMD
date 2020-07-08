"""
Components/File Manager
=======================

A simple manager for selecting directories and files.

Usage
-----

.. code-block:: python

    path = '/'  # path to the directory that will be opened in the file manager
    file_manager = MDFileManager(
        exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
        select_path=self.select_path,  # function called when selecting a file/directory
    )
    file_manager.show(path)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager.png
    :align: center

Or with ``preview`` mode:

.. code-block:: python

    file_manager = MDFileManager(
        exit_manager=self.exit_manager,
        select_path=self.select_path,
        preview=True,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-previous.png
    :align: center

.. warning:: The `preview` mode is intended only for viewing images and will
    not display other types of files.

Example
-------

.. code-block:: python

    from kivy.core.window import Window
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.filemanager import MDFileManager
    from kivymd.toast import toast


    KV = '''
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "MDFileManager"
            left_action_items: [['menu', lambda x: None]]
            elevation: 10

        FloatLayout:

            MDRoundFlatIconButton:
                text: "Open manager"
                icon: "folder"
                pos_hint: {'center_x': .5, 'center_y': .6}
                on_release: app.file_manager_open()
    '''


    class Example(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Window.bind(on_keyboard=self.events)
            self.manager_open = False
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,
                select_path=self.select_path,
                preview=True,
            )

        def build(self):
            return Builder.load_string(KV)

        def file_manager_open(self):
            self.file_manager.show('/')  # output manager to the screen
            self.manager_open = True

        def select_path(self, path):
            '''It will be called when you click on the file name
            or the catalog selection button.

            :type path: str;
            :param path: path to the selected directory or file;
            '''

            self.exit_manager()
            toast(path)

        def exit_manager(self, *args):
            '''Called when the user reaches the root of the directory tree.'''

            self.manager_open = False
            self.file_manager.close()

        def events(self, instance, keyboard, keycode, text, modifiers):
            '''Called when buttons are pressed on the mobile device.'''

            if keyboard in (1001, 27):
                if self.manager_open:
                    self.file_manager.back()
            return True


    Example().run()
"""

__all__ = ("MDFileManager",)

import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView

from kivymd import images_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import BaseListItem, ContainerSupport
from kivymd.utils.fitimage import FitImage

ACTIVITY_MANAGER = """
#:import os os


<BodyManager@BoxLayout>
    icon: "folder"
    path: ""
    background_normal: ""
    background_down: ""
    dir_or_file_name: ""
    events_callback: lambda x: None
    orientation: "vertical"

    ModifiedOneLineIconListItem:
        text: root.dir_or_file_name
        on_release: root.events_callback(root.path)

        IconLeftWidget:
            icon: root.icon
            theme_text_color: "Custom"
            text_color: self.theme_cls.primary_color

    MDSeparator:


<LabelContent@MDLabel>
    size_hint_y: None
    height: self.texture_size[1]
    shorten: True
    shorten_from: "center"
    halign: "center"
    text_size: self.width, None


<BodyManagerWithPreview>
    name: ""
    path: ""
    realpath: ""
    type: "folder"
    events_callback: lambda x: None
    orientation: "vertical"
    size_hint_y: None
    hright: root.height
    padding: dp(20)

    IconButton:
        mipmap: True
        source: root.path
        on_release:
            root.events_callback(\
            os.path.join(root.path if root.type != "folder" else root.realpath, \
            root.name))

    LabelContent:
        text: root.name


<FloatButton>
    anchor_x: "right"
    anchor_y: "bottom"
    size_hint_y: None
    height: dp(56)
    padding: dp(10)

    MDFloatingActionButton:
        size_hint: None, None
        size:dp(56), dp(56)
        icon: root.icon
        opposite_colors: True
        elevation: 8
        on_release: root.callback()
        md_bg_color: root.md_bg_color


<MDFileManager>
    md_bg_color: root.theme_cls.bg_normal

    BoxLayout:
        orientation: "vertical"
        spacing: dp(5)

        MDToolbar:
            id: toolbar
            title: root.current_path
            right_action_items: [["close-box", lambda x: root.exit_manager(1)]]
            left_action_items: [["chevron-left", lambda x: root.back()]]
            elevation: 10

        RecycleView:
            id: rv
            key_viewclass: "viewclass"
            key_size: "height"
            bar_width: dp(4)
            bar_color: root.theme_cls.primary_color
            #on_scroll_stop: root._update_list_images()

            RecycleGridLayout:
                padding: dp(10)
                cols: 3 if root.preview else 1
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"


<ModifiedOneLineIconListItem>

    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height / 2 - self.height / 2
        size: dp(48), dp(48)
"""


class BodyManagerWithPreview(MDBoxLayout):
    """Base class for folder icons and thumbnails images in ``preview`` mode.
    """


class IconButton(CircularRippleBehavior, ButtonBehavior, FitImage):
    """Folder icons/thumbnails images in ``preview`` mode."""


class FloatButton(AnchorLayout):
    callback = ObjectProperty()
    md_bg_color = ListProperty([1, 1, 1, 1])
    icon = StringProperty()


class ModifiedOneLineIconListItem(ContainerSupport, BaseListItem):
    _txt_left_pad = NumericProperty("72dp")
    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")
    _num_lines = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(48)


class MDFileManager(ThemableBehavior, MDFloatLayout):
    icon = StringProperty("check")
    """
    The icon that will be used on the directory selection button.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `check`.
    """

    icon_folder = StringProperty(f"{images_path}folder.png")
    """
    The icon that will be used for folder icons when using ``preview = True``.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `check`.
    """

    exit_manager = ObjectProperty(lambda x: None)
    """
    Function called when the user reaches directory tree root.

    :attr:`exit_manager` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `lambda x: None`.
    """

    select_path = ObjectProperty(lambda x: None)
    """
    Function, called when selecting a file/directory.

    :attr:`select_path` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `lambda x: None`.
    """

    ext = ListProperty()
    """
    List of file extensions to be displayed
    in the manager. For example, `['py', 'kv']` - will filter out all files,
    except python scripts and Kv Language.

    :attr:`ext` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    search = OptionProperty("all", options=["all", "files"])
    """
    It can take the values 'dirs' 'files' - display only directories
    or only files. By default, it displays and folders, and files.
    Available options are: `'all'`, `'files'`.

    :attr:`search` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `all`.
    """

    current_path = StringProperty(os.getcwd())
    """
    Current directory.

    :attr:`current_path` is an :class:`~kivy.properties.StringProperty`
    and defaults to `/`.
    """

    use_access = BooleanProperty(True)
    """
    Show access to files and directories.

    :attr:`use_access` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    preview = BooleanProperty(False)
    """
    Shows only image previews.

    :attr:`preview` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _window_manager = None
    _window_manager_open = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = []  # directory navigation history
        # If False - do not add a directory to the history -
        # The user moves down the tree.
        self.history_flag = True
        toolbar_label = self.ids.toolbar.children[1].children[0]
        toolbar_label.font_style = "Subtitle1"
        self.add_widget(
            FloatButton(
                callback=self.select_directory_on_press_button,
                md_bg_color=self.theme_cls.primary_color,
                icon=self.icon,
            )
        )
        if self.preview:
            self.ext = [".png", ".jpg", ".jpeg"]

    def show(self, path):
        """Forms the body of a directory tree.

        :param path:
            The path to the directory that will be opened in the file manager.
        """

        dirs, files = self.get_content(path)
        self.current_path = path
        manager_list = []

        if dirs == [] and files == []:  # selected directory
            pass
        elif not dirs and not files:  # directory is unavailable
            return

        if self.preview:
            for name_dir in dirs:
                manager_list.append(
                    {
                        "viewclass": "BodyManagerWithPreview",
                        "path": self.icon_folder,
                        "realpath": os.path.join(path),
                        "type": "folder",
                        "name": name_dir,
                        "events_callback": self.select_dir_or_file,
                        "height": dp(150),
                    }
                )
            for name_file in files:
                if (
                    os.path.splitext(os.path.join(path, name_file))[1]
                    in self.ext
                ):
                    manager_list.append(
                        {
                            "viewclass": "BodyManagerWithPreview",
                            "path": os.path.join(path, name_file),
                            "name": name_file,
                            "type": "files",
                            "events_callback": self.select_dir_or_file,
                            "height": dp(150),
                        }
                    )
        else:
            for name in dirs:
                _path = path + name if path == "/" else path + "/" + name
                access_string = self.get_access_string(_path)
                if "r" not in access_string:
                    icon = "folder-lock"
                else:
                    icon = "folder"

                manager_list.append(
                    {
                        "viewclass": "BodyManager",
                        "path": _path,
                        "icon": icon,
                        "dir_or_file_name": name,
                        "events_callback": self.select_dir_or_file,
                    }
                )
            for name in files:
                _path = path + name if path == "/" else path + "/" + name
                if self.ext and os.path.splitext(name)[1] in self.ext:
                    manager_list.append(
                        {
                            "viewclass": "BodyManager",
                            "path": _path,
                            "icon": "file-outline",
                            "dir_or_file_name": name,
                            "events_callback": self.select_dir_or_file,
                        }
                    )
        self.ids.rv.data = manager_list

        if not self._window_manager:
            self._window_manager = ModalView(
                size_hint=(1, 1), auto_dismiss=False
            )
            self._window_manager.add_widget(self)
        if not self._window_manager_open:
            self._window_manager.open()
            self._window_manager_open = True

    def get_access_string(self, path):
        access_string = ""
        if self.use_access:
            access_data = {"r": os.R_OK, "w": os.W_OK, "x": os.X_OK}
            for access in access_data.keys():
                access_string += (
                    access if os.access(path, access_data[access]) else "-"
                )
        return access_string

    def get_content(self, path):
        """Returns a list of the type [[Folder List], [file list]]."""

        try:
            files = []
            dirs = []

            if self.history_flag:
                self.history.append(path)
            if not self.history_flag:
                self.history_flag = True

            for content in os.listdir(path):
                if os.path.isdir(os.path.join(path, content)):
                    if self.search == "all" or self.search == "dirs":
                        dirs.append(content)
                else:
                    if self.search == "all" or self.search == "files":
                        if len(self.ext) != 0:
                            try:
                                files.append(os.path.join(path, content))
                            except IndexError:
                                pass
                        else:
                            files.append(content)
            return dirs, files
        except OSError:
            self.history.pop()
            return None, None

    def close(self):
        """Closes the file manager window."""

        self._window_manager.dismiss()
        self._window_manager_open = False

    def select_dir_or_file(self, path):
        """Called by tap on the name of the directory or file."""

        if os.path.isfile(path):
            self.select_path(path)
            return

        self.current_path = path
        self.show(path)

    def back(self):
        """Returning to the branch down in the directory tree."""

        if len(self.history) == 1:
            path, end = os.path.split(self.history[0])
            if end == "":
                self.close()
                self.exit_manager(1)
                return
            self.history[0] = path
        else:
            self.history.pop()
            path = self.history[-1]
        self.history_flag = False
        self.select_dir_or_file(path)

    def select_directory_on_press_button(self, *args):
        """Called when a click on a floating button."""

        self.select_path(self.current_path)


Builder.load_string(ACTIVITY_MANAGER)
