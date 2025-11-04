"""
Components/SliverAppbar
=======================

.. versionadded:: 1.0.0

.. rubric:: MDSliverAppbar is a Material Design widget in KivyMD which gives
    scrollable or collapsible
    `MDTopAppBar <https://kivymd.readthedocs.io/en/latest/components/appbar/>`_

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-appbar-preview.gif
    :align: center

.. note:: This widget is a modification of the
    `silverappbar.py <https://github.com/kivymd-extensions/akivymd/blob/main/kivymd_extensions/akivymd/uix/silverappbar.py>`_ module.

Usage
-----

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            MDScreen:

                MDSliverAppbar:

                    MDTopAppBar:
                        [...]

                    MDSliverAppbarHeader:

                        # Custom content.
                        [...]

                    # Custom list.
                    MDSliverAppbarContent:

    .. tab:: Declarative Python style

        .. code-block:: python

            MDScreen(
                MDSliverAppbar(
                    MDTopAppBar(
                        [...]
                    ),
                    MDSliverAppbarHeader(
                        # Custom content.
                        [...]
                    ),
                    MDSliverAppbarContent(
                        # Custom list.
                        [...]
                    ),
                )
            )

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-appbar-anatomy.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.list import MDListItem

            KV = '''
            <GuitarItem>
                theme_bg_color: "Custom"
                md_bg_color: "2d4a50"

                MDListItemLeadingAvatar
                    source: "avatar.png"

                MDListItemHeadlineText:
                    text: "Ibanez"

                MDListItemSupportingText:
                    text: "GRG121DX-BKF"

                MDListItemTertiaryText:
                    text: "$445,99"

                MDListItemTrailingIcon:
                    icon: "guitar-electric"


            MDScreen:

                MDSliverAppbar:
                    background_color: "2d4a50"
                    hide_appbar: True

                    MDTopAppBar:
                        type: "medium"

                        MDTopAppBarLeadingButtonContainer:

                            MDActionTopAppBarButton:
                                icon: "arrow-left"

                        MDTopAppBarTitle:
                            text: "Sliver toolbar"

                        MDTopAppBarTrailingButtonContainer:

                            MDActionTopAppBarButton:
                                icon: "attachment"

                            MDActionTopAppBarButton:
                                icon: "calendar"

                            MDActionTopAppBarButton:
                                icon: "dots-vertical"

                    MDSliverAppbarHeader:

                        FitImage:
                            source: "bg.jpg"

                    MDSliverAppbarContent:
                        id: content
                        orientation: "vertical"
                        padding: "12dp"
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
            '''


            class GuitarItem(MDListItem):
                ...


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)

                def on_start(self):
                    for x in range(10):
                        self.root.ids.content.add_widget(GuitarItem())


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.appbar import (
                MDTopAppBar,
                MDTopAppBarLeadingButtonContainer,
                MDActionTopAppBarButton,
                MDTopAppBarTitle,
                MDTopAppBarTrailingButtonContainer,
            )
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.list import (
                MDListItem,
                MDListItemLeadingAvatar,
                MDListItemHeadlineText,
                MDListItemSupportingText,
                MDListItemTertiaryText,
                MDListItemTrailingIcon,
            )
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.sliverappbar import (
                MDSliverAppbar,
                MDSliverAppbarHeader,
                MDSliverAppbarContent,
            )


            class GuitarItem(MDListItem):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.theme_bg_color = "Custom"
                    self.md_bg_color = "2d4a50"
                    self.widgets = [
                        MDListItemLeadingAvatar(source="avatar.png"),
                        MDListItemHeadlineText(text="Ibanez"),
                        MDListItemSupportingText(text="GRG121DX-BKF"),
                        MDListItemTertiaryText(text="$445,99"),
                        MDListItemTrailingIcon(icon="guitar-electric"),
                    ]


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return MDScreen(
                        MDSliverAppbar(
                            MDTopAppBar(
                                MDTopAppBarLeadingButtonContainer(
                                    MDActionTopAppBarButton(
                                        icon="arrow-left",
                                    ),
                                ),
                                MDTopAppBarTitle(
                                    text="Sliver toolbar",
                                ),
                                MDTopAppBarTrailingButtonContainer(
                                    MDActionTopAppBarButton(
                                        icon="attachment",
                                    ),
                                    MDActionTopAppBarButton(
                                        icon="calendar",
                                    ),
                                    MDActionTopAppBarButton(
                                        icon="dots-vertical",
                                    ),
                                ),
                                type="medium",
                            ),
                            MDSliverAppbarHeader(
                                FitImage(
                                    source="bg.jpg",
                                ),
                            ),
                            MDSliverAppbarContent(
                                id="content",
                                orientation="vertical",
                                padding="12dp",
                                theme_bg_color="Custom",
                                md_bg_color="2d4a50",
                            ),
                            background_color="2d4a50",
                            hide_appbar=True,
                        )
                    )

                def on_start(self):
                    for x in range(10):
                        self.root.get_ids().content.add_widget(GuitarItem())


            Example().run()

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    #:import SliverToolbar __main__.SliverToolbar

    Root:

        MDSliverAppbar:
            [...]

            MDSliverAppbarHeader:

                [...]

            MDSliverAppbarContent:
                [...]

.. code-block:: python

    class SliverToolbar(MDTopAppBar):
        [...]

2.0.0 version
-------------

.. code-block:: kv

    Root:

        MDSliverAppbar:
            [...]

            MDTopAppBar:
                [...]

            MDSliverAppbarHeader:

                [...]

            MDSliverAppbarContent:
                [...]
"""

__all__ = ("MDSliverAppbar", "MDSliverAppbarHeader", "MDSliverAppbarContent")

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    VariableListProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.appbar import MDTopAppBar
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.boxlayout import MDBoxLayout

with open(
    os.path.join(uix_path, "sliverappbar", "sliverappbar.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDSliverAppbarException(Exception):
    pass


class MDSliverAppbarContent(MDBoxLayout):
    """
    Implements a box for a scrollable list of custom items.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.
    """


class MDSliverAppbarHeader(DeclarativeBehavior, BoxLayout):
    """
    Sliver app bar header class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDSliverAppbar(DeclarativeBehavior, ThemableBehavior, BoxLayout):
    """
    Sliver appbar class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.

    :Events:
        :attr:`on_scroll_content`
            Fired when the list of custom content is being scrolled.
    """

    background_color = ColorProperty(None)
    """
    Background color of appbar in (r, g, b, a) or string format.

    :attr:`background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    max_height = NumericProperty(Window.height / 2)
    """
    Distance from top of screen to start of custom list content.

    .. code-block:: kv

        MDSliverAppbar:
            max_height: "200dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-appbar-max-height.png
        :align: center

    :attr:`max_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `Window.height / 2`.
    """

    hide_appbar = BooleanProperty(None)
    """
    Whether to hide the appbar when scrolling through a list
    of custom content.

    .. versionchanged:: 2.0.0

        Rename `hide_toolbar` to `hide_appbar` attribute.

    .. code-block:: kv

        MDSliverAppbar:
            hide_appbar: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-appbar-hide-appbar-false.gif
        :align: center

    .. code-block:: kv

        MDSliverAppbar:
            hide_appbar: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-appbar-hide-appbar-true.gif
        :align: center

    :attr:`hide_appbar` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([20], length=4)
    """
    Box radius for custom item list.

    .. code-block:: kv

        MDSliverAppbar:
            radius: 20

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[20]`.
    """

    max_opacity = NumericProperty(1)
    """
    Maximum background transparency value for the
    :class:`~kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbarHeader` class.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-opacity.gif
        :align: center

    .. code-block:: kv

        MDSliverAppbar:
            max_opacity: .5

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-opacity-05.gif
        :align: center

    :attr:`max_opacity` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    _opacity = NumericProperty()
    _scroll_was_moving = BooleanProperty(False)
    _last_scroll_y_pos = 0.0
    _appbar = ObjectProperty()

    __events__ = ("on_scroll_content",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_hide_appbar(self, instance, value) -> None:
        """Fired when the `hide_appbar` value changes."""

        if not value:
            self.background_color = self.theme_cls.transparentColor

    def on_scroll_content(
        self,
        instance: object = None,
        value: float = 1.0,
        direction: str = "up",
    ):
        """
        Fired when the list of custom content is being scrolled.

        :param instance: :class:`~MDSliverAppbar`
        :param value: see :attr:`~kivy.uix.scrollview.ScrollView.scroll_y`
        :param direction: scroll direction: 'up/down'
        """

    def on_background_color(self, instance, color) -> None:
        """Fired when the `background_color` value changes."""

        if self._appbar:
            self._appbar.canvas.get_group("md-top-app-bar-color")[
                0
            ].rgba = color

    def on_vbar(self) -> None:
        if not self.background_color:
            self.background_color = self.theme_cls.primaryColor

        scroll_box = self.ids.scroll_box
        vbar = self.ids.scroll.vbar
        appbar_percent = (self._appbar.height / scroll_box.height) * 100
        current_percent = (vbar[0] + vbar[1]) * 100
        percent_min = (
            1 - self.max_height / scroll_box.height
        ) * 100 + appbar_percent

        if self._scroll_was_moving:
            direction = self._get_direction_swipe(self.ids.scroll.scroll_y)
            self._last_scroll_y_pos = self.ids.scroll.scroll_y
            self.dispatch(
                "on_scroll_content", self.ids.scroll.scroll_y, direction
            )

        if self.hide_appbar:
            if percent_min <= current_percent:
                opacity = (current_percent - percent_min) / (100 - percent_min)
                self._opacity = self.max_opacity * (1 - opacity)
                self.background_color = self.background_color[0:3] + [
                    1 - opacity
                ]
            else:
                self.background_color = self.background_color[0:3] + [1]

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDSliverAppbarContent):
            Clock.schedule_once(lambda x: self._set_radius(widget))
            self.ids.scroll_box.add_widget(widget)
        elif isinstance(widget, MDSliverAppbarHeader):
            self.ids.header.add_widget(widget)
        elif isinstance(widget, MDTopAppBar):
            self._appbar = widget
            widget.pos_hint = {"top": 1}
            self.ids.float_box.add_widget(widget)
        else:
            super().add_widget(widget, index=index, canvas=canvas)

    def on__appbar(self, instance, value):
        def set_rgba_appbar(*args):
            if self.hide_appbar:
                value.theme_elevation_level = "Custom"
                value.elevation_level = 0
                value.theme_shadow_color = "Custom"
                value.shadow_color = self.theme_cls.transparentColor
                value.md_bg_color = self.theme_cls.transparentColor
                value.canvas.get_group("md-top-app-bar-color")[
                    0
                ].rgba = self.theme_cls.transparentColor

        Clock.schedule_once(set_rgba_appbar, 0.5)

    def _set_radius(self, instance: MDSliverAppbarContent):
        instance.radius = self.radius

    def _get_direction_swipe(self, current_percent: float):
        if self._last_scroll_y_pos > current_percent:
            direction = "up"
        else:
            direction = "down"
        return direction
