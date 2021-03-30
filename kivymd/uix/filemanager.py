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

.. warning:: Be careful! To use the `/` path on Android devices, you need
    special permissions. Therefore, you are likely to get an error.

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

import locale
import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
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
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.utils.fitimage import FitImage

ACTIVITY_MANAGER = """
#:import os os


<BodyManager@BoxLayout>
    icon: "folder"
    path: ""
    background_normal: ""
    background_down: ""
    dir_or_file_name: ""
    _selected: False
    events_callback: lambda x: None
    orientation: "vertical"

    ModifiedOneLineIconListItem:
        text: root.dir_or_file_name
        bg_color: self.theme_cls.bg_darkest if root._selected else self.theme_cls.bg_normal
        on_release: root.events_callback(root.path, root)

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
    _selected: False
    orientation: "vertical"
    size_hint_y: None
    hright: root.height
    padding: dp(20)

    IconButton:
        mipmap: True
        source: root.path
        bg_color: app.theme_cls.bg_darkest if root._selected else app.theme_cls.bg_normal
        on_release:
            root.events_callback(\
            os.path.join(root.path if root.type != "folder" else root.realpath, \
            root.name), root)

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

    MDBoxLayout:
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

            RecycleGridLayout:
                padding: "10dp"
                spacing: "2dp"
                cols: 3 if root.preview else 1
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height


<ModifiedOneLineIconListItem>

    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height / 2 - self.height / 2
        size: dp(48), dp(48)
"""


class BodyManagerWithPreview(MDBoxLayout):
    """Base class for folder icons and thumbnails images in ``preview`` mode."""


class IconButton(CircularRippleBehavior, ButtonBehavior, FitImage):
    """Folder icons/thumbnails images in ``preview`` mode."""


class FloatButton(AnchorLayout):
    callback = ObjectProperty()
    md_bg_color = ColorProperty([1, 1, 1, 1])
    icon = StringProperty()


class ModifiedOneLineIconListItem(ContainerSupport, BaseListItem):
    _txt_left_pad = NumericProperty("72dp")
    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")
    _num_lines = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(48)


class MDFileManager(ThemableBehavior, MDRelativeLayout):
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
    List of file extensions to be displayed in the manager.
    For example, `['.py', '.kv']` - will filter out all files,
    except python scripts and Kv Language.

    :attr:`ext` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    search = OptionProperty("all", options=["all", "dirs", "files"])
    """
    It can take the values 'all' 'dirs' 'files' - display only directories
    or only files or both them. By default, it displays folders, and files.
    Available options are: `'all'`, `'dirs'`, `'files'`.

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

    show_hidden_files = BooleanProperty(False)
    """
    Shows hidden files.

    :attr:`show_hidden_files` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    sort_by = OptionProperty(
        "name", options=["nothing", "name", "date", "size", "type"]
    )
    """
    It can take the values 'nothing' 'name' 'date' 'size' 'type' - sorts files by option
    By default, sort by name.
    Available options are: `'nothing'`, `'name'`, `'date'`, `'size'`, `'type'`.

    :attr:`sort_by` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `name`.
    """

    sort_by_desc = BooleanProperty(False)
    """
    Sort by descending.

    :attr:`sort_by_desc` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    selector = OptionProperty("any", options=["any", "file", "folder", "multi"])
    """
    It can take the values 'any' 'file' 'folder' 'multi'
    By default, any.
    Available options are: `'any'`, `'file'`, `'folder'`, `'multi'`.

    :attr:`selector` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `any`.
    """

    selection = ListProperty()
    """
    Contains the list of files that are currently selected.

    :attr:`selection` is a read-only :class:`~kivy.properties.ListProperty` and
    defaults to `[]`.
    """

    _window_manager = None
    _window_manager_open = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        toolbar_label = self.ids.toolbar.children[1].children[0]
        toolbar_label.font_style = "Subtitle1"
        if (
            self.selector == "any"
            or self.selector == "multi"
            or self.selector == "folder"
        ):
            self.add_widget(
                FloatButton(
                    callback=self.select_directory_on_press_button,
                    md_bg_color=self.theme_cls.primary_color,
                    icon=self.icon,
                )
            )

        if self.preview:
            self.ext = [".png", ".jpg", ".jpeg"]

    def __sort_files(self, files):
        def sort_by_name(files):
            files.sort(key=locale.strxfrm)
            files.sort(key=str.casefold)
            return files

        if self.sort_by == "name":
            sorted_files = sort_by_name(files)
        elif self.sort_by == "date":
            _files = sort_by_name(files)
            _sorted_files = [os.path.join(self.current_path, f) for f in _files]
            _sorted_files.sort(key=os.path.getmtime, reverse=True)
            sorted_files = [os.path.basename(f) for f in _sorted_files]
        elif self.sort_by == "size":
            _files = sort_by_name(files)
            _sorted_files = [os.path.join(self.current_path, f) for f in _files]
            _sorted_files.sort(key=os.path.getsize, reverse=True)
            sorted_files = [os.path.basename(f) for f in _sorted_files]
        elif self.sort_by == "type":
            _files = sort_by_name(files)
            sorted_files = sorted(
                _files,
                key=lambda f: (os.path.splitext(f)[1], os.path.splitext(f)[0]),
            )
        else:
            sorted_files = files

        if self.sort_by_desc:
            sorted_files.reverse()

        return sorted_files

    def show(self, path):
        """Forms the body of a directory tree.

        :param path:
            The path to the directory that will be opened in the file manager.
        """

        self.current_path = path
        self.selection = []
        dirs, files = self.get_content()
        manager_list = []

        if dirs == [] and files == []:  # selected directory
            pass
        elif not dirs and not files:  # directory is unavailable
            return

        if self.preview:
            for name_dir in self.__sort_files(dirs):
                manager_list.append(
                    {
                        "viewclass": "BodyManagerWithPreview",
                        "path": self.icon_folder,
                        "realpath": os.path.join(path),
                        "type": "folder",
                        "name": name_dir,
                        "events_callback": self.select_dir_or_file,
                        "height": dp(150),
                        "_selected": False,
                    }
                )
            for name_file in self.__sort_files(files):
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
                            "_selected": False,
                        }
                    )
        else:
            for name in self.__sort_files(dirs):
                _path = os.path.join(path, name)
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
                        "_selected": False,
                    }
                )
            for name in self.__sort_files(files):
                if self.ext and os.path.splitext(name)[1] not in self.ext:
                    continue

                manager_list.append(
                    {
                        "viewclass": "BodyManager",
                        "path": name,
                        "icon": "file-outline",
                        "dir_or_file_name": os.path.split(name)[1],
                        "events_callback": self.select_dir_or_file,
                        "_selected": False,
                    }
                )
        self.ids.rv.data = manager_list

        if not self._window_manager:
            self._window_manager = ModalView(
                size_hint=self.size_hint, auto_dismiss=False
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

    def get_content(self):
        """Returns a list of the type [[Folder List], [file list]]."""

        try:
            files = []
            dirs = []

            for content in os.listdir(self.current_path):
                if os.path.isdir(os.path.join(self.current_path, content)):
                    if self.search == "all" or self.search == "dirs":
                        if (not self.show_hidden_files) and (
                            content.startswith(".")
                        ):
                            continue
                        else:
                            dirs.append(content)

                else:
                    if self.search == "all" or self.search == "files":
                        if len(self.ext) != 0:
                            try:
                                files.append(
                                    os.path.join(self.current_path, content)
                                )
                            except IndexError:
                                pass
                        else:
                            if (
                                not self.show_hidden_files
                                and content.startswith(".")
                            ):
                                continue
                            else:
                                files.append(content)

            return dirs, files

        except OSError:
            return None, None

    def close(self):
        """Closes the file manager window."""

        self._window_manager.dismiss()
        self._window_manager_open = False

    def select_dir_or_file(self, path, widget):
        """Called by tap on the name of the directory or file."""

        if os.path.isfile(os.path.join(self.current_path, path)):
            if self.selector == "multi":
                file_path = os.path.join(self.current_path, path)
                if file_path in self.selection:
                    widget._selected = False
                    self.selection.remove(file_path)
                else:
                    widget._selected = True
                    self.selection.append(file_path)
            elif self.selector == "folder":
                return
            else:
                self.select_path(os.path.join(self.current_path, path))

        else:
            self.current_path = path
            self.show(path)

    def back(self):
        """Returning to the branch down in the directory tree."""

        path, end = os.path.split(self.current_path)

        if not end:
            self.close()
            self.exit_manager(1)

        else:
            self.show(path)

    def select_directory_on_press_button(self, *args):
        """Called when a click on a floating button."""

        if self.selector == "multi":
            if len(self.selection) > 0:
                self.select_path(self.selection)
        else:
            if self.selector == "folder" or self.selector == "any":
                self.select_path(self.current_path)


Builder.load_string(ACTIVITY_MANAGER)
