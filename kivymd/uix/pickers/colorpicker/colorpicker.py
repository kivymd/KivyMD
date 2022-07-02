"""
Components/ColorPicker
======================

.. versionadded:: 1.0.0

.. rubric:: Create, share, and apply color palettes to your UI, as well as measure the accessibility level of any color combination..

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/color-picker-preview.png
    :align: center

Usage
-----

.. code-block:: python

    from typing import Union

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.pickers import MDColorPicker

    KV = '''
    MDScreen:

        MDTopAppBar:
            id: toolbar
            title: "MDTopAppBar"
            pos_hint: {"top": 1}

        MDRaisedButton:
            text: "OPEN PICKER"
            pos_hint: {"center_x": .5, "center_y": .5}
            md_bg_color: toolbar.md_bg_color
            on_release: app.open_color_picker()
    '''


    class MyApp(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def open_color_picker(self):
            color_picker = MDColorPicker(size_hint=(0.45, 0.85))
            color_picker.open()
            color_picker.bind(
                on_select_color=self.on_select_color,
                on_release=self.get_selected_color,
            )

        def update_color(self, color: list) -> None:
            self.root.ids.toolbar.md_bg_color = color

        def get_selected_color(
            self,
            instance_color_picker: MDColorPicker,
            type_color: str,
            selected_color: Union[list, str],
        ):
            '''Return selected color.'''

            print(f"Selected color is {selected_color}")
            self.update_color(selected_color[:-1] + [1])

        def on_select_color(self, instance_gradient_tab, color: list) -> None:
            '''Called when a gradient image is clicked.'''


    MyApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/color-picker-usage.png
    :align: center
"""

import os
import struct
from io import BytesIO
from typing import List, Union

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.graphics import RoundedRectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex, get_hex_from_color
from PIL import Image as PilImage
from PIL import ImageDraw

from kivymd import uix_path
from kivymd.color_definitions import colors as _colors
from kivymd.color_definitions import text_colors
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.tab import MDTabs, MDTabsBase, MDTabsLabel

__all__ = ("MDColorPicker",)

with open(
    os.path.join(uix_path, "pickers", "colorpicker", "colorpicker.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class TypeColorButton(MDRaisedButton, MDToggleButton):
    """
    The class implements the button to switch the color type -
    'RGBA', 'HEX', 'RGB'.
    """

    theme_text_color = "Custom"
    text_color = (0, 0, 0, 1)
    elevation = 0


class SelectAlphaChannelWidget(MDBoxLayout):
    """
    The class implements the widget with the current color and slider to set
    the value of the transparency of the selected color.
    """

    # :class:`~kivymd.uix.colorpicker.MDColorPicker` class.
    color_picker = ObjectProperty()

    # The `RGB` value for the transparency preview widget of the selected
    # color.
    _rgb = ColorProperty([0, 0, 0, 0])
    # The opacity value for the transparency preview widget of the selected
    # color.
    _opacity_value_selected_color = NumericProperty(1)

    def on_color_picker(
        self, instance_select_alpha_channel_widget, instance_color_picker
    ) -> None:
        instance_color_picker.bind(_rgb=self.set_scale_rgb)

    def set_scale_rgb(
        self,
        instance_color_picker,
        color: Union[List[int], List[float]],
    ) -> None:
        if color[0] > 1:
            self._rgb = [x / 255.0 for x in color]
        else:
            self._rgb = color


class SliderTab(MDBoxLayout):
    """
    The class has implemented `RGB` value sliders and a scale for setting the
    transparency value of the selected color. This is the third tab on the
    bottom navigation panel.
    """

    # :class:`~kivymd.uix.colorpicker.MDColorPicker` class.
    color_picker = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_slide_value")

    def get_color(self) -> List[float]:
        return [
            self.ids.slider_red.ids.slider.value / 255,
            self.ids.slider_green.ids.slider.value / 255,
            self.ids.slider_blue.ids.slider.value / 255,
            self.color_picker._opacity_value_selected_color,
        ]

    def on_slide_value(self, *args) -> None:
        """Basic event handler for changing the slider value."""


class GradientTab(ThemableBehavior, MDBoxLayout):
    """
    The class implements a tab with a gradient, a color selection scale and
    a scale for setting the transparency value of the selected color.
    This is the first tab on the bottom navigation panel.
    """

    # :class:`~kivymd.uix.colorpicker.MDColorPicker` class.
    color_picker = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rectangle = None
        self.texture = None
        Clock.schedule_once(lambda x: self.create_gradient_texture())
        Clock.schedule_once(self.create_canvas_with_gradient_texture)

    def create_gradient_texture(
        self, r_g_b=None, interval: Union[int, float] = 0
    ) -> None:
        """
        Creates a gradient value buffer and texture object.
        Called when clicking on the gradient bar to the right.
        """

        # TODO: Perhaps there is a better way to create a gradient.
        #  The implementation using the PIL package is most likely not the most
        #  better. In any case, performance tests should be carried out.
        gradient_widget_width = int(self.ids.gradient_widget.width)
        gradient_widget_height = int(self.ids.gradient_widget.height - dp(100))
        img = PilImage.new(
            "RGBA", (gradient_widget_width, gradient_widget_height), "#FFFFFF"
        )
        draw = ImageDraw.Draw(img)

        if not self.color_picker.default_color:
            r, g, b = (
                r_g_b
                if r_g_b
                else self.color_picker.get_rgb(self.theme_cls.primary_color)
            )
        else:
            r, g, b = [
                int(value * 255)
                for value in self.color_picker.default_color[:-1]
            ]
        self.color_picker._rgb = [r, g, b]
        (
            r_adjacent_color_constant,
            g_adjacent_color_constant,
            b_adjacent_color_constant,
        ) = (
            self.color_picker.adjacent_color_constants
            if r_g_b != (0, 0, 0)
            else (0.40, 0.40, 0.40)  # if the selected color is black
        )

        for i in range(gradient_widget_width):
            r, g, b = (
                r + r_adjacent_color_constant,
                g + g_adjacent_color_constant,
                b + b_adjacent_color_constant,
            )
            draw.line(
                (i, 0, i, gradient_widget_width), fill=(int(r), int(g), int(b))
            )

        data = BytesIO()
        img.save(data, format="png")
        data.seek(0)
        self.texture = CoreImage(BytesIO(data.read()), ext="png").texture

    def create_canvas_with_gradient_texture(
        self, interval: Union[int, float]
    ) -> None:
        """Creates a canvas with a gradient texture."""

        with self.ids.color_selection_box.canvas:
            self.rectangle = RoundedRectangle(
                texture=self.texture,
                pos=self.ids.gradient_widget.pos,
                size=self.ids.gradient_widget.size,
                radius=self.color_picker.radius,
                group="gradient",
            )
            self.bind(
                size=lambda instance, size: Clock.schedule_once(
                    lambda dt: self._update_canvas(instance, size)
                )
            )

    def get_rgba_color_from_touch_region(self, widget, touch) -> List[int]:
        """
        Returns the color of the pixel in the gradient that was clicked.
        """

        pixel = widget.texture.get_region(*touch.pos, 1, 1)
        rgba = struct.unpack("4B", pixel.pixels)
        return rgba

    def updated_canvas(self, widget, touch, color=None) -> None:
        """
        Called when clicking on the gradient bar to the right.
        Updates the color of the gradient texture.
        """

        if self.color_picker.default_color:
            self.color_picker.default_color = None

        self.ids.color_selection_box.canvas.remove_group("gradient")
        if not color:
            # (0-255, 0-255, 0-255, 0-255)
            color = self.get_rgba_color_from_touch_region(widget, touch)
            self.create_gradient_texture(color[:-1])
            self.color_picker.dispatch(
                "on_select_color", [x / 255.0 for x in color]
            )
        else:
            self.create_gradient_texture(color)
        self.create_canvas_with_gradient_texture(0)

    def on_touch_down(self, touch):
        """Handles the ``self.ids.gradient_widget`` touch event."""

        if self.ids.gradient_widget.collide_point(*touch.pos):
            color = self.get_rgba_color_from_touch_region(self, touch)
            self.color_picker.dispatch(
                "on_select_color", [x / 255.0 for x in color]
            )
        return super().on_touch_down(touch)

    def _update_canvas(self, instance_gradient_widget, size: list) -> None:
        self.rectangle.size = self.ids.gradient_widget.size
        self.rectangle.pos = self.ids.gradient_widget.pos


class TabColorList(MDBoxLayout, MDTabsBase):
    """Implements a tab for :class:`~ColorListTab` class."""


class ColorListTab(MDTabs):
    """
    The class implements a tab with tabs with a list of colors.
    This is the second tab on the bottom navigation panel.
    """

    # :class:`~kivymd.uix.colorpicker.MDColorPicker` class.
    color_picker = ObjectProperty()

    def generates_list_colors(
        self,
        instance_color_list_tab,
        instance_tab_color_list: TabColorList,
        instance_tabs_label: MDTabsLabel,
        tab_label_text: str,
    ) -> None:
        """
        Generates list of colors.
        Called when you click the tab of :class:`~TabColorList` class.
        """

        if not tab_label_text:
            tab_label_text = "Red"
        if not instance_tab_color_list.rv.data:
            for hue in _colors[tab_label_text]:
                color = get_color_from_hex(_colors[tab_label_text][hue])
                if tab_label_text == "Light":
                    text_color = (0, 0, 0, 1)
                elif tab_label_text == "Dark":
                    text_color = (1, 1, 1, 1)
                else:
                    text_color = text_colors[tab_label_text][hue]
                instance_tab_color_list.rv.data.append(
                    {
                        "viewclass": "ColorListItem",
                        "color": color,
                        "hue_code": hue,
                        "text_color": text_color,
                        "on_press": lambda x=color: self.on_press_color_item(x),
                    }
                )

    def on_press_color_item(self, color: list) -> None:
        """Called when you click on the color item from the list of colors."""

        rgb = [int(value * 255) for value in color[:-1]]
        self.color_picker._rgb = rgb
        self.background_color = color
        self.color_picker.dispatch("on_select_color", color)


class ColorListItem(RectangularRippleBehavior, ButtonBehavior, MDBoxLayout):
    """Implements the item for the list of :class:`~TabColorList` class."""

    color = ColorProperty()
    text_color = ColorProperty()
    hue_code = StringProperty()


class MDColorPicker(BaseDialog):
    adjacent_color_constants = ListProperty([0.299, 0.887, 0.411])
    """
    A list of values that are used to create the gradient. These values are
    selected empirically. Each of these values will be added to the selected
    ``RGB`` value, thus creating colors that are close in value.

    :attr:`adjacent_color_constants` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0.299, 0.887, 0.411]`.
    """

    default_color = ColorProperty(None, allownone=True)
    """
    Default color value The set color value will be used when you open the
    dialog.

    :attr:`default_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    type_color = OptionProperty("RGB", options=["RGBA", "HEX", "RGB"])
    """
    Type of color.
    Available options are: `'RGBA'`, `'HEX'`, `'RGB'`.

    :attr:`type_color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'RGB'`.
    """

    background_down_button_selected_type_color = ColorProperty([1, 1, 1, 0.3])
    """
    Button background for choosing a color type ('RGBA', 'HEX', 'HSL', 'RGB').

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/color-picker-background-down-button-selected-type-color.png
        :align: center

    :attr:`background_down_button_selected_type_color` is an
    :class:`~kivy.properties.ColorProperty` and defaults to `[1, 1, 1, 0.3]`.
    """

    radius_color_scale = VariableListProperty([8])
    """
    The radius value for the color scale.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/color-picker-gradient-scale-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[8, 8, 8, 8]`.
    """

    text_button_ok = StringProperty("SELECT")
    """
    Color selection button text.

    :attr:`text_button_ok` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'SELECT'`.
    """

    text_button_cancel = StringProperty("CANCEL")
    """
    Cancel button text.

    :attr:`text_button_cancel` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'CANCEL'`.
    """

    selected_color = None
    # One of the objects of classes:
    # :class:`~GradientTab`, :class:`~ColorListTab`, :class:`~SliderTab`.
    _current_tab = ObjectProperty()
    # The `RGB` value for the transparency preview widget of the selected
    # color.
    _rgb = ListProperty()
    # The opacity value for the transparency preview widget of the selected
    # color.
    _opacity_value_selected_color = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gradient_tab = None
        self.register_event_type("on_select_color")
        self.register_event_type("on_switch_tabs")
        self.register_event_type("on_release")
        self.on_background_down_button_selected_type_color(
            None, self.background_down_button_selected_type_color
        )

        self.on_background_down_button_selected_type_color(
            None, self.background_down_button_selected_type_color
        )
        Clock.schedule_once(lambda x: self.on_type_color(self), 1)

    def update_color_slider_item_bottom_navigation(self, color: list) -> None:
        """
        Updates the color of the slider that sets the transparency value of the
        selected color and the color of bottom navigation items.
        """

        if "select_alpha_channel_widget" in self._current_tab.ids:
            self._current_tab.ids.select_alpha_channel_widget.ids.slider.color = (
                color
            )
        self.ids.bottom_navigation.text_color_active = color

    def update_color_type_buttons(self, color: list) -> None:
        """
        Updating button colors (display buttons of type of color) to match the
        selected color.
        """

        for instance_toggle_button in self.ids.type_color_button_box.children:
            if instance_toggle_button.state != "down":
                instance_toggle_button.md_bg_color = color
            instance_toggle_button.background_normal = color

    def get_rgb(self, color: list) -> list:
        """Returns an ``RGB`` list of values from 0 to 255."""

        return [
            int(value * 255)
            for value in (color[:-1] if len(color) == 4 else color)
        ]

    def on_background_down_button_selected_type_color(
        self, instance_color_picker, color: list
    ) -> None:
        def set_background_down(interval: Union[float, int]) -> None:
            for (
                instance_toggle_button
            ) in self.ids.type_color_button_box.children:
                instance_toggle_button.background_down = color
                if self.type_color == instance_toggle_button.text:
                    instance_toggle_button.state = "down"

        Clock.schedule_once(set_background_down)

    def on_type_color(
        self,
        instance_color_picker,
        type_color: str = "",
        interval: Union[float, int] = 0,
    ) -> None:
        """Called when buttons are clicked to set the color type."""

        if not type_color:
            type_color = self.type_color

        if self._rgb:
            rgb = self._rgb if self._rgb[0] > 1 else self.get_rgb(self._rgb)
            opacity = self._opacity_value_selected_color
            color = ""

            if type_color == "RGB":
                self.selected_color = [value for value in rgb]
                color = f"RGB({', '.join([str(value) for value in self.selected_color])})"
            elif type_color == "RGBA":
                self.selected_color = [x / 255.0 for x in rgb] + [opacity]
                color = f"RGBA({', '.join([str(x / 255.0) for x in rgb])}, {opacity})"
            elif type_color == "HEX":
                self.selected_color = get_hex_from_color(
                    [x / 255.0 for x in rgb] + [opacity]
                )
                color = f"HEX({self.selected_color})"

            self.ids.lbl_color_value.text = color

    def on_open(self) -> None:
        """Default open event handler."""

        if not self.ids.bottom_navigation_gradient.children:
            self.gradient_tab = GradientTab(color_picker=self)
            self._current_tab = self.gradient_tab
            self.ids.bottom_navigation_gradient.add_widget(self.gradient_tab)

    def on_select_color(self, color: list) -> None:
        """Called when a gradient image is clicked."""

        if len(color) == 3:
            color += [self._opacity_value_selected_color]

        self.ids.header.md_bg_color = color
        self._rgb = color[:-1]
        self.on_type_color(self, self.type_color)
        self.update_color_type_buttons(color)
        self.update_color_slider_item_bottom_navigation(color)

    def on_switch_tabs(
        self,
        bottom_navigation_instance,
        bottom_navigation_item_instance,
        name_tab,
    ) -> None:
        """Called when switching tabs of bottom navigation."""

        if name_tab == "bottom navigation gradient":
            self._current_tab = self.gradient_tab
            bottom_navigation_item_instance.children[0].updated_canvas(
                None,
                None,
                self._rgb if self._rgb[0] > 1 else self.get_rgb(self._rgb),
            )
            instance_slider_tab = (
                bottom_navigation_instance.ids.tab_manager.get_screen(
                    "tune"
                ).children[0]
            )
            select_alpha_channel_widget = (
                self.gradient_tab.ids.select_alpha_channel_widget
            )
            select_alpha_channel_widget.ids.slider.value = (
                instance_slider_tab.ids.select_alpha_channel_widget.ids.slider.value
            )
            select_alpha_channel_widget.ids.slider.color = [
                x / 255.0 for x in self._rgb
            ] + [1]
        elif name_tab == "tune":
            if self._rgb[0] <= 1:
                color = self.get_rgb(self._rgb)
            else:
                color = self._rgb
            instance_slider_tab = self.ids.tune.children[0]
            self._current_tab = instance_slider_tab
            instance_slider_tab.ids.slider_red.ids.slider.value = color[0]
            instance_slider_tab.ids.slider_green.ids.slider.value = color[1]
            instance_slider_tab.ids.slider_blue.ids.slider.value = color[2]
            instance_slider_tab.ids.select_alpha_channel_widget.ids.slider.value = (
                self._opacity_value_selected_color
            )
        elif name_tab == "view headline":
            color = self._rgb + [1]
            color_list_tabs = self.ids.view_headline.children[0]
            self._current_tab = color_list_tabs
            try:
                color_list_tabs.background_color = color
            except ValueError:
                color_list_tabs.background_color = [x / 255.0 for x in color][
                    :-1
                ] + [1]
            if not color_list_tabs.get_tab_list():
                for color in _colors.keys():
                    tab_widget = TabColorList(title=str(color))
                    color_list_tabs.add_widget(tab_widget)

    def on_release(self, *args):
        """Called when the `SELECT` button is pressed"""

    def _get_selected_color(self, selected_color: Union[list, str]) -> list:
        """
        Convert [0-255, 0-255, 0-255] and '#rrggbb' to kivy color format.
        Return kivy color format.
        """

        rgba = [0, 0, 0, 0]
        if isinstance(selected_color, list):
            if selected_color[0] > 1:
                rgba = [x / 255.0 for x in selected_color] + [
                    self._opacity_value_selected_color
                ]
            else:
                rgba = selected_color
        elif isinstance(selected_color, str):
            rgba = get_color_from_hex(selected_color)[:-1] + [
                self._opacity_value_selected_color
            ]
        return rgba
