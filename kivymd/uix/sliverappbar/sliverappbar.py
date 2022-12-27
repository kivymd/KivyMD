"""
Components/SliverAppbar
=======================

.. versionadded:: 1.0.0

.. rubric:: MDSliverAppbar is a Material Design widget in KivyMD which gives
    scrollable or collapsible
    `MDTopAppBar <https://kivymd.readthedocs.io/en/latest/components/toolbar/>`_

.. note:: This widget is a modification of the
    `silverappbar.py <https://github.com/kivymd-extensions/akivymd/blob/main/kivymd_extensions/akivymd/uix/silverappbar.py>`_ module.

Usage
-----

.. code-block:: kv

    MDScreen:

        MDSliverAppbar:

            MDSliverAppbarHeader:

                # Custom content.
                ...

            # Custom list.
            MDSliverAppbarContent:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-usage.png
    :align: center

Example
-------

.. code-block:: python

    from kivy.lang.builder import Builder

    from kivymd.app import MDApp
    from kivymd.uix.card import MDCard

    KV = '''
    <CardItem>
        size_hint_y: None
        height: "86dp"
        padding: "4dp"
        radius: 12

        FitImage:
            source: "avatar.jpg"
            radius: root.radius
            size_hint_x: None
            width: root.height

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            spacing: "6dp"
            padding: "12dp", 0, 0, 0
            pos_hint: {"center_y": .5}

            MDLabel:
                text: "Title text"
                font_style: "H5"
                bold: True
                adaptive_height: True

            MDLabel:
                text: "Subtitle text"
                theme_text_color: "Hint"
                adaptive_height: True


    MDScreen:

        MDSliverAppbar:
            background_color: "2d4a50"

            MDSliverAppbarHeader:

                MDRelativeLayout:

                    FitImage:
                        source: "bg.jpg"

            MDSliverAppbarContent:
                id: content
                orientation: "vertical"
                padding: "12dp"
                spacing: "12dp"
                adaptive_height: True
    '''


    class CardItem(MDCard):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.elevation = 1


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for x in range(10):
                self.root.ids.content.add_widget(CardItem())


    Example().run()
"""


__all__ = ("MDSliverAppbar", "MDSliverAppbarHeader", "MDSliverAppbarContent")

import os
from typing import Union

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

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar

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

    md_bg_color = ColorProperty([0, 0, 0, 0])
    """
    See :attr:`~kivymd.uix.sliverappbar.sliverappbar.MDSliverAppbar.background_color`.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_bg_color)

    def set_bg_color(self, interval: Union[int, float]) -> None:
        if self.md_bg_color == [0, 0, 0, 0]:
            self.md_bg_color = self.theme_cls.bg_normal


class MDSliverAppbarHeader(MDBoxLayout):
    """
    Sliver app bar header class.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.
    """


class MDSliverAppbar(MDBoxLayout):
    """
    Sliver app bar class.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` class documentation.

    :Events:
        :attr:`on_scroll_content`
            Called when the list of custom content is being scrolled.
    """

    toolbar_cls = ObjectProperty()
    """
    Must be an object of the :class:`~kivymd.uix.toolbar.toolbar.MDTopAppBar' class.
    See :class:`~kivymd.uix.toolbar.toolbar.MDTopAppBar` class documentation
    for more information.

    By default, MDSliverAppbar widget uses the MDTopAppBar class with no
    parameters.

    .. code-block:: python

        from kivy.lang.builder import Builder

        from kivymd.uix.card import MDCard
        from kivymd.uix.toolbar import MDTopAppBar

        KV = '''
        #:import SliverToolbar __main__.SliverToolbar


        <CardItem>
            size_hint_y: None
            height: "86dp"
            padding: "4dp"
            radius: 12

            FitImage:
                source: "avatar.jpg"
                radius: root.radius
                size_hint_x: None
                width: root.height

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "6dp"
                padding: "12dp", 0, 0, 0
                pos_hint: {"center_y": .5}

                MDLabel:
                    text: "Title text"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True

                MDLabel:
                    text: "Subtitle text"
                    theme_text_color: "Hint"
                    adaptive_height: True


        MDScreen:

            MDSliverAppbar:
                background_color: "2d4a50"
                toolbar_cls: SliverToolbar()

                MDSliverAppbarHeader:

                    MDRelativeLayout:

                        FitImage:
                            source: "bg.jpg"

                MDSliverAppbarContent:
                    id: content
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "12dp"
                    adaptive_height: True
        '''


        class CardItem(MDCard):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.elevation = 1


        class SliverToolbar(MDTopAppBar):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.shadow_color = (0, 0, 0, 0)
                self.type_height = "medium"
                self.headline_text = "Headline medium"
                self.left_action_items = [["arrow-left", lambda x: x]]
                self.right_action_items = [
                    ["attachment", lambda x: x],
                    ["calendar", lambda x: x],
                    ["dots-vertical", lambda x: x],
                ]


        class Example(MDApp):
            def build(self):
                self.theme_cls.material_style = "M3"
                return Builder.load_string(KV)

            def on_start(self):
                for x in range(10):
                    self.root.ids.content.add_widget(CardItem())


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-toolbar-cls.gif
        :align: center

    :attr:`toolbar_cls` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    background_color = ColorProperty(None)
    """
    Background color of toolbar in (r, g, b, a) or string format.

    .. code-block:: kv

        MDSliverAppbar:
            background_color: "2d4a50"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-background-color.png
        :align: center

    :attr:`background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    max_height = NumericProperty(Window.height / 2)
    """
    Distance from top of screen to start of custom list content.

    .. code-block:: kv

        MDSliverAppbar:
            max_height: "200dp"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-max-height.png
        :align: center

    :attr:`max_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `Window.height / 2`.
    """

    hide_toolbar = BooleanProperty(True)
    """
    Whether to hide the toolbar when scrolling through a list
    of custom content.

    .. code-block:: kv

        MDSliverAppbar:
            hide_toolbar: False

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-hide-toolbar.gif
        :align: center

        MDSliverAppbar:
            hide_toolbar: True

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/sliver-app-bar-hide-toolbar-true.gif
        :align: center

    :attr:`hide_toolbar` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_scroll_content")

    def on_scroll_content(
        self,
        instance_sliverappbar: object = None,
        value: float = 1.0,
        direction: str = "up",
    ):
        """
        Called when the list of custom content is being scrolled.

        :param instance_sliverappbar: :class:`~MDSliverAppbar`
        :param value: see :attr:`~kivy.uix.scrollview.ScrollView.scroll_y`
        :param direction: scroll direction: 'up/down'
        """

    def on_background_color(
        self, instance_sliver_appbar, color_value: list
    ) -> None:
        if self.toolbar_cls:
            self.toolbar_cls.md_bg_color = color_value

    def on_toolbar_cls(
        self, instance_sliver_appbar, instance_toolbar_cls: MDTopAppBar
    ) -> None:
        """Called when a value is set to the :attr:`toolbar_cls` parameter."""

        def on_toolbar_cls(*args):
            # If an MDTopAppBar object is already in use, delete it
            # before adding a new MDTopAppBar object.
            for widget in self.ids.float_box.children:
                if issubclass(widget.__class__, MDTopAppBar):
                    self.ids.float_box.remove_widget(widget)

            # Adding a custom MDTopAppBar object.
            if issubclass(instance_toolbar_cls.__class__, MDTopAppBar):
                instance_toolbar_cls.pos_hint = {"top": 1}
                instance_toolbar_cls.elevation = 0
                self.ids.float_box.add_widget(instance_toolbar_cls)
            else:
                raise MDSliverAppbarException(
                    "The `toolbar_cls` parameter must be an object of the "
                    "`kivymd.uix.toolbar.MDTopAppBar class`"
                )

        # Schedule using for declarative style.
        # Otherwise get AttributeError exception.
        Clock.schedule_once(on_toolbar_cls)

    def on_vbar(self) -> None:
        if not self.background_color:
            self.background_color = self.theme_cls.primary_color

        if not self.toolbar_cls:
            self.toolbar_cls = self.get_default_toolbar()

        scroll_box = self.ids.scroll_box
        vbar = self.ids.scroll.vbar
        toolbar_percent = (self.toolbar_cls.height / scroll_box.height) * 100
        current_percent = (vbar[0] + vbar[1]) * 100
        percent_min = (
            1 - self.max_height / scroll_box.height
        ) * 100 + toolbar_percent

        if self._scroll_was_moving:
            direction = self._get_direction_swipe(self.ids.scroll.scroll_y)
            self._last_scroll_y_pos = self.ids.scroll.scroll_y
            self.dispatch(
                "on_scroll_content", self.ids.scroll.scroll_y, direction
            )

        if self.hide_toolbar:
            if percent_min <= current_percent:
                opacity = (current_percent - percent_min) / (100 - percent_min)
                self._opacity = self.max_opacity * (1 - opacity)
                self.background_color = self.background_color[0:3] + [
                    1 - opacity
                ]
                self.toolbar_cls._hard_shadow_a = 1 - opacity
                self.toolbar_cls._soft_shadow_a = 1 - opacity
            else:
                self.background_color = self.background_color[0:3] + [1]

    def get_default_toolbar(self) -> MDTopAppBar:
        """Called if no value is passed for the toolbar_cls attribute."""

        return MDTopAppBar(
            pos_hint={"top": 1}, md_bg_color=self.background_color
        )

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, MDSliverAppbarContent):
            Clock.schedule_once(lambda x: self._set_radius(widget))
            self.ids.scroll_box.add_widget(widget)
        elif issubclass(widget.__class__, MDSliverAppbarHeader):
            self.ids.header.add_widget(widget)
        else:
            super().add_widget(widget, index=index, canvas=canvas)

    def _set_radius(self, instance: MDSliverAppbarContent) -> None:
        instance.radius = self.radius

    def _get_direction_swipe(self, current_percent: float) -> str:
        if self._last_scroll_y_pos > current_percent:
            direction = "up"
        else:
            direction = "down"
        return direction
