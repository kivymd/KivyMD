"""
Themes/Font Definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""

from kivy.core.text import LabelBase

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

theme_font_styles = [
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Subtitle1",
    "Subtitle2",
    "Body1",
    "Body2",
    "Button",
    "Caption",
    "Overline",
    "Icon",
]
"""
.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-styles-2.png
"""
