"""
Cards
=====

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Cards <https://material.io/design/components/cards.html>`_

Example
-------

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.cards import MDCardPost
from kivymd.theming import ThemeManager
from kivymd.toast import toast


Builder.load_string('''
#:import MDToolbar kivymd.toolbar.MDToolbar


<ExampleCardPost@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)

    MDToolbar:
        id: toolbar
        title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color


    ScrollView:
        id: scroll
        size_hint: 1, 1
        do_scroll_x: False

        GridLayout:
            id: grid_card
            cols: 1
            spacing: dp(5)
            padding: dp(5)
            size_hint_y: None
            height: self.minimum_height
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    title = "Card Post"
    cards_created = False

    def build(self):
        self.screen = Factory.ExampleCardPost()
        return self.screen

    def on_start(self):
        def callback_for_menu_items(text_item):
            toast(text_item)

        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                toast('Delete post %s' % str(instance))

        instance_grid_card = self.screen.ids.grid_card
        buttons = ['facebook', 'vk', 'twitter']
        menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': callback_for_menu_items}
            for i in range(2)
        ]

        if not self.cards_created:
            self.cards_created = True

            instance_grid_card.add_widget(
                MDCardPost(text_post='Card with text',
                           swipe=True, callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    right_menu=menu_items, swipe=True,
                    text_post='Card with a button to open the menu MDDropDown',
                    callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    likes_stars=True, callback=callback, swipe=True,
                    text_post='Card with asterisks for voting.'))

            instance_grid_card.add_widget(
                MDCardPost(
                    source="./assets/kitten-1049129_1280.jpg",
                    tile_text="Little Baby",
                    tile_font_style="H5",
                    text_post="This is my favorite cat. He's only six months "
                              "old. He loves milk and steals sausages :) "
                              "And he likes to play in the garden.",
                    with_image=True, swipe=True, callback=callback,
                    buttons=buttons))


Example().run()
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    BoundedNumericProperty,
    ReferenceListProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    ObjectProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivymd.button import MDIconButton
from kivymd.elevation import RectangularElevationBehavior
from kivymd.list import ILeftBody
from kivymd.menus import MDDropdownMenu
from kivymd.navigationdrawer import NavigationLayout
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
#:import images_path kivymd.images_path
#:import SmartTileWithLabel kivymd.imagelists.SmartTileWithLabel


<MDCard>
    canvas:
        Color:
            rgba: self.md_bg_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [self.border_radius]
            source: root.background
        Color:
            rgba: self.theme_cls.divider_color
            a: self.border_color_a
        Line:
            rounded_rectangle:
                (self.pos[0], self.pos[1], self.size[0], self.size[1],\
                self.border_radius) 
    md_bg_color: self.theme_cls.bg_light


<MDSeparator>
    canvas:
        Color:
            rgba: self.theme_cls.divider_color
        Rectangle:
            size: self.size
            pos: self.pos


<CardPostImage>
    spacing: dp(10)
    padding: dp(5)
    orientation: 'vertical'
    size_hint: None, None
    size: root.card_size

    SmartTileWithLabel:
        source: root.source
        text: ' %s' % root.tile_text
        color: root.tile_text_color
        size_hint_y: None
        font_style: root.tile_font_style
        height: dp(200)
        on_release: root.callback(root, [self, self.source])

    MDLabel:
        text: root.text_post
        size_hint_y: None
        halign: 'justify'
        valign: 'top'
        height: dp(60)
        text_size: self.width - 20, dp(60)

    AnchorLayout:
        anchor_x: 'right'
        size_hint_y: None
        height: dp(40)

        BoxLayout:
            id: box_buttons


<MDCardPost>
    spacing: dp(5)
    padding: dp(5)
    orientation: 'vertical'
    size_hint: None, None
    size: root.card_size

    FloatLayout:

        BoxLayout:
            id: root_box
            spacing: dp(5)
            pos_hint: {'top': 1}
            orientation: 'vertical'
            x: dp(10)

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

            MDSeparator:
                id: sep
                height: dp(1)

        AnchorLayout:
            id: box_delete_post_button
            size_hint: None, None
            size: dp(90), root.height - dp(15)
            pos_hint: {'top': 1, 'right': 1}
            anchor_x: 'center'
            opacity: 0

            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            canvas.after:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: f'{images_path}swipe_shadow.png'

            MDIconButton:
                id: delet_post_button
                size_hint: None, None
                size: dp(56), dp(56)
                icon: 'delete'
                disabled: True
                on_release: root.callback(root, None)
"""
)


class MDSeparator(ThemableBehavior, BoxLayout):
    """A separator line"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_orientation()

    def on_orientation(self, *args):
        self.size_hint = (1, None) if self.orientation == "horizontal" else (None, 1)
        if self.orientation == "horizontal":
            self.height = dp(1)
        else:
            self.width = dp(1)


class MDCard(ThemableBehavior, RectangularElevationBehavior, BoxLayout):
    r = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    g = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    b = BoundedNumericProperty(1.0, min=0.0, max=1.0)
    a = BoundedNumericProperty(0.0, min=0.0, max=1.0)

    border_radius = BoundedNumericProperty(dp(3), min=0)
    border_color_a = BoundedNumericProperty(0, min=0.0, max=1.0)
    md_bg_color = ReferenceListProperty(r, g, b, a)
    background = StringProperty()


class LeftIcon(ILeftBody, Image):
    pass


class CardPostImage(BoxLayout):
    source = StringProperty()
    text_post = StringProperty()
    tile_text = StringProperty("Title")
    tile_font_style = StringProperty("H5")
    tile_text_color = ListProperty([1, 1, 1, 1])
    callback = ObjectProperty(lambda *x: None)
    card_size = ListProperty((Window.width - 10, dp(335)))


class MDCardPost(BoxLayout):
    name_data = StringProperty("Name Author\nDate and time")
    text_post = StringProperty("Your text post...")
    path_to_avatar = StringProperty("data/logo/kivy-icon-512.png")
    card_size = ListProperty((Window.width - 10, dp(180)))

    source = StringProperty()
    tile_text = StringProperty("Title")
    tile_font_style = StringProperty("H5")
    tile_text_color = ListProperty([1, 1, 1, 1])

    buttons = ListProperty()
    """A list of icons for buttons that will be used under the text of the post
    when "with_image" is True
    """

    right_menu = ListProperty()
    """If the list is not empty a button will be added to display the menu list
    """

    likes_stars = BooleanProperty(False)
    """If True, stars will be added to the card for evaluation"""

    callback = ObjectProperty(lambda *x: None)
    """User function"""

    swipe = BooleanProperty(False)
    """Whether to apply to the card the function of a swap"""

    with_image = BooleanProperty(False)
    """If True, we use a post with an image"""

    _list_instance_likes_stars = ListProperty()
    _card_shifted = False
    _shift_x = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.card_shifted = None

        # ---------------------------------------------------------------------
        if self.with_image:
            self.ids.root_box.clear_widgets()
            self._shift_x = dp(5)
            self.ids.root_box.x = self._shift_x
            self.card_size[1] = dp(335)
            card_post = CardPostImage(
                source=self.source,
                text_post=self.text_post,
                tile_text=self.tile_text,
                tile_font_style=self.tile_font_style,
                tile_text_color=self.tile_text_color,
                callback=self.callback,
            )
            for name_icon in self.buttons:
                card_post.ids.box_buttons.add_widget(
                    MDIconButton(
                        icon=name_icon,
                        on_release=lambda x, y=name_icon: self.callback(x, y),
                    )
                )
            self.ids.root_box.add_widget(card_post)
        # ---------------------------------------------------------------------
        if len(self.right_menu) and not self.with_image:
            self.ids.title_box.add_widget(
                MDIconButton(icon="dots-vertical", on_release=self.open_menu)
            )
        # ---------------------------------------------------------------------
        if self.likes_stars:
            box_likes_stars_right = AnchorLayout(
                anchor_x="right", size_hint_y=None, height=dp(30)
            )
            self.box_likes_stars = BoxLayout(spacing=(dp(5)))
            self.box_likes_stars.add_widget(Widget())
            for i in range(5):  # adding stars
                like_star = MDIconButton(
                    icon="star-outline",
                    size_hint=(None, None),
                    size=(dp(30), dp(30)),
                    id=str(i),
                    on_release=lambda x, y=i: self._update_likes_stars(y),
                )
                self.box_likes_stars.add_widget(like_star)
                self._list_instance_likes_stars.append(like_star)
            box_likes_stars_right.add_widget(self.box_likes_stars)
            self.ids.root_box.remove_widget(self.ids.sep)
            self.add_widget(box_likes_stars_right)

    def open_menu(self, instance):
        MDDropdownMenu(items=self.right_menu, width_mult=3).open(instance)

    def _update_likes_stars(self, index_star):
        i = 0
        for instance_like_star in self._list_instance_likes_stars:
            if int(instance_like_star.id) <= index_star:
                if instance_like_star.icon == "star-outline":
                    instance_like_star.icon = "star"
                    i = 1
                else:
                    if int(instance_like_star.id) == index_star:
                        instance_like_star.icon = "star-outline"
            elif int(instance_like_star.id) >= index_star:
                if instance_like_star.icon == "star":
                    instance_like_star.icon = "star-outline"
        self.callback(self, index_star + i)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos) and self.swipe and not self._card_shifted:
            if touch.x < Window.width - 10:
                # When the Navigation panel is open and
                # the list of its menu is scrolled,
                # the event is also processed on the cards
                for widget in Window.children:
                    if widget.__class__ is NavigationLayout:
                        if widget.state == "open":
                            return
                self.shift_post_left()
        return super().on_touch_move(touch)

    def on_touch_down(self, touch):
        if self.swipe and self.card_shifted:
            Clock.schedule_once(self.shift_post_right, 0.1)
        return super().on_touch_down(touch)

    def shift_post_left(self):
        def on_anim_complete(*args):
            self._card_shifted = True
            self.card_shifted = self
            self.ids.delet_post_button.disabled = False

        Animation(x=-dp(90), d=0.1, t="in_out_cubic").start(self.ids.root_box)
        if self.likes_stars:
            Animation(x=-dp(90), d=0.1, t="in_out_cubic").start(self.children[0])
        anim = Animation(opacity=1, d=0.5, t="in_out_cubic")
        anim.bind(on_complete=on_anim_complete)
        anim.start(self.ids.box_delete_post_button)

    def shift_post_right(self, interval=0.1):
        def on_anim_complete(*args):
            self._card_shifted = False
            self.card_shifted = None
            self.ids.delet_post_button.disabled = True

        Animation(x=self._shift_x, d=0.1, t="in_out_cubic").start(self.ids.root_box)
        if self.likes_stars:
            Animation(x=self._shift_x, d=0.3, t="in_out_cubic").start(self.children[0])
        anim = Animation(opacity=0, d=0.05, t="in_out_cubic")
        anim.bind(on_complete=on_anim_complete)
        anim.start(self.ids.box_delete_post_button)
