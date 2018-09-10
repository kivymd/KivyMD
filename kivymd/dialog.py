# -*- coding: utf-8 -*-

'''
dailog.py

Copyright © 2010-2018 HeaTTheatR

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

EXAMPLE:

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.utils import get_hex_from_color

from kivymd.dialog import MDInputDialog, MDOkCancelDialog
from kivymd.theming import ThemeManager


Builder.load_string("""
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton


<ExampleDialogs@BoxLayout>:
    orientation: 'vertical'
    spacing: dp(5)

    Toolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    FloatLayout:
        MDRectangleFlatButton:
            text: "Open input dialog"
            pos_hint: {'center_x': .5, 'center_y': .7}
            opposite_colors: True
            on_release: app.show_example_input_dialog()

        MDRectangleFlatButton:
            text: "Open Ok Cancel dialog"
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release: app.show_example_okcancel_dialog()
""")


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Dialogs"

    def build(self):
        return Factory.ExampleDialogs()

    def show_example_input_dialog(self):
        dialog = MDInputDialog(
            title='Title', hint_text='Hint text', size_hint=(.8, .4),
            text_button_ok='Yes', events_callback=lambda x: None)
        dialog.open()

    def show_example_okcancel_dialog(self):
        dialog = MDOkCancelDialog(
            title='Title', size_hint=(.8, .3), text_button_ok='Yes',
            text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
                self.theme_cls.primary_color),
            text_button_cancel='Cancel', events_callback=lambda x: None)
        dialog.open()


Example().run()
'''

from kivy.logger import Logger
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from kivy.animation import Animation
from kivy.uix.popup import PopupException

from kivymd.card import MDCard
from kivymd.theming import ThemableBehavior
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.button import MDFlatButton


Builder.load_string('''
#:import MDTextField kivymd.textfields.MDTextField
#:import MDCard kivymd.card.MDCard


<MDDialog>:
    canvas:
        Color:
            rgba: self.theme_cls.bg_light
        Rectangle:
            size: self.size
            pos: self.pos

    _container: container
    _action_area:action_area
    elevation: 12
    GridLayout:
        cols: 1
        GridLayout:
            cols: 1
            padding: dp(24), dp(24), dp(24), dp(24)
            spacing: dp(20)
            MDLabel:
                text: root.title
                font_style: 'Title'
                theme_text_color: 'Primary'
                halign: 'left'
                valign: 'middle'
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]
            ScrollView:
                effect_cls: 'ScrollEffect'
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    id: container
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'center'
            size_hint: 1, None
            height: dp(52) if len(root._action_buttons) > 0 else 0
            padding: dp(8), dp(8)
            GridLayout:
                id: action_area
                rows: 1
                size_hint: None, None if len(root._action_buttons) > 0 else 1
                height: dp(36) if len(root._action_buttons) > 0 else 0
                width: self.minimum_width
                spacing: dp(8)


<ContentInputDialog>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    MDLabel:
        font_style: 'Title'
        theme_text_color: 'Primary'
        text: root.title
        halign: 'left'

    MDTextField:
        id: text_field
        size_hint: 1, None
        height: dp(48)
        hint_text: root.hint_text

    Widget:
    Widget:

    AnchorLayout:
        anchor_x: 'right'

        MDFlatButton:
            text: root.text_button_ok
            #theme_text_color: 'Custom'
            #text_color: app.theme_cls.primary_color
            on_release: root.events_callback(text_field.text)


<ContentMDOkCancelDialog>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    MDLabel:
        text: root.title
        font_style: 'Title'
        theme_text_color: 'Primary'
        halign: 'left'
        valign: 'top'
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]

    MDLabel:
        theme_text_color: 'Primary'
        text: root.text
        size_hint_y: None
        height: self.texture_size[1]
        valign: 'top'
        markup: True

    Widget:

    AnchorLayout:
        anchor_x: 'right'
        size_hint_y: None
        height: dp(30)

        BoxLayout:
            size_hint_x: None
            width: self.minimum_width
            spacing: dp(5)

            MDRaisedButton:
                text: root.text_button_ok
                #theme_text_color: 'Custom'
                #text_color: app.theme_cls.primary_color
                on_release: root.events_callback(self.text)

            MDFlatButton:
                text: root.text_button_cancel
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
                on_release: root.events_callback(self.text)
''')


class MDDialog(ThemableBehavior, RectangularElevationBehavior, ModalView):
    title = StringProperty('')
    content = ObjectProperty(None)
    md_bg_color = ListProperty([0, 0, 0, .2])
    _container = ObjectProperty()
    _action_buttons = ListProperty([])
    _action_area = ObjectProperty()

    def __init__(self, **kwargs):
        super(MDDialog, self).__init__(**kwargs)
        self.bind(_action_buttons=self._update_action_buttons,
                  auto_dismiss=lambda *x: setattr(
                      self.shadow, 'on_release',
                      self.shadow.dismiss if self.auto_dismiss else None))

    def add_action_button(self, text, action=None):
        """Add an :class:`FlatButton` to the right of the action area.

        :param icon: Unicode character for the icon
        :type icon: str or None
        :param action: Function set to trigger when on_release fires
        :type action: function or None
        """

        button = MDFlatButton(text=text,
                              size_hint=(None, None),
                              height=dp(36))
        if action:
            button.bind(on_release=action)
        button.text_color = self.theme_cls.primary_color
        button.md_bg_color = self.theme_cls.bg_light
        self._action_buttons.append(button)

    def add_widget(self, widget):
        if self._container:
            if self.content:
                raise PopupException(
                    'Popup can have only one widget as content')
            self.content = widget
        else:
            super(MDDialog, self).add_widget(widget)

    def open(self, *largs):
        '''Show the view window from the :attr:`attach_to` widget. If set, it
        will attach to the nearest window. If the widget is not attached to any
        window, the view will attach to the global
        :class:`~kivy.core.window.Window`.
        '''

        if self._window is not None:
            Logger.warning('ModalView: you can only open once.')
            return self
        # search window
        self._window = self._search_window()
        if not self._window:
            Logger.warning('ModalView: cannot open view, no window found.')
            return self
        self._window.add_widget(self)
        self._window.bind(on_resize=self._align_center,
                          on_keyboard=self._handle_keyboard)
        self.center = self._window.center
        self.bind(size=self._align_center)
        a = Animation(_anim_alpha=1., d=self._anim_duration)
        a.bind(on_complete=lambda *x: self.dispatch('on_open'))
        a.start(self)
        return self

    def dismiss(self, *largs, **kwargs):
        '''Close the view if it is open. If you really want to close the
        view, whatever the on_dismiss event returns, you can use the *force*
        argument:
        ::

            view = ModalView(...)
            view.dismiss(force=True)

        When the view is dismissed, it will be faded out before being
        removed from the parent. If you don't want animation, use::

            view.dismiss(animation=False)

        '''
        if self._window is None:
            return self
        if self.dispatch('on_dismiss') is True:
            if kwargs.get('force', False) is not True:
                return self
        if kwargs.get('animation', True):
            Animation(_anim_alpha=0., d=self._anim_duration).start(self)
        else:
            self._anim_alpha = 0
            self._real_remove_widget()
        return self

    def on_content(self, instance, value):
        if self._container:
            self._container.clear_widgets()
            self._container.add_widget(value)

    def on__container(self, instance, value):
        if value is None or self.content is None:
            return
        self._container.clear_widgets()
        self._container.add_widget(self.content)

    def on_touch_down(self, touch):
        if self.disabled and self.collide_point(*touch.pos):
            return True
        return super(MDDialog, self).on_touch_down(touch)

    def _update_action_buttons(self, *args):
        self._action_area.clear_widgets()
        for btn in self._action_buttons:
            btn.content.texture_update()
            btn.width = btn.content.texture_size[0] + dp(16)
            self._action_area.add_widget(btn)


class MDInputDialog(ModalView):
    title = StringProperty('Title')
    hint_text = StringProperty('Write something')
    text_button_ok = StringProperty('OK')
    events_callback = ObjectProperty()

    def __init__(self, **kwargs):
        super(MDInputDialog, self).__init__(**kwargs)
        self.set_content()

    def set_content(self, *args):
        def set_field_focus(interval):
            content_dialog.ids.text_field.focus = True

        def _events_callback(result_press):
            self.dismiss()
            if result_press:
                self.events_callback(
                    content_dialog.ids.text_field.text)

        content_dialog = ContentInputDialog(
            title=self.title, hint_text=self.hint_text,
            text_button_ok=self.text_button_ok,
            events_callback=_events_callback)
        self.add_widget(content_dialog)
        Clock.schedule_once(set_field_focus, .5)


class ContentInputDialog(MDCard):
    text_button_ok = StringProperty()
    hint_text = StringProperty()
    title = StringProperty()
    events_callback = ObjectProperty()


class MDOkCancelDialog(ModalView):
    title = StringProperty('Title')
    text = StringProperty('Text dialog')
    text_button_cancel = StringProperty('CANCEL')
    text_button_ok = StringProperty('OK')
    events_callback = ObjectProperty()

    def __init__(self, **kwargs):
        super(MDOkCancelDialog, self).__init__(**kwargs)
        self.set_content()

    def set_content(self, *args):
        def _events_callback(result_press):
            self.dismiss()
            if result_press:
                self.events_callback(result_press)

        content_dialog = ContentMDOkCancelDialog(
            title=self.title, text=self.text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            events_callback=_events_callback)
        self.add_widget(content_dialog)


class ContentMDOkCancelDialog(MDCard):
    title = StringProperty()
    text = StringProperty()
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty()
    events_callback = ObjectProperty()
