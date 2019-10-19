"""
Grid
====

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Image lists <https://material.io/design/components/image-lists.htheme_clsl>`_

Example
-------

import os

from kivy.app import App
from kivy.lang import Builder

from kivymd.theming import ThemeManager
from kivymd.utils.cropimage import crop_image

kv = '''
<MySmartTileWithLabel@SmartTileWithLabel>
    mipmap: True
    font_style: 'Subtitle1'


BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: app.title
        elevation: 10
        left_action_items: [['menu', lambda x: x]]
        md_bg_color: app.theme_cls.primary_color

    ScreenManager:
        id: manager

        Screen:
            name: 'one'

            MDFlatButton:
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: manager.current = 'two'
                text: 'Open Grid'

        Screen:
            name: 'two'
            on_enter:
                app.crop_image_for_tile(tile_1, tile_1.size,\
                'demos/kitchen_sink/assets/beautiful-931152_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_2, tile_2.size,\
                'demos/kitchen_sink/assets/african-lion-951778_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_3, tile_3.size,\
                'demos/kitchen_sink/assets/guitar-1139397_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_4, tile_4.size,\
                'demos/kitchen_sink/assets/robin-944887_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_5, tile_5.size,\
                'demos/kitchen_sink/assets/kitten-1049129_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_6, tile_6.size,\
                'demos/kitchen_sink/assets/light-bulb-1042480_1280_tile_crop.jpg')
                app.crop_image_for_tile(tile_7, tile_7.size,\
                'demos/kitchen_sink/assets/tangerines-1111529_1280_tile_crop.jpg')

            ScrollView:
                do_scroll_x: False

                GridLayout:
                    cols: 2
                    row_default_height:
                        (self.width - self.cols*self.spacing[0])/self.cols
                    row_force_default: True
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(4), dp(4)
                    spacing: dp(4)

                    SmartTileWithStar:
                        id: tile_2
                        mipmap: True
                        stars: 3
                    SmartTileWithStar:
                        id: tile_3
                        mipmap: True
                        stars: 3
                    SmartTileWithLabel:
                        id: tile_1
                        text:
                            "Beautiful\\n[size=12]beautiful-931152_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_4
                        text:
                            "Robin\\n[size=12]robin-944887_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_5
                        text:
                            "Kitten\\n[size=12]kitten-1049129_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_6
                        text:
                            "Light-Bulb\\n[size=12]light-bulb-1042480_1280.jpg[/size]"
                    SmartTileWithLabel:
                        id: tile_7
                        text:
                            "Tangerines\\n[size=12]tangerines-1111529_1280.jpg[/size]"
'''


class MyApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    title = 'Example Smart Tile'
    md_app_bar = None

    def build(self):
        root = Builder.load_string(kv)
        return root

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image


MyApp().run()
"""

from kivy.lang import Builder
from kivy.properties import (
    StringProperty,
    BooleanProperty,
    ObjectProperty,
    NumericProperty,
    ListProperty,
    OptionProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<SmartTile>
    _img_widget: img
    _img_overlay: img_overlay
    _box_overlay: box

    AsyncImage:
        id: img
        allow_stretch: root.allow_stretch
        anim_delay: root.anim_delay
        anim_loop: root.anim_loop
        color: root.img_color
        keep_ratio: root.keep_ratio
        mipmap: root.mipmap
        source: root.source
        size_hint_y: 1 if root.overlap else None
        x: root.x
        y: root.y if root.overlap or root.box_position == 'header' else box.top

    BoxLayout:
        id: img_overlay
        size_hint: img.size_hint
        size: img.size
        pos: img.pos

    BoxLayout:
        canvas:
            Color:
                rgba: root.box_color
            Rectangle:
                pos: self.pos
                size: self.size
        id: box
        size_hint_y: None
        height: dp(68) if root.lines == 2 else dp(48)
        x: root.x
        y: root.y if root.box_position == 'footer'\
            else root.y + root.height - self.height


<SmartTileWithLabel>
    _img_widget: img
    _img_overlay: img_overlay
    _box_overlay: box
    _box_label: boxlabel

    AsyncImage:
        id: img
        allow_stretch: root.allow_stretch
        anim_delay: root.anim_delay
        anim_loop: root.anim_loop
        color: root.img_color
        keep_ratio: root.keep_ratio
        mipmap: root.mipmap
        source: root.source
        size_hint_y: 1 if root.overlap else None
        x: root.x
        y: root.y if root.overlap or root.box_position == 'header' else box.top

    BoxLayout:
        id: img_overlay
        size_hint: img.size_hint
        size: img.size
        pos: img.pos

    BoxLayout:
        canvas:
            Color:
                rgba: root.box_color
            Rectangle:
                pos: self.pos
                size: self.size

        id: box
        size_hint_y: None
        padding: dp(5), 0, 0, 0
        height: self.minimum_height #dp(68) if root.lines == 2 else dp(48)
        x: root.x
        y: root.y if root.box_position == 'footer'\
            else root.y + root.height - self.height

        MDLabel:
            id: boxlabel
            font_style: root.font_style
            #halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            color: root.tile_text_color
            markup: True
"""
)


class Tile(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, BoxLayout
):
    """A simple tile. It does nothing special, just inherits the right
    behaviors to work as a building block.
    """

    pass


class SmartTile(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, FloatLayout
):
    """A tile for more complex needs.

    Includes an image, a container to place overlays and a box that can act
    as a header or a footer, as described in the Material Design specs.
    """

    box_color = ListProperty([0, 0, 0, 0.5])
    """Sets the color and opacity for the information box."""

    box_position = OptionProperty("footer", options=["footer", "header"])
    """Determines wether the information box acts as a header or footer to the
    image.
    """

    lines = OptionProperty(1, options=[1, 2])
    """Number of lines in the header/footer.

    As per Material Design specs, only 1 and 2 are valid values.
    """

    overlap = BooleanProperty(True)
    """Determines if the header/footer overlaps on top of the image or not"""

    # Img properties
    allow_stretch = BooleanProperty(True)
    anim_delay = NumericProperty(0.25)
    anim_loop = NumericProperty(0)
    img_color = ListProperty([1, 1, 1, 1])
    keep_ratio = BooleanProperty(False)
    mipmap = BooleanProperty(False)
    source = StringProperty()

    _img_widget = ObjectProperty()
    _img_overlay = ObjectProperty()
    _box_overlay = ObjectProperty()
    _box_label = ObjectProperty()

    def reload(self):
        self._img_widget.reload()

    def add_widget(self, widget, index=0, canvas=None):
        if issubclass(widget.__class__, IOverlay):
            self._img_overlay.add_widget(widget, index, canvas)
        elif issubclass(widget.__class__, IBoxOverlay):
            self._box_overlay.add_widget(widget, index, canvas)
        else:
            super().add_widget(widget, index, canvas)


class SmartTileWithLabel(SmartTile):
    _box_label = ObjectProperty()

    # MDLabel properties
    font_style = StringProperty("Caption")
    theme_text_color = StringProperty("Custom")
    tile_text_color = ListProperty([1, 1, 1, 1])
    text = StringProperty("")
    """Determines the text for the box footer/header"""


class Star(MDIconButton):
    def on_touch_down(self, touch):
        return True


class SmartTileWithStar(SmartTileWithLabel):
    stars = NumericProperty(1)

    def on_stars(self, *args):
        for star in range(self.stars):
            self.ids.box.add_widget(
                Star(
                    icon="star-outline",
                    theme_text_color="Custom",
                    text_color=[1, 1, 1, 1],
                )
            )


class IBoxOverlay:
    """An interface to specify widgets that belong to to the image overlay
    in the :class:`SmartTile` widget when added as a child.
    """

    pass


class IOverlay:
    """An interface to specify widgets that belong to to the image overlay
    in the :class:`SmartTile` widget when added as a child.
    """

    pass
