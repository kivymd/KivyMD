"""
Themes/Theming
==============

.. seealso::

   `Material Design spec, Dynamic color <https://m3.material.io/styles/color/dynamic-color/overview>`_

Material App
------------

The main class of your application, which in `Kivy` inherits from the
:class:`~kivy.app.App` class, in `KivyMD` must inherit from the
:class:`~kivymd.app.MDApp` class. The :class:`~kivymd.app.MDApp` class has
properties that allow you to control application properties such as
:attr:`color/style/font` of interface elements and much more.

Control material properties
---------------------------

The main application class inherited from the :class:`~kivymd.app.MDApp` class
has the :attr:`~kivymd.app.MDApp.theme_cls` attribute, with which you control
the material properties of your application.
"""


from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty
)
from kivy.utils import get_color_from_hex, hex_colormap, rgba
from materialyoucolor.dislike.dislike_analyzer import DislikeAnalyzer
from materialyoucolor.dynamiccolor.material_dynamic_colors import (
    MaterialDynamicColors,
)
from materialyoucolor.hct import Hct
from materialyoucolor.utils.color_utils import argb_from_rgba_01
from materialyoucolor.utils.platform_utils import SCHEMES, get_dynamic_scheme

from kivymd.dynamic_color import DynamicColor
from kivymd.font_definitions import theme_font_styles
from kivymd.material_resources import DEVICE_IOS


class ThemeManager(EventDispatcher, DynamicColor):
    primary_palette = OptionProperty(
        None,
        options=[name_color.capitalize() for name_color in hex_colormap.keys()],
    )
    """
    The name of the color scheme that the application will use.
    All major `material` components will have the color
    of the specified color theme.

    See :attr:`kivy.utils.hex_colormap` keys for available values.

    To change the color scheme of an application:

    .. tabs::

        .. tab:: Imperative python style with KV

            .. code-block:: python

                from kivy.lang import Builder

                from kivymd.app import MDApp

                KV = '''
                MDScreen:
                    md_bg_color: self.theme_cls.backgroundColor

                    MDButton:
                        style: "elevated"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MDButtonIcon:
                            icon: "plus"

                        MDButtonText:
                            text: "Button"
                '''


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"
                        return Builder.load_string(KV)


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivymd.app import MDApp
                from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
                from kivymd.uix.screen import MDScreen


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"

                        return (
                            MDScreen(
                                MDButton(
                                    MDButtonIcon(
                                        icon="plus",
                                    ),
                                    MDButtonText(
                                        text="Button",
                                    ),
                                    style="elevated",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                ),
                                md_bg_color=self.theme_cls.backgroundColor,
                            )
                        )


                Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/primary-palette-m3.png
        :align: center

    :attr:`primary_palette` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    dynamic_color_quality = NumericProperty(1 if platform == "android" else 10)
    """
    The quality of the generated color scheme from the system wallpaper.
    It is equal to or higher than `1`, with `1` representing the maximum quality.

    .. warning::

        Remember that by increasing the quality value, you also increase the
        generation time of the color scheme.

    :attr:`dynamic_color_quality` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `10` if platform is not Android else `1`.
    """

    dynamic_color = BooleanProperty(False)
    """
    Enables or disables dynamic color.

    .. versionadded:: 2.0.0

    .. seealso::

        `Material Design spec, Dynamic color <https://m3.material.io/styles/color/dynamic-color/overview>`_

    To build the color scheme of your application from user wallpapers, you
    must enable the `READ_EXTERNAL_STORAGE
    <https://github.com/Android-for-Python/Android-for-Python-Users?tab=readme-ov-file#storage-permissions>`_
    permission if your android version is below 8.1:

    .. tabs::

        .. tab:: Imperative python style with KV

            .. code-block:: python

                from kivy import platform
                from kivy.lang import Builder
                from kivy.clock import Clock

                from kivymd.app import MDApp

                KV = '''
                MDScreen:
                    md_bg_color: app.theme_cls.surfaceColor

                    MDButton:
                        style: "elevated"
                        pos_hint: {"center_x": .5, "center_y": .5}
        
                        MDButtonIcon:
                            icon: "plus"
        
                        MDButtonText:
                            text: "Elevated"
                '''


                class Example(MDApp):
                    def build(self):
                        return Builder.load_string(KV)

                    def on_resume(self, *args):
                        '''Updating the color scheme when the application resumes.'''

                        self.theme_cls.set_colors()

                    def set_dynamic_color(self, *args) -> None:
                        '''
                        When sets the `dynamic_color` value, the self method will be
                        `called.theme_cls.set_colors()` which will generate a color
                        scheme from a custom wallpaper if `dynamic_color` is `True`.
                        '''

                        self.theme_cls.dynamic_color = True

                    def on_start(self) -> None:
                        '''
                        It is fired at the start of the application and requests the
                        necessary permissions.
                        '''

                        def callback(permission, results):
                            if all([res for res in results]):
                                Clock.schedule_once(self.set_dynamic_color)

                        if platform == "android":
                            from android.permissions import Permission, request_permissions

                            permissions = [Permission.READ_EXTERNAL_STORAGE]
                            request_permissions(permissions, callback)


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivy import platform
                from kivy.clock import Clock

                from kivymd.app import MDApp
                from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
                from kivymd.uix.screen import MDScreen


                class Example(MDApp):
                    def build(self):
                        return (
                            MDScreen(
                                MDButton(
                                    MDButtonIcon(
                                        icon="plus",
                                    ),
                                    MDButtonText(
                                        text="Elevated",
                                    ),
                                    style="elevated",
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                md_bg_color=self.theme_cls.surfaceColor,
                            )
                        )

                    def on_resume(self, *args):
                        '''Updating the color scheme when the application resumes.'''

                        self.theme_cls.set_colors()

                    def set_dynamic_color(self, *args) -> None:
                        '''
                        When sets the `dynamic_color` value, the self method will be
                        `called.theme_cls.set_colors()` which will generate a color
                        scheme from a custom wallpaper if `dynamic_color` is `True`.
                        '''

                        self.theme_cls.dynamic_color = True

                    def on_start(self) -> None:
                        '''
                        It is fired at the start of the application and requests the
                        necessary permissions.
                        '''

                        def callback(permission, results):
                            if all([res for res in results]):
                                Clock.schedule_once(self.set_dynamic_color)

                        if platform == "android":
                            from android.permissions import Permission, request_permissions

                            permissions = [Permission.READ_EXTERNAL_STORAGE]
                            request_permissions(permissions, callback)


                Example().run()

    :attr:`dynamic_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    dynamic_scheme_name = OptionProperty("TONAL_SPOT", options=SCHEMES.keys())
    """
    Name of the dynamic scheme. Availabe schemes `TONAL_SPOT`, `SPRITZ`
    `VIBRANT`, `EXPRESSIVE`, `FRUIT_SALAD`, `RAINBOW`, `MONOCHROME`, `FIDELITY`
    and `CONTENT`.

    :attr:`dynamic_scheme_name` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'TONAL_SPOT'`.
    """

    dynamic_scheme_contrast = NumericProperty(0.0)
    """
    The contrast of the generated color scheme.

    :attr:`dynamic_scheme_contrast` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.0`.
    """

    path_to_wallpaper = StringProperty()
    """
    The path to the image to set the color scheme. You can use this option
    if you want to use dynamic color on platforms other than the Android
    platform.

    .. versionadded:: 2.0.0

    :attr:`path_to_wallpaper` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    theme_style_switch_animation = BooleanProperty(True)
    """
    Animate app colors when switching app color scheme ('Dark/light').

    .. versionadded:: 1.1.0

    .. tabs::

        .. tab:: Declarative KV style

            .. code-block:: python

                from kivy.lang import Builder

                from kivymd.app import MDApp

                KV = '''
                MDScreen:
                    md_bg_color: self.theme_cls.backgroundColor

                    MDCard:
                        orientation: "vertical"
                        padding: 0, 0, 0 , "36dp"
                        size_hint: .5, .5
                        style: "elevated"
                        pos_hint: {"center_x": .5, "center_y": .5}

                        MDLabel:
                            text: "Theme style - {}".format(app.theme_cls.theme_style)
                            halign: "center"
                            valign: "center"
                            bold: True
                            font_style: "Display"
                            role: "small"

                        MDButton:
                            on_release: app.switch_theme_style()
                            pos_hint: {"center_x": .5}

                            MDButtonText:
                                text: "Set theme"
                '''


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style_switch_animation = True
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return Builder.load_string(KV)

                    def switch_theme_style(self):
                        self.theme_cls.primary_palette = (
                            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
                        )
                        self.theme_cls.theme_style = (
                            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
                        )


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivy.clock import Clock

                from kivymd.app import MDApp
                from kivymd.uix.button import MDButton, MDButtonText
                from kivymd.uix.card import MDCard
                from kivymd.uix.label import MDLabel
                from kivymd.uix.screen import MDScreen


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style_switch_animation = True
                        self.theme_cls.theme_style = "Dark"
                        self.theme_cls.primary_palette = "Orange"
                        return (
                            MDScreen(
                                MDCard(
                                    MDLabel(
                                        id="label",
                                        text="Theme style - {}".format(
                                            self.theme_cls.theme_style),
                                        halign="center",
                                        valign="center",
                                        bold=True,
                                        font_style="Display",
                                        role="small",
                                    ),
                                    MDButton(
                                        MDButtonText(
                                            text="Set theme",
                                        ),
                                        on_release=self.switch_theme_style,
                                        pos_hint={"center_x": 0.5},
                                    ),
                                    id="card",
                                    orientation="vertical",
                                    padding=(0, 0, 0, "36dp"),
                                    size_hint=(0.5, 0.5),
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    style="elevated",
                                )
                            )
                        )

                    def on_start(self):
                        def on_start(*args):
                            self.root.md_bg_color = self.theme_cls.backgroundColor

                        Clock.schedule_once(on_start)

                    def switch_theme_style(self, *args):
                        self.theme_cls.primary_palette = (
                            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
                        )
                        self.theme_cls.theme_style = (
                            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
                        )
                        self.root.get_ids().label.text = (
                            "Theme style - {}".format(self.theme_cls.theme_style)
                        )


                Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/theme-style-switch-animation.gif
        :align: center

    :attr:`theme_style_switch_animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    theme_style_switch_animation_duration = NumericProperty(0.2)
    """
    Duration of the animation of switching the color scheme of the application
    ("Dark/light").

    .. versionadded:: 1.1.0

    .. code-block:: python

        class Example(MDApp):
            def build(self):
                self.theme_cls.theme_style_switch_animation = True
                self.theme_cls.theme_style_switch_animation_duration = 0.8

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/theme-style-switch-animation-duration.gif
        :align: center

    :attr:`theme_style_switch_animation_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    theme_style = OptionProperty("Light", options=["Light", "Dark"])
    """
    App theme style.

    .. code-block:: python

        from kivy.clock import Clock

        from kivymd.app import MDApp
        from kivymd.uix.screen import MDScreen
        from kivymd.uix.button import MDButton, MDButtonText


        class Example(MDApp):
            def build(self):
                self.theme_cls.primary_palette = "Orange"
                self.theme_cls.theme_style = "Light"  # "Dark"
                return MDScreen(
                    MDButton(
                        MDButtonText(
                            text="Hello, World",
                        ),
                        style="outlined",
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )

            def on_start(self):
                def on_start(*args):
                    self.root.md_bg_color = self.theme_cls.backgroundColor

                Clock.schedule_once(on_start)


        Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/theme-style.png
        :align: center

    :attr:`theme_style` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Light'`.
    """

    def _get_theme_style(self, opposite: bool) -> str:
        if opposite:
            return "Light" if self.theme_style == "Dark" else "Dark"
        else:
            return self.theme_style

    def _get_disabled_hint_text_color(self, opposite: bool = False) -> list:
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

    def _determine_device_orientation(self, _, window_size) -> None:
        if window_size[0] > window_size[1]:
            self.device_orientation = "landscape"
        elif window_size[1] >= window_size[0]:
            self.device_orientation = "portrait"

    device_orientation = StringProperty()
    """
    Device orientation.

    :attr:`device_orientation` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    # Font name, size (sp), always caps, letter spacing (sp).
    font_styles = DictProperty(theme_font_styles)
    """
    Data of default font styles.

    Add custom font
    ---------------

    .. tabs::

        .. tab:: Declarative style with KV

            .. code-block:: python

                from kivy.core.text import LabelBase
                from kivy.lang import Builder
                from kivy.metrics import sp

                from kivymd.app import MDApp

                KV = '''
                MDScreen:
                    md_bg_color: self.theme_cls.backgroundColor

                    MDLabel:
                        text: "MDLabel"
                        halign: "center"
                        font_style: "nasalization"
                '''


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"

                        LabelBase.register(
                            name="nasalization",
                            fn_regular="nasalization.ttf",
                        )

                        self.theme_cls.font_styles["nasalization"] = {
                            "large": {
                                "line-height": 1.64,
                                "font-name": "nasalization",
                                "font-size": sp(57),
                            },
                            "medium": {
                                "line-height": 1.52,
                                "font-name": "nasalization",
                                "font-size": sp(45),
                            },
                            "small": {
                                "line-height": 1.44,
                                "font-name": "nasalization",
                                "font-size": sp(36),
                            },
                        }

                        return Builder.load_string(KV)


                Example().run()

        .. tab:: Declarative python style

            .. code-block:: python

                from kivy.core.text import LabelBase
                from kivy.metrics import sp

                from kivymd.uix.label import MDLabel
                from kivymd.uix.screen import MDScreen
                from kivymd.app import MDApp


                class Example(MDApp):
                    def build(self):
                        self.theme_cls.theme_style = "Dark"

                        LabelBase.register(
                            name="nasalization",
                            fn_regular="/Users/urijivanov/Projects/Dev/MyGithub/Articles/StarTest/data/font/nasalization-rg.ttf",
                        )

                        self.theme_cls.font_styles["nasalization"] = {
                            "large": {
                                "line-height": 1.64,
                                "font-name": "nasalization",
                                "font-size": sp(57),
                            },
                            "medium": {
                                "line-height": 1.52,
                                "font-name": "nasalization",
                                "font-size": sp(45),
                            },
                            "small": {
                                "line-height": 1.44,
                                "font-name": "nasalization",
                                "font-size": sp(36),
                            },
                        }

                        return (
                            MDScreen(
                                MDLabel(
                                    text="JetBrainsMono",
                                    halign="center",
                                    font_style="nasalization",
                                )
                            )
                        )


                Example().run()

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-font-styles.png
        :align: center

    :attr:`font_styles` is an :class:`~kivy.properties.DictProperty`.
    """

    on_colors = None
    """
    A Helper function called when colors are changed.

    :attr: `on_colors` defaults to `None`.
    """

    def _get_dynamic_color_names(self):
        return [
            attr for attr in dir(self) if attr.endswith("Color")
        ]

    dynamic_color_names = AliasProperty(_get_dynamic_color_names)
    """
    List of material design dynamic color palette names:

        • backgroundColor
        • disabledTextColor
        • errorColor
        • errorContainerColor
        • inverseOnSurfaceColor
        • inversePrimaryColor
        • inverseSurfaceColor
        • neutral_paletteKeyColorColor
        • neutral_variant_paletteKeyColorColor
        • onBackgroundColor
        • onErrorColor
        • onErrorContainerColor
        • onPrimaryColor
        • onPrimaryContainerColor
        • onPrimaryFixedColor
        • onPrimaryFixedVariantColor
        • onSecondaryColor
        • onSecondaryContainerColor
        • onSecondaryFixedColor
        • onSecondaryFixedVariantColor
        • onSurfaceColor
        • onSurfaceLightColor
        • onSurfaceVariantColor
        • onTertiaryColor
        • onTertiaryContainerColor
        • onTertiaryFixedColor
        • onTertiaryFixedVariantColor
        • outlineColor
        • outlineVariantColor
        • primaryColor
        • primaryContainerColor
        • primaryFixedColor
        • primaryFixedDimColor
        • primary_paletteKeyColorColor
        • rippleColor
        • scrimColor
        • secondaryColor
        • secondaryContainerColor
        • secondaryFixedColor
        • secondaryFixedDimColor
        • secondary_paletteKeyColorColor
        • shadowColor
        • surfaceBrightColor
        • surfaceColor
        • surfaceContainerColor
        • surfaceContainerHighColor
        • surfaceContainerHighestColor
        • surfaceContainerLowColor
        • surfaceContainerLowestColor
        • surfaceDimColor
        • surfaceTintColor
        • surfaceVariantColor
        • tertiaryColor
        • tertiaryContainerColor
        • tertiaryFixedColor
        • tertiaryFixedDimColor
        • tertiary_paletteKeyColorColor
        • transparentColor

    :attr:`dynamic_color_names` is an :class:`~kivy.properties.AliasProperty`
    and for internal usage only.
    """

    _size_current_wallpaper = NumericProperty(0)
    _dark_mode = lambda self: False if self.theme_style == "Light" else True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._determine_device_orientation(None, Window.size)
        Window.bind(size=self._determine_device_orientation)

    def set_colors(self, *args) -> None:
        """Fired methods for setting a new color scheme."""

        if not self.dynamic_color:
            if not self.primary_palette:
                self._set_application_scheme()
            else:
                self._set_palette_color()
        else:
            system_scheme = get_dynamic_scheme(
                dark_mode=self._dark_mode(),
                contrast=self.dynamic_scheme_contrast,
                dynamic_color_quality=self.dynamic_color_quality,
                fallback_wallpaper_path=self.path_to_wallpaper,
                fallback_scheme_name=self.dynamic_scheme_name,
                message_logger=Logger.info,
                logger_head="KivyMD",
            )
            if system_scheme:
                self._set_color_names(system_scheme)
            else:
                self._set_application_scheme()

    def update_theme_colors(self, *args) -> None:
        """Fired when the :attr:`theme_style` value changes."""

        self.set_colors()

    def on_dynamic_scheme_name(self, *args) -> None:
        """Fired when the :attr:`dynamic_scheme_name` value changes."""

        self.set_colors()

    def on_dynamic_scheme_contrast(self, *args) -> None:
        """Fired when the :attr:`dynamic_scheme_contrast` value changes."""

        self.set_colors()

    def on_path_to_wallpaper(self, *args) -> None:
        """Fired when the :attr:`path_to_wallpaper` value changes."""

        self.set_colors()

    def switch_theme(self) -> None:
        """Switches the theme from light to dark."""

        self.theme_style = "Dark" if self.theme_style == "Light" else "Light"

    def sync_theme_styles(self, *args) -> None:
        # Syncs the values from self.font_styles to theme_font_styles
        # this will ensure continuity when someone registers a new font_style.
        for num, style in enumerate(theme_font_styles):
            if style not in self.font_styles:
                theme_font_styles.pop(num)
        for style in self.font_styles.keys():
            theme_font_styles.append(style)

    def _set_application_scheme(
        self,
        color="blue",  # Google default
    ) -> None:
        if not self.primary_palette:
            color = "blue"
        else:
            color = self.primary_palette

        color = get_color_from_hex(hex_colormap[color.lower()])
        color = Hct.from_int(argb_from_rgba_01(color))
        color = DislikeAnalyzer.fix_if_disliked(color).to_int()

        self._set_color_names(
            SCHEMES[self.dynamic_scheme_name](
                Hct.from_int(color),
                self._dark_mode(),
                self.dynamic_scheme_contrast,
            )
        )

    def _set_color_names(self, scheme) -> None:
        for color_name in vars(MaterialDynamicColors).keys():
            attr = getattr(MaterialDynamicColors, color_name)
            if hasattr(attr, "get_hct"):
                color_value = rgba(attr.get_hct(scheme).to_rgba())
                setattr(self, f"{color_name}Color", color_value)

        self.disabledTextColor = self._get_disabled_hint_text_color()
        if self.on_colors:
            self.on_colors()

    def _set_palette_color(self) -> None:
        if not self.primary_palette:
            self.primary_palette = "Blue"
        self._set_application_scheme(self.primary_palette)


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

    theme_line_color = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Line color scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_line_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_bg_color = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Background color scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_bg_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_shadow_color = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Elevation color scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_shadow_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_shadow_offset = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Elevation offset scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_shadow_offset` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_elevation_level = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Elevation level scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_elevation_level` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_font_size = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Font size scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_font_size` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_width = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Widget width scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_width` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_height = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Widget width scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_height` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_line_height = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Line height scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_line_height` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_font_name = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Font name scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_font_name` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_shadow_softness = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Elevation softness scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_shadow_softness` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_focus_color = OptionProperty("Primary", options=["Primary", "Custom"])
    """
    Focus color scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_focus_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_divider_color = OptionProperty(
        "Primary", options=["Primary", "Custom"]
    )
    """
    Divider color scheme name.

    .. versionadded:: 2.0.0

    Available options are: `'Primary'`, `'Custom'`.

    :attr:`theme_divider_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_text_color = OptionProperty(
        "Primary",
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
        ],
    )
    """
    Label color scheme name.

    Available options are: `'Primary'`, `'Secondary'`, `'Hint'`, `'Error'`,
    `'Custom'`.

    :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    theme_icon_color = OptionProperty(
        "Primary",
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
        ],
    )
    """
    Label color scheme name.

    Available options are: `'Primary'`, `'Secondary'`, `'Hint'`, `'Error'`,
    `'Custom'`.

    :attr:`theme_icon_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Primary'`.
    """

    def __init__(self, **kwargs):
        if self.theme_cls is None:
            try:
                if not isinstance(
                    App.get_running_app().property("theme_cls", True),
                    ObjectProperty,
                ):
                    raise ValueError(
                        "KivyMD: App object must be inherited from "
                        "`kivymd.app.MDApp`"
                    )
            except AttributeError:
                raise ValueError(
                    "KivyMD: App object must be initialized before loading "
                    "root widget. See "
                    "https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions"
                )
            self.theme_cls = App.get_running_app().theme_cls

        super().__init__(**kwargs)

        # Fix circular imports.
        from kivymd.uix.behaviors import CommonElevationBehavior
        from kivymd.uix.label import MDLabel
        from kivymd.uix.textfield import MDTextField

        self.common_elevation_behavior = CommonElevationBehavior
        self.md_label = MDLabel
        self.md_textfield = MDTextField

    def remove_widget(self, widget) -> None:
        if not hasattr(widget, "theme_cls"):
            super().remove_widget(widget)
            return

        callbacks = widget.theme_cls.get_property_observers("theme_style")

        for callback in callbacks:
            try:
                if hasattr(callback, "proxy") and hasattr(
                    callback.proxy, "theme_cls"
                ):
                    for property_name in ["theme_style", "primary_palette"]:
                        if widget == callback.proxy:
                            widget.theme_cls.unbind(
                                **{
                                    property_name: getattr(
                                        callback.proxy, callback.method_name
                                    )
                                }
                            )
            except ReferenceError:
                pass

        # Canceling a scheduled method call on_window_touch for MDLabel
        # objects.
        if (
            issubclass(widget.__class__, self.md_label)
            and self.md_label.allow_selection
        ):
            Window.unbind(on_touch_down=widget.on_window_touch)

        super().remove_widget(widget)
