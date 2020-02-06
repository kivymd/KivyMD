"""
Components/Navigation Drawer
============================

.. seealso::

   `Material Design spec, Navigation drawer <https://material.io/design/components/navigation-drawer.html>`

Example
-------

from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarListItem

KV = '''
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path


<NavigationItem>
    theme_text_color: 'Custom'
    divider: None

    IconLeftWidget:
        icon: root.icon


<ContentNavigationDrawer>

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            size_hint_y: None
            height: "200dp"

            canvas:
                Color:
                    rgba: app.theme_cls.primary_color
                Rectangle:
                    pos: self.pos
                    size: self.size

            BoxLayout:
                id: top_box
                size_hint_y: None
                height: "200dp"
                #padding: "10dp"
                x: root.parent.x
                pos_hint: {"top": 1}

                FitImage:
                    source: f"{images_path}kivymd_alpha.png"

            MDIconButton:
                icon: "close"
                x: root.parent.x + dp(10)
                pos_hint: {"top": 1}
                on_release: root.parent.toggle_nav_drawer()

            MDLabel:
                markup: True
                text: "[b]KivyMD[/b]\\nVersion: 0.102.1"
                #pos_hint: {'center_y': .5}
                x: root.parent.x + dp(10)
                y: root.height - top_box.height + dp(10)
                size_hint_y: None
                height: self.texture_size[1]

        ScrollView:
            pos_hint: {"top": 1}

            GridLayout:
                id: box_item
                cols: 1
                size_hint_y: None
                height: self.minimum_height


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        md_bg_color: app.theme_cls.primary_color
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    pass


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for items in {
            "home-circle-outline": "Home",
            "update": "Check for Update",
            "settings-outline": "Settings",
            "exit-to-app": "Exit",
        }.items():
            self.root.ids.content_drawer.ids.box_item.add_widget(
                NavigationItem(
                    text=items[1],
                    icon=items[0],
                )
            )


TestNavigationDrawer().run()

"""

from kivy.core.window import Window
from kivy.logger import Logger
from kivy.animation import Animation, AnimationTransition
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    OptionProperty,
    BooleanProperty,
    ListProperty,
    ObjectProperty,
    AliasProperty,
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
        """Only two layouts are allowed:
        ScreenManager and MDNavigationDrawer.

        """

        if not isinstance(
            widget, (MDNavigationDrawer, ScreenManager, MDToolbar)
        ):
            raise NavigationDrawerContentError(
                "The NavigationLayout should contain "
                "only MDNavigationDrawer and ScreenManager"
            )
        if isinstance(widget, ScreenManager):
            self.add_scrim(widget)
        if len(self.children) > 3:
            raise NavigationDrawerContentError(
                "The NavigationLayout should contain "
                "only MDNavigationDrawer and ScreenManager"
            )
        return super().add_widget(widget)


class MDNavigationDrawer(MDCard):
    anchor = OptionProperty("left", options=("left", "right"))
    """Anchoring screen edge for drawer. Set it to "right" for right-to-left
    languages."""

    close_on_click = BooleanProperty(True)
    """Close when click on scrim or keyboard escape."""

    state = OptionProperty("close", options=("close", "open"))
    """Indicates if panel closed or opened. Sets after :attr:`status` change."""

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
    """Detailed state. Sets before :attr:`state`. Bind to :attr:`state` instead
    of :attr:`status`."""

    open_progress = NumericProperty(0.0)
    """Percent of visible part of side panel. The percent is specified as a
    floating point number in the range 0-1. 0.0 if panel is closed and 1.0 if
    panel is opened."""

    swipe_distance = NumericProperty(10)
    """The distance of the swipe with which the movement of navigation drawer
    begins."""

    swipe_edge_width = NumericProperty(20)
    """The size of the area in px inside which should start swipe to drag
    navigation drawer."""

    scrim_color = ListProperty([0, 0, 0, 0.5])
    """Color for scrim. Alpha channel will be multiplied with
    :attr:`_scrim_alpha`. Set fourth channel to 0 if you want to disable
    scrim."""

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
    """Multiplier for alpha channel of :attr:`scrim_color`. For internal
    usage only."""

    scrim_alpha_transition = StringProperty("linear")
    """The name of the animation transition type to use for changing
    :attr:`scrim_alpha`. Defaults to 'linear'."""

    def _get_scrim_alpha_transition(self):
        return getattr(AnimationTransition, self.scrim_alpha_transition)

    _scrim_alpha_transition = AliasProperty(
        _get_scrim_alpha_transition,
        None,
        bind=("scrim_alpha_transition",),
        cache=True,
    )

    opening_transition = StringProperty("out_cubic")
    """The name of the animation transition type to use when animating to
    the :attr:`state` "open". Defaults to 'out_cubic'."""

    opening_time = NumericProperty(0.2)
    """The time taken for the panel to slide to the :attr:`state` "open"."""

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` "close". Defaults to 'out_sine'."""

    closing_time = NumericProperty(0.2)
    """The time taken for the panel to slide to the :attr:`state` "close"."""

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

        new_state can be one of "toggle", "open" or "close"."""
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
            if (
                self.close_on_click
                and self.get_dist_from_side(touch.ox) > self.width
            ):
                self.set_state("close", animation=True)
        elif self.status == "closed":
            return False
        return True

    def _handle_keyboard(self, window, key, *largs):
        if key == 27 and self.status == "opened" and self.close_on_click:
            self.set_state("close")
            return True
