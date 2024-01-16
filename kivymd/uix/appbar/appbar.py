"""
Components/Appbar
=================

.. seealso::

    `Material Design spec, App bars: top <https://m3.material.io/components/top-app-bar/overview>`_

    `Material Design spec, App bars: bottom <https://m3.material.io/components/bottom-app-bar/overview>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-top.png
    :align: center

`KivyMD` provides the following bar positions for use:

- TopAppBar_
- BottomAppBar_

.. TopAppBar_:

TopAppBar
---------

- Contains a title and actions related to the current screen
- Four types: center-aligned, small, medium, and large
- On scroll, apply a container fill color to separate app bar from body content
- Top app bars have the same width as the device window

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-available-types.png
    :align: center

1. Center-aligned
2. Small
3. Medium
4. Large

.. note:: KivyMD does not provide a `Center-aligned` type panel. But you can
    easily create this pit panel yourself (read the documentation below).

Usage
-----

.. code-block:: kv

    MDTopAppBar:
        type: "small"

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "menu"

        MDTopAppBarTitle:
            text: "AppBar Center-aligned"
            pos_hint: {"center_x": .5}

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "account-circle-outline"

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-anatomy.png
    :align: center

Configurations
==============

1. Center-aligned
-----------------

.. code-block:: kv

    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor

        MDTopAppBar:
            type: "small"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "menu"

            MDTopAppBarTitle:
                text: "AppBar small"
                pos_hint: {"center_x": .5}

            MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "account-circle-outline"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-center-aligned.png
    :align: center

2. Small
--------

.. code-block:: kv

    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor

        MDTopAppBar:
            type: "small"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "arrow-left"

            MDTopAppBarTitle:
                text: "AppBar small"

            MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "attachment"

                MDActionTopAppBarButton:
                    icon: "calendar"

                MDActionTopAppBarButton:
                    icon: "dots-vertical"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-small.png
    :align: center

3. Medium
---------

.. code-block:: kv

    MDTopAppBar:
        type: "medium"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-medium.png
    :align: center

4. Large
--------

.. code-block:: kv

    MDTopAppBar:
        type: "large"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/top-appbar-large.png
    :align: center

.. BottomAppBar:

BottomAppBar
------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/app-bar-bottom-m3.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDBottomAppBar:

            MDFabBottomAppBarButton:
                icon: "plus"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-1.png
    :align: center

Add action items
----------------

.. code-block:: kv

    #:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton


    MDScreen:

        MDBottomAppBar:
            action_items:
                [
                MDActionBottomAppBarButton(icon="gmail"),
                MDActionBottomAppBarButton(icon="label-outline"),
                MDActionBottomAppBarButton(icon="bookmark"),
                ]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-2.png
    :align: center

Change action items
-------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.appbar import MDActionBottomAppBarButton

    KV = '''
    #:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDBottomAppBar:
            id: bottom_appbar
            action_items:
                [
                MDActionBottomAppBarButton(icon="gmail"),
                MDActionBottomAppBarButton(icon="bookmark"),
                ]

            MDFabBottomAppBarButton:
                icon: "plus"
                on_release: app.change_actions_items()
    '''


    class Example(MDApp):
        def change_actions_items(self):
            self.root.ids.bottom_appbar.action_items = [
                MDActionBottomAppBarButton(icon="magnify"),
                MDActionBottomAppBarButton(icon="trash-can-outline"),
                MDActionBottomAppBarButton(icon="download-box-outline"),
            ]

        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-3.gif
    :align: center

A practical example
-------------------

.. code-block:: python

    import asynckivy

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
    from kivy.uix.behaviors import FocusBehavior
    from kivy.uix.recycleboxlayout import RecycleBoxLayout
    from kivy.uix.recycleview.layout import LayoutSelectionBehavior
    from kivy.uix.recycleview.views import RecycleDataViewBehavior

    from kivymd.uix.appbar import MDActionBottomAppBarButton
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.app import MDApp

    from faker import Faker  # pip install Faker

    KV = '''
    #:import MDFabBottomAppBarButton kivymd.uix.appbar.MDFabBottomAppBarButton


    <UserCard>
        orientation: "vertical"
        adaptive_height: True
        md_bg_color: "#373A22" if self.selected else "#1F1E15"
        radius: 16
        padding: 0, 0, 0, "16dp"

        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: root.md_bg_color
            radius: root.radius
            ripple_effect: False

            MDListItemLeadingAvatar:
                source: root.avatar
                # radius: self.height / 2

            MDListItemHeadlineText:
                text: root.name
                theme_text_color: "Custom"
                text_color: "#8A8D79"

            MDListItemSupportingText:
                text: root.time
                theme_text_color: "Custom"
                text_color: "#8A8D79"

        MDLabel:
            text: root.text
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: "#8A8D79"
            padding_x: "16dp"
            shorten: True
            shorten_from: "right"

        Widget:


    MDFloatLayout:
        md_bg_color: "#151511"

        RecycleView:
            id: card_list
            viewclass: "UserCard"

            SelectableRecycleGridLayout:
                orientation: 'vertical'
                spacing: "16dp"
                padding: "16dp"
                default_size: None, dp(120)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                multiselect: True
                touch_multiselect: True

        MDBottomAppBar:
            id: bottom_appbar
            scroll_cls: card_list
            allow_hidden: True
            theme_bg_color: "Custom"
            md_bg_color: "#232217"

            MDFabBottomAppBarButton:
                id: fab_button
                icon: "plus"
                theme_bg_color: "Custom"
                md_bg_color: "#373A22"
                theme_icon_color: "Custom"
                icon_color: "#ffffff"
    '''


    class UserCard(RecycleDataViewBehavior, MDBoxLayout):
        name = StringProperty()
        time = StringProperty()
        text = StringProperty()
        avatar = StringProperty()
        callback = ObjectProperty(lambda x: x)

        index = None
        selected = BooleanProperty(False)
        selectable = BooleanProperty(True)

        def refresh_view_attrs(self, rv, index, data):
            self.index = index
            return super().refresh_view_attrs(rv, index, data)

        def on_touch_down(self, touch):
            if super().on_touch_down(touch):
                return True
            if self.collide_point(*touch.pos) and self.selectable:
                Clock.schedule_once(self.callback)
                return self.parent.select_with_touch(self.index, touch)

        def apply_selection(self, rv, index, is_selected):
            self.selected = is_selected
            rv.data[index]["selected"] = is_selected


    class SelectableRecycleGridLayout(
        FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout
    ):
        pass


    class BottomAppBarButton(MDActionBottomAppBarButton):
        theme_icon_color = "Custom"
        icon_color = "#8A8D79"


    class Example(MDApp):
        selected_cards = False

        def build(self):
            return Builder.load_string(KV)

        def on_tap_card(self, *args):
            datas = [data["selected"] for data in self.root.ids.card_list.data]
            if True in datas and not self.selected_cards:
                self.root.ids.bottom_appbar.action_items = [
                    BottomAppBarButton(icon="gmail"),
                    BottomAppBarButton(icon="label-outline"),
                    BottomAppBarButton(icon="bookmark"),
                ]
                self.root.ids.fab_button.icon = "pencil"
                self.selected_cards = True
            else:
                if len(list(set(datas))) == 1 and not list(set(datas))[0]:
                    self.selected_cards = False
                if not self.selected_cards:
                    self.root.ids.bottom_appbar.action_items = [
                        BottomAppBarButton(icon="magnify"),
                        BottomAppBarButton(icon="trash-can-outline"),
                        BottomAppBarButton(icon="download-box-outline"),
                    ]
                    self.root.ids.fab_button.icon = "plus"

        def on_start(self):
            async def generate_card():
                for i in range(10):
                    await asynckivy.sleep(0)
                    self.root.ids.card_list.data.append(
                        {
                            "name": fake.name(),
                            "time": fake.date(),
                            "avatar": fake.image_url(),
                            "text": fake.text(),
                            "selected": False,
                            "callback": self.on_tap_card,
                        }
                    )

            super().on_start()
            self.on_tap_card()
            fake = Faker()
            Clock.schedule_once(lambda x: asynckivy.start(generate_card()))


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottom-app-bar-m3-style-4.gif
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDTopAppBar:
        type_height: "large"
        headline_text: "Headline"
        left_action_items: [["arrow-left", lambda x: x]]
        right_action_items:
            [ \
            ["attachment", lambda x: x], \
            ["calendar", lambda x: x], \
            ["dots-vertical", lambda x: x], \
            ]
        anchor_title: "left"

2.0.0 version
-------------

.. code-block:: kv

    MDTopAppBar:
        type: "large"

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "arrow-left"

        MDTopAppBarTitle:
            text: "AppBar small"

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "attachment"

            MDActionTopAppBarButton:
                icon: "calendar"

            MDActionTopAppBarButton:
                icon: "dots-vertical"
"""

from __future__ import annotations

__all__ = (
    "MDTopAppBar",
    "MDTopAppBarTitle",
    "MDBottomAppBar",
    "MDActionTopAppBarButton",
    "MDActionBottomAppBarButton",
    "MDFabBottomAppBarButton",
    "MDTopAppBarLeadingButtonContainer",
    "MDTopAppBarTrailingButtonContainer",
)

import os

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    ColorProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CommonElevationBehavior,
    DeclarativeBehavior,
    RotateBehavior,
    ScaleBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.button import MDFabButton, MDIconButton
from kivymd.uix.controllers import WindowController
from kivymd.uix.label import MDLabel
from kivymd.utils.set_bars_colors import set_bars_colors

import asynckivy

with open(
    os.path.join(uix_path, "appbar", "appbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseTopAppBarButtonContainer(DeclarativeBehavior, BoxLayout):
    # kivymd.uix.appbar.appbar.MDTopAppBar object.
    _appbar = ObjectProperty()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDActionTopAppBarButton):
            Clock.schedule_once(lambda x: self._check_icon_color(widget))

        return super().add_widget(widget)

    def _check_icon_color(self, widget):
        if widget.theme_icon_color == "Primary" and widget.icon_color == None:
            widget.theme_icon_color = "Custom"
            widget.icon_color = widget.theme_cls.onSurfaceColor


class MDFabBottomAppBarButton(MDFabButton, RotateBehavior, ScaleBehavior):
    """
    Implements a floating action button (FAB) for a bar with type 'bottom'.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDFabButton` and
    :class:`~kivymd.uix.behaviors.rotate_behavior.RotateBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    classes documentation.
    """


class MDActionTopAppBarButton(MDIconButton):
    """
    Implements action buttons on the bar.

    For more information, see in the
    :class:`~kivymd.uix.button.button.MDIconButton` class documentation.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the button when
    the button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDActionBottomAppBarButton(MDActionTopAppBarButton):
    """
    Implements action buttons for a
    :class:'~kivymd.uix.appbar.appbar.MDBottomAppBar' class.

    .. versionadded:: 1.2.0

    For more information, see in the
    :class:`~kivymd.uix.appbar.appbar.MDActionTopAppBarButton`
    class documentation.
    """


class MDTopAppBarTitle(MDLabel):
    """
    Implements the panel title.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    _appbar = ObjectProperty()
    _title_width = NumericProperty(0)

    # FIXME: When changing the text, the texture_size property returns an
    #  incorrect value, which causes the panel title to shift.
    def on_text(self, instance, value) -> None:
        """Fired when the :attr:`text` value changes."""

        def set_title_width(*args) -> None:
            self._title_width = self.texture_size[0]

        Clock.schedule_once(set_title_width)

    def on_pos_hint(self, instance, value) -> None:
        """Fired when the :attr:`pos_hint` value changes."""

        if self._appbar:
            Clock.schedule_once(
                lambda x: self._appbar._set_padding_title(value)
            )


class MDTopAppBarLeadingButtonContainer(BaseTopAppBarButtonContainer):
    """
    Implements a container for the leading action buttons.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """


class MDTopAppBarTrailingButtonContainer(BaseTopAppBarButtonContainer):
    """
    Implements a container for the trailing action buttons.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """


# FIXME: The on_enter/on_leave event is not triggered for
#  MDActionTopAppBarButton buttons in the MDTopAppBarTrailingButtonContainer
#  container.
class MDTopAppBar(
    DeclarativeBehavior,
    ThemableBehavior,
    CommonElevationBehavior,
    BackgroundColorBehavior,
    BoxLayout,
    WindowController,
):
    """
    Top app bar class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` and
    :class:`~kivymd.uix.controllers.windowcontroller.WindowController`
    classes documentation.

    :Events:
        `on_action_button`
            Method for the button used for the :class:`~MDBottomAppBar` class.
    """

    set_bars_color = BooleanProperty(False)
    """
    If `True` the background color of the bar status will be set automatically
    according to the current color of the bar.

    .. versionadded:: 1.0.0

    See `set_bars_colors <https://kivymd.readthedocs.io/en/latest/api/kivymd/utils/set_bars_colors/>`_
    for more information.

    :attr:`set_bars_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    type = OptionProperty("small", options=["medium", "large", "small"])
    """
    Bar height type.

    .. versionadded:: 1.0.0

    Available options are: 'medium', 'large', 'small'.

    :attr:`type_height` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'small'`.
    """

    _trailing_button_container = ObjectProperty()
    _leading_button_container = ObjectProperty()
    _appbar_title = ObjectProperty()

    def on_type(self, instance, value) -> None:
        def on_type(*args):
            if value in ("medium", "large"):
                self.ids.root_box.add_widget(Widget(), index=1)

        Clock.schedule_once(on_type, 0.5)

    def on_size(self, instance, size) -> None:
        """Fired when the application screen size changes."""

        if self._appbar_title:
            if not self._appbar_title._title_width:
                self._appbar_title._title_width = (
                    self._appbar_title.texture_size[0]
                )
            Clock.schedule_once(
                lambda x: self._appbar_title.on_pos_hint(
                    self._appbar_title, self._appbar_title.pos_hint
                )
            )

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDTopAppBarTitle):
            widget._appbar = self
            self._appbar_title = widget
            Clock.schedule_once(lambda x: self._add_title(widget))
        elif isinstance(widget, MDTopAppBarTrailingButtonContainer):
            self._trailing_button_container = widget
            widget._appbar = self
            Clock.schedule_once(lambda x: self.ids.root_box.add_widget(widget))
        elif isinstance(widget, MDTopAppBarLeadingButtonContainer):
            widget._appbar = self
            self._leading_button_container = widget
            Clock.schedule_once(lambda x: self.ids.root_box.add_widget(widget))
        else:
            return super().add_widget(widget)

    def _add_title(self, widget):
        if self.type == "small":
            self.ids.root_box.add_widget(widget)
        else:
            self.ids.title_box.add_widget(widget)

    def _set_padding_title(self, value):
        if value.get("center_x", 0) == 0.5 and self.type == "small":
            if (
                not self._trailing_button_container
                and self._leading_button_container
            ):
                left_padding = (self.width // 2) - (
                    self._leading_button_container.width
                    + (self._appbar_title._title_width // 2)
                )
                self._appbar_title.padding = [left_padding, 0, 0, 0]
            elif (
                self._trailing_button_container
                and not self._leading_button_container
            ):
                left_padding = (self.width // 2) - (
                    self._appbar_title._title_width // 2
                )
                right_padding = (self.width // 2) - (
                    self._trailing_button_container.width
                    + (self._appbar_title._title_width // 2)
                )
                self._appbar_title.padding = [left_padding, 0, right_padding, 0]
            elif (
                not self._trailing_button_container
                and not self._leading_button_container
            ):
                left_padding = (self.width // 2) - (
                    self._appbar_title._title_width // 2
                )
                right_padding = (self.width // 2) - (
                    self._appbar_title._title_width // 2
                )
                self._appbar_title.padding = [left_padding, 0, right_padding, 0]
            elif (
                self._trailing_button_container
                and self._leading_button_container
            ):
                left_padding = (self.width // 2) - (
                    self._leading_button_container.width
                    + (self._appbar_title._title_width // 2)
                )
                right_padding = (self.width // 2) - (
                    self._trailing_button_container.width
                    + (self._appbar_title._title_width // 2)
                )
                self._appbar_title.padding = [left_padding, 0, right_padding, 0]
        elif (
            not value
            and self._trailing_button_container
            and self._leading_button_container
        ):
            if self.type == "small":
                right_padding = self.width - (
                    self._trailing_button_container.width
                    + self._leading_button_container.width
                    + self._appbar_title._title_width
                )
                self._appbar_title.padding = [0, 0, right_padding, 0]
        elif (
            not value
            and self._trailing_button_container
            and not self._leading_button_container
        ):
            if self.type == "small":
                right_padding = self.width - (
                    self._trailing_button_container.width
                    + self._appbar_title._title_width
                )
                self._appbar_title.padding = [
                    dp(16),
                    0,
                    right_padding - dp(16),
                    0,
                ]
        elif (
            not value
            and not self._trailing_button_container
            and not self._leading_button_container
        ):
            self._appbar_title.padding_x = dp(16)


class MDBottomAppBar(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
    FloatLayout,
):
    """
    Bottom app bar class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    classes documentation.

    :Events:
        `on_show_bar`
            The method is fired when the :class:`~MDBottomAppBar` panel
            is shown.
        `on_hide_bar`
            The method is fired when the :class:`~MDBottomAppBar` panel
            is hidden.
    """

    action_items = ListProperty()
    """
    The icons on the left bar.

    .. versionadded:: 1.2.0

    :attr:`action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    animation = BooleanProperty(True)
    """
    # TODO: add description.
    # FIXME: changing the value does not affect anything.

    .. versionadded:: 1.2.0

    :attr:`animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    show_transition = StringProperty("linear")
    """
    Type of button display transition.

    .. versionadded:: 1.2.0

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    hide_transition = StringProperty("in_back")
    """
    Type of button hidden transition.

    .. versionadded:: 1.2.0

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_back'`.
    """

    hide_duration = NumericProperty(0.4)
    """
    Duration of button hidden transition.

    .. versionadded:: 1.2.0

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    show_duration = NumericProperty(0.2)
    """
    Duration of button display transition.

    .. versionadded:: 1.2.0

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    scroll_cls = ObjectProperty()
    """
    Widget inherited from the :class:`~kivy.uix.scrollview.ScrollView` class.
    The value must be set if the :attr:`allow_hidden` parameter is `True`.

    .. versionadded:: 1.2.0

    :attr:`scroll_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    allow_hidden = BooleanProperty(False)
    """
    Allows or disables hiding the panel when scrolling content.
    If the value is `True`, the :attr:`scroll_cls` parameter must be specified.

    .. versionadded:: 1.2.0

    :attr:`allow_hidden` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    bar_is_hidden = BooleanProperty(False)
    """
    Is the panel currently hidden.

    .. versionadded:: 1.2.0

    :attr:`bar_is_hidden` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _padding = dp(16)
    _x = -dp(48)
    _scroll_cls_y = 0
    _cache = []
    _current_data = []
    _wait_removed = False
    _animated_hidden = True
    _animated_show = True
    _fab_bottom_app_bar_button = None
    _action_overflow_button = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_show_bar")
        self.register_event_type("on_hide_bar")

    def button_centering_animation(
        self,
        button: MDActionBottomAppBarButton | MDFabBottomAppBarButton,
    ) -> None:
        """
        Animation of centering buttons for
        :class:`~MDActionOverFlowButton`,
        :class:`~MDActionBottomAppBarButton` and
        :class:`~MDFabBottomAppBarButton` classes.
        """

        if self.animation:
            Animation(
                y=self.height / 2 - dp(48) / 2,
                opacity=1,
                d=self.show_duration,
                t=self.show_transition,
            ).start(button)

    def check_scroll_direction(self, scroll_cls, y: float) -> None:
        """
        Checks the scrolling direction.
        Depending on the scrolling direction, hides or shows the
        :class:`~MDBottomAppBar` panel.
        """

        if round(y, 1) < self._scroll_cls_y and not self.bar_is_hidden:
            self.hide_bar()
        if round(y, 1) > self._scroll_cls_y and self.bar_is_hidden:
            self.show_bar()

        self._scroll_cls_y = round(y, 1)

    def show_bar(self) -> None:
        """Show :class:`~MDBottomAppBar` panel."""

        def on_complete(*args):
            self.dispatch("on_show_bar")

        def on_progress(animation, instance, progress):
            if progress > 0.5 and self._animated_show:
                self._animated_show = False
                for i, widget in enumerate(self.children):
                    if isinstance(widget, MDActionBottomAppBarButton):
                        anim_icon = Animation(
                            y=self.height / 2 - dp(48) / 2,
                            d=self.show_duration,
                            t=self.show_transition,
                        )
                        Clock.schedule_once(
                            lambda x, y=widget: anim_icon.start(y),
                            i / 10,
                        )
                if self._fab_bottom_app_bar_button:
                    Animation(
                        y=self._fab_bottom_app_bar_button.y + dp(4),
                        d=self.show_duration,
                        t=self.show_transition,
                    ).start(self._fab_bottom_app_bar_button)

        self.bar_is_hidden = False
        self._animated_show = True
        anim = Animation(
            y=0,
            d=self.show_duration,
            t=self.show_transition,
        )
        anim.bind(on_progress=on_progress, on_complete=on_complete)
        anim.start(self)

    def hide_bar(self) -> None:
        """Hide :class:`~MDBottomAppBar` panel."""

        def on_complete(*args):
            self.dispatch("on_hide_bar")

        def on_progress(animation, instance, progress):
            if (
                progress > 0.5
                and self._animated_hidden
                and widget_icon == instance.icon
            ):
                self._animated_hidden = False
                anim_bar = Animation(
                    y=-self.height,
                    d=self.hide_duration,
                    # t=self.hide_transition,
                )
                anim_bar.bind(on_complete=on_complete)
                anim_bar.start(self)

                if self._fab_bottom_app_bar_button:
                    Animation(
                        y=self._fab_bottom_app_bar_button.y - dp(4),
                        d=self.hide_duration,
                        t=self.hide_transition,
                    ).start(self._fab_bottom_app_bar_button)

        self.bar_is_hidden = True
        self._animated_hidden = True
        len_children = len(self.children)
        widget_icon = ""

        for i, widget in enumerate(self.children):
            if isinstance(widget, MDActionBottomAppBarButton):
                anim = Animation(
                    y=-widget.height,
                    d=self.hide_duration,
                    t=self.hide_transition,
                )
                if i + 2 == len_children:
                    widget_icon = widget.icon
                    anim.bind(on_progress=on_progress)
                Clock.schedule_once(
                    lambda x, y=widget: anim.start(y),
                    i / 10,
                )

    def on_show_bar(self, *args) -> None:
        """
        The method is fired when the :class:`~MDBottomAppBar` panel
        is shown.
        """

    def on_hide_bar(self, *args) -> None:
        """
        The method is fired when the :class:`~MDBottomAppBar` panel
        is hidden.
        """

    def on_scroll_cls(self, instance, scroll_cls) -> None:
        """
        Fired when the value of the :attr:`scroll_cls` attribute changes.
        """

        def on_scroll_cls(*args):
            if not self.allow_hidden:
                Logger.warning(
                    "KivyMD: "
                    "In order for the bottom bar to be automatically hidden "
                    "in addition to the `scroll_cls` parameter, set the value "
                    "of the `allow_hidden` parameter to `True`"
                )

            if issubclass(scroll_cls.__class__, ScrollView):
                if self.allow_hidden:
                    scroll_cls.bind(scroll_y=self.check_scroll_direction)
            else:
                raise TypeError(
                    f"The `scroll_cls` parameter must be an object inherited "
                    f"from the {ScrollView} class"
                )

        Clock.schedule_once(on_scroll_cls)

    def on_size(self, *args) -> None:
        """Fired when the root screen is resized."""

        if self._fab_bottom_app_bar_button:
            self._fab_bottom_app_bar_button.x = Window.width - (dp(56) + dp(16))

    def on_action_items(self, instance, value: list) -> None:
        """
        Fired when the value of the :attr:`action_items` attribute changes.
        """

        def wait_removed(*args):
            if len(self.children) == 1 or not self.children:
                Clock.unschedule(wait_removed)
                self._wait_removed = False
                self._x = -dp(48)
                asynckivy.start(add_widget())

        async def add_widget():
            for button in value:
                await asynckivy.sleep(0)
                self.add_widget(button)

        if self._cache:
            self._cache.append(value)

            for data in self._cache:
                if value[0] in data:
                    for i, widget in enumerate(self.children):
                        if not self._wait_removed:
                            Clock.schedule_interval(wait_removed, 0)
                            self._wait_removed = True
                        if isinstance(widget, MDActionBottomAppBarButton):
                            anim = Animation(
                                y=-widget.height,
                                d=self.hide_duration,
                                t=self.hide_transition,
                            )
                            anim.bind(
                                on_complete=lambda x, y=widget: self.remove_widget(
                                    y
                                )
                            )
                            Clock.schedule_once(
                                lambda x, y=widget: anim.start(y),
                                i / 10,
                            )
        else:
            self._cache.append(value)
            self._current_data = value
            asynckivy.start(add_widget())

    def set_fab_opacity(self, *ars) -> None:
        """
        Sets the transparency value of the:class:`~MDFabBottomAppBarButton`
        button.
        """

        # self._fab_bottom_app_bar_button.opacity = 1

    def set_fab_icon(self, instance, value) -> None:
        """
        Animates the size of the :class:`~MDFabBottomAppBarButton` button.
        """

        # self._fab_bottom_app_bar_button.opacity = 0
        anim = Animation(
            scale_value_x=0,
            scale_value_y=0,
            opacity=0,
            d=self.hide_duration,
            t=self.hide_transition,
        ) + Animation(
            scale_value_x=1,
            scale_value_y=1,
            opacity=1,
            d=self.show_duration,
            t=self.show_transition,
        )
        anim.bind(on_complete=self.set_fab_opacity)
        anim.start(instance)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDActionBottomAppBarButton):
            self._x += widget.width
            widget.pos = (
                self._x + self._padding,
                -dp(48) if self.animation else self.height / 2 - dp(48) / 2,
            )
            widget.opacity = int(not self.animation)
            super().add_widget(widget)
            self.button_centering_animation(widget)
        elif isinstance(widget, MDFabBottomAppBarButton):
            widget.bind(icon=self.set_fab_icon)
            self._fab_bottom_app_bar_button = widget
            Clock.schedule_once(self.set_fab_opacity)
            widget.scale_value_x = int(not self.animation)
            widget.scale_value_y = int(not self.animation)
            widget.pos = (
                Window.width - (dp(56) + self._padding),
                self.height / 2 - dp(56) / 2,
            )
            super().add_widget(widget)
