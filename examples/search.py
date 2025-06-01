from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.recycleboxlayout import MDRecycleBoxLayout
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.screen import MDScreen
from kivymd.uix.search import (
    MDSearchBar,
    MDSearchBarLeadingContainer,
    MDSearchBarTrailingContainer,
    MDSearchLeadingIcon,
    MDSearchTextInput,
    MDSearchTrailingAvatar,
    MDSearchTrailingIcon,
    MDSearchView,
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
            MDSearchView(
                rv := MDRecycleView(
                    MDRecycleBoxLayout(
                        padding=(dp(10), dp(10), 0, dp(10)),
                        default_size=(None, dp(48)),
                        default_size_hint=(1, None),
                        size_hint_y=None,
                        adaptive_height=True,
                        orientation="vertical",
                    ),
                    id="rv",
                )
            ),
            view_root=self.layout,
        )
        self.layout.add_widget(self.search, index=2)
        self.layout.add_widget(Widget())
        self.layout.add_widget(
            MDLabel(
                text="This should be replaced", height=dp(30), size_hint_y=None
            )
        )
        self.root_layout = MDBoxLayout(
            self.layout,
            MDLabel(text="But this not", height=dp(30), size_hint_y=None),
            orientation="vertical",
        )
        self.screen = MDScreen(
            self.root_layout, md_bg_color=self.theme_cls.backgroundColor
        )

        rv.key_viewclass = "viewclass"
        rv.key_size = "height"
        rv.data = [{"viewclass": "Button", "text": f"{i}"} for i in range(30)]

        return self.screen


MainApp().run()
