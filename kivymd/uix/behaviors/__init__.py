"""
Behaviors
=========

Modules and classes implementing various behaviors for buttons etc.
"""

from .backgroundcolor_behavior import (
    BackgroundColorBehavior,
    SpecificBackgroundColorBehavior,
)

# flake8: NOQA
from .declarative_bahavior import DeclarativeBehavior
from .elevation import (
    CircularElevationBehavior,
    CommonElevationBehavior,
    FakeCircularElevationBehavior,
    FakeRectangularElevationBehavior,
    ObservableShadow,
    RectangularElevationBehavior,
    RoundedRectangularElevationBehavior,
)
from .magic_behavior import MagicBehavior
from .ripple_behavior import CircularRippleBehavior, RectangularRippleBehavior
from .touch_behavior import TouchBehavior

from .hover_behavior import HoverBehavior  # isort:skip
