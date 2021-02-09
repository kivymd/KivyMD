"""
Behaviors
=========

Modules and classes implementing various behaviors for buttons etc.
"""

# flake8: NOQA
from .hover_behavior import HoverBehavior  # isort:skip
from .backgroundcolor_behavior import (
    BackgroundColorBehavior,
    SpecificBackgroundColorBehavior,
)
from .elevation import (
    CircularElevationBehavior,
    CommonElevationBehavior,
    FakeCircularElevationBehavior,
    FakeRectangularElevationBehavior,
    ObservableShadow,
    RectangularElevationBehavior,
    RoundedRectangularElevationBehavior,
)
from .focus_behavior import FocusBehavior
from .magic_behavior import MagicBehavior
from .ripple_behavior import CircularRippleBehavior, RectangularRippleBehavior
from .touch_behavior import TouchBehavior
