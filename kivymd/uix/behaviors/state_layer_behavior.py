# TODO: Add docs.

"""
Behaviors/State Layer
=====================

.. seealso::

   `Material Design spec, State layers <https://m3.material.io/foundations/interaction/states/state-layers>`_
"""

from kivy import platform
from kivy.lang import Builder
from kivy.properties import ColorProperty, NumericProperty

from kivymd.uix.behaviors.focus_behavior import FocusBehavior


Builder.load_string(
    """
<StateLayerBehavior>
    canvas.after:
        Color
            rgba: self.state_layer_color
        RoundedRectangle:
            group: "State_layer_instruction"
            size: self.size
            pos: self.pos
            radius: self.radius if hasattr(self, "radius") else [0, ]
""",
    filename="StateLayerBehavior.kv",
)

# TODO: Add methods `set_text_color` and `set_icon_color`
#  (methods that set the color of text and icons in the state
#  `on_enter` and `on_leave` and `pressed`).


class StateLayerBehavior(FocusBehavior):
    state_layer_color = ColorProperty([0, 0, 0, 0])
    """
    The color of the layer state.

    :attr:`state_layer_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    state_hover = NumericProperty(0.08)
    """
    The transparency level of the layer as a percentage when hovering.
    
    :attr:`state_hover` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.08`.
    """

    state_press = NumericProperty(0.12)
    """
    The transparency level of the layer as a percentage when pressed.

    :attr:`state_press` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.12`.
    """

    state_drag = NumericProperty(0.16)
    """
    The transparency level of the layer as a percentage when dragged.

    :attr:`state_drag` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.16`.
    """

    # The transparency value of the disabled state.
    # These values are specified in the M3 specification.

    # -------------------------------------------------------------------------
    #                            MDIconButton
    # -------------------------------------------------------------------------

    # Filled.
    icon_button_filled_opacity_value_disabled_container = NumericProperty(0.12)
    icon_button_filled_opacity_value_disabled_icon = NumericProperty(0.38)

    # Tonal.
    icon_button_tonal_opacity_value_disabled_container = NumericProperty(0.12)
    icon_button_tonal_opacity_value_disabled_icon = NumericProperty(0.38)

    # Outlined.
    icon_button_outlined_opacity_value_disabled_container = NumericProperty(
        0.12
    )
    icon_button_outlined_opacity_value_disabled_line = NumericProperty(0.12)
    icon_button_outlined_opacity_value_disabled_icon = NumericProperty(0.38)

    # Standard.
    icon_button_standard_opacity_value_disabled_icon = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                              MDFabButton
    # -------------------------------------------------------------------------

    fab_button_opacity_value_disabled_container = NumericProperty(0.12)
    fab_button_opacity_value_disabled_icon = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                              MDButton
    # -------------------------------------------------------------------------

    # Filled.
    button_filled_opacity_value_disabled_container = NumericProperty(0.12)
    button_filled_opacity_value_disabled_icon = NumericProperty(0.38)
    button_filled_opacity_value_disabled_text = NumericProperty(0.38)

    # Tonal.
    button_tonal_opacity_value_disabled_container = NumericProperty(0.12)
    button_tonal_opacity_value_disabled_icon = NumericProperty(0.38)
    button_tonal_opacity_value_disabled_text = NumericProperty(0.38)

    # Outlined.
    button_outlined_opacity_value_disabled_container = NumericProperty(0.12)
    button_outlined_opacity_value_disabled_line = NumericProperty(0.12)
    button_outlined_opacity_value_disabled_icon = NumericProperty(0.38)
    button_outlined_opacity_value_disabled_text = NumericProperty(0.38)

    # Elevated.
    button_elevated_opacity_value_disabled_container = NumericProperty(0.12)
    button_elevated_opacity_value_disabled_icon = NumericProperty(0.38)
    button_elevated_opacity_value_disabled_text = NumericProperty(0.38)

    # Text.
    button_text_opacity_value_disabled_icon = NumericProperty(0.38)
    button_text_opacity_value_disabled_text = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                               MDLabel
    # -------------------------------------------------------------------------

    label_opacity_value_disabled_text = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                               MDCard
    # -------------------------------------------------------------------------

    card_filled_opacity_value_disabled_state_container = NumericProperty(0.38)
    card_outlined_opacity_value_disabled_state_container = NumericProperty(0.12)
    card_opacity_value_disabled_state_elevated_container = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                         MDSegmentedButton
    # -------------------------------------------------------------------------

    segmented_button_opacity_value_disabled_container = NumericProperty(0.12)
    segmented_button_opacity_value_disabled_container_active = NumericProperty(
        0.38
    )
    segmented_button_opacity_value_disabled_line = NumericProperty(0.12)
    segmented_button_opacity_value_disabled_icon = NumericProperty(0.38)
    segmented_button_opacity_value_disabled_text = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                              MDChip
    # -------------------------------------------------------------------------

    chip_opacity_value_disabled_container = NumericProperty(0.12)
    chip_opacity_value_disabled_text = NumericProperty(0.38)
    chip_opacity_value_disabled_icon = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                              MDSwitch
    # -------------------------------------------------------------------------

    switch_opacity_value_disabled_line = NumericProperty(0.12)
    switch_opacity_value_disabled_container = NumericProperty(0.12)
    switch_thumb_opacity_value_disabled_container = NumericProperty(0.38)
    switch_opacity_value_disabled_icon = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                              MDCheckbox
    # -------------------------------------------------------------------------

    checkbox_opacity_value_disabled_container = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                                List
    # -------------------------------------------------------------------------

    list_opacity_value_disabled_container = NumericProperty(0.38)
    list_opacity_value_disabled_leading_avatar = NumericProperty(0.38)

    # -------------------------------------------------------------------------
    #                             MDTextField
    # -------------------------------------------------------------------------

    text_field_filled_opacity_value_disabled_state_container = NumericProperty(
        0.18
    )
    text_field_outlined_opacity_value_disabled_state_container = (
        NumericProperty(0)
    )
    text_field_opacity_value_disabled_max_length_label = NumericProperty(0.60)
    text_field_opacity_value_disabled_helper_text_label = NumericProperty(0.60)
    text_field_opacity_value_disabled_hint_text_label = NumericProperty(0.60)
    text_field_opacity_value_disabled_leading_icon = NumericProperty(0.60)
    text_field_opacity_value_disabled_trailing_icon = NumericProperty(0.60)
    text_field_opacity_value_disabled_line = NumericProperty(0.12)

    _state = 0.0
    _bg_color = (0, 0, 0, 0)
    _is_already_disabled = False
    _shadow_softness = [0, 0]
    _elevation_level = 0

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def set_properties_widget(self) -> None:
        """Fired `on_release/on_press/on_enter/on_leave` events."""

        if not self.disabled:
            self._restore_properties()
            self._set_state_layer_color()

    def on_disabled(self, instance, value) -> None:
        """Fired when the `disabled` value changes."""

        from kivymd.uix.card import MDCard
        from kivymd.uix.button import (
            MDIconButton,
            MDButton,
            MDFabButton,
            MDExtendedFabButton,
        )
        from kivymd.uix.segmentedbutton import MDSegmentedButtonItem
        from kivymd.uix.segmentedbutton.segmentedbutton import (
            MDSegmentButtonSelectedIcon,
        )
        from kivymd.uix.selectioncontrol import MDSwitch
        from kivymd.uix.list import BaseListItem
        from kivymd.uix.textfield import MDTextField

        if value and not self._is_already_disabled:
            self._is_already_disabled = True
            if isinstance(self, MDCard):
                self.state_layer_color = (
                    {
                        "filled": self.theme_cls.surfaceColor[:-1]
                        + [
                            self.card_filled_opacity_value_disabled_state_container
                        ],
                        "outlined": self.theme_cls.outlineColor[:-1]
                        + [
                            self.card_outlined_opacity_value_disabled_state_container
                        ],
                        "elevated": self.theme_cls.surfaceVariantColor[:-1]
                        + [
                            self.card_opacity_value_disabled_state_elevated_container
                        ],
                    }[self.style]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
            elif isinstance(self, MDIconButton):
                self.state_layer_color = (
                    {
                        "tonal": self.theme_cls.onSurfaceColor[:-1]
                        + [
                            self.icon_button_tonal_opacity_value_disabled_container
                        ],
                        "filled": self.theme_cls.onSurfaceColor[:-1]
                        + [
                            self.icon_button_filled_opacity_value_disabled_container
                        ],
                        "outlined": self.theme_cls.onSurfaceColor[:-1]
                        + [
                            self.icon_button_outlined_opacity_value_disabled_container
                        ],
                        "standard": self.theme_cls.transparentColor,
                    }[self.style]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
            elif isinstance(self, MDButton):
                self.state_layer_color = (
                    {
                        "elevated": self.theme_cls.onSurfaceColor[:-1]
                        + [
                            self.button_elevated_opacity_value_disabled_container
                        ],
                        "tonal": self.theme_cls.onSurfaceColor[:-1]
                        + [self.button_tonal_opacity_value_disabled_container],
                        "filled": self.theme_cls.onSurfaceColor[:-1]
                        + [self.button_filled_opacity_value_disabled_container],
                        "outlined": self.theme_cls.onSurfaceColor[:-1]
                        + [
                            self.button_outlined_opacity_value_disabled_container
                        ],
                        "text": self.theme_cls.transparentColor,
                    }[self.style]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
            elif isinstance(self, (MDFabButton, MDExtendedFabButton)):
                self.state_layer_color = (
                    self.theme_cls.onSurfaceColor[:-1]
                    + [self.fab_button_opacity_value_disabled_container]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
            elif isinstance(self, MDTextField):
                if self.mode == "filled":
                    self.state_layer_color = self.theme_cls.onSurfaceColor[
                        :-1
                    ] + [
                        self.text_field_filled_opacity_value_disabled_state_container
                    ]
                else:
                    self.state_layer_color = self.theme_cls.transparentColor
            elif isinstance(self.parent, MDSegmentedButtonItem):
                self.state_layer_color = (
                    self.theme_cls.onSurfaceColor[:-1]
                    + [self.segmented_button_opacity_value_disabled_container]
                    if not self.parent.md_bg_color_disabled
                    else self.parent.md_bg_color_disabled
                )
            elif isinstance(self, MDSwitch):
                self.state_layer_color = (
                    (
                        self.theme_cls.surfaceContainerHighestColor
                        if not self.active
                        else self.theme_cls.onSurfaceColor
                    )[:-1]
                    + [self.switch_opacity_value_disabled_container]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
            elif isinstance(self, BaseListItem):
                self.state_layer_color = (
                    self.theme_cls.onSurfaceColor[:-1]
                    + [self.list_opacity_value_disabled_container]
                    if not self.md_bg_color_disabled
                    else self.md_bg_color_disabled
                )
        elif not value and self._is_already_disabled:
            self.state_layer_color = self.theme_cls.transparentColor
            self._is_already_disabled = False

    def on_enter(self) -> None:
        """Fired when mouse enter the bbox of the widget."""

        self._state = self.state_hover
        self.set_properties_widget()

    def on_leave(self) -> None:
        """Fired when the mouse goes outside the widget border."""

        self._state = 0.0
        self.set_properties_widget()

    def _on_release(self, *args):
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        if platform in ["android", "ios"]:
            self._state = 0.0
            self.set_properties_widget()
        else:
            self.on_enter()

    def _on_press(self, *args):
        """Fired when the button is pressed."""

        self._state = self.state_press
        self.set_properties_widget()

    def _restore_properties(self):
        if self._state == self.state_hover and self.focus_behavior:
            if hasattr(self, "elevation_level"):
                self._elevation_level = self.elevation_level
            if hasattr(self, "shadow_softness"):
                self._shadow_softness = self.shadow_softness
            if hasattr(self, "md_bg_color"):
                self._bg_color = self.md_bg_color
        elif not self._state:
            if hasattr(self, "elevation_level"):
                self.elevation_level = self._elevation_level
            if hasattr(self, "shadow_softness"):
                self.shadow_softness = self._shadow_softness
            if hasattr(self, "bg_color"):
                self.bg_color = self._md_bg_color

    # FIXME:  For some widgets, the color of the state of its elements is
    #  ignored. For example, for the `MDSwitch` widget, the color of the status
    #  of the `Thumb` element and the color of the icon are ignored.
    def _get_target_color(self):
        from kivymd.uix.card import MDCard
        from kivymd.uix.button import (
            MDIconButton,
            MDButton,
            MDFabButton,
            MDExtendedFabButton,
        )
        from kivymd.uix.segmentedbutton.segmentedbutton import (
            MDSegmentedButtonContainer,
        )
        from kivymd.uix.chip import MDChip
        from kivymd.uix.selectioncontrol import MDSwitch, MDCheckbox
        from kivymd.uix.list import BaseListItem
        from kivymd.uix.textfield import MDTextField
        from kivymd.uix.navigationdrawer import MDNavigationDrawerItem

        target_color = None

        if not self.disabled:
            self._restore_properties()

            if isinstance(self, MDTextField):
                if self.mode == "filled":
                    target_color = self.theme_cls.onSurfaceColor
                else:
                    target_color = self.theme_cls.transparentColor
            elif isinstance(self, (MDCard, BaseListItem)) and not isinstance(
                self, MDNavigationDrawerItem
            ):
                target_color = self.theme_cls.onSurfaceColor
            elif isinstance(self, MDNavigationDrawerItem):
                target_color = self.theme_cls.onSecondaryContainerColor
            elif isinstance(self.parent, MDSegmentedButtonContainer):
                target_color = (
                    self.theme_cls.onSurfaceColor
                    if not self.active
                    else self.theme_cls.onSecondaryContainerColor
                )
            elif isinstance(self, MDChip):
                # Here, depending on the widget state (focus/pressed...)
                # we set the target color of the widget's layer.
                # For example:
                #
                #     if self._state == self.state_press:
                #         target_color = [., ., ., .]
                #     else:
                #         ...
                if self.type == "assist":
                    target_color = self.theme_cls.onSurfaceColor
                elif self.type in ["filter", "input", "suggestion"]:
                    target_color = self.theme_cls.onSurfaceVariantColor
            elif isinstance(self, MDIconButton):
                if self.style == "filled":
                    target_color = self.theme_cls.onPrimaryColor
                elif self.style == "tonal":
                    target_color = self.theme_cls.onSecondaryContainerColor
                elif self.style in ["outlined", "standard"]:
                    target_color = self.theme_cls.onSurfaceVariantColor
            elif isinstance(self, MDButton):
                target_color = (
                    self.theme_cls.onPrimaryColor
                    if self.style == "filled"
                    else self.theme_cls.primaryColor
                )
            elif isinstance(self, MDCheckbox):
                target_color = (
                    self.theme_cls.primaryColor
                    if self.active
                    else self.theme_cls.onSurfaceColor
                )
            elif isinstance(self, (MDFabButton, MDExtendedFabButton)):
                target_color = self.theme_cls.onPrimaryContainerColor
            elif isinstance(self, MDSwitch):
                target_color = (
                    self.theme_cls.primaryColor
                    if self.active
                    else self.theme_cls.onSurfaceVariantColor
                )
            else:
                target_color = self.theme_cls.onSurfaceColor

        return target_color

    def _set_state_layer_color(self):
        from kivymd.uix.card import MDCard
        from kivymd.uix.button import (
            MDIconButton,
            MDButton,
            MDFabButton,
            MDExtendedFabButton,
        )
        from kivymd.uix.segmentedbutton.segmentedbutton import (
            MDSegmentedButtonContainer,
        )
        from kivymd.uix.chip import MDChip
        from kivymd.uix.selectioncontrol import MDSwitch, MDCheckbox
        from kivymd.uix.list import BaseListItem
        from kivymd.uix.textfield import MDTextField
        from kivymd.uix.tab.tab import MDTabsItemBase

        target_color = self._get_target_color()
        if (
            isinstance(
                self,
                (
                    MDCard,
                    MDTextField,
                    MDIconButton,
                    MDButton,
                    MDFabButton,
                    MDExtendedFabButton,
                    MDChip,
                    MDSwitch,
                    MDCheckbox,
                    BaseListItem,
                    MDTabsItemBase,
                ),
            )
            or isinstance(self.parent, MDSegmentedButtonContainer)
            and target_color
        ):
            if self._state == self.state_hover and self.focus_behavior:
                if (
                    not self.focus_color
                    or self.theme_cls.dynamic_color
                    and self.theme_focus_color == "Primary"
                ):
                    if (
                        isinstance(self, MDTextField)
                        and self.mode == "outlined"
                    ):
                        self.state_layer_color = target_color
                    else:
                        self.state_layer_color = target_color[:-1] + [
                            self._state
                        ]
                else:
                    self.state_layer_color = self.focus_color
            elif self._state == self.state_press:
                self.state_layer_color = target_color[:-1] + [self._state]
            elif not self._state:
                self.state_layer_color = target_color[:-1] + [self._state]
