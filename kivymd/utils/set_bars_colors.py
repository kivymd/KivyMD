# The code is taken from AKivyMD project -
#     https://github.com/kivymd-extensions/akivymd
#
# Source code -
#     kivymd_extensions/akivymd/uix/statusbarcolor.py
#
# Author Sina Namadian -
#     https://github.com/quitegreensky

from typing import Union

from kivy.utils import get_hex_from_color, platform


def set_bars_colors(
    status_bar_color: Union[None, list],
    navigation_bar_color: Union[None, list],
    icons_color: str = "Light",
):
    """
    Sets the color of the status of the StatusBar and NavigationBar.

    .. versionadded:: 1.0.0
    """

    if platform == "android":
        from android.runnable import run_on_ui_thread
        from jnius import autoclass

        Color = autoclass("android.graphics.Color")
        WindowManager = autoclass("android.view.WindowManager$LayoutParams")
        activity = autoclass("org.kivy.android.PythonActivity").mActivity
        View = autoclass("android.view.View")

        def statusbar(*args):
            status_color = None
            navigation_color = None

            if status_bar_color:
                status_color = get_hex_from_color(status_bar_color)[:7]
            if navigation_bar_color:
                navigation_color = get_hex_from_color(navigation_bar_color)[:7]
            window = activity.getWindow()

            if icons_color == "Dark":
                window.getDecorView().setSystemUiVisibility(
                    View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                )
            elif icons_color == "Light":
                window.getDecorView().setSystemUiVisibility(0)

            window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
            window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)

            if status_color:
                window.setStatusBarColor(Color.parseColor(status_color))
            if navigation_color:
                window.setNavigationBarColor(Color.parseColor(navigation_color))

        return run_on_ui_thread(statusbar)()
