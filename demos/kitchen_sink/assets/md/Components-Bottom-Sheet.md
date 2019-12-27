![bottomsheet.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/bottomsheet.gif)

## Example of using MDBottomSheet:

```python
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.uix.bottomsheet import (
    MDCustomBottomSheet,
    MDGridBottomSheet,
    MDListBottomSheet,
)

Builder.load_string(
    '''
#:import Window kivy.core.window.Window
#:import get_hex_from_color kivy.utils.get_hex_from_color


<ContentForPopupScreen@BoxLayout>
    id: box
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {'top': 1}

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:

        MDRoundFlatButton:
            text: "Free call"
            on_press: app.callback_for_menu_items(self.text)
            md_bg_color: 1, 1, 1, .4
            text_color: app.theme_cls.bg_dark

        Widget:

        MDRoundFlatButton:
            text: "Free message"
            on_press: app.callback_for_menu_items(self.text)
            md_bg_color: 1, 1, 1, .4
            text_color: app.theme_cls.bg_dark

        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: app.callback_for_menu_items(self.text)

        IconLeftWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: app.callback_for_menu_items(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color([0, 0, 0, .5])

        IconLeftWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: app.callback_for_menu_items(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color([0, 0, 0, .5])

        IconLeftWidget:
            icon: 'remote'


<BoxContentForBottomSheetCustomScreenList>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {'top': 1}

    ScrollView:

        GridLayout:
            id: box
            size_hint_y: None
            height: self.minimum_height
            cols: 1


<ContentForBottomSheetCustomScreenList@TwoLineIconListItem>
    text: "Call over mobile network"
    on_press: app.callback_for_menu_items(self.text)
    secondary_text:
        "[color=%s]Operator's tariffs apply[/color]" \
        % get_hex_from_color([0, 0, 0, .5])

    IconLeftWidget:
        icon: 'remote'


<CustomItemButton@AnchorLayout>
    size_hint_y: None
    height: "32dp"
    anchor_x: "center"
    text: ""
    callback: None

    MDRaisedButton:
        text: root.text
        on_release: root.callback()


<BottomSheet@Screen>
    name: 'bottom sheet'

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)

        MDToolbar:
            title: 'Example BottomSheet'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: x]]
            background_palette: 'Primary'

        ScrollView:

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: "20dp"
                padding: "20dp"
                cols: 1

                CustomItemButton:
                    text: "Open custom bottom sheet"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom")

                CustomItemButton:
                    text: "Open custom bottom sheet with list"
                    callback: lambda: app.show_example_custom_bottom_sheet("list")

                CustomItemButton:
                    text: "Open list bottom sheet"
                    callback: lambda: app.show_example_bottom_sheet()

                CustomItemButton:
                    text: "Open grid bottom sheet"
                    callback: lambda: app.show_example_grid_bottom_sheet()

                Widget:
                    size_hint_y: None
                    height: "5dp"

                MDLabel:
                    text: "MDBottomSheet corners"
                    halign: "center"
                    font_style: "H6"

                MDSeparator:

                CustomItemButton:
                    text: "Corner 'top_left'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "top_left")

                CustomItemButton:
                    text: "Corner 'top_right'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "top_right")

                CustomItemButton:
                    text: "Corners 'top'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "top")

                CustomItemButton:
                    text: "Corner 'bottom_left'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "bottom_left")

                CustomItemButton:
                    text: "Corner 'bottom_right'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "bottom_right")

                CustomItemButton:
                    text: "Corners 'bottom'"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", "bottom")

                Widget:
                    size_hint_y: None
                    height: "5dp"

                MDLabel:
                    text: "MDBottomSheet without animation opening"
                    halign: "center"
                    font_style: "H6"

                MDSeparator:

                CustomItemButton:
                    text: "MDBottomSheet without animation opening"
                    callback: lambda: app.show_example_custom_bottom_sheet("custom", None, False)
'''
)


class BoxContentForBottomSheetCustomScreenList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(10):
            self.ids.box.add_widget(
                Factory.ContentForBottomSheetCustomScreenList()
            )


class Example(App):
    theme_cls = ThemeManager()

    def build(self):
        return Factory.BottomSheet()

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_custom_bottom_sheet(
            self, type, corner=None, animation=True
    ):
        """Show menu from the screen BottomSheet."""

        if type == "custom":
            custom_screen_for_bottom_sheet = Factory.ContentForPopupScreen()
        elif type == "list":
            custom_screen_for_bottom_sheet = (
                BoxContentForBottomSheetCustomScreenList()
            )

        MDCustomBottomSheet(
            screen=custom_screen_for_bottom_sheet,
            bg_color=[0.2, 0.2, 0.2, 1],
            animation=animation,
            radius_from=corner,
        ).open()

    def show_example_bottom_sheet(self):
        bs_menu = MDListBottomSheet()
        bs_menu.add_item(
            "Here's an item with text only",
            lambda x: self.callback_for_menu_items(
                "Here's an item with text only"
            ),
        )
        bs_menu.add_item(
            "Here's an item with an icon",
            lambda x: self.callback_for_menu_items(
                "Here's an item with an icon"
            ),
            icon="clipboard-account",
        )
        bs_menu.add_item(
            "Here's another!",
            lambda x: self.callback_for_menu_items("Here's another!"),
            icon="nfc",
        )
        bs_menu.open()

    def show_example_grid_bottom_sheet(self):
        bs_menu = MDGridBottomSheet()
        bs_menu.add_item(
            "Facebook",
            lambda x: self.callback_for_menu_items("Facebook"),
            icon_src="demos/kitchen_sink/assets/facebook-box.png",
        )
        bs_menu.add_item(
            "YouTube",
            lambda x: self.callback_for_menu_items("YouTube"),
            icon_src="demos/kitchen_sink/assets/youtube-play.png",
        )
        bs_menu.add_item(
            "Twitter",
            lambda x: self.callback_for_menu_items("Twitter"),
            icon_src="demos/kitchen_sink/assets/twitter.png",
        )
        bs_menu.add_item(
            "Da Cloud",
            lambda x: self.callback_for_menu_items("Da Cloud"),
            icon_src="demos/kitchen_sink/assets/cloud-upload.png",
        )
        bs_menu.add_item(
            "Camera",
            lambda x: self.callback_for_menu_items("Camera"),
            icon_src="demos/kitchen_sink/assets/camera.png",
        )
        bs_menu.open()


Example().run()
```