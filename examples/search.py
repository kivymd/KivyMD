from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemSupportingText,
)
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
    MDSearchViewLeadingContainer,
    MDSearchViewTrailingContainer,
)


class Item(MDListItem):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headline_text_widget = MDListItemHeadlineText(
            text=self.text,
        )
        self.support_text_widget = MDListItemSupportingText(
            text=self.text,
        )
        self.add_widget(self.headline_text_widget)
        self.add_widget(self.support_text_widget)

    def on_text(self, instance, value):
        self.headline_text_widget.text = value
        self.support_text_widget.text = value


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.root_layout = None
        self.search = None
        self.screen = None
        self.search_view_root = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.search_view_root = MDBoxLayout(orientation="vertical")
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
            MDSearchViewLeadingContainer(
                MDSearchLeadingIcon(icon="arrow-left"),
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
                )
            ),
            MDSearchViewTrailingContainer(
                MDSearchLeadingIcon(icon="numeric-4-box")
            ),
            view_root=self.search_view_root,
            docked=True,
            size_hint_x=None,
            width=dp(300),
        )
        self.search_view_root.add_widget(self.search)
        self.search_view_root.add_widget(Widget())
        self.root_layout = MDBoxLayout(
            MDBoxLayout(
                self.search_view_root,
                orientation="vertical",
            ),
            orientation="horizontal",
        )
        self.screen = MDScreen(
            self.root_layout, md_bg_color=self.theme_cls.backgroundColor
        )

        rv.key_viewclass = "viewclass"
        rv.data = [{"viewclass": "Item", "text": f"{i}"} for i in range(30)]
        return self.screen


MainApp().run()
