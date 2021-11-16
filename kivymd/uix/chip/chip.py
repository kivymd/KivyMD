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

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDChip:
            text: "Portland"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.on_release_chip(self)
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_release_chip(self, instance_check):
            print(instance_check)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/ordinary-chip.png
    :align: center

Use with right icon
-------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_right: "close-circle-outline"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-right-icon.png
    :align: center

Use with left icon
------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "map-marker"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-left-icon.png
    :align: center

Use with custom left icon
-------------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "avatar.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-custom-left-icon.png
    :align: center

Use with left and right icon
----------------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "avatar.png"
        icon_right: "close-circle-outline"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-left-right-icon.png
    :align: center

Use with outline
----------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "avatar.png"
        icon_right: "close-circle-outline"
        line_color: app.theme_cls.disabled_hint_text_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-outline.png
    :align: center

Use with custom color
---------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "avatar.png"
        icon_right: "close-circle-outline"
        line_color: app.theme_cls.disabled_hint_text_color
        md_bg_color: 1, 0, 0, .5

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-custom-color.png
    :align: center

Use with elevation
------------------

.. code-block:: kv

    MDChip:
        text: "Portland"
        icon_left: "avatar.png"
        icon_right: "close-circle-outline"
        line_color: app.theme_cls.disabled_hint_text_color
        md_bg_color: 1, 0, 0, .5
        elevation: 12

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-with-elevation.png
    :align: center

Behavior
========

Long press on the chip, it will be marked.
When you click on the marked chip, the mark will be removed:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-activate.gif
    :align: center

Examples
========

Multiple choose
---------------

Selecting a single choice chip automatically deselects all other chips in the set.

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder

    from kivymd.uix.screen import MDScreen
    from kivymd.uix.chip import MDChip
    from kivymd.app import MDApp

    KV = '''
    <MyScreen>

        MDBoxLayout:
            orientation: "vertical"
            adaptive_size: True
            spacing: "12dp"
            padding: "56dp"
            pos_hint: {"center_x": .5, "center_y": .5}

            MDLabel:
                text: "Multiple choice"
                bold: True
                font_style: "H5"
                adaptive_size: True

            MDBoxLayout:
                id: chip_box
                adaptive_size: True
                spacing: "8dp"

                MyChip:
                    text: "Elevator"
                    on_press: if self.active: root.removes_marks_all_chips()

                MyChip:
                    text: "Washer / Dryer"
                    on_press: if self.active: root.removes_marks_all_chips()

                MyChip:
                    text: "Fireplace"
                    on_press: if self.active: root.removes_marks_all_chips()


    ScreenManager:

        MyScreen:
    '''


    class MyChip(MDChip):
        icon_check_color = (0, 0, 0, 1)
        text_color = (0, 0, 0, 0.5)
        _no_ripple_effect = True

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.bind(active=self.set_chip_bg_color)
            self.bind(active=self.set_chip_text_color)

        def set_chip_bg_color(self, instance_chip, active_value: int):
            '''
            Will be called every time the chip is activated/deactivated.
            Sets the background color of the chip.
            '''

            self.md_bg_color = (
                (0, 0, 0, 0.4)
                if active_value
                else (
                    self.theme_cls.bg_darkest
                    if self.theme_cls.theme_style == "Light"
                    else (
                        self.theme_cls.bg_light
                        if not self.disabled
                        else self.theme_cls.disabled_hint_text_color
                    )
                )
            )

        def set_chip_text_color(self, instance_chip, active_value: int):
            Animation(
                color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2
            ).start(self.ids.label)


    class MyScreen(MDScreen):
        def removes_marks_all_chips(self):
            for instance_chip in self.ids.chip_box.children:
                if instance_chip.active:
                    instance_chip.active = False


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-multiple-choose.gif
    :align: center

Only choose
-----------

Only one chip will be selected.

.. code-block:: python

    KV = '''
    <MyScreen>

        [...]

            MDBoxLayout:
                id: chip_box
                adaptive_size: True
                spacing: "8dp"

                MyChip:
                    text: "Elevator"
                    on_active: if self.active: root.removes_marks_all_chips(self)

                MyChip:
                    text: "Washer / Dryer"
                    on_active: if self.active: root.removes_marks_all_chips(self)

                MyChip:
                    text: "Fireplace"
                    on_active: if self.active: root.removes_marks_all_chips(self)


    [...]
    '''


    class MyScreen(MDScreen):
        def removes_marks_all_chips(self, selected_instance_chip):
            for instance_chip in self.ids.chip_box.children:
                if instance_chip != selected_instance_chip:
                    instance_chip.active = False

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-only-choose.gif
    :align: center
"""

__all__ = ("MDChip",)

import os
from typing import NoReturn

from kivy import Logger
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ColorProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    FakeRectangularElevationBehavior,
    RectangularRippleBehavior,
    TouchBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.templates import ScaleWidget

with open(
    os.path.join(uix_path, "chip", "chip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDChip(
    ThemableBehavior,
    RectangularRippleBehavior,
    FakeRectangularElevationBehavior,
    TouchBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    text = StringProperty()
    """
    Chip text.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty("checkbox-blank-circle", deprecated=True)
    """
    Chip icon.

    .. deprecated:: 1.0.0
        Use :attr:`icon_right` and :attr:`icon_left` instead.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'checkbox-blank-circle'`.
    """

    icon_left = StringProperty()
    """
    Chip left icon.

    .. versionadded:: 1.0.0

    :attr:`icon_left` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_right = StringProperty()
    """
    Chip right icon.

    .. versionadded:: 1.0.0

    :attr:`icon_right` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    color = ColorProperty(None, deprecated=True)
    """
    Chip color in ``rgba`` format.

    .. deprecated:: 1.0.0

    :attr:`color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Chip's text color in ``rgba`` format.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color = ColorProperty(None, deprecated=True)
    """
    Chip's icon color in ``rgba`` format.

    .. deprecated:: 1.0.0
        Use :attr:`icon_right_color` and :attr:`icon_left_color` instead.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_right_color = ColorProperty(None)
    """
    Chip's right icon color in ``rgba`` format.

    .. versionadded:: 1.0.0

    :attr:`icon_right_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_left_color = ColorProperty(None)
    """
    Chip's left icon color in ``rgba`` format.

    .. versionadded:: 1.0.0

    :attr:`icon_left_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_check_color = ColorProperty(None)
    """
    Chip's check icon color in ``rgba`` format.

    .. versionadded:: 1.0.0

    :attr:`icon_check_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    check = BooleanProperty(False, deprecated=True)
    """
    If `True`, a checkmark is added to the left when touch to the chip.

    .. deprecated:: 1.0.0

    :attr:`check` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    selected_chip_color = ColorProperty(None, deprecated=True)
    """
    The color of the chip that is currently selected in ``rgba`` format.

    .. deprecated:: 1.0.0

    :attr:`selected_chip_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    active = BooleanProperty(False)
    """
    Whether the check is marked or not.

    .. versionadded:: 1.0.0

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_long_touch(self, *args) -> NoReturn:
        if self.active:
            return
        self.active = True if not self.active else False

    def on_active(self, instance_check, active_value: bool) -> NoReturn:
        if active_value:
            self.do_animation_check((0, 0, 0, 0.4), 1)
        else:
            self.do_animation_check((0, 0, 0, 0), 0)

    def do_animation_check(
        self, md_bg_color: list, scale_value: int
    ) -> NoReturn:
        Animation(md_bg_color=md_bg_color, t="out_sine", d=0.1).start(
            self.ids.icon_left_box
        )
        Animation(
            scale_value_x=scale_value,
            scale_value_y=scale_value,
            scale_value_z=scale_value,
            t="out_sine",
            d=0.1,
        ).start(self.ids.check_icon)

        if not self.icon_left:
            if scale_value:
                self.ids.check_icon.x = -dp(4)
                Animation(size=(dp(24), dp(24)), t="out_sine", d=0.1).start(
                    self.ids.relative_box
                )
            else:
                self.ids.check_icon.x = 0
                Animation(size=(0, 0), t="out_sine", d=0.1).start(
                    self.ids.relative_box
                )

    def on_press(self, *args):
        if self.active:
            self.active = False


class MDChooseChip(MDStackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            "MDChooseChip: "
            "class is deprecated and will be removed in a future version"
        )


class MDScalableCheckIcon(MDIcon, ScaleWidget):
    pos_hint = {"center_y": 0.5}


if __name__ == "__main__":
    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen

    KV = """
<MyScreen>

    MDBoxLayout:
        orientation: "vertical"
        adaptive_size: True
        spacing: "12dp"
        padding: "56dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Multiple choose"
            bold: True
            font_style: "H5"
            adaptive_size: True

        MDBoxLayout:
            id: chip_box
            adaptive_size: True
            spacing: "8dp"

            MyChip:
                text: "Elevator"
                on_press: if self.active: root.removes_marks_all_chips()

            MyChip:
                text: "Washer / Dryer"
                on_press: if self.active: root.removes_marks_all_chips()

            MyChip:
                text: "Fireplace"
                on_press: if self.active: root.removes_marks_all_chips()

        MDSeparator:

        MDLabel:
            text: "Only choose"
            bold: True
            font_style: "H5"
            adaptive_size: True

        MDBoxLayout:
            id: chip_only_box
            adaptive_size: True
            spacing: "8dp"

            MyChip:
                text: "Elevator"
                on_active: if self.active: root.removes_marks_all_chips(self, False)

            MyChip:
                text: "Washer / Dryer"
                on_active: if self.active: root.removes_marks_all_chips(self, False)

            MyChip:
                text: "Fireplace"
                on_active: if self.active: root.removes_marks_all_chips(self, False)


ScreenManager:

    MyScreen:
    """

    class MyChip(MDChip):
        icon_check_color = (0, 0, 0, 1)
        text_color = (0, 0, 0, 0.5)
        _no_ripple_effect = True

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.bind(active=self.set_chip_bg_color)
            self.bind(active=self.set_chip_text_color)

        def set_chip_bg_color(self, instance_chip, active_value: int):
            """
            Will be called every time the chip is activated/deactivated.
            Sets the background color of the chip.
            """

            self.md_bg_color = (
                (0, 0, 0, 0.4)
                if active_value
                else (
                    self.theme_cls.bg_darkest
                    if self.theme_cls.theme_style == "Light"
                    else (
                        self.theme_cls.bg_light
                        if not self.disabled
                        else self.theme_cls.disabled_hint_text_color
                    )
                )
            )

        def set_chip_text_color(self, instance_chip, active_value: int):
            Animation(
                color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2
            ).start(self.ids.label)

    class MyScreen(MDScreen):
        def removes_marks_all_chips(
            self, selected_instance_chip=None, multiple=True
        ):
            if multiple:
                for instance_chip in self.ids.chip_box.children:
                    if instance_chip.active:
                        instance_chip.active = False
            else:
                for instance_chip in self.ids.chip_only_box.children:
                    if instance_chip != selected_instance_chip:
                        instance_chip.active = False

    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

    Test().run()
