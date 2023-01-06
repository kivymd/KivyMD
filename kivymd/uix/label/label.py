"""
Components/Label
================

.. rubric:: The :class:`MDLabel` widget is for rendering text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label.png
    :align: center

- MDLabel_
- MDIcon_

.. MDLabel:
MDLabel
-------

Class :class:`MDLabel` inherited from the :class:`~kivy.uix.label.Label` class
but for :class:`MDLabel` the ``text_size`` parameter is ``(self.width, None)``
and default is positioned on the left:

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    text: "MDLabel"
            '''


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Test().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.label import MDLabel


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                text="MDLabel"
                            )
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-left.png
    :align: center

.. Note:: See :attr:`~kivy.uix.label.Label.halign`
    and :attr:`~kivy.uix.label.Label.valign` attributes
    of the :class:`~kivy.uix.label.Label` class

.. code-block:: kv

        MDLabel:
            text: "MDLabel"
            halign: "center"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-center.png
    :align: center

:class:`~MDLabel` color:
------------------------

:class:`~MDLabel` provides standard color themes for label color management:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
    '''


    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(KV)

            # Names of standard color themes.
            for name_theme in [
                "Primary",
                "Secondary",
                "Hint",
                "Error",
                "ContrastParentBackground",
            ]:
                screen.add_widget(
                    MDLabel(
                        text=name_theme,
                        halign="center",
                        theme_text_color=name_theme,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-theme-text-color.png
    :align: center

To use a custom color for :class:`~MDLabel`, use a theme `'Custom'`.
After that, you can specify the desired color in the ``rgba`` format
in the ``text_color`` parameter:

.. code-block:: kv

    MDLabel:
        text: "Custom color"
        halign: "center"
        theme_text_color: "Custom"
        text_color: "blue"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-custom-color.png
    :align: center

:class:`~MDLabel` provides standard font styles for labels. To do this,
specify the name of the desired style in the :attr:`~MDLabel.font_style`
parameter:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.font_definitions import theme_font_styles

    KV = '''
    MDScrollView:

        MDList:
            id: box
            spacing: "8dp"
    '''


    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(KV)

            # Names of standard font styles.
            for name_style in theme_font_styles[:-1]:
                screen.ids.box.add_widget(
                    MDLabel(
                        text=f"{name_style} style",
                        halign="center",
                        font_style=name_style,
                        adaptive_height=True,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style.png
    :align: center

Highlighting and copying labels
===============================

You can highlight labels by double tap on the label:
----------------------------------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    text: "MDLabel"
                    allow_selection: True
                    padding: "4dp", "4dp"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                adaptive_size=True,
                                pos_hint={"center_x": .5, "center_y": .5},
                                text="MDLabel",
                                allow_selection=True,
                                padding=("4dp", "4dp"),
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-allow-selection.gif
    :align: center

You can copy the label text by double clicking on it:
-----------------------------------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    text: "MDLabel"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    on_copy: print("The text is copied to the clipboard")
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                id="label",
                                adaptive_size=True,
                                pos_hint={"center_x": .5, "center_y": .5},
                                text="MDLabel",
                                allow_selection=True,
                                allow_copy=True,
                                padding=("4dp", "4dp"),
                            )
                        )
                    )

                def on_start(self):
                    self.root.ids.label.bind(on_copy=self.on_copy)

                def on_copy(self, instance_label: MDLabel):
                    print("The text is copied to the clipboard")


            Example().run()

Example of copying/cutting labels using the context menu
--------------------------------------------------------

.. code-block:: python

    from kivy.core.clipboard import Clipboard
    from kivy.lang.builder import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.toast import toast

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
        spacing: "12dp"
        padding: "24dp"

        MDScrollView:

            MDBoxLayout:
                id: box
                orientation: "vertical"
                padding: "24dp"
                spacing: "12dp"
                adaptive_height: True

        MDTextField:
            max_height: "200dp"
            mode: "fill"
            multiline: True

        MDWidget:
    '''

    data = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed blandit libero volutpat sed cras ornare arcu. Nisl vel pretium "
        "lectus quam id leo in. Tincidunt arcu non sodales neque sodales ut etiam.",
        "Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. "
        "Nisl rhoncus mattis rhoncus urna neque. Orci nulla pellentesque "
        "dignissim enim. Ac auctor augue mauris augue neque gravida in fermentum. "
        "Lacus suspendisse faucibus interdum posuere."

    ]


    class CopyLabel(MDLabel):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.allow_selection = True
            self.adaptive_height = True
            self.theme_text_color = "Custom"
            self.text_color = self.theme_cls.text_color


    class Example(MDApp):
        context_menu = None

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def on_start(self):
            for text in data:
                copy_label = CopyLabel(text=text)
                copy_label.bind(
                    on_selection=self.open_context_menu,
                    on_cancel_selection=self.restore_text_color,
                )
                self.root.ids.box.add_widget(copy_label)

        def click_item_context_menu(
            self, type_click: str, instance_label: CopyLabel
        ) -> None:
            Clipboard.copy(instance_label.text)

            if type_click == "copy":
                toast("Copied")
            elif type_click == "cut":
                self.root.ids.box.remove_widget(instance_label)
                toast("Cut")
            if self.context_menu:
                self.context_menu.dismiss()

        def restore_text_color(self, instance_label: CopyLabel) -> None:
            instance_label.text_color = self.theme_cls.text_color

        def open_context_menu(self, instance_label: CopyLabel) -> None:
            instance_label.text_color = "black"
            menu_items = [
                {
                    "text": "Copy text",
                    "viewclass": "OneLineListItem",
                    "height": dp(48),
                    "on_release": lambda: self.click_item_context_menu(
                        "copy", instance_label
                    ),
                },
                {
                    "text": "Cut text",
                    "viewclass": "OneLineListItem",
                    "height": dp(48),
                    "on_release": lambda: self.click_item_context_menu(
                        "cut", instance_label
                    ),
                },
            ]
            self.context_menu = MDDropdownMenu(
                caller=instance_label, items=menu_items, width_mult=3
            )
            self.context_menu.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/copying-cutting-labels-using-context-menu.gif
    :align: center

.. MDIcon:
MDIcon
-------

You can use labels to display material design icons using the
:class:`~MDIcon` class.

.. seealso::

    `Material Design Icons <https://materialdesignicons.com/>`_

    `Material Design Icon Names <https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py>`_

The :class:`~MDIcon` class is inherited from
:class:`~MDLabel` and has the same parameters.

.. Warning:: For the :class:`~MDIcon` class, you cannot use ``text``
    and ``font_style`` options!

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon.png
    :align: center

MDIcon with badge icon
----------------------

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        badge_icon: "numeric-10"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-badge.png
    :align: center
"""

from __future__ import annotations

__all__ = ("MDLabel", "MDIcon")

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.theming_dynamic_text import get_contrast_text_color
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, TouchBehavior
from kivymd.uix.floatlayout import MDFloatLayout

__MDLabel_colors__ = {
    "Primary": "text_color",
    "Secondary": "secondary_text_color",
    "Hint": "disabled_hint_text_color",
    "Error": "error_color",
    "OP": {
        "Primary": "opposite_text_color",
        "Secondary": "opposite_secondary_text_color",
        "Hint": "opposite_disabled_hint_text_color",
    },
}

with open(
    os.path.join(uix_path, "label", "label.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDLabel(
    DeclarativeBehavior,
    ThemableBehavior,
    Label,
    MDAdaptiveWidget,
    TouchBehavior,
):
    """
    Label class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.label.Label` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivymd.uix.behaviors.TouchBehavior`
    classes documentation.

    :Events:
        `on_ref_press`
            Called when the user clicks on a word referenced with a
            ``[ref]`` tag in a text markup.
        `on_copy`
            Called when double-tapping on the label.
        `on_selection`
            Called when double-tapping on the label.
        `on_cancel_selection`
            Called when the highlighting is removed from the label text.
    """

    font_style = StringProperty("Body1")
    """
    Label font style.

    Available vanilla font_style are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`,
    `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`font_style` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Body1'`.
    """

    _capitalizing = BooleanProperty(False)

    def _get_text(self):
        if self._capitalizing:
            return self._text.upper()
        return self._text

    def _set_text(self, value):
        self._text = value

    _text = StringProperty()

    text = AliasProperty(_get_text, _set_text, bind=["_text", "_capitalizing"])
    """Text of the label."""

    theme_text_color = OptionProperty(
        "Primary",
        allownone=True,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
        ],
    )
    """
    Label color scheme name.

    Available options are: `'Primary'`, `'Secondary'`, `'Hint'`, `'Error'`,
    `'Custom'`, `'ContrastParentBackground'`.

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    text_color = ColorProperty(None)
    """
    Label text color in (r, g, b, a) or string format.

    :attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    allow_copy = BooleanProperty(False)
    """
    Allows you to copy text to the clipboard by double-clicking on the label.

    .. versionadded:: 1.2.0

    :attr:`allow_copy` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    allow_selection = BooleanProperty(False)
    """
    Allows to highlight text by double-clicking on the label.

    .. versionadded:: 1.2.0

    :attr:`allow_selection` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    color_selection = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the text selection when the
    value of the :attr:`allow_selection` attribute is True.

    .. versionadded:: 1.2.0

    :attr:`color_selection` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    color_deselection = ColorProperty(None)
    """
    The color in (r, g, b, a) or string format of the text deselection when the
    value of the :attr:`allow_selection` attribute is True.

    .. versionadded:: 1.2.0

    :attr:`color_deselection` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    is_selected = BooleanProperty(False)
    """
    Is the label text highlighted.

    .. versionadded:: 1.2.0

    :attr:`is_selected` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _text_color_str = StringProperty()

    parent_background = ColorProperty(None)
    can_capitalize = BooleanProperty(True)
    canvas_bg = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(
            font_style=self.update_font_style,
            can_capitalize=self.update_font_style,
        )
        self.theme_cls.bind(theme_style=self._do_update_theme_color)
        self.register_event_type("on_copy")
        self.register_event_type("on_selection")
        self.register_event_type("on_cancel_selection")
        self.on_theme_text_color(None, self.theme_text_color)
        self.update_font_style(None, "")
        self.on_opposite_colors(None, self.opposite_colors)
        Clock.schedule_once(self.check_font_styles)

    def check_font_styles(self, interval: Union[int, float] = 0) -> bool:
        if self.font_style not in list(self.theme_cls.font_styles.keys()):
            raise ValueError(
                f"MDLabel.font_style is set to an invalid option '{self.font_style}'."
                f"Must be one of: {list(self.theme_cls.font_styles)}"
            )
        else:
            return True

    def update_font_style(self, instance_label, font_style: str) -> None:
        if self.check_font_styles() is True:
            font_info = self.theme_cls.font_styles[self.font_style]
            self.font_name = font_info[0]
            if self.font_style in list(self.theme_cls.font_styles.keys())[0:14]:
                self.font_size = sp(font_info[1])

            if font_info[2] and self.can_capitalize:
                self._capitalizing = True
            else:
                self._capitalizing = False

        # TODO: Add letter spacing change
        # self.letter_spacing = font_info[3]

    def do_selection(self) -> None:
        if not self.is_selected:
            self.md_bg_color = (
                self.theme_cls.primary_light
                if not self.color_selection
                else self.color_selection
            )

    def cancel_selection(self) -> None:
        if self.is_selected:
            self.md_bg_color = (
                self.theme_cls.bg_normal
                if not self.color_deselection
                else self.color_deselection
            )
            self.dispatch("on_cancel_selection")
            self.is_selected = False

    def on_double_tap(self, touch, *args) -> None:
        if self.allow_copy and self.collide_point(*touch.pos):
            Clipboard.copy(self.text)
            self.dispatch("on_copy")
        if self.allow_selection and self.collide_point(*touch.pos):
            self.do_selection()
            self.dispatch("on_selection")
            self.is_selected = True

    def on_window_touch(self, *args):
        if self.is_selected:
            self.cancel_selection()

    def on_copy(self, *args) -> None:
        """
        Called when double-tapping on the label.

        .. versionadded:: 1.2.0
        """

    def on_selection(self, *args) -> None:
        """
        Called when double-tapping on the label.

        .. versionadded:: 1.2.0
        """

    def on_cancel_selection(self, *args) -> None:
        """
        Called when the highlighting is removed from the label text.

        .. versionadded:: 1.2.0
        """

    def on_allow_selection(self, instance_label, selection: bool) -> None:
        if selection:
            Window.bind(on_touch_down=self.on_window_touch)
        else:
            Window.unbind(on_touch_down=self.on_window_touch)

    def on_theme_text_color(
        self, instance_label, theme_text_color: str
    ) -> None:
        op = self.opposite_colors
        if op:
            self._text_color_str = __MDLabel_colors__.get("OP", "").get(
                theme_text_color, ""
            )
        else:
            self._text_color_str = __MDLabel_colors__.get(theme_text_color, "")
        if self._text_color_str:
            self._do_update_theme_color()
        else:
            # 'Custom' and 'ContrastParentBackground' lead here, as well as the
            # generic None value it's not yet been set
            self._text_color_str = ""
            if theme_text_color == "Custom" and self.text_color:
                color = self.text_color
            elif (
                theme_text_color == "ContrastParentBackground"
                and self.parent_background
            ):
                color = get_contrast_text_color(self.parent_background)
            else:
                color = [0, 0, 0, 1]

            if self.theme_cls.theme_style_switch_animation:
                Animation(
                    color=color,
                    d=self.theme_cls.theme_style_switch_animation_duration,
                    t="linear",
                ).start(self)
            else:
                self.color = color

    def on_text_color(self, instance_label, color: Union[list, str]) -> None:
        if self.theme_text_color == "Custom":
            if self.theme_cls.theme_style_switch_animation:
                Animation(
                    color=self.text_color,
                    d=self.theme_cls.theme_style_switch_animation_duration,
                    t="linear",
                ).start(self)
            else:
                self.color = self.text_color

    def on_opposite_colors(self, *args) -> None:
        self.on_theme_text_color(self, self.theme_text_color)

    def on_md_bg_color(self, instance_label, color: Union[list, str]) -> None:
        self.canvas.remove_group("Background_instruction")
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=color)
            self.canvas_bg = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_canvas_bg_pos)

    def on_size(self, instance_label, size: list) -> None:
        if self.canvas_bg:
            self.canvas_bg.size = size

    def update_canvas_bg_pos(self, instance_label, pos: list) -> None:
        if self.canvas_bg:
            self.canvas_bg.pos = pos

    def _do_update_theme_color(self, *args):
        if self._text_color_str:
            if not self.disabled:
                color = getattr(self.theme_cls, self._text_color_str)
            else:
                color = getattr(self.theme_cls, "disabled_hint_text_color")

            if self.theme_cls.theme_style_switch_animation:
                Animation(
                    color=color,
                    d=self.theme_cls.theme_style_switch_animation_duration,
                    t="linear",
                ).start(self)
            else:
                self.color = color


class MDIcon(MDFloatLayout, MDLabel):
    """
    Icon class.

    For more information, see in the :class:`~MDLabel` and
    :class:`~kivymd.uix.floatlayout.MDFloatLayout` classes documentation.
    """

    icon = StringProperty("android")
    """
    Label icon name.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    badge_icon = StringProperty()
    """
    Label badge icon name.

    .. versionadded:: 1.0.0

    :attr:`badge_icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    badge_icon_color = ColorProperty([1, 1, 1, 1])
    """
    Badge icon color in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    :attr:`badge_icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_bg_color = ColorProperty(None)
    """
    Badge icon background color in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    :attr:`badge_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    badge_font_size = NumericProperty()
    """
    Badge font size.

    .. versionadded:: 1.0.0

    :attr:`badge_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    source = StringProperty(None, allownone=True)
    """
    Path to icon.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    _size = ListProperty((0, 0))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.adjust_size)

    def adjust_size(self, *args) -> None:
        from kivymd.uix.selectioncontrol import MDCheckbox

        if not isinstance(self, MDCheckbox):
            self.size_hint = (None, None)
            self._size = self.texture_size[1], self.texture_size[1]
            self.adaptive_size = True
