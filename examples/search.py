from kivy.metrics import dp
from kivy.uix.widget import Widget

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.search import (
    MDSearchBar,
    MDSearchBarLeadingContainer,
    MDSearchBarTrailingContainer,
    MDSearchLeadingIcon,
    MDSearchTextInput,
    MDSearchTrailingAvatar,
    MDSearchTrailingIcon,
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.root_layout = None
        self.search = None
        self.screen = None
        self.layout = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.layout = MDBoxLayout(orientation="vertical")
        self.search = MDSearchBar(
            MDSearchBarLeadingContainer(
                MDSearchLeadingIcon(icon="numeric-1-box"),
            ),
            MDSearchTextInput(),
            MDSearchBarTrailingContainer(
                MDSearchTrailingIcon(icon="numeric-2-box"),
                MDSearchTrailingAvatar(
                    source=f"{images_path}/logo/kivymd-icon-128.png"
                ),
            ),
            view_root=self.layout,
        )
        self.layout.add_widget(self.search)
        self.layout.add_widget(Widget())
        self.root_layout = MDBoxLayout(
            self.layout,
            MDLabel(text="Do not replace", height=dp(30), size_hint_y=None),
            orientation="vertical",
        )
        self.screen = MDScreen(
            self.root_layout, md_bg_color=self.theme_cls.backgroundColor
        )

        return self.screen


MainApp().run()
