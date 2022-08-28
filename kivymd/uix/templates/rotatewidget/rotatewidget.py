"""
Templates/RotateWidget
======================

.. deprecated:: 1.0.0

.. note:: `RotateWidget` class has been deprecated. Please use
    `RotateBahavior <https://kivymd.readthedocs.io/en/latest/behaviors/rotate/>`_
    class instead.
"""

__all__ = ("RotateWidget",)

from kivy import Logger

from kivymd.uix.behaviors import RotateBehavior


class RotateWidget(RotateBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~kivymd.uix.behaviors.rotate_behavior.RotateBehavior`
        class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `RotateWidget` class has been deprecated. "
            "Use the `RotateBehavior` class instead."
        )
