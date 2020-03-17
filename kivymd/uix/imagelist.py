"""
Components/Image List
=====================

.. seealso::

    `Material Design spec, Image lists <https://material.io/components/image-lists>`_

.. rubric:: Image lists display a collection of images in an organized grid.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/image-list.png
    :align: center

`KivyMD` provides the following tile classes for use:

- SmartTileWithStar_
- SmartTileWithLabel_

.. SmartTileWithStar:
SmartTileWithStar
-----------------

.. code-block::

    from kivymd.app import MDApp
    from kivy.lang import Builder

    KV = '''
    ScrollView:

        MDGridLayout:
            cols: 3
            row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
            row_force_default: True
            adaptive_height: True
            padding: dp(4), dp(4)
            spacing: dp(4)

            SmartTileWithStar:
                stars: 5
                source: "cat-1.jpg"

            SmartTileWithStar:
                stars: 5
                source: "cat-2.jpg"

            SmartTileWithStar:
                stars: 5
                source: "cat-.jpg"
    '''


    class MyApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MyApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/SmartTileWithStar.gif
    :align: center

.. SmartTileWithLabel:
SmartTileWithLabel
------------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivy.lang import Builder

    KV = '''
    ScrollView:

        MDGridLayout:
            cols: 3
            row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
            row_force_default: True
            adaptive_height: True
            padding: dp(4), dp(4)
            spacing: dp(4)

            SmartTileWithLabel:
                source: "cat-1.jpg"
                text: "[size=26]Cat 1[/size]\\n[size=14]cat-1.jpg[/size]"

            SmartTileWithLabel:
                source: "cat-2.jpg"
                text: "[size=26]Cat 2[/size]\\n[size=14]cat-2.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color

            SmartTileWithLabel:
                source: "cat-3.jpg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size]\\n[size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
    '''


    class MyApp(MDApp):
        def build(self):
            root = Builder.load_string(KV)
            return root


    MyApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/SmartTileWithLabel.png
    :align: center
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
        y: root.y if root.box_position == 'footer' else root.y + root.height - self.height


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
        padding: "5dp", 0, 0, 0
        height: self.minimum_height
        x: root.x
        y: root.y if root.box_position == 'footer' else root.y + root.height - self.height

        MDLabel:
            id: boxlabel
            font_style: root.font_style
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
    """
    A simple tile. It does nothing special, just inherits the right
    behaviors to work as a building block.
    """

    pass


class SmartTile(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, FloatLayout
):
    """
    A tile for more complex needs.

    Includes an image, a container to place overlays and a box that can act
    as a header or a footer, as described in the Material Design specs.
    """

    box_color = ListProperty([0, 0, 0, 0.5])
    """
    Sets the color and opacity for the information box.

    :attr:`box_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    box_position = OptionProperty("footer", options=["footer", "header"])
    """
    Determines wether the information box acts as a header or footer to the
    image. Available are options: `'footer'`, `'header'`.

    :attr:`box_position` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'footer'`.
    """

    lines = OptionProperty(1, options=[1, 2])
    """
    Number of lines in the `header/footer`. As per `Material Design specs`,
    only 1 and 2 are valid values. Available are options: ``1``, ``2``.

    :attr:`lines` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `1`.
    """

    overlap = BooleanProperty(True)
    """
    Determines if the `header/footer` overlaps on top of the image or not.

    :attr:`overlap` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    allow_stretch = BooleanProperty(True)
    """
    See :attr:`~kivy.uix.image.Image.allow_stretch`.

    :attr:`allow_stretch` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    anim_delay = NumericProperty(0.25)
    """
    See :attr:`~kivy.uix.image.Image.anim_delay`.

    :attr:`anim_delay` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.25`.
    """

    anim_loop = NumericProperty(0)
    """
    See :attr:`~kivy.uix.image.Image.anim_loop`.

    :attr:`anim_loop` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    keep_ratio = BooleanProperty(False)
    """
    See :attr:`~kivy.uix.image.Image.keep_ratio`.

    :attr:`keep_ratio` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    mipmap = BooleanProperty(False)
    """
    See :attr:`~kivy.uix.image.Image.mipmap`.

    :attr:`mipmap` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    source = StringProperty()
    """
    Path to tile image. See :attr:`~kivy.uix.image.Image.source`.

    :attr:`source` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

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
    font_style = StringProperty("Caption")
    """
    Tile font style.

    :attr:`font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Caption'`.
    """

    tile_text_color = ListProperty([1, 1, 1, 1])
    """
    Tile text color in ``rgba`` format.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to ``.
    """

    text = StringProperty("")
    """
    Determines the text for the box `footer/header`.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    _box_label = ObjectProperty()


class Star(MDIconButton):
    def on_touch_down(self, touch):
        return True


class SmartTileWithStar(SmartTileWithLabel):
    stars = NumericProperty(1)
    """
    Tile stars.

    :attr:`stars` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

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
    """
    An interface to specify widgets that belong to to the image overlay
    in the :class:`SmartTile` widget when added as a child.
    """


class IOverlay:
    """
    An interface to specify widgets that belong to to the image overlay
    in the :class:`SmartTile` widget when added as a child.
    """
