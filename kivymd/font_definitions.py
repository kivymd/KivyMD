"""
Themes/Font definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_

Example
=======

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.font_definitions import theme_font_styles
            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDRecycleView:
                    id: rv
                    key_viewclass: 'viewclass'
                    key_size: 'height'

                    RecycleBoxLayout:
                        padding: dp(10)
                        spacing: dp(10)
                        default_size: None, dp(48)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: "vertical"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)

                def on_start(self):
                    for style in theme_font_styles:
                        if style != "Icon":
                            for role in theme_font_styles[style]:
                                font_size = int(theme_font_styles[style][role]["font-size"])
                                self.root.ids.rv.data.append(
                                    {
                                        "viewclass": "MDLabel",
                                        "text": f"{style} {role} {font_size} sp",
                                        "adaptive_height": "True",
                                        "font_style": style,
                                        "role": role,
                                    }
                                )


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.material_resources import dp
            from kivymd.uix.recycleboxlayout import MDRecycleBoxLayout
            from kivymd.uix.recycleview import MDRecycleView
            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp
            from kivymd.font_definitions import theme_font_styles


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.screen = (
                        MDScreen(
                            MDRecycleView(
                                MDRecycleBoxLayout(
                                    padding=(dp(10), dp(10), 0, dp(10)),
                                    default_size=(None, dp(48)),
                                    default_size_hint=(1, None),
                                    size_hint_y=None,
                                    adaptive_height=True,
                                    orientation='vertical',
                                ),
                                id="rv",
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )
                    rv = self.screen.get_ids().rv
                    rv.key_viewclass = 'viewclass'
                    rv.key_size = 'height'
                    return self.screen

                def on_start(self):
                    for style in theme_font_styles:
                        if style != "Icon":
                            for role in theme_font_styles[style]:
                                font_size = int(theme_font_styles[style][role]["font-size"])
                                self.screen.get_ids().rv.data.append(
                                    {
                                        "viewclass": "MDLabel",
                                        "text": f"{style} {role} {font_size} sp",
                                        "adaptive_height": "True",
                                        "font_style": style,
                                        "role": role,
                                    }
                                )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-font-style-preview.png
    :align: center
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
