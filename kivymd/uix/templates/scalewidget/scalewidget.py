"""
Templates/ScaleWidget
=====================

.. deprecated:: 1.1.0

Base class for controlling the scale of the widget.

.. note:: `ScaleWidget` class has been deprecated. Please use
    `ScaleBahavior <https://kivymd.readthedocs.io/en/latest/behaviors/scale/>`_
    class instead.
"""

__all__ = ("ScaleWidget",)

from kivymd.uix.behaviors.scale_behavior import ScaleBahavior


class ScaleWidget(ScaleBahavior):
    """
    .. deprecated:: 1.1.0
        Use :class:`~kivymd.uix.behaviors.scale_bahavior.ScaleBahavior`
        class instead.
    """
