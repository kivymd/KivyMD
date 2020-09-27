"""
Components/Label
=================

.. rubric:: The :class:`MDLabel` widget is for rendering text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label.png
    :align: center

- MDLabel_
- MDIcon_

.. MDLabel:

MDLabel
--------

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
-------------------------

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

    `Material Design Icons <https://materialdesignicons.com/>`

    `Material Design Icon Names <https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py>`

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
from pathlib import Path

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import InstructionGroup
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.label import Label

from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.theming_dynamic_text import get_contrast_text_color

# ------------------------------------------------------------------------------
# MDLabel
# ------------------------------------------------------------------------------
Builder.load_string(
    """
#:import md_icons kivymd.icon_definitions.md_icons

<MDLabel>
    disabled_color: self.theme_cls.disabled_hint_text_color
    text_size: self.width, None

""",
    filename="MDLabel.kv",
)


class MDLabel(ThemableBehavior, Label):
    font_style = StringProperty("Body1")
    """
    Label font style.

    Available deffault font_style are:
    `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`, `'H6'`,
    `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
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

    text_color = ListProperty(None, allownone=True)
    """Label text color in ``rgba`` format.

    :attr:`text_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `None`.

    """

    parent_background = ListProperty(None, allownone=True)

    _currently_bound_property = {}

    can_capitalize = BooleanProperty(True)

    static_size = BooleanProperty(None)
    """
    allows the widget to apply it's boundingbox to resize and
    not only it's texture size.

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(
            font_style=self.update_font_style,
            can_capitalize=self.update_font_style,
        )
        self.on_theme_text_color(None, self.theme_text_color)
        self.update_font_style()
        self.on_opposite_colors(None, self.opposite_colors)
        Clock.schedule_once(self.__after_init__, -1)

    def __after_init__(self, *dt):
        """
        This funciton's purpose is to add the ability to call new funcitons that
        rely in the configuraion betweem KVLang and python code instances to all
        subclassess of MDLabel.

        """
        if self.static_size is None:
            # This will make execute all resizing rules
            self.static_size = False
        self.check_font_styles()
        pass

    def check_font_styles(self, *dt):
        if self.font_style not in list(self.theme_cls.font_styles.keys()):
            raise ValueError(
                f"MDLabel.font_style is set to an invalid option '{self.font_style}'."
                f"Must be one of: {list(self.theme_cls.font_styles)}"
            )
        else:
            return True

    def update_font_style(self, *args):
        if self.check_font_styles() is True:
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


# ------------------------------------------------------------------------------
# MDIcon
# ------------------------------------------------------------------------------
Builder.load_string(
    """
<MDIcon>:
    valign:"middle"
    halign:"center"
    font_style: "Icon"
    text: u"{}".format(md_icons[self.icon]) if self.icon in md_icons else ""
    source: None if self.icon in md_icons else self.icon
    size_hint:(None,None)
    on_font_size:
        root.force_size()
    on_icon:
        root.force_size()
    on_text:
        root.force_size()
    canvas.before:
        PushMatrix
        Rotate:
            axis: 0,0,1
            angle: root.rotation
            origin: self.center
    canvas.after:
        PopMatrix

""",
    filename="MDIcon.kv",
)


class MDIcon(MDLabel):
    """
    MDIcon is a subclass of MDLabel. with the difference that this class only
    accepts one character as input.

    You can either use the `text` property to setup an icon from a custom font or
    you could use the property `icon` to set a listed icon in
    `kivymd.icon_definitions.md_icons`.

    Take in count that if you set the `icon` property while having something
    in `text`, the `text` property will be overrode by the `icon` property

    .. note:: size_hint!
        Note that the MDIcon has a deffault size_hint of `(None,None)` and
        the size will always be `[font_size, font_size]` This allows a better
        representation on screen.

    """

    icon = StringProperty(None)
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

    _has_texture = BooleanProperty()

    ev = ObjectProperty(None, allownone=True)

    rotation = NumericProperty(0)
    __Icon_instruction = ObjectProperty()
    __current_rotation = 0
    _icon_cl_bg = ObjectProperty(None, allownone=True)
    _icon_bg = ObjectProperty(None, allownone=True)
    anim_in = ObjectProperty(None, allownone=True)
    anim_out = ObjectProperty(None, allownone=True)
    next_icon = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        self.__Icon_instruction = InstructionGroup()
        self.current_font_size = 0
        super().__init__(**kwargs)

    def __after_init__(self, *dt):
        if self.static_size is None:
            self.static_size = False
        super().__after_init__(*dt)
        self.canvas.before.add(self.__Icon_instruction)
        if self.icon is None:
            self.icon = "help"
            self._has_texture = False
        else:
            x = Path(self.icon).resolve()
            if x.exists and x.is_file():
                self._has_texture = True
            else:
                self._has_texture = False
        self.force_size()

    def on_text(self, instance, value):
        if 0 > len(value) > 1:
            # It only accepts a character in case it's an outside font
            self.text = value[0]
            self._has_texture = False

    def on_icon(self, instance, value):
        value = Path(self.icon).resolve()
        self.text = ""
        self._has_texture = False
        #
        if self.icon in md_icons:
            self.source = None
        elif value.exists() and value.is_file():
            self.source = self.icon
            self._has_texture = True
            self.on_source(self, self.source)
        else:
            self.icon = "help"
            self.source = None

    def on_source(self, instance, value):
        if value:
            _value = Path(self.icon)
            if _value.exists() and _value.is_file():
                # Setup color.
                if self._icon_cl_bg is None:
                    self._icon_cl_bg = Color([1] * 4)
                # Setup texture.
                if self._icon_bg is None:
                    self._icon_bg = Rectangle(
                        pos=self.pos,
                        size=self.size,
                        source=value,
                    )
                    self.bind(
                        pos=lambda x, y: setattr(self._icon_bg, "pos", y)
                        if self._icon_bg
                        else "",
                    )
                    self.bind(
                        size=lambda x, y: setattr(self._icon_bg, "size", y)
                        if self._icon_bg
                        else "",
                    )
                self._icon_bg.source = value
                self.__Icon_instruction.clear()
                self.__Icon_instruction.add(self._icon_cl_bg)
                self.__Icon_instruction.add(self._icon_bg)
            else:
                raise ValueError(
                    "Invalid File Extension.\n"
                    f"The file '{value}' is not a valid image!"
                )

            #
        else:
            # Clean instructions
            if self._icon_cl_bg is not None:
                self.__Icon_instruction.remove(self._icon_cl_bg)
                # self._icon_cl_bg = None
            #
            if self._icon_bg is not None:
                # unbind resize and position events
                self.unbind(
                    pos=lambda x, y: setattr(self._icon_bg, "pos", y),
                )
                self.unbind(
                    size=lambda x, y: setattr(self._icon_bg, "size", y),
                )
                self.__Icon_instruction.remove(self._icon_bg)
                # self._icon_bg = None

    def animate_rotation(self, degree, *dt, t=0.125, reverse=False):
        """
        Animate_rotation allows the developer to reproduce a simple rotation
        animation over the widget canvas

        #. the icon rotation is in degrees. rotated from the middle of the canvas.

        #. The deffault duration time is 0.125 s

        #. t is "in_quad" by deffect (for performance this setting is static)

        seet Animation for more details about arguments
        you can override this function to allow a more complex animaiton.
        """
        self.ev = Animation(
            rotation=degree,
            duration=t,
            t="in_quad",
        )
        self.ev.start(self)

    def force_size(self, *dt):
        if self.static_size is False:
            self.size = [self.font_size, self.font_size]
        else:
            pass

    def on_disabled(self, instance, value):
        # super().on_disabled(instance, value)
        if self._has_texture and self._icon_cl_bg:
            self._icon_cl_bg.rgba = [1] * 4 if value is False else [0.7] * 4

    def change_icon(self, *dt):
        if self.next_icon:
            self.icon = self.next_icon
            self.next_icon = None
        self.anim_in.start(self)

    def EOA(self, *dt, callback=None):
        """End Of Animation"""
        self.static_size = False
        if callback:
            callback()

    def zoom_in_animation(self, next_icon=None, callback=None):
        if next_icon is not None:
            self.next_icon = next_icon
        self.current_font_size = self.font_size
        self.anim_in = Animation(
            font_size=self.current_font_size,
            duration=0.1,
        )
        if self.anim_out is None:
            self.anim_out = Animation(
                font_size=0,
                duration=0.1,
            )
        self.anim_out.bind(on_complete=self.change_icon)
        self.anim_in.bind(on_complete=lambda *x: self.EOA(callback=callback))
        self.static_size = True
        self.anim_in.cancel(self)
        self.anim_out.start(self)
