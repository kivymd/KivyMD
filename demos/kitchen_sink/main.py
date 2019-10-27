"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os
import sys
import webbrowser

from kivy.effects.scroll import ScrollEffect
from kivy.uix.scrollview import ScrollView

if getattr(sys, "frozen", False):  # Bundle mode with PyInstaller
    os.environ["KITCHEN_SINK_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["KITCHEN_SINK_ROOT"] = os.path.dirname(os.path.abspath(__file__))
os.environ["KITCHEN_SINK_ASSETS"] = os.path.join(
    os.environ["KITCHEN_SINK_ROOT"], f"assets{os.sep}"
)

from kivy.factory import Factory
from kivy.metrics import dp, sp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

Window.softinput_mode = "below_target"

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color
from kivy import platform

from screens import Screens
from dialogs import DialogLoadKvFiles

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.fanscreenmanager import MDFanScreen
from kivymd.uix.list import (
    IRightBodyTouch,
    OneLineIconListItem,
    ThreeLineRightIconListItem,
)
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.card import MDCard
from kivymd.utils.cropimage import crop_image
from kivymd.utils import asynckivy
from kivymd.theming import ThemeManager
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.icon_definitions import md_icons


def toast(text):
    from kivymd.toast.kivytoast import toast

    toast(text)


main_widget_kv = """
#:import Window kivy.core.window.Window
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import images_path kivymd.images_path
#:import environ os.environ

# FIXME: if you remove the import of this class,
#        an error is returned when using the `MDMenu` example
#        NameError: name 'MDDropdownMenu' is not defined
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu


<ShrinePresplashTile@Label>
    color: app.theme_cls.text_color
    font_size: "24sp"
    size_hint_y: None
    height: self.texture_size[1]


<ContentPopup@BoxLayout>
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: f'{environ["KITCHEN_SINK_ASSETS"]}guitar-1139397_1280_crop.png'
        size_hint: 1, None
        height: dp(Window.height * 35 // 100)
        allow_stretch: True
        keep_ratio: False

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5}
        on_release: root.parent.show()

    Widget:


<ContentForAnimCard>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:

        MDRoundFlatButton:
            text: "Free call"
            on_press: root.callback(self.text)

        Widget:

        MDRoundFlatButton:
            text: "Free message"
            on_press: root.callback(self.text)

        Widget:

    OneLineIconListItem:
        text: "Video call"
        on_press: root.callback(self.text)

        IconLeftWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        # FIXME: Don't work "secondary_text_color" parameter
        # secondary_text_color: app.theme_cls.primary_color

        IconLeftWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)

        IconLeftWidget:
            icon: 'remote'


<ContentNavigationDrawer@MDNavigationDrawer>
    drawer_logo: f'{environ["KITCHEN_SINK_ASSETS"]}drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu of Examples:"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Bottom App Bar"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Bottom Navigation"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Bottom Sheets"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Buttons"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Cards"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Chips"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Dialogs"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Download File"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Dropdown Item"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.open_drop_items_examples()

    NavigationDrawerIconButton:
        text: "Expansion Panel"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Floating Buttons"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Files Manager"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Fan Manager"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Grid lists"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Labels"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Lists"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        icon: "gesture-swipe"
        text: "Manager Swiper"
        on_release:
            app.show_manager_swiper()
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "MD Icons"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Menus"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Pickers"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Progress & activity"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Progress and Slider"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Refresh Layout"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Selection controls"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Snackbars"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Tabs"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Text fields"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Themes"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "Toolbars"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)

    NavigationDrawerIconButton:
        text: "User Animation Card"
        icon: app.drawer_item_icons.get(self.text, 'checkbox-blank-circle')
        on_release:
            app.show_screen(self.text)
            app.set_title_toolbar(self.text)


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    FloatLayout:
        id: float_box

        BoxLayout:
            id: box_for_manager
            orientation: 'vertical'

            MDToolbar:
                id: toolbar
                title: app.title
                md_bg_color: app.theme_cls.primary_color
                background_palette: 'Primary'
                background_hue: '500'
                elevation: 10
                left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
                right_action_items:
                    [['dots-vertical', lambda x: app.open_context_menu_source_code(toolbar)]] \
                    if scr_mngr.current != "previous" else []

            ScreenManager:
                id: scr_mngr
                transition: NoTransition()
                on_current: app.set_source_code_file()

                Screen:
                    name: 'previous'

                    FloatLayout:

                        Image:
                            source: f'{images_path}kivy-logo-white-512.png'
                            opacity: .3

                        ScrollView:
                            size_hint_y: None
                            height: Window.height - dp(200)
                            pos_hint: {'center_x': .5, 'center_y': .5}

                            GridLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                cols: 1
                                pos_hint: {'center_x': .5, 'center_y': .5}
    
                                BoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(10)
                                    size_hint_y: None
                                    height: self.minimum_height
                                    pos_hint: {'center_x': .5, 'center_y': .5}
        
                                    MDLabel:
                                        text: app.previous_text
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        font_style: 'Subtitle1'
                                        theme_text_color: 'Primary'
                                        markup: True
                                        halign: 'center'
                                        text_size: self.width - 20, None
        
                                    MDRaisedButton:
                                        text: 'Click Me'
                                        pos_hint: {'center_x': .5}
                                        on_release: scr_mngr.current = "stuidies list"

                                    MDLabel:
                                        text: app.previous_text_end
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        font_style: 'Subtitle1'
                                        theme_text_color: 'Primary'
                                        markup: True
                                        halign: 'center'
                                        text_size: self.width - 20, None

                Screen:
                    name: "stuidies list"

                    ScrollView:

                        GridLayout:
                            size_hint_y: None
                            height: self.minimum_height
                            cols: 1

                            BoxLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                orientation: "vertical"
                                spacing: "15dp"

                                Image:
                                    source: f"{environ['KITCHEN_SINK_ASSETS']}shrine.png"
                                    size_hint: None, None
                                    width: scr_mngr.width
                                    height: scr_mngr.height - demo_name.height * 2
                                    on_touch_down: if self.collide_point(*args[1].pos): scr_mngr.current = "shrine demo"

                                MDLabel:
                                    id: demo_name
                                    text:
                                        "Demo [color={COLOR}][b]Shrine[b][/color]".format(\
                                        COLOR=get_hex_from_color(app.theme_cls.primary_color))
                                    font_style: "H6"
                                    markup: True
                                    halign: "center"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                            Widget:
                                size_hint_y: None
                                height: "50dp"

                Screen:
                    name: "shrine demo"
                    on_enter: app.show_demo_shrine(self)
                    on_leave:
                        app.theme_cls.primary_palette = "BlueGray"
                        app.set_chevron_menu()
                        app.set_title_toolbar("Kitchen Sink")
                        toolbar.height = "56dp"
"""


class KitchenSink(App, Screens):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "BlueGray"
    theme_cls.accent_palette = "Gray"
    previous_date = ObjectProperty()
    title = "Kitchen Sink"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": "Example item %d" % i,
                "callback": self.callback_for_menu_items,
            }
            for i in range(15)
        ]
        self.Window = Window

        # Default class instances.
        self.manager = None
        self.md_app_bar = None
        self.instance_menu_source_code = None
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.user_card = None
        self.my_snackbar = None
        self.dialog_load_kv_files = None

        self.create_stack_floating_buttons = False
        self.manager_open = False
        self.cards_created = False

        self._interval = 0
        self.tick = 0
        self.x = 0
        self.y = 25
        self.file_source_code = ""

        self.hex_primary_color = get_hex_from_color(
            self.theme_cls.primary_color
        )
        self.drawer_item_icons = {
            "Bottom App Bar": "dock-bottom",
            "Buttons": "rectangle",
            "Cards": "cards-variant",
            "Dialogs": "window-open",
            "Download File": "download",
            "Dropdown Item": "arrow-down-drop-circle",
            "Expansion Panel": "arrow-expand-vertical",
            "Floating Buttons": "format-float-right",
            "Files Manager": "file-tree",
            "Grid lists": "grid",
            "Labels": "label",
            "Lists": "format-list-bulleted",
            "MD Icons": "material-design",
            "Menus": "menu",
            "Pickers": "calendar",
            "Refresh Layout": "refresh",
            "Selection controls": "checkbox-marked-circle-outline",
            "Tabs": "tab",
            "Text fields": "signature-text",
            "Themes": "theme-light-dark",
            "Toolbars": "set-top-box",
            "User Animation Card": "animation",
            "Bottom Navigation": "picture-in-picture-bottom-right",
            "Bottom Sheets": "file-document-box-outline",
            "Chips": "label-variant",
            "Fan Manager": "fan",
            "Progress & activity": "progress-check",
            "Progress and Slider": "percent",
            "Snackbars": "dock-window",
        }
        self.previous_text = (
            f"Welcome to the application [b][color={self.hex_primary_color}]"
            f"Kitchen Sink[/color][/b].\nTo see [b]"
            f"[color={self.hex_primary_color}]KivyMD[/color][/b] "
            f"examples, open the menu and select from the list the desired "
            f"example or"
        )
        self.previous_text_end = (
            f"for show example apps\n\n"
            f"Author - [b][color={self.hex_primary_color}]"
            f"Andrés Rodríguez[/color][/b]\n"
            f"[u][b][color={self.hex_primary_color}]"
            f"andres.rodriguez@lithersoft.com[/color][/b][/u]\n\n\n"
            f"Authors this Fork:\n\n"
            f"[b][color={self.hex_primary_color}]"
            f"Ivanov Yuri[/color][/b]\n"
            f"[u][b][color={self.hex_primary_color}]"
            f"kivydevelopment@gmail.com[/color][/b][/u]\n\n"
            f"[b][color={self.hex_primary_color}]Artem S. Bulgakov[/color][/b]\n"
            f"[u][b][color={self.hex_primary_color}]"
            f"bulgakov-a-s@yandex.ru[/color][/b][/u]\n\n"
            f"and contributors..."
        )
        self.names_contacts = (
            "Alexandr Taylor",
            "Yuri Ivanov",
            "Robert Patric",
            "Bob Marley",
            "Magnus Carlsen",
            "Jon Romero",
            "Anna Bell",
            "Maxim Kramerer",
            "Sasha Gray",
            "Vladimir Ivanenko",
        )
        self.list_name_icons = list(md_icons.keys())[0:15]
        Window.bind(on_keyboard=self.events)
        crop_image(
            (Window.width, int(dp(Window.height * 35 // 100))),
            f"{os.environ['KITCHEN_SINK_ASSETS']}guitar-1139397_1280.png",
            f"{os.environ['KITCHEN_SINK_ASSETS']}guitar-1139397_1280_crop.png",
        )

    def show_demo_shrine(self, instance):
        """
        :type instance <Screen name='shrine demo'> object

        """

        def add_screen_shrine(MDShrine):
            def remove_box(*args):
                instance.remove_widget(box)

            md_shrine = MDShrine()
            md_shrine.opacity = 0
            instance.add_widget(md_shrine)

            anim = Animation(opacity=0, d=0.5)
            anim.bind(on_complete=remove_box)
            anim.start(box)
            Animation(opacity=2, d=0.5).start(md_shrine)
            self.theme_cls.primary_palette = "Red"

        def show_demo_shrine(interval):
            from demos.kitchen_sink.studies.shrine.shrine import MDShrine

            anim = Animation(
                size_hint=(0.2, 0.2), pos_hint={"center_y": 0.7}, d=0.5
            )
            anim.bind(on_complete=lambda *x: add_screen_shrine(MDShrine))
            anim.start(box)

        from kivy.uix.image import Image

        self.main_widget.ids.toolbar.right_action_items = []
        self.main_widget.ids.toolbar.left_action_items = []
        self.main_widget.ids.toolbar.height = 0
        self.main_widget.ids.toolbar.title = ""
        box = BoxLayout(
            orientation="vertical",
            size_hint=(0.4, 0.6),
            spacing=dp(10),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        path_to_logo = (
            f"{os.environ['KITCHEN_SINK_ROOT']}/studies/shrine/data/images/shrine-white.png"
            if self.theme_cls.theme_style == "Dark"
            else f"{os.environ['KITCHEN_SINK_ROOT']}/studies/shrine/data/images/shrine-dark.png"
        )
        logo = Image(
            source=path_to_logo, size_hint_x=0.8, pos_hint={"center_x": 0.5}
        )
        box.add_widget(logo)
        box.add_widget(Factory.ShrinePresplashTile(text="SHRINE"))
        instance.add_widget(box)
        Clock.schedule_once(show_demo_shrine, 1)

    def set_list_for_refresh_layout(self):
        async def set_list_for_refresh_layout():
            names_icons_list = list(md_icons.keys())[self.x : self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.data["Refresh Layout"]["object"].ids.box.add_widget(
                    ItemForListRefreshLayout(icon=name_icon, text=name_icon)
                )
            self.data["Refresh Layout"][
                "object"
            ].ids.refresh_layout.refresh_done()

        asynckivy.start(set_list_for_refresh_layout())

    def refresh_callback(self, *args):
        """A method that updates the state of your application
        while the spinner remains on the screen."""

        def refresh_callback(interval):
            self.data["Refresh Layout"]["object"].ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 25, 50
            else:
                self.x, self.y = 0, 25
            self.set_list_for_refresh_layout()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def build_tabs(self):
        for name_tab in self.list_name_icons:
            tab = Factory.MyTab(text=name_tab)
            self.data["Tabs"]["object"].ids.android_tabs.add_widget(tab)

    def switch_tabs_to_icon(self, istance_android_tabs):
        for i, instance_tab in enumerate(
            istance_android_tabs.ids.scrollview.children[0].children
        ):
            istance_android_tabs.ids.scrollview.children[0].remove_widget(
                instance_tab
            )
            istance_android_tabs.add_widget(
                Factory.MyTab(text=self.list_name_icons[i])
            )

    def switch_tabs_to_text(self, istance_android_tabs):
        for instance_tab in istance_android_tabs.ids.scrollview.children[
            0
        ].children:
            for k, v in md_icons.items():
                if v == instance_tab.text:
                    istance_android_tabs.ids.scrollview.children[
                        0
                    ].remove_widget(instance_tab)
                    istance_android_tabs.add_widget(
                        Factory.MyTab(text=" ".join(k.split("-")).capitalize())
                    )
                    break

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""

        if not os.path.exists(os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

    def theme_picker_open(self):
        if not self.md_theme_picker:
            from kivymd.uix.picker import MDThemePicker

            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open()

    def example_add_stack_floating_buttons(self):
        from kivymd.uix.stackfloatingbutton import MDStackFloatingButtons

        def set_my_language(instance_button):
            toast(instance_button.icon)

        if not self.create_stack_floating_buttons:
            screen = self.main_widget.ids.scr_mngr.get_screen("stack buttons")
            screen.add_widget(
                MDStackFloatingButtons(
                    icon="lead-pencil",
                    floating_data={
                        "Python": "language-python",
                        "Php": "language-php",
                        "C++": "language-cpp",
                    },
                    callback=set_my_language,
                )
            )
            self.create_stack_floating_buttons = True

    def set_expansion_panel(self):
        from kivymd.uix.expansionpanel import MDExpansionPanel

        def callback(text):
            toast(f"{text} to {content.name_item}")

        content = ContentForAnimCard(callback=callback)

        for name_contact in self.names_contacts:
            self.data["Expansion Panel"]["object"].ids.anim_list.add_widget(
                MDExpansionPanel(
                    content=content,
                    icon=f"{os.environ['KITCHEN_SINK_ASSETS']}kivy-logo-white-512.png",
                    title=name_contact,
                )
            )

    def set_chevron_back_screen(self):
        """Sets the return chevron to the previous screen in ToolBar."""

        self.main_widget.ids.toolbar.right_action_items = [
            ["dots-vertical", lambda x: self.root.toggle_nav_drawer()]
        ]

    def download_progress_hide(self, instance_progress, value):
        """Hides progress progress."""

        self.main_widget.ids.toolbar.right_action_items = [
            [
                "download",
                lambda x: self.download_progress_show(instance_progress),
            ]
        ]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        from kivymd.uix.progressloader import MDProgressLoader

        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket

            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port)
                )
                return True
            except (TimeoutError, ConnectionError, OSError):
                return False

        if get_connect():
            link = (
                "https://www.python.org/ftp/python/3.5.1/"
                "python-3.5.1-embed-win32.zip"
            )
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(self.directory, "python-3.5.1.zip"),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide,
            )
            progress.start(self.data["Download File"]["object"].ids.box_flt)
        else:
            toast("Connect error!")

    def download_complete(self):
        self.set_chevron_back_screen()
        toast("Done")

    def open_drop_items_examples(self):
        from kivymd.uix.dialog import MDDialog

        def set_list_drop_items():
            for i in range(20):
                self.data["Dropdown Item List"]["object"].ids.box.add_widget(
                    ItemForDropItemList(
                        items=[str(i + 1), str(i + 2), str(i + 3)]
                    )
                )

        def open_drop_items_examples(text_item, dialog):
            dialog.dismiss()
            data = {"Item": "Dropdown Item", "List": "Dropdown Item List"}
            self.show_screen(data[text_item])
            self.set_title_toolbar(data[text_item])
            set_list_drop_items()

        MDDialog(
            title="Kitchen Sink",
            size_hint=(0.8, 0.4),
            text_button_ok="Item",
            text="Open MDDropDownItem or ListButtonDropDown?",
            text_button_cancel="List",
            events_callback=open_drop_items_examples,
        ).open()

    def file_manager_open(self):
        from kivymd.uix.filemanager import MDFileManager
        from kivymd.uix.dialog import MDDialog

        def open_file_manager(text_item, dialog):
            previous = False if text_item == "List" else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager,
                select_path=self.select_path,
                previous=previous,
            )
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(self.user_data_dir)
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title="Kitchen Sink",
            size_hint=(0.8, 0.4),
            text_button_ok="List",
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel="Previous",
            events_callback=open_file_manager,
        ).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.
        :type path: str;
        :param path: path to the selected directory or file;
        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False
        self.set_chevron_menu()

    def set_chevron_menu(self):
        self.main_widget.ids.toolbar.left_action_items = [
            ["menu", lambda x: self.root.toggle_nav_drawer()]
        ]

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def add_cards(self, instance_grid_card):
        """Adds MDCardPost objects to the screen Cards
        when the screen is open."""

        from kivymd.uix.card import MDCardPost

        def callback(instance, value):
            if value is None:
                toast("Delete post %s" % str(instance))
            elif isinstance(value, int):
                toast("Set like in %d stars" % value)
            elif isinstance(value, str):
                toast("Repost with %s " % value)
            elif isinstance(value, list):
                toast(value[1])

        if not self.cards_created:
            self.cards_created = True
            menu_items = [
                {
                    "viewclass": "MDMenuItem",
                    "text": "Example item %d" % i,
                    "callback": self.callback_for_menu_items,
                }
                for i in range(2)
            ]
            buttons = ["facebook", "vk", "twitter"]

            instance_grid_card.add_widget(
                MDCardPost(
                    text_post="Card with text", swipe=True, callback=callback
                )
            )
            instance_grid_card.add_widget(
                MDCardPost(
                    right_menu=menu_items,
                    swipe=True,
                    text_post="Card with a button to open the menu MDDropDown",
                    callback=callback,
                )
            )
            instance_grid_card.add_widget(
                MDCardPost(
                    likes_stars=True,
                    callback=callback,
                    swipe=True,
                    text_post="Card with asterisks for voting.",
                )
            )

            image_for_card = f"{os.environ['KITCHEN_SINK_ASSETS']}kitten-for_card-1049129_1280-crop.png"
            if not os.path.exists(image_for_card):
                crop_image(
                    (int(Window.width), int(dp(200))),
                    f"{os.environ['KITCHEN_SINK_ASSETS']}kitten-1049129_1280.png",
                    image_for_card,
                )
            instance_grid_card.add_widget(
                MDCardPost(
                    source=image_for_card,
                    tile_text="Little Baby",
                    tile_font_style="H5",
                    text_post="This is my favorite cat. He's only six months "
                    "old. He loves milk and steals sausages :) "
                    "And he likes to play in the garden.",
                    with_image=True,
                    swipe=True,
                    callback=callback,
                    buttons=buttons,
                )
            )

    def update_screen(self, instance):
        """Set new label on the screen UpdateSpinner."""

        def update_screen(interval):
            self.tick += 1
            if self.tick > 2:
                instance.update = True
                self.tick = 0
                self.data["Update Screen Widget"][
                    "object"
                ].ids.upd_lbl.text = "New string"
                Clock.unschedule(update_screen)

        Clock.schedule_interval(update_screen, 1)

    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        return self.main_widget

    def show_user_example_animation_card(self):
        """Create and open instance MDUserAnimationCard
        for the screen UserCard."""

        from kivymd.uix.useranimationcard import MDUserAnimationCard

        def main_back_callback():
            toast("Close card")

        if not self.user_card:
            image_for_user_card = f"{os.environ['KITCHEN_SINK_ASSETS']}guitar-for-user-card1139397_1280-crop.png"
            if not os.path.exists(image_for_user_card):
                crop_image(
                    (int(Window.width), int(dp(Window.height * 40 // 100))),
                    f"{os.environ['KITCHEN_SINK_ASSETS']}guitar-1139397_1280.png",
                    image_for_user_card,
                )

            self.user_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar=image_for_user_card,
                callback=main_back_callback,
            )
            self.user_card.box_content.add_widget(ContentForAnimCard())
        self.user_card.open()

    def show_example_snackbar(self, snack_type):
        """Create and show instance Snackbar for the screen MySnackBar."""

        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=0.2)
                anim.start(self.data["Snackbars"]["object"].ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        from kivymd.uix.snackbar import Snackbar

        if snack_type == "simple":
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == "button":
            Snackbar(
                text="This is a snackbar",
                button_text="WITH A BUTTON",
                button_callback=callback,
            ).show()
        elif snack_type == "verylong":
            Snackbar(
                text="This is a very very very very very very very "
                "long snackbar!"
            ).show()
        elif snack_type == "float":
            if not self.my_snackbar:
                self.my_snackbar = Snackbar(
                    text="This is a snackbar!",
                    button_text="Button",
                    duration=3,
                    button_callback=callback,
                )
                self.my_snackbar.show()
                anim = Animation(y=dp(72), d=0.2)
                anim.bind(
                    on_complete=lambda *args: Clock.schedule_interval(
                        wait_interval, 0
                    )
                )
                anim.start(self.data["Snackbars"]["object"].ids.button)

    def show_example_input_dialog(self):
        """Creates an instance of the dialog box and displays it
        on the screen for the screen Dialogs."""

        def result(text_button, instance):
            toast(instance.text_field.text)

        if not self.input_dialog:
            from kivymd.uix.dialog import MDInputDialog

            self.input_dialog = MDInputDialog(
                title="Title",
                hint_text="Hint text",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                events_callback=result,
            )
        self.input_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            from kivymd.uix.dialog import MDDialog

            self.alert_dialog = MDDialog(
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="This is Alert dialog",
                events_callback=self.callback_for_menu_items,
            )
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.uix.dialog import MDDialog

            self.ok_cancel_dialog = MDDialog(
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Ok",
                text="This is Ok Cancel dialog",
                text_button_cancel="Cancel",
                events_callback=self.callback_for_menu_items,
            )
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            from kivymd.uix.dialog import MDDialog

            self.long_dialog = MDDialog(
                text="Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit, sed do eiusmod tempor incididunt ut labore et "
                "dolore magna aliqua. Ut enim ad minim veniam, quis "
                "nostrud exercitation ullamco laboris nisi ut aliquip "
                "ex ea commodo consequat. Duis aute irure dolor in "
                "reprehenderit in voluptate velit esse cillum dolore eu "
                "fugiat nulla pariatur. Excepteur sint occaecat "
                "cupidatat non proident, sunt in culpa qui officia "
                "deserunt mollit anim id est laborum.",
                title="Title",
                size_hint=(0.8, 0.4),
                text_button_ok="Yes",
                events_callback=self.callback_for_menu_items,
            )
        self.long_dialog.open()

    def get_time_picker_date(self, instance, time):
        """Get date for MDTimePicker from the screen Pickers."""

        self.data["Pickers"]["object"].ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        """Show MDTimePicker from the screen Pickers."""

        from kivymd.uix.picker import MDTimePicker

        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_date)

        if self.data["Pickers"][
            "object"
        ].ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        """Set previous date for MDDatePicker from the screen Pickers."""

        self.previous_date = date_obj
        self.data["Pickers"]["object"].ids.date_picker_label.text = str(
            date_obj
        )

    def show_example_date_picker(self):
        """Show MDDatePicker from the screen Pickers."""

        from kivymd.uix.picker import MDDatePicker

        if self.data["Pickers"][
            "object"
        ].ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(
                    self.set_previous_date, pd.year, pd.month, pd.day
                ).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def show_example_custom_bottom_sheet(
        self, type, corner=None, animation=True
    ):
        """Show menu from the screen BottomSheet."""

        from kivymd.uix.bottomsheet import MDCustomBottomSheet

        if type == "custom":
            custom_screen_for_bottom_sheet = self.data["Popup Screen"]["object"]
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
        from kivymd.uix.bottomsheet import MDListBottomSheet

        bs_menu_1 = MDListBottomSheet()
        bs_menu_1.add_item(
            "Here's an item with text only",
            lambda x: self.callback_for_menu_items(
                "Here's an item with text only"
            ),
        )
        bs_menu_1.add_item(
            "Here's an item with an icon",
            lambda x: self.callback_for_menu_items(
                "Here's an item with an icon"
            ),
            icon="clipboard-account",
        )
        bs_menu_1.add_item(
            "Here's another!",
            lambda x: self.callback_for_menu_items("Here's another!"),
            icon="nfc",
        )
        bs_menu_1.open()

    def show_example_grid_bottom_sheet(self):
        from kivymd.uix.bottomsheet import MDGridBottomSheet

        bs_menu = MDGridBottomSheet()
        bs_menu.add_item(
            "Facebook",
            lambda x: self.callback_for_menu_items("Facebook"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}facebook-box.png",
        )
        bs_menu.add_item(
            "YouTube",
            lambda x: self.callback_for_menu_items("YouTube"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}youtube-play.png",
        )
        bs_menu.add_item(
            "Twitter",
            lambda x: self.callback_for_menu_items("Twitter"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}twitter.png",
        )
        bs_menu.add_item(
            "Da Cloud",
            lambda x: self.callback_for_menu_items("Da Cloud"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}cloud-upload.png",
        )
        bs_menu.add_item(
            "Camera",
            lambda x: self.callback_for_menu_items("Camera"),
            icon_src=f"{os.environ['KITCHEN_SINK_ASSETS']}camera.png",
        )
        bs_menu.open()

    def set_title_toolbar(self, title):
        """Set string title in MDToolbar for the whole application."""

        self.main_widget.ids.toolbar.title = title

    def set_appbar(self):
        """Create MDBottomAppBar for the screen BottomAppBar."""

        from kivymd.uix.toolbar import MDBottomAppBar

        def press_button(inctance):
            toast("Press Button")

        self.md_app_bar = MDBottomAppBar(
            md_bg_color=self.theme_cls.primary_color,
            left_action_items=[
                ["menu", lambda x: x],
                ["clock", lambda x: x],
                ["dots-vertical", lambda x: x],
            ],
            anchor="right",
            callback=press_button,
        )

    def move_item_menu(self, anchor):
        """Sets icons in MDBottomAppBar for the screen BottomAppBar."""

        md_app_bar = self.md_app_bar
        if md_app_bar.anchor != anchor:
            if len(md_app_bar.right_action_items):
                md_app_bar.left_action_items.append(
                    md_app_bar.right_action_items[0]
                )
                md_app_bar.right_action_items = []
            else:
                left_action_items = md_app_bar.left_action_items
                action_items = left_action_items[0:2]
                md_app_bar.right_action_items = [left_action_items[-1]]
                md_app_bar.left_action_items = action_items

    def show_password(self, field, button):
        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = "eye" if button.icon == "eye-off" else "eye-off"

    def set_error_message(self, *args):
        """Checks text of TextField with type "on_error"
        for the screen TextFields."""

        text_field_error = args[0]
        if len(text_field_error.text) == 2:
            text_field_error.error = True
        else:
            text_field_error.error = False

    def set_list_md_icons(self, text="", search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.main_widget.ids.scr_mngr.get_screen(
                "md icons"
            ).ids.rv.data.append(
                {
                    "viewclass": "MDIconItemForMdIconsList",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": self.callback_for_menu_items,
                }
            )

        self.main_widget.ids.scr_mngr.get_screen("md icons").ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def set_source_code_file(self):
        """Assigns the file_source_code attribute the file name
        with example code for the current screen."""

        if self.main_widget.ids.scr_mngr.current == "code viewer":
            return

        has_screen = False
        for name_item_drawer in self.data.keys():
            if (
                self.data[name_item_drawer]["name_screen"]
                == self.main_widget.ids.scr_mngr.current
            ):
                self.file_source_code = self.data[name_item_drawer].get(
                    "source_code", None
                )
                has_screen = True
                break
        if not has_screen:
            self.file_source_code = None

    def open_context_menu_source_code(self, instance):
        def callback_context_menu(icon):
            context_menu.dismiss()

            if not self.file_source_code:
                from kivymd.uix.snackbar import Snackbar

                Snackbar(text="No source code for this example").show()
                return
            elif icon == "source-repository":
                if platform in ("win", "linux", "macosx"):
                    webbrowser.open(
                        f"https://github.com/HeaTTheatR/KivyMD/wiki/"
                        f"{os.path.splitext(self.file_source_code)[0]}"
                    )
            elif icon == "language-python":
                self.main_widget.ids.scr_mngr.current = "code viewer"
                try:
                    self.data["Source code"][
                        "object"
                    ].ids.code_input.text = open(
                        f"{os.environ['KITCHEN_SINK_ASSETS']}md/{self.file_source_code}",
                        "rt",
                        encoding="utf-8",
                    ).read()
                except FileNotFoundError:
                    from kivymd.uix.snackbar import Snackbar

                    Snackbar(text="Cannot load source code").show()

        menu_for_context_menu_source_code = []
        data = {
            "Source code": "language-python",
            "Open in Wiki": "source-repository",
        }
        if self.main_widget.ids.scr_mngr.current == "code viewer":
            data = {"Open in Wiki": "source-repository"}
        for name_item in data.keys():
            menu_for_context_menu_source_code.append(
                {
                    "viewclass": "MDIconItemForMdIconsList",
                    "text": name_item,
                    "icon": data[name_item],
                    "text_color": [1, 1, 1, 1],
                    "callback": lambda x=name_item: callback_context_menu(x),
                }
            )
        context_menu = MDDropdownMenu(
            items=menu_for_context_menu_source_code,
            max_height=dp(260),
            width_mult=4,
            width_rectangle=0.1,
            background_color=self.theme_cls.primary_dark,
        )
        context_menu.open(instance.ids.right_actions.children[0])

    def on_pause(self):
        return True

    def on_start(self):
        async def load_all_kv_files():
            count_kvs = len(list(self.data.keys()))
            for i, name_screen in enumerate(self.data.keys()):
                await asynckivy.sleep(0)
                self.dialog_load_kv_files.name_kv_file = name_screen
                self.dialog_load_kv_files.percent = str(
                    ((i + 1) * 100) // count_kvs
                )
                Builder.load_string(self.data[name_screen]["kv_string"])
                self.data[name_screen]["object"] = eval(
                    self.data[name_screen]["Factory"]
                )
                if name_screen == "Bottom App Bar":
                    self.set_appbar()
                    self.data[name_screen]["object"].add_widget(self.md_app_bar)
                if name_screen != "Popup Screen":
                    self.main_widget.ids.scr_mngr.add_widget(
                        self.data[name_screen]["object"]
                    )
                if name_screen == "Text fields":
                    self.data[name_screen]["object"].ids.text_field_error.bind(
                        on_text_validate=self.set_error_message,
                        on_focus=self.set_error_message,
                    )
                elif name_screen == "MD Icons":
                    self.set_list_md_icons()
                elif name_screen == "Tabs":
                    self.build_tabs()
                elif name_screen == "Refresh Layout":
                    self.set_list_for_refresh_layout()

            self.dialog_load_kv_files.dismiss()

        self.dialog_load_kv_files = DialogLoadKvFiles()
        self.dialog_load_kv_files.open()
        asynckivy.start(load_all_kv_files())

    def on_stop(self):
        pass

    def open_settings(self, *args):
        return False


class CodeInputViewer(ScrollView):
    text = StringProperty()
    path = StringProperty()
    effect_cls = ScrollEffect


class ContentForAnimCard(BoxLayout):
    callback = ObjectProperty(lambda x: None)


class BaseFanScreen(MDFanScreen):
    path_to_image = StringProperty()


class ScreenOne(BaseFanScreen):
    pass


class ScreenTwo(BaseFanScreen):
    pass


class ScreenTree(BaseFanScreen):
    pass


class ScreenFour(BaseFanScreen):
    pass


class BoxContentForBottomSheetCustomScreenList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(10):
            self.ids.box.add_widget(
                Factory.ContentForBottomSheetCustomScreenList()
            )


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class ListButtonDropdown(IRightBodyTouch, MDDropDownItem):
    pass


class ItemForListRefreshLayout(OneLineIconListItem):
    icon = StringProperty()


class MyCard(MDCard):
    text = StringProperty("")


class ItemForDropItemList(ThreeLineRightIconListItem):
    items = ListProperty()


if __name__ == "__main__":
    KitchenSink().run()
