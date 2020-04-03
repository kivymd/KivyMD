"""
Behaviors
=========

Modules and classes implementing various behaviors for buttons etc.
"""

from .ripplebehavior import CircularRippleBehavior, RectangularRippleBehavior
from .hover_behavior import HoverBehavior
from .focus_behavior import FocusBehavior
from .elevation import (
    CommonElevationBehavior,
    RectangularElevationBehavior,
    CircularElevationBehavior,
    RectangularElevationBehavior,
)
from .backgroundcolorbehavior import (
    BackgroundColorBehavior,
    SpecificBackgroundColorBehavior,
)
from .magic_behavior import MagicBehavior
from .touch_behavior import TouchBehavior
