"""
Components/Search
==========================
.. versionadded:: 2.0.0

.. seealso::

    `Material Design spec, Search <https://m3.material.io/components/search/overview>`_

.. rubric:: Search lets people enter a keyword or phrase to get relevant information


.. image:: TODO: LINK SEARCH PREVIEW
    :align: center

- Use search bars and views for navigating a product through search queries
- Search bars can display suggested keywords or phrases as the user types
- Always display results in a search view

Anatomy
-------

.. image:: TODO: SEARCH BAR
    :align: center

.. image:: TODO: SEARCH VIEW
    :align: center

The search view grows out of the search bar showing its contents, it will try to fully fill the area taken by the view root

Examples
-------

Full (not docked)
^^^^^^^

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDSegmentedButton:

                MDSegmentedButtonItem:

                    MDSegmentButtonIcon:
                        icon: "language-python"

                MDSegmentedButtonItem:

                    MDSegmentButtonIcon:
                        icon: "language-javascript"

                MDSegmentedButtonItem:

                    MDSegmentButtonIcon:
                        icon: "language-swift"

    .. tab:: Pure Python

        .. code-block:: python

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
                        view_root=self.search_view_root,
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
.. image:: TODO: Add gif full bar opening and closing
    :align: center
"""

from collections.abc import Callable

from kivy.animation import Animation
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
from kivy.uix.image import Image
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.behaviors.addition_complete_behaviour import AdditionComplete
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDIcon
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.utils.wrong_child import WrongChildException


class MDSearchTrailingAvatar(ButtonBehavior, Image):
    """
    Avatar shown after the icon in the search bar while it's not focused
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(30), dp(30))


class MDSearchLeadingIcon(RectangularRippleBehavior, ButtonBehavior, MDIcon):
    """
    Icon in front of the search bar.
    """

    width = NumericProperty(dp(24))
    icon_color = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_icon_color()  # There should be a more elegant way to do this but IDK?
        self.size_hint = (None, None)
        self.size = (dp(24), dp(24))

    def update_icon_color(self):
        # Access the app's theme and set the color
        app = MDApp.get_running_app()
        if app and hasattr(app, "theme_cls"):
            self.icon_color = app.theme_cls.onSurfaceColor


class MDSearchTrailingIcon(RectangularRippleBehavior, ButtonBehavior, MDIcon):
    """
    Icon after the search bar
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_icon_color()
        self.size_hint = (None, None)
        self.size = (dp(24), dp(24))

    def update_icon_color(self):
        # Access the app's theme and set the color
        app = MDApp.get_running_app()
        if app and hasattr(app, "theme_cls"):
            self.icon_color = app.theme_cls.onSurfaceColor


class _BarContainer(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        self.support_layouts: dict[Widget, MDBoxLayout] = {}

        super().__init__(*args, **kwargs)
        self.size_hint_x = None
        self.size_hint_y = 1
        self.padding = [dp(16), 0, dp(16), 0]
        self.spacing = dp(16)

    def add_widget(self, widget, *args, **kwargs):
        """
        Support layouts need to be added since, to facilitate ripple animations of the icons
        """
        self.support_layouts[widget] = MDAnchorLayout(
            widget,
            size_hint=(None, 1),
            anchor_x="left",
            anchor_y="center",
            width=widget.width,
        )
        super().add_widget(self.support_layouts[widget])


class MDSearchBarTrailingContainer(_BarContainer):
    """
    Container placed after the search bar
    """

    ...


class MDSearchBarLeadingContainer(_BarContainer):
    """
    Container placed before the search bar
    """

    ...


class MDSearchViewTrailingContainer(_BarContainer):
    """
    Container shown behind the search bar after search view expansion is triggered
    """

    ...


class MDSearchViewLeadingContainer(_BarContainer):
    """
    Container shown in front of the search bar after search view expansion is triggered
    """

    ...


class MDSearchView(MDBoxLayout):
    """
    Housing for search Results, add them here
    """

    def __init__(self, *args, **kwargs):
        app = MDApp.get_running_app()
        super().__init__(*args, **kwargs)
        self.size_hint = [0, 0]
        with self.canvas.before:
            Color(*app.theme_cls.surfaceContainerHighColor)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        def update_rect(instance, value):
            instance.rect.pos = self.pos
            instance.rect.size = self.size

        # listen to size and position changes
        self.bind(pos=update_rect, size=update_rect)


class MDSearchViewDivider(MDDivider, AdditionComplete):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_fully_added(self, parent_widget):
        assert isinstance(parent_widget, MDSearchView)
        self.orientation = parent_widget.orientation
        if parent_widget.orientation == "vertical":
            self.size_hint_x = 1
            self.size_hint_y = None
            self.height = dp(1)

        if parent_widget.orientation == "horizontal":
            self.size_hint_x = None
            self.size_hint_y = 1
            self.width = dp(1)


class MDSearchTextInput(TextInput):
    """
    Text input for the search bar
    :attr:`~.self.text` is the searched text
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = MDApp.get_running_app()
        self.background_color = (0, 0, 0, 0)
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
            focus=lambda _, state: self.parent.switch_state(state),
        )
        # Set initial padding
        self._update_padding()

    def _update_padding(self, *args):
        self.padding = [0, (self.height - self.line_height) / 2]


def __deffer_target(
    item: Animation,
    animations: list[Animation],
    callback: Callable,
    previous: Callable,
    widget: Widget,
):
    previous(widget)
    try:
        animations.remove(item)
    except ValueError:
        pass
    if not animations:
        callback()


def _deffer(animations: list[Animation], callback: Callable):
    """
    Executes a `~callback` after all animations have finished playing
    :param animations: List of animations
    :param callback: Callback to execute
    :return:
    """
    for animation in animations:
        previous = animation.on_complete
        animation.on_complete = lambda widget: __deffer_target(
            animation, animations, callback, previous, widget
        )


def _fade_icons(old: Widget, new: MDBoxLayout):
    """
    Generic animation to fade the old widget and show the new
    :param old: Shown item
    :param new: Item to be shown
    :return: None
    """
    fade_in = Animation(opacity=1, t="in_out_circ", d=0.2)
    fade_out = Animation(opacity=0, t="in_out_circ", d=0.2)
    width = Animation(width=new.minimum_width, t="in_out_circ", d=0.4)

    fade_out.start(old)
    width.start(new.parent)
    fade_out.on_complete = lambda *_: fade_in.start(new)


def _rotated_expand_animation(
    widget: Widget,
    view_root: Widget,
    target_height: float,
    target_width: float,
    search_bar: "MDSearchBar",
) -> Animation:
    """
    Generic animation for expanding/closing a widget in a RelativeLayout
    :param widget: Widget to be expanded
    :param view_root: Container to contain the expansion
    :param target_height: Target height
    :param target_width: Target width
    :return:
    """
    animation = Animation(
        height=target_height, width=target_width, t="in_out_circ", d=0.4
    )

    start_h = widget.height

    animation.on_progress = lambda instance, _: (
        setattr(
            instance,
            "y",
            view_root.y
            + (target_height if target_height != 0 else start_h)
            - instance.height,
        ),
        setattr(instance, "center_x", search_bar.center_x - view_root.x),
    )
    return animation


class MDSearchBar(RectangularRippleBehavior, MDBoxLayout, AdditionComplete):
    """
    Material Design search widget
    """

    leading_icon = StringProperty("magnify")
    supporting_text = StringProperty("Hinted search text")
    view_root: Widget = ObjectProperty(
        None
    )  # What will be replaced when docked = False
    docked_height = NumericProperty(dp(240))
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
        self._search_view_support_layout = MDRelativeLayout(
            size_hint=[None, None], width=0, height=0
        )
        super().__init__(*args, **kwargs)
        self.open = False
        self.radius = dp(28)

        self._lock = False

        self._swap_container_leading: MDFloatLayout = MDRelativeLayout(
            size_hint=[None, 1]
        )
        self._swap_container_trailing: MDFloatLayout = MDRelativeLayout(
            size_hint=[None, 1]
        )

    def on_fully_added(self, parent):
        self._assert_state()
        self._define_layout()

    def add_widget(self, widget, *args, **kwargs):
        if widget.__class__.__name__ == "MDSearchView":
            self._search_view_support_layout.add_widget(widget)
            self.search_view = widget
        elif self._view_map.get(widget.__class__.__name__):
            setattr(self, self._view_map[widget.__class__.__name__], widget)
        else:
            raise WrongChildException(self, widget, list(self._view_map.keys()))

    def _define_layout(self):
        """
        Create layout
        """
        app = MDApp.get_running_app()

        # Add widgets in order, might want to change this to a list later
        super().add_widget(self._swap_container_leading)
        if self.search_bar_leading_container:
            self._swap_container_leading.add_widget(
                self.search_bar_leading_container
            )
        if self.search_view_leading_container:
            self._swap_container_leading.add_widget(
                self.search_view_leading_container
            )
        super().add_widget(self.text_input)
        super().add_widget(self._swap_container_trailing)
        if self.search_bar_trailing_container:
            self._swap_container_trailing.add_widget(
                self.search_bar_trailing_container
            )
        if self.search_view_trailing_container:
            self._swap_container_trailing.add_widget(
                self.search_view_trailing_container
            )

        self._swap_container_leading.width = (
            self.search_bar_leading_container.width
        )
        self._swap_container_trailing.width = (
            self.search_bar_trailing_container.width
        )

        self.height = dp(56)
        self.size_hint_y = None
        self.md_bg_color = (
            app.theme_cls.surfaceContainerHighColor
        )  # pyright: ignore [reportOptionalMemberAccess]
        self.radius = dp(28)
        self.view_root.parent.add_widget(self._search_view_support_layout)

        self.search_view_leading_container.opacity = 0
        self.search_view_trailing_container.opacity = 0

    def update_open(self, *args):
        self.search_view.pos = self._search_view_support_layout.to_local(
            self.view_root.x, self.view_root.y
        )

        self.search_view.width = self.view_root.width
        self.search_view.height = self.view_root.height - self.height

    def state_open_common(self):
        """
        Animate the opening of the search view.
        """
        self._lock = True
        self.open = True

        self.search_view.size_hint = [None, None]

        self.bind(pos=self.update_open, size=self.update_open)
        self.search_view.pos = self.view_root.x, self.view_root.y
        self.search_view.height = dp(0)

        animations: list[Animation] = [
            _rotated_expand_animation(
                self.search_view,
                self.view_root,
                (self.view_root.height - self.view_root.y) - self.height,
                self.width,
                self,
            )
        ]

        for animation in animations:
            animation.start(self.search_view)

        _deffer(animations, lambda: setattr(self, "_lock", False))
        _deffer(
            animations,
            lambda: self.text_input.setter("focus")(self.text_input, True),
        )

        # Icons
        _fade_icons(
            self.search_bar_leading_container,
            self.search_view_leading_container,
        )
        _fade_icons(
            self.search_bar_trailing_container,
            self.search_view_trailing_container,
        )
        if self.docked:
            self.open_docked()
        else:
            self.open_undocked()

    def open_docked(self):
        search_bar_open = Animation(
            radius=[dp(28), dp(28), dp(0), dp(0)],
            t="in_out_circ",
            d=0.2,
        )
        search_bar_open.start(self)

    def open_undocked(self):
        search_bar_open = Animation(
            radius=[dp(0)] * 4,
            t="in_out_circ",
            d=0.2,
        )
        search_bar_open.start(self)

    def state_closed_common(self):
        self._lock = True
        self.open = False

        self.unbind(pos=self.update_open, size=self.update_open)

        search_bar_close = Animation(
            radius=[dp(28)] * 4, t="in_out_circ", d=0.4
        )
        search_bar_close.start(self)

        animations: list[Animation] = [
            _rotated_expand_animation(
                self.search_view, self.view_root, 0, 0, self
            )
        ]
        for animation in animations:
            animation.start(self.search_view)

        _deffer(animations, lambda: setattr(self, "_lock", False))
        _deffer(animations, self.enable_ripple)
        _deffer(
            animations,
            lambda: self.text_input.setter("focus")(self.text_input, False),
        )

        # Icons
        _fade_icons(
            self.search_view_leading_container,
            self.search_bar_leading_container,
        )
        _fade_icons(
            self.search_view_trailing_container,
            self.search_bar_trailing_container,
        )

    def _assert_state(self):
        """
        Check if widget is set up correctly
        """
        assert isinstance(self.view_root, Widget)
        assert self in self.view_root.children

    def switch_state(self, opened):
        """
        Checks if a lock is in force, if not switches the state of the search bar
        """
        self.disable_ripple()
        if self._lock:
            return
        if opened:
            self.state_open_common()
        else:
            self.state_closed_common()

    def disable_ripple(self):
        self.lay_canvas_instructions = lambda *args: None

    def enable_ripple(self):
        self.lay_canvas_instructions = super().lay_canvas_instructions
