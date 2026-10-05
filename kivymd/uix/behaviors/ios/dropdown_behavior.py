"""
Behaviors/iOS Dropdown
======================

.. versionadded:: 2.0.1

.. rubric:: Provides liquid metaball morphing and glassmorphic dropdown behavior
    inspired by iOS visual effects.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-preview.jpeg
    :align: center

- Streamlines single tasks or options, keeping the user in flow;
- Supports basic pop-ups and expanded full-size menus;
- Blends and splits elements with dynamic GLSL shader animations;
- Rendered as frosted glass with refraction, blur, and smooth corners;
- Displays relevant info for quick changes or confirmations;

Anatomy
=======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-anatomy.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                FitImage:
                    id: bg_image
                    source: "https://picsum.photos/800/600?random=1"

                IOSLiquidDropdownContainer:
                    id: dropdown_container
                    caller: trigger_btn
                    menu: menu_btn

                    IOSButton:
                        id: trigger_btn
                        size_hint: None, None
                        size: dp(56), dp(56)
                        border_radius: [dp(28)] * 4
                        target_background: bg_image
                        pos_hint: {"center_x": 0.5, "center_y": 0.65}
                        on_release: dropdown_container.toggle_dropdown()

                        IOSIconButton:
                            icon: "filter-variant"
                            theme_icon_color: "Custom"
                            icon_color: "white"

                    IOSButton:
                        id: menu_btn
                        adaptive_size: True
                        target_background: bg_image
                        border_radius: [dp(22)] * 4
                        on_release: dropdown_container.toggle_dropdown()

                        IOSButtonText:
                            text: "IOS Button"
                            theme_text_color: "Custom"
                            text_color: "white"
            '''


            class LiquidGlassDropdownDemo(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            if __name__ == "__main__":
                LiquidGlassDropdownDemo().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import IOSLiquidDropdownContainer
            from kivymd.uix.button import IOSButton, IOSIconButton, IOSButtonText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen


            class LiquidGlassDropdownDemo(MDApp):
                def build(self):
                    bg_image = FitImage(
                        id="bg_image",
                        source="https://picsum.photos/800/600?random=1",
                    )
                    dropdown_container = IOSLiquidDropdownContainer()

                    trigger_btn = IOSButton(
                        IOSIconButton(
                            icon="filter-variant",
                            theme_icon_color="Custom",
                            icon_color="white",
                        ),
                        size_hint=[None, None],
                        size=[dp(56), dp(56)],
                        border_radius=[dp(28)] * 4,
                        target_background=bg_image,
                        pos_hint={"center_x": 0.5, "center_y": 0.65},
                    )
                    trigger_btn.bind(
                        on_release=lambda x: dropdown_container.toggle_dropdown()
                    )

                    menu = IOSButton(
                        IOSButtonText(
                            text="IOS Button",
                            theme_text_color="Custom",
                            text_color="white",
                        ),
                        adaptive_size=True,
                        border_radius=[dp(22)] * 4,
                        target_background=bg_image,
                    )
                    menu.bind(
                        on_release=lambda x: dropdown_container.toggle_dropdown()
                    )

                    dropdown_container.widgets = [
                        trigger_btn,
                        menu,
                    ]
                    dropdown_container.caller = trigger_btn
                    dropdown_container.menu = menu

                    return MDScreen(
                        bg_image,
                        dropdown_container,
                    )


            if __name__ == "__main__":
                LiquidGlassDropdownDemo().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-example.gif
    :align: center

Menu example
------------

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import ListProperty, ObjectProperty

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.list import (
                MDListItem,
                MDListItemHeadlineText,
                MDListItemLeadingIcon,
                MDListItemSupportingText,
            )

            KV = '''
            <ListLayout>
                orientation: "vertical"
                adaptive_height: True
                spacing: dp(4)


            MDScreen:

                FitImage:
                    id: bg_image
                    source: "https://picsum.photos/800/600?random=1"

                IOSLiquidDropdownContainer:
                    id: dropdown_container
                    caller: trigger_btn
                    menu: menu_box

                    IOSButton:
                        id: trigger_btn
                        size_hint: None, None
                        size: dp(56), dp(56)
                        border_radius: [dp(28), dp(28), dp(28), dp(28)]
                        target_background: bg_image
                        pos_hint: {"center_x": 0.5, "center_y": 0.65}
                        on_release: dropdown_container.toggle_dropdown()

                        IOSIconButton:
                            icon: "filter-variant"
                            theme_icon_color: "Custom"
                            icon_color: "white"

                    MDBoxLayout:
                        id: menu_box
                        size_hint: None, None
                        size: dp(400), dp(200)
                        orientation: "vertical"
                        padding: dp(16)
                        spacing: dp(10)
                        border_radius: [dp(32), dp(32), dp(32), dp(32)]

                        MDScrollView:
                            do_scroll_x: False
                            bar_width: 0

                            ListLayout:
                                dropdown_container: dropdown_container
            '''


            class ListLayout(MDBoxLayout):
                dropdown_container = ObjectProperty(allownone=True)
                items_data = ListProperty([
                    ("account-circle-outline", "My Profile", "Account settings"),
                    ("message-text-outline", "Messages", "Notifications and chats"),
                    ("heart-outline", "Favorites", "Saved items"),
                    ("cog-outline", "Settings", "App preferences"),
                    ("logout-variant", "Log Out", "End current session"),
                ])

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.generate_items()

                def generate_items(self):
                    self.clear_widgets()

                    for icon, title, subtitle in self.items_data:
                        item = MDListItem(
                            MDListItemLeadingIcon(
                                icon=icon,
                                theme_icon_color="Custom",
                                icon_color=[1, 1, 1, 0.9],
                            ),
                            MDListItemHeadlineText(
                                text=title,
                                theme_text_color="Custom",
                                text_color=[1, 1, 1, 1],
                            ),
                            MDListItemSupportingText(
                                text=subtitle,
                                theme_text_color="Custom",
                                text_color=[1, 1, 1, 0.6],
                            ),
                            theme_bg_color="Custom",
                            md_bg_color=[0, 0, 0, 0],
                        )

                        item.bind(on_release=self._on_item_release)
                        self.add_widget(item)

                def _on_item_release(self, instance):
                    if self.dropdown_container:
                        self.dropdown_container.toggle_dropdown()



            class LiquidGlassDropdownDemo(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            if __name__ == "__main__":
                LiquidGlassDropdownDemo().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.properties import ObjectProperty

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import IOSLiquidDropdownContainer
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import IOSButton, IOSIconButton
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.list import (
                MDListItem,
                MDListItemHeadlineText,
                MDListItemLeadingIcon,
                MDListItemSupportingText,
            )
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.scrollview import MDScrollView


            class ListLayout(MDBoxLayout):
                dropdown_container = ObjectProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    items_data = [
                        ("account-circle-outline", "My Profile", "Account settings"),
                        ("message-text-outline", "Messages", "Notifications and chats"),
                        ("heart-outline", "Favorites", "Saved items"),
                        ("cog-outline", "Settings", "App preferences"),
                        ("logout-variant", "Log Out", "End current session"),
                    ]

                    self.orientation = "vertical"
                    self.adaptive_height = True
                    self.spacing = dp(4)

                    widgets = []
                    for icon, title, subtitle in items_data:
                        item = MDListItem(
                            MDListItemLeadingIcon(
                                icon=icon,
                                theme_icon_color="Custom",
                                icon_color=[1, 1, 1, 0.9],
                            ),
                            MDListItemHeadlineText(
                                text=title,
                                theme_text_color="Custom",
                                text_color=[1, 1, 1, 1],
                            ),
                            MDListItemSupportingText(
                                text=subtitle,
                                theme_text_color="Custom",
                                text_color=[1, 1, 1, 0.6],
                            ),
                            theme_bg_color="Custom",
                            md_bg_color=[0, 0, 0, 0],
                        )

                        if self.dropdown_container:
                            item.bind(
                                on_release=lambda x: self.dropdown_container.toggle_dropdown()
                            )

                        widgets.append(item)

                    self.widgets = widgets


            class MenuScreen(MDScreen):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    bg_image = FitImage(
                        source="https://picsum.photos/800/600?random=1",
                    )
                    dropdown_container = IOSLiquidDropdownContainer()

                    trigger_btn = IOSButton(
                        IOSIconButton(
                            icon="filter-variant",
                            theme_icon_color="Custom",
                            icon_color="white",
                        ),
                        size_hint=[None, None],
                        size=[dp(56), dp(56)],
                        border_radius=[dp(28)] * 4,
                        target_background=bg_image,
                        pos_hint={"center_x": 0.5, "center_y": 0.65},
                    )
                    trigger_btn.bind(
                        on_release=lambda x: dropdown_container.toggle_dropdown()
                    )

                    menu = MDBoxLayout(
                        MDScrollView(
                            ListLayout(
                                dropdown_container=dropdown_container,
                            ),
                            do_scroll_x=False,
                            bar_width=0,
                        ),
                        size_hint=[None, None],
                        size=[dp(400), dp(200)],
                        orientation="vertical",
                        padding=dp(16),
                        spacing=dp(10),
                    )
                    menu.border_radius = [dp(32)] * 4

                    dropdown_container.widgets = [
                        trigger_btn,
                        menu,
                    ]
                    dropdown_container.caller = trigger_btn
                    dropdown_container.menu = menu

                    self.widgets = [
                        bg_image,
                        dropdown_container,
                    ]


            class LiquidGlassDropdownDemo(MDApp):
                def build(self):
                    return MenuScreen()


            if __name__ == "__main__":
                LiquidGlassDropdownDemo().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-menu-example.gif
    :align: center
"""

__all__ = (
    "IOSLiquidDropdownBehavior",
    "IOSLiquidDropdownContainer",
)

import math
import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.floatlayout import FloatLayout

from kivymd import glsl_path
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.behaviors.ios.glass_behavior import IOSBaseGlassBehavior

GLSL_IOS_DROPDOWN_PATH = os.path.join(glsl_path, "ios", "dropdown")
GLSL_IOS_DROPDOWN_VS_PATH = os.path.join(
    GLSL_IOS_DROPDOWN_PATH, "liquid_dropdown_vs.glsl"
)
GLSL_IOS_DROPDOWN_FS_PATH = os.path.join(
    GLSL_IOS_DROPDOWN_PATH, "liquid_dropdown_fs.glsl"
)

with open(
    GLSL_IOS_DROPDOWN_VS_PATH,
    encoding="utf-8",
) as shader_file:
    IOS_LIQUID_DROPDOWN_VS = "$HEADER$\n" + shader_file.read()

with open(GLSL_IOS_DROPDOWN_FS_PATH, encoding="utf-8") as shader_file:
    IOS_LIQUID_DROPDOWN_FS = shader_file.read()


class IOSLiquidDropdownBehavior(IOSBaseGlassBehavior):
    """
    Behavior class responsible for orchestrating the liquid metaball
    transition, shader uniform synchronization, and wobble dynamics between a
    trigger button and a dropdown menu.

    For more information see in the
    :class:`~kivymd.uix.behaviors.ios.glass_behavior.IOSBaseGlassBehavior`
    class documentation.
    """

    direction = OptionProperty(
        "bottom",
        options=[
            "bottom",
            "top",
            "left",
            "right",
            "bottom-left",
            "bottom-right",
            "top-left",
            "top-right",
        ],
    )
    """
    Direction in which the dropdown menu expands relative to the caller button.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-direction.png
        :align: center

    Available options: 'bottom', 'top', 'left', 'right', 'bottom-left',
    'bottom-right', 'top-left', 'top-right'.

    :attr:`direction` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'bottom'`.
    """

    spacing = NumericProperty(dp(12))
    """
    Gap between the trigger button and the dropdown menu.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-behavior-spacing.png
        :align: center

    :attr:`spacing` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(12)`.
    """

    open_transition = StringProperty("out_cubic")
    """
    Easing curve transition type for the expansion animation.

    :attr:`open_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    open_duration = NumericProperty(0.6)
    """
    Total time in seconds required to fully expand the dropdown menu.

    :attr:`open_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.6`.
    """

    close_transition = StringProperty("in_out_cubic")
    """
    Easing curve transition type for the collapse animation.

    :attr:`close_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_out_cubic'`.
    """

    close_duration = NumericProperty(0.45)
    """
    Total time in seconds required to collapse back into the trigger button.

    :attr:`close_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.45`.
    """

    viscosity = NumericProperty(dp(100))
    """
    Maximum smooth-minimum blending factor (k) controlling the liquid neck
    stretch.

    :attr:`viscosity` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(100)`.
    """

    is_open = BooleanProperty(False)
    """
    State flag indicating whether the dropdown menu is currently open.

    :attr:`is_open` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    btn_fade_out_transition = StringProperty("out_quad")
    """
    Easing curve transition for hiding trigger button on open.

    :attr:`btn_fade_out_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    btn_fade_in_transition = StringProperty("in_quad")
    """
    Easing curve transition for restoring trigger button on close.

    :attr:`btn_fade_in_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_quad'`.
    """

    menu_fade_in_transition = StringProperty("out_quad")
    """
    Easing curve transition for revealing dropdown menu content on open completion.

    :attr:`menu_fade_in_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    menu_fade_out_transition = StringProperty("out_quad")
    """
    Easing curve transition for hiding dropdown menu content on close.

    :attr:`menu_fade_out_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    k_ramp_up_transition = StringProperty("out_quad")
    """
    Easing curve transition for increasing viscosity (k).

    :attr:`k_ramp_up_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_quad'`.
    """

    k_ramp_down_transition = StringProperty("in_cubic")
    """
    Easing curve transition for collapsing viscosity (k).

    :attr:`k_ramp_down_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'in_cubic'`.
    """

    # Internal animated smooth-minimum blending factor passed to GLSL uniform
    # `u_k`.
    _current_k = NumericProperty(0.0)
    # Internal interpolation factor (0.0 to 1.0) passed to GLSL uniform
    # `u_menu_alpha`.
    _menu_alpha = NumericProperty(0.0)

    __events__ = ("on_open", "on_close")

    # Keys to unbind from default child widget handlers to override custom
    # rendering.
    _UNBIND_KEYS = (
        "pos",
        "size",
        "border_radius",
        "glass_color",
        "blur_amount",
        "lens_power",
        "bevel_power",
        "_press_factor",
        "_scale_factor",
        "_touch_pos",
    )

    def __init__(self, *args, **kwargs):
        self.time = 0.0
        self.wobble_time = 0.0
        self.is_wobbling = False
        self._trigger_btn = None
        self._dropdown_menu = None
        self._bound_screen = None
        self._update_event = None

        super().__init__(*args, **kwargs)

        Window.bind(size=self._trigger_window_resize)

    def on_open(self, *args) -> None:
        """Default event handler fired when expansion animation finishes."""

    def on_close(self, *args) -> None:
        """Default event handler fired when collapse animation finishes."""

    def on_parent(self, instance, parent):
        """Cleanup when removing a widget from the layout."""

        if parent is None:
            self._stop_shader_updates()

            try:
                Window.unbind(size=self._trigger_window_resize)
            except Exception:
                pass

            if self._bound_screen:
                try:
                    self._bound_screen.unbind(on_enter=self._on_screen_enter)
                    self._bound_screen.unbind(on_leave=self._on_screen_leave)
                except Exception:
                    pass
                self._bound_screen = None
        else:
            Window.bind(size=self._trigger_window_resize)
            Clock.schedule_once(lambda dt: self._find_and_bind_screen(), 0)

    def on_touch_down(self, touch):
        if self._handle_outside_touch(touch):
            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self._handle_outside_touch(touch):
            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self._handle_outside_touch(touch):
            return True

        return super().on_touch_up(touch)

    def update_menu_position(self, *args) -> None:
        """
        Dynamically repositions the dropdown menu relative to the trigger button
        based on direction and properties.
        """

        if not self._trigger_btn or not self._dropdown_menu:
            return

        btn = self._trigger_btn
        menu = self._dropdown_menu

        menu.pos_hint = {}

        btn_x, btn_y = btn.pos
        btn_w, btn_h = btn.size
        menu_w, menu_h = menu.size

        x, y = btn_x, btn_y

        if self.direction == "bottom":
            x = btn_x + (btn_w - menu_w) / 2.0
            y = btn_y - menu_h - self.spacing
        elif self.direction == "top":
            x = btn_x + (btn_w - menu_w) / 2.0
            y = btn_y + btn_h + self.spacing
        elif self.direction == "left":
            x = btn_x - menu_w - self.spacing
        elif self.direction == "right":
            x = btn_x + btn_w + self.spacing
        elif self.direction == "bottom-left":
            x = btn_x - menu_w + btn_w
            y = btn_y - menu_h - self.spacing
        elif self.direction == "bottom-right":
            x = btn_x
            y = btn_y - menu_h - self.spacing
        elif self.direction == "top-left":
            x = btn_x - menu_w + btn_w
            y = btn_y + btn_h + self.spacing
        elif self.direction == "top-right":
            x = btn_x
            y = btn_y + btn_h + self.spacing

        menu.pos = (x, y)

    def toggle_dropdown(self) -> None:
        """Toggle between open and close states."""

        if self.is_open:
            self.close()
        else:
            self.open()

    def open(self) -> None:
        """
        Triggers liquid expansion sequence: stretches metaball neck,
        triggers pinch-off wobble impulse, and reveals content upon completion.
        """

        if self.is_open or not self._trigger_btn or not self._dropdown_menu:
            return

        if self._dropdown_menu.parent is None:
            self.add_widget(self._dropdown_menu)

        self.update_menu_position()

        self.is_open = True
        # Trigger immediate wobble wave right as motion starts.
        self.is_wobbling = True
        self.wobble_time = 0.0

        # Hide native button graphic while custom liquid canvas renders
        # transition.
        Animation(
            opacity=0.0,
            d=0.15,
            t=self.btn_fade_out_transition,
        ).start(self._trigger_btn)

        self._dropdown_menu.opacity = 0.0
        self._dropdown_menu.disabled = True

        def _on_open_complete(anim, widget):
            """Reveal menu UI elements after liquid body settles."""

            self._dropdown_menu.disabled = False

            Animation(
                opacity=1.0,
                d=0.12,
                t=self.menu_fade_in_transition,
            ).start(self._dropdown_menu)

            self.dispatch("on_open")

        Animation.stop_all(self, "_current_k", "_menu_alpha")

        # Viscosity (k) ramps up quickly to form neck, then collapses to snap
        # connection.
        anim_k = Animation(
            _current_k=self.viscosity,
            d=self.open_duration * 0.3,
            t=self.k_ramp_up_transition,
        ) + Animation(
            _current_k=0.0,
            d=self.open_duration * 0.4,
            t=self.k_ramp_down_transition,
        )

        anim_alpha = Animation(
            _menu_alpha=1.0,
            d=self.open_duration,
            t=self.open_transition,
        )
        anim_alpha.bind(on_complete=_on_open_complete)

        anim_k.start(self)
        anim_alpha.start(self)

    def close(self) -> None:
        """
        Triggers liquid collapse sequence: hides menu UI immediately, pulls
        liquid body back into trigger button, and restores original UI state.
        """

        if not self.is_open or not self._trigger_btn or not self._dropdown_menu:
            return

        self.is_open = False
        # Trigger immediate wobble wave upon snapping back.
        self.is_wobbling = True
        self.wobble_time = 0.0

        self._dropdown_menu.disabled = True
        self._dropdown_menu.opacity = 0.0

        def _on_close_complete(anim, widget):
            """Restore original trigger button visibility when collapsed."""

            if self._dropdown_menu and self._dropdown_menu.parent:
                self.remove_widget(self._dropdown_menu)

            Animation(
                opacity=1.0,
                d=0.15,
                t=self.btn_fade_in_transition,
            ).start(self._trigger_btn)
            self.dispatch("on_close")

        Animation.stop_all(self, "_current_k", "_menu_alpha")

        # Viscosity curve during return transition.
        anim_k = Animation(
            _current_k=self.viscosity,
            d=self.close_duration * 0.4,
            t=self.k_ramp_up_transition,
        ) + Animation(
            _current_k=0.0,
            d=self.close_duration * 0.6,
            t=self.k_ramp_down_transition,
        )

        anim_alpha = Animation(
            _menu_alpha=0.0,
            d=self.close_duration,
            t=self.close_transition,
        )
        anim_alpha.bind(on_complete=_on_close_complete)

        anim_k.start(self)
        anim_alpha.start(self)

    def _trigger_window_resize(self, *args):
        self.update_menu_position()
        Clock.schedule_once(self._update_shader_uniforms)

    def _handle_outside_touch(self, touch):
        if not self.is_open:
            return False

        btn_hit = self._trigger_btn and self._trigger_btn.collide_point(
            *touch.pos
        )
        menu_hit = self._dropdown_menu and self._dropdown_menu.collide_point(
            *touch.pos
        )

        if not btn_hit and not menu_hit:
            self.close()
            return True

        return False

    # =========================================================================
    #
    # SCREEN LIFECYCLE MANAGEMENT & SHADER UPDATE TIMER
    #
    # This set of methods binds the widget to its parent MDScreen and controls
    # the 60 FPS _update_shader_uniforms loop. It ensures that uniform and
    # geometry calculations run exclusively when the host screen is active and
    # visible, completely eliminating CPU/GPU overhead when navigating away or
    # when the widget is hidden.

    def _find_and_bind_screen(self):
        current = self.parent

        while current:
            if hasattr(current, "is_event_type") and current.is_event_type(
                "on_enter"
            ):
                if self._bound_screen != current:
                    if self._bound_screen:
                        try:
                            self._bound_screen.unbind(
                                on_enter=self._on_screen_enter,
                                on_leave=self._on_screen_leave,
                            )
                        except Exception:
                            pass

                    self._bound_screen = current
                    self._bound_screen.bind(
                        on_enter=self._on_screen_enter,
                        on_leave=self._on_screen_leave,
                    )

                    self._start_shader_updates()
                break

            current = getattr(current, "parent", None)
        else:
            self._start_shader_updates()

    def _on_screen_enter(self, screen_instance):
        self._start_shader_updates()

    def _on_screen_leave(self, screen_instance):
        self._stop_shader_updates()

    def _start_shader_updates(self):
        if not self._update_event:
            self._update_event = Clock.schedule_interval(
                self._update_shader_uniforms, 1.0 / 60.0
            )

    def _stop_shader_updates(self):
        if self._update_event:
            self._update_event.cancel()
            self._update_event = None

    # =========================================================================

    def _update_shader_uniforms(self, dt) -> None:
        """
        Per-frame loop calculating wobble dynamics, screen-space coordinates,
        bounding boxes, and updating GLSL uniforms.
        """

        if not self._trigger_btn or not self._dropdown_menu:
            return

        btn = self._trigger_btn
        menu = self._dropdown_menu
        screen = self._bound_screen

        if screen and hasattr(screen, "manager") and screen.manager:
            # If the manager's currently active screen is not ours, we halt
            # the calculations.
            if screen.manager.current_screen != screen:
                self._stop_shader_updates()
                return

        self.time += dt

        # Calculate exponential decay wave for physical wobble distortion.
        wobble = 0.0

        if self.is_wobbling:
            self.wobble_time += dt
            decay = math.exp(-2.5 * self.wobble_time)
            wobble = math.sin(28.0 * self.wobble_time) * decay

            if decay < 0.001:
                self.is_wobbling = False

        # Convert widget-local positions to global window space for GLSL.
        wx1, wy1 = btn.to_window(*btn.pos)
        wx2, wy2 = menu.to_window(*menu.pos)

        glass_color = getattr(
            self, "glass_color", getattr(btn, "glass_color", [1, 1, 1, 0.15])
        )
        blur_amount = getattr(
            self, "blur_amount", getattr(btn, "blur_amount", 10.0)
        )
        lens_power = getattr(
            self, "lens_power", getattr(btn, "lens_power", 0.08)
        )
        bevel_power = getattr(
            self, "bevel_power", getattr(btn, "bevel_power", 0.15)
        )
        border_opacity = getattr(
            self, "border_opacity", getattr(btn, "border_opacity", 0.6)
        )

        btn_radius = getattr(btn, "border_radius", self.border_radius)
        menu_radius = getattr(menu, "border_radius", self.border_radius)

        shared = {
            "iResolution": [float(Window.width), float(Window.height)],
            "u_pos": [float(wx1), float(wy1)],
            "u_size": [float(btn.width), float(btn.height)],
            "u_radius": self._get_shader_radius(btn_radius),
            "u_pos2": [float(wx2), float(wy2)],
            "u_size2": [float(menu.width), float(menu.height)],
            "u_radius2": self._get_shader_radius(menu_radius),
            "u_k": float(self._current_k),
            "u_menu_alpha": float(self._menu_alpha),
            "u_wobble": float(wobble),
            "u_time": float(self.time),
            "u_glass_color": [float(c) for c in glass_color],
            "u_blur_amount": float(blur_amount),
            "u_lens_power": float(lens_power),
            "u_bevel_power": float(bevel_power),
            "u_border_opacity": float(border_opacity),
            "u_pressed": float(getattr(btn, "_press_factor", 0.0)),
            "u_touch_pos": [
                float(getattr(btn, "_touch_pos", [0, 0])[0]),
                float(getattr(btn, "_touch_pos", [0, 0])[1]),
            ],
        }

        # Dynamically compute combined bounding box enclosing both shapes +
        # neck padding.
        pad = float(self._current_k) * 2.5 + dp(60)
        x1, y1 = min(wx1, wx2) - pad, min(wy1, wy2) - pad
        x2 = max(wx1 + btn.width, wx2 + menu.width) + pad
        y2 = max(wy1 + btn.height, wy2 + menu.height) + pad

        rc = getattr(btn, "_glass_rc", None)
        glass_rect = getattr(btn, "_glass_rect", None)

        if rc and glass_rect:
            for key, val in shared.items():
                rc[key] = val

            # Update full render canvas geometry.
            glass_rect.pos = (x1, y1)
            glass_rect.size = (x2 - x1, y2 - y1)

    def _prepare_glass_child(self, widget) -> None:
        """
        Injects custom liquid shaders and unbinds conflicting standard
        handlers.
        """

        if not hasattr(widget, "_glass_rc"):
            return

        widget._glass_rc.shader.vs = IOS_LIQUID_DROPDOWN_VS
        widget._glass_rc.shader.fs = IOS_LIQUID_DROPDOWN_FS

        for key in self._UNBIND_KEYS:
            try:
                widget.unbind(**{key: widget._update_glass_uniforms})
            except Exception:
                pass

    def _get_shader_radius(self, border_radius) -> list[float]:
        """
        Normalizes variable border radius inputs into a 4-float vec4 array
        ordered for GLSL shader consumption (Top-Right, Bottom-Right, Top-Left,
        Bottom-Left).
        """

        if isinstance(border_radius, (int, float)):
            border_radius = [border_radius] * 4

        tl, tr, br, bl = border_radius

        return [float(tr), float(br), float(tl), float(bl)]


class IOSLiquidDropdownContainer(
    DeclarativeBehavior,
    IOSLiquidDropdownBehavior,
    FloatLayout,
    MDAdaptiveWidget,
):
    """
    Container handling liquid drop transition logic.

    For more information see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~IOSLiquidDropdownBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout` and
    :class:`~kivymd.uix.MDAdaptiveWidget`
    class documentation.
    """

    caller = ObjectProperty()
    """
    A widget trigger (button) that initiates the droplet animation.

    :attr:`caller` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    menu = ObjectProperty()
    """
    Drop-down menu.

    :attr:`menu` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind(
            caller=self._setup_dropdown_elements,
            menu=self._setup_dropdown_elements,
        )

    def on_touch_down(self, touch):
        if not self.is_open:
            if self._trigger_btn and self._trigger_btn.collide_point(
                *touch.pos
            ):
                return super().on_touch_down(touch)

            return False

        return super().on_touch_down(touch)

    def _setup_dropdown_elements(self, *args) -> None:
        """Initializes the caller (trigger) and the menu (menu container)."""

        self._trigger_btn = self.caller
        self._dropdown_menu = self.menu

        if self._dropdown_menu:
            if self._dropdown_menu.parent:
                self.remove_widget(self._dropdown_menu)

            self._dropdown_menu.opacity = 0.0
            self._dropdown_menu.disabled = True

        if self._trigger_btn:
            self._prepare_glass_child(self._trigger_btn)

        if self._trigger_btn and self._dropdown_menu:
            self._trigger_btn.bind(
                pos=self.update_menu_position, size=self.update_menu_position
            )
            self._dropdown_menu.bind(size=self.update_menu_position)
            self.bind(
                direction=self.update_menu_position,
                spacing=self.update_menu_position,
            )
            Clock.schedule_once(self.update_menu_position, 0)
