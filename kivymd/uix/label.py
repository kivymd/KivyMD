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

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    Screen:

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                title: "MDLabel"

            MDLabel:
                text: "MDLabel"
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


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
    Screen:

        BoxLayout:
            id: box
            orientation: "vertical"

            MDToolbar:
                title: "MDLabel"
    '''


    class Test(MDApp):
        def build(self):
            screen = Builder.load_string(KV)
            # Names of standard color themes.
            for name_theme in [
                "Primary",
                "Secondary",
                "Hint",
                "Error",
                "ContrastParentBackground",
            ]:
                screen.ids.box.add_widget(
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
        text_color: 0, 0, 1, 1

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
    Screen:

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                title: "MDLabel"

            ScrollView:

                MDList:
                    id: box
    '''


    class Test(MDApp):
        def build(self):
            screen = Builder.load_string(KV)
            # Names of standard font styles.
            for name_style in theme_font_styles[:-1]:
                screen.ids.box.add_widget(
                    MDLabel(
                        text=f"{name_style} style",
                        halign="center",
                        font_style=name_style,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style.gif
    :align: center

.. MDIcon:
MDIcon
-------

You can use labels to display material design icons using the
:class:`~MDIcon` class.

.. seealso::

    `Material Design Icons <https://materialdesignicons.com/>`_

    `Material Design Icon Names <https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py>`_

The :class:`~MDIcon` class is inherited from
:class:`~MDLabel` and has the same parameters.

.. Warning:: For the :class:`~MDIcon` class, you cannot use ``text``
    and ``font_style`` options!

.. code-block:: kv

    MDIcon:
        halign: "center"
        icon: "language-python"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon.png
    :align: center
"""

__all__ = ("MDLabel", "MDIcon")

from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ListProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label

from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.theming_dynamic_text import get_contrast_text_color

Builder.load_string(
    """
#:import md_icons kivymd.icon_definitions.md_icons


<MDLabel>
    disabled_color: self.theme_cls.disabled_hint_text_color
    text_size: self.width, None


<MDIcon>:
    font_style: "Icon"
    text: u"{}".format(md_icons[self.icon]) if self.icon in md_icons else ""
    source: None if self.icon in md_icons else self.icon
    canvas:
        Color:
            rgba: (1, 1, 1, 1) if self.source else (0, 0, 0, 0)
        Rectangle:
            source: self.source if self.source else None
            pos: self.pos
            size: self.size
"""
)


class MDLabel(ThemableBehavior, Label):
    font_style = OptionProperty("Body1", options=theme_font_styles)
    """
    Label font style.

    Available options are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`, `'H6'`,
    `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    `'Caption'`, `'Overline'`, `'Icon'`.

    :attr:`font_style` is an :class:`~kivy.properties.OptionProperty`
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

    text_color = ListProperty(None, allownone=True)
    """Label text color in ``rgba`` format.

    :attr:`text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `None`.
    """

    parent_background = ListProperty(None, allownone=True)

    _currently_bound_property = {}

    can_capitalize = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            font_style=self.update_font_style,
            can_capitalize=self.update_font_style,
        )
        self.on_theme_text_color(None, self.theme_text_color)
        self.update_font_style()
        self.on_opposite_colors(None, self.opposite_colors)

    def update_font_style(self, *args):
        font_info = self.theme_cls.font_styles[self.font_style]
        self.font_name = font_info[0]
        self.font_size = sp(font_info[1])
        if font_info[2] and self.can_capitalize:
            self._capitalizing = True
        else:
            self._capitalizing = False
        # TODO: Add letter spacing change
        # self.letter_spacing = font_info[3]

    def on_theme_text_color(self, instance, value):
        t = self.theme_cls
        op = self.opposite_colors
        setter = self.setter("color")
        t.unbind(**self._currently_bound_property)
        attr_name = {
            "Primary": "text_color" if not op else "opposite_text_color",
            "Secondary": "secondary_text_color"
            if not op
            else "opposite_secondary_text_color",
            "Hint": "disabled_hint_text_color"
            if not op
            else "opposite_disabled_hint_text_color",
            "Error": "error_color",
        }.get(value, None)
        if attr_name:
            c = {attr_name: setter}
            t.bind(**c)
            self._currently_bound_property = c
            self.color = getattr(t, attr_name)
        else:
            # 'Custom' and 'ContrastParentBackground' lead here, as well as the
            # generic None value it's not yet been set
            if value == "Custom" and self.text_color:
                self.color = self.text_color
            elif value == "ContrastParentBackground" and self.parent_background:
                self.color = get_contrast_text_color(self.parent_background)
            else:
                self.color = [0, 0, 0, 1]

    def on_text_color(self, *args):
        if self.theme_text_color == "Custom":
            self.color = self.text_color

    def on_opposite_colors(self, instance, value):
        self.on_theme_text_color(self, self.theme_text_color)


class MDIcon(MDLabel):
    icon = StringProperty("android")
    """
    Label icon name.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    source = StringProperty(None, allownone=True)
    """
    Path to icon.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `None`.
    """
