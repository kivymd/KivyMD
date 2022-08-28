"""
Templates/ScaleWidget
=====================

.. deprecated:: 1.1.0

Base class for controlling the scale of the widget.

.. note:: `ScaleWidget` class has been deprecated. Please use
    `ScaleBehavior <https://kivymd.readthedocs.io/en/latest/behaviors/scale/>`_
    class instead.
"""

__all__ = ("ScaleWidget",)

from kivy import Logger

from kivymd.uix.behaviors import ScaleBehavior


class ScaleWidget(ScaleBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior`
        class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `ScaleWidget` class has been deprecated. "
            "Use the `ScaleBehavior` class instead."
        )
