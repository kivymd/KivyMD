"""
Accordion List Item
===================

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.button import MDIconButton
from kivymd.list import ILeftBodyTouch
from kivymd.theming import ThemeManager
from kivymd.accordionlistitem import MDAccordionListItem
from kivymd.toast import toast

Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import TwoLineIconListItem kivymd.list.TwoLineIconListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton


<ContentForAnimCard>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:
        MDRoundFlatButton:
            text: "Free call"
            on_press: root.callback(self.text)
        Widget:
        MDRoundFlatButton:
            text: "Free message"
            on_press: root.callback(self.text)
        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: root.callback(self.text)
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]"\
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'


<ExampleAccordionList@BoxLayout>
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: 'Primary'
        elevation: 10
        left_action_items: [['dots-vertical', lambda x: None]]

    Screen:

        ScrollView:

            GridLayout:
                id: anim_list
                cols: 1
                size_hint_y: None
                height: self.minimum_height
''')


class ContentForAnimCard(BoxLayout):
    callback = ObjectProperty(lambda x: None)


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = "Example Accordion List"
    main_widget = None

    def build(self):
        self.main_widget = Factory.ExampleAccordionList()
        return self.main_widget

    def on_start(self):
        def callback(text):
            toast(f'{text} to {content.name_item}')

        content = ContentForAnimCard(callback=callback)
        names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko')

        for name_contact in names_contacts:
            self.main_widget.ids.anim_list.add_widget(
                MDAccordionListItem(content=content,
                                    icon='data/logo/kivy-icon-128.png',
                                    title=name_contact))


Example().run()
"""

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivymd.button import MDIconButton
from kivymd.list import IRightBodyTouch, OneLineAvatarIconListItem, ILeftBody

Builder.load_string(
    """
<AccordionListItem>
    text: root.title

    AvatarLeft:
        source: root.icon

    ChevronRight:
        icon: 'chevron-right'
        disabled: True

        canvas.before:
            PushMatrix
            Rotate:
                angle: self.angle
                axis: (0, 0, 1)
                origin: self.center
        canvas.after:
            PopMatrix


<MDAccordionListItem>
    size_hint_y: None
    height: dp(68)

    BoxLayout:
        id: box_item
        size_hint_y: None
        height: root.height
        orientation: 'vertical'

        AccordionListItem:
            id: item_anim
            title: root.title
            icon: root.icon
            _no_ripple_effect: True
            on_press: root.check_open_box(self)
"""
)


class AvatarLeft(ILeftBody, Image):
    pass


class ChevronRight(IRightBodyTouch, MDIconButton):
    angle = NumericProperty(0)


class AccordionListItem(OneLineAvatarIconListItem):
    title = StringProperty()
    icon = StringProperty()


class MDAccordionListItem(BoxLayout):
    content = ObjectProperty()
    icon = StringProperty()
    title = StringProperty()

    def check_open_box(self, instance):
        press_current_item = False

        for box in self.parent.children:
            if len(box.ids.box_item.children) == 2:
                if instance is box.ids.item_anim:
                    press_current_item = True
                box.ids.box_item.remove_widget(box.ids.box_item.children[0])
                chevron = box.ids.box_item.children[0].children[0].children[0]
                self.anim_chevron_up(chevron)
                self.anim_resize_close(box)
                break

        if not press_current_item:
            self.anim_chevron_down()

    def anim_chevron_down(self):
        chevron = self.ids.item_anim.children[0].children[0]
        angle = -90
        Animation(angle=angle, d=0.2).start(chevron)
        self.anim_resize_open_item()

    def anim_chevron_up(self, instance):
        angle = 0
        Animation(angle=angle, d=0.2).start(instance)

    def anim_resize_close(self, box):
        Animation(height=dp(68), d=0.1, t="in_cubic").start(box)

    def anim_resize_open_item(self, *args):
        self.content.name_item = self.title
        anim = Animation(height=self.content.height + dp(70), d=0.2, t="in_cubic")
        anim.bind(on_complete=self.add_content)
        anim.start(self)

    def add_content(self, *args):
        if self.content:
            self.ids.box_item.add_widget(self.content)
