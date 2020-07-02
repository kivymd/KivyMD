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
    <MyTile@SmartTileWithStar>
        size_hint_y: None
        height: "240dp"


    ScrollView:

        MDGridLayout:
            cols: 3
            adaptive_height: True
            padding: dp(4), dp(4)
            spacing: dp(4)

            MyTile:
                stars: 5
                source: "cat-1.jpg"

            MyTile:
                stars: 5
                source: "cat-2.jpg"

            MyTile:
                stars: 5
                source: "cat-3.jpg"
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
    <MyTile@SmartTileWithStar>
        size_hint_y: None
        height: "240dp"


    ScrollView:

        MDGridLayout:
            cols: 3
            adaptive_height: True
            padding: dp(4), dp(4)
            spacing: dp(4)

            MyTile:
                source: "cat-1.jpg"
                text: "[size=26]Cat 1[/size]\\n[size=14]cat-1.jpg[/size]"

            MyTile:
                source: "cat-2.jpg"
                text: "[size=26]Cat 2[/size]\\n[size=14]cat-2.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color

            MyTile:
                source: "cat-3.jpg"
                text: "[size=26][color=#ffffff]Cat 3[/color][/size]\\n[size=14]cat-3.jpg[/size]"
                tile_text_color: app.theme_cls.accent_color
    '''


    class MyApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MyApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/SmartTileWithLabel.png
    :align: center
"""

__all__ = ("SmartTile", "SmartTileWithLabel", "SmartTileWithStar")

from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
    """
<SmartTile>
    _img_widget: img
    _img_overlay: img_overlay
    _box_overlay: box

    FitImage:
        id: img
        source: root.source
        x: root.x
        y: root.y if root.overlap or root.box_position == 'header' else box.top

    BoxLayout:
        id: img_overlay
        size_hint: img.size_hint
        size: img.size
        pos: img.pos

    MDBoxLayout:
        id: box
        md_bg_color: root.box_color
        size_hint_y: None
        height: "68dp" if root.lines == 2 else "48dp"
        x: root.x
        y: root.y if root.box_position == 'footer' else root.y + root.height - self.height


<SmartTileWithLabel>
    _img_widget: img
    _img_overlay: img_overlay
    _box_overlay: box
    _box_label: boxlabel

    FitImage:
        id: img
        source: root.source
        x: root.x
        y: root.y if root.overlap or root.box_position == 'header' else box.top

    BoxLayout:
        id: img_overlay
        size_hint: img.size_hint
        size: img.size
        pos: img.pos

    MDBoxLayout:
        id: box
        padding: "5dp", 0, 0, 0
        md_bg_color: root.box_color
        adaptive_height: True
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


class SmartTile(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, MDFloatLayout
):
    """
    A tile for more complex needs.

    Includes an image, a container to place overlays and a box that can act
    as a header or a footer, as described in the Material Design specs.
    """

    box_color = ListProperty((0, 0, 0, 0.5))
    """
    Sets the color and opacity for the information box.

    :attr:`box_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `(0, 0, 0, 0.5)`.
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


class SmartTileWithLabel(SmartTile):
    font_style = StringProperty("Caption")
    """
    Tile font style.

    :attr:`font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Caption'`.
    """

    tile_text_color = ListProperty((1, 1, 1, 1))
    """
    Tile text color in ``rgba`` format.

    :attr:`tile_text_color` is a :class:`~kivy.properties.StringProperty`
    and defaults to `(1, 1, 1, 1)`.
    """

    text = StringProperty()
    """
    Determines the text for the box `footer/header`.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    _box_label = ObjectProperty()


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
                _Star(
                    icon="star-outline",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                )
            )


class _Star(MDIconButton):
    def on_touch_down(self, touch):
        return True
