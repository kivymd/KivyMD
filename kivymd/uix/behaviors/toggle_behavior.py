"""
Behaviors/ToggleButton
======================

This behavior must always be inherited after the button's Widget class since it
works with the inherited properties of the button class.

example:

.. code-block:: python

    class MyToggleButtonWidget(MDButton, MDToggleButton):
        # [...]
        pass


.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
            from kivymd.uix.button import MDButton

            KV = '''
            MDScreen:

                MDBoxLayout:
                    adaptive_size: True
                    spacing: "12dp"
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MyToggleButton:
                        group: "x"

                        MDButtonText:
                            text: "Show ads"

                    MyToggleButton:
                        group: "x"

                        MDButtonText:
                            text: "Do not show ads"

                    MyToggleButton:
                        group: "x"

                        MDButtonIcon:
                            icon: "pencil"

                        MDButtonText:
                            text: "Does not matter"
            '''


            class MyToggleButton(MDButton, MDToggleButton):
                ...


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Test().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
            from kivymd.uix.screen import MDScreen


            class MyToggleButton(MDButton, MDToggleButton):
                ...


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDBoxLayout(
                                MyToggleButton(
                                    MDButtonText(
                                        text="Show ads",
                                    ),
                                group="x",
                                ),
                                MyToggleButton(
                                    MDButtonIcon(
                                        icon="pencil",
                                    ),
                                    MDButtonText(
                                        text="Do not show ads",
                                    ),
                                    group="x",
                                ),
                                MyToggleButton(
                                    MDButtonText(
                                        text="Does not matter",
                                    ),
                                    group="x",
                                ),
                                adaptive_size=True,
                                spacing="12dp",
                                pos_hint={"center_x": .5, "center_y": .5},
                            ),
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toggle-button-1.gif
    :align: center

You can inherit the ``MyToggleButton`` class only from the following classes
----------------------------------------------------------------------------

- :class:`~kivymd.uix.button.MDRaisedButton`
- :class:`~kivymd.uix.button.MDFlatButton`
- :class:`~kivymd.uix.button.MDRectangleFlatButton`
- :class:`~kivymd.uix.button.MDRectangleFlatIconButton`
- :class:`~kivymd.uix.button.MDRoundFlatButton`
- :class:`~kivymd.uix.button.MDRoundFlatIconButton`
- :class:`~kivymd.uix.button.MDFillRoundFlatButton`
- :class:`~kivymd.uix.button.MDFillRoundFlatIconButton`
"""

__all__ = ("MDToggleButtonBehavior",)

from kivy import Logger
from kivy.properties import BooleanProperty, ColorProperty
from kivy.clock import Clock
from kivy.uix.behaviors import ToggleButtonBehavior

from kivymd.uix.button import MDButton, MDIconButton, MDFabButton


class MDToggleButtonBehavior(ToggleButtonBehavior):
    background_normal = ColorProperty(None)
    """
    Color of the button in ``rgba`` format for the 'normal' state.

    :attr:`background_normal` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    background_down = ColorProperty(None)
    """
    Color of the button in ``rgba`` format for the 'down' state.

    :attr:`background_down` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    font_color_normal = ColorProperty(None)
    """
    Color of the font's button in ``rgba`` format for the 'normal' state.

    :attr:`font_color_normal` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    font_color_down = ColorProperty(None)
    """
    Color of the font's button in ``rgba`` format for the 'down' state.

    :attr:`font_color_down` is a :class:`~kivy.properties.ColorProperty`
    and is defaults to `None`.
    """

    _origin_md_bg_color = None
    _origin_icon_color = None
    _origin_text_color = None

    __is_filled = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classinfo = (MDButton, MDIconButton, MDFabButton)
        Clock.schedule_once(self._set_custom_theme_properties)
        Clock.schedule_once(self.set_properties, 0.1)

    def set_properties(self, *args):
        if not issubclass(self.__class__, self.classinfo):
            raise ValueError(
                f"{self.__class__} must inherit from one of {self.classinfo}"
            )

        self._set_origin_color_properties()

        color_map = self._get_color_map()
        color_key = (
            self.style if not isinstance(self, MDFabButton) else self.color_map
        )
        self.md_bg_color = self.background_normal or (
            getattr(self, "md_bg_color", None)
            if not isinstance(self, MDFabButton)
            else color_map[color_key]
        )
        self.background_down = (
            self.background_down or self.theme_cls.primaryColor
        )
        self.font_color_normal = self.font_color_normal or (
            color_map.get(color_key, self.theme_cls.primaryColor)
            if not isinstance(self, MDFabButton)
            else {
                "surface": self.theme_cls.onPrimaryContainerColor,
                "secondary": self.theme_cls.onSecondaryContainerColor,
                "tertiary": self.theme_cls.onTertiaryContainerColor,
            }[self.color_map]
        )
        self._set_text_and_icon_colors(self.font_color_normal)
        self.fbind("state", self._update_colors)

    def _get_color_map(self):
        """
        Returns a dictionary mapping button styles to their corresponding
        default colors.

        The returned color map depends on the type of the button:
        - For MDButton, returns a map based on Material Design button styles
          (elevated, filled, tonal, outlined, text).
        - For MDIconButton, returns a map for icon button styles
          (standard, outlined, tonal, filled).
        - For other cases (fallback), returns a general-purpose color map
          based on surface-level roles (surface, secondary, tertiary).
        """

        if isinstance(self, MDButton):
            return {
                "elevated": self.theme_cls.primaryColor,
                "filled": self.theme_cls.onPrimaryColor,
                "tonal": self.theme_cls.onSecondaryContainerColor,
                "outlined": self.theme_cls.primaryColor,
                "text": self.theme_cls.primaryColor,
            }
        elif isinstance(self, MDIconButton):
            return {
                "standard": self.theme_cls.transparentColor,
                "outlined": self.theme_cls.transparentColor,
                "tonal": self.theme_cls.secondaryContainerColor,
                "filled": self.theme_cls.primaryColor,
            }
        return {
            "surface": self.theme_cls.surfaceColor,
            "secondary": self.theme_cls.secondaryColor,
            "tertiary": self.theme_cls.tertiaryColor,
        }

    def _set_origin_color_properties(self):
        """
        Store original background, icon, and text colors for later restoration.
        """

        self._origin_md_bg_color = (
            getattr(self, "md_bg_color", None)
            if not isinstance(self, MDFabButton)
            else self._get_color_map()[self.color_map]
        )
        fallback = self.font_color_normal
        if isinstance(self, MDFabButton):
            self._origin_icon_color = fallback or self.icon_color
            self._origin_text_color = fallback or self.icon_color
        else:
            if hasattr(self, "_button_icon") and self._button_icon:
                self._origin_icon_color = (
                    fallback or self._button_icon.icon_color
                )
            if hasattr(self, "_button_text") and self._button_text:
                self._origin_text_color = (
                    fallback or self._button_text.text_color
                )

    def _set_custom_theme_properties(self, *args):
        """
        Replace any 'Primary' theme values with 'Custom' to allow overrides.
        """

        for attr in ("theme_bg_color", "theme_icon_color"):
            if getattr(self, attr, None) == "Primary":
                setattr(self, attr, "Custom")
        if (
            hasattr(self, "_button_text")
            and self._button_text
            and self._button_text.theme_text_color == "Primary"
        ):
            self._button_text.theme_text_color = "Custom"
        if (
            hasattr(self, "_button_icon")
            and self._button_icon
            and self._button_icon.theme_icon_color == "Primary"
        ):
            self._button_icon.theme_icon_color = "Custom"

    def _update_colors(self, instance, value):
        """Update background and font/icon colors based on button state."""

        if value == "down":
            self.md_bg_color = (
                self.background_down or self.theme_cls.primaryColor
            )
            color = (
                self.font_color_down or self.theme_cls.surfaceContainerHighColor
            )
            self._set_text_and_icon_colors(color)
            if isinstance(self, MDIconButton):
                self.icon_color = self.theme_cls.onPrimaryColor
            if isinstance(self, MDFabButton):
                self.icon_color = color
            if self.group:
                self._release_group(self)
        else:
            self.md_bg_color = (
                self.background_normal
                or self._origin_md_bg_color
                or self._get_default_style_color()
            )
            if isinstance(self, MDIconButton):
                self.icon_color = (
                    self._origin_icon_color or self.theme_cls.primaryColor
                )
            self._set_text_and_icon_colors(
                self._origin_text_color, self._origin_icon_color
            )

    def _set_text_and_icon_colors(self, text_color=None, icon_color=None):
        """Set text and icon colors if components exist."""

        if isinstance(self, MDFabButton):
            self.icon_color = text_color
        else:
            if hasattr(self, "_button_text") and self._button_text:
                self._button_text.text_color = text_color
            if hasattr(self, "_button_icon") and self._button_icon:
                self._button_icon.icon_color = icon_color or text_color

    def _get_default_style_color(self):
        """Return default background color based on button style."""

        return {
            "elevated": self.theme_cls.surfaceContainerLowColor,
            "filled": self.theme_cls.primaryColor,
            "tonal": self.theme_cls.secondaryContainerColor,
            "outlined": self.theme_cls.transparentColor,
            "text": self.theme_cls.transparentColor,
        }.get(self.style, self.theme_cls.surfaceColor)


class MDToggleButton(MDToggleButtonBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.warning(
            f"KivyMD: "
            f"The `{self.__class__.__name__}` class has been deprecated. "
            f"Use the `MDToggleButtonBehavior` class instead."
        )
