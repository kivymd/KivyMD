"""
PyInstaller hook for KivyMD
===========================

Adds fonts, images and KV files to package.

All modules from uix directory are added by Kivy hook.
"""

import os
from pathlib import Path

import kivymd

datas = [
    # Add `.ttf` files from the `kivymd/fonts` directory.
    (
        kivymd.fonts_path,
        str(Path("kivymd").joinpath(Path(kivymd.fonts_path).name)),
    ),
    # Add files from the `kivymd/images` directory.
    (
        kivymd.images_path,
        str(Path("kivymd").joinpath(Path(kivymd.images_path).name)),
    ),
]

# Add `.kv. files from the `kivymd/uix` directory.
for path_to_kv_file in Path(kivymd.uix_path).glob("**/*.kv"):
    datas.append(
        (
            str(Path(path_to_kv_file).parent.joinpath("*.kv")),
            str(
                Path("kivymd").joinpath(
                    "uix",
                    str(Path(path_to_kv_file).parent).split(
                        str(Path("kivymd").joinpath("uix")) + os.sep
                    )[1],
                )
            ),
        )
    )
