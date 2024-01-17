"""
Themes/Font definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""

from kivy.core.text import LabelBase
from kivy.metrics import sp

from kivymd import fonts_path

fonts = [
    {
        "name": "Roboto",
        "fn_regular": fonts_path + "Roboto-Regular.ttf",
        "fn_bold": fonts_path + "Roboto-Bold.ttf",
        "fn_italic": fonts_path + "Roboto-Italic.ttf",
        "fn_bolditalic": fonts_path + "Roboto-BoldItalic.ttf",
    },
    {
        "name": "RobotoThin",
        "fn_regular": fonts_path + "Roboto-Thin.ttf",
        "fn_italic": fonts_path + "Roboto-ThinItalic.ttf",
    },
    {
        "name": "RobotoLight",
        "fn_regular": fonts_path + "Roboto-Light.ttf",
        "fn_italic": fonts_path + "Roboto-LightItalic.ttf",
    },
    {
        "name": "RobotoMedium",
        "fn_regular": fonts_path + "Roboto-Medium.ttf",
        "fn_italic": fonts_path + "Roboto-MediumItalic.ttf",
    },
    {
        "name": "RobotoBlack",
        "fn_regular": fonts_path + "Roboto-Black.ttf",
        "fn_italic": fonts_path + "Roboto-BlackItalic.ttf",
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

# TODO: Add `weight` properties.
theme_font_styles = {
    "Icon": {
        "large": {
            "line-height": 1,
            "font-name": "Icons",
            "font-size": sp(24),
        },
    },
    "Display": {
        "large": {
            "line-height": 1.64,
            "font-name": "Roboto",
            "font-size": sp(57),
        },
        "medium": {
            "line-height": 1.52,
            "font-name": "Roboto",
            "font-size": sp(45),
        },
        "small": {
            "line-height": 1.44,
            "font-name": "Roboto",
            "font-size": sp(36),
        },
    },
    "Headline": {
        "large": {
            "line-height": 1.40,
            "font-name": "Roboto",
            "font-size": sp(32),
        },
        "medium": {
            "line-height": 1.36,
            "font-name": "Roboto",
            "font-size": sp(28),
        },
        "small": {
            "line-height": 1.32,
            "font-name": "Roboto",
            "font-size": sp(24),
        },
    },
    "Title": {
        "large": {
            "line-height": 1.28,
            "font-name": "Roboto",
            "font-size": sp(22),
        },
        "medium": {
            "line-height": 1.24,
            "font-name": "Roboto",
            "font-size": sp(16),
        },
        "small": {
            "line-height": 1.20,
            "font-name": "Roboto",
            "font-size": sp(14),
        },
    },
    "Body": {
        "large": {
            "line-height": 1.24,
            "font-name": "Roboto",
            "font-size": sp(16),
        },
        "medium": {
            "line-height": 1.20,
            "font-name": "Roboto",
            "font-size": sp(14),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "Roboto",
            "font-size": sp(12),
        },
    },
    "Label": {
        "large": {
            "line-height": 1.20,
            "font-name": "Roboto",
            "font-size": sp(14),
        },
        "medium": {
            "line-height": 1.16,
            "font-name": "Roboto",
            "font-size": sp(12),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "Roboto",
            "font-size": sp(11),
        },
    },
}
"""
.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-font-style-preview.png
    :align: center
"""
