"""
Components/Chip
===============

.. seealso::

    `Material Design spec, Chips <https://material.io/components/chips>`_

.. rubric:: Chips are compact elements that represent an input, attribute, or action.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chips.png
    :align: center

Usage
-----

.. code-block:: kv

    MDChip:
        text: 'Coffee'
        color: .4470588235118, .1960787254902, 0, 1
        icon: 'coffee'
        on_release: app.callback_for_menu_items(self)

The user function takes two arguments - the object and the text of the chip:

.. code-block:: python

    def callback_for_menu_items(self, instance):
        print(instance)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ordinary-chip.png
    :align: center

Use custom icon
---------------

.. code-block:: kv

    MDChip:
        text: 'Kivy'
        icon: 'data/logo/kivy-icon-256.png'

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-custom-icon.png
    :align: center

Use without icon
----------------

.. code-block:: kv

    MDChip:
        text: 'Without icon'
        icon: ''

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-without-icon.png
    :align: center

Chips with check
----------------

.. code-block:: kv

    MDChip:
        text: 'Check with icon'
        icon: 'city'
        check: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-check-icon.gif
    :align: center

Choose chip
-----------

.. code-block:: kv

    MDChooseChip:

        MDChip:
            text: 'Earth'
            icon: 'earth'
            selected_chip_color: .21176470535294, .098039627451, 1, 1

        MDChip:
            text: 'Face'
            icon: 'face'
            selected_chip_color: .21176470535294, .098039627451, 1, 1

        MDChip:
            text: 'Facebook'
            icon: 'facebook'
            selected_chip_color: .21176470535294, .098039627451, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-shoose-icon.gif
    :align: center

.. Note:: `See full example <https://github.com/kivymd/KivyMD/wiki/Components-Chip>`_
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDIcon
from kivymd.uix.stacklayout import MDStackLayout

Builder.load_string(
    """
#:import DEVICE_TYPE kivymd.material_resources.DEVICE_TYPE


<MDChooseChip>
    adaptive_height: True
    spacing: "5dp"


<MDChip>
    size_hint: None,  None
    height: "26dp"
    padding: 0, 0, "8dp", 0
    width:
        self.minimum_width - (dp(10) if DEVICE_TYPE == "desktop" else dp(20)) \
        if root.icon != 'checkbox-blank-circle' else self.minimum_width

    canvas:
        Color:
            rgba: root.theme_cls.primary_color if not root.color else root.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius

    MDBoxLayout:
        id: box_check
        adaptive_size: True
        pos_hint: {'center_y': .5}
        padding: "8dp", 0, 0, 0

    MDBoxLayout:
        adaptive_width: True
        padding: dp(10)

        Label:
            id: label
            text: root.text
            size_hint_x: None
            width: self.texture_size[0]
            color: root.text_color if root.text_color else (root.theme_cls.text_color)
            markup: True

    MDIcon:
        id: icon
        icon: root.icon
        size_hint: None, None
        size: "26dp", "26dp"
        font_size: "20sp"
        theme_text_color: "Custom"
        text_color: root.icon_color if root.icon_color else (root.theme_cls.text_color)
"""
)


class MDChip(ThemableBehavior, ButtonBehavior, BoxLayout):
    text = StringProperty()
    """
    Chip text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty("checkbox-blank-circle")
    """
    Chip icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    color = ColorProperty(None)
    """
    Chip color in ``rgba`` format.

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Chip's text color in ``rgba`` format.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color = ColorProperty(None)
    """
    Chip's icon color in ``rgba`` format.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    check = BooleanProperty(False)
    """
    If True, a checkmark is added to the left when touch to the chip.

    :attr:`check` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    radius = ListProperty(
        [
            dp(12),
        ]
    )
    """
    Corner radius values.

    :attr:`radius` is an :class:`~kivy.properties.ListProperty`
    and defaults to `'[dp(12),]'`.
    """

    selected_chip_color = ColorProperty(None)
    """
    The color of the chip that is currently selected in ``rgba`` format.

    :attr:`selected_chip_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _color = ColorProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_color)

    def set_color(self, interval):
        if not self.color:
            self.color = self.theme_cls.primary_color
        else:
            self._color = self.color

    def on_icon(self, instance, value):
        def remove_icon(interval):
            self.remove_widget(self.ids.icon)

        if value == "":
            self.icon = "checkbox-blank-circle"
            Clock.schedule_once(remove_icon)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dispatch("on_press")
            self.dispatch("on_release")
            md_choose_chip = self.parent

            if self.selected_chip_color:
                Animation(
                    color=self.theme_cls.primary_dark
                    if not self.selected_chip_color
                    else self.selected_chip_color,
                    d=0.3,
                ).start(self)

            if issubclass(md_choose_chip.__class__, MDChooseChip):
                for chip in md_choose_chip.children:
                    if chip is not self:
                        chip.color = (
                            self.theme_cls.primary_color
                            if not chip._color
                            else chip._color
                        )
                    else:
                        chip.color = self.theme_cls.primary_color

            if self.check:
                if not len(self.ids.box_check.children):
                    self.ids.box_check.add_widget(
                        MDIcon(
                            icon="check",
                            size_hint=(None, None),
                            size=("26dp", "26dp"),
                            font_size=sp(20),
                        )
                    )
                else:
                    check = self.ids.box_check.children[0]
                    self.ids.box_check.remove_widget(check)


class MDChooseChip(MDStackLayout):
    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDChip):
            return super().add_widget(widget)
