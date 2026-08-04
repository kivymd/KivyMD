"""
Components/Search
=================

.. versionadded:: 2.0.0

.. seealso::

    `Material Design spec, Search <https://m3.material.io/components/search/overview>`_

.. rubric:: Search allows users to enter a keyword or phrase to get relevant information.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/search-preview.png
    :align: center

Usage
-----

.. code-block:: kv

    MDSearchBar:
        id: search_bar
        supporting_text: "Search in text"
        view_root: root

        # Search Bar.
        MDSearchBarLeadingContainer:
            MDSearchLeadingIcon:
                icon: "menu"
                on_release: app.open_menu(self)

        MDSearchBarTrailingContainer:

            MDSearchTrailingIcon:
                icon:"microphone"

            MDSearchTrailingAvatar:
                source:f"{images_path}/logo/kivymd-icon-128.png"

        # Search View.
        MDSearchViewLeadingContainer:

            MDSearchLeadingIcon:
                icon: "arrow-left"
                on_release: search_bar.close_view()

        MDSearchViewTrailingContainer:

            MDSearchTrailingIcon:
                icon: "window-close"

        MDSearchViewContainer:
            ...

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/searchbar-anatomy-1.png
    :align: center

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/searchbar-anatomy-2.png
    :align: center

Full example
------------

.. tabs::

    .. tab:: Imperative KV style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty

            from kivymd.app import MDApp
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.list import MDListItem


            class IconItem(MDListItem):
                icon = StringProperty()
                text = StringProperty()


            KV = '''
            #:import images_path kivymd.images_path

            <IconItem>
                theme_bg_color: "Custom"
                md_bg_color: [0, 0, 0, 0]

                MDListItemLeadingIcon:
                    icon: root.icon

                MDListItemSupportingText:
                    text: root.text


            MDScreen:
                md_bg_color: app.theme_cls.backgroundColor

                BoxLayout:
                    padding: [dp(10), dp(30), dp(10), dp(10)]
                    orientation: "vertical"

                    MDSearchBar:
                        id: search_bar
                        supporting_text: "Search in text"
                        view_root: root
                        on_text: app.set_list_md_icons(text=args[-1], search=True)

                        # Search Bar items.
                        MDSearchBarLeadingContainer:

                            MDSearchLeadingIcon:
                                icon: "menu"
                                on_release: print("Menu pressed")

                        MDSearchBarTrailingContainer:

                            MDSearchTrailingIcon:
                                icon: "microphone"
                                on_press: print("Microphone pressed")

                            MDSearchTrailingAvatar:
                                source: f"{images_path}/logo/kivymd-icon-128.png"
                                on_press: print("Avatar pressed")

                        # Search View.
                        MDSearchViewLeadingContainer:

                            MDSearchLeadingIcon:
                                icon: "arrow-left"
                                on_release: search_bar.close_view()

                        MDSearchViewTrailingContainer:

                            MDSearchTrailingIcon:
                                icon: "window-close"
                                on_release: search_bar.text = ""

                        MDSearchViewContainer:

                            RecycleView:
                                id: rv
                                key_viewclass: 'viewclass'
                                key_size: 'height'

                                RecycleBoxLayout:
                                    default_size: None, dp(48)
                                    default_size_hint: 1, None
                                    size_hint_y: None
                                    height: self.minimum_height
                                    orientation: 'vertical'

                    Widget:

                    BoxLayout:
                        size_hint_y: None
                        height: dp(30)
                        spacing: dp(10)

                        MDLabel:
                            text: "Bar dock"
                            halign: "right"

                        MDSwitch:
                            on_active: search_bar.docked = args[-1]
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def on_select_text(self, text):
                    self.root.ids.search_bar.text = text

                def on_start(self):
                    self.set_list_md_icons()

                def set_list_md_icons(self, text="", search=False):
                    def add_icon_item(name_icon):
                        self.root.ids.rv.data.append(
                            {
                                "viewclass": "IconItem",
                                "icon": name_icon,
                                "text": name_icon,
                                "on_release": lambda y=name_icon: self.on_select_text(y),
                            }
                        )

                    self.root.ids.rv.data = []

                    for name_icon in md_icons.keys():
                        if search:
                            if text in name_icon:
                                add_icon_item(name_icon)
                        else:
                            add_icon_item(name_icon)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.properties import StringProperty

            from kivymd import images_path
            from kivymd.icon_definitions import md_icons
            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.label import MDLabel
            from kivymd.uix.recycleboxlayout import MDRecycleBoxLayout
            from kivymd.uix.list import (
                MDListItem,
                MDListItemLeadingIcon,
                MDListItemSupportingText,
            )
            from kivymd.uix.recycleview import MDRecycleView
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.search import (
                MDSearchBar,
                MDSearchBarLeadingContainer,
                MDSearchLeadingIcon,
                MDSearchBarTrailingContainer,
                MDSearchTrailingIcon,
                MDSearchTrailingAvatar,
                MDSearchViewLeadingContainer,
                MDSearchViewTrailingContainer,
                MDSearchViewContainer,
            )
            from kivymd.uix.selectioncontrol import MDSwitch
            from kivymd.uix.widget import MDWidget


            class IconItem(MDListItem):
                icon = StringProperty()
                text = StringProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    self.theme_bg_color = "Custom"
                    self.md_bg_color = [0, 0, 0, 0]

                    self.leading_icon = MDListItemLeadingIcon()
                    self.supporting_text = MDListItemSupportingText()

                    self.widgets = [
                        self.leading_icon,
                        self.supporting_text,
                    ]

                def on_icon(self, instance, value):
                    self.leading_icon.icon = value

                def on_text(self, instance, value):
                    self.supporting_text.text = value


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Olive"
                    return MDScreen(
                        MDBoxLayout(
                            MDSearchBar(
                                MDSearchBarLeadingContainer(
                                    MDSearchLeadingIcon(
                                        icon="menu",
                                        on_release=lambda x: print("Menu pressed"),
                                    ),
                                ),
                                MDSearchBarTrailingContainer(
                                    MDSearchTrailingIcon(
                                        icon="microphone",
                                        on_press=lambda x: print("Microphone pressed"),
                                    ),
                                    MDSearchTrailingAvatar(
                                        source=f"{images_path}/logo/kivymd-icon-128.png",
                                        on_press=lambda x: print("Avatar pressed"),
                                    ),
                                ),
                                MDSearchViewLeadingContainer(
                                    MDSearchLeadingIcon(
                                        icon="arrow-left",
                                        on_release=lambda x: self.search_bar_close_view(),
                                    ),
                                ),
                                MDSearchViewTrailingContainer(
                                    MDSearchTrailingIcon(
                                        icon="window-close",
                                        on_release=lambda x: self.set_search_bar_text(),
                                    ),
                                ),
                                MDSearchViewContainer(
                                    MDRecycleView(
                                        MDRecycleBoxLayout(
                                            id="rv_box",
                                            default_size=[None, dp(48)],
                                            default_size_hint=[1, None],
                                            size_hint_y=None,
                                            orientation="vertical",
                                        ),
                                        id="rv",
                                    ),
                                ),
                                id="search_bar",
                                supporting_text="Search in text",
                            ),
                            MDWidget(),
                            MDBoxLayout(
                                MDLabel(
                                    text="Bar dock",
                                    halign="right",
                                ),
                                MDSwitch(
                                    on_active=lambda x, y: self.set_docked(y),
                                ),
                                size_hint_y=None,
                                height=dp(30),
                                spacing=dp(10),
                            ),
                            padding=[dp(10), dp(30), dp(10), dp(10)],
                            orientation="vertical",
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )

                def set_docked(self, value):
                    self.root.get_ids().search_bar.docked = value

                def search_bar_close_view(self):
                    self.root.get_ids().search_bar.close_view()

                def set_search_bar_text(self):
                    self.root.get_ids().search_bar.text = ""

                def on_select_text(self, text):
                    self.root.get_ids().search_bar.text = text

                def on_start(self):
                    search_bar = self.root.get_ids().search_bar
                    rv = self.root.get_ids().rv
                    rv_box = self.root.get_ids().rv_box

                    rv.key_size = "height"
                    rv.key_viewclass = "viewclass"
                    search_bar.view_root = self.root

                    rv_box.bind(minimum_height=rv_box.setter("height"))
                    search_bar.bind(
                        text=lambda instance, text: self.set_list_md_icons(text, True)
                    )

                    self.set_list_md_icons()

                def set_list_md_icons(self, text="", search=False):
                    def add_icon_item(name_icon):
                        self.root.get_ids().rv.data.append(
                            {
                                "viewclass": "IconItem",
                                "icon": name_icon,
                                "text": name_icon,
                                "on_release": lambda y=name_icon: self.on_select_text(y),
                            }
                        )

                    self.root.get_ids().rv.data = []

                    for name_icon in md_icons.keys():
                        if search:
                            if text in name_icon:
                                add_icon_item(name_icon)
                        else:
                            add_icon_item(name_icon)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/searchbar-example.gif
    :align: center
"""

from __future__ import annotations

__all__ = (
    "MDSearchBar",
    "MDSearchTrailingAvatar",
    "MDSearchTrailingIcon",
    "MDSearchLeadingIcon",
    "MDSearchViewContainer",
    "MDSearchBarLeadingContainer",
    "MDSearchBarTrailingContainer",
    "MDSearchViewLeadingContainer",
    "MDSearchViewTrailingContainer",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDIcon
from kivymd.utils import next_frame

with open(
    os.path.join(uix_path, "search", "search.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSearchTrailingAvatar(ButtonBehavior, Image):
    """
    Trailing avatar class.

    For more information, see in the
    :class:`~kivy.uix.behaviors.button.ButtonBehavior` and
    :class:`~kivy.uix.image.Image`
    classes documentation.
    """


class MDSearchLeadingIcon(ButtonBehavior, MDIcon):
    """
    Leading icon class.

    For more information, see in the
    :class:`~kivy.uix.behaviors.button.ButtonBehavior` and
    :class:`~kivymd.uix.label.MDIcon`
    classes documentation.
    """


class MDSearchTrailingIcon(ButtonBehavior, MDIcon):
    """
    Trailing icon class.

    For more information, see in the
    :class:`~kivy.uix.behaviors.button.ButtonBehavior` and
    :class:`~kivymd.uix.label.MDIcon`
    classes documentation.
    """


class MDSearchBarTrailingContainer(DeclarativeBehavior, BoxLayout):
    """
    Trailing container class for search bar.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout`
    class documentation.
    """


class MDSearchBarLeadingContainer(DeclarativeBehavior, BoxLayout):
    """
    Leading container class for search bar.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout`
    class documentation.
    """


class MDSearchViewTrailingContainer(DeclarativeBehavior, BoxLayout):
    """
    Trailing container class for search view.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout`
    class documentation.
    """


class MDSearchViewLeadingContainer(DeclarativeBehavior, BoxLayout):
    """
    Leading container class for search view.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout`
    class documentation.
    """


class MDSearchViewContainer(DeclarativeBehavior, BoxLayout):
    """
    A container for widgets that are displayed when the search bar is in focus.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout`
    class documentation.
    """

    _d = 0.3
    _children = None

    def add_widget(self, widget, *args, **kwargs):
        if self._children is not None:
            raise Exception("MDSearchViewContainer only accetps single widget")

        self._children = widget

    def show_child(self, anim_time: float) -> None:
        """
        Displays the stored child widget with a fade-in animation.

        :param anim_time: Delay before showing the widget.
        """

        self._children.opacity = 0
        next_frame(
            Animation(opacity=1, d=self._d).start, self._children, t=anim_time
        )
        next_frame(super().add_widget, self._children, t=anim_time)

    def hide_child(self) -> None:
        """Removes the stored child widget from the layout."""

        super().remove_widget(self._children)

    def remove_widget(self, widget):
        if self._children == widget:
            super().remove_widget(self._children)


class MDSearchWidget(RelativeLayout):
    """
    Internal widget for the search bar.

    For more information, see in the
    :class:`~kivy.uix.relativelayout.RelativeLayout`
    class documentation.
    """

    _font_style = theme_font_styles["Title"]["medium"]
    _d = 0.3
    _t = "easing_standard"
    state = "close"

    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

    def update_bar(self, *args) -> None:
        """
        Updates the search widget geometry.

        Adjusts the size, position, and corner radius of the search
        container depending on whether the search view is opened or
        closed, and whether the search bar is docked.
        """

        if self.state == "close":
            self.ids.root_container.size = self.root.size
            self.ids.root_container.radius = dp(28)
            self.ids.root_container.pos = self.root.pos
        else:
            if self.root.docked:
                self.ids.root_container.radius = [dp(28)] * 4
                docked_size = self.root.width, dp(56) + self.root.docked_height
                self.ids.root_container.pos = [
                    self.root.pos[0],
                    self.root.pos[1] - docked_size[1] + dp(56),
                ]
            else:
                self.ids.root_container.radius = [0] * 4
                self.ids.root_container.pos = [0, 0]
                self.ids.root_container.size = self.size

    def _docked_open(self, opacity_down, opacity_up):
        docked_size = self.root.width, dp(56) + self.root.docked_height
        Animation(
            size=docked_size,
            pos=[self.root.pos[0], self.root.pos[1] - docked_size[1] + dp(56)],
            radius=[dp(28)] * 4,
            t=self._t,
            d=self._d,
        ).start(self.ids.root_container)

        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 0
        self.root._view_container.padding = [0, 0, 0, dp(16)]

        next_frame(
            self.ids.root_container.add_widget,
            self.root._view_container,
            index=0,
        )
        next_frame(opacity_up.start, self.root._view_container, t=self._d)
        self.icons_open(opacity_up, opacity_down, self._d / 2)
        self.root._view_container.show_child(self._d)

    def _docked_close(self, opacity_down, opacity_up):
        self._close(opacity_down, opacity_up)

    def _open(self, opacity_down, opacity_up):
        h_d = self._d / 2

        # Container.
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 0
        self.root._view_container.padding = [0] * 4

        self.ids.root_container.add_widget(self.root._view_container, index=0)
        next_frame(opacity_up.start, self.root._view_container, t=h_d / 1.5)
        Animation(
            size=self.size, pos=self.pos, radius=[0] * 4, t=self._t, d=self._d
        ).start(self.ids.root_container)

        # Header.
        Animation(height=dp(70), t=self._t, d=self._d).start(self.ids.header)
        self.icons_open(opacity_up, opacity_down, h_d)
        self.root._view_container.show_child(self._d)

    def _close(self, opacity_down, opacity_up):
        h_d = self._d / 2

        # Container.
        self.root._view_container.size_hint_y = 1
        self.root._view_container.opacity = 1

        opacity_down.start(self.root._view_container)

        if self.root._view_container in self.ids.root_container.children:
            next_frame(
                self.ids.root_container.remove_widget,
                self.root._view_container,
                t=self._d,
            )

        next_frame(setattr, self.root._view_container, "height", dp(56), t=h_d)

        Animation(
            size=[self.root.width, dp(56)],
            pos=self.root.pos,
            radius=[dp(28)] * 4,
            t=self._t,
            d=self._d,
        ).start(self.ids.root_container)

        # Header.
        Animation(height=dp(56), t=self._t, d=self._d).start(self.ids.header)
        self.icons_close(opacity_up, opacity_down, h_d)
        self.root._view_container.hide_child()

    def icons_close(self, opacity_up, opacity_down, h_d) -> None:
        """
        Animates the transition to the closed search bar icons.

        Fades out the search view leading and trailing containers,
        updates the header layout, and fades in the search bar
        leading and trailing containers.

        :param opacity_up: Animation used to fade widgets in.
        :param opacity_down: Animation used to fade widgets out.
        :param h_d: Delay before switching the header containers.
        """

        opacity_down.start(self.root._view_trailing_container)
        opacity_down.start(self.root._view_leading_container)

        self.root._bar_leading_container.opacity = 0
        self.root._bar_trailing_container.opacity = 0

        next_frame(self.update_state_closed, t=h_d)
        next_frame(opacity_up.start, self.root._bar_trailing_container, t=h_d)
        next_frame(opacity_up.start, self.root._bar_leading_container, t=h_d)

    def icons_open(self, opacity_up, opacity_down, h_d) -> None:
        """
        Animates the transition to the opened search view icons.

        Fades out the search bar leading and trailing containers,
        updates the header layout, and fades in the search view
        leading and trailing containers.

        :param opacity_up: Animation used to fade widgets in.
        :param opacity_down: Animation used to fade widgets out.
        :param h_d: Delay before switching the header containers.
        """

        opacity_down.start(self.root._bar_trailing_container)
        opacity_down.start(self.root._bar_leading_container)

        self.root._view_leading_container.opacity = 0
        self.root._view_trailing_container.opacity = 0

        next_frame(self.update_state_opened, t=h_d)
        next_frame(opacity_up.start, self.root._view_trailing_container, t=h_d)
        next_frame(opacity_up.start, self.root._view_leading_container, t=h_d)

    switching_state = False

    def switch_state(self, new_state: str) -> None:
        """
        Switches the search widget between opened and closed states.

        Starts the corresponding animations and prevents overlapping
        state transitions while an animation is already running.

        :param new_state: Target state. Either ``"open"`` or ``"close"``.
        """

        if self.switching_state or new_state == self.state:
            return

        self.switching_state = True

        opacity_down = Animation(opacity=0, d=self._d / 2)
        opacity_up = Animation(opacity=1, d=self._d / 2)

        if self.root.docked:
            self.root.width = self.root.docked_width
            self.ids.root_container.width = self.root.docked_width
            getattr(self, "_docked_" + new_state)(opacity_down, opacity_up)
        else:
            getattr(self, "_" + new_state)(opacity_down, opacity_up)

        if new_state == "close":
            self.ids.text_input.focus = False

        self.state = new_state
        Clock.schedule_once(
            lambda dt: setattr(self, "switching_state", False), self._d
        )

    def clean_header(self) -> None:
        """Removes all header widgets except the text input."""

        for child in self.ids.header.children:
            if child.__class__.__name__ != "TextInput":
                self.ids.header.remove_widget(child)

    def init_state(self) -> None:
        """
        Initializes the search widget.

        Sets the initial size and layout according to the current
        ``docked`` state and updates the header to the closed state.
        """

        if self.root.docked:
            self.root.size_hint_x = None
            self.root.width = self.root.docked_width
        else:
            self.root.size_hint_x = 1

        self.ids.root_container.size = [self.root.width, dp(56)]
        self.update_state_closed()

    def update_state_opened(self, *args):
        """
        Updates the header layout for the opened search view.

        Replaces the search bar containers with the search view leading and
        trailing containers.
        """

        self.clean_header()
        self.ids.header.add_widget(self.root._view_leading_container, index=2)
        self.ids.header.add_widget(self.root._view_trailing_container, index=0)

    def update_state_closed(self, *args):
        """
        Updates the header layout for the closed search bar.

        Replaces the search view containers with the search bar leading and
        trailing containers.
        """

        self.clean_header()
        self.ids.header.add_widget(self.root._bar_leading_container, index=2)
        self.ids.header.add_widget(self.root._bar_trailing_container, index=0)


class MDSearchBar(DeclarativeBehavior, Widget):
    """
    Search bar class.

    For more information, see in the
    :class:`~kivy.uix.widget.Widget`
    class documentation.
    """

    leading_icon = StringProperty("magnify")
    """
    Leading icon name.

    :attr:`leading_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'magnify'`.
    """

    supporting_text = StringProperty("Hinted search text")
    """
    Supporting text.

    :attr:`supporting_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Hinted search text'`.
    """

    view_root = ObjectProperty(None)
    """
    Root widget for search view.

    :attr:`view_root` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    docked_width = NumericProperty(dp(360))
    """
    Docked width.

    :attr:`docked_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(360)`.
    """

    docked_height = NumericProperty(dp(240))
    """
    Docked height.

    :attr:`docked_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(240)`.
    """

    docked = BooleanProperty(False)
    """
    If `True`, the search bar will be docked.

    :attr:`docked` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    text = StringProperty("")
    """
    Search query text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    # Internal props.
    _search_widget = None
    _bar_leading_container = None
    _bar_trailing_container = None
    _view_leading_container = None
    _view_trailing_container = None
    _view_container = None
    _view_map = {
        "MDSearchBarLeadingContainer": "_bar_leading_container",
        "MDSearchBarTrailingContainer": "_bar_trailing_container",
        "MDSearchViewLeadingContainer": "_view_leading_container",
        "MDSearchViewTrailingContainer": "_view_trailing_container",
        "MDSearchViewContainer": "_view_container",
    }
    __events__ = (
        "on_open",
        "on_close",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_widget = MDSearchWidget(self)
        self.bind(pos=self._search_widget.update_bar)
        self.bind(size=self._search_widget.update_bar)
        self.on_docked(self, self.docked)

    def on_docked(self, instance, docked) -> None:
        """
        Called when the :attr:`docked` property changes.

        :param instance: The MDSearchBar instance.
        :param docked: The new docked value (True/False).

        Updates the size_hint_x and width accordingly. When docked,
        sets a fixed width using docked_width property.
        """

        if docked:
            self.size_hint_x = None
            self.width = self.docked_width
        else:
            self.size_hint_x = 1

    def on_supporting_text(self, instance, text: str) -> None:
        """
        Called when the :attr:`supporting_text` property changes.

        :param instance: The MDSearchBar instance.
        :param text: The new supporting text.

        Updates the hint text of the text input field to display
        the provided supporting text.
        """

        def set_hint_text(*args):
            self._search_widget.ids.text_input.hint_text = text

        Clock.schedule_once(set_hint_text)

    def on_view_root(self, *args) -> None:
        """
        Called when the view_root property changes.

        :param args: Arguments passed to the method.

        Removes the search widget from its current parent (if any),
        adds it to the new view_root, and initializes the search widget
        state and position.
        """

        if self._search_widget.parent:
            self._search_widget.parent.remove_widget(self._search_widget)

        self.view_root.add_widget(self._search_widget)
        self._search_widget.init_state()
        self._search_widget.update_bar()
        self.view_root.bind(size=self._search_widget.update_bar)

    def add_widget(self, widget):
        if widget.__class__.__name__ in self._view_map.keys():
            setattr(self, self._view_map[widget.__class__.__name__], widget)

    def close_view(self) -> None:
        """Closes the search view."""

        self._search_widget.switch_state("close")
        self.dispatch("on_close")

    def open_view(self) -> None:
        """Opens the search view."""

        self._search_widget.switch_state("open")
        self.dispatch("on_open")

    def on_open(self) -> None:
        """
        Event handler for the on_open event.

        Override this method in subclasses to handle the search view
        opening event.
        """

    def on_close(self) -> None:
        """
        Event handler for the on_close event.

        Override this method in subclasses to handle the search view
        closing event.
        """

    def on_text(self, *args) -> None:
        """
        Called when the :attr:`text` property changes.

        :param args: containing MDSearchBar instance and new text value.

        Updates the text in the text input field to match the new text
        property value.
        """

        self._search_widget.ids.text_input.text = args[-1]
