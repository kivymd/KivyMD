"""
Dialog
======

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Dialogs <https://material.io/design/components/dialogs.html>`_

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.utils import get_hex_from_color

from kivymd.dialog import MDInputDialog, MDDialog
from kivymd.theming import ThemeManager


Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton


<ExampleDialogs@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
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
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Dialogs"

    def build(self):
        return Factory.ExampleDialogs()

    def callback_for_menu_items(self, *args):
        from kivymd.toast.kivytoast import toast
        toast(args[0])

    def show_example_input_dialog(self):
        dialog = MDInputDialog(
            title='Title', hint_text='Hint text', size_hint=(.8, .4),
            text_button_ok='Yes',
            events_callback=self.callback_for_menu_items)
        dialog.open()

    def show_example_okcancel_dialog(self):
        dialog = MDDialog(
            title='Title', size_hint=(.8, .3), text_button_ok='Yes',
            text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
                self.theme_cls.primary_color),
            text_button_cancel='Cancel',
            events_callback=self.callback_for_menu_items)
        dialog.open()


Example().run()
"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput

from kivymd.cards import MDCard
from kivymd.textfields import MDTextField, MDTextFieldRect
from kivymd.theming import ThemableBehavior
from kivymd.button import MDFlatButton, MDRaisedButton, MDTextButton
from kivymd import images_path
from kivymd.material_resources import DEVICE_IOS


Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import MDSeparator kivymd.cards.MDSeparator


<ContentInputDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    MDLabel:
        font_style: 'H6'
        text: root.title
        halign: 'left' if not root.device_ios else 'center'

    BoxLayout:
        id: box_input
        size_hint: 1, None

    Widget:
    Widget:

    MDSeparator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0


<ContentMDDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    text_button_ok: ''
    text_button_cancel: ''

    MDLabel:
        id: title
        text: root.title
        font_style: 'H6'
        halign: 'left' if not root.device_ios else 'center'
        valign: 'top'
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]

    ScrollView:
        id: scroll
        size_hint_y: None
        height:
            root.height - (box_buttons.height + title.height + dp(48)\
            + sep.height)

        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                #source: f'{images_path}dialog_in_fade.png'
                source: f'{images_path}transparent.png'

        MDLabel:
            text: '\\n' + root.text + '\\n'
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'top'
            halign: 'left' if not root.device_ios else 'center'
            markup: True

    MDSeparator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0
"""
)

if DEVICE_IOS:
    Heir = BoxLayout
else:
    Heir = MDCard


# FIXME: Not work themes for iOS.
class BaseDialog(ThemableBehavior, ModalView):
    def set_content(self, instance_content_dialog):
        def _events_callback(result_press):
            self.dismiss()
            if result_press:
                self.events_callback(result_press, self)

        if self.device_ios:  # create buttons for iOS
            self.background = self._background

            if instance_content_dialog.__class__ is ContentInputDialog:
                self.text_field = MDTextFieldRect(
                    pos_hint={"center_x": 0.5},
                    size_hint=(1, None),
                    multiline=False,
                    height=dp(33),
                    cursor_color=self.theme_cls.primary_color,
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(33)
                instance_content_dialog.ids.box_input.add_widget(self.text_field)

            if self.text_button_cancel != "":
                anchor = "left"
            else:
                anchor = "center"
            box_button_ok = AnchorLayout(anchor_x=anchor)
            box_button_ok.add_widget(
                MDTextButton(
                    text=self.text_button_ok,
                    font_size="18sp",
                    on_release=lambda x: _events_callback(self.text_button_ok),
                )
            )
            instance_content_dialog.ids.box_buttons.add_widget(box_button_ok)

            if self.text_button_cancel != "":
                box_button_ok.anchor_x = "left"
                box_button_cancel = AnchorLayout(anchor_x="right")
                box_button_cancel.add_widget(
                    MDTextButton(
                        text=self.text_button_cancel,
                        font_size="18sp",
                        on_release=lambda x: _events_callback(self.text_button_cancel),
                    )
                )
                instance_content_dialog.ids.box_buttons.add_widget(box_button_cancel)

        else:  # create buttons for Android
            if instance_content_dialog.__class__ is ContentInputDialog:
                self.text_field = MDTextField(
                    size_hint=(1, None),
                    height=dp(48),
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(48)
                instance_content_dialog.ids.box_input.add_widget(self.text_field)
                instance_content_dialog.ids.box_buttons.remove_widget(
                    instance_content_dialog.ids.sep
                )

            box_buttons = AnchorLayout(
                anchor_x="right", size_hint_y=None, height=dp(30)
            )
            box = BoxLayout(size_hint_x=None, spacing=dp(5))
            box.bind(minimum_width=box.setter("width"))
            button_ok = MDRaisedButton(
                text=self.text_button_ok,
                on_release=lambda x: _events_callback(self.text_button_ok),
            )
            box.add_widget(button_ok)

            if self.text_button_cancel != "":
                button_cancel = MDFlatButton(
                    text=self.text_button_cancel,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: _events_callback(self.text_button_cancel),
                )
                box.add_widget(button_cancel)

            box_buttons.add_widget(box)
            instance_content_dialog.ids.box_buttons.add_widget(box_buttons)
            instance_content_dialog.ids.box_buttons.height = button_ok.height
            instance_content_dialog.remove_widget(instance_content_dialog.ids.sep)


class MDInputDialog(BaseDialog):
    title = StringProperty("Title")
    hint_text = StringProperty()
    text_button_ok = StringProperty("Ok")
    text_button_cancel = StringProperty()
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.content_dialog = ContentInputDialog(
            title=self.title,
            hint_text=self.hint_text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(self.content_dialog)
        self.set_content(self.content_dialog)
        Clock.schedule_once(self.set_field_focus, 0.5)

    def set_field_focus(self, interval):
        self.text_field.focus = True


class MDDialog(BaseDialog):
    title = StringProperty("Title")
    text = StringProperty("Text dialog")
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty("Ok")
    events_callback = ObjectProperty()
    _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content_dialog = ContentMDDialog(
            title=self.title,
            text=self.text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(content_dialog)
        self.set_content(content_dialog)


class ContentInputDialog(Heir):
    title = StringProperty()
    hint_text = StringProperty()
    text_button_ok = StringProperty()
    text_button_cancel = StringProperty()
    device_ios = BooleanProperty()


class ContentMDDialog(Heir):
    title = StringProperty()
    text = StringProperty()
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty()
    device_ios = BooleanProperty()
