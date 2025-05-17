"""
Components/FileManager
======================

A simple manager for selecting directories and files.

Usage
-----

.. code-block:: python

    path = os.path.expanduser("~")  # path to the directory that will be opened in the file manager
    file_manager = MDFileManager(
        exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
        select_path=self.select_path,  # function called when selecting a file/directory
    )
    file_manager.show(path)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager.png
    :align: center

.. warning:: Be careful! To use the `'/'` path on Android devices, you need
    special permissions. Therefore, you are likely to get an error.

Or with ``preview`` mode:

.. code-block:: python

    file_manager = MDFileManager(
        exit_manager=self.exit_manager,
        select_path=self.select_path,
        preview=True,
    )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-preview.png
    :align: center

.. warning:: The `preview` mode is intended only for viewing images and will
    not display other types of files.

Example
-------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            import os

            from kivy.core.window import Window
            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.filemanager import MDFileManager
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.file_manager_open()

                    MDButtonText:
                        text: "Open manager"
            '''


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    Window.bind(on_keyboard=self.events)
                    self.manager_open = False
                    self.file_manager = MDFileManager(
                        exit_manager=self.exit_manager, select_path=self.select_path
                    )

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)

                def file_manager_open(self):
                    self.file_manager.show(
                        os.path.expanduser("~"))  # output manager to the screen
                    self.manager_open = True

                def select_path(self, path: str):
                    '''
                    It will be called when you click on the file name
                    or the catalog selection button.

                    :param path: path to the selected directory or file;
                    '''

                    self.exit_manager()
                    MDSnackbar(
                        MDSnackbarText(
                            text=path,
                        ),
                        y=dp(24),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.8,
                    ).open()

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

    .. tab:: Declarative python style

        .. code-block:: python

            import os

            from kivy.core.window import Window
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.filemanager import MDFileManager
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    Window.bind(on_keyboard=self.events)
                    self.manager_open = False
                    self.file_manager = MDFileManager(
                        exit_manager=self.exit_manager, select_path=self.select_path
                    )

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open manager"
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=self.file_manager_open,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def file_manager_open(self, *args):
                    self.file_manager.show(
                        os.path.expanduser("~"))  # output manager to the screen
                    self.manager_open = True

                def select_path(self, path: str):
                    '''
                    It will be called when you click on the file name
                    or the catalog selection button.

                    :param path: path to the selected directory or file;
                    '''

                    self.exit_manager()
                    MDSnackbar(
                        MDSnackbarText(
                            text=path,
                        ),
                        y=dp(24),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.8,
                    ).open()

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

.. versionadded:: 1.0.0

Added a feature that allows you to show the available disks first, then the
files contained in them. Works correctly on: `Windows`, `Linux`, `OSX`, `Android`.
Not tested on `iOS`.

.. code-block:: python

    def file_manager_open(self):
        self.file_manager.show_disks()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-show-disks.png
    :align: center
"""

from __future__ import annotations

__all__ = ("MDFileManager",)

import locale
import os
import re
from typing import List, Tuple, Union

from kivy import platform
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.relativelayout import RelativeLayout

from kivymd import images_path, uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.uix.button import MDFabButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import MDListItem

with open(
    os.path.join(uix_path, "filemanager", "filemanager.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDFileManagerItem(MDListItem):
    """
    Base class for folders and files icons.

    .. versionchanged:: 2.0.0

        The `BodyManager` class has been renamed to `MDFileManagerItem`.

    For more information, see in the
    :class:`~kivymd.uix.list.list.MDListItem` class documentation.
    """


class MDFileManagerItemPreview(BoxLayout):
    """
    Base class for folder icons and thumbnails images in `preview` mode.

    .. versionchanged:: 2.0.0

        The `BodyManagerWithPreview` class has been renamed
        to `MDFileManagerItemPreview`.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDFileManagerThumbnail(CircularRippleBehavior, ButtonBehavior, FitImage):
    """
    Folder icons/thumbnails images in `preview` mode.

    .. versionchanged:: 2.0.0

        The `IconButton` class has been renamed to `MDFileManagerThumbnail`.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.fitimage.fitimage.FitImage`
    classes documentation.
    """


class MDFileManager(ThemableBehavior, RelativeLayout):
    """
    Implements a modal dialog with a file manager.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    classes documentation.

    :Events:
        `on_pre_open`:
            Called before the MDFileManager is opened.
        `on_open`:
            Called when the MDFileManager is opened.
        `on_pre_dismiss`:
            Called before the MDFileManager is closed.
        `on_dismiss`:
            Called when the MDFileManager is closed.
    """

    icon = StringProperty("check", deprecated=True)
    """
    Icon that will be used on the directory selection button.

    .. deprecated:: 1.1.0
        Use :attr:`icon_selection_button` instead.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `check`.
    """

    icon_selection_button = StringProperty("check")
    """
    Icon that will be used on the directory selection button.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDFileManager(
            ...
            icon_selection_button="pencil",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-icon-selection-button.png
        :align: center

    :attr:`icon_selection_button` is an :class:`~kivy.properties.StringProperty`
    and defaults to `check`.
    """

    background_color_selection_button = ColorProperty(None)
    """
    Background color in (r, g, b, a) or string format of the current
    directory/path selection button.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDFileManager(
            ...
            background_color_selection_button="brown",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-background-color-selection-button.png
        :align: center

    :attr:`background_color_selection_button` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    background_color_toolbar = ColorProperty(None)
    """
    Background color in (r, g, b, a) or string format of the file manager toolbar.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDFileManager(
            ...
            background_color_toolbar="brown",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-background-color-toolbar.png
        :align: center

    :attr:`background_color_toolbar` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_folder = StringProperty(f"{images_path}folder.png")
    """
    Icon that will be used for folder icons when using ``preview = True``.

    .. code-block:: python

        MDFileManager(
            ...
            preview=True,
            icon_folder="path/to/icon.png",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-icon-folder.png
        :align: center

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `check`.
    """

    icon_color = ColorProperty(None)
    """
    Color in (r, g, b, a) or string format of the folder icon when the
    :attr:`preview` property is set to False.

    .. versionadded:: 1.1.0

    .. code-block:: python

        MDFileManager(
            ...
            preview=False,
            icon_color="brown",
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/file-manager-icon-color.png
        :align: center

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
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

    current_path = StringProperty(os.path.expanduser("~"))
    """
    Current directory.

    :attr:`current_path` is an :class:`~kivy.properties.StringProperty`
    and defaults to `os.path.expanduser("~")`.
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
    It can take the values 'nothing' 'name' 'date' 'size' 'type' - sorts files
    by option. By default, sort by name.
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

    :attr:`selection` is a read-only :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    selection_button = ObjectProperty()
    """
    The instance of the directory/path selection button.

    .. versionadded:: 1.1.0

    :attr:`selection_button` is a read-only :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _window_manager = None
    _window_manager_open = False

    __events__ = ("on_pre_open", "on_open", "on_pre_dismiss", "on_dismiss")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._create_selection_button)

        if self.preview:
            self.ext = [".png", ".jpg", ".jpeg"]
        self.disks = []

    def show_disks(self) -> None:
        if platform == "win":
            self.disks = sorted(
                re.findall(
                    r"[A-Z]+:.*$",
                    os.popen("mountvol /").read(),
                    re.MULTILINE,
                )
            )
        elif platform in ["linux", "android"]:
            self.disks = sorted(
                re.findall(
                    r"on\s(/.*)\stype",
                    os.popen("mount").read(),
                )
            )
        elif platform == "macosx":
            self.disks = sorted(
                re.findall(
                    r"on\s(/.*)\s\(",
                    os.popen("mount").read(),
                )
            )
        else:
            return

        self.current_path = ""
        manager_list = []

        for disk in self.disks:
            access_string = self.get_access_string(disk)
            if "r" not in access_string:
                icon = "harddisk-remove"
            else:
                icon = "harddisk"

            manager_list.append(
                {
                    "viewclass": "MDFileManagerItem",
                    "path": disk,
                    "icon": icon,
                    "dir_or_file_name": disk,
                    "events_callback": self.select_dir_or_file,
                    "_selected": False,
                }
            )
        self.ids.rv.data = manager_list
        self._show()

    def show(self, path: str) -> None:
        """
        Forms the body of a directory tree.

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
                        "viewclass": "MDFileManagerItemPreview",
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
                            "viewclass": "MDFileManagerItemPreview",
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
                        "viewclass": "MDFileManagerItem",
                        "path": _path,
                        "icon": icon,
                        "dir_or_file_name": name,
                        "events_callback": self.select_dir_or_file,
                        "icon_color": (
                            self.theme_cls.primaryColor
                            if not self.icon_color
                            else self.icon_color
                        ),
                        "_selected": False,
                    }
                )
            for name in self.__sort_files(files):
                if self.ext and os.path.splitext(name)[1] not in self.ext:
                    continue

                manager_list.append(
                    {
                        "viewclass": "MDFileManagerItem",
                        "path": name,
                        "icon": "file-outline",
                        "dir_or_file_name": os.path.split(name)[1],
                        "events_callback": self.select_dir_or_file,
                        "icon_color": (
                            self.theme_cls.primaryColor
                            if not self.icon_color
                            else self.icon_color
                        ),
                        "_selected": False,
                    }
                )

        self.ids.rv.data = manager_list
        self._show()

    def get_access_string(self, path: str) -> str:
        access_string = ""
        if self.use_access:
            access_data = {"r": os.R_OK, "w": os.W_OK, "x": os.X_OK}
            for access in access_data.keys():
                access_string += (
                    access if os.access(path, access_data[access]) else "-"
                )
        return access_string

    def get_content(
        self,
    ) -> Union[Tuple[List[str], List[str]], Tuple[None, None]]:
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

    def close(self) -> None:
        """Closes the file manager window."""

        self.dispatch("on_pre_dismiss")
        self._window_manager.dismiss()
        self.dispatch("on_dismiss")
        self._window_manager_open = False

    def select_dir_or_file(
        self,
        path: str,
        widget: MDFileManagerItemPreview | MDFileManagerItem,
    ) -> None:
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

    def back(self) -> None:
        """Returning to the branch down in the directory tree."""

        path, end = os.path.split(self.current_path)

        if self.current_path and path == self.current_path:
            self.show_disks()
        else:
            if not end:
                self.close()
                self.exit_manager(1)
            else:
                self.show(path)

    def select_directory_on_press_button(self, *args) -> None:
        """Called when a click on a floating button."""

        if self.selector == "multi":
            if len(self.selection) > 0:
                self.select_path(self.selection)
        else:
            if self.selector == "folder" or self.selector == "any":
                self.select_path(self.current_path)

    def on_icon(self, instance_file_manager, icon_name: str) -> None:
        """Called when the :attr:`icon` property is changed."""

        self.icon_selection_button = icon_name

    def on_background_color_toolbar(
        self, instance_file_manager, color: str | list
    ) -> None:
        """
        Called when the :attr:`background_color_toolbar` property is changed.
        """

        def on_background_color_toolbar(*args) -> None:
            self.ids.toolbar.md_bg_color = color

        Clock.schedule_once(on_background_color_toolbar)

    def on_pre_open(self, *args) -> None:
        """
        Default pre-open event handler.

        .. versionadded:: 1.1.0
        """

    def on_open(self, *args) -> None:
        """
        Default open event handler.

        .. versionadded:: 1.1.0
        """

    def on_pre_dismiss(self, *args) -> None:
        """
        Default pre-dismiss event handler.

        .. versionadded:: 1.1.0
        """

    def on_dismiss(self, *args) -> None:
        """
        Default dismiss event handler.

        .. versionadded:: 1.1.0
        """

    def _show(self):
        if not self._window_manager:
            self._window_manager = ModalView(
                size_hint=self.size_hint, auto_dismiss=False
            )
            self.size_hint = (1, 1)
            self._window_manager.add_widget(self)

        if not self._window_manager_open:
            self._window_manager.open()
            self._window_manager_open = True

        self.dispatch("on_pre_open")
        self.dispatch("on_open")

    def _create_selection_button(self, *args):
        if (
            self.selector == "any"
            or self.selector == "multi"
            or self.selector == "folder"
        ):
            self.selection_button = MDFabButton(
                on_release=self.select_directory_on_press_button,
                theme_bg_color="Custom",
                md_bg_color=(
                    self.theme_cls.primaryColor
                    if not self.background_color_selection_button
                    else self.background_color_selection_button
                ),
                icon=self.icon_selection_button,
                pos_hint={"right": 0.99},
                y=dp(12),
            )
            self.add_widget(self.selection_button)

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
