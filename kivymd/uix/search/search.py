from kivy.clock import Clock
from kivy.core.image import Texture
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from win32comext.adsi.demos.search import search

from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors.addition_complete_behaviour import AdditionComplete
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.utils.wrong_child import WrongChildException


class MDSearchTrailingAvatar(ButtonBehavior, Image):
    """
    Avatar shown after the icon in the search bar while it's not focused
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = dp(30)


class MDSearchLeadingIcon(ButtonBehavior, MDIcon):
    """
    Icon in front of the search bar.
    """

    width = NumericProperty(dp(24))
    icon_color = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_icon_color()  # There should be a more elegant way to do this but IDK?
        self.size_hint_x = None
        self.size_hint_y = 1

    def update_icon_color(self):
        # Access the app's theme and set the color
        app = MDApp.get_running_app()
        if app and hasattr(app, "theme_cls"):
            self.icon_color = app.theme_cls.onSurfaceColor


class MDSearchTrailingIcon(ButtonBehavior, MDIcon):
    """
    Icon after the search bar
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_icon_color()
        self.size_hint_x = None
        self.size_hint_y = 1
        self.width = dp(24)

    def update_icon_color(self):
        # Access the app's theme and set the color
        app = MDApp.get_running_app()
        if app and hasattr(app, "theme_cls"):
            self.icon_color = app.theme_cls.onSurfaceColor


class MDSearchBarTrailingContainer(MDBoxLayout):
    """
    Container placed after the search bar
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_x = None
        self.size_hint_y = 1
        self.padding = [dp(16), 0, dp(16), 0]
        self.spacing = dp(16)
        self.bind(minimum_width=self.setter("width"))


class MDSearchBarLeadingContainer(MDBoxLayout):
    """
    Container placed before the search bar
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_x = None
        self.minimum_width = 0
        self.size_hint_y = 1
        self.padding = [dp(16), 0, dp(16), 0]

        self.width = dp(16) * 2 + dp(24)


class MDSearchViewTrailingContainer(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_x = None
        self.spacing = dp(16)


class MDSearchViewLeadingContainer(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_x = None
        self.width = dp(30)
        self.spacing = dp(16)


class MDSearchView(MDBoxLayout):
    """
    Housing for search Results, add them here
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint = [0, 0]
        self.md_bg_color = (0, 1, 0, 1)
        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        # listen to size and position changes
        self.bind(pos=update_rect, size=update_rect)


class MDSearchTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        self.background_color = app.theme_cls.surfaceContainerHighColor
        self.foreground_color = app.theme_cls.onSurfaceColor
        self.cursor_color = app.theme_cls.primaryColor
        self.hint_text_color = app.theme_cls.onSurfaceVariantColor
        self.background_active = ""
        self.background_normal = ""
        self.size_hint_x = 1
        self.multiline = False
        self.font_size = app.theme_cls.font_styles["Body"]["large"]["font-size"]
        self.font_name = app.theme_cls.font_styles["Body"]["large"]["font-name"]
        self.line_height = app.theme_cls.font_styles["Body"]["large"][
            "line-height"
        ]

        self.bind(size=self._update_padding, text=self._update_padding)
        self.bind(
            focus=lambda _, state: self.parent.state_open()
            if state
            else self.parent.state_closed()
        )
        # Set initial padding
        self._update_padding()

    def _update_padding(self, *args):
        self.padding = [0, (self.height - self.line_height) / 2]


def print_widget_tree(widget, indent=0):
    """Prints the widget tree structure."""
    prefix = "    " * indent
    print(f"{prefix}└── {widget.__class__.__name__} ")
    for child in widget.children:
        print_widget_tree(child, indent + 1)


class MDSearchBar(MDBoxLayout, AdditionComplete):
    """
    Material Design search widget
    @property @required view_root
    """

    leading_icon = StringProperty("magnify")
    supporting_text = StringProperty("Hinted search text")
    view_root: Widget = ObjectProperty(
        None
    )  # What will be replaced when docked = False
    docked_width = NumericProperty(dp(360))
    docked_height = NumericProperty(dp(240))
    view_z_index = NumericProperty(100)
    docked = BooleanProperty(False)

    _view_map = {
        "MDSearchBarLeadingContainer": "search_bar_leading_container",
        "MDSearchBarTrailingContainer": "search_bar_trailing_container",
        "MDSearchViewLeadingContainer": "search_view_leading_container",
        "MDSearchViewTrailingContainer": "search_view_trailing_container",
        "MDSearchTextInput": "text_input",
        "MDSearchView": "search_view",
    }

    search_bar_leading_container: MDSearchBarLeadingContainer
    search_bar_trailing_container: MDSearchBarTrailingContainer
    search_view_leading_container: MDSearchViewLeadingContainer
    search_view_trailing_container: MDSearchViewTrailingContainer
    search_view: MDSearchView
    text_input: TextInput

    def __init__(self, *args, **kwargs):
        self._search_view_support_layout = FloatLayout(
            size_hint=[None, None], width=0, height=0
        )

        super().__init__(*args, **kwargs)
        self.open = False
        self.internal_add = self.add_widget
        self.radius = dp(28)

    def on_fully_added(self, parent):
        self._assert_state()
        self._define_layout()

    def add_widget(self, widget, *args, **kwargs):
        if widget.__class__.__name__ == "MDSearchView":
            self._search_view_support_layout.add_widget(widget, index=2)
            self.search_view = widget
        elif self._view_map.get(widget.__class__.__name__):
            setattr(self, self._view_map[widget.__class__.__name__], widget)
            super().add_widget(widget, index=2)
        else:
            raise WrongChildException(self, widget, list(self._view_map.keys()))

    def _define_layout(self):
        """
        Create layout
        """
        app = MDApp.get_running_app()

        self.height = dp(56)
        self.size_hint_y = None
        self.md_bg_color = app.theme_cls.surfaceContainerHighColor
        self.view_root.parent.add_widget(self._search_view_support_layout)

        self.state_closed()

    def state_closed(self):
        self.open = False

        self.radius = dp(28)

    def state_open(self):
        self.open = True

        self.radius = dp(0)
        # Zero the position of the search view
        self.search_view.pos = self._search_view_support_layout.to_local(
            self.view_root.x, self.view_root.y
        )

        # Set a size as large as the size of the view_root (account for the height of the bar itself):
        self.search_view.size_hint = [None, None]
        self.search_view.width = self.view_root.width
        self.search_view.height = self.view_root.height - self.height
        print_widget_tree(self.get_root_window())

    def _assert_state(self):
        """
        Check if widget is set up correctly
        """
        assert isinstance(self.view_root, Widget)
        assert self in self.view_root.children
