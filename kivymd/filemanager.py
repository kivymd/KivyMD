# -*- coding: utf-8 -*-

"""
filemanager.py

A simple manager for selecting directories and files.
Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

EXAMPLE:

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.filemanager import MDFileManager


class Test(App):

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGrey'

    def build(self):
        self.manager_open = False
        Window.bind(on_keyboard=self.events)
        self.box = BoxLayout()
        # More infromation about the parameters of the class, see
        # in the source code of the class MDFileManager.
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        self.add_button()

        return self.box

    def show(self, *args):
        self.box.clear_widgets()
        self.box.add_widget(self.file_manager)
        self.file_manager.show('/')  # вывод менеджера на экран
        self.manager_open = True

    def add_button(self):
        self.box.clear_widgets()
        self.box.add_widget(
            Button(text='Press for test...', on_release=self.show))

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;

        '''

        self.add_button()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.add_button()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Test().run()
"""

import os

from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex, hex_colormap
from kivy.properties import ObjectProperty, StringProperty, ListProperty, \
    BooleanProperty, NumericProperty, OptionProperty

import kivymd.material_resources as m_res
from kivymd.list import ILeftBodyTouch, ILeftBody, IRightBody, IRightBodyTouch
from kivymd.ripplebehavior import RectangularRippleBehavior
from kivymd.theming import ThemableBehavior
from kivymd.toolbar import Toolbar
from kivymd.button import MDFloatingActionButton, MDIconButton
from kivymd.card import MDSeparator


ACTIVITY_MANAGER = '''
<BodyManager@BoxLayout>:
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

<MDFileManager>:

    canvas:
        Color:
            rgba:
                1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        size_hint_y: None
        height: dp(40)
        y: root.height - toolbar.height
        spacing: dp(5)

        Toolbar:
            id: toolbar
            title: '%s' % root.current_path
            right_action_items: [['close-box', lambda x: root.exit_manager(1)]]
            elevation: 10
            md_bg_color: root.floating_button_color

    RecycleView:
        id: rv
        key_viewclass: 'viewclass'
        key_size: 'height'
        bar_width: dp(4)
        bar_color: root.floating_button_color
        y: -toolbar.height

        RecycleBoxLayout:
            default_size: None, dp(48)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

    AnchorLayout:
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
            on_release: root.select_directory_on_press_button()
            md_bg_color: root.floating_button_color


<ModifiedBaseListItem>:
    size_hint_y: None

    canvas:
        Color:
            rgba: self.theme_cls.divider_color if root.divider is not None else (0, 0, 0, 0)

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
        padding: root._txt_left_pad, root._txt_top_pad, root._txt_right_pad, root._txt_bot_pad

        MDLabel:
            id: _lbl_primary
            text: root.text
            font_style: root.font_style
            theme_text_color: root.theme_text_color
            size_hint_y: None
            shorten: True
            max_lines: 1
            height: self.texture_size[1]

<ModifiedOneLineIconListItem>:
    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)
'''


class ModifiedBaseListItem(ThemableBehavior, RectangularRippleBehavior,
                           ButtonBehavior, FloatLayout):
    '''Base class to all ListItems. Not supposed to be instantiated on its own.
    '''

    text = StringProperty()
    '''Text shown in the first line.

    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults
    to "".
    '''

    text_color = ListProperty(None)
    ''' Text color used if theme_text_color is set to 'Custom' '''

    font_style = OptionProperty(
        'Subhead', options=['Body1', 'Body2', 'Caption', 'Subhead', 'Title',
                            'Headline', 'Display1', 'Display2', 'Display3',
                            'Display4', 'Button', 'Icon'])

    theme_text_color = StringProperty('Primary', allownone=True)
    ''' Theme text color for primary text '''

    secondary_text = StringProperty()
    '''Text shown in the second and potentially third line.

    The text will wrap into the third line if the ListItem's type is set to
    \'one-line\'. It can be forced into the third line by adding a \\n
    escape sequence.

    :attr:`secondary_text` is a :class:`~kivy.properties.StringProperty` and
    defaults to "".
    '''

    secondary_text_color = ListProperty(None)
    ''' Text color used for secondary text if secondary_theme_text_color 
    is set to 'Custom' '''

    secondary_theme_text_color = StringProperty('Secondary', allownone=True)
    ''' Theme text color for secondary primary text '''

    secondary_font_style = OptionProperty(
        'Body1', options=['Body1', 'Body2', 'Caption', 'Subhead', 'Title',
                          'Headline', 'Display1', 'Display2', 'Display3',
                          'Display4', 'Button', 'Icon'])

    divider = OptionProperty('Full', options=['Full', 'Inset', None],
                             allownone=True)

    _txt_left_pad = NumericProperty(dp(16))
    _txt_top_pad = NumericProperty()
    _txt_bot_pad = NumericProperty()
    _txt_right_pad = NumericProperty(m_res.HORIZ_MARGINS)
    _num_lines = 2


class ModifiedOneLineListItem(ModifiedBaseListItem):
    ''' A one line list item'''

    _txt_top_pad = NumericProperty(dp(16))
    _txt_bot_pad = NumericProperty(dp(15))  # dp(20) - dp(5)
    _num_lines = 1

    def __init__(self, **kwargs):
        super(ModifiedOneLineListItem, self).__init__(**kwargs)
        self.height = dp(48)


class ContainerSupport:
    '''Overrides add_widget in a ListItem to include support for I*Body
    widgets when the appropiate containers are present.
    '''

    _touchable_widgets = ListProperty()

    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, ILeftBody):
            self.ids['_left_container'].add_widget(widget)
        elif issubclass(widget.__class__, ILeftBodyTouch):
            self.ids['_left_container'].add_widget(widget)
            self._touchable_widgets.append(widget)
        elif issubclass(widget.__class__, IRightBody):
            self.ids['_right_container'].add_widget(widget)
        elif issubclass(widget.__class__, IRightBodyTouch):
            self.ids['_right_container'].add_widget(widget)
            self._touchable_widgets.append(widget)
        else:
            return super(ModifiedBaseListItem, self).add_widget(widget)

    def remove_widget(self, widget):
        super(ModifiedBaseListItem, self).remove_widget(widget)
        if widget in self._touchable_widgets:
            self._touchable_widgets.remove(widget)

    def on_touch_down(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, 'down'):
            return
        super(ModifiedBaseListItem, self).on_touch_down(touch)

    def on_touch_move(self, touch, *args):
        if self.propagate_touch_to_touchable_widgets(touch, 'move', *args):
            return
        super(ModifiedBaseListItem, self).on_touch_move(touch, *args)

    def on_touch_up(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, 'up'):
            return
        super(ModifiedBaseListItem, self).on_touch_up(touch)

    def propagate_touch_to_touchable_widgets(self, touch, touch_event, *args):
        triggered = False
        for i in self._touchable_widgets:
            if i.collide_point(touch.x, touch.y):
                triggered = True
                if touch_event == 'down':
                    i.on_touch_down(touch)
                elif touch_event == 'move':
                    i.on_touch_move(touch, *args)
                elif touch_event == 'up':
                    i.on_touch_up(touch)
        return triggered


class ModifiedOneLineIconListItem(ContainerSupport, ModifiedOneLineListItem):
    _txt_left_pad = NumericProperty(dp(72))


class IconFolder(ILeftBodyTouch, MDIconButton):
    pass


class MDFileManager(ThemableBehavior, FloatLayout):
    home_path = StringProperty(os.path.split(__file__)[0])

    icon = StringProperty('check')
    '''The icon that will be used on the directory selection button.'''

    exit_manager = ObjectProperty(lambda x: None)
    '''Function called when the user reaches directory tree root.'''

    select_path = ObjectProperty(lambda x: None)
    '''Function, called when selecting a file/directory.'''

    ext = ListProperty()
    '''List of file extensions to be displayed
     in the manager. For example, ['py', 'kv'] - will filter out all files,
     except python scripts and Kv Language.'''

    search = StringProperty('all')
    '''It can take the values 'dirs' 'files' - display only directories
    or only files. By default, it displays and folders, and files.'''

    current_path = StringProperty('/')
    '''Current directory.'''

    floating_button_color = ListProperty(
        get_color_from_hex(hex_colormap['teal'])
    )
    '''Button color.'''

    use_access = BooleanProperty(True)
    '''Show accec to files and directories.'''

    def __init__(self, **kwargs):
        super(MDFileManager, self).__init__(**kwargs)
        self.history = []  # directory navigation history
         # If False - do not add a directory to the history -
         # The user moves down the tree.
        self.history_flag = True
        toolbar_label = self.ids.toolbar.children[1].children[0]
        toolbar_label.font_style = 'Subhead'

    def check_theme(self):
        print(self.canvas.children)
        self.canvas.children[0].rgba = \
            [0, 0, 0, 1] if self.theme_cls.theme_style == 'Dark' else [1, 1, 1, 1]

    def show(self, path):
        '''Forms the body of a directory tree.'''

        self.check_theme()
        dirs, files = self.get_content(path)
        self.current_path = path
        manager_list = []

        if dirs == [] and files == []:  # selected directory
            pass
        elif not dirs and not files:  # directory is unavailable
            return

        for name in dirs:
            _path = path + name if path == '/' else path + '/' + name
            access_string = self.get_access_string(_path)
            if 'r' not in access_string:
                icon = 'folder-lock'
            else:
                icon = 'folder'

            manager_list.append({
                'viewclass': 'BodyManager',
                'path': _path,
                'icon': icon,
                'dir_or_file_name': name,
                'access_string': access_string,
                'events_callback': self.select_dir_or_file
            })

        for name in files:
            _path = path + name if path == '/' else path + '/' + name
            manager_list.append({
                'viewclass': 'BodyManager',
                'path': _path,
                'icon': 'file-outline',
                'dir_or_file_name': name,
                'access_string': self.get_access_string(_path),
                'events_callback': self.select_dir_or_file
            })

        self.ids.rv.data = manager_list

    def get_access_string(self, path):
        access_string = ''
        if self.use_access:
            access_data = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
            for access in access_data.keys():
                access_string += access if os.access(path, access_data[
                    access]) else '-'

        return access_string

    def get_content(self, path):
        '''Returns a list of the type [[Folder List], [file list]].'''

        try:
            files = []
            dirs = []

            if self.history_flag:
                self.history.append(path)
            if not self.history_flag:
                self.history_flag = True

            for content in os.listdir(path):
                if os.path.isdir('%s/%s' % (path, content)):
                    if self.search == 'all' or self.search == 'dirs':
                        dirs.append(content)
                else:
                    if self.search == 'all' or self.search == 'files':
                        if len(self.ext) != 0:
                            try:
                                if content.split('.')[1].lower() in self.ext \
                                        or content.split('.')[1].upper() in self.ext:
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
        '''Called by tap on the name of the directory or file.'''

        if os.path.isfile(path):
            self.history = []
            self.select_path(path)
            return

        self.current_path = path
        self.show(path)

    def back(self):
        '''Returning to the branch down in the directory tree.'''

        if len(self.history) == 1:
            path, end = os.path.split(self.history[0])
            if end == '':
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
