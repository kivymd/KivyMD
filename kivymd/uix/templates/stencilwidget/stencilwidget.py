"""
Templates/StencilWidget
=======================

.. deprecated:: 1.1.0

Base class for controlling the stencil instructions of the widget.

.. note:: `StencilWidget` class has been deprecated. Please use
    `StencilBehavior <https://kivymd.readthedocs.io/en/latest/behaviors/stencil/>`_
    class instead.
"""

__all__ = ("StencilWidget",)

from kivy import Logger

from kivymd.uix.behaviors import StencilBehavior


class StencilWidget(StencilBehavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~kivymd.uix.behaviors.scale_behavior.StencilBehavior`
        class instead.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "KivyMD: "
            "The `StencilWidget` class has been deprecated. "
            "Use the `StencilBehavior` class instead."
        )
