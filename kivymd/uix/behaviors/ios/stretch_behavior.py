"""
Behaviors/iOS Stretch
=====================

.. versionadded:: 2.0.1

The IOSStretchBehavior class is a KivyMD behavior that implements a stretching
(rubber-band) effect for iOS-style widgets. When applied to a widget
(such as IOSButton), it enables the widget to stretch non-uniformly like rubber
when touched and dragged, with contents (text/icon) stretching along with the
container, and smoothly returning to normal state upon release.

Key Features:

- Expansion-only stretching: Widget expands in any drag direction but never
  shrinks/compresses
- Minimal effect: Maximum expansion limited to 20% (scale factor 1.0 → 1.2) for
  subtle visual feedback
- Direction-sensitive: Uses absolute touch delta values so stretching occurs
  regardless of drag direction (left/right/up/down)
- Smooth reset: Implements damped animation (damping factor 0.85) to return to
  normal state on touch release
- Glass effect integration: Properly updates shader uniforms and glass
  rectangle dimensions to maintain visual correctness during stretch
- Content stretching: Applies canvas transformation (PushMatrix/Scale/PopMatrix)
  ensuring both glass effect and widget children stretch uniformly

Example
-------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.boxlayout import BoxLayout

            from kivymd.uix.behaviors import IOSGlassBehavior, IOSStretchBehavior
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


            class GlassContainer(IOSStretchBehavior, IOSGlassBehavior, BoxLayout):
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
            from kivymd.uix.behaviors import IOSGlassBehavior, IOSStretchBehavior
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


            class GlassContainer(IOSStretchBehavior, IOSGlassBehavior, BoxLayout):
                pass


            class Example(MDApp):
                def build(self):
                    return MyScreen()


            Example().run()
"""

__all__ = ("IOSStretchBehavior",)

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import PopMatrix, PushMatrix, Scale
from kivy.properties import BooleanProperty, ListProperty, NumericProperty


class IOSStretchBehavior:
    """
    Behavior that implements a stretching (rubber-band) effect for iOS-style
    widgets.
    """

    # Stretch effect properties.
    _stretch_factor = ListProperty([1.0, 1.0])  # [x_scale, y_scale]
    _initial_touch = ListProperty([0, 0])
    _is_stretching = BooleanProperty(False)
    _stretch_damping = NumericProperty(
        0.85
    )  # damping factor for returning to normal
    # Base size (non‑stretched) – used to keep the widget’s bounding box
    # in sync with the visual stretch so that nothing gets clipped.
    _base_size = ListProperty([0, 0])
    # Flag to prevent recursive calls when adjusting size/pos
    # (plain attribute, not a Property, to avoid triggering property machinery).
    _syncing_size = False

    def __init__(self, **kwargs):
        self._touch_offset = [0, 0]  # offset between touch and widget center
        # Initialize base size – will be set on first size assignment.
        self._base_size = [0, 0]
        # Initialize sync flag.
        self._syncing_size = False
        # Time of last stretch update (to throttle size/pos changes).
        self._last_stretch_update_time = 0

        super().__init__(**kwargs)

        self.bind(
            _stretch_factor=self._update_glass_uniforms,
        )

        # Remove the glass render context from canvas.before so we can insert
        # our transformation instructions before it, ensuring the stretch
        # transformation is applied to the glass effect.
        if hasattr(self, "_glass_rc"):
            glass_rc = self._glass_rc
            self.canvas.before.remove(glass_rc)
        else:
            glass_rc = None

        # Initialize canvas transformation instructions for stretch effect.
        with self.canvas.before:
            self._stretch_push = PushMatrix()
            self._stretch_scale = Scale(1.0, 1.0, 1)
            # Re-add the glass render context so it is drawn after the
            # transformation.
            if glass_rc is not None:
                self.canvas.before.add(glass_rc)

        with self.canvas.after:
            self._stretch_pop = PopMatrix()

        # Set initial transformation (identity).
        self._update_stretch_transformation()

    def on_size(self, *args):
        # Update base size when size changes, unless we are currently adjusting
        # size for stretch or actively stretching.
        if not self._syncing_size and not self._is_stretching:
            self._base_size = list(self.size)

    def _sync_size_to_stretch(self, width=None, height=None, x=None, y=None):
        """
        Ensure the widget's bounding box matches the current visual stretch
        so that Kivy's scissor test does not clip the stretched glass. If
        width, height, x, y are provided, they are used directly. Otherwise,
        the size/pos are computed from _base_size and _stretch_factor. Only
        modifies bounds when stretching is significant enough to prevent
        interference with tap animations.
        """

        # Prevent recursive entry.
        if self._syncing_size:
            return
        self._syncing_size = True

        try:
            if not hasattr(self, "_glass_rect"):
                return

            # Set base size if not yet set and we are not currently stretching.
            if self._base_size == [0, 0] and not self._is_stretching:
                self._base_size = list(self.size)

            if width is None or height is None or x is None or y is None:
                base_w, base_h = self._base_size
                sx, sy = self._stretch_factor

                # Desired visual size after stretch.
                visual_w = base_w * sx
                visual_h = base_h * sy

                # How much we need to expand on each side to keep the visual
                # centered.
                dx = (visual_w - base_w) / 2.0
                dy = (visual_h - base_h) / 2.0

                width = visual_w
                height = visual_h
                x = self.x - dx
                y = self.y - dy

                # Only modify bounds if stretching is significant enough to
                # avoid interfering with tap animations. For very small
                # stretches (tap-like movements), we skip bounds modification
                # to let ButtonBehavior's scaling animation work smoothly.
                stretch_threshold = 1.002  # 0.2% stretch threshold

                if sx < stretch_threshold and sy < stretch_threshold:
                    # Stretch is too small to warrant bounds modification -
                    # likely just tap-related micro-movements
                    return

            # Adjust pos and size so the widget's bbox exactly covers the
            # stretched glass. We modify the actual Kivy properties – this
            # moves the scissor rectangle.
            self.size = (width, height)
            self.pos = (x, y)
        finally:
            self._syncing_size = False

    def _update_stretch_transformation(self):
        """
        Update the canvas transformation to apply the current stretch factor.
        """

        if hasattr(self, "_stretch_scale"):
            # Center the transformation on the widget's center.
            self._stretch_scale.origin = self.center
            self._stretch_scale.x = self._stretch_factor[0]
            self._stretch_scale.y = self._stretch_factor[1]

    def on_touch_down(self, touch):
        """Handle touch down events to initiate stretching effect."""

        if not self.disabled and self.collide_point(touch.x, touch.y):
            # Record initial touch position relative to widget center.
            self._initial_touch = [
                touch.x - self.center_x,
                touch.y - self.center_y,
            ]
            self._is_stretching = True
            # Calculate offset for maintaining touch point during stretch.
            self._touch_offset = [touch.x - self.x, touch.y - self.y]

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        """Handle touch move events to update stretching effect."""

        if self._is_stretching:
            # Calculate touch delta from initial position.
            delta_x = touch.x - self.center_x - self._initial_touch[0]
            delta_y = touch.y - self.center_y - self._initial_touch[1]

            # Calculate stretch factors based on movement.
            # Use absolute delta to ensure stretching only (expansion) in any
            # direction.
            stretch_x = 1.0 + (abs(delta_x) / self.width) * 0.02
            stretch_y = 1.0 + (abs(delta_y) / self.height) * 0.02

            # Clamp to reasonable values to prevent extreme distortion.
            # Minimum is 1.0 (no stretching), maximum is 1.2 for minimal
            # stretching effect.
            stretch_x = max(1.0, min(1.2, stretch_x))
            stretch_y = max(1.0, min(1.2, stretch_y))

            self._stretch_factor = [stretch_x, stretch_y]

            # Update touch position for shader effects.
            self._touch_pos = [touch.x, touch.y]
            self._press_factor = 1.0

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        """Handle touch up events to reset stretching effect."""

        was_stretching = self._is_stretching
        if was_stretching:
            self._is_stretching = False
            # Animate back to normal state.
            Clock.schedule_once(lambda dt: self._animate_reset_stretch(), 0.016)

        # Let superclass handle the touch event.
        result = super().on_touch_up(touch)

        # Ensure stretching reset happens even if superclass consumes the event.
        if was_stretching and self._is_stretching:
            # This shouldn't happen, but just in case
            self._is_stretching = False
            Clock.schedule_once(lambda dt: self._animate_reset_stretch(), 0.016)

        return result

    def _animate_reset_stretch(self):
        """Animate the stretch factor back to [1.0, 1.0] with damping."""

        current_x, current_y = self._stretch_factor
        target_x, target_y = 1.0, 1.0

        # Apply damping.
        new_x = current_x + (target_x - current_x) * self._stretch_damping
        new_y = current_y + (target_y - current_y) * self._stretch_damping

        # Check if we're close enough to target.
        if abs(new_x - target_x) < 0.01 and abs(new_y - target_y) < 0.01:
            self._stretch_factor = [1.0, 1.0]
            self._press_factor = 0.0

            # Restore original size and position when stretch is finished.
            if self._base_size != [0, 0]:
                self.size = tuple(self._base_size)
                # Re‑center the widget based on the stored base size.
                # The pos correction applied during stretching is undone
                # by resetting the size; the pos will be whatever it was
                # before the first stretch (we keep it as‑is).

        else:
            self._stretch_factor = [new_x, new_y]
            # Continue animating.
            Clock.schedule_once(lambda dt: self._animate_reset_stretch(), 0.016)

    def _update_glass_uniforms(self, *args):
        if not hasattr(self, "_glass_rect"):
            return

        # If the button/container is hidden, collapse the mesh size to 0,
        # so that the FBO and shader do not physically appear when clicked.
        if (
            self.opacity <= 0.001
            or getattr(self.parent, "opacity", 1.0) <= 0.001
        ):
            self._glass_rect.size = (0, 0)

            return

        # Apply stretch factor to size calculations.
        scaled_w = float(
            self.size[0] * self._scale_factor * self._stretch_factor[0]
        )
        scaled_h = float(
            self.size[1] * self._scale_factor * self._stretch_factor[1]
        )
        scaled_x = float(self.center_x - scaled_w / 2.0)
        scaled_y = float(self.center_y - scaled_h / 2.0)

        self._glass_rect.pos = (scaled_x, scaled_y)
        self._glass_rect.size = (scaled_w, scaled_h)

        r = self.border_radius
        # Apply stretch factor to border radius.
        radius_vec = [
            float(r[0]) * self._scale_factor * self._stretch_factor[0],
            float(r[1]) * self._scale_factor * self._stretch_factor[1],
            float(r[2]) * self._scale_factor * self._stretch_factor[0],
            float(r[3]) * self._scale_factor * self._stretch_factor[1],
        ]

        self._glass_rc["iResolution"] = [
            float(Window.width),
            float(Window.height),
        ]
        self._glass_rc["u_pos"] = [scaled_x, scaled_y]
        self._glass_rc["u_size"] = [scaled_w, scaled_h]
        self._glass_rc["u_radius"] = radius_vec
        g_col = [float(c) for c in self.glass_color]
        self._glass_rc["u_glass_color"] = g_col
        self._glass_rc["u_blur_amount"] = float(self.blur_amount)
        self._glass_rc["u_lens_power"] = float(self.lens_power)
        self._glass_rc["u_bevel_power"] = float(self.bevel_power)
        self._glass_rc["u_border_opacity"] = float(self.border_opacity)
        self._glass_rc["u_pressed"] = float(self._press_factor)
        self._glass_rc["u_touch_pos"] = [
            float(self._touch_pos[0]),
            float(self._touch_pos[1]),
        ]
        # Pass stretch factor to shader for non-uniform scaling effects.
        self._glass_rc["u_stretch_factor"] = [
            float(self._stretch_factor[0]),
            float(self._stretch_factor[1]),
        ]

        # Update the canvas transformation for stretch effect.
        self._update_stretch_transformation()
