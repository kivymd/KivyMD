"""
Themes/Theming
==============

.. seealso::

   `Material Design spec, Material theming <https://material.io/design/material-theming>`_

Material App
------------

The main class of your application, which in `Kivy` inherits from the App class,
in `KivyMD` must inherit from the `MDApp` class. The `MDApp` class has
properties that allow you to control application properties
such as :attr:`color/style/font` of interface elements and much more.

Control material properties
---------------------------

The main application class inherited from the `MDApp` class has the :attr:`theme_cls`
attribute, with which you control the material properties of your application.
"""

from kivy.app import App
from kivy.atlas import Atlas
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    DictProperty,
    ListProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.utils import get_color_from_hex

from kivymd import images_path
from kivymd.color_definitions import colors, hue, palette
from kivymd.material_resources import DEVICE_IOS, DEVICE_TYPE

from kivymd.font_definitions import theme_font_styles  # NOQA: F401


class ThemeManager(EventDispatcher):
    primary_palette = OptionProperty("Blue", options=palette)
    """
    The name of the color scheme that the application will use.
    All major `material` components will have the color
    of the specified color theme.

    Available options are: `'Red'`, `'Pink'`, `'Purple'`, `'DeepPurple'`,
    `'Indigo'`, `'Blue'`, `'LightBlue'`, `'Cyan'`, `'Teal'`, `'Green'`,
    `'LightGreen'`, `'Lime'`, `'Yellow'`, `'Amber'`, `'Orange'`, `'DeepOrange'`,
    `'Brown'`, `'Gray'`, `'BlueGray'`.

    To change the color scheme of an application:

    .. code-block:: python

        from kivy.uix.screenmanager import Screen

        from kivymd.app import MDApp
        from kivymd.uix.button import MDRectangleFlatButton


        class MainApp(MDApp):
            def build(self):
                self.theme_cls.primary_palette = "Green"  # "Purple", "Red"

                screen = Screen()
                screen.add_widget(
                    MDRectangleFlatButton(
                        text="Hello, World",
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )
                return screen


        MainApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-palette.png

    :attr:`primary_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Blue'`.
    """

    primary_hue = OptionProperty("500", options=hue)
    """
    The color hue of the application.

    Available options are: `'50'`, `'100'`, `'200'`, `'300'`, `'400'`, `'500'`,
    `'600'`, `'700'`, `'800'`, `'900'`, `'A100'`, `'A200'`, `'A400'`, `'A700'`.

    To change the hue color scheme of an application:

    .. code-block:: python

        from kivy.uix.screenmanager import Screen

        from kivymd.app import MDApp
        from kivymd.uix.button import MDRectangleFlatButton


        class MainApp(MDApp):
            def build(self):
                self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
                self.theme_cls.primary_hue = "200"  # "500"

                screen = Screen()
                screen.add_widget(
                    MDRectangleFlatButton(
                        text="Hello, World",
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )
                return screen


        MainApp().run()

    With a value of ``self.theme_cls.primary_hue = "500"``:

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-palette.png

    With a value of ``self.theme_cls.primary_hue = "200"``:

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-hue.png

    :attr:`primary_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    primary_light_hue = OptionProperty("200", options=hue)
    """
    Hue value for :attr:`primary_light`.

    :attr:`primary_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'200'`.
    """

    primary_dark_hue = OptionProperty("700", options=hue)
    """
    Hue value for :attr:`primary_dark`.

    :attr:`primary_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'700'`.
    """

    def _get_primary_color(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_hue]
        )

    primary_color = AliasProperty(
        _get_primary_color, bind=("primary_palette", "primary_hue")
    )
    """
    The color of the current application theme in ``rgba`` format.

    :attr:`primary_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme, property is readonly.
    """

    def _get_primary_light(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_light_hue]
        )

    primary_light = AliasProperty(
        _get_primary_light, bind=("primary_palette", "primary_light_hue")
    )
    """
    Colors of the current application color theme in ``rgba`` format
    (in lighter color).

    .. code-block:: python

        from kivy.lang import Builder

        from kivymd.app import MDApp


        KV = '''
        Screen:

            MDRaisedButton:
                text: "primary_light"
                pos_hint: {"center_x": 0.5, "center_y": 0.7}
                md_bg_color: app.theme_cls.primary_light

            MDRaisedButton:
                text: "primary_color"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                text: "primary_dark"
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                md_bg_color: app.theme_cls.primary_dark
        '''


        class MainApp(MDApp):
            def build(self):
                self.theme_cls.primary_palette = "Green"
                return Builder.load_string(KV)


        MainApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-colors-light-dark.png
        :align: center

    :attr:`primary_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme (in lighter color),
    property is readonly.
    """

    def _get_primary_dark(self):
        return get_color_from_hex(
            colors[self.primary_palette][self.primary_dark_hue]
        )

    primary_dark = AliasProperty(
        _get_primary_dark, bind=("primary_palette", "primary_dark_hue")
    )
    """
    Colors of the current application color theme
    in ``rgba`` format (in darker color).

    :attr:`primary_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value of the current application theme (in darker color),
    property is readonly.
    """

    accent_palette = OptionProperty("Amber", options=palette)
    """
    The application color palette used for items such as the tab indicator
    in the :attr:`MDTabsBar` class and so on...

    The image below shows the color schemes with the values
    ``self.theme_cls.accent_palette = 'Blue'``, ``Red'`` and​​ ``Yellow'``:

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/accent-palette.png

    :attr:`primary_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Amber'`.
    """

    accent_hue = OptionProperty("500", options=hue)
    """Similar to :attr:`primary_hue`,
    but returns a value for :attr:`accent_palette`.

    :attr:`accent_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'500'`.
    """

    accent_light_hue = OptionProperty("200", options=hue)
    """
    Hue value for :attr:`accent_light`.

    :attr:`accent_light_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'200'`.
    """

    accent_dark_hue = OptionProperty("700", options=hue)
    """
    Hue value for :attr:`accent_dark`.

    :attr:`accent_dark_hue` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'700'`.
    """

    def _get_accent_color(self):
        return get_color_from_hex(colors[self.accent_palette][self.accent_hue])

    accent_color = AliasProperty(
        _get_accent_color, bind=["accent_palette", "accent_hue"]
    )
    """Similar to :attr:`primary_color`,
    but returns a value for :attr:`accent_color`.

    :attr:`accent_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_color`,
    property is readonly.
    """

    def _get_accent_light(self):
        return get_color_from_hex(
            colors[self.accent_palette][self.accent_light_hue]
        )

    accent_light = AliasProperty(
        _get_accent_light, bind=["accent_palette", "accent_light_hue"]
    )
    """Similar to :attr:`primary_light`,
    but returns a value for :attr:`accent_light`.

    :attr:`accent_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_light`,
    property is readonly.
    """

    def _get_accent_dark(self):
        return get_color_from_hex(
            colors[self.accent_palette][self.accent_dark_hue]
        )

    accent_dark = AliasProperty(
        _get_accent_dark, bind=["accent_palette", "accent_dark_hue"]
    )
    """Similar to :attr:`primary_dark`,
    but returns a value for :attr:`accent_dark`.

    :attr:`accent_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`accent_dark`,
    property is readonly.
    """

    theme_style = OptionProperty("Light", options=["Light", "Dark"])
    """App theme style.

    .. code-block:: python

        from kivy.uix.screenmanager import Screen

        from kivymd.app import MDApp
        from kivymd.uix.button import MDRectangleFlatButton


        class MainApp(MDApp):
            def build(self):
                self.theme_cls.theme_style = "Dark"  # "Light"

                screen = Screen()
                screen.add_widget(
                    MDRectangleFlatButton(
                        text="Hello, World",
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )
                return screen


        MainApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/theme-style.png

    :attr:`theme_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Light'`.
    """

    def _get_theme_style(self, opposite):
        if opposite:
            return "Light" if self.theme_style == "Dark" else "Dark"
        else:
            return self.theme_style

    def _get_bg_darkest(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["StatusBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["StatusBar"])

    bg_darkest = AliasProperty(_get_bg_darkest, bind=["theme_style"])
    """
    Similar to :attr:`bg_dark`,
    but the color values ​​are a tone lower (darker) than :attr:`bg_dark`.

    .. code-block:: python

        KV = '''
        <Box@BoxLayout>:
            bg: 0, 0, 0, 0

            canvas:
                Color:
                    rgba: root.bg
                Rectangle:
                    pos: self.pos
                    size: self.size

        BoxLayout:

            Box:
                bg: app.theme_cls.bg_light
            Box:
                bg: app.theme_cls.bg_normal
            Box:
                bg: app.theme_cls.bg_dark
            Box:
                bg: app.theme_cls.bg_darkest
        '''

        from kivy.lang import Builder

        from kivymd.app import MDApp


        class MainApp(MDApp):
            def build(self):
                self.theme_cls.theme_style = "Dark"  # "Light"
                return Builder.load_string(KV)


        MainApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bg-normal-dark-darkest.png

    :attr:`bg_darkest` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_darkest`,
    property is readonly.
    """

    def _get_op_bg_darkest(self):
        return self._get_bg_darkest(True)

    opposite_bg_darkest = AliasProperty(
        _get_op_bg_darkest, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`bg_darkest`.

    :attr:`opposite_bg_darkest` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_darkest`,
    property is readonly.
    """

    def _get_bg_dark(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["AppBar"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["AppBar"])

    bg_dark = AliasProperty(_get_bg_dark, bind=["theme_style"])
    """
    Similar to :attr:`bg_normal`,
    but the color values ​​are one tone lower (darker) than :attr:`bg_normal`.

    :attr:`bg_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_dark`,
    property is readonly.
    """

    def _get_op_bg_dark(self):
        return self._get_bg_dark(True)

    opposite_bg_dark = AliasProperty(_get_op_bg_dark, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_dark`.

    :attr:`opposite_bg_dark` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`opposite_bg_dark`,
    property is readonly.
    """

    def _get_bg_normal(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["Background"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["Background"])

    bg_normal = AliasProperty(_get_bg_normal, bind=["theme_style"])
    """
    Similar to :attr:`bg_light`,
    but the color values ​​are one tone lower (darker) than :attr:`bg_light`.

    :attr:`bg_normal` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_normal`,
    property is readonly.
    """

    def _get_op_bg_normal(self):
        return self._get_bg_normal(True)

    opposite_bg_normal = AliasProperty(_get_op_bg_normal, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_normal`.

    :attr:`opposite_bg_normal` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_normal`,
    property is readonly.
    """

    def _get_bg_light(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            return get_color_from_hex(colors["Light"]["CardsDialogs"])
        elif theme_style == "Dark":
            return get_color_from_hex(colors["Dark"]["CardsDialogs"])

    bg_light = AliasProperty(_get_bg_light, bind=["theme_style"])
    """"
    Depending on the style of the theme (`'Dark'` or `'Light`')
    that the application uses, :attr:`bg_light` contains the color value
    in ``rgba`` format for the widgets background.

    :attr:`bg_light` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`bg_light`,
    property is readonly.
    """

    def _get_op_bg_light(self):
        return self._get_bg_light(True)

    opposite_bg_light = AliasProperty(_get_op_bg_light, bind=["theme_style"])
    """
    The opposite value of color in the :attr:`bg_light`.

    :attr:`opposite_bg_light` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_bg_light`,
    property is readonly.
    """

    def _get_divider_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        color[3] = 0.12
        return color

    divider_color = AliasProperty(_get_divider_color, bind=["theme_style"])
    """
    Color for dividing lines such as  :class:`~kivymd.uix.card.MDSeparator`.

    :attr:`divider_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`divider_color`,
    property is readonly.
    """

    def _get_op_divider_color(self):
        return self._get_divider_color(True)

    opposite_divider_color = AliasProperty(
        _get_op_divider_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`divider_color`.

    :attr:`opposite_divider_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_divider_color`,
    property is readonly.
    """

    def _get_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.87
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    text_color = AliasProperty(_get_text_color, bind=["theme_style"])
    """
    Color of the text used in the :class:`~kivymd.uix.label.MDLabel`.

    :attr:`text_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`text_color`,
    property is readonly.
    """

    def _get_op_text_color(self):
        return self._get_text_color(True)

    opposite_text_color = AliasProperty(
        _get_op_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`text_color`.

    :attr:`opposite_text_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_text_color`,
    property is readonly.
    """

    def _get_secondary_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.70
        return color

    secondary_text_color = AliasProperty(
        _get_secondary_text_color, bind=["theme_style"]
    )
    """
    The color for the secondary text that is used in classes
    from the module :class:`~kivymd/uix/list.TwoLineListItem`.

    :attr:`secondary_text_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`secondary_text_color`,
    property is readonly.
    """

    def _get_op_secondary_text_color(self):
        return self._get_secondary_text_color(True)

    opposite_secondary_text_color = AliasProperty(
        _get_op_secondary_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`secondary_text_color`.

    :attr:`opposite_secondary_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`opposite_secondary_text_color`,
    property is readonly.
    """

    def _get_icon_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.54
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
        return color

    icon_color = AliasProperty(_get_icon_color, bind=["theme_style"])
    """
    Color of the icon used in the :class:`~kivymd.uix.button.MDIconButton`.

    :attr:`icon_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`icon_color`,
    property is readonly.
    """

    def _get_op_icon_color(self):
        return self._get_icon_color(True)

    opposite_icon_color = AliasProperty(
        _get_op_icon_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`icon_color`.

    :attr:`opposite_icon_color` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`opposite_icon_color`,
    property is readonly.
    """

    def _get_disabled_hint_text_color(self, opposite=False):
        theme_style = self._get_theme_style(opposite)
        if theme_style == "Light":
            color = get_color_from_hex("000000")
            color[3] = 0.38
        elif theme_style == "Dark":
            color = get_color_from_hex("FFFFFF")
            color[3] = 0.50
        return color

    disabled_hint_text_color = AliasProperty(
        _get_disabled_hint_text_color, bind=["theme_style"]
    )
    """
    Color of the disabled text used in the :class:`~kivymd.uix.textfield.MDTextField`.

    :attr:`disabled_hint_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`disabled_hint_text_color`,
    property is readonly.
    """

    def _get_op_disabled_hint_text_color(self):
        return self._get_disabled_hint_text_color(True)

    opposite_disabled_hint_text_color = AliasProperty(
        _get_op_disabled_hint_text_color, bind=["theme_style"]
    )
    """
    The opposite value of color in the :attr:`disabled_hint_text_color`.

    :attr:`opposite_disabled_hint_text_color`
    is an :class:`~kivy.properties.AliasProperty` that returns the value
    in ``rgba`` format for :attr:`opposite_disabled_hint_text_color`,
    property is readonly.
    """

    # Hardcoded because muh standard
    def _get_error_color(self):
        return get_color_from_hex(colors["Red"]["A700"])

    error_color = AliasProperty(_get_error_color)
    """
    Color of the error text used
    in the :class:`~kivymd.uix.textfield.MDTextField`.

    :attr:`error_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`error_color`,
    property is readonly.
    """

    def _get_ripple_color(self):
        return self._ripple_color

    def _set_ripple_color(self, value):
        self._ripple_color = value

    _ripple_color = ListProperty(get_color_from_hex(colors["Gray"]["400"]))
    """Private value."""

    ripple_color = AliasProperty(
        _get_ripple_color, _set_ripple_color, bind=["_ripple_color"]
    )
    """
    Color of ripple effects.

    :attr:`ripple_color` is an :class:`~kivy.properties.AliasProperty` that
    returns the value in ``rgba`` format for :attr:`ripple_color`,
    property is readonly.
    """

    def _determine_device_orientation(self, _, window_size):
        if window_size[0] > window_size[1]:
            self.device_orientation = "landscape"
        elif window_size[1] >= window_size[0]:
            self.device_orientation = "portrait"

    device_orientation = StringProperty("")
    """
    Device orientation.

    :attr:`device_orientation` is an :class:`~kivy.properties.StringProperty`.
    """

    def _get_standard_increment(self):
        if DEVICE_TYPE == "mobile":
            if self.device_orientation == "landscape":
                return dp(48)
            else:
                return dp(56)
        else:
            return dp(64)

    standard_increment = AliasProperty(
        _get_standard_increment, bind=["device_orientation"]
    )
    """
    Value of standard increment.

    :attr:`standard_increment` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`standard_increment`,
    property is readonly.
    """

    def _get_horizontal_margins(self):
        if DEVICE_TYPE == "mobile":
            return dp(16)
        else:
            return dp(24)

    horizontal_margins = AliasProperty(_get_horizontal_margins)
    """
    Value of horizontal margins.

    :attr:`horizontal_margins` is an :class:`~kivy.properties.AliasProperty`
    that returns the value in ``rgba`` format for :attr:`horizontal_margins`,
    property is readonly.
    """

    def on_theme_style(self, instance, value):
        if (
            hasattr(App.get_running_app(), "theme_cls")
            and App.get_running_app().theme_cls == self
        ):
            self.set_clearcolor_by_theme_style(value)

    set_clearcolor = BooleanProperty(True)

    def set_clearcolor_by_theme_style(self, theme_style):
        if not self.set_clearcolor:
            return
        if theme_style == "Light":
            Window.clearcolor = get_color_from_hex(
                colors["Light"]["Background"]
            )
        elif theme_style == "Dark":
            Window.clearcolor = get_color_from_hex(colors["Dark"]["Background"])

    # font name, size (sp), always caps, letter spacing (sp)
    font_styles = DictProperty(
        {
            "H1": ["RobotoLight", 96, False, -1.5],
            "H2": ["RobotoLight", 60, False, -0.5],
            "H3": ["Roboto", 48, False, 0],
            "H4": ["Roboto", 34, False, 0.25],
            "H5": ["Roboto", 24, False, 0],
            "H6": ["RobotoMedium", 20, False, 0.15],
            "Subtitle1": ["Roboto", 16, False, 0.15],
            "Subtitle2": ["RobotoMedium", 14, False, 0.1],
            "Body1": ["Roboto", 16, False, 0.5],
            "Body2": ["Roboto", 14, False, 0.25],
            "Button": ["RobotoMedium", 14, True, 1.25],
            "Caption": ["Roboto", 12, False, 0.4],
            "Overline": ["Roboto", 10, True, 1.5],
            "Icon": ["Icons", 24, False, 0],
        }
    )
    """
    Data of default font styles.

    Add custom font:

    .. code-block:: python

        KV = '''
        Screen:

            MDLabel:
                text: "JetBrainsMono"
                halign: "center"
                font_style: "JetBrainsMono"
        '''

        from kivy.core.text import LabelBase

        from kivy.lang import Builder

        from kivymd.app import MDApp
        from kivymd.font_definitions import theme_font_styles


        class MainApp(MDApp):
            def build(self):
                LabelBase.register(
                    name="JetBrainsMono",
                    fn_regular="JetBrainsMono-Regular.ttf")

                theme_font_styles.append('JetBrainsMono')
                self.theme_cls.font_styles["JetBrainsMono"] = [
                    "JetBrainsMono",
                    16,
                    False,
                    0.15,
                ]
                return Builder.load_string(KV)


        MainApp().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/font-styles.png

    :attr:`font_styles` is an :class:`~kivy.properties.DictProperty`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rec_shadow = Atlas(f"{images_path}rec_shadow.atlas")
        self.rec_st_shadow = Atlas(f"{images_path}rec_st_shadow.atlas")
        self.quad_shadow = Atlas(f"{images_path}quad_shadow.atlas")
        self.round_shadow = Atlas(f"{images_path}round_shadow.atlas")
        Clock.schedule_once(lambda x: self.on_theme_style(0, self.theme_style))
        self._determine_device_orientation(None, Window.size)
        Window.bind(size=self._determine_device_orientation)


class ThemableBehavior(EventDispatcher):
    theme_cls = ObjectProperty()
    """
    Instance of :class:`~ThemeManager` class.

    :attr:`theme_cls` is an :class:`~kivy.properties.ObjectProperty`.
    """

    device_ios = BooleanProperty(DEVICE_IOS)
    """
    ``True`` if device is ``iOS``.

    :attr:`device_ios` is an :class:`~kivy.properties.BooleanProperty`.
    """

    opposite_colors = BooleanProperty(False)

    def __init__(self, **kwargs):
        if self.theme_cls is not None:
            pass
        else:
            try:
                if not isinstance(
                    App.get_running_app().property("theme_cls", True),
                    ObjectProperty,
                ):
                    raise ValueError(
                        "KivyMD: App object must be inherited from "
                        "`kivymd.app.MDApp`. See "
                        "https://github.com/HeaTTheatR/KivyMD/blob/master/README.md#api-breaking-changes"
                    )
            except AttributeError:
                raise ValueError(
                    "KivyMD: App object must be initialized before loading "
                    "root widget. See "
                    "https://github.com/HeaTTheatR/KivyMD/wiki/Modules-Material-App#exceptions"
                )
            self.theme_cls = App.get_running_app().theme_cls
        super().__init__(**kwargs)
