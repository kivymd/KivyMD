"""
Components/Dynamic color
========================

.. seealso::

    `Material Design spec, Dynamic color
    <https://m3.material.io/styles/color/dynamic-color/overview>`_

.. rubric:: Dynamic color can create accessible UI color schemes based on
    content or user settings

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dynamic-color.png
    :align: center

Dynamic color experiences are built with M3 color schemes. Beginning with
Android 12, users can generate individualized schemes through wallpaper
selection and other customization settings. With M3 as a foundation,
user-generated colors can coexist with app colors, putting a range of
customizable visual experiences in the hands of users.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dynamic-color-preview.png
    :align: center

1. Baseline scheme
2. Colors extracted from a wallpaper
3. Colors extracted from content

Example of dynamic color from the list of standard color schemes
----------------------------------------------------------------

.. code-block:: python

    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.properties import StringProperty, ColorProperty
    from kivy.uix.boxlayout import BoxLayout
    from kivy.utils import hex_colormap

    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.app import MDApp


    KV = '''
    <ColorCard>
        orientation: "vertical"

        MDLabel:
            text: root.text
            color: "grey"
            adaptive_height: True

        MDCard:
            theme_bg_color: "Custom"
            md_bg_color: root.bg_color


    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor

        MDIconButton:
            on_release: app.open_menu(self)
            pos_hint: {"top": .98}
            x: "12dp"
            icon: "menu"

        MDRecycleView:
            id: card_list
            viewclass: "ColorCard"
            bar_width: 0
            size_hint_y: None
            height: root.height - dp(68)

            RecycleGridLayout:
                cols: 3
                spacing: "16dp"
                padding: "16dp"
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
    '''


    class ColorCard(BoxLayout):
        text = StringProperty()
        bg_color = ColorProperty()


    class Example(MDApp):
        menu: MDDropdownMenu = None

        def build(self):
            self.theme_cls.dynamic_color = True
            return Builder.load_string(KV)

        def get_instance_from_menu(self, name_item):
            index = 0
            rv = self.menu.ids.md_menu
            opts = rv.layout_manager.view_opts
            datas = rv.data[0]

            for data in rv.data:
                if data["text"] == name_item:
                    index = rv.data.index(data)
                    break

            instance = rv.view_adapter.get_view(
                index, datas, opts[index]["viewclass"]
            )

            return instance

        def open_menu(self, menu_button):
            menu_items = []
            for item, method in {
                "Set palette": lambda: self.set_palette(),
                "Switch theme style": lambda: self.theme_switch(),
            }.items():
                menu_items.append({"text": item, "on_release": method})
            self.menu = MDDropdownMenu(
                caller=menu_button,
                items=menu_items,
            )
            self.menu.open()

        def set_palette(self):
            instance_from_menu = self.get_instance_from_menu("Set palette")
            available_palettes = [
                name_color.capitalize() for name_color in hex_colormap.keys()
            ]

            menu_items = []
            for name_palette in available_palettes:
                menu_items.append(
                    {
                        "text": name_palette,
                        "on_release": lambda x=name_palette: self.switch_palette(x),
                    }
                )
            MDDropdownMenu(
                caller=instance_from_menu,
                items=menu_items,
            ).open()

        def switch_palette(self, selected_palette):
            self.theme_cls.primary_palette = selected_palette
            Clock.schedule_once(self.generate_cards, 0.5)

        def theme_switch(self) -> None:
            self.theme_cls.switch_theme()
            Clock.schedule_once(self.generate_cards, 0.5)

        def generate_cards(self, *args):
            self.root.ids.card_list.data = []
            for color in self.theme_cls.dynamic_color_names:
                self.root.ids.card_list.data.append(
                    {
                        "bg_color": getattr(self.theme_cls, color),
                        "text": color,
                    }
                )

        def on_start(self):
            Clock.schedule_once(self.generate_cards)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dynamic-color.gif
    :align: center

Example of a dynamic color from an image
----------------------------------------

.. seealso::

     :attr:`kivymd.theming.ThemeManager.path_to_wallpaper`

.. code-block:: python

    import os

    from kivy.clock import Clock
    from kivy.core.window import Window
    from kivy.core.window.window_sdl2 import WindowSDL
    from kivy.lang import Builder
    from kivy.properties import StringProperty, ColorProperty

    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.app import MDApp


    KV = '''
    <ColorCard>
        orientation: "vertical"

        MDLabel:
            text: root.text
            color: "grey"
            adaptive_height: True

        MDCard:
            theme_bg_color: "Custom"
            md_bg_color: root.bg_color


    MDScreen:
        md_bg_color: app.theme_cls.backgroundColor

        MDRecycleView:
            id: card_list
            viewclass: "ColorCard"
            bar_width: 0

            RecycleGridLayout:
                cols: 3
                spacing: "16dp"
                padding: "16dp"
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
    '''


    class ColorCard(MDBoxLayout):
        text = StringProperty()
        bg_color = ColorProperty()


    class Example(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Window.bind(on_dropfile=self.on_drop_file)

        def on_drop_file(self, sdl: WindowSDL, path_to_file: str) -> None:
            ext = os.path.splitext(path_to_file)[1]
            if isinstance(path_to_file, bytes):
                path_to_file = path_to_file.decode()
            if isinstance(ext, bytes):
                ext = ext.decode()
            if ext in [".png", ".jpg"]:
                self.theme_cls.path_to_wallpaper = path_to_file
                Clock.schedule_once(self.generate_cards, 0.5)

        def build(self):
            self.theme_cls.dynamic_color = True
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def theme_switch(self) -> None:
            self.theme_cls.switch_theme()
            Clock.schedule_once(self.generate_cards, 0.5)

        def generate_cards(self, *args):
            self.root.ids.card_list.data = []
            for color in self.theme_cls.dynamic_color_names:
                self.root.ids.card_list.data.append(
                    {
                        "bg_color": getattr(self.theme_cls, color),
                        "text": color,
                    }
                )

        def on_start(self):
            Clock.schedule_once(self.generate_cards)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/dynamic-color-path-to_wallpapper.gif
    :align: center
"""

from kivy.properties import ColorProperty


class DynamicColor:
    """
    Dynamic color class.

    .. versionadded:: 2.0.0
    """

    # Primary.
    primaryColor = ColorProperty()
    """
    Primary color.

    :attr:`primaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    primaryContainerColor = ColorProperty()
    """
    Primary container color.

    :attr:`primaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Primary.
    onPrimaryColor = ColorProperty()
    """
    On primary color.

    :attr:`onPrimaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onPrimaryContainerColor = ColorProperty()
    """
    On primary container color.

    :attr:`onPrimaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Secondary.
    secondaryColor = ColorProperty()
    """
    Secondary color.

    :attr:`secondaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    secondaryContainerColor = ColorProperty()
    """
    Secondary container color.

    :attr:`secondaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Secondary.
    onSecondaryColor = ColorProperty()
    """
    On secondary color.

    :attr:`onSecondaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onSecondaryContainerColor = ColorProperty()
    """
    On secondary container color.

    :attr:`onSecondaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Tertiary.
    tertiaryColor = ColorProperty()
    """
    Tertiary color.

    :attr:`tertiaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    tertiaryContainerColor = ColorProperty()
    """
    Tertiary container color.

    :attr:`tertiaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Tertiary.
    onTertiaryColor = ColorProperty()
    """
    On tertiary color.

    :attr:`onTertiaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onTertiaryContainerColor = ColorProperty()
    """
    On tertiary container color.

    :attr:`onTertiaryContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Surface.
    surfaceColor = ColorProperty()
    """
    Surface color.

    :attr:`surfaceColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceDimColor = ColorProperty()
    """
    Surface dim color.

    :attr:`surfaceDimColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceBrightColor = ColorProperty()
    """
    Surface bright color.

    :attr:`surfaceBrightColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceContainerLowestColor = ColorProperty()
    """
    Surface container lowest color.

    :attr:`surfaceContainerLowestColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceContainerLowColor = ColorProperty()
    """
    Surface container low color.

    :attr:`surfaceContainerLowColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceContainerColor = ColorProperty()
    """
    Surface container color.

    :attr:`surfaceContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceContainerHighColor = ColorProperty()
    """
    Surface container high color.

    :attr:`surfaceContainerHighColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceContainerHighestColor = ColorProperty()
    """
    Surface container highest color.

    :attr:`surfaceContainerHighestColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceVariantColor = ColorProperty()
    """
    Surface variant color.

    :attr:`surfaceVariantColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    surfaceTintColor = ColorProperty()
    """
    Surface tint color.

    :attr:`surfaceTintColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Surface.
    onSurfaceColor = ColorProperty()
    """
    On surface color.

    :attr:`onSurfaceColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onSurfaceLightColor = ColorProperty()
    """
    On surface light color.

    :attr:`onSurfaceLightColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onSurfaceVariantColor = ColorProperty()
    """
    On surface variant color.

    :attr:`onSurfaceVariantColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Inverse.
    inverseSurfaceColor = ColorProperty()
    """
    Inverse surface color.

    :attr:`inverseSurfaceColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    inverseOnSurfaceColor = ColorProperty()
    """
    Inverse on surface color.

    :attr:`inverseOnSurfaceColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    inversePrimaryColor = ColorProperty()
    """
    Inverse primary color.

    :attr:`inversePrimaryColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Background.
    backgroundColor = ColorProperty()
    """
    Background color.

    :attr:`backgroundColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Background.
    onBackgroundColor = ColorProperty()
    """
    On background color.

    :attr:`onBackgroundColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Error.
    errorColor = ColorProperty()
    """
    Error color.

    :attr:`errorColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    errorContainerColor = ColorProperty()
    """
    Error container color.

    :attr:`errorContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # On Error.
    onErrorColor = ColorProperty()
    """
    On error color.

    :attr:`onErrorColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    onErrorContainerColor = ColorProperty()
    """
    On error container color.

    :attr:`onErrorContainerColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Outline.
    outlineColor = ColorProperty()
    """
    Outline color.

    :attr:`outlineColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    outlineVariantColor = ColorProperty()
    """
    Outline variant color.

    :attr:`outlineVariantColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Shadow/scrim.
    shadowColor = ColorProperty()
    """
    Shadow color.

    :attr:`shadowColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    scrimColor = ColorProperty()
    """
    Scrim color.

    :attr:`scrimColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Disabled.
    disabledTextColor = ColorProperty()
    """
    Disabled text color.

    :attr:`disabledTextColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    # Transparent.
    transparentColor = ColorProperty([0, 0, 0, 0])
    """
    Transparent color.

    :attr:`transparentColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    # Ripple.
    rippleColor = ColorProperty("#BDBDBD")
    """
    Ripple color.

    :attr:`rippleColor` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `'#BDBDBD'`.
    """
