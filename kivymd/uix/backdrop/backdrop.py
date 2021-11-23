"""
Components/Backdrop
===================

.. seealso::

    `Material Design spec, Backdrop <https://material.io/components/backdrop>`_

.. rubric:: Skeleton layout for using :class:`~MDBackdrop`:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/backdrop.png
    :align: center

Usage
-----

.. code-block:: kv

    <Root>

        MDBackdrop:

            MDBackdropBackLayer:

                ContentForBackdropBackLayer:

            MDBackdropFrontLayer:

                 ContentForBackdropFrontLayer:

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.uix.screen import MDScreen
    from kivymd.app import MDApp

    # Your layouts.
    Builder.load_string(
        '''
    #:import Window kivy.core.window.Window
    #:import IconLeftWidget kivymd.uix.list.IconLeftWidget


    <ItemBackdropFrontLayer@TwoLineAvatarListItem>
        icon: "android"

        IconLeftWidget:
            icon: root.icon


    <MyBackdropFrontLayer@ItemBackdropFrontLayer>
        backdrop: None
        text: "Lower the front layer"
        secondary_text: " by 50 %"
        icon: "transfer-down"
        on_press: root.backdrop.open(-Window.height / 2)
        pos_hint: {"top": 1}
        _no_ripple_effect: True


    <MyBackdropBackLayer@Image>
        size_hint: .8, .8
        source: "data/logo/kivy-icon-512.png"
        pos_hint: {"center_x": .5, "center_y": .6}
    '''
    )

    # Usage example of MDBackdrop.
    Builder.load_string(
        '''
    <ExampleBackdrop>

        MDBackdrop:
            id: backdrop
            left_action_items: [['menu', lambda x: self.open()]]
            title: "Example Backdrop"
            radius_left: "25dp"
            radius_right: "0dp"
            header_text: "Menu:"

            MDBackdropBackLayer:
                MyBackdropBackLayer:
                    id: backlayer

            MDBackdropFrontLayer:
                MyBackdropFrontLayer:
                    backdrop: backdrop
    '''
    )


    class ExampleBackdrop(MDScreen):
        pass


    class TestBackdrop(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def build(self):
            return ExampleBackdrop()


    TestBackdrop().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/backdrop.gif
    :width: 280 px
    :align: center

.. Note:: `See full example <https://github.com/kivymd/KivyMD/wiki/Components-Backdrop>`_
"""

__all__ = (
    "MDBackdropToolbar",
    "MDBackdropFrontLayer",
    "MDBackdropBackLayer",
    "MDBackdrop",
)

import os
from typing import NoReturn, Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDActionTopAppBarButton, MDToolbar

with open(
    os.path.join(uix_path, "backdrop", "backdrop.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDBackdrop(ThemableBehavior, MDFloatLayout):
    """
    :Events:
        :attr:`on_open`
            When the front layer drops.
        :attr:`on_close`
            When the front layer rises.
    """

    padding = ListProperty([0, 0, 0, 0])
    """
    Padding for contents of the front layer.

    :attr:`padding` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    left_action_items = ListProperty()
    """
    The icons and methods left of the :class:`kivymd.uix.toolbar.MDToolbar`
    in back layer. For more information, see the
    :class:`kivymd.uix.toolbar.MDToolbar` module
    and :attr:`left_action_items` parameter.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """
    Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """
    See the :class:`kivymd.uix.toolbar.MDToolbar.title` parameter.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    back_layer_color = ColorProperty(None)
    """
    Background color of back layer.

    :attr:`back_layer_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    front_layer_color = ColorProperty(None)
    """
    Background color of front layer.

    :attr:`front_layer_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius_left = NumericProperty("16dp")
    """
    The value of the rounding radius of the upper left corner
    of the front layer.

    :attr:`radius_left` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `16dp`.
    """

    radius_right = NumericProperty("16dp")
    """
    The value of the rounding radius of the upper right corner
    of the front layer.

    :attr:`radius_right` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `16dp`.
    """

    header = BooleanProperty(True)
    """
    Whether to use a header above the contents of the front layer.

    :attr:`header` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    header_text = StringProperty("Header")
    """
    Text of header.

    :attr:`header_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Header'`.
    """

    close_icon = StringProperty("close")
    """
    The name of the icon that will be installed on the toolbar
    on the left when opening the front layer.

    :attr:`close_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'close'`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'open'`.

    .. versionadded:: 1.0.0

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    opening_transition = StringProperty("out_quad")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    .. versionadded:: 1.0.0

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    closing_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'close'`.

    .. versionadded:: 1.0.0

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_transition = StringProperty("out_quad")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    .. versionadded:: 1.0.0

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    _open_icon = ""
    _front_layer_open = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")
        Clock.schedule_once(
            lambda x: self.on_left_action_items(self, self.left_action_items)
        )

    def on_open(self) -> NoReturn:
        """When the front layer drops."""

    def on_close(self) -> NoReturn:
        """When the front layer rises."""

    def on_left_action_items(self, instance_backdrop, menu: list) -> NoReturn:
        if menu:
            self.left_action_items = [menu[0]]
        else:
            self.left_action_items = [["menu", lambda x: self.open()]]
        self._open_icon = self.left_action_items[0][0]

    def on_header(self, instance_backdrop, value: bool) -> NoReturn:
        if not value:
            self.ids._front_layer.remove_widget(self.ids.header_button)

    def open(self, open_up_to: int = 0) -> NoReturn:
        """
        Opens the front layer.

        :open_up_to:
            the height to which the front screen will be lowered;
            if equal to zero - falls to the bottom of the screen;
        """

        self.animate_opacity_icon()
        if self._front_layer_open:
            self.close()
            return

        if open_up_to:
            if open_up_to < (
                self.ids.header_button.height - self.ids._front_layer.height
            ):
                y = self.ids.header_button.height - self.ids._front_layer.height
            elif open_up_to > 0:
                y = 0
            else:
                y = open_up_to
        else:
            y = self.ids.header_button.height - self.ids._front_layer.height

        Animation(y=y, d=self.opening_time, t=self.opening_transition).start(
            self.ids._front_layer
        )
        self._front_layer_open = True
        self.dispatch("on_open")

    def close(self) -> NoReturn:
        """Opens the front layer."""

        Animation(y=0, d=self.closing_time, t=self.closing_transition).start(
            self.ids._front_layer
        )
        self._front_layer_open = False
        self.dispatch("on_close")

    def animate_opacity_icon(
        self,
        instance_icon_menu: Union[MDActionTopAppBarButton, None] = None,
        opacity_value: int = 0,
        call_set_new_icon: bool = True,
    ) -> NoReturn:
        """Starts the opacity animation of the icon."""

        if not instance_icon_menu:
            instance_icon_menu = self.ids.toolbar.ids.left_actions.children[0]
        anim = Animation(
            opacity=opacity_value,
            d=self.opening_time,
            t=self.opening_transition,
        )
        if call_set_new_icon:
            anim.bind(on_complete=self.set_new_icon)
        anim.start(instance_icon_menu)

    def set_new_icon(
        self,
        instance_animation: Animation,
        instance_icon_menu: MDActionTopAppBarButton,
    ) -> NoReturn:
        """
        Sets the icon of the button depending on the state of the backdrop.
        """

        instance_icon_menu.icon = (
            self.close_icon
            if instance_icon_menu.icon == self._open_icon
            else self._open_icon
        )
        self.animate_opacity_icon(instance_icon_menu, 1, False)

    def add_widget(self, widget, index=0, canvas=None):
        if widget.__class__ in (MDBackdropToolbar, _BackLayer, _FrontLayer):
            return super().add_widget(widget)
        else:
            if widget.__class__ is MDBackdropBackLayer:
                self.ids.back_layer.add_widget(widget)
            elif widget.__class__ is MDBackdropFrontLayer:
                self.ids.front_layer.add_widget(widget)


class MDBackdropToolbar(MDToolbar):
    """Implements a toolbar for back content."""


class MDBackdropFrontLayer(BoxLayout):
    """Container for front content."""


class MDBackdropBackLayer(BoxLayout):
    """Container for back content."""


class _BackLayer(BoxLayout):
    pass


class _FrontLayer(MDCard, FakeRectangularElevationBehavior):
    pass
