"""
Behaviors/iOS Glass
===================

.. versionadded:: 2.0.1

.. rubric:: Classes implements an iOS-style liquid glass effect.

To create a widget with glass effect, you must create a new class
that inherits from the :class:`~IOSGlassBehavior` class.

Example
-------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.boxlayout import BoxLayout

            from kivymd.uix.behaviors import IOSGlassBehavior
            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                FitImage:
                    id: bg_image
                    source: "https://picsum.photos/800/600?random=2"

                GlassContainer:
                    target_background: bg_image
                    border_radius: [dp(26), dp(26), dp(26), dp(26)]
                    glass_color: [1.0, 1.0, 1.0, 0.18]
                    blur_amount: 10.0
                    size_hint: None, None
                    size: "400dp", "200dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class GlassContainer(IOSGlassBehavior, BoxLayout):
                pass


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.uix.boxlayout import BoxLayout

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import IOSGlassBehavior
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen


            class MyScreen(MDScreen):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    bg_image = FitImage(source="https://picsum.photos/800/600?random=2")
                    self.widgets = [
                        bg_image,
                        GlassContainer(
                            target_background=bg_image,
                            border_radius=[dp(26), dp(26), dp(26), dp(26)],
                            glass_color=[1.0, 1.0, 1.0, 0.18],
                            blur_amount=10.0,
                            size_hint=(None, None),
                            size=("400dp", "200dp"),
                            pos_hint={"center_x": .5, "center_y": .5},
                        ),
                    ]


            class GlassContainer(IOSGlassBehavior, BoxLayout):
                pass


            class Example(MDApp):
                def build(self):
                    return MyScreen()


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-glass-container.png
    :align: center
"""

__all__ = ("IOSGlassBehavior",)

import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Fbo, RenderContext, SmoothRectangle
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    VariableListProperty,
)

from kivymd import glsl_path

GLSL_IOS_BUTTON_PATH = os.path.join(glsl_path, "ios", "glass")
GLSL_IOS_BUTTON_VS_PATH = os.path.join(
    GLSL_IOS_BUTTON_PATH, "liquid_glass_vs.glsl"
)
GLSL_IOS_BUTTON_FS_PATH = os.path.join(
    GLSL_IOS_BUTTON_PATH, "liquid_glass_fs.glsl"
)

_SHARED_FBOS = {}

with open(
    GLSL_IOS_BUTTON_VS_PATH,
    encoding="utf-8",
) as shader_file:
    IOS_BUTTON_VS = "$HEADER$\n" + shader_file.read()

with open(GLSL_IOS_BUTTON_FS_PATH, encoding="utf-8") as shader_file:
    IOS_BUTTON_FS = shader_file.read()


class IOSGlassBehavior:
    """
    Behavior that implements an iOS-style liquid glass effect with blur,
    refraction, and touch response.
    """

    border_radius = VariableListProperty([dp(12)] * 4)
    """
    Border radius for the glass corners in the order (Top-Left, Top-Right,
    Bottom-Right, Bottom-Left).

    .. code-block:: python

        GlassContainer(
            border_radius=[dp(46), dp(46), dp(26), dp(26)],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/glass-behavior-border-radius.png
        :align: center

    :attr:`border_radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(12), dp(12), dp(12), dp(12)]`.
    """

    glass_color = ColorProperty([1.0, 1.0, 1.0, 0.15])
    """
    Tint color of the glass in (r, g, b, a) format.

    .. code-block:: python

        GlassContainer(
            glass_color=[1.0, 0.0, 0.0, 0.48],
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/glass-behavior-glass-color.png
        :align: center

    :attr:`glass_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1.0, 1.0, 1.0, 0.15]`.
    """

    blur_amount = NumericProperty(10.0)
    """
    Amount of background blur applied inside the glass widget.

    .. code-block:: python

        GlassContainer(
            blur_amount=20.0,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/glass-behavior-blur-amount.png
        :align: center

    :attr:`blur_amount` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `14.0`.
    """

    target_background = ObjectProperty(None, allownone=True)
    """
    Reference to the background widget or layout captured by the glass shader.

    .. code-block:: python

        class MyScreen(MDScreen):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.widgets = [
                    FitImage(source="https://picsum.photos/800/600?random=2"),
                    GlassContainer(
                        target_background=self,
                    ),
                ]

    Example
    -------

    .. tabs::

        .. tab:: Imperative Python style

            .. code-block:: python

                from kivy.lang import Builder
                from kivy.properties import StringProperty

                from kivymd.app import MDApp
                from kivymd.uix.button import IOSButton
                from kivymd.uix.list import (
                    MDListItem,
                    MDListItemHeadlineText,
                    MDListItemLeadingAvatar,
                    MDListItemSupportingText, MDListItemTrailingCheckbox,
                )

                from faker import Faker  # pip install Faker

                KV = '''
                <CommonIOSButton>
                    size_hint: None, None
                    width: "56dp"
                    height: "56dp"
                    border_radius: [dp(28), dp(28), dp(28), dp(28)]
                    glass_color: [1.0, 1.0, 1.0, 0.08]
                    blur_amount: 3.0

                    IOSIconButton:
                        icon: root.icon

                MDScreen:

                    MDScrollView:
                        id: scroll

                        MDGridLayout:
                            id: grid
                            size_hint_y: None
                            height: self.minimum_height
                            cols: 1

                    CommonIOSButton:
                        target_background: scroll
                        icon: "view-grid"
                        x: dp(24)
                        y: root.height - (self.height + dp(24))

                    CommonIOSButton:
                        target_background: scroll
                        icon: "check"
                        x: root.width - (self.width + dp(24))
                        y: root.height - (self.height + dp(24))
                '''


                class CommonIOSButton(IOSButton):
                    icon = StringProperty("blank")


                class TestApp(MDApp):
                    def on_start(self):
                        fake = Faker("en_US")

                        for i in range(40):
                            bg_color = (0.2, 0.2, 0.2, 0.4) if i % 2 == 0 else (0, 0, 0, 0)
                            list_item = MDListItem(
                                theme_bg_color="Custom", md_bg_color=bg_color
                            )
                            leading_avatar = MDListItemLeadingAvatar(
                                source=f"https://picsum.photos/800/600?random={i}"
                            )
                            headline_text = MDListItemHeadlineText(text=fake.name())
                            supporting_text = MDListItemSupportingText(text=fake.job())
                            trailing_checkbox = MDListItemTrailingCheckbox()

                            list_item.add_widget(leading_avatar)
                            list_item.add_widget(headline_text)
                            list_item.add_widget(supporting_text)
                            list_item.add_widget(trailing_checkbox)

                            self.root.ids.grid.add_widget(list_item)

                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        return Builder.load_string(KV)


                if __name__ == "__main__":
                    TestApp().run()

        .. tab:: Declarative Python style

            .. code-block:: python

                from kivy.metrics import dp
                from kivy.properties import StringProperty

                from kivymd.app import MDApp
                from kivymd.uix.button import IOSButton, IOSIconButton
                from kivymd.uix.gridlayout import MDGridLayout
                from kivymd.uix.list import (
                    MDListItem,
                    MDListItemHeadlineText,
                    MDListItemLeadingAvatar,
                    MDListItemSupportingText,
                    MDListItemTrailingCheckbox,
                )
                from kivymd.uix.screen import MDScreen
                from kivymd.uix.scrollview import MDScrollView

                from faker import Faker  # pip install Faker


                class CommonIOSButton(IOSButton):
                    icon = StringProperty("blank")

                    def __init__(self, **kwargs):
                        super().__init__(**kwargs)

                        self.size_hint = (None, None)
                        self.size = (dp(56), dp(56))
                        self.border_radius = [dp(28)] * 4
                        self.glass_color = [1.0, 1.0, 1.0, 0.08]
                        self.blur_amount = 3.0

                        self.widgets = [
                            IOSIconButton(
                                icon=self.icon,
                            )
                        ]


                class MyScreen(MDScreen):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                        scroll = MDScrollView(
                            MyGridLayout()
                        )

                        self.bind(size=self._update_buttons_pos)

                        self.widgets = [
                            scroll,
                            CommonIOSButton(
                                id="view_grid_button",
                                icon="view-grid",
                                target_background=scroll,
                            ),
                            CommonIOSButton(
                                id="check_button",
                                icon="check",
                                target_background=scroll,
                            ),
                        ]

                    def _update_buttons_pos(self, instance, size):
                        screen_width, screen_height = size
                        view_grid_button = self.get_ids().view_grid_button
                        check_button = self.get_ids().check_button

                        view_grid_button.x = dp(24)
                        view_grid_button.y = screen_height - (view_grid_button.height + dp(24))

                        check_button.x = screen_width - (check_button.width + dp(24))
                        check_button.y = screen_height - (check_button.height + dp(24))


                class MyGridLayout(MDGridLayout):
                    def __init__(self, *args, **kwargs):
                        super().__init__(*args, **kwargs)

                        self.cols = 1
                        self.size_hint_y = None
                        self.bind(minimum_height=self.setter("height"))

                        fake = Faker("en_US")
                        self.widgets = [
                            MDListItem(
                                MDListItemLeadingAvatar(
                                    source=f"https://picsum.photos/800/600?random={i}"
                                ),
                                MDListItemHeadlineText(text=fake.name()),
                                MDListItemSupportingText(text=fake.job()),
                                MDListItemTrailingCheckbox(),
                                theme_bg_color="Custom",
                                md_bg_color=(0.2, 0.2, 0.2, 0.4) if i % 2 == 0 else (0, 0, 0, 0),
                            ) for i in range(40)
                        ]


                class TestApp(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        return MyScreen()


                if __name__ == "__main__":
                    TestApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/glass-behavior-background.gif
        :align: center

    :attr:`target_background` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _scale_factor = NumericProperty(1.0)
    _touch_pos = ListProperty([0, 0])
    _press_factor = NumericProperty(0.0)

    def __init__(self, **kwargs):
        self._attached_bg = None
        super().__init__(**kwargs)

        self._fbo = None
        self._glass_rc = RenderContext(
            use_parent_projection=True, use_parent_modelview=True
        )
        self._glass_rc.shader.vs = IOS_BUTTON_VS
        self._glass_rc.shader.fs = IOS_BUTTON_FS

        with self._glass_rc:
            self._glass_rect = SmoothRectangle(size=self.size, pos=self.pos)

        self.canvas.before.add(self._glass_rc)

        self.bind(
            pos=self._update_glass_uniforms,
            size=self._update_glass_uniforms,
            border_radius=self._update_glass_uniforms,
            glass_color=self._update_glass_uniforms,
            blur_amount=self._update_glass_uniforms,
            _press_factor=self._update_glass_uniforms,
            _scale_factor=self._update_glass_uniforms,
            _touch_pos=self._update_glass_uniforms,
        )
        Window.bind(size=self._on_glass_window_resize)
        Clock.schedule_once(self._on_bg_update, 1)

    def on_target_background(self, instance, value):
        """Fired when the value of the :attr:`target_background` attribute changes."""

        # 1. Detach the old background when changing or clearing it.
        if hasattr(self, "_attached_bg") and self._attached_bg:
            self._unbind_bg_events(self._attached_bg)
            self._attached_bg = None

        if not value:
            return

        # 2. We attach the new background.
        self._attached_bg = value

        def _bind_widget(w):
            if not hasattr(w, "bind"):
                return

            # We bind each property SEPARATELY so that the absence of one
            # doesn't break the others.
            for prop in ("scroll_y", "scroll_x", "pos", "size", "texture"):
                if hasattr(w, prop) or (
                    hasattr(w, "properties") and prop in w.properties()
                ):
                    try:
                        w.bind(**{prop: self._on_bg_update_scheduled})
                    except Exception:
                        pass

            # Subscribing to the 'on_load' event for AsyncImage.
            if hasattr(w, "is_event_type") and w.is_event_type("on_load"):
                try:
                    w.bind(on_load=self._on_bg_update_scheduled)
                except Exception:
                    pass

        # 1. Subscribe to the background itself (ScrollView, FitImage, etc.).
        _bind_widget(value)

        # 2. Adding children
        #    (AsyncImage inside FitImage, Layout inside ScrollView).
        if hasattr(value, "children"):
            for child in value.children:
                _bind_widget(child)

        Clock.schedule_once(lambda dt: self._setup_glass_fbo(), 0.4)

    def on_parent(self, instance, parent):
        """Cleanup when removing a widget from the layout."""

        if parent is None:
            try:
                Window.unbind(size=self._on_glass_window_resize)
            except Exception:
                pass

            Clock.unschedule(self._on_bg_update)
            Clock.unschedule(self._on_bg_update_scheduled)

            if hasattr(self, "_attached_bg") and self._attached_bg:
                self._unbind_bg_events(self._attached_bg)
                self._attached_bg = None

    def _on_bg_update_scheduled(self, *args):
        """
        Defers the FBO redraw by one frame to allow Kivy time to update the
        canvas with the texture.
        """

        Clock.unschedule(self._on_bg_update)
        Clock.schedule_once(self._on_bg_update, 0)

    def _update_glass_uniforms(self, *args):
        if not hasattr(self, "_glass_rect"):
            return

        self._glass_rect.pos = self.pos
        self._glass_rect.size = self.size

        scaled_w = float(self.size[0] * self._scale_factor)
        scaled_h = float(self.size[1] * self._scale_factor)
        scaled_x = float(self.center_x - scaled_w / 2.0)
        scaled_y = float(self.center_y - scaled_h / 2.0)

        r = self.border_radius
        radius_vec = [
            float(r[0]) * self._scale_factor,
            float(r[1]) * self._scale_factor,
            float(r[2]) * self._scale_factor,
            float(r[3]) * self._scale_factor,
        ]

        self._glass_rc["iResolution"] = [
            float(Window.width),
            float(Window.height),
        ]
        self._glass_rc["u_pos"] = [scaled_x, scaled_y]
        self._glass_rc["u_size"] = [scaled_w, scaled_h]
        self._glass_rc["u_radius"] = radius_vec
        self._glass_rc["u_glass_color"] = list(self.glass_color)
        self._glass_rc["u_blur_amount"] = float(self.blur_amount)
        self._glass_rc["u_pressed"] = float(self._press_factor)
        self._glass_rc["u_touch_pos"] = [
            float(self._touch_pos[0]),
            float(self._touch_pos[1]),
        ]

        if self._fbo and self.target_background:
            self._fbo.draw()

    def _draw_bg_to_fbo(self, fbo, bg):
        """
        Background rendering while preserving the original Z-index (layer).
        """

        if not bg or not hasattr(bg, "canvas"):
            return

        # Clearing the FBO before re-rendering.
        fbo.bind()
        fbo.clear_color = (0, 0, 0, 0)
        fbo.clear_buffer()
        fbo.release()

        bg_canvas = bg.canvas
        parent_widget = bg.parent

        if parent_widget and hasattr(parent_widget, "canvas"):
            parent_canvas = parent_widget.canvas

            if bg_canvas in parent_canvas.children:
                # 1. We note the exact position of the list in the rendering
                # queue.
                index = parent_canvas.children.index(bg_canvas)

                # 2. Rendering to an FBO.
                parent_canvas.remove(bg_canvas)
                fbo.add(bg_canvas)
                fbo.draw()
                fbo.remove(bg_canvas)

                # 3. Return the canvas STRICTLY to its original layer
                # (BENEATH the buttons).
                parent_canvas.insert(index, bg_canvas)
            else:
                fbo.add(bg_canvas)
                fbo.draw()
                fbo.remove(bg_canvas)
        else:
            fbo.add(bg_canvas)
            fbo.draw()
            fbo.remove(bg_canvas)

    def _on_bg_update(self, *args):
        if self.target_background:
            bg_id = id(self.target_background)

            if bg_id in _SHARED_FBOS:
                fbo = _SHARED_FBOS[bg_id]["fbo"]
                self._draw_bg_to_fbo(fbo, self.target_background)
                self._update_glass_uniforms()

    def _setup_glass_fbo(self):
        if not hasattr(self, "_glass_rect") or not self.target_background:
            return

        if Window.width <= 0 or Window.height <= 0:
            return

        bg_id = id(self.target_background)

        if bg_id not in _SHARED_FBOS or _SHARED_FBOS[bg_id]["size"] != list(
            Window.size
        ):
            _SHARED_FBOS[bg_id] = {
                "fbo": Fbo(size=Window.size, with_stencilbuffer=True),
                "size": list(Window.size),
            }

        self._fbo = _SHARED_FBOS[bg_id]["fbo"]

        # Capture the background using a safe method.
        self._draw_bg_to_fbo(self._fbo, self.target_background)

        self._glass_rect.texture = self._fbo.texture
        self._update_glass_uniforms()

    def _on_glass_window_resize(self, instance, size):
        if size[0] > 0 and size[1] > 0:
            self._setup_glass_fbo()

    def _unbind_bg_events(self, widget):
        """Detachment of events from the widget and its children."""

        if not widget:
            return

        def _unbind_widget(w):
            if not hasattr(w, "unbind"):
                return

            for prop in ("scroll_y", "scroll_x", "pos", "size", "texture"):
                if hasattr(w, prop) or (
                    hasattr(w, "properties") and prop in w.properties()
                ):
                    try:
                        w.unbind(**{prop: self._on_bg_update_scheduled})
                    except Exception:
                        pass

            if hasattr(w, "is_event_type") and w.is_event_type("on_load"):
                try:
                    w.unbind(on_load=self._on_bg_update_scheduled)
                except Exception:
                    pass

        _unbind_widget(widget)

        if hasattr(widget, "children"):
            for child in widget.children:
                _unbind_widget(child)
