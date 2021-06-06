"""
Components/Navigation Rail
==========================

.. seealso::

    `Material Design spec, Navigation rail <https://material.io/components/navigation-rail>`_

.. rubric:: Navigation rails provide ergonomic movement between primary destinations in apps.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail.png
    :align: center

Usage
=====

.. code-block:: kv

    MDNavigationRail:

        MDNavigationRailItem:

        MDNavigationRailItem:

        MDNavigationRailItem:

.. code-block:: python

    from kivy.factory import Factory
    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    #:import get_color_from_hex kivy.utils.get_color_from_hex


    <MyTile@SmartTileWithStar>
        size_hint_y: None
        height: "240dp"


    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDNavigationRail"
            md_bg_color: rail.md_bg_color

        MDBoxLayout:

            MDNavigationRail:
                id: rail
                md_bg_color: get_color_from_hex("#344954")
                color_normal: get_color_from_hex("#718089")
                color_active: get_color_from_hex("#f3ab44")

                MDNavigationRailItem:
                    icon: "language-cpp"
                    text: "C++"

                MDNavigationRailItem:
                    icon: "language-python"
                    text: "Python"

                MDNavigationRailItem:
                    icon: "language-swift"
                    text: "Swift"

            MDBoxLayout:
                padding: "24dp"

                ScrollView:

                    MDList:
                        id: box
                        cols: 3
                        spacing: "12dp"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(9):
                tile = Factory.MyTile(source="cpp.png")
                tile.stars = 5
                self.root.ids.box.add_widget(tile)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-usage.png
    :align: center

"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior, HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

Builder.load_string(
    """
#:import StiffScrollEffect kivymd.effects.stiffscroll.StiffScrollEffect


<NavigationRailTitle>
    id: title_box
    padding: "12dp", "8dp", "8dp", "8dp"
    spacing: "16dp"

    MDIconButton:
        id: title_icon
        icon: root.icon
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            root.navigation_rail.rail_state = "open" \
            if root.navigation_rail.rail_state == "close" else "close"

    MDLabel:
        id: lbl_title
        text: root.title
        size_hint: None, None
        -text_size: dp(140), None
        size: dp(140), self.texture_size[1]
        pos_hint: {"center_y": .5}
        opacity: 0
        markup: True

    MDIconButton:
        id: icon_settings
        opacity: 0
        opposite_colors: True
        icon: "cog"
        pos_hint: {"center_y": .5}


<BaseNavigationRailFloatingButton>
    theme_text_color: "Custom"

    canvas.before:
        Color:
            rgba: root.md_bg_color
        RoundedRectangle:
            pos: dp(8), self.y - self._padding_right / 2 + dp(1.5)
            size:
                self.width + self._canvas_width - dp(3), \
                self.height + self._padding_right - dp(3)
            radius: [self.height / 2]

        Color:
            rgba: 1, 1, 1, self._alpha
        Rectangle:
            texture: self._lbl_text.texture
            size: self._lbl_text.texture_size
            pos: self.width + dp(8), self.y + dp(18)


<BaseNavigationRailBoxItem>
    spacing: "8dp"
    padding: "16dp"


<MDNavigationRailItem>
    orientation: "vertical"
    spacing: "12dp"
    adaptive_height: True

    MDIcon:
        id: btn_icon
        icon: root.icon
        font_size: "24dp"
        halign: "center"
        theme_text_color: "Custom"
        text_color:
            root.theme_cls.text_color \
            if not root._color_normal else root._color_normal
        pos_hint: {"center_y": .5}

    MDLabel:
        id: lbl_text
        text: root.text
        size_hint_y: None
        height: self.texture_size[1]
        halign: "center"
        markup: True
        theme_text_color: "Custom"
        text_color:
            btn_icon.text_color \
            if root.navigation_rail.visible == "Persistent" else (0, 0, 0, 0)


<MDNavigationRail>
    orientation: "vertical"
    padding: 0, "8dp", 0, "8dp"
    elevation: root.elevation

    MDBoxLayout:
        id: box_title
        size_hint: None, None
        size: root.width * 2, "56dp"

    ScrollView:
        effect_cls: StiffScrollEffect
        bar_width: 0

        MDList:
            id: box
            spacing: "8dp"
"""
)

__all__ = ("MDNavigationRail",)


class BaseNavigationRailBoxItem(MDBoxLayout):
    """The base class to which the menu items will be added
    (:class:`~MDNavigationRailItem` classes)."""


class BaseNavigationRailFloatingButton(MDFloatingActionButton):
    """Class for a custom MDFloatingActionButton that can stretch."""

    text = StringProperty()
    """
    The text will be placed to the left of the button icon..

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    _canvas_width = NumericProperty(0)
    _alpha = NumericProperty(0)
    _padding_right = NumericProperty(0)
    _lbl_text = MDLabel(markup=True)

    def on_text(self, instance, value):
        self._lbl_text.text = value


class NavigationRailTitle(MDBoxLayout):
    navigation_rail = ObjectProperty()
    """
    `:class:`~kivymd.uix.navigationrail.MDNavigationRail` object.

    :attr:`navigation_rail` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty("menu")
    """
    Icon item.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'blank'`.
    """

    title = StringProperty("Rail")
    """
    Text title.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Rail'`.
    """


class MDNavigationRailItem(
    ThemableBehavior,
    HoverBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    BaseNavigationRailBoxItem,
):
    icon = StringProperty("checkbox-blank")
    """
    Icon item.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank'`.
    """

    text = StringProperty()
    """
    Text item.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    navigation_rail = ObjectProperty()
    """
    `:class:`~kivymd.uix.navigationrail.MDNavigationRail` object.

    :attr:`navigation_rail` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    color_normal = ColorProperty(None)
    """See :attr:`~MDNavigationRail.color_normal` attribute."""

    color_active = ColorProperty(None)
    """See :attr:`~MDNavigationRail.color_active` attribute."""

    _color_normal = ColorProperty(None)
    _color_active = ColorProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._no_ripple_effect = True
        Clock.schedule_once(self.set_width)

    def set_width(self, interval):
        """Sets the size of the menu item."""

        self.size_hint = (None, None)
        self.size = (self.navigation_rail.width, self.navigation_rail.width)

    def on_enter(self):
        if self.navigation_rail.use_hover_behavior:
            Animation(
                md_bg_color=self.theme_cls.bg_darkest
                if not self.navigation_rail.hover_bg
                else self.navigation_rail.hover_bg,
                t=self.navigation_rail.color_transition,
                d=self.navigation_rail.color_change_duration,
            ).start(self)

    def on_leave(self):
        if self.navigation_rail.use_hover_behavior:
            Animation(
                md_bg_color=self.theme_cls.bg_light
                if self.navigation_rail.md_bg_color == self.theme_cls.bg_light
                else self.navigation_rail.md_bg_color,
                t=self.navigation_rail.color_transition,
                d=self.navigation_rail.color_change_duration,
            ).start(self)

    def on_release(self):
        self.navigation_rail.set_color_menu_item(self)
        self.navigation_rail.dispatch("on_item_switch", self)

    def on_visible(self, instance, value):
        if value in ("Selected", "Unlabeled"):
            Clock.schedule_once(self.set_item_label_transparency)

    def set_item_label_transparency(self, interval):
        self.ids.lbl_text.text_color = (0, 0, 0, 0)


class MDNavigationRail(MDCard):
    """
    :Events:
        `on_item_switch`
            Called when the menu item is switched.
        `on_open`
            Called when a rail is opened.
        `on_close`
            Called when a rail is closed.
        `on_action_button`
    """

    use_hover_behavior = BooleanProperty(False)
    """
    Whether to use the HoverBehavior effect for menu items.

    .. code-block:: kv

        MDNavigationRail:
            use_hover_behavior: True
            hover_bg: 0, 0, 0, .2

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-hover-behavior.gif
        :align: center

    :attr:`use_hover_behavior` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    hover_bg = ColorProperty(None)
    """
    The background color for the menu item.
    Used when :attr:`use_hover_behavior` parameter is `True`.
    """

    use_resizeable = BooleanProperty(False)
    """
    Allows you to change the width of the rail (open/close).

    .. code-block:: python

        from kivy.factory import Factory
        from kivy.lang import Builder

        from kivymd.app import MDApp

        KV = '''
        #:import get_color_from_hex kivy.utils.get_color_from_hex


        <MyTile@SmartTileWithStar>
            size_hint_y: None
            height: "240dp"


        MDBoxLayout:
            orientation: "vertical"

            MDToolbar:
                title: "MDNavigationRail"
                md_bg_color: rail.md_bg_color
                left_action_items: [["menu", lambda x: app.rail_open()]]

            MDBoxLayout:

                MDNavigationRail:
                    id: rail
                    md_bg_color: get_color_from_hex("#344954")
                    color_normal: get_color_from_hex("#718089")
                    color_active: get_color_from_hex("#f3ab44")
                    use_resizeable: True

                    MDNavigationRailItem:
                        icon: "language-cpp"
                        text: "C++"

                    MDNavigationRailItem:
                        icon: "language-java"
                        text: "Java"

                    MDNavigationRailItem:
                        icon: "language-swift"
                        text: "Swift"

                MDBoxLayout:
                    padding: "24dp"

                    ScrollView:

                        MDList:
                            id: box
                            cols: 3
                            spacing: "12dp"
        '''


        class Test(MDApp):
            def build(self):
                return Builder.load_string(KV)

            def rail_open(self):
                if self.root.ids.rail.rail_state == "open":
                    self.root.ids.rail.rail_state = "close"
                else:
                    self.root.ids.rail.rail_state = "open"

            def on_start(self):
                for i in range(9):
                    tile = Factory.MyTile(source="kitten.png")
                    tile.stars = 5
                    self.root.ids.box.add_widget(tile)


        Test().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-use-resizeable.gif
        :align: center

    :attr:`use_resizeable` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    use_title = BooleanProperty(False)
    """
    Whether to use an additional panel at the top of the rail.

    .. code-block:: kv

        MDNavigationRail:
            use_resizeable: True
            use_title: True
            icon_title: "logo.png"
            text_title: "[b][color=#ffffff]Example[/color][/b]"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-use-title.gif
        :align: center

    :attr:`use_title` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    icon_title = StringProperty("menu")
    """
    Icon (name or path to `png` file) for :class:`~NavigationRailTitle` class.

    :attr:`icon_title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'menu'`.
    """

    text_title = StringProperty("Rail")
    """
    Text title  for :class:`~NavigationRailTitle` class.

    :attr:`text_title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Rail'`.
    """

    use_action_button = BooleanProperty(False)
    """
    Should :class:`~MDFloatingActionButton` button be used.

    .. code-block:: kv

        MDNavigationRail:
            use_action_button: True
            action_text_button: "COMPOSE"
            on_action_button: print(args)

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-use-action-button.gif
        :align: center

    :attr:`use_action_button` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    action_icon_button = StringProperty("plus")
    """
    Icon of :attr:`~use_action_button`.

    :attr:`action_icon_button` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'plus'`.
    """

    action_text_button = StringProperty()
    """
    Text of :attr:`~use_action_button`.

    :attr:`action_text_button` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    action_color_button = ColorProperty(None)
    """
    Text of :attr:`~use_action_button`.

    :attr:`action_color_button` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_normal = ColorProperty(None)
    """
    Color normal of item menu.

    :attr:`color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_active = ColorProperty(None)
    """
    Color active of item menu.

    :attr:`color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    visible = OptionProperty(
        "Persistent", options=["Selected", "Persistent", "Unlabeled"]
    )
    """
    Item label visible type.
    Available options are: `'Selected'`, `'Persistent'`, `'Unlabeled'`.

    Persistent
    ~~~~~~~~~~

    .. code-block:: kv

        MDNavigationRail:
            visible: "Persistent"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-visible-persistent.gif
        :align: center

    Selected
    ~~~~~~~~

    .. code-block:: kv

        MDNavigationRail:
            visible: "Selected"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-visible-selected.gif
        :align: center

    Unlabeled
    ~~~~~~~~~

    .. code-block:: kv

        MDNavigationRail:
            visible: "Unlabeled"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-rail-visible-unlabeled.gif
        :align: center

    :attr:`visible` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Persistent'`.
    """

    color_transition = StringProperty("linear")
    """
    Animation type when changing the color of a menu item.

    :attr:`color_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    color_change_duration = NumericProperty(0.2)
    """
    Animation duration when changing menu item color.

    :attr:`color_change_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    rail_state = OptionProperty("close", options=("close", "open"))
    """
    Closed or open rails.

    :attr:`rail_state` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.floating_action_button = None
        self.elevation = 0

        self.register_event_type("on_action_button")
        self.register_event_type("on_item_switch")
        self.register_event_type("on_open")
        self.register_event_type("on_close")

        Clock.schedule_once(self.set_items_visible)
        Clock.schedule_once(self.set_width)
        Clock.schedule_once(self.set_action_icon_button)
        Clock.schedule_once(self.set_action_text_button)
        Clock.schedule_once(self.set_box_title_size)
        Clock.schedule_once(self.set_action_color_button)
        Clock.schedule_once(self.set_items_color)

    def anim_color_normal(self, item):
        color = (
            self.theme_cls.text_color
            if not item.color_normal
            else item.color_normal
        )
        Animation(
            _color_normal=color,
            t=self.color_transition,
            d=self.color_change_duration,
        ).start(item)
        if item.visible == "Selected":
            Animation(
                text_color=(0, 0, 0, 0),
                t=self.color_transition,
                d=self.color_change_duration,
            ).start(item.ids.lbl_text)

    def anim_color_active(self, item):
        color = (
            self.theme_cls.primary_color
            if not item.color_active
            else item.color_active
        )
        Animation(
            _color_normal=color,
            t=self.color_transition,
            d=self.color_change_duration,
        ).start(item)
        if item.visible == "Selected":
            item.ids.lbl_text.text_color = item._color_normal
            Animation(
                text_color=color,
                t=self.color_transition,
                d=self.color_change_duration,
            ).start(item.ids.lbl_text)

    def item_switch(self, instance_item):
        instance_item.dispatch("on_release")

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDNavigationRailItem):
            widget.navigation_rail = self
            self.bind(color_normal=widget.setter("color_normal"))
            self.bind(color_normal=widget.setter("_color_normal"))
            self.bind(color_active=widget.setter("color_active"))
            self.ids.box.add_widget(widget)
        else:
            return super().add_widget(widget)

    def open(self):
        def set_opacity_title_component(*args):
            if self.use_title:
                Animation(opacity=1, d=0.2).start(
                    self.ids.box_title.children[0].ids.lbl_title
                )
                Animation(opacity=1, d=0.2).start(
                    self.ids.box_title.children[0].ids.icon_settings
                )

        if self.use_resizeable:
            anim = Animation(width=self.width * 4, d=0.2)
            anim.bind(on_complete=set_opacity_title_component)
            anim.start(self)

            if self.floating_action_button:
                Animation(
                    _canvas_width=self.floating_action_button.width + dp(124),
                    _padding_right=dp(8),
                    _alpha=1,
                    d=0.2,
                ).start(self.floating_action_button)
            self.dispatch("on_open")

    def close(self):
        if self.use_resizeable:
            Animation(width=self.width / 4, d=0.2).start(self)
            if self.use_title:
                Animation(opacity=0, d=0.2).start(
                    self.ids.box_title.children[0].ids.lbl_title
                )
                Animation(opacity=0, d=0.02).start(
                    self.ids.box_title.children[0].ids.icon_settings
                )
            if self.floating_action_button:
                Animation(
                    _canvas_width=0,
                    _padding_right=0,
                    d=0.2,
                    _alpha=0,
                ).start(self.floating_action_button)
            self.dispatch("on_close")

    def on_rail_state(self, instance, value):
        if value == "open":
            self.open()
        elif value == "close":
            self.close()

    def on_item_switch(self, instance_item):
        """Called when the menu item is switched."""

    def on_open(self):
        """Called when a rail is opened."""

    def on_close(self):
        """Called when a rail is closed."""

    def on_action_button(self, floating_action_button):
        """Called when the `MDFloatingActionButton` is pressed."""

    def on_visible(self, instance, value):
        for widget in self.ids.box.children:
            if isinstance(widget, MDNavigationRailItem):
                widget.visible = value

    def on_use_title(self, instance, value):
        def add_title(interval):
            if value:
                self.ids.box_title.add_widget(
                    NavigationRailTitle(
                        navigation_rail=self,
                        icon=self.icon_title,
                        title=self.text_title,
                    )
                )

        Clock.schedule_once(add_title)

    def on_use_resizeable(self, instance, value):
        def add_item(interval):
            if value:
                for widget in self.ids.box.children:
                    if isinstance(widget, MDNavigationRailItem):
                        widget.orientation = "horizontal"
                        self.ids.box.spacing = "24dp"
                        self.use_hover_behavior = False
                        widget._no_ripple_effect = True
                        widget.size_hint_x = None
                        widget.width = self.width * 2

        Clock.schedule_once(add_item)

    def on_use_action_button(self, instance, value):
        if value:
            rail_box = BaseNavigationRailBoxItem(
                size_hint=(None, None),
                width=self.width,
                padding=dp(8),
            )
            self.floating_action_button = BaseNavigationRailFloatingButton(
                pos_hint={"top": 1},
            )
            self.floating_action_button.bind(
                on_release=self.press_floating_action_button
            )
            rail_box.height = self.floating_action_button.height + dp(16)
            rail_box.add_widget(self.floating_action_button)
            self.ids.box.add_widget(rail_box)
            self.ids.box.children.reverse()

    def press_floating_action_button(self, floating_action_button):
        self.dispatch("on_action_button", floating_action_button)

    def set_action_color_button(self, interval):
        if self.floating_action_button and self.action_color_button:
            self.floating_action_button.md_bg_color = self.action_color_button

    def set_width(self, interval):
        self.size_hint_x = None
        self.width = dp(72)

    def set_box_title_size(self, interval):
        if not self.use_title:
            self.remove_widget(self.ids.box_title)

    def set_action_icon_button(self, interval):
        if self.floating_action_button:
            self.floating_action_button.icon = self.action_icon_button

    def set_action_text_button(self, interval):
        if self.floating_action_button:
            self.floating_action_button.text = self.action_text_button

    def set_color_menu_item(self, instance_item):
        for item in self.ids.box.children:
            if isinstance(item, MDNavigationRailItem):
                if instance_item is item:
                    self.anim_color_active(item)
                else:
                    self.anim_color_normal(item)

    def set_items_color(self, interval):
        if not self.color_normal:
            self.color_normal = self.theme_cls.text_color
        if not self.color_active:
            self.color_active = self.theme_cls.bg_light

    def set_items_visible(self, interval):
        # If the user does not set the `visible` parameter.
        if self.visible == "Persistent":
            for widget in self.ids.box.children:
                if isinstance(widget, MDNavigationRailItem):
                    widget.visible = "Persistent"
