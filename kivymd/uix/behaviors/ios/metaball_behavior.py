"""
Behaviors/iOS Metaball
======================

.. versionadded:: 2.0.1
"""

__all__ = (
    "IOSMetaballBehavior",
    "IOSMetaballContainer",
)

import math
import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty

from kivymd import glsl_path
from kivymd.uix.floatlayout import MDFloatLayout

GLSL_IOS_METABALL_PATH = os.path.join(glsl_path, "ios", "metaball")
GLSL_IOS_METABALL_VS_PATH = os.path.join(
    GLSL_IOS_METABALL_PATH, "metaball_vs.glsl"
)
GLSL_IOS_METABALL_FS_PATH = os.path.join(
    GLSL_IOS_METABALL_PATH, "metaball_fs.glsl"
)

with open(
    GLSL_IOS_METABALL_VS_PATH,
    encoding="utf-8",
) as shader_file:
    IOS_METABALL_VS = "$HEADER$\n" + shader_file.read()

with open(GLSL_IOS_METABALL_FS_PATH, encoding="utf-8") as shader_file:
    IOS_METABALL_FS = shader_file.read()


class IOSMetaballBehavior:
    """
    Behavior that implements an iOS-style liquid glass metaball effect,
    enabling dynamic fluid merging, separation animations, and surface wobble
    interactions between glass elements.
    """

    active_button_merge_transition = StringProperty("out_cubic")
    """
    Animation type for the active button during merging.

    :attr:`active_button_merge_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    active_button_merge_duration = NumericProperty(0.85)
    """
    Duration of the active button animation during merging.

    :attr:`active_button_merge_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.85`.
    """

    passive_button_merge_transition = StringProperty("out_cubic")
    """
    Animation type for the passive button during merging.

    :attr:`passive_button_merge_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    passive_button_merge_duration = NumericProperty(0.85)
    """
    Duration of the passive button animation during merging.

    :attr:`passive_button_merge_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.85`.
    """

    viscosity_merge_transition = StringProperty("out_cubic")
    """
    Animation type for smoothness of blending during merging.

    :attr:`viscosity_merge_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    viscosity_merge_duration = NumericProperty(0.85)
    """
    Duration of smoothness of blending during merging.

    :attr:`viscosity_merge_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.85`.
    """

    viscosity_separate_transition = StringProperty("out_cubic")
    """
    Animation type for smoothness of blending during merging.

    :attr:`viscosity_separate_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    viscosity_separate_duration = NumericProperty(0.85)
    """
    Duration of smoothness of blending during merging.

    :attr:`viscosity_separate_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.85`.
    """

    buttons_separate_transition = StringProperty("out_cubic")
    """
    Button animation type during separate.

    :attr:`buttons_separate_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    buttons_separate_duration = NumericProperty(0.85)
    """
    Button animation duration during separate.

    :attr:`buttons_separate_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.85`.
    """

    buttons_reset_press_state_transition = StringProperty("out_cubic")
    """
    Animation type for the pressed button state return.

    :attr:`buttons_reset_press_state_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    buttons_reset_press_state_duration = NumericProperty(0.2)
    """
    Duration of the animation for returning the button from the pressed state.

    :attr:`buttons_reset_press_state_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    merge_distance = NumericProperty(dp(12))
    """
    Additional threshold distance added to touch detection before triggering
    a merge connection event.

    :attr:`merge_distance` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(12)`.
    """

    viscosity = NumericProperty(dp(55))
    """
    Smooth union strength (u_k) governing fluid blending intensity between
    objects.

    :attr:`viscosity` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(55)`.
    """

    _current_k = NumericProperty(0.0)
    __events__ = ("on_merge", "on_separate")

    # Property keys to unbind from child's default uniform updater when
    # metaballs are active.
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
        self.was_connected = None
        self.is_merged = False
        self._initial_states = {}
        self._active_btn = None

        super().__init__(*args, **kwargs)

        Clock.schedule_interval(self._update_shader_uniforms, 1.0 / 60.0)
        Clock.schedule_once(self._setup_metaball_shader_owner)

    def on_merge(self, *args) -> None:
        """Fired when metaball objects successfully finish merging."""

    def on_separate(self, *args) -> None:
        """Fired when metaball objects successfully finish separating."""

    def toggle_state(self, sender=None) -> None | bool:
        """Toggles state between merged metaballs and separated widgets."""

        if sender.opacity <= 0.001:
            return False

        if self.is_merged:
            self.animate_separate()
        else:
            self.animate_merge(sender=sender)

    def animate_merge(self, sender=None) -> None:
        """
        Animates child widgets into a single unified metaball fluid shape.
        """

        def _on_merge_complete(anim, widget):
            self.dispatch("on_merge")

        metaballs = self._get_metaball_children()
        if len(metaballs) < 2:
            return

        # Reset the press highlight for all buttons.
        for mb in metaballs:
            self._store_initial_state(mb)
            self._reset_press_state(mb)

        active_btn = sender if sender in metaballs else metaballs[0]
        passive_btn = (
            metaballs[1] if active_btn is metaballs[0] else metaballs[0]
        )

        self._active_btn = active_btn
        self._bring_to_front(active_btn)

        # We stop only the transform animations, leaving `_press_factor`
        # untouched.
        Animation.stop_all(
            active_btn, "center_x", "center_y", "width", "height", "opacity"
        )
        Animation.stop_all(
            passive_btn, "center_x", "center_y", "width", "height", "opacity"
        )

        # Merge center - active button.
        target_center_x = active_btn.center_x
        target_center_y = active_btn.center_y

        active_btn.pos_hint = {}
        passive_btn.pos_hint = {}

        anim_active = Animation(
            center_x=target_center_x,
            center_y=target_center_y,
            width=active_btn.width,
            height=active_btn.height,
            d=self.active_button_merge_duration,
            t=self.active_button_merge_transition,
        )
        anim_passive = Animation(
            center_x=target_center_x,
            center_y=target_center_y,
            width=active_btn.width,
            height=active_btn.height,
            opacity=0.0,
            d=self.passive_button_merge_duration,
            t=self.passive_button_merge_transition,
        )

        anim_active.bind(on_complete=_on_merge_complete)
        anim_active.start(active_btn)
        anim_passive.start(passive_btn)

        self.is_merged = True
        Animation(
            _current_k=self.viscosity,
            d=self.viscosity_merge_duration,
            t=self.viscosity_merge_transition,
        ).start(self)

    def animate_separate(self) -> None:
        """
        Animates merged metaball shapes back to their individual initial
        states.
        """

        metaballs = self._get_metaball_children()

        # Reset the press highlight for all buttons.
        for mb in metaballs:
            self._reset_press_state(mb)

        for child in list(self._initial_states.keys()):
            if child in self.children:
                self.remove_widget(child)
                self.add_widget(child)

        if len(metaballs) < 2:
            return

        self.is_merged = False
        Animation(
            _current_k=0.0,
            d=self.viscosity_separate_duration,
            t=self.viscosity_separate_transition,
        ).start(self)

        for i, mb in enumerate(metaballs):
            # We stop only the transform animations, leaving `_press_factor`
            # untouched.
            Animation.stop_all(
                mb, "center_x", "center_y", "width", "height", "opacity"
            )
            mb.pos_hint = {}

            state = self._initial_states.get(mb, {})
            saved_hint = state.get("pos_hint", {})
            target_w = state.get("width", mb.width)
            target_h = state.get("height", mb.height)

            # Calculation of reverse coordinates:
            # If pos_hint had center_x, take it relative to the container.
            # Otherwise, return exactly to the original x_offset in pixels.
            cx_hint = state.get("center_x_hint")
            cy_hint = state.get("center_y_hint")

            if cx_hint is not None:
                target_cx = self.x + self.width * cx_hint
            else:
                target_cx = self.x + state.get("x_offset", 0) + target_w * 0.5

            if cy_hint is not None:
                target_cy = self.y + self.height * cy_hint
            else:
                target_cy = self.y + state.get("y_offset", 0) + target_h * 0.5

            if state.get("border_radius"):
                mb.border_radius = list(state["border_radius"])

            def _restore_state(
                anim,
                widget,
                hint_to_restore=saved_hint,
                is_last=(i == len(metaballs) - 1),
            ):
                if not self.is_merged and hint_to_restore:
                    widget.pos_hint = dict(hint_to_restore)

                s_rect = getattr(widget, "_glass_rect", None)

                if s_rect:
                    s_rect.size = (widget.width, widget.height)
                if is_last:
                    self.dispatch("on_separate")

            anim = Animation(
                center_x=target_cx,
                center_y=target_cy,
                width=target_w,
                height=target_h,
                opacity=1.0,
                d=self.buttons_separate_duration,
                t=self.buttons_separate_transition,
            )
            anim.bind(on_complete=_restore_state)
            anim.start(mb)

    def _setup_metaball_shader_owner(self, dt) -> None:
        """
        Assigns the primary rendering owner for the shared shader context.
        """

        metaballs = self._get_metaball_children()

        if len(metaballs) < 2:
            return

        owner = metaballs[-1]

        for mb in metaballs:
            mb._metaball_shader_owner = mb is owner

    def _prepare_child(self, widget) -> None:
        """
        Attaches the metaball custom GLSL shader to a child widget if it has
        not been applied yet.
        """

        if not hasattr(widget, "_glass_rc"):
            return

        if getattr(widget, "_metaball_shader_owner", None) in (True, False):
            return

        widget._glass_rc.shader.vs = IOS_METABALL_VS
        widget._glass_rc.shader.fs = IOS_METABALL_FS

        # Unbind standard glass render callbacks to avoid redundant GPU calls.
        for key in self._UNBIND_KEYS:
            try:
                widget.unbind(**{key: widget._update_glass_uniforms})
            except Exception:
                pass

        widget._metaball_shader_owner = False

    def _bring_to_front(self, widget) -> None:
        """
        Brings the designated widget to the top of the canvas Z-order index.
        """

        if widget.parent is self:
            self.remove_widget(widget)
            self.add_widget(widget, index=0)

    def _store_initial_state(self, widget) -> None:
        """
        Caches the unmerged original position, layout hints, and dimensions of
        a child.
        """

        if widget in self._initial_states:
            state = self._initial_states[widget]
            state["width"] = widget.width
            state["height"] = widget.height

            return

        pos_hint = dict(widget.pos_hint) if widget.pos_hint else {}

        # If there is pos_hint, save relative hints
        # If straight lines x/y are specified, we save the exact offsets in
        # pixels from the container.
        self._initial_states[widget] = {
            "center_x_hint": pos_hint.get("center_x"),
            "center_y_hint": pos_hint.get("center_y"),
            "x_offset": widget.x - self.x,
            "y_offset": widget.y - self.y,
            "width": widget.width,
            "height": widget.height,
            "pos_hint": pos_hint,
            "border_radius": list(getattr(widget, "border_radius", [0] * 4)),
        }

    def _get_metaball_children(self) -> list:
        """Returns a list of valid metaball-enabled glass children."""

        return [
            child
            for child in self.children
            if hasattr(child, "_glass_rc")
            and hasattr(child, "_metaball_shader_owner")
        ]

    def _check_contact(self, metaballs) -> None:
        """
        Calculates distance between two metaballs to trigger edge wobble
        oscillations on touch/break boundaries.
        """

        if len(metaballs) < 2:
            return

        p1, p2 = metaballs[0].center, metaballs[1].center
        dx, dy = p1[0] - p2[0], p1[1] - p2[1]
        distance = math.sqrt(dx * dx + dy * dy)

        threshold = (
            metaballs[0].width + metaballs[1].width
        ) * 0.45 + self.merge_distance
        is_connected = distance < threshold

        if self.was_connected is None:
            self.was_connected = is_connected
            return

        if is_connected != self.was_connected:
            self.is_wobbling = True
            self.wobble_time = 0.0
            self.was_connected = is_connected

    def _get_shader_radius(self, border_radius) -> list[float]:
        """
        Converts Kivy border radius array to match GLSL shader uniform format.
        """

        tl, tr, br, bl = border_radius

        return [float(tr), float(br), float(tl), float(bl)]

    def _render_single(self, mb):
        """Fallback rendering routine for standalone single glass elements."""

        mb._metaball_shader_owner = True
        mb._update_glass_uniforms()

        rc = getattr(mb, "_glass_rc", None)

        if not rc:
            return

        wx, wy = mb.to_window(*mb.pos)
        radius = self._get_shader_radius(mb.border_radius)

        rc["u_k"] = 0.0
        rc["u_wobble"] = 0.0
        rc["u_time"] = float(self.time)
        rc["u_pos2"] = [float(wx), float(wy)]
        rc["u_size2"] = [float(mb.width), float(mb.height)]
        rc["u_radius2"] = radius

    def _update_shader_uniforms(self, dt) -> None:
        """
        Pushes current positioning, resolution, wobble, and SDF variables to
        GLSL shader.
        """

        metaballs = self._get_metaball_children()

        if not metaballs or not Window.width or not Window.height:
            return

        if len(metaballs) == 1:
            self._render_single(metaballs[0])

            return

        self.time += dt
        self._check_contact(metaballs)

        if not self.is_merged and self._current_k <= 0.001:
            for mb in metaballs:
                if hasattr(mb, "_update_glass_uniforms"):
                    mb._update_glass_uniforms()

            return

        # Calculate decay factor for organic liquid border oscillation.
        wobble = 0.0

        if self.is_wobbling:
            self.wobble_time += dt
            decay = math.exp(-5.5 * self.wobble_time)
            wobble = math.sin(28.0 * self.wobble_time) * decay

            if decay < 0.005:
                self.is_wobbling = False

        b1, b2 = metaballs[0], metaballs[1]
        active_mb = self._active_btn if self._active_btn in metaballs else b1

        wx1, wy1 = b1.to_window(*b1.pos)
        wx2, wy2 = b2.to_window(*b2.pos)

        shared = {
            "iResolution": [float(Window.width), float(Window.height)],
            "u_pos": [float(wx1), float(wy1)],
            "u_size": [float(b1.width), float(b1.height)],
            "u_radius": self._get_shader_radius(b1.border_radius),
            "u_pos2": [float(wx2), float(wy2)],
            "u_size2": [float(b2.width), float(b2.height)],
            "u_radius2": self._get_shader_radius(b2.border_radius),
            "u_k": float(self._current_k),
            "u_wobble": float(wobble),
            "u_time": float(self.time),
            "u_glass_color": [float(c) for c in active_mb.glass_color],
            "u_blur_amount": float(active_mb.blur_amount),
            "u_lens_power": float(active_mb.lens_power),
            "u_bevel_power": float(active_mb.bevel_power),
            "u_pressed": float(active_mb._press_factor),
            "u_container_opacity": float(self.opacity),
            "u_touch_pos": [
                float(active_mb._touch_pos[0]),
                float(active_mb._touch_pos[1]),
            ],
        }

        # Calculate bounding box with padding to prevent clipping during
        # liquid morphing.
        pad = float(self._current_k) * 2.5 + dp(24)
        x1, y1 = min(b1.x, b2.x) - pad, min(b1.y, b2.y) - pad
        x2, y2 = max(b1.right, b2.right) + pad, max(b1.top, b2.top) + pad

        owner = next(
            (
                mb
                for mb in metaballs
                if getattr(mb, "_metaball_shader_owner", False)
            ),
            b1,
        )
        rc = getattr(owner, "_glass_rc", None)
        glass_rect = getattr(owner, "_glass_rect", None)

        if rc and glass_rect:
            for key, value in shared.items():
                rc[key] = value
            glass_rect.pos = (x1, y1)
            glass_rect.size = (x2 - x1, y2 - y1)

        # Hide non-owner glass mesh rectangles so only owner renders single
        # unified quad.
        for mb in metaballs:
            if mb is not owner:
                r = getattr(mb, "_glass_rect", None)
                if r:
                    r.size = (0, 0)

    def _reset_press_state(self, mb) -> None:
        """Forces the button's pressed state back to normal."""

        if hasattr(mb, "_press_factor"):
            Animation.stop_all(mb, "_press_factor")
            Animation(
                _press_factor=0.0,
                d=0.2,
                t=self.buttons_reset_press_state_transition,
            ).start(mb)

        if hasattr(mb, "state"):
            mb.state = "normal"


class IOSMetaballContainer(IOSMetaballBehavior, MDFloatLayout):
    """
    Layout container managing liquid metaball UI components, layout bindings,
    and widget life cycles.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.metaball_behavior.IOSMetaballBehavior` and
    :class:`~kivymd.uix.floatlayout.MDFloatLayout`
    classes documentation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bind(size=self._on_size)

    def on_parent(self, instance, parent) -> None:
        """Stops the schedule when the container is deleted."""

        if parent is None:
            Clock.unschedule(self._update_shader_uniforms)

    def add_widget(self, widget, *args, **kwargs) -> None:
        super().add_widget(widget, *args, **kwargs)

        self._prepare_child(widget)

        if (
            hasattr(widget, "_glass_rc")
            and hasattr(widget, "_metaball_shader_owner")
            and widget not in self._initial_states
        ):
            Clock.schedule_once(lambda dt: self._store_initial_state(widget))

    def _on_size(self, instance, value) -> None:
        """Recalculates position hints and centers when container resizes."""

        if not self.width or not self.height:
            return

        center_x = self.x + self.width * 0.5
        center_y = self.y + self.height * 0.5

        for mb, state in self._initial_states.items():
            if self.is_merged:
                mb.center_x = center_x
                mb.center_y = center_y
            elif state.get("pos_hint"):
                mb.pos_hint = dict(state["pos_hint"])
