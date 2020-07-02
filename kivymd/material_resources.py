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

TOUCH_TARGET_HEIGHT = dp(48)
