"""
File Manager
============

Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

A simple manager for selecting directories and files.

Example
-------

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.modalview import ModalView

from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string('''


<ExampleFileManager@BoxLayout>
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


class Example(MDApp):
    title = "File Manage"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager.dismiss()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device..'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Example().run()
"""

import os
import threading

from PIL import Image

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    NumericProperty,
    OptionProperty,
)

import kivymd.material_resources as m_res
from kivymd import images_path
from kivymd.uix.list import (
    ILeftBodyTouch,
    ILeftBody,
    IRightBody,
    IRightBodyTouch,
)
from kivymd.uix.button import MDIconButton
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    CircularRippleBehavior,
)
from kivymd.theming import ThemableBehavior

ACTIVITY_MANAGER = """
#:import os os
#:import Window kivy.core.window.Window


<BodyManager@BoxLayout>
    icon: 'folder'
    path: ''
    background_normal: ''
    background_down: ''
    dir_or_file_name: ''
    access_string: ''
    events_callback: lambda x: None
    orientation: 'vertical'

    ModifiedOneLineIconListItem:
        text: root.dir_or_file_name
        on_release: root.events_callback(root.path)
        IconFolder:
            disabled: True
            icon: root.icon

    MDSeparator:


<LabelContent@MDLabel>
    size_hint_y: None
    height: self.texture_size[1]
    shorten: True
    shorten_from: 'center'
    halign: 'center'
    text_size: self.width, None


<BodyManagerWithPrevious>
    paths: []
    path: ''
    type: 'folder'
    events_callback: lambda x: None

    GridLayout:
        id: grid_box
        cols: 3
        row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
        row_force_default: True
        size_hint_y: None
        height: self.minimum_height
        padding: dp(4), dp(4)
        spacing: dp(4)

        BoxLayout:
            orientation: 'vertical'
            IconButton:
                mipmap: True
                source:
                    root.get_source(\
                    app, root.type, label_box_1, root.paths, 1, self)
                on_release:
                    root.events_callback(\
                    os.path.join(root.path, label_box_1.text))
            LabelContent:
                id: label_box_1
                text:
                    os.path.split(root.paths[0])[1].replace('thumb_', '')\
                    if len(root.paths) >= 1 else ''

        BoxLayout:
            orientation: 'vertical'
            IconButton:
                mipmap: True
                source:
                    root.get_source(\
                    app, root.type, label_box_2, root.paths, 2, self)
                on_release:
                    root.events_callback(\
                    os.path.join(root.path, label_box_2.text))
            LabelContent:
                id: label_box_2
                text:
                    os.path.split(root.paths[1])[1].replace('thumb_', '')\
                    if len(root.paths) >= 2 else ''

        BoxLayout:
            orientation: 'vertical'
            IconButton:
                mipmap: True
                source:
                    root.get_source(\
                    app, root.type, label_box_3, root.paths, 3, self)
                on_release:
                    root.events_callback(\
                    os.path.join(root.path, label_box_3.text))
            LabelContent:
                id: label_box_3
                text:
                    os.path.split(root.paths[2])[1].replace('thumb_', '')\
                    if len(root.paths) >= 3 else ''


<FloatButton>
    anchor_x: 'right'
    anchor_y: 'bottom'
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
    canvas:
        Color:
            rgba:
                1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(5)

        MDToolbar:
            id: toolbar
            title: '%s' % root.current_path
            right_action_items: [['close-box', lambda x: root.exit_manager(1)]]
            left_action_items: [['chevron-left', lambda x: root.back()]]
            elevation: 10
            md_bg_color: root.theme_cls.primary_color

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            bar_width: dp(4)
            bar_color: root.theme_cls.primary_color
            on_scroll_stop: root.update_list_images()

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'


<ModifiedBaseListItem>
    size_hint_y: None
    canvas:
        Color:
            rgba:
                self.theme_cls.divider_color if root.divider is not None\
                else (0, 0, 0, 0)

        Line:
            points: (root.x ,root.y, root.x+self.width, root.y)\
                    if root.divider == 'Full' else\
                    (root.x+root._txt_left_pad, root.y,\
                    root.x+self.width-root._txt_left_pad-root._txt_right_pad,\
                    root.y)

    BoxLayout:
        id: _text_container
        orientation: 'vertical'
        pos: root.pos
        padding:
            root._txt_left_pad, root._txt_top_pad,\
            root._txt_right_pad, root._txt_bot_pad

        MDLabel:
            id: _lbl_primary
            text: root.text
            font_style: root.font_style
            theme_text_color: root.theme_text_color
            size_hint_y: None
            shorten: True
            max_lines: 1
            height: self.texture_size[1]


<ModifiedOneLineIconListItem>
    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)
"""


class IconButton(CircularRippleBehavior, ButtonBehavior, AsyncImage):
    pass


class FloatButton(AnchorLayout):
    callback = ObjectProperty()
    md_bg_color = ListProperty([1, 1, 1, 1])
    icon = StringProperty()


class ModifiedBaseListItem(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, FloatLayout
):
    """Base class to all ListItems. Not supposed to be instantiated on its own.
    """

    text = StringProperty()
    """Text shown in the first line.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults
    to "".
    """

    text_color = ListProperty(None)
    """Text color used if theme_text_color is set to 'Custom'"""

    font_style = OptionProperty("Subtitle1", options=theme_font_styles)

    theme_text_color = StringProperty("Primary", allownone=True)
    """Theme text color for primary text"""

    secondary_text = StringProperty()
    """Text shown in the second and potentially third line.

    The text will wrap into the third line if the ListItem's type is set to
    \'one-line\'. It can be forced into the third line by adding a \\n
    escape sequence.

    :attr:`secondary_text` is a :class:`~kivy.properties.StringProperty` and
    defaults to "".
    """

    secondary_text_color = ListProperty(None)
    """Text color used for secondary text if secondary_theme_text_color 
    is set to 'Custom'"""

    secondary_theme_text_color = StringProperty("Secondary", allownone=True)
    """Theme text color for secondary primary text"""

    secondary_font_style = OptionProperty("Body1", options=theme_font_styles)

    divider = OptionProperty(
        "Full", options=["Full", "Inset", None], allownone=True
    )

    _txt_left_pad = NumericProperty(dp(16))
    _txt_top_pad = NumericProperty()
    _txt_bot_pad = NumericProperty()
    _txt_right_pad = NumericProperty(m_res.HORIZ_MARGINS)
    _num_lines = 2


class ModifiedOneLineListItem(ModifiedBaseListItem):
    """A one line list item"""

    _txt_top_pad = NumericProperty(dp(16))
    _txt_bot_pad = NumericProperty(dp(15))  # dp(20) - dp(5)
    _num_lines = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(48)


class ContainerSupport:
    """Overrides add_widget in a ListItem to include support for I*Body
    widgets when the appropiate containers are present.
    """

    _touchable_widgets = ListProperty()

    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, ILeftBody):
            self.ids["_left_container"].add_widget(widget)
        elif issubclass(widget.__class__, ILeftBodyTouch):
            self.ids["_left_container"].add_widget(widget)
            self._touchable_widgets.append(widget)
        elif issubclass(widget.__class__, IRightBody):
            self.ids["_right_container"].add_widget(widget)
        elif issubclass(widget.__class__, IRightBodyTouch):
            self.ids["_right_container"].add_widget(widget)
            self._touchable_widgets.append(widget)
        else:
            return super().add_widget(widget)

    def remove_widget(self, widget):
        super().remove_widget(widget)
        if widget in self._touchable_widgets:
            self._touchable_widgets.remove(widget)

    def on_touch_down(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, "down"):
            return
        super().on_touch_down(touch)

    def on_touch_move(self, touch, *args):
        if self.propagate_touch_to_touchable_widgets(touch, "move", *args):
            return
        super().on_touch_move(touch, *args)

    def on_touch_up(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, "up"):
            return
        super().on_touch_up(touch)

    def propagate_touch_to_touchable_widgets(self, touch, touch_event, *args):
        triggered = False
        for i in self._touchable_widgets:
            if i.collide_point(touch.x, touch.y):
                triggered = True
                if touch_event == "down":
                    i.on_touch_down(touch)
                elif touch_event == "move":
                    i.on_touch_move(touch, *args)
                elif touch_event == "up":
                    i.on_touch_up(touch)
        return triggered


class ModifiedOneLineIconListItem(ContainerSupport, ModifiedOneLineListItem):
    _txt_left_pad = NumericProperty(dp(72))


class IconFolder(ILeftBodyTouch, MDIconButton):
    pass


class BodyManagerWithPrevious(BoxLayout):
    def get_source(
        self, app, source_type, instance_label, paths, index, instance_content
    ):
        if source_type == "folder" and instance_label.text != "":
            source = f"{images_path}folder.png"
        else:
            if len(paths) >= index:
                source = paths[index - 1]
            else:
                source = f"{images_path}transparent.png"
        return source


# FIXME: Add color for Black and White theme
# FIXME: When you first create the application cache,
#        it crashes after a while with error:

"""
 Traceback (most recent call last):
   File "/home/kivy/Projects/KivyMD/demos/kitchen_sink/main.py", line 1698, 
       in <module>
     KitchenSink().run()
   File "/usr/lib/python3/dist-packages/kivy/app.py", line 826, in run
     runTouchApp()
   File "/usr/lib/python3/dist-packages/kivy/base.py", line 502, in runTouchApp
     EventLoop.window.mainloop()
   File "/usr/lib/python3/dist-packages/kivy/core/window/window_sdl2.py", 
       line 727, in mainloop
     self._mainloop()
   File "/usr/lib/python3/dist-packages/kivy/core/window/window_sdl2.py", 
       line 460, in _mainloop
     EventLoop.idle()
   File "/usr/lib/python3/dist-packages/kivy/base.py", line 337, in idle
     Clock.tick()
   File "/usr/lib/python3/dist-packages/kivy/clock.py", line 581, in tick
     self._process_events()

   File "kivy/_clock.pyx", line 384,
       in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7839)
   File "kivy/_clock.pyx", line 414,
       in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7597)
   File "kivy/_clock.pyx", line 412,
       in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7519)
   File "kivy/_clock.pyx", line 167,
       in kivy._clock.ClockEvent.tick (kivy/_clock.c:3248)
   File "/usr/lib/python3/dist-packages/kivy/cache.py",
       line 212, in _purge_by_timeout
     lastaccess = Cache._objects[category][key]['lastaccess']
 KeyError: '/path/to/image'
"""


class MDFileManager(ThemableBehavior, FloatLayout):
    icon = StringProperty("check")
    """The icon that will be used on the directory selection button."""

    exit_manager = ObjectProperty(lambda x: None)
    """Function called when the user reaches directory tree root."""

    select_path = ObjectProperty(lambda x: None)
    """Function, called when selecting a file/directory."""

    ext = ListProperty()
    """List of file extensions to be displayed
     in the manager. For example, ['py', 'kv'] - will filter out all files,
     except python scripts and Kv Language."""

    search = StringProperty("all")
    """It can take the values 'dirs' 'files' - display only directories
    or only files. By default, it displays and folders, and files."""

    current_path = StringProperty("/")
    """Current directory."""

    use_access = BooleanProperty(True)
    """Show accec to files and directories."""

    previous = BooleanProperty(False)
    """Shows only image previews."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = []  # directory navigation history
        # If False - do not add a directory to the history -
        # The user moves down the tree.
        self.history_flag = True
        toolbar_label = self.ids.toolbar.children[1].children[0]
        toolbar_label.font_style = "Subtitle1"

        if self.previous:
            self.ext = [".png", ".jpg", ".jpeg"]
            self.app = App.get_running_app()
            if not os.path.exists("%s/thumb" % self.app.user_data_dir):
                os.mkdir("%s/thumb" % self.app.user_data_dir)
        else:
            action_button = FloatButton(
                callback=self.select_directory_on_press_button,
                md_bg_color=self.theme_cls.primary_color,
                icon=self.icon,
            )
            self.add_widget(action_button)

    def update_list_images(self):
        self.ids.rv.refresh_from_layout()

    def split_list(self, l, n):
        n = max(1, n)
        return (l[i : i + n] for i in range(0, len(l), n))

    def create_previous(self, path):
        for image in os.listdir(path):
            _path = os.path.join(path, image)
            if os.path.isfile(_path):
                if self.count_ext(_path):
                    path_to_thumb = "%s/thumb/thumb_%s" % (
                        self.app.user_data_dir,
                        image,
                    )
                    if not os.path.exists(path_to_thumb):
                        im = Image.open(os.path.join(path, image))
                        im.thumbnail((200, 200))
                        im.save(path_to_thumb, "PNG")

    def check_theme(self):
        self.canvas.children[0].rgba = (
            [0, 0, 0, 1]
            if self.theme_cls.theme_style == "Dark"
            else [1, 1, 1, 1]
        )

    def show(self, path):
        """Forms the body of a directory tree."""

        self.check_theme()
        dirs, files = self.get_content(path)

        if self.previous:
            threading.Thread(target=self.create_previous, args=(path,)).start()
            split_dirs = self.split_list(dirs, 3)
            split_files = self.split_list(files, 3)

        self.current_path = path
        manager_list = []

        if dirs == [] and files == []:  # selected directory
            pass
        elif not dirs and not files:  # directory is unavailable
            return

        if self.previous:
            for list_dirs in split_dirs:
                manager_list.append(
                    {
                        "viewclass": "BodyManagerWithPrevious",
                        "path": path,
                        "paths": list_dirs,
                        "type": "folder",
                        "events_callback": self.select_dir_or_file,
                        "height": dp(105),
                    }
                )

            for list_files in list(split_files):
                manager_list.append(
                    {
                        "viewclass": "BodyManagerWithPrevious",
                        "path": path,
                        "paths": list_files,
                        "type": "files",
                        "events_callback": self.select_dir_or_file,
                        "height": dp(105),
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
                        "access_string": access_string,
                        "events_callback": self.select_dir_or_file,
                    }
                )

            for name in files:
                _path = path + name if path == "/" else path + "/" + name
                manager_list.append(
                    {
                        "viewclass": "BodyManager",
                        "path": _path,
                        "icon": "file-outline",
                        "dir_or_file_name": name,
                        "access_string": self.get_access_string(_path),
                        "events_callback": self.select_dir_or_file,
                    }
                )

        self.ids.rv.data = manager_list

    def count_ext(self, path):
        ext = os.path.splitext(path)[1]
        if ext != "":
            if ext.lower() in self.ext or ext.upper() in self.ext:
                return True
        return False

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
                if os.path.isdir("%s/%s" % (path, content)):
                    if self.search == "all" or self.search == "dirs":
                        dirs.append(content)
                else:
                    if self.search == "all" or self.search == "files":
                        if len(self.ext) != 0:
                            try:
                                if self.count_ext(content):
                                    if self.previous:
                                        files.append(
                                            "%s/thumb/thumb_%s"
                                            % (self.app.user_data_dir, content)
                                        )
                                    else:
                                        files.append(content)
                            except IndexError:
                                pass
                        else:
                            files.append(content)
            return dirs, files
        except OSError:
            self.history.pop()
            return None, None

    def select_dir_or_file(self, path):
        """Called by tap on the name of the directory or file."""

        if os.path.isfile(path):
            self.history = []
            self.select_path(path)
            return

        self.current_path = path
        self.show(path)

    def back(self):
        """Returning to the branch down in the directory tree."""

        if len(self.history) == 1:
            path, end = os.path.split(self.history[0])
            if end == "":
                self.exit_manager(1)
                return
            self.history[0] = path
        else:
            self.history.pop()
            path = self.history[-1]
        self.history_flag = False
        self.select_dir_or_file(path)

    def select_directory_on_press_button(self, *args):
        self.history = []
        self.select_path(self.current_path)


Builder.load_string(ACTIVITY_MANAGER)
