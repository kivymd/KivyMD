# -*- coding: utf-8 -*-

"""
progressloader.py

Progressbar downloads files from the server.

A simple manager for selecting directories and files.
Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

EXAMPLE:

import os

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.progressloader import MDProgressLoader
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string(
'''
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDRaisedButton kivymd.button.MDRaisedButton


<Root@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(5)

    Toolbar:
        id: toolbar
        title: 'MD Progress Loader'
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        MDRaisedButton:
            text: "Download file"
            size_hint: None, None
            size: 3 * dp(48), dp(48)
            opposite_colors: True
            on_release: app.show_example_download_file()
''')


class Test(App):
    theme_cls = ThemeManager()

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def build(self):
        self.main_widget = Factory.Root()
        return self.main_widget

    def set_chevron_back_screen(self):
        '''Sets the return chevron to the previous screen in ToolBar.'''

        self.main_widget.ids.toolbar.right_action_items = []

    def download_progress_hide(self, instance_progress, value):
        '''Hides progress progress.'''

        instance_progress.dismiss()
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
        progress.open()
        Clock.schedule_once(progress.download_start, .1)
        progress.animation_progress_from_fade()

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')


Test().run()

"""

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.network.urlrequest import UrlRequest
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty


Builder.load_string('''
#:import Window kivy.core.window.Window
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDLabel kivymd.label.MDLabel
#:import MDCard kivymd.card.MDCard


<MDProgressLoader>:
    size_hint: .8, None
    height: spinner.height + dp(20)
    auto_dismiss: False
    background: 'images/transparent.png'

    FloatLayout:

        MDCard:
            id: window_progress
            pos: (Window.width // 2) - (self.width // 2), (Window.height // 2) - (self.height // 2)
            size_hint_y: None
            size_hint_x: .8
            height: spinner.height + dp(20)
            spacing: dp(10)
            padding: dp(10)#, dp(50), dp(10), dp(20)

            MDSpinner
                id: spinner
                size_hint: None, None
                size: dp(46), dp(46)

            MDLabel:
                id: label_download
                shorten: True
                max_lines: 1
                halign: 'left'
                valign: 'top'
                text_size: self.width, None
                size_hint_y: None
                height: spinner.height

            Widget:
                size_hint_x: .1
''')


class MDProgressLoader(ModalView):
    path_to_file = StringProperty()
    '''The path to which the uploaded file will be saved.'''

    url_on_image = StringProperty()
    '''Link to uploaded file.'''

    label_download = StringProperty('Download')
    '''Signature of the downloaded file.'''

    download_complete = ObjectProperty()
    '''Function, called after a successful file upload.'''

    download_hide = ObjectProperty(lambda x: None)
    '''Function that is called when the download window is closed.'''

    download_flag = BooleanProperty(False)
    '''If True - the download process is in progress.'''

    def __init__(self, **kwargs):
        super(MDProgressLoader, self).__init__(**kwargs)

    def download_start(self, *args):
        self.download_flag = True
        self.retrieve_progress_load(self.url_on_image, self.path_to_file)
        self.open()
        Clock.schedule_once(self.animation_progress_to_fade, 2.5)

    def draw_progress(self, percent):
        '''
        :type percent: int;
        :param percent: loading percentage;

        '''

        self.ids.label_download.text = '%s: %d %%' % (
        self.label_download, percent)

    def animation_progress_to_fade(self, interval):
        if not self.download_flag:
            return

        animation = Animation(
            center_y=Window.height, center_x=Window.width,
            opacity=0, d=0.2, t='out_quad'
        )
        animation.bind(on_complete=lambda x, y: self.download_hide(self, None))
        animation.start(self.ids.window_progress)

    def animation_progress_from_fade(self):
        animation = Animation(
            center_y=Window.height // 2, center_x=Window.width // 2,
            opacity=1, d=0.2, t='out_quad'
        )
        animation.start(self.ids.window_progress)
        Clock.schedule_once(self.animation_progress_to_fade, 2.5)

    def retrieve_progress_load(self, url, path):
        '''
        :type url: str;
        :param url: link to content;

        :type path: str;
        :param path: path to save content;
        '''

        req = UrlRequest(
            url, on_progress=self.update_progress, chunk_size=1024,
            on_success=self.on_success, file_path=path)

    def update_progress(self, request, current_size, total_size):
        percent = current_size * 100 // total_size
        self.draw_progress(percent)

    def on_success(self, req, result):
        self.dismiss()
        self.download_complete()
        self.download_flag = False
