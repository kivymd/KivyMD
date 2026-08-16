"""
Behaviors
=========

Modules and classes implementing various behaviors for buttons etc.
"""

from .backgroundcolor_behavior import BackgroundColorBehavior

# flake8: NOQA
from .declarative_behavior import DeclarativeBehavior
from .elevation import CommonElevationBehavior
from .ios import IOSButtonBehavior, IOSGlassBehavior
from .magic_behavior import MagicBehavior
from .motion_behavior import (
    MotionDialogBehavior,
    MotionDropDownMenuBehavior,
    MotionShackBehavior,
)
from .ripple_behavior import (
    CircularRippleBehavior,
    M3CircularRippleBehavior,
    M3RectangularRippleBehavior,
    RectangularRippleBehavior,
)
from .rotate_behavior import RotateBehavior
from .scale_behavior import ScaleBehavior
from .stencil_behavior import StencilBehavior
from .touch_behavior import TouchBehavior

from .hover_behavior import HoverBehavior  # isort:skip
