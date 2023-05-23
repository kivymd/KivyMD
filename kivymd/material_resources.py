"""
Material Resources
==================
"""

import os

from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform

if "KIVY_DOC_INCLUDE" in os.environ:
    dp = lambda x: x  # NOQA: F811

# Feel free to override this const if you're designing for a device such as
# a GNU/Linux tablet.
DEVICE_IOS = platform == "ios" or platform == "macosx"
if platform != "android" and platform != "ios":
    DEVICE_TYPE = "desktop"
elif Window.width >= dp(600) and Window.height >= dp(600):
    DEVICE_TYPE = "tablet"
else:
    DEVICE_TYPE = "mobile"

if DEVICE_TYPE == "mobile":
    MAX_NAV_DRAWER_WIDTH = dp(300)
    HORIZ_MARGINS = dp(16)
    STANDARD_INCREMENT = dp(56)
    PORTRAIT_TOOLBAR_HEIGHT = STANDARD_INCREMENT
    LANDSCAPE_TOOLBAR_HEIGHT = STANDARD_INCREMENT - dp(8)
else:
    MAX_NAV_DRAWER_WIDTH = dp(400)
    HORIZ_MARGINS = dp(24)
    STANDARD_INCREMENT = dp(64)
    PORTRAIT_TOOLBAR_HEIGHT = STANDARD_INCREMENT
    LANDSCAPE_TOOLBAR_HEIGHT = STANDARD_INCREMENT

# Elevation.
SEGMENT_CONTROL_SEGMENT_SWITCH_ELEVATION = 1
FILE_MANAGER_TOP_APP_BAR_ELEVATION = 1
FLOATING_ACTION_BUTTON_M2_ELEVATION = 1
FLOATING_ACTION_BUTTON_M3_ELEVATION = 0.5
CARD_STYLE_ELEVATED_M3_ELEVATION = 0.5
CARD_STYLE_OUTLINED_FILLED_M3_ELEVATION = 0
DATA_TABLE_ELEVATION = 4
DROP_DOWN_MENU_ELEVATION = 2
TOP_APP_BAR_ELEVATION = 2
SNACK_BAR_ELEVATION = 2

# Shadow softness.
RAISED_BUTTON_SOFTNESS = 4
FLOATING_ACTION_BUTTON_M3_SOFTNESS = 0
DATA_TABLE_SOFTNESS = 12
DROP_DOWN_MENU_SOFTNESS = 6

# Shadow offset.
RAISED_BUTTON_OFFSET = (0, -2)
FLOATING_ACTION_BUTTON_M2_OFFSET = (0, -1)
FLOATING_ACTION_BUTTON_M3_OFFSET = (0, -2)
DATA_TABLE_OFFSET = (0, -2)
DROP_DOWN_MENU_OFFSET = (0, -2)
SNACK_BAR_OFFSET = (0, -2)

TOUCH_TARGET_HEIGHT = dp(48)
