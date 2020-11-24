"""
    This module had taken in
        https://github.com/kivymd-extensions/akivymd
"""


from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemableBehavior


class NavigationItem(ThemableBehavior, ButtonBehavior, BoxLayout):
    duration = NumericProperty(0.3)
    button_width = NumericProperty(dp(120))
    button_height = NumericProperty(dp(40))
    text = StringProperty()
    icon = StringProperty()
    icon_color = ColorProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_release(self):
        for button in self.parent.children:
            if button == self:
                continue
            button._button_shrink()

        self._button_expand()
        return super().on_release()

    def _button_expand(self):
        label_anim = Animation(
            opacity=1, transition="in_sine", duration=self.duration
        )
        label_anim.start(self.ids._label)

        anim = Animation(
            width=self.button_width,
            t="linear",
            duration=self.duration,
            icon_color=self.theme_cls.text_color,
        )
        anim.start(self)

    def _button_shrink(self):

        label_anim = Animation(
            opacity=0, transition="out_sine", duration=self.duration
        )
        label_anim.start(self.ids._label)

        but_anim = Animation(
            width=self.height,
            t="linear",
            duration=self.duration,
            icon_color=self.theme_cls.disabled_hint_text_color,
        )
        but_anim.start(self)


class NavigationBar(ThemableBehavior, BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self._update)
        Clock.schedule_once(lambda x: self.set_current(None))
        Clock.schedule_once(lambda x: self._update())

    def _update(self, *args):
        self.width = Window.width
        buttons = self.ids._button_box.children
        button_sizes = (
            (len(buttons) - 1) * buttons[0].button_height
        ) + buttons[0].button_width
        space = self.width - button_sizes
        spacing = space / (len(buttons) + 1)
        self.ids._button_box.spacing = spacing
        self.ids._button_box.padding = [spacing, 0, spacing, 0]

    def set_current(self, index):
        if not index:
            index = -1
        button = self.ids._button_box.children[index]
        button.dispatch("on_release")

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, NavigationItem):
            return self.ids._button_box.add_widget(widget)
        else:
            return super().add_widget(widget, index=(index), canvas=canvas)
