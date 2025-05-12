"""
PyInstaller freezing test
=========================

PyInstaller must package KivyMD apps correctly.
"""

import subprocess

from PyInstaller import __main__ as pyi_main


def test_datas(tmp_path) -> None:
    """Test fonts and images."""

    app_name = "userapp"
    workpath = tmp_path / "build"
    distpath = tmp_path / "dist"
    app = tmp_path / (app_name + ".py")
    app.write_text(
        """
import os

from kivy.core.text import LabelBase

import kivymd

fonts = os.listdir(kivymd.fonts_path)
print(fonts)
assert "Roboto-Regular.ttf" in fonts
assert "materialdesignicons-webfont.ttf" in fonts
print(LabelBase._fonts.keys())
assert "Roboto" in LabelBase._fonts.keys()  # NOQA
assert "Icons" in LabelBase._fonts.keys()  # NOQA

images = os.listdir(kivymd.images_path)
print(images)
assert "logo" in images
assert "folder.png" in images
assert "transparent.png" in images
"""
    )
    pyi_main.run(
        [
            "--workpath",
            str(workpath),
            "--distpath",
            str(distpath),
            "--specpath",
            str(tmp_path),
            str(app),
        ]
    )
    subprocess.run([str(distpath / app_name / app_name)], check=True)


def test_widgets(tmp_path) -> None:
    """Test that all widgets are accesible."""

    app_name = "userapp"
    workpath = tmp_path / "build"
    distpath = tmp_path / "dist"
    app = tmp_path / (app_name + ".py")
    app.write_text(
        """
import os

import kivymd  # NOQA
__import__("kivymd.uix.label")
__import__("kivymd.uix.button")
__import__("kivymd.uix.list")
__import__("kivymd.uix.navigationdrawer")

print(os.listdir(os.path.dirname(kivymd.uix.__path__[0])))
"""
    )
    pyi_main.run(
        [
            "--workpath",
            str(workpath),
            "--distpath",
            str(distpath),
            "--specpath",
            str(tmp_path),
            str(app),
        ]
    )
    subprocess.run([str(distpath / app_name / app_name)], check=True)
