"""
Components/Label
================

.. rubric:: The `MDLabel` widget is for rendering text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label.png
    :align: center

- MDLabel_
- MDIcon_

.. MDLabel:

MDLabel
-------

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDLabel:
                    text: "MDLabel"
                    halign: "center"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.label import MDLabel


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDLabel(
                                text="MDLabel",
                                halign="center",
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-example.png
    :align: center

To use a custom color for :class:`~MDLabel`, use a theme `'Custom'`.
After that, you can specify the desired color in the ``text_color`` parameter:

.. code-block:: kv

    MDLabel:
        text: "Custom color"
        halign: "center"
        theme_text_color: "Custom"
        text_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-custom-color.png
    :align: center

:class:`~MDLabel` provides standard font styles for labels. To do this,
specify the name of the desired style in the :attr:`~MDLabel.font_style`
and :attr:`~MDLabel.role` parameters:

.. code-block:: kv

    MDLabel:
        text: "Display, role - 'large'"
        font_style: "Display"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style-display-large.png
    :align: center

.. code-block:: kv

    MDLabel:
        text: "Display, role - 'small'"
        font_style: "Display"
        role: "small"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style-display-small.png
    :align: center

.. seealso::

    `Material Design spec, Typography <https://m3.material.io/styles/typography/type-scale-tokens>`_


All styles
----------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.font_definitions import theme_font_styles
    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDRecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                spacing: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def on_start(self):
            for style in theme_font_styles:
                if style != "Icon":
                    for role in theme_font_styles[style]:
                        font_size = int(theme_font_styles[style][role]["font-size"])
                        self.root.ids.rv.data.append(
                            {
                                "viewclass": "MDLabel",
                                "text": f"{style} {role} {font_size} sp",
                                "adaptive_height": "True",
                                "font_style": style,
                                "role": role,
                            }
                        )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-font-style-preview.png
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
                md_bg_color: self.theme_cls.backgroundColor

                MDLabel:
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    text: "Do a double click on me"
                    allow_selection: True
                    padding: "4dp", "4dp"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def on_start(self):
                    def on_start(dt):
                        self.root.md_bg_color = self.theme_cls.backgroundColor

                    Clock.schedule_once(on_start)

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDLabel(
                                adaptive_size=True,
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                text="Do a double click on me",
                                allow_selection=True,
                                padding=("4dp", "4dp"),
                            ),
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

    from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.menu import MDDropdownMenu

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
        spacing: "12dp"
        padding: "24dp"
        md_bg_color: self.theme_cls.backgroundColor

        MDBoxLayout:
            id: box
            orientation: "vertical"
            padding: "24dp"
            spacing: "12dp"
            adaptive_height: True

        MDTextField:
            max_height: "200dp"
            mode: "filled"
            multiline: True

        Widget:
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


    def toast(text):
        MDSnackbar(
            MDSnackbarText(
                text=text,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.3,
        ).open()


    class CopyLabel(MDLabel):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.allow_selection = True
            self.adaptive_height = True


    class Example(MDApp):
        context_menu = None

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for text in data:
                copy_label = CopyLabel(text=text)
                copy_label.bind(on_selection=self.open_context_menu)
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

        def open_context_menu(self, instance_label: CopyLabel) -> None:
            instance_label.text_color = "black"
            menu_items = [
                {
                    "text": "Copy text",
                    "on_release": lambda: self.click_item_context_menu(
                        "copy", instance_label
                    ),
                },
                {
                    "text": "Cut text",
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

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon.png
    :align: center

MDIcon with badge icon
----------------------

.. code-block:: kv

    MDIcon:
        icon: "gmail"

        MDBadge:
            text: "10+"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-badge.png
    :align: center

MDIcon with a custom font icon
------------------------------

You can use custom fonts to display icons. Such as for example
`Material Symbols <https://fonts.google.com/icons?icon=>`_. You can find the
necessary fonts in the
`materialsymbols-python <https://github.com/T-Dynamos/materialsymbols-python>`_
repository

.. code-block:: python

    from kivy.core.text import LabelBase
    from kivy.lang import Builder
    from kivy.metrics import sp

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDIcon:
            icon: "music_video"
            theme_font_name: "Custom"
            font_name: "MaterialSymbols"
            pos_hint: {"center_x": .5, "center_y": .58}

        MDButton:
            pos_hint: {"center_x": .5, "center_y": .47}

            MDButtonIcon:
                icon: "music_video"
                theme_font_name: "Custom"
                font_name: "MaterialSymbols"

            MDButtonText:
                text: "Elevated"
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"

            LabelBase.register(
                name="MaterialSymbols",
                fn_regular="Material_Symbols_Outlined-20-200-1_200.ttf",
            )

            self.theme_cls.font_styles["MaterialSymbols"] = {
                "large": {
                    "line-height": 1.64,
                    "font-name": "MaterialSymbols",
                    "font-size": sp(57),
                },
                "medium": {
                    "line-height": 1.52,
                    "font-name": "MaterialSymbols",
                    "font-size": sp(45),
                },
                "small": {
                    "line-height": 1.44,
                    "font-name": "MaterialSymbols",
                    "font-size": sp(36),
                },
            }

            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-castom-font.png
    :align: center
"""

from __future__ import annotations

__all__ = ("MDLabel", "MDIcon")

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.graphics import Color, SmoothRoundedRectangle
from kivy.lang import Builder

from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
    OptionProperty,
)
from kivy.uix.label import Label

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import (
    DeclarativeBehavior,
    TouchBehavior,
    BackgroundColorBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior


with open(
    os.path.join(uix_path, "label", "label.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDLabel(
    DeclarativeBehavior,
    ThemableBehavior,
    BackgroundColorBehavior,
    Label,
    MDAdaptiveWidget,
    TouchBehavior,
    StateLayerBehavior,
):
    """
    Label class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.label.Label` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivymd.uix.behaviors.touch_behavior.TouchBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior`
    classes documentation.

    :Events:
        `on_ref_press`
            Fired when the user clicks on a word referenced with a
            ``[ref]`` tag in a text markup.
        `on_copy`
            Fired when double-tapping on the label.
        `on_selection`
            Fired when double-tapping on the label.
        `on_cancel_selection`
            Fired when the highlighting is removed from the label text.
    """

    font_style = StringProperty("Body")
    """
    Label font style.

    .. versionchanged:: 2.0.0

    Available vanilla font_style are: `'Display'`, `'Headline'`, `'Title'`,
    `'Label'`, `'Body'``.

    :attr:`font_style` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Body'`.
    """

    role = OptionProperty("large", options=["large", "medium", "small"])
    """
    Role of font style.

    .. versionadded:: 2.0.0

    Available options are: `'large'`, `'medium'`, `'small'`.

    :attr:`role` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'large'`.
    """

    text = StringProperty()
    """
    Text of the label.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
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

    radius = VariableListProperty([0], length=4)
    """
    Label radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    _canvas_bg = ObjectProperty(allownone=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_copy")
        self.register_event_type("on_selection")
        self.register_event_type("on_cancel_selection")

    def do_selection(self) -> None:
        if not self.is_selected:
            self.md_bg_color = (
                self.theme_cls.secondaryContainerColor
                if not self.color_selection
                else self.color_selection
            )

    def cancel_selection(self) -> None:
        if self.is_selected:
            self.canvas.before.remove_group("md-label-selection-color")
            self.canvas.before.remove_group(
                "md-label-selection-color-rectangle"
            )
            self.md_bg_color = (
                self.parent.md_bg_color
                if not self.color_deselection
                else self.color_deselection
            )
            self.dispatch("on_cancel_selection")
            self.is_selected = False
            self._canvas_bg = None

    def on_double_tap(self, touch, *args) -> None:
        """Fired by double-clicking on the widget."""

        if self.allow_copy and self.collide_point(*touch.pos):
            Clipboard.copy(self.text)
            self.dispatch("on_copy")
        if self.allow_selection and self.collide_point(*touch.pos):
            self.do_selection()
            self.dispatch("on_selection")
            self.is_selected = True

    def on_window_touch(self, *args) -> None:
        """Fired at the on_touch_down event."""

        if self.is_selected:
            self.cancel_selection()

    def on_copy(self, *args) -> None:
        """
        Fired when double-tapping on the label.

        .. versionadded:: 1.2.0
        """

    def on_selection(self, *args) -> None:
        """
        Fired when double-tapping on the label.

        .. versionadded:: 1.2.0
        """

    def on_cancel_selection(self, *args) -> None:
        """
        Fired when the highlighting is removed from the label text.

        .. versionadded:: 1.2.0
        """

    def on_allow_selection(self, instance_label, selection: bool) -> None:
        """Fired when the :attr:`allow_selection` value changes."""

        if selection:
            Window.bind(on_touch_down=self.on_window_touch)
        else:
            Window.unbind(on_touch_down=self.on_window_touch)

    def on_text_color(self, instance_label, color: list | str) -> None:
        """Fired when the :attr:`text_color` value changes."""

        if self.theme_text_color == "Custom":
            if self.theme_cls.theme_style_switch_animation:
                Animation(
                    color=self.text_color,
                    d=self.theme_cls.theme_style_switch_animation_duration,
                    t="linear",
                ).start(self)
            else:
                self.color = self.text_color

    def on_md_bg_color(self, instance_label, color: list | str) -> None:
        """Fired when the :attr:`md_bg_color` value changes."""

        def on_md_bg_color(*args) -> None:
            from kivymd.uix.selectioncontrol import MDCheckbox
            from kivymd.uix.tooltip import MDTooltipPlain

            if not issubclass(
                self.__class__, (MDCheckbox, MDIcon, MDTooltipPlain)
            ):
                self.canvas.remove_group("Background_instruction")

                # FIXME: IndexError
                # try:
                #     self.canvas.before.clear()
                # except IndexError:
                #     pass

                with self.canvas.before:
                    Color(rgba=color, group="md-label-selection-color")
                    self._canvas_bg = SmoothRoundedRectangle(
                        pos=self.pos,
                        size=self.size,
                        radius=self.radius,
                        group="md-label-selection-color-rectangle",
                    )
                    self.bind(pos=self.update_canvas_bg_pos)

        Clock.schedule_once(on_md_bg_color)

    def on_size(self, instance_label, size: list) -> None:
        """Fired when the parent window of the application is resized."""

        if self._canvas_bg:
            self._canvas_bg.size = size

    def update_canvas_bg_pos(self, instance_label, pos: list) -> None:
        if self._canvas_bg:
            self._canvas_bg.pos = pos


class MDIcon(MDLabel):
    """
    Icon class.

    For more information, see in the
    :class:`~MDLabel` class documentation.
    """

    icon = StringProperty("blank")
    """
    Label icon name.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'blank'`.
    """

    source = StringProperty(None, allownone=True)
    """
    Path to icon.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """

    icon_color = ColorProperty(None)
    """
    Icon color in (r, g, b, a) or string format.

    .. versionadded:: 2.0.0

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_disabled = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the button when
    the button is disabled.

    .. versionadded:: 2.0.0

    :attr:`icon_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # kivymd.uix.badge.badge.MDBadge object.
    _badge = ObjectProperty()

    def add_widget(self, widget, index=0, canvas=None):
        from kivymd.uix.badge import MDBadge

        if isinstance(widget, MDBadge):
            self._badge = widget
            return super().add_widget(widget)
