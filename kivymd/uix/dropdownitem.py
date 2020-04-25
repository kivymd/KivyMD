"""
Components/Dropdown Item
========================

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-item.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    Screen

        MDDropDownItem:
            id: drop_item
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'Item'
            on_release: self.set_item("New Item")
    '''


    class Test(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)

        def build(self):
            return self.screen


    Test().run()

.. seealso::

    `Work with the class MDDropdownMenu see here <https://kivymd.readthedocs.io/en/latest/components/menu/index.html#center-position>`_
"""

__all__ = ("MDDropDownItem",)

from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget

from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<_Triangle>:
    canvas:
        Color:
            rgba: root.theme_cls.text_color
        Triangle:
            points:
                [ \
                self.right-14, self.y+7, \
                self.right-7, self.y+7, \
                self.right-7, self.y+14 \
                ]


<MDDropDownItem>
    orientation: "vertical"
    adaptive_size: True
    spacing: "5dp"
    padding: "5dp", "5dp", "5dp", 0

    MDBoxLayout:
        adaptive_size: True
        spacing: "10dp"

        Label:
            id: label_item
            size_hint: None, None
            size: self.texture_size
            color: root.theme_cls.text_color
            font_size: root.font_size


        _Triangle:
            size_hint: None, None
            size: "20dp", "20dp"

    MDSeparator:
"""
)


class _Triangle(ThemableBehavior, Widget):
    pass


class MDDropDownItem(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, MDBoxLayout
):
    text = StringProperty()
    """
    Text item.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    current_item = StringProperty()
    """
    Current name item.

    :attr:`current_item` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("16sp")
    """
    Item font size.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'16sp'`.
    """

    def on_text(self, instance, value):
        self.ids.label_item.text = value

    def set_item(self, name_item):
        """Sets new text for an item."""

        self.ids.label_item.text = name_item
        self.current_item = name_item
