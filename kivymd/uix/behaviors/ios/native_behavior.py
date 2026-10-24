"""
Components/iOS Native
=====================

.. versionadded:: 2.0.1

.. rubric:: Behavior that provides a bridge for native iOS APIs using pyobjus,
    supporting haptic feedback and other platform-specific capabilities
    for KivyMD components.

Example
-------

.. code-block:: python

    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import IOSNativeBehavior
    from kivymd.uix.button import IOSButtonText, IOSButton
    from kivymd.uix.fitimage import FitImage
    from kivymd.uix.screen import MDScreen


    class VibrateIOSButton(IOSButton, IOSNativeBehavior):
        def on_press(self):
            super().on_press()
            self.trigger_haptic_feedback()


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            bg_image = FitImage(source="https://picsum.photos/800/600?random=2")

            return MDScreen(
                bg_image,
                VibrateIOSButton(
                    IOSButtonText(
                        text="Tap for Haptic",
                    ),
                    target_background=bg_image,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    border_radius=[dp(22)] * 4,
                    adaptive_width=True,
                ),
            )


    if __name__ == "__main__":
        Example().run()
"""

__all__ = (
    "IOSNativeBehavior",
)

from kivy.utils import platform


class IOSNativeBehavior:
    """
    Behavior that provides a bridge for native iOS APIs using pyobjus,
    supporting haptic feedback and other platform-specific capabilities
    for KivyMD components.
    """

    def __init__(self, **kwargs):
        self._haptic_generator = None
        self._last_vibrated_step = 0

        if platform == "ios":
            try:
                from pyobjus import autoclass

                UISelectionFeedbackGenerator = autoclass(
                    "UISelectionFeedbackGenerator"
                )
                self._haptic_generator = (
                    UISelectionFeedbackGenerator.alloc().init()
                )
                self._haptic_generator.prepare()
            except Exception:
                pass

        super().__init__(**kwargs)

    def trigger_haptic_feedback(self) -> None:
        """Triggers the native iOS selection haptic feedback."""

        if platform == "ios" and self._haptic_generator:
            try:
                self._haptic_generator.prepare()
                self._haptic_generator.selectionChanged()
            except Exception:
                pass

    def check_and_trigger_haptic(self, value: float) -> None:
        """
        Calculates discrete steps using widget's min/step attributes
        and triggers haptic feedback if the step has changed.
        """

        step_val = getattr(self, "step", 1)
        min_val = getattr(self, "min", 0)

        current_step = round((value - min_val) / step_val) if step_val else 0

        if self._last_vibrated_step != current_step:
            self._last_vibrated_step = current_step
            self.trigger_haptic_feedback()
