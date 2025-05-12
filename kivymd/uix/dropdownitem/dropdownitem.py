"""
Components/DropdownItem
=======================

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dropdown-item.png
    :align: center

Usage
-----

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivymd.uix.menu import MDDropdownMenu

            from kivymd.app import MDApp

            KV = '''
            MDScreen
                md_bg_color: self.theme_cls.backgroundColor

                MDDropDownItem:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.open_menu(self)

                    MDDropDownItemText:
                        id: drop_text
                        text: "Item"
            '''


            class Example(MDApp):
                def open_menu(self, item):
                    menu_items = [
                        {
                            "text": f"{i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(caller=item, items=menu_items).open()

                def menu_callback(self, text_item):
                    self.root.ids.drop_text.text = text_item

                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.dropdownitem import MDDropDownItem, MDDropDownItemText
            from kivymd.uix.menu import MDDropdownMenu
            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def open_menu(self, item):
                    menu_items = [
                        {
                            "text": f"{i}",
                            "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                        } for i in range(5)
                    ]
                    MDDropdownMenu(caller=item, items=menu_items).open()

                def menu_callback(self, text_item):
                    self.root.get_ids().drop_text.text = text_item

                def build(self):
                    return (
                        MDScreen(
                            MDDropDownItem(
                                MDDropDownItemText(
                                    id="drop_text",
                                    text="Item",
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                                on_release=self.open_menu,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )


            Example().run()

.. seealso::

    `Work with the class MDDropdownMenu see here <https://kivymd.readthedocs.io/en/latest/components/menu/index.html#center-position>`_

API break
=========

1.2.0 version
-------------

.. code-block:: kv

    MDDropDownItem:
        text: 'Item'
        on_release: print(*args)

2.0.0 version
-------------

.. code-block:: kv

    MDDropDownItem:
        on_release:  print(*args)

        MDDropDownItemText:
            text: "Item text"
"""

__all__ = ("MDDropDownItem", "MDDropDownItemText")

import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.label import MDLabel

with open(
    os.path.join(uix_path, "dropdownitem", "dropdownitem.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


# FIXME: When resizing the texture of the `MDDropDownItemText` widget,
#  the canvas instruction that implements the triangle looks terrible.
#  You need to edit the Triangle instructions according to the size
#  of the `MDDropDownItemText` texture.
class MDDropDownItemText(MDLabel):
    """
    Base texture for :class:`~MDDropDownItem` class (item text).

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.

    .. versionadded:: 2.0.0
    """


class MDDropDownItem(
    DeclarativeBehavior, ThemableBehavior, ButtonBehavior, BoxLayout
):
    """
    Dropdown item class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    _drop_down_text = ObjectProperty()
    _size = ListProperty()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDDropDownItemText):
            self._drop_down_text = widget
            widget.bind(text=self.update_text_item)
            Clock.schedule_once(lambda x: self.on_disabled(self, self.disabled))
        else:
            return super().add_widget(widget)

    def update_text_item(self, instance, value) -> None:
        """Updates the text of the item."""

        self._drop_down_text.texture_update()
        drop_down_item_text = self.canvas.get_group("drop-down-item-text")[0]
        drop_down_item_text.texture = None
        drop_down_item_text.texture = self._drop_down_text.texture
        drop_down_item_text.size = self._drop_down_text.texture_size
        drop_down_item_text.pos = (self.x, self.y + dp(8))
        self._size = self._drop_down_text.texture_size

    def on_disabled(self, instance, value) -> None:
        """Fired when the values of :attr:`disabled` change."""

        self._drop_down_text.disabled = value
        drop_down_item_triangle_color = self.canvas.get_group(
            "drop-down-item-triangle-color"
        )[0]
        drop_down_item_triangle_color.rgba = (
            self._drop_down_text.disabled_color
            if value
            else self._drop_down_text.color
        )

    def on__drop_down_text(self, instance, value) -> None:
        """Fired when the values of :attr:`_drop_down_text` change."""

        def set_size(*args):
            self._size = value.texture_size

        Clock.schedule_once(set_size)
