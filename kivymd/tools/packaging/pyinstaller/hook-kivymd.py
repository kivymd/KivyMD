"""
PyInstaller hook for KivyMD
===========================

Adds fonts and images to package.

All modules from uix directory are added by Kivy hook.
"""

from pathlib import Path

import kivymd

datas = [
    (
        kivymd.fonts_path,
        str(Path("kivymd").joinpath(Path(kivymd.fonts_path).name)),
    ),
    (
        kivymd.images_path,
        str(Path("kivymd").joinpath(Path(kivymd.images_path).name)),
    ),
]
