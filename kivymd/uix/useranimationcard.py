"""
Components/User Animation Card
==============================

Example
-------

.. code-block:: python

    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivy.factory import Factory

    from kivymd.toast import toast
    from kivymd.theming import ThemeManager
    from kivymd.uix.useranimationcard import MDUserAnimationCard
    from kivymd.uix.button import MDIconButton
    from kivymd.uix.list import ILeftBodyTouch

    # Your content for a contact card.
    Builder.load_string('''
    #:import get_hex_from_color kivy.utils.get_hex_from_color


    <TestAnimationCard@MDBoxLayout>
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        adaptive_height: True

        MDBoxLayout:
            adaptive_height: True

            Widget:
            MDRoundFlatButton:
                text: "Free call"
            Widget:
            MDRoundFlatButton:
                text: "Free message"
            Widget:

        OneLineIconListItem:
            text: "Video call"
            IconLeftSampleWidget:
                icon: 'camera-front-variant'

        TwoLineIconListItem:
            text: "Call Viber Out"
            secondary_text: "[color=%s]Advantageous rates for calls[/color]" % get_hex_from_color(app.theme_cls.primary_color)
            IconLeftSampleWidget:
                icon: 'phone'

        TwoLineIconListItem:
            text: "Call over mobile network"
            secondary_text: "[color=%s]Operator's tariffs apply[/color]" % get_hex_from_color(app.theme_cls.primary_color)
            IconLeftSampleWidget:
                icon: 'remote'
    ''')


    class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
        pass


    class Example(MDApp):
        title = "Example Animation Card"

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.user_animation_card = None

        def build(self):
            def main_back_callback():
                toast('Close card')

            if not self.user_animation_card:
                self.user_animation_card = MDUserAnimationCard(
                    user_name="Lion Lion",
                    path_to_avatar="./assets/african-lion-951778_1280.jpg",
                    callback=main_back_callback)
                self.user_animation_card.box_content.add_widget(
                    Factory.TestAnimationCard())
            self.user_animation_card.open()


    Example().run()
"""


from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import SpecificBackgroundColorBehavior
from kivymd.uix.button import MDIconButton

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import StiffScrollEffect kivymd.stiffscroll.StiffScrollEffect


<ModifiedToolbar>
    size_hint_y: None
    height: root.theme_cls.standard_increment
    padding: [root.theme_cls.horizontal_margins - dp(12), 0]

    BoxLayout:
        id: left_actions
        orientation: 'horizontal'
        size_hint_x: None
        padding: [0, (self.height - dp(48))/2]

    BoxLayout:
        padding: dp(12), 0

        MDLabel:
            font_style: 'H6'
            opposite_colors: root.opposite_colors
            theme_text_color: 'Custom'
            text_color: root.specific_text_color
            text: root.title
            shorten: True
            shorten_from: 'right'

    BoxLayout:
        id: right_actions
        orientation: 'horizontal'
        size_hint_x: None
        padding: [0, (self.height - dp(48))/2]


<UserAnimationCard>
    canvas:
        Color:
            rgba:
                root.theme_cls.bg_dark \
                if root.theme_cls.theme_style == 'Dark' \
                else root.theme_cls.bg_light
        Rectangle:
            size: self.size
            pos: self.pos

    FitImage:
        id: image
        source: root.path_to_avatar
        size_hint: 1, None
        height: Window.height * 40 // 100
        y: Window.height - self.height
        allow_stretch: True
        keep_ratio: False

        canvas.after:
            Color:
                rgba: root._primary_color
            Rectangle:
                size: self.size
                pos: self.pos

    MDLabel:
        id: user_name
        font_style: 'H4'
        theme_text_color: 'Custom'
        color: 1, 1, 1, 1
        shorten: True
        shorten_from: 'right'
        text: root.user_name
        size_hint_y: None
        height: self.texture_size[1]

    ModifiedToolbar:
        id: toolbar
        md_bg_color: 0, 0, 0, 0
        left_action_items: [['arrow-left', lambda x: root._callback_back()]]
        y: Window.height - self.height

    ScrollView:
        id: scroll
        y: -image.height
        effect_cls: StiffScrollEffect
        scroll_distance: 100

        canvas.before:
            Color:
                rgba:
                    root.theme_cls.bg_dark
            Rectangle:
                size: self.size
                pos: self.pos

        MDGridLayout:
            id: box_content
            adaptive_height: True
            cols: 1

            canvas:
                Color:
                    rgba:
                        root.theme_cls.bg_dark
                Rectangle:
                    size: self.size
                    pos: self.pos
"""
)


class MDUserAnimationCard(ThemableBehavior, ModalView):
    user_name = StringProperty()
    path_to_avatar = StringProperty()
    box_content = ObjectProperty()
    callback = ObjectProperty()
    _anim_bottom = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._primary_color = self.theme_cls.primary_color
        self._primary_color[3] = 0
        self.user_animation_card = UserAnimationCard(
            user_name=self.user_name,
            path_to_avatar=self.path_to_avatar,
            _callback_back=self._callback_back,
            _primary_color=self._primary_color,
        )
        self.user_animation_card.ids.user_name.pos = (
            dp(15),
            Window.height - self.user_animation_card.ids.image.height,
        )
        self.box_content = self.user_animation_card.ids.box_content
        self.add_widget(self.user_animation_card)

        self._obj_avatar = self.user_animation_card.ids.image
        self._obj_user_name = self.user_animation_card.ids.user_name
        self._obj_toolbar = self.user_animation_card.ids.toolbar
        self._obj_scroll = self.user_animation_card.ids.scroll
        self._set_current_pos_objects()

    def _callback_back(self):
        self.dismiss()
        if self.callback:
            self.callback()

    def on_open(self):
        self._primary_color = self.theme_cls.primary_color
        self._primary_color[3] = 0
        self.user_animation_card._primary_color = self._primary_color

    def _set_current_pos_objects(self):
        self._avatar_y = self._obj_avatar.y
        self._toolbar_y = self._obj_toolbar.y
        self._user_name_y = self._obj_user_name.y
        self._scroll_y = self._obj_scroll.y

    def on_touch_move(self, touch):
        if touch.ud["swipe_begin"] < touch.y:
            if self._anim_bottom:
                self._anim_bottom = False
                self.animation_to_top()
        else:
            if not self._anim_bottom:
                self._anim_bottom = True
                self.animation_to_bottom()

    def on_touch_down(self, touch):
        touch.ud["swipe_begin"] = touch.y
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        touch.ud["swipe_begin"] = 0

    def animation_to_bottom(self):
        Animation(y=self._scroll_y, d=0.4, t="in_out_cubic").start(
            self._obj_scroll
        )
        Animation(y=self._user_name_y, d=0.5, x=dp(15), t="in_out_cubic").start(
            self._obj_user_name
        )
        Animation(font_size=sp(36), d=0.3, t="in_out_cubic").start(
            self._obj_user_name
        )
        Animation(_primary_color=[0, 0, 0, 0], d=0.3, t="in_out_cubic").start(
            self.user_animation_card
        )
        Animation(y=self._avatar_y, d=0.4, t="in_out_cubic").start(
            self._obj_avatar
        )

    def animation_to_top(self):
        user_name_y = (
            Window.height
            - self._obj_toolbar.height
            + (self.theme_cls.standard_increment // 2 - dp(12))
        )
        user_name_x = self.theme_cls.horizontal_margins + dp(12) * 5

        Animation(y=-self._obj_toolbar.height, d=0.4, t="in_out_cubic").start(
            self._obj_scroll
        )
        Animation(y=user_name_y, d=0.3, x=user_name_x, t="in_out_cubic").start(
            self._obj_user_name
        )
        Animation(font_size=sp(20), d=0.3, t="in_out_cubic").start(
            self._obj_user_name
        )
        Animation(
            _primary_color=self.theme_cls.primary_color, d=0.3, t="in_out_cubic"
        ).start(self.user_animation_card)
        Animation(y=self._obj_avatar.y + 30, d=0.4, t="in_out_cubic").start(
            self._obj_avatar
        )


class UserAnimationCard(ThemableBehavior, FloatLayout):
    user_name = StringProperty()
    path_to_avatar = StringProperty()
    _callback_back = ObjectProperty()
    _primary_color = ListProperty()


class ModifiedToolbar(
    ThemableBehavior, SpecificBackgroundColorBehavior, BoxLayout
):
    left_action_items = ListProperty()
    title = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            action_bar.add_widget(
                MDIconButton(
                    icon=item[0],
                    on_release=item[1],
                    opposite_colors=True,
                    text_color=self.specific_text_color,
                    theme_text_color="Custom",
                )
            )
        action_bar.width = new_width

    def update_action_bar_text_colors(self, instance, value):
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
