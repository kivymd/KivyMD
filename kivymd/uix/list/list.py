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

Events of List
--------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    ScrollView:

        MDList:

            OneLineAvatarIconListItem:
                on_release: print("Click!")

                IconLeftWidget:
                    icon: "github"

            OneLineAvatarIconListItem:
                on_release: print("Click 2!")

                IconLeftWidget:
                    icon: "gitlab"
    '''


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MainApp().run()

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

    OneLineIconListItem:
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


    MDBoxLayout:

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
            icon: "cog"

        YourContainer:
            id: container

            MDIconButton:
                icon: "minus"

            MDIconButton:
                icon: "plus"
    '''


    class YourContainer(IRightBodyTouch, MDBoxLayout):
        adaptive_width = True


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)


    MainApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-list-right-container.png
    :align: center

Behavior
--------

When using the `AvatarListItem` and `IconListItem` classes, when an icon is clicked,
the event of this icon is triggered:

.. code-block:: kv

    OneLineIconListItem:
        text: "Single-line item with icon"

        IconLeftWidget:
            icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/list-icon-trigger.gif
    :align: center

You can disable the icon event using the `WithoutTouch` classes:

.. code-block:: kv

    OneLineIconListItem:
        text: "Single-line item with icon"

        IconLeftWidgetWithoutTouch:
            icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/list-icon-without-trigger.gif
    :align: center
"""

__all__ = (
    "BaseListItem",
    "MDList",
    "ILeftBodyTouch",
    "IRightBodyTouch",
    "OneLineListItem",
    "TwoLineListItem",
    "ThreeLineListItem",
    "OneLineAvatarListItem",
    "TwoLineAvatarListItem",
    "ThreeLineAvatarListItem",
    "OneLineIconListItem",
    "TwoLineIconListItem",
    "ThreeLineIconListItem",
    "OneLineRightIconListItem",
    "TwoLineRightIconListItem",
    "ThreeLineRightIconListItem",
    "OneLineAvatarIconListItem",
    "TwoLineAvatarIconListItem",
    "ThreeLineAvatarIconListItem",
    "ImageLeftWidget",
    "ImageRightWidget",
    "IconRightWidget",
    "IconLeftWidget",
    "CheckboxLeftWidget",
    "IconLeftWidgetWithoutTouch",
    "IconRightWidgetWithoutTouch",
    "ImageRightWidgetWithoutTouch",
    "ImageLeftWidgetWithoutTouch",
)

import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout

import kivymd.material_resources as m_res
from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
)
from kivymd.uix.button import MDIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.selectioncontrol import MDCheckbox

with open(
    os.path.join(uix_path, "list", "list.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDList(MDGridLayout):
    """
    ListItem container. Best used in conjunction with a
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
    DeclarativeBehavior,
    ThemableBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    FloatLayout,
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

    text_color = ColorProperty(None)
    """
    Text color in ``rgba`` format used if :attr:`~theme_text_color` is set
    to `'Custom'`.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_style = StringProperty("Subtitle1")
    """
    Text font style. See ``kivymd.font_definitions.py``.

    :attr:`font_style` is a :class:`~kivy.properties.StringProperty`
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

    secondary_text_color = ColorProperty(None)
    """
    Text color in ``rgba`` format used for secondary text
    if :attr:`~secondary_theme_text_color` is set to `'Custom'`.

    :attr:`secondary_text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    tertiary_text_color = ColorProperty(None)
    """
    Text color in ``rgba`` format used for tertiary text
    if :attr:`~tertiary_theme_text_color` is set to 'Custom'.

    :attr:`tertiary_text_color` is a :class:`~kivy.properties.ColorProperty`
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

    secondary_font_style = StringProperty("Body1")
    """
    Font style for secondary line. See ``kivymd.font_definitions.py``.

    :attr:`secondary_font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    tertiary_font_style = StringProperty("Body1")
    """
    Font style for tertiary line. See ``kivymd.font_definitions.py``.

    :attr:`tertiary_font_style` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    divider = OptionProperty(
        "Full", options=["Full", "Inset", None], allownone=True
    )
    """
    Divider mode. Available options are: `'Full'`, `'Inset'`
    and default to `'Full'`.

    :attr:`divider` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `'Full'`.
    """

    divider_color = ColorProperty(None)
    """
    Divider color.

    .. versionadded:: 1.0.0

    :attr:`divider_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    bg_color = ColorProperty(None)
    """
    Background color for menu item.

    :attr:`bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([0], length=4)
    """
    Canvas radius.

    .. code-block:: python

        # Top left corner slice.
        MDBoxLayout:
            md_bg_color: app.theme_cls.primary_color
            radius: [25, 0, 0, 0]

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    _txt_left_pad = NumericProperty("16dp")
    _txt_top_pad = NumericProperty()
    _txt_bot_pad = NumericProperty()
    _txt_right_pad = NumericProperty(m_res.HORIZ_MARGINS)
    _num_lines = 3
    _no_ripple_effect = BooleanProperty(False)
    _touchable_widgets = ListProperty()

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

    def add_widget(self, widget):
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


class ILeftBody:
    """
    Pseudo-interface for widgets that go in the left container for
    ListItems that support it.

    Implements nothing and requires no implementation, for annotation only.
    """


class ILeftBodyTouch:
    """
    Same as :class:`~ILeftBody`, but allows the widget to receive touch
    events instead of triggering the ListItem's ripple effect.
    """


class IRightBody:
    """
    Pseudo-interface for widgets that go in the right container for
    ListItems that support it.

    Implements nothing and requires no implementation, for annotation only.
    """


class IRightBodyTouch:
    """
    Same as :class:`~IRightBody`, but allows the widget to receive touch
    events instead of triggering the ``ListItem``'s ripple effect
    """


class OneLineListItem(BaseListItem):
    """A one line list item."""

    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()
    _num_lines = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = dp(48) if not self._height else self._height


class TwoLineListItem(BaseListItem):
    """A two line list item."""

    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineListItem(BaseListItem):
    """A three line list item."""

    _txt_top_pad = NumericProperty("16dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()
    _num_lines = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = dp(88) if not self._height else self._height


class OneLineAvatarListItem(BaseListItem):
    _txt_left_pad = NumericProperty("72dp")
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("19dp")
    _height = NumericProperty()
    _num_lines = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = dp(56) if not self._height else self._height


class TwoLineAvatarListItem(OneLineAvatarListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineAvatarListItem(ThreeLineListItem):
    _txt_left_pad = NumericProperty("72dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OneLineIconListItem(OneLineListItem):
    _txt_left_pad = NumericProperty("72dp")


class TwoLineIconListItem(OneLineIconListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineIconListItem(ThreeLineListItem):
    _txt_left_pad = NumericProperty("72dp")


class OneLineRightIconListItem(OneLineListItem):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class TwoLineRightIconListItem(OneLineRightIconListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height


class ThreeLineRightIconListItem(ThreeLineListItem):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class OneLineAvatarIconListItem(OneLineAvatarListItem):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class TwoLineAvatarIconListItem(TwoLineAvatarListItem):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class ThreeLineAvatarIconListItem(ThreeLineAvatarListItem):
    _txt_right_pad = NumericProperty("40dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS


class TouchBehavior:
    def on_release(self):
        if issubclass(self.parent.parent.__class__, BaseListItem):
            self.parent.parent.dispatch("on_release")


class ImageLeftWidget(
    CircularRippleBehavior, ButtonBehavior, ILeftBodyTouch, FitImage
):
    pass


class ImageLeftWidgetWithoutTouch(
    CircularRippleBehavior, TouchBehavior, ButtonBehavior, ILeftBody, FitImage
):
    """
    .. versionadded:: 1.0.0
    """

    _no_ripple_effect = True


class ImageRightWidget(
    CircularRippleBehavior, ButtonBehavior, IRightBodyTouch, FitImage
):
    pass


class ImageRightWidgetWithoutTouch(
    CircularRippleBehavior, TouchBehavior, ButtonBehavior, IRightBody, FitImage
):
    """
    .. versionadded:: 1.0.0
    """

    _no_ripple_effect = True


class IconRightWidget(IRightBodyTouch, MDIconButton):
    pos_hint = {"center_y": 0.5}


class IconRightWidgetWithoutTouch(TouchBehavior, IRightBody, MDIconButton):
    """
    .. versionadded:: 1.0.0
    """

    pos_hint = {"center_y": 0.5}
    _no_ripple_effect = True


class IconLeftWidget(ILeftBodyTouch, MDIconButton):
    pos_hint = {"center_y": 0.5}


class IconLeftWidgetWithoutTouch(TouchBehavior, ILeftBody, MDIconButton):
    """
    .. versionadded:: 1.0.0
    """

    pos_hint = {"center_y": 0.5}
    _no_ripple_effect = True


class CheckboxLeftWidget(ILeftBodyTouch, MDCheckbox):
    pass
