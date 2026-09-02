"""
Behaviors/Tilt
==============

.. versionadded:: 2.0.1

.. rubric:: The TiltBehavior class adds an interactive 3D perspective tilt
    effect, content parallax shift, and a dynamic gradient glare to Kivy and
    KivyMD widgets based on cursor movement or touch interaction.

Features
--------

- 3D Perspective Tilt: Smoothly rotates the widget along the X and Y axes
  depending on the cursor's relative position from the center.
- Dynamic Glare Effect: Generates a real-time lighting glare that tracks mouse
  movement across the widget surface with adjustable radius and opacity.
- Parallax Shift: Shifts inner textures or content slightly to create a
  multi-layered depth illusion.
- Smooth Animation: Utilizes linear interpolation (LERP) inside a 60 FPS clock
  cycle to ensure fluid, lag-free transitions.

Base example
------------

.. tabs::

    .. tab:: Imperative Python style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.widget import Widget
            from kivy.graphics import Color, Rectangle

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import TiltBehavior


            class TiltCard(TiltBehavior, Widget):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)

                    with self.canvas:
                        Color(1, 0, 0, 1)
                        self.rect = Rectangle(
                            size=self.card_size,
                            pos=(-self.card_size[0] / 2, -self.card_size[1] / 2),
                        )

                    self.bind(card_size=self._update_rect)

                def _update_rect(self, instance, value):
                    self.rect.size = value
                    self.rect.pos = (-value[0] / 2, -value[1] / 2)


            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                TiltCard:
                    size_hint: None, None
                    size: dp(200), dp(350)
                    card_size: self.size
                    pos_hint: {"center_x": .5, "center_y": .5}
                    corner_radius: dp(24)
            '''


            class TiltExample(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            TiltExample().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.uix.widget import Widget
            from kivy.graphics import Color, Rectangle

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import TiltBehavior
            from kivymd.uix.screen import MDScreen


            class TiltCard(TiltBehavior, Widget):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)

                    with self.canvas:
                        Color(1, 0, 0, 1)
                        self.rect = Rectangle(
                            size=self.card_size,
                            pos=(-self.card_size[0] / 2, -self.card_size[1] / 2),
                        )

                    self.bind(card_size=self._update_rect)

                def _update_rect(self, instance, value):
                    self.rect.size = value
                    self.rect.pos = (-value[0] / 2, -value[1] / 2)


            class TiltExample(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            TiltCard(
                                size_hint=(None, None),
                                size=(dp(200), dp(350)),
                                card_size=(dp(200), dp(350)),
                                pos_hint={"center_x": .5, "center_y": .5},
                                corner_radius=dp(24),
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            TiltExample().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-base-example.gif
    :align: center

.. note:: See also `kivymd.uix.tilt.TiltCard`
"""

import math
import os

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import RenderContext
from kivy.graphics.transformation import Matrix
from kivy.metrics import dp
from kivy.properties import ColorProperty, ListProperty, NumericProperty

__all__ = ("TiltBehavior",)

from kivymd import glsl_path

TILT_VS_SHADER = os.path.join(glsl_path, "tilt", "tilt_vs.glsl")
TILT_FS_SHADER = os.path.join(glsl_path, "tilt", "tilt_fs.glsl")


class TiltBehavior:
    """
    A behavior class that adds an interactive 3D tilt effect, parallax, and
    glare to a Kivy/KivyMD widget based on mouse/touch movement.

    This class should be inherited alongside a Kivy/KivyMD `Widget` or its
    subclasses. It uses a custom `RenderContext` with custom GLSL shaders to
    perform 3D transformations directly on the GPU.
    """

    card_size = ListProperty([dp(100), dp(100)])
    """
    Dimensions of the 3D card/widget plane.

    :attr:`card_size` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[dp(100), dp(100)]`.
    """

    fov = NumericProperty(45.0)
    """
    Field of View (FOV) for the 3D perspective camera.

    :attr:`fov` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `45.0`.
    """

    max_tilt_angle = NumericProperty(2.0)
    """
    Maximum tilt angle in degrees when hovering over the edges.

    .. code-block:: python

        TiltCard(
            max_tilt_angle=20,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-max-tilt-angle-20.gif
        :align: center

    .. code-block:: python

        TiltCard(
            max_tilt_angle=2,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-max-tilt-angle-2.gif
        :align: center

    :attr:`max_tilt_angle` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.0`.
    """

    smoothness = NumericProperty(0.06)
    """
    Interpolation factor for smooth animations (lower is slower/smoother).

    :attr:`smoothness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.06`.
    """

    parallax_strength = NumericProperty(0.05)
    """
    Multiplier for the texture/content parallax shift.

    :attr:`parallax_strength` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.05`.
    """

    text_z_offset = NumericProperty(25.0)
    """
    Z-axis offset for child widgets (e.g., text) to make them pop out.

    .. code-block:: python

        TiltCard(
            text_z_offset=25,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-text-z-offset-25.png
        :align: center

    .. code-block:: python

        TiltCard(
            text_z_offset=0,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-text-z-offset-0.png
        :align: center

    :attr:`text_z_offset` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `25.0`.
    """

    corner_radius = NumericProperty(0)
    """
    Border radius to clip the shader rendering.

    :attr:`corner_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    glare_radius = NumericProperty(0.6)
    """
    Size of the gradient glare effect.

    .. code-block:: python

        TiltCard(
            glare_radius=1,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-glare-radiuse-1.gif
        :align: center

    .. code-block:: python

        TiltCard(
            glare_radius=0.6,
        )

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tilt-behavior-glare-radiuse-06.gif
        :align: center

    :attr:`glare_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.6`.
    """

    glare_max_opacity = NumericProperty(0.35)
    """
    Opacity of the gradient glare effect.

    :attr:`glare_max_opacity` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.35`.
    """

    glare_color = ColorProperty([1.0, 1.0, 1.0, 1.0])
    """
    Color of the glare effect.

    :attr:`glare_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[1.0, 1.0, 1.0, 1.0]`.
    """

    flip_angle = NumericProperty(0.0)
    """
    Initial or programmatic rotation around the Y-axis (for card flips).

    :attr:`flip_angle` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    def __init__(self, **kwargs):
        self.canvas = RenderContext(use_parent_projection=False)

        with open(TILT_VS_SHADER, "r", encoding="utf-8") as shader_file:
            self.canvas.shader.vs = "$HEADER$\n" + shader_file.read()

        with open(TILT_FS_SHADER, "r", encoding="utf-8") as shader_file:
            self.canvas.shader.fs = "$HEADER$\n" + shader_file.read()

        # Target and current variables for smooth interpolation.
        self._target_rot_x = 0.0
        self._target_rot_y = 0.0
        self._current_rot_x = 0.0
        self._current_rot_y = 0.0

        self._target_glare_pos = [0.5, 0.5]
        self._current_glare_pos = [0.5, 0.5]
        self._target_glare_opacity = 0.0
        self._current_glare_opacity = 0.0

        self._target_parallax = [0.0, 0.0]
        self._current_parallax = [0.0, 0.0]

        self._z_depth = 0.0

        super().__init__(**kwargs)

        self.bind(
            pos=self.update_matrices,
            size=self.update_matrices,
            card_size=self.update_matrices,
            corner_radius=self.update_matrices,
        )

        self._update_z_depth()
        Window.bind(mouse_pos=self.on_mouse_move)

        self.update_matrices()
        Clock.schedule_interval(self.update_transform, 1 / 60.0)

    def update_matrices(self, *args):
        """
        Updates the 3D projection matrix. This is called whenever the
        window is resized or the widget changes its dimensions/position.
        """

        self._update_z_depth()
        asp = float(Window.width) / float(Window.height)
        proj = Matrix()
        proj.perspective(self.fov, asp, 1.0, 5000.0)
        self.canvas["projection_mat"] = proj

    def on_mouse_move(self, window, pos):
        """
        Tracks the mouse position and calculates target rotation,
        glare position, and parallax offset if the mouse is over the widget.
        """

        card_w, card_h = self.card_size

        # Use standard Kivy widget center coordinates for positioning
        # calculations.
        center_x = self.center_x
        center_y = self.center_y

        x, y = pos
        rel_x = x - center_x
        rel_y = y - center_y

        half_w = card_w / 2.0
        half_h = card_h / 2.0

        # Check if the mouse cursor is inside the boundaries of the card.
        if (-half_w <= rel_x <= half_w) and (-half_h <= rel_y <= half_h):
            dx = rel_x / half_w
            dy = rel_y / half_h

            # Calculate target rotations (inverted on X-axis for natural feel).
            self._target_rot_x = -dy * self.max_tilt_angle
            self._target_rot_y = dx * self.max_tilt_angle

            # Calculate target parallax offset
            self._target_parallax = [
                -dx * self.parallax_strength,
                dy * self.parallax_strength,
            ]

            # Calculate UV coordinates for the glare effect (0.0 to 1.0).
            u = (rel_x + half_w) / card_w
            v = 1.0 - ((rel_y + half_h) / card_h)

            self._target_glare_pos = [u, v]
            self._target_glare_opacity = 1.0
        else:
            # Reset variables when the mouse leaves the widget area.
            self._target_rot_x = 0.0
            self._target_rot_y = 0.0
            self._target_glare_opacity = 0.0
            self._target_parallax = [0.0, 0.0]

    def update_transform(self, dt):
        """
        Called every frame. Smoothly interpolates the current values towards
        the target values and passes them as uniforms to the shaders.
        """

        s = self.smoothness

        # Smooth interpolation for rotations.
        self._current_rot_x += (self._target_rot_x - self._current_rot_x) * s
        self._current_rot_y += (self._target_rot_y - self._current_rot_y) * s

        # Smooth interpolation for glare.
        self._current_glare_pos[0] += (
            self._target_glare_pos[0] - self._current_glare_pos[0]
        ) * s
        self._current_glare_pos[1] += (
            self._target_glare_pos[1] - self._current_glare_pos[1]
        ) * s
        self._current_glare_opacity += (
            self._target_glare_opacity - self._current_glare_opacity
        ) * s

        # Smooth interpolation for parallax.
        self._current_parallax[0] += (
            self._target_parallax[0] - self._current_parallax[0]
        ) * s
        self._current_parallax[1] += (
            self._target_parallax[1] - self._current_parallax[1]
        ) * s

        # Pass updated variables to the fragment shader.
        self.canvas["u_mouse"] = self._current_glare_pos
        self.canvas["u_glare_opacity"] = self._current_glare_opacity
        self.canvas["u_glare_radius"] = float(self.glare_radius)
        self.canvas["u_max_opacity"] = float(self.glare_max_opacity)
        self.canvas["u_glare_color"] = self.glare_color[:3]
        self.canvas["u_parallax_offset"] = self._current_parallax
        self.canvas["u_card_size"] = (
            float(self.card_size[0]),
            float(self.card_size[1]),
        )
        self.canvas["u_corner_radius"] = float(self.corner_radius)

        # Calculate translation offsets from the center of the window to the
        # widget's center.
        tx = self.center_x - (Window.width / 2.0)
        ty = self.center_y - (Window.height / 2.0)

        # Build the modelview matrix applying translation and rotations.
        modelview = Matrix()

        # Apply standard Kivy positioning via translation.
        modelview = modelview.translate(tx, ty, self._z_depth)

        # Apply rotations (Flip, X-axis tilt, Y-axis tilt).
        modelview = modelview.rotate(self.flip_angle, 0, 1, 0)
        modelview = modelview.rotate(self._current_rot_x, 1, 0, 0)
        modelview = modelview.rotate(self._current_rot_y, 0, 1, 0)

        # Pass the matrix to the vertex shader.
        self.canvas["modelview_mat"] = modelview

    def _update_z_depth(self):
        """
        Calculates the Z-axis camera depth required to fit the widget
        correctly onto the screen based on the Field of View (FOV).
        """

        fov_rad = math.radians(self.fov)
        self._z_depth = -(Window.height / (2.0 * math.tan(fov_rad / 2.0)))
