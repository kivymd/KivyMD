"""
Components/List
===============

.. seealso::

    `Material Design spec, Lists <https://material.io/components/lists>`_

.. rubric:: Lists are continuous, vertical indexes of text or images.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.png
    :align: center

The class :class:`~MDList` in combination with a :class:`~BaseListItem` like
:class:`~OneLineListItem` will create a list that expands as items are added to
it, working nicely with `Kivy's` :class:`~kivy.uix.scrollview.ScrollView`.

Due to the variety in sizes and controls in the `Material Design spec`,
this module suffers from a certain level of complexity to keep the widgets
compliant, flexible and performant.

For this `KivyMD` provides list items that try to cover the most common usecases,
when those are insufficient, there's a base class called :class:`~BaseListItem`
which you can use to create your own list items. This documentation will only
cover the provided ones, for custom implementations please refer to this
module's source code.

`KivyMD` provides the following list items classes for use:

Text only ListItems
-------------------

- OneLineListItem_
- TwoLineListItem_
- ThreeLineListItem_

ListItems with widget containers
--------------------------------

These widgets will take other widgets that inherit from :class:`~ILeftBody`,
:class:`ILeftBodyTouch`, :class:`~IRightBody` or :class:`~IRightBodyTouch` and
put them in their corresponding container.

As the name implies, :class:`~ILeftBody` and :class:`~IRightBody` will signal
that the widget goes into the left or right container, respectively.

:class:`~ILeftBodyTouch` and :class:`~IRightBodyTouch` do the same thing,
except these widgets will also receive touch events that occur within their
surfaces.

`KivyMD` provides base classes such as :class:`~ImageLeftWidget`,
:class:`~ImageRightWidget`, :class:`~IconRightWidget`, :class:`~IconLeftWidget`,
based on the above classes.

.. rubric:: Allows the use of items with custom widgets on the left.

- OneLineAvatarListItem_
- TwoLineAvatarListItem_
- ThreeLineAvatarListItem_
- OneLineIconListItem_
- TwoLineIconListItem_
- ThreeLineIconListItem_

.. rubric:: It allows the use of elements with custom widgets on the left
    and the right.

- OneLineAvatarIconListItem_
- TwoLineAvatarIconListItem_
- ThreeLineAvatarIconListItem_

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.list import OneLineListItem

    KV = '''
    ScrollView:

        MDList:
            id: container
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(20):
                self.root.ids.container.add_widget(
                    OneLineListItem(text=f"Single-line item {i}")
                )

    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.gif
    :align: center

.. OneLineListItem:
OneLineListItem
---------------

.. code-block:: kv

    OneLineListItem:
        text: "Single-line item"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/OneLineListItem.png
    :align: center

.. TwoLineListItem:
TwoLineListItem
---------------

.. code-block:: kv

    TwoLineListItem:
        text: "Two-line item"
        secondary_text: "Secondary text here"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/TwoLineListItem.png
    :align: center

.. ThreeLineListItem:
ThreeLineListItem
-----------------

.. code-block:: kv

    ThreeLineListItem:
        text: "Three-line item"
        secondary_text: "This is a multi-line label where you can"
        tertiary_text: "fit more text than usual"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ThreeLineListItem.png
    :align: center

.. OneLineAvatarListItem:
OneLineAvatarListItem
---------------------

.. code-block:: kv

    OneLineAvatarListItem:
        text: "Single-line item with avatar"

        ImageLeftWidget:
            source: "data/logo/kivy-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists-map.png
    :align: center

.. TwoLineAvatarListItem:
TwoLineAvatarListItem
---------------------

.. code-block:: kv

    TwoLineAvatarListItem:
        text: "Two-line item with avatar"
        secondary_text: "Secondary text here"

        ImageLeftWidget:
            source: "data/logo/kivy-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/TwoLineAvatarListItem.png
    :align: center


.. ThreeLineAvatarListItem:
ThreeLineAvatarListItem
-----------------------

.. code-block:: kv

    ThreeLineAvatarListItem:
        text: "Three-line item with avatar"
        secondary_text: "Secondary text here"
        tertiary_text: "fit more text than usual"

        ImageLeftWidget:
            source: "data/logo/kivy-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ThreeLineAvatarListItem.png
    :align: center

.. OneLineIconListItem:
OneLineIconListItem
-------------------

.. code-block:: kv

    OneLineAvatarListItem:
        text: "Single-line item with avatar"

        IconLeftWidget:
            icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/OneLineIconListItem.png
    :align: center

.. TwoLineIconListItem:
TwoLineIconListItem
-------------------

.. code-block:: kv

    TwoLineIconListItem:
        text: "Two-line item with avatar"
        secondary_text: "Secondary text here"

        IconLeftWidget:
            icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/TwoLineIconListItem.png
    :align: center

.. ThreeLineIconListItem:
ThreeLineIconListItem
---------------------

.. code-block:: kv

    ThreeLineIconListItem:
        text: "Three-line item with avatar"
        secondary_text: "Secondary text here"
        tertiary_text: "fit more text than usual"

        IconLeftWidget:
            icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ThreeLineIconListItem.png
    :align: center

.. OneLineAvatarIconListItem:
OneLineAvatarIconListItem
-------------------------

.. code-block:: kv

    OneLineAvatarIconListItem:
        text: "One-line item with avatar"

        IconLeftWidget:
            icon: "plus"

        IconRightWidget:
            icon: "minus"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/OneLineAvatarIconListItem.png
    :align: center

.. TwoLineAvatarIconListItem:
TwoLineAvatarIconListItem
-------------------------

.. code-block:: kv

    TwoLineAvatarIconListItem:
        text: "Two-line item with avatar"
        secondary_text: "Secondary text here"

        IconLeftWidget:
            icon: "plus"

        IconRightWidget:
            icon: "minus"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/TwoLineAvatarIconListItem.png
    :align: center

.. ThreeLineAvatarIconListItem:
ThreeLineAvatarIconListItem
---------------------------

.. code-block:: kv

    ThreeLineAvatarIconListItem:
        text: "Three-line item with avatar"
        secondary_text: "Secondary text here"
        tertiary_text: "fit more text than usual"

        IconLeftWidget:
            icon: "plus"

        IconRightWidget:
            icon: "minus"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ThreeLineAvatarIconListItem.png
    :align: center

Custom list item
----------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
    from kivymd.uix.selectioncontrol import MDCheckbox
    from kivymd.icon_definitions import md_icons


    KV = '''
    <ListItemWithCheckbox>:

        IconLeftWidget:
            icon: root.icon

        RightCheckbox:


    BoxLayout:

        ScrollView:

            MDList:
                id: scroll
    '''


    class ListItemWithCheckbox(OneLineAvatarIconListItem):
        '''Custom list item.'''

        icon = StringProperty("android")


    class RightCheckbox(IRightBodyTouch, MDCheckbox):
        '''Custom right container.'''


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            icons = list(md_icons.keys())
            for i in range(30):
                self.root.ids.scroll.add_widget(
                    ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
                )


    MainApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-list-item.png
    :align: center

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.list import IRightBodyTouch

    KV = '''
    OneLineAvatarIconListItem:
        text: "One-line item with avatar"
        on_size:
            self.ids._right_container.width = container.width
            self.ids._right_container.x = container.width

        IconLeftWidget:
            icon: "settings"

        Container:
            id: container

            MDIconButton:
                icon: "minus"

            MDIconButton:
                icon: "plus"
    '''


    class Container(IRightBodyTouch, MDBoxLayout):
        adaptive_width = True


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MainApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-list-right-container.png
    :align: center
"""

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    StringProperty,
    NumericProperty,
    ListProperty,
    OptionProperty,
    BooleanProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

import kivymd.material_resources as m_res
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.button import MDIconButton
from kivymd.theming import ThemableBehavior
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.selectioncontrol import MDCheckbox

Builder.load_string(
    """
#:import m_res kivymd.material_resources


<MDList>
    cols: 1
    adaptive_height: True
    padding: 0, self._list_vertical_padding


<BaseListItem>
    size_hint_y: None
    canvas:
        Color:
            rgba:
                self.theme_cls.divider_color if root.divider is not None\
                else (0, 0, 0, 0)
        Line:
            points: (root.x ,root.y, root.x+self.width, root.y)\
                    if root.divider == 'Full' else\
                    (root.x+root._txt_left_pad, root.y,\
                    root.x+self.width-root._txt_left_pad-root._txt_right_pad,\
                    root.y)
        Color:
            rgba: root.bg_color if root.bg_color else (0, 0, 0, 0)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        id: _text_container
        orientation: 'vertical'
        pos: root.pos
        padding:
            root._txt_left_pad, root._txt_top_pad,\
            root._txt_right_pad, root._txt_bot_pad

        MDLabel:
            id: _lbl_primary
            text: root.text
            font_style: root.font_style
            theme_text_color: root.theme_text_color
            text_color: root.text_color
            size_hint_y: None
            height: self.texture_size[1]
            markup: True
            shorten_from: 'right'
            shorten: True

        MDLabel:
            id: _lbl_secondary
            text: '' if root._num_lines == 1 else root.secondary_text
            font_style: root.secondary_font_style
            theme_text_color: root.secondary_theme_text_color
            text_color: root.secondary_text_color
            size_hint_y: None
            height: 0 if root._num_lines == 1 else self.texture_size[1]
            shorten: True
            shorten_from: 'right'
            markup: True

        MDLabel:
            id: _lbl_tertiary
            text: '' if root._num_lines == 1 else root.tertiary_text
            font_style: root.tertiary_font_style
            theme_text_color: root.tertiary_theme_text_color
            text_color: root.tertiary_text_color
            size_hint_y: None
            height: 0 if root._num_lines == 1 else self.texture_size[1]
            shorten: True
            shorten_from: 'right'
            markup: True


<OneLineAvatarListItem>

    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height/2 - self.height/2
        size: dp(40), dp(40)


<ThreeLineAvatarListItem>

    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height - root._txt_top_pad - self.height - dp(5)
        size: dp(40), dp(40)


<OneLineIconListItem>

    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)


<ThreeLineIconListItem>
    BoxLayout:
        id: _left_container
        size_hint: None, None
        x: root.x + dp(16)
        y: root.y + root.height - root._txt_top_pad - self.height - dp(5)
        size: dp(48), dp(48)


<OneLineRightIconListItem>

    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)


<ThreeLineRightIconListItem>

    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)


<OneLineAvatarIconListItem>

    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)


<TwoLineAvatarIconListItem>

    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
        y: root.y + root.height/2 - self.height/2
        size: dp(48), dp(48)


<ThreeLineAvatarIconListItem>

    BoxLayout:
        id: _right_container
        size_hint: None, None
        x: root.x + root.width - m_res.HORIZ_MARGINS - self.width
        y: root.y + root.height - root._txt_top_pad - self.height - dp(5)
        size: dp(48), dp(48)
"""
)


class MDList(MDGridLayout):
    """ListItem container. Best used in conjunction with a
    :class:`kivy.uix.ScrollView`.

    When adding (or removing) a widget, it will resize itself to fit its
    children, plus top and bottom paddings as described by the `MD` spec.
    """

    _list_vertical_padding = NumericProperty("8dp")

    def add_widget(self, widget, index=0, canvas=None):
        super().add_widget(widget, index, canvas)
        self.height += widget.height

    def remove_widget(self, widget):
        super().remove_widget(widget)
        self.height -= widget.height


class BaseListItem(
    ThemableBehavior, RectangularRippleBehavior, ButtonBehavior, FloatLayout
):
    """
    Base class to all ListItems. Not supposed to be instantiated on its own.
    """

    text = StringProperty()
    """
    Text shown in the first line.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    text_color = ListProperty(None)
    """
    Text color in ``rgba`` format used if :attr:`~theme_text_color` is set
    to `'Custom'`.
    
    :attr:`text_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.
    """

    font_style = OptionProperty("Subtitle1", options=theme_font_styles)
    """
    Text font style. See ``kivymd.font_definitions.py``.

    :attr:`font_style` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Subtitle1'`.
    """

    theme_text_color = StringProperty("Primary", allownone=True)
    """
    Theme text color in ``rgba`` format for primary text.

    :attr:`theme_text_color` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Primary'`.
    """

    secondary_text = StringProperty()
    """
    Text shown in the second line.

    :attr:`secondary_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    tertiary_text = StringProperty()
    """
    The text is displayed on the third line.

    :attr:`tertiary_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    secondary_text_color = ListProperty(None)
    """
    Text color in ``rgba`` format used for secondary text
    if :attr:`~secondary_theme_text_color` is set to `'Custom'`.

    :attr:`secondary_text_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.
    """

    tertiary_text_color = ListProperty(None)
    """
    Text color in ``rgba`` format used for tertiary text
    if :attr:`~secondary_theme_text_color` is set to 'Custom'.

    :attr:`tertiary_text_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.
    """

    secondary_theme_text_color = StringProperty("Secondary", allownone=True)
    """
    Theme text color for secondary text.

    :attr:`secondary_theme_text_color` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Secondary'`.
    """

    tertiary_theme_text_color = StringProperty("Secondary", allownone=True)
    """
    Theme text color for tertiary text.

    :attr:`tertiary_theme_text_color` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Secondary'`.
    """

    secondary_font_style = OptionProperty("Body1", options=theme_font_styles)
    """
    Font style for secondary line. See ``kivymd.font_definitions.py``.

    :attr:`secondary_font_style` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Body1'`.
    """

    tertiary_font_style = OptionProperty("Body1", options=theme_font_styles)
    """
    Font style for tertiary line. See ``kivymd.font_definitions.py``.

    :attr:`tertiary_font_style` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Body1'`.
    """

    divider = OptionProperty(
        "Full", options=["Full", "Inset", None], allownone=True
    )
    """
    Divider mode. Available options are: `'Full'`, `'Inset'`
    and default to `'Full'`.

    :attr:`tertiary_font_style` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Body1'`.
    """

    bg_color = ListProperty()
    """
    Background color for menu item.

    :attr:`bg_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    _txt_left_pad = NumericProperty("16dp")
    _txt_top_pad = NumericProperty()
    _txt_bot_pad = NumericProperty()
    _txt_right_pad = NumericProperty(m_res.HORIZ_MARGINS)
    _num_lines = 3
    _no_ripple_effect = BooleanProperty(False)


class ILeftBody:
    """
    Pseudo-interface for widgets that go in the left container for
    ListItems that support it.

    Implements nothing and requires no implementation, for annotation only.
    """

    pass


class ILeftBodyTouch:
    """
    Same as :class:`~ILeftBody`, but allows the widget to receive touch
    events instead of triggering the ListItem's ripple effect.
    """

    pass


class IRightBody:
    """
    Pseudo-interface for widgets that go in the right container for
    ListItems that support it.

    Implements nothing and requires no implementation, for annotation only.
    """

    pass


class IRightBodyTouch:
    """
    Same as :class:`~IRightBody`, but allows the widget to receive touch
    events instead of triggering the ``ListItem``'s ripple effect
    """

    pass


class ContainerSupport:
    """
    Overrides ``add_widget`` in a ``ListItem`` to include support
    for ``I*Body`` widgets when the appropiate containers are present.
    """

    _touchable_widgets = ListProperty()

    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, ILeftBody):
            self.ids._left_container.add_widget(widget)
        elif issubclass(widget.__class__, ILeftBodyTouch):
            self.ids._left_container.add_widget(widget)
            self._touchable_widgets.append(widget)
        elif issubclass(widget.__class__, IRightBody):
            self.ids._right_container.add_widget(widget)
        elif issubclass(widget.__class__, IRightBodyTouch):
            self.ids._right_container.add_widget(widget)
            self._touchable_widgets.append(widget)
        else:
            return super().add_widget(widget)

    def remove_widget(self, widget):
        super().remove_widget(widget)
        if widget in self._touchable_widgets:
            self._touchable_widgets.remove(widget)

    def on_touch_down(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, "down"):
            return
        super().on_touch_down(touch)

    def on_touch_move(self, touch, *args):
        if self.propagate_touch_to_touchable_widgets(touch, "move", *args):
            return
        super().on_touch_move(touch, *args)

    def on_touch_up(self, touch):
        if self.propagate_touch_to_touchable_widgets(touch, "up"):
            return
        super().on_touch_up(touch)

    def propagate_touch_to_touchable_widgets(self, touch, touch_event, *args):
        triggered = False
        for i in self._touchable_widgets:
            if i.collide_point(touch.x, touch.y):
                triggered = True
                if touch_event == "down":
                    i.on_touch_down(touch)
                elif touch_event == "move":
                    i.on_touch_move(touch, *args)
                elif touch_event == "up":
                    i.on_touch_up(touch)
        return triggered


class OneLineListItem(BaseListItem):
    """A one line list item."""

    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(48) if not self._height else self._height


class TwoLineListItem(BaseListItem):
    """A two line list item."""

    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineListItem(BaseListItem):
    """A three line list item."""

    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 3

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(88) if not self._height else self._height


class OneLineAvatarListItem(ContainerSupport, BaseListItem):
    _txt_left_pad = NumericProperty("72dp")
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("19dp")  # dp(24) - dp(5)
    _height = NumericProperty()
    _num_lines = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(56) if not self._height else self._height


class TwoLineAvatarListItem(OneLineAvatarListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineAvatarListItem(ContainerSupport, ThreeLineListItem):
    _txt_left_pad = NumericProperty("72dp")


class OneLineIconListItem(ContainerSupport, OneLineListItem):
    _txt_left_pad = NumericProperty("72dp")


class TwoLineIconListItem(OneLineIconListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineIconListItem(ContainerSupport, ThreeLineListItem):
    _txt_left_pad = NumericProperty("72dp")


class OneLineRightIconListItem(ContainerSupport, OneLineListItem):
    # dp(40) = dp(16) + dp(24):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class TwoLineRightIconListItem(OneLineRightIconListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineRightIconListItem(ContainerSupport, ThreeLineListItem):
    # dp(40) = dp(16) + dp(24):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class OneLineAvatarIconListItem(OneLineAvatarListItem):
    # dp(40) = dp(16) + dp(24):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class TwoLineAvatarIconListItem(TwoLineAvatarListItem):
    # dp(40) = dp(16) + dp(24):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class ThreeLineAvatarIconListItem(ThreeLineAvatarListItem):
    # dp(40) = dp(16) + dp(24):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class ImageLeftWidget(ILeftBody, Image):
    pass


class ImageRightWidget(IRightBodyTouch, Image):
    pass


class IconRightWidget(IRightBodyTouch, MDIconButton):
    pass


class IconLeftWidget(ILeftBodyTouch, MDIconButton):
    pass


class CheckboxRightWidget(ILeftBodyTouch, MDCheckbox):
    pass
