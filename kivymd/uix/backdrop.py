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

    <Root>:

        MDBackdrop:

            MDBackdropBackLayer:

                ContentForBackdropBackLayer:

            MDBackdropFrontLayer:

                 ContentForBackdropFrontLayer:

Example
-------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.screenmanager import Screen

    from kivymd.app import MDApp

    # Your layouts.
    Builder.load_string(
        '''
    #:import Window kivy.core.window.Window
    #:import IconLeftWidget kivymd.uix.list.IconLeftWidget
    #:import images_path kivymd.images_path


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
        source: f"{images_path}/kivymd_logo.png"
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
            header_text: "Menu:"

            MDBackdropBackLayer:
                MyBackdropBackLayer:
                    id: backlayer

            MDBackdropFrontLayer:
                MyBackdropFrontLayer:
                    backdrop: backdrop
    '''
    )


    class ExampleBackdrop(Screen):
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

.. Note:: `See full example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Backdrop>`_
"""

__all__ = (
    "MDBackdropToolbar",
    "MDBackdropFrontLayer",
    "MDBackdropBackLayer",
    "MDBackdrop",
)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar

Builder.load_string(
    """
<MDBackdrop>

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_color if not root.background_color \
                else root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

    MDBackdropToolbar:
        id: toolbar
        title: root.title
        elevation: 0
        md_bg_color:
            root.theme_cls.primary_color if not root.background_color \
            else root.background_color
        left_action_items: root.left_action_items
        right_action_items: root.right_action_items
        pos_hint: {'top': 1}

    _BackLayer:
        id: back_layer
        y: -toolbar.height
        padding: 0, 0, 0, toolbar.height + dp(10)

    _FrontLayer:
        id: _front_layer
        md_bg_color: 0, 0, 0, 0
        orientation: "vertical"
        size_hint_y: None
        height: root.height - toolbar.height
        padding: root.padding

        canvas:
            Color:
                rgba: root.theme_cls.bg_normal
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius:
                    [
                    (root.radius, root.radius),
                    (0, 0),
                    (0, 0),
                    (0, 0)
                    ]

        OneLineListItem:
            id: header_button
            text: root.header_text
            divider: None
            _no_ripple_effect: True
            on_press: root.open()

        BoxLayout:
            id: front_layer
            padding: 0, 0, 0, "10dp"
"""
)


class MDBackdrop(ThemableBehavior, FloatLayout):
    """
    :Events:
        :attr:`on_open`
            When the front layer drops.
        :attr:`on_close`
            When the front layer rises.
    """

    padding = ListProperty([0, 0, 0, 0])
    """Padding for contents of the front layer.

    :attr:`padding` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    left_action_items = ListProperty()
    """The icons and methods left of the :class:`kivymd.uix.toolbar.MDToolbar`
    in back layer. For more information, see the :class:`kivymd.uix.toolbar.MDToolbar` module
    and :attr:`left_action_items` parameter.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """See the :class:`kivymd.uix.toolbar.MDToolbar.title` parameter.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    background_color = ListProperty()
    """Background color of back layer.

    :attr:`background_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    radius = NumericProperty(25)
    """The value of the rounding radius of the upper left corner
    of the front layer.

    :attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `25`.
    """

    header = BooleanProperty(True)
    """Whether to use a header above the contents of the front layer.

    :attr:`header` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    header_text = StringProperty("Header")
    """Text of header.

    :attr:`header_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Header'`.
    """

    close_icon = StringProperty("close")
    """The name of the icon that will be installed on the toolbar
    on the left when opening the front layer.

    :attr:`close_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'close'`.
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

    def on_open(self):
        """When the front layer drops."""

    def on_close(self):
        """When the front layer rises."""

    def on_left_action_items(self, instance, value):
        if value:
            self.left_action_items = [value[0]]
        else:
            self.left_action_items = [["menu", lambda x: self.open()]]
        self._open_icon = self.left_action_items[0][0]

    def on_header(self, instance, value):
        if not value:
            self.ids._front_layer.remove_widget(self.ids.header_button)

    def open(self, open_up_to=0):
        """
        Opens the front layer.

        :open_up_to:
            the height to which the front screen will be lowered;
            if equal to zero - falls to the bottom of the screen;
        """

        self.animtion_icon_menu()
        if self._front_layer_open:
            self.close()
            return
        if open_up_to:
            y = open_up_to
        else:
            y = dp(120) - self.height
        Animation(y=y, d=0.2, t="out_quad").start(self.ids._front_layer)
        self._front_layer_open = True
        self.dispatch("on_open")

    def close(self):
        """Opens the front layer."""

        Animation(y=0, d=0.2, t="out_quad").start(self.ids._front_layer)
        self._front_layer_open = False
        self.dispatch("on_close")

    def animtion_icon_menu(self):
        icon_menu = self.ids.toolbar.ids.left_actions.children[0]
        anim = Animation(opacity=0, d=0.2, t="out_quad")
        anim.bind(on_complete=self.animtion_icon_close)
        anim.start(icon_menu)

    def animtion_icon_close(self, instance_animation, instance_icon_menu):
        instance_icon_menu.icon = (
            self.close_icon
            if instance_icon_menu.icon == self._open_icon
            else self._open_icon
        )
        Animation(opacity=1, d=0.2).start(instance_icon_menu)

    def add_widget(self, widget, index=0, canvas=None):
        if widget.__class__ in (MDBackdropToolbar, _BackLayer, _FrontLayer):
            return super().add_widget(widget)
        else:
            if widget.__class__ is MDBackdropBackLayer:
                self.ids.back_layer.add_widget(widget)
            elif widget.__class__ is MDBackdropFrontLayer:
                self.ids.front_layer.add_widget(widget)


class MDBackdropToolbar(MDToolbar):
    pass


class MDBackdropFrontLayer(BoxLayout):
    pass


class MDBackdropBackLayer(BoxLayout):
    pass


class _BackLayer(BoxLayout):
    pass


class _FrontLayer(MDCard):
    pass
