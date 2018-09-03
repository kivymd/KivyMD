# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.properties import BoundedNumericProperty, ReferenceListProperty, \
    StringProperty, ListProperty, BooleanProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivymd.button import MDIconButton
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.list import ILeftBody
from kivymd.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior


Builder.load_string('''
<MDCard>
    canvas:
        Color:
            rgba: self.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [self.border_radius]
        Color:
            rgba: self.theme_cls.divider_color
            a: self.border_color_a
        Line:
            rounded_rectangle:
                (self.pos[0],self.pos[1],self.size[0],self.size[1],self.border_radius) 
    md_bg_color: self.theme_cls.bg_light
    

<MDSeparator>
    canvas:
        Color:
            rgba: self.theme_cls.divider_color
        Rectangle:
            size: self.size
            pos: self.pos


<CardPost>:
    spacing: dp(5)
    padding: dp(5)
    orientation: 'vertical'
    size_hint: None, None
    size: root.card_size

    BoxLayout:
        id: title_box
        size_hint_y: None
        height: dp(50)
        spacing: dp(10)

        LeftIcon:
            source: root.path_to_avatar
            size_hint_x: None
            width: self.height
            allow_stretch: True

        MDLabel:
            markup: True
            text: root.name_data
            text_size: self.width, None
            theme_text_color: 'Primary'
            bold: True
            font_size: '12sp'

    MDSeparator:
        height: dp(1)

    MDLabel:
        id: text_post
        text: root.text_post
        markup: True
        font_size: '14sp'
        size_hint_y: None
        valign: 'top'
        height: self.texture_size[1]
        text_size: self.width - dp(5), None
        theme_text_color: 'Primary'

    Widget:

''')


class MDSeparator(ThemableBehavior, BoxLayout):
    """ A separator line """

    def __init__(self, *args, **kwargs):
        super(MDSeparator, self).__init__(*args, **kwargs)
        self.on_orientation()
    
    def on_orientation(self,*args):
        self.size_hint = (1, None) if self.orientation == 'horizontal' else (None, 1)
        if self.orientation == 'horizontal':
            self.height = dp(1)
        else:
            self.width = dp(1)


class MDCard(ThemableBehavior, RectangularElevationBehavior, BoxLayout):
    r = BoundedNumericProperty(1., min=0., max=1.)
    g = BoundedNumericProperty(1., min=0., max=1.)
    b = BoundedNumericProperty(1., min=0., max=1.)
    a = BoundedNumericProperty(0., min=0., max=1.)
    
    border_radius = BoundedNumericProperty(dp(3),min=0)
    border_color_a = BoundedNumericProperty(0, min=0., max=1.)
    md_bg_color = ReferenceListProperty(r, g, b, a)


class LeftIcon(ILeftBody, Image):
    pass


class CardPost(MDCard):
    name_data = StringProperty('Name Author\nDate and time')
    text_post = StringProperty('Your text post...')
    path_to_avatar = StringProperty('./assets/avatar.png')
    card_size = ListProperty((Window.width - 10, dp(180)))

    right_menu = ListProperty()
    '''If the list is not empty a button will be added to display the menu list
    '''

    likes_stars = BooleanProperty(False)
    '''If True, stars will be added to the card for evaluation
    '''

    callback_on_star = ObjectProperty(lambda x: None)

    _list_instance_likes_stars = ListProperty()

    def __init__(self, **kwargs):
        super(CardPost, self).__init__(**kwargs)
        # ---------------------------------------------------------------------
        if len(self.right_menu):
            self.ids.title_box.add_widget(
                MDIconButton(
                    icon='dots-vertical',
                    on_release=self.open_menu))
        # ---------------------------------------------------------------------
        if self.likes_stars:
            box_likes_stars_right = AnchorLayout(
                anchor_x='right', size_hint_y=None, height=dp(30))
            self.box_likes_stars = BoxLayout(spacing=(dp(5)))
            self.box_likes_stars.add_widget(Widget())
            for i in range(5):  # adding stars
                like_star = MDIconButton(
                    icon='star-outline', size_hint=(None, None),
                    size=(dp(30), dp(30)), id=str(i),
                    on_release=lambda x, y=i: self._update_likes_stars(y))
                self.box_likes_stars.add_widget(like_star)
                self._list_instance_likes_stars.append(like_star)
            box_likes_stars_right.add_widget(self.box_likes_stars)
            self.add_widget(box_likes_stars_right)

    def open_menu(self, instance):
        MDDropdownMenu(items=self.right_menu, width_mult=3).open(instance)

    def _update_likes_stars(self, index_star):
        i = 0
        for instance_like_star in self._list_instance_likes_stars:
            if int(instance_like_star.id) <= index_star:
                if instance_like_star.icon == 'star-outline':
                    instance_like_star.icon = 'star'
                    i = 1
                else:
                    if int(instance_like_star.id) == index_star:
                        instance_like_star.icon = 'star-outline'
            elif int(instance_like_star.id) >= index_star:
                if instance_like_star.icon == 'star':
                    instance_like_star.icon = 'star-outline'
        self.callback_on_star(index_star + i)
