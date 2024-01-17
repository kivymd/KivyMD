"""
Components/List
===============

.. seealso::

    `Material Design spec, Lists <https://m3.material.io/components/lists/overview>`_

.. rubric:: Lists are continuous, vertical indexes of text or images.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.png
    :align: center

- Use lists to help users find a specific item and act on it;
- Order list items in logical ways (like alphabetical or numerical);
- Three sizes: one-line, two-line, and three-line;
- Keep items short and easy to scan;
- Show icons, text, and actions in a consistent format;

Usage
-----

.. code-block:: kv

    MDListItem:

        MDListItemLeadingIcon:  # MDListItemLeadingAvatar

        MDListItemHeadlineText:

        MDListItemSupportingText:

        MDListItemTertiaryText:

        MDListItemTrailingIcon:  # MDListItemTrailingCheckbox

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists-anatomy.png
    :align: center

Example:
========

One line list item
------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDListItem:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: .8

                    MDListItemHeadlineText:
                        text: "Headline"
            '''


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python styles

        .. code-block:: python

            from kivymd.uix.list import MDListItem, MDListItemHeadlineText
            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp


            class Example(MDApp):
                def build(self):
                    return (
                        MDScreen(
                            MDListItem(
                                MDListItemHeadlineText(
                                    text="Headline",
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                size_hint_x=0.8,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-list.gif
    :align: center

Two line list item
------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDListItem:

                MDListItemHeadlineText:
                    text: "Headline"

                MDListItemSupportingText:
                    text: "Supporting text"

    .. tab:: Declarative Python styles

        .. code-block:: python

            MDListItem(
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-supporting-list.png
    :align: center

Three line list item
--------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDListItem:

                MDListItemHeadlineText:
                    text: "Headline"

                MDListItemSupportingText:
                    text: "Supporting text"

                MDListItemTertiaryText:
                    text: "Tertiary text"

    .. tab:: Declarative Python styles

        .. code-block:: python

            MDListItem(
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
                MDListItemTertiaryText(
                    text="Tertiary text",
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-supporting-tertiary-list.png
    :align: center

List item with leading icon
---------------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDListItem:

                MDListItemLeadingIcon:
                    icon: "account"

                MDListItemHeadlineText:
                    text: "Headline"

                MDListItemSupportingText:
                    text: "Supporting text"

                MDListItemTertiaryText:
                    text: "Tertiary text"

    .. tab:: Declarative Python styles

        .. code-block:: python

            MDListItem(
                MDListItemLeadingIcon(
                    icon="account",
                ),
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
                MDListItemTertiaryText(
                    text="Tertiary text",
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-supporting-tertiary-leading-icon-list.png
    :align: center

List item with trailing icon
----------------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDListItem:

                MDListItemLeadingIcon:
                    icon: "account"

                MDListItemHeadlineText:
                    text: "Headline"

                MDListItemSupportingText:
                    text: "Supporting text"

                MDListItemTertiaryText:
                    text: "Tertiary text"

                MDListItemTrailingIcon:
                    icon: "trash-can-outline"

    .. tab:: Declarative Python styles

        .. code-block:: python

            MDListItem(
                MDListItemLeadingIcon(
                    icon="account",
                ),
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
                MDListItemTertiaryText(
                    text="Tertiary text",
                ),
                MDListItemTrailingIcon(
                    icon="trash-can-outline",
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-supporting-tertiary-leading-trailing-icon-list.png
    :align: center

List item with trailing check
-----------------------------

.. tabs::

    .. tab:: Declarative KV styles

        .. code-block:: kv

            MDListItem:

                MDListItemLeadingIcon:
                    icon: "account"

                MDListItemHeadlineText:
                    text: "Headline"

                MDListItemSupportingText:
                    text: "Supporting text"

                MDListItemTertiaryText:
                    text: "Tertiary text"

                MDListItemTrailingCheckbox:

    .. tab:: Declarative Python styles

        .. code-block:: python

            MDListItem(
                MDListItemLeadingIcon(
                    icon="account",
                ),
                MDListItemHeadlineText(
                    text="Headline",
                ),
                MDListItemSupportingText(
                    text="Supporting text",
                ),
                MDListItemTertiaryText(
                    text="Tertiary text",
                ),
                MDListItemTrailingCheckbox(
                ),
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/headline-supporting-tertiary-leading-trailing-check-list.png
    :align: center
"""

from __future__ import annotations

__all__ = (
    "BaseListItemText",
    "BaseListItem",
    "BaseListItemIcon",
    "MDList",
    "MDListItem",
    "MDListItemHeadlineText",
    "MDListItemSupportingText",
    "MDListItemTrailingSupportingText",
    "MDListItemLeadingIcon",
    "MDListItemTrailingIcon",
    "MDListItemTrailingCheckbox",
    "MDListItemLeadingAvatar",
    "MDListItemTertiaryText",
)

import os

from kivy import Logger
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    BooleanProperty,
    ColorProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    DeclarativeBehavior,
    RectangularRippleBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.fitimage import FitImage
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon

with open(
    os.path.join(uix_path, "list", "list.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDList(MDGridLayout):
    """
    ListItem container.
    Best used in conjunction with a :class:`kivy.uix.ScrollView`.

    When adding (or removing) a widget, it will resize itself to fit its
    children, plus top and bottom paddings as described by the `MD` spec.

    For more information, see in the
    :class:`~kivymd.uix.gridlayout.MDGridLayout` class documentation.
    """

    _list_vertical_padding = NumericProperty("8dp")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adaptive_height = True


class BaseListItem(
    DeclarativeBehavior,
    BackgroundColorBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    ThemableBehavior,
    StateLayerBehavior,
):
    """
    Base class for list items.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.behaviors.state_layer_behavior.StateLayerBehavior`
    classes documentation.
    """

    divider = BooleanProperty(False)
    """
    Should I use divider for a list item.

    :attr:`divider` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    divider_color = ColorProperty(None)
    """
    The divider color in (r, g, b, a) or string format.

    :attr:`divider_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the list item when
    the list item is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class BaseListItemText(MDLabel):
    """
    Base class for text labels of a list item.

    For more information, see in the :class:`~kivymd.uix.label.label.MDLabel`
    class documentation.
    """


class BaseListItemIcon(MDIcon):
    """
    Base class for leading/trailing icon of list item.

    For more information, see in the :class:`~kivymd.uix.label.label.MDIcon`
    class documentation.
    """

    icon_color = ColorProperty(None)
    """
    Icon color in (r, g, b, a) or string format.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_disabled = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the list item when
    the list item is disabled.

    :attr:`icon_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class MDListItemHeadlineText(BaseListItemText):
    """
    Implements a class for headline text of list item.

    For more information, see in the :class:`~BaseListItemText`
    class documentation.
    """


class MDListItemSupportingText(BaseListItemText):
    """
    Implements a class for secondary text of list item.

    For more information, see in the :class:`~BaseListItemText`
    class documentation.
    """


class MDListItemTertiaryText(BaseListItemText):
    """
    Implements a class for tertiary text of list item.

    For more information, see in the :class:`~BaseListItemText`
    class documentation.
    """


class MDListItemTrailingSupportingText(BaseListItemText):
    """
    Implements a class for trailing text of list item.

    For more information, see in the :class:`~BaseListItemText`
    class documentation.
    """


class MDListItemLeadingIcon(BaseListItemIcon):
    """
    Implements a class for leading icon class.

    For more information, see in the :class:`~BaseListItemIcon`
    class documentation.
    """


class MDListItemLeadingAvatar(
    ThemableBehavior, CircularRippleBehavior, ButtonBehavior, FitImage
):
    """
    Implements a class for leading avatar class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.fitimage.fitimage.FitImage`
    classes documentation.
    """

    _list_item = ObjectProperty()


class MDListItemTrailingIcon(BaseListItemIcon):
    """
    Implements a class for trailing icon class.

    For more information, see in the :class:`~BaseListItemIcon`
    class documentation.
    """


class MDListItemTrailingCheckbox(MDCheckbox):
    """
    Implements a class for trailing checkbox class.

    For more information, see in the
    :class:`~kivymd.uix.selectioncontrol.selectioncontrol.MDCheckbox`
    class documentation.
    """


class MDListItem(BaseListItem, BoxLayout):
    """
    Implements a list item.

    For more information, see in the
    :class:`~BaseListItem` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(
            widget,
            (
                MDListItemHeadlineText,
                MDListItemSupportingText,
                MDListItemTertiaryText,
            ),
        ):
            if len(self.ids.text_container.children) < 3:
                self.ids.text_container.add_widget(widget)
            elif len(self.ids.text_container.children) > 3:
                self._set_warnings(widget)
        elif isinstance(
            widget, (MDListItemLeadingIcon, MDListItemLeadingAvatar)
        ):
            if not self.ids.leading_container.children:
                widget._list_item = self
                self.ids.leading_container.add_widget(widget)
                Clock.schedule_once(
                    lambda x: self._set_with_container(
                        self.ids.leading_container, widget
                    )
                )
            else:
                self._set_warnings(widget)
        elif isinstance(
            widget,
            (
                MDListItemTrailingIcon,
                MDListItemTrailingCheckbox,
                MDListItemTrailingSupportingText,
            ),
        ):
            if not self.ids.trailing_container.children:
                self.ids.trailing_container.add_widget(widget)
                Clock.schedule_once(
                    lambda x: self._set_with_container(
                        self.ids.trailing_container, widget
                    )
                )
            else:
                self._set_warnings(widget)
        else:
            return super().add_widget(widget)

    def _set_warnings(self, widget):
        Logger.warning(
            f"KivyMD: "
            f"Do not use more than one <{widget.__class__.__name__}> "
            f"widget. This is contrary to the material design rules "
            f"of version 3"
        )

    def _set_with_container(self, container, widget):
        container.width = widget.width
