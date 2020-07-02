"""
Components/Navigation Drawer
============================

.. seealso::

    `Material Design spec, Navigation drawer <https://material.io/components/navigation-drawer>`_

.. rubric:: Navigation drawers provide access to destinations in your app.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer.png
    :align: center

When using the class :class:`~MDNavigationDrawer` skeleton of your `KV` markup
should look like this:

.. code-block:: kv

    Root:

        NavigationLayout:

            ScreenManager:

                Screen_1:

                Screen_2:

            MDNavigationDrawer:
                # This custom rule should implement what will be appear in your MDNavigationDrawer
                ContentNavigationDrawer

A simple example:

.. code-block:: python

    from kivy.uix.boxlayout import BoxLayout

    from kivymd.app import MDApp
    from kivy.lang import Builder

    KV = '''
    Screen:

        NavigationLayout:

            ScreenManager:

                Screen:

                    BoxLayout:
                        orientation: 'vertical'

                        MDToolbar:
                            title: "Navigation Drawer"
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                        Widget:


            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
    '''


    class ContentNavigationDrawer(BoxLayout):
        pass


    class TestNavigationDrawer(MDApp):
        def build(self):
            return Builder.load_string(KV)


    TestNavigationDrawer().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/navigation-drawer.gif
    :align: center

.. Note:: :class:`~MDNavigationDrawer` is an empty
    :class:`~kivymd.uix.card.MDCard` panel.

Let's extend the ``ContentNavigationDrawer`` class from the above example and
create content for our :class:`~MDNavigationDrawer` panel:

.. code-block:: kv

    # Menu item in the DrawerList list.
    <ItemDrawer>:
        theme_text_color: "Custom"
        on_release: self.parent.set_color_item(self)

        IconLeftWidget:
            id: icon
            icon: root.icon
            theme_text_color: "Custom"
            text_color: root.text_color

.. code-block:: python

    class ItemDrawer(OneLineIconListItem):
        icon = StringProperty()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/drawer-item.png
    :align: center

Top of ``ContentNavigationDrawer`` and ``DrawerList`` for menu items:

.. code-block:: kv

    <ContentNavigationDrawer>:
        orientation: "vertical"
        padding: "8dp"
        spacing: "8dp"

        AnchorLayout:
            anchor_x: "left"
            size_hint_y: None
            height: avatar.height

            Image:
                id: avatar
                size_hint: None, None
                size: "56dp", "56dp"
                source: "kivymd_logo.png"

        MDLabel:
            text: "KivyMD library"
            font_style: "Button"
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: "kivydevelopment@gmail.com"
            font_style: "Caption"
            size_hint_y: None
            height: self.texture_size[1]

        ScrollView:

            DrawerList:
                id: md_list

.. code-block:: python

    class ContentNavigationDrawer(BoxLayout):
        pass


    class DrawerList(ThemableBehavior, MDList):
        def set_color_item(self, instance_item):
            '''Called when tap on a menu item.'''

            # Set the color of the icon and text for the menu item.
            for item in self.children:
                if item.text_color == self.theme_cls.primary_color:
                    item.text_color = self.theme_cls.text_color
                    break
            instance_item.text_color = self.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/drawer-top.png
    :align: center

Create a menu list for ``ContentNavigationDrawer``:

.. code-block:: python

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/drawer-work.gif
    :align: center

Switching screens in the ``ScreenManager`` and using the common ``MDToolbar``
---------------------------------------------------------------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.boxlayout import BoxLayout
    from kivy.properties import ObjectProperty

    from kivymd.app import MDApp

    KV = '''
    <ContentNavigationDrawer>:

        ScrollView:

            MDList:

                OneLineListItem:
                    text: "Screen 1"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 1"

                OneLineListItem:
                    text: "Screen 2"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"


    Screen:

        MDToolbar:
            id: toolbar
            pos_hint: {"top": 1}
            elevation: 10
            title: "MDNavigationDrawer"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        NavigationLayout:
            x: toolbar.height

            ScreenManager:
                id: screen_manager

                Screen:
                    name: "scr 1"

                    MDLabel:
                        text: "Screen 1"
                        halign: "center"

                Screen:
                    name: "scr 2"

                    MDLabel:
                        text: "Screen 2"
                        halign: "center"

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
    '''


    class ContentNavigationDrawer(BoxLayout):
        screen_manager = ObjectProperty()
        nav_drawer = ObjectProperty()


    class TestNavigationDrawer(MDApp):
        def build(self):
            return Builder.load_string(KV)


    TestNavigationDrawer().run()

.. seealso::

    `Full example of Components-Navigation-Drawer <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Navigation-Drawer>`_
"""

__all__ = ("NavigationLayout", "MDNavigationDrawer")

from kivy.animation import Animation, AnimationTransition
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar

Builder.load_string(
    """
#:import Window kivy.core.window.Window


<MDNavigationDrawer>:
    size_hint_x: None
    width: Window.width - dp(56) if Window.width <= dp(376) else dp(320)
    x:
        (self.width * (self.open_progress - 1)) \
        if self.anchor == "left" \
        else (Window.width - self.width * self.open_progress)
    elevation: 10
"""
)


class NavigationDrawerContentError(Exception):
    pass


class NavigationLayout(FloatLayout):
    _scrim_color = ObjectProperty(None)
    _scrim_rectangle = ObjectProperty(None)

    def add_scrim(self, widget):
        with widget.canvas.after:
            self._scrim_color = Color(rgba=[0, 0, 0, 0])
            self._scrim_rectangle = Rectangle(pos=widget.pos, size=widget.size)
            widget.bind(
                pos=self.update_scrim_rectangle,
                size=self.update_scrim_rectangle,
            )

    def update_scrim_rectangle(self, *args):
        self._scrim_rectangle.pos = self.pos
        self._scrim_rectangle.size = self.size

    def add_widget(self, widget, index=0, canvas=None):
        """
        Only two layouts are allowed:
        :class:`~kivy.uix.screenmanager.ScreenManager` and
        :class:`~MDNavigationDrawer`.
        """

        if not isinstance(
            widget, (MDNavigationDrawer, ScreenManager, MDToolbar)
        ):
            raise NavigationDrawerContentError(
                "The NavigationLayout must contain "
                "only `MDNavigationDrawer` and `ScreenManager`"
            )
        if isinstance(widget, ScreenManager):
            self.add_scrim(widget)
        if len(self.children) > 3:
            raise NavigationDrawerContentError(
                "The NavigationLayout must contain "
                "only `MDNavigationDrawer` and `ScreenManager`"
            )
        return super().add_widget(widget)


class MDNavigationDrawer(MDCard):
    anchor = OptionProperty("left", options=("left", "right"))
    """
    Anchoring screen edge for drawer. Set it to `'right'` for right-to-left
    languages. Available options are: `'left'`, `'right'`.

    :attr:`anchor` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `left`.
    """

    close_on_click = BooleanProperty(True)
    """
    Close when click on scrim or keyboard escape.

    :attr:`close_on_click` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    state = OptionProperty("close", options=("close", "open"))
    """
    Indicates if panel closed or opened. Sets after :attr:`status` change.
    Available options are: `'close'`, `'open'`.

    :attr:`state` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'close'`.
    """

    status = OptionProperty(
        "closed",
        options=(
            "closed",
            "opening_with_swipe",
            "opening_with_animation",
            "opened",
            "closing_with_swipe",
            "closing_with_animation",
        ),
    )
    """
    Detailed state. Sets before :attr:`state`. Bind to :attr:`state` instead
    of :attr:`status`. Available options are: `'closed'`,
    `'opening_with_swipe'`, `'opening_with_animation'`, `'opened'`,
    `'closing_with_swipe'`, `'closing_with_animation'`.

    :attr:`status` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'closed'`.
    """

    open_progress = NumericProperty(0.0)
    """
    Percent of visible part of side panel. The percent is specified as a
    floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if
    panel is opened.

    :attr:`open_progress` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    swipe_distance = NumericProperty(10)
    """
    The distance of the swipe with which the movement of navigation drawer
    begins.

    :attr:`swipe_distance` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `10`.
    """

    swipe_edge_width = NumericProperty(20)
    """
    The size of the area in px inside which should start swipe to drag
    navigation drawer.

    :attr:`swipe_edge_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `20`.
    """

    scrim_color = ListProperty([0, 0, 0, 0.5])
    """
    Color for scrim. Alpha channel will be multiplied with
    :attr:`_scrim_alpha`. Set fourth channel to 0 if you want to disable
    scrim.

    :attr:`scrim_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    def _get_scrim_alpha(self):
        _scrim_alpha = self._scrim_alpha_transition(self.open_progress)
        if isinstance(self.parent, NavigationLayout):
            self.parent._scrim_color.rgba = self.scrim_color[:3] + [
                self.scrim_color[3] * _scrim_alpha
            ]
        return _scrim_alpha

    _scrim_alpha = AliasProperty(
        _get_scrim_alpha,
        None,
        bind=("_scrim_alpha_transition", "open_progress", "scrim_color"),
    )
    """
    Multiplier for alpha channel of :attr:`scrim_color`. For internal
    usage only.
    """

    scrim_alpha_transition = StringProperty("linear")
    """
    The name of the animation transition type to use for changing
    :attr:`scrim_alpha`.

    :attr:`scrim_alpha_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'linear'`.
    """

    def _get_scrim_alpha_transition(self):
        return getattr(AnimationTransition, self.scrim_alpha_transition)

    _scrim_alpha_transition = AliasProperty(
        _get_scrim_alpha_transition,
        None,
        bind=("scrim_alpha_transition",),
        cache=True,
    )

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    closing_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'close'`.

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            open_progress=self.update_status,
            status=self.update_status,
            state=self.update_status,
        )
        Window.bind(on_keyboard=self._handle_keyboard)

    def set_state(self, new_state="toggle", animation=True):
        """Change state of the side panel.
        New_state can be one of `"toggle"`, `"open"` or `"close"`.
        """

        if new_state == "toggle":
            new_state = "close" if self.state == "open" else "open"

        if new_state == "open":
            Animation.cancel_all(self, "open_progress")
            self.status = "opening_with_animation"
            if animation:
                Animation(
                    open_progress=1.0,
                    d=self.opening_time * (1 - self.open_progress),
                    t=self.opening_transition,
                ).start(self)
            else:
                self.open_progress = 1
        else:  # "close"
            Animation.cancel_all(self, "open_progress")
            self.status = "closing_with_animation"
            if animation:
                Animation(
                    open_progress=0.0,
                    d=self.closing_time * self.open_progress,
                    t=self.closing_transition,
                ).start(self)
            else:
                self.open_progress = 0

    def toggle_nav_drawer(self):
        Logger.warning(
            "KivyMD: The 'toggle_nav_drawer' method is deprecated, "
            "use 'set_state' instead."
        )
        self.set_state("toggle", animation=True)

    def update_status(self, *_):
        status = self.status
        if status == "closed":
            self.state = "close"
        elif status == "opened":
            self.state = "open"
        elif self.open_progress == 1 and status == "opening_with_animation":
            self.status = "opened"
            self.state = "open"
        elif self.open_progress == 0 and status == "closing_with_animation":
            self.status = "closed"
            self.state = "close"
        elif status in (
            "opening_with_swipe",
            "opening_with_animation",
            "closing_with_swipe",
            "closing_with_animation",
        ):
            pass

    def get_dist_from_side(self, x):
        if self.anchor == "left":
            return 0 if x < 0 else x
        return 0 if x > Window.width else Window.width - x

    def on_touch_down(self, touch):
        if self.status == "closed":
            return False
        elif self.status == "opened":
            for child in self.children[:]:
                if child.dispatch("on_touch_down", touch):
                    return True
        return True

    def on_touch_move(self, touch):
        if self.status == "closed":
            if (
                self.get_dist_from_side(touch.ox) <= self.swipe_edge_width
                and abs(touch.x - touch.ox) > self.swipe_distance
            ):
                self.status = "opening_with_swipe"
        elif self.status == "opened":
            self.status = "closing_with_swipe"

        if self.status in ("opening_with_swipe", "closing_with_swipe"):
            self.open_progress = max(
                min(self.open_progress + touch.dx / self.width, 1), 0
            )
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.status == "opening_with_swipe":
            if self.open_progress > 0.5:
                self.set_state("open", animation=True)
            else:
                self.set_state("close", animation=True)
        elif self.status == "closing_with_swipe":
            if self.open_progress < 0.5:
                self.set_state("close", animation=True)
            else:
                self.set_state("open", animation=True)
        elif self.status == "opened":
            if self.close_on_click and not self.collide_point(
                touch.ox, touch.oy
            ):
                self.set_state("close", animation=True)
        elif self.status == "closed":
            return False
        return True

    def _handle_keyboard(self, window, key, *largs):
        if key == 27 and self.status == "opened" and self.close_on_click:
            self.set_state("close")
            return True
