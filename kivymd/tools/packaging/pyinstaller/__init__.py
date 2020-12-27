"""
PyInstaller hooks
=================

Add ``hookspath=[kivymd.hooks_path]`` to your .spec file.

Example of .spec file
=====================

.. code-block:: python

    # -*- mode: python ; coding: utf-8 -*-

    import sys
    import os

    from kivy_deps import sdl2, glew

    from kivymd import hooks_path as kivymd_hooks_path

    path = os.path.abspath(".")

    a = Analysis(
        ["main.py"],
        pathex=[path],
        hookspath=[kivymd_hooks_path],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=None,
        noarchive=False,
    )
    pyz = PYZ(a.pure, a.zipped_data, cipher=None)

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        debug=False,
        strip=False,
        upx=True,
        name="app_name",
        console=True,
    )
"""

__all__ = ("hooks_path", "get_hook_dirs", "get_pyinstaller_tests")

import os
from pathlib import Path

import kivymd

hooks_path = str(Path(__file__).absolute().parent)
"""Path to hook directory to use with PyInstaller.
See :mod:`kivymd.tools.packaging.pyinstaller` for more information."""


def get_hook_dirs():
    return [hooks_path]


def get_pyinstaller_tests():
    return [os.path.join(kivymd.path, "tests", "pyinstaller")]


if __name__ == "__main__":
    print(hooks_path)
    print(get_hook_dirs())
    print(get_pyinstaller_tests())
