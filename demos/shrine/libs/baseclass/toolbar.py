from os import environ

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class ShrineToolbar(ThemableBehavior, MDBoxLayout):
    """`Toolbar` for `ShrineRootScreen` screen."""

    bottom_manu_open = False
    """Open or closed box."""

    search = False
    path_to_icon_menu = StringProperty(
        f"{environ['SHRINE_ROOT']}/assets/images/menu-dark.png"
    )
    path_to_icon_logo = StringProperty()
    title = StringProperty("SHRINE")

    def set_title_animation_text(self, text):
        """Animates text from `Title old` to `Title new`."""

        def set_new_text(*args):
            self.ids.title.text = text
            Animation(color=self.theme_cls.text_color, d=0.2).start(
                self.ids.title
            )

        anim = Animation(color=(0, 0, 0, 0), d=0.2)
        anim.bind(on_complete=set_new_text)
        anim.start(self.ids.title)

    def set_search_field(self):
        def set_focus_search_field(interval):
            self.ids.search_field.focus = focus

        if not self.search:
            self.search = True
            size = 0
            opacity = 1
            opacity_button_tune = 0
            disabled = False
            focus = True
            title = "SEARCH"
        else:
            self.search = False
            size = dp(42)
            opacity = 0
            opacity_button_tune = 1
            disabled = True
            focus = False
            title = self.title

        Animation(size=(size, size), opacity=opacity_button_tune, d=0.2).start(
            self.ids.button_tune
        )
        Animation(size=(size, size), d=0.2).start(self.ids.button_logo)
        Animation(size=(size, size), d=0.2).start(self.ids.button_menu)
        self.set_title_animation_text(title)
        self.ids.search_field.disabled = disabled
        Animation(opacity=opacity, d=0.2).start(self.ids.search_field)
        Clock.schedule_once(set_focus_search_field, 0.3)
