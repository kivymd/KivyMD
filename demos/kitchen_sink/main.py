"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os
import sys

from kivy.factory import Factory

sys.path.append(os.path.abspath(__file__).split('demos')[0])

from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color

from screens import Screens

from kivymd.utils.cropimage import crop_image
from kivymd.utils import asynckivy
from kivymd.fanscreenmanager import MDFanScreen
from kivymd.popupscreen import MDPopupScreen
from kivymd.button import MDIconButton
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, \
    OneLineIconListItem, OneLineListItem
from kivymd.selectioncontrols import MDCheckbox
from kivymd.theming import ThemeManager
from kivymd.ripplebehavior import CircularRippleBehavior
from kivymd.cards import MDCard
from kivymd.icon_definitions import md_icons


def toast(text):
    from kivymd.toast.kivytoast import toast
    toast(text)


main_widget_kv = '''
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import images_path kivymd.images_path
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import MDLabel kivymd.label.MDLabel
#:import MDDropdownMenu kivymd.menus.MDDropdownMenu


<ContentPopup@BoxLayout>
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: 'assets/guitar-1139397_1280_crop.png'
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

        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        # FIXME: Don't work "secondary_text_color" parameter
        # secondary_text_color: app.theme_cls.primary_color

        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        on_press: root.callback(self.text)
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)

        IconLeftSampleWidget:
            icon: 'remote'


<MyNavigationDrawerIconButton@NavigationDrawerIconButton>
    icon: 'checkbox-blank-circle'
    on_release:
        app.show_screen(root.text)
        app.set_title_toolbar(root.text)


<ContentNavigationDrawer@MDNavigationDrawer>
    drawer_logo: './assets/drawer_logo.png'
    use_logo: 'logo'

    NavigationDrawerSubheader:
        text: "Menu of Examples:"

    MyNavigationDrawerIconButton:
        text: "Accordion"

    MyNavigationDrawerIconButton:
        text: "Bottom App Bar"

    MyNavigationDrawerIconButton:
        text: "Accordion List"

    MyNavigationDrawerIconButton:
        text: "Bottom Navigation"

    MyNavigationDrawerIconButton:
        text: "Bottom Sheets"

    MyNavigationDrawerIconButton:
        text: "Buttons"

    MyNavigationDrawerIconButton:
        text: "Cards"

    MyNavigationDrawerIconButton:
        text: "Chips"

    MyNavigationDrawerIconButton:
        text: "Dialogs"

    MyNavigationDrawerIconButton:
        text: "Download File"

    MyNavigationDrawerIconButton:
        text: "Floating Buttons"

    MyNavigationDrawerIconButton:
        text: "Files Manager"

    MyNavigationDrawerIconButton:
        text: "Fan Manager"

    MyNavigationDrawerIconButton:
        text: "Grid lists"

    MyNavigationDrawerIconButton:
        text: "Labels"

    MyNavigationDrawerIconButton:
        text: "Lists"

    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Manager Swiper"
        on_release:
            app.show_manager_swiper()
            app.set_title_toolbar(self.text)

    MyNavigationDrawerIconButton:
        text: "MD Icons"

    MyNavigationDrawerIconButton:
        text: "Menus"

    MyNavigationDrawerIconButton:
        text: "Pickers"

    MyNavigationDrawerIconButton:
        text: "Progress & activity"

    MyNavigationDrawerIconButton:
        text: "Popup Screen"

    MyNavigationDrawerIconButton:
        text: "Progress bars"

    MyNavigationDrawerIconButton:
        text: "Refresh Layout"

    MyNavigationDrawerIconButton:
        text: "Selection controls"

    MyNavigationDrawerIconButton:
        text: "Sliders"

    MyNavigationDrawerIconButton:
        text: "Snackbars"

    MyNavigationDrawerIconButton:
        text: "Tabs"

    MyNavigationDrawerIconButton:
        text: "Text fields"

    MyNavigationDrawerIconButton:
        text: "Themes"

    MyNavigationDrawerIconButton:
        text: "Toolbars"

    MyNavigationDrawerIconButton:
        text: "User Animation Card"


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
                left_action_items:
                    [['menu', lambda x: app.root.toggle_nav_drawer()]]
                right_action_items:
                    [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]

            ScreenManager:
                id: scr_mngr
                transition: NoTransition()

                Screen:
                    name: 'previous'

                    FloatLayout:

                        Image:
                            source: f'{images_path}kivy-logo-white-512.png'
                            opacity: .3

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
                                on_release:
                                    app.set_menu_for_demo_apps()
                                    app.instance_menu_demo_apps = MDDropdownMenu(\
                                    items=app.menu_for_demo_apps, \
                                    max_height=dp(260), width_mult=4)
                                    app.instance_menu_demo_apps.open(self)

                            MDLabel:
                                text: app.previous_text_end
                                size_hint_y: None
                                height: self.texture_size[1]
                                font_style: 'Subtitle1'
                                theme_text_color: 'Primary'
                                markup: True
                                halign: 'center'
                                text_size: self.width - 20, None
'''


class KitchenSink(App, Screens):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'
    theme_cls.accent_palette = 'Gray'
    previous_date = ObjectProperty()
    title = "Kitchen Sink"
    theme_cls.theme_style = 'Dark'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': self.callback_for_menu_items}
            for i in range(15)
        ]
        self.Window = Window
        self.manager = None
        self.md_app_bar = None
        self.instance_menu_demo_apps = None
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.manager_open = False
        self.cards_created = False
        self.user_card = None
        self.bs_menu_1 = None
        self.bs_menu_2 = None
        self.my_snackbar = None
        self._interval = 0
        self.tick = 0
        self.x = 0
        self.y = 25
        self.create_stack_floating_buttons = False
        self.hex_primary_color = get_hex_from_color(
                self.theme_cls.primary_color)
        self.previous_text = \
            f"Welcome to the application [b][color={self.hex_primary_color}]" \
            f"Kitchen Sink[/color][/b].\nTo see [b]" \
            f"[color={self.hex_primary_color}]KivyMD[/color][/b] " \
            f"examples, open the menu and select from the list the desired " \
            f"example or"
        self.previous_text_end = \
            f"for show example apps\n\n" \
            f"Author - [b][color={self.hex_primary_color}]" \
            f"Andrés Rodríguez[/color][/b]\n" \
            f"[u][b][color={self.hex_primary_color}]" \
            f"andres.rodriguez@lithersoft.com[/color][/b][/u]\n\n" \
            f"Author this Fork - [b][color={self.hex_primary_color}]" \
            f"Ivanov Yuri[/color][/b]\n" \
            f"[u][b][color={self.hex_primary_color}]" \
            f"kivydevelopment@gmail.com[/color][/b][u]"
        self.names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko')
        self.demo_apps_list = [
            'Shop Window', 'Coffee Menu', 'Fitness Club', 'Registration',
            'Account Page']
        self.menu_for_demo_apps = []
        self.list_name_icons = list(md_icons.keys())[0:15]
        Window.bind(on_keyboard=self.events)
        crop_image((Window.width, int(dp(Window.height * 35 // 100))),
                   f'{self.directory}/assets/guitar-1139397_1280.png',
                   f'{self.directory}/assets/guitar-1139397_1280_crop.png')

    def set_list_for_refresh_layout(self):
        async def set_list_for_refresh_layout():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.data['Refresh Layout']['object'].\
                    ids.box.add_widget(ItemForListRefreshLayout(
                        icon=name_icon, text=name_icon))
            self.data['Refresh Layout']['object'].ids.refresh_layout.refresh_done()

        asynckivy.start(set_list_for_refresh_layout())

    def refresh_callback(self, *args):
        """A method that updates the state of your application
        while the spinner remains on the screen."""

        def refresh_callback(interval):
            self.data['Refresh Layout']['object'].\
                ids.box.clear_widgets()
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
            self.data['Tabs']['object'].ids.android_tabs.add_widget(tab)

    def switch_tabs_to_icon(self, istance_android_tabs):
        for i, instance_tab in enumerate(
                istance_android_tabs.ids.scrollview.children[0].children):
            istance_android_tabs.ids.scrollview.children[0].remove_widget(
                instance_tab)
            istance_android_tabs.add_widget(
                Factory.MyTab(text=self.list_name_icons[i]))

    def switch_tabs_to_text(self, istance_android_tabs):
        for instance_tab in istance_android_tabs.ids.scrollview.children[
                0].children:
            for k, v in md_icons.items():
                if v == instance_tab.text:
                    istance_android_tabs.ids.scrollview.children[
                        0].remove_widget(instance_tab)
                    istance_android_tabs.add_widget(
                        Factory.MyTab(text=' '.join(k.split('-')).capitalize()))
                    break

    def crop_image_for_tile(self, instance, size, path_to_crop_image):
        """Crop images for Grid screen."""

        if not os.path.exists(
                os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace('_tile_crop', '')
            crop_image(size, path_to_origin_image, path_to_crop_image)
        instance.source = path_to_crop_image

    def theme_picker_open(self):
        if not self.md_theme_picker:
            from kivymd.pickers import MDThemePicker
            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open()

    def example_add_stack_floating_buttons(self):
        from kivymd.stackfloatingbuttons import MDStackFloatingButtons

        def set_my_language(instance_button):
            toast(instance_button.icon)

        if not self.create_stack_floating_buttons:
            screen = self.main_widget.ids.scr_mngr.get_screen('stack buttons')
            screen.add_widget(MDStackFloatingButtons(
                icon='lead-pencil',
                floating_data={
                    'Python': 'language-python',
                    'Php': 'language-php',
                    'C++': 'language-cpp'},
                callback=set_my_language))
            self.create_stack_floating_buttons = True

    def set_accordion_list(self):
        from kivymd.accordionlistitem import MDAccordionListItem

        def callback(text):
            toast(f'{text} to {content.name_item}')

        content = ContentForAnimCard(callback=callback)

        for name_contact in self.names_contacts:
            self.data['Accordion List']['object'].ids.anim_list.add_widget(
                MDAccordionListItem(content=content,
                                    icon='assets/kivy-logo-white-512.png',
                                    title=name_contact))

    def set_chevron_back_screen(self):
        """Sets the return chevron to the previous screen in ToolBar."""

        self.main_widget.ids.toolbar.right_action_items = [
            ['dots-vertical', lambda x: self.root.toggle_nav_drawer()]]

    def download_progress_hide(self, instance_progress, value):
        """Hides progress progress."""

        self.main_widget.ids.toolbar.right_action_items =\
            [['download',
              lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        from kivymd.progressloader import MDProgressLoader

        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port))
                return True
            except (TimeoutError, ConnectionError, OSError):
                return False

        if get_connect():
            link = 'https://www.python.org/ftp/python/3.5.1/'\
                   'python-3.5.1-embed-win32.zip'
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide
            )
            progress.start(self.data['Download File']['object'].ids.box_flt)
        else:
            toast('Connect error!')

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')

    def file_manager_open(self):
        from kivymd.filemanager import MDFileManager
        from kivymd.dialog import MDDialog

        def open_file_manager(text_item, dialog):
            previous = False if text_item == 'List' else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path,
                                              previous=previous)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(self.user_data_dir)
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title='Title', size_hint=(.8, .4), text_button_ok='List',
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel='Previous',
            events_callback=open_file_manager).open()

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
            ['menu', lambda x: self.root.toggle_nav_drawer()]]

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

        from kivymd.cards import MDCardPost

        def callback(instance, value):
            if value is None:
                toast('Delete post %s' % str(instance))
            elif isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif isinstance(value, str):
                toast('Repost with %s ' % value)
            elif isinstance(value, list):
                toast(value[1])

        if not self.cards_created:
            self.cards_created = True
            menu_items = [
                {'viewclass': 'MDMenuItem',
                 'text': 'Example item %d' % i,
                 'callback': self.callback_for_menu_items}
                for i in range(2)
            ]
            buttons = ['facebook', 'vk', 'twitter']

            instance_grid_card.add_widget(
                MDCardPost(text_post='Card with text',
                           swipe=True, callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    right_menu=menu_items, swipe=True,
                    text_post='Card with a button to open the menu MDDropDown',
                    callback=callback))
            instance_grid_card.add_widget(
                MDCardPost(
                    likes_stars=True, callback=callback, swipe=True,
                    text_post='Card with asterisks for voting.'))

            instance_grid_card.add_widget(
                MDCardPost(
                    source="./assets/kitten-1049129_1280.png",
                    tile_text="Little Baby",
                    tile_font_style="H5",
                    text_post="This is my favorite cat. He's only six months "
                              "old. He loves milk and steals sausages :) "
                              "And he likes to play in the garden.",
                    with_image=True, swipe=True, callback=callback,
                    buttons=buttons))

    def update_screen(self, instance):
        """Set new label on the screen UpdateSpinner."""

        def update_screen(interval):
            self.tick += 1
            if self.tick > 2:
                instance.update = True
                self.tick = 0
                self.data['Update Screen Widget']['object'].\
                    ids.upd_lbl.text = "New string"
                Clock.unschedule(update_screen)

        Clock.schedule_interval(update_screen, 1)

    main_widget = None

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        return self.main_widget

    def set_popup_screen(self, content_popup):
        popup_menu = ContentForAnimCard()
        popup_menu.add_widget(Widget(size_hint_y=None, height=dp(150)))
        popup_screen = self.data['Popup Screen']['object'].ids.popup_screen
        popup_screen.screen = popup_menu
        popup_screen.background_color = [.3, .3, .3, 1]
        popup_screen.max_height = content_popup.ids.image.height + dp(5)

    def show_user_example_animation_card(self):
        """Create and open instance MDUserAnimationCard
        for the screen UserCard."""

        from kivymd.useranimationcard import MDUserAnimationCard

        def main_back_callback():
            toast('Close card')

        if not self.user_card:
            self.user_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar="./assets/guitar-1139397_1280.png",
                callback=main_back_callback)
            self.user_card.box_content.add_widget(
                ContentForAnimCard())
        self.user_card.open()

    def show_example_snackbar(self, snack_type):
        """Create and show instance Snackbar for the screen MySnackBar."""

        def callback(instance):
            toast(instance.text)

        def wait_interval(interval):
            self._interval += interval
            if self._interval > self.my_snackbar.duration:
                anim = Animation(y=dp(10), d=.2)
                anim.start(self.data['Snackbars']['object'].ids.button)
                Clock.unschedule(wait_interval)
                self._interval = 0
                self.my_snackbar = None

        from kivymd.snackbars import Snackbar

        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=callback).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()
        elif snack_type == 'float':
            if not self.my_snackbar:
                self.my_snackbar = Snackbar(
                    text="This is a snackbar!", button_text='Button',
                    duration=3, button_callback=callback)
                self.my_snackbar.show()
                anim = Animation(y=dp(72), d=.2)
                anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                    wait_interval, 0))
                anim.start(self.data['Snackbars']['object'].ids.button)

    def show_example_input_dialog(self):
        """Creates an instance of the dialog box and displays it
        on the screen for the screen Dialogs."""

        def result(text_button, instance):
            toast(instance.text_field.text)

        if not self.input_dialog:
            from kivymd.dialog import MDInputDialog

            self.input_dialog = MDInputDialog(
                title='Title', hint_text='Hint text', size_hint=(.8, .4),
                text_button_ok='Ok', events_callback=result)
        self.input_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            from kivymd.dialog import MDDialog

            self.alert_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Alert dialog",
                events_callback=self.callback_for_menu_items)
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            from kivymd.dialog import MDDialog

            self.ok_cancel_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Ok Cancel dialog", text_button_cancel='Cancel',
                events_callback=self.callback_for_menu_items)
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            from kivymd.dialog import MDDialog

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
                title='Title', size_hint=(.8, .4), text_button_ok='Yes',
                events_callback=self.callback_for_menu_items)
        self.long_dialog.open()

    def get_time_picker_date(self, instance, time):
        """Get date for MDTimePicker from the screen Pickers."""

        self.data['Pickers']['object'].ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        """Show MDTimePicker from the screen Pickers."""

        from kivymd.pickers import MDTimePicker

        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_date)

        if self.data['Pickers']['object'].\
                ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        """Set previous date for MDDatePicker from the screen Pickers."""

        self.previous_date = date_obj
        self.data['Pickers']['object'].\
            ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        """Show MDDatePicker from the screen Pickers."""

        from kivymd.pickers import MDDatePicker

        if self.data['Pickers']['object'].\
                ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def show_example_bottom_sheet(self):
        """Show menu from the screen BottomSheet."""

        from kivymd.bottomsheet import MDListBottomSheet

        if not self.bs_menu_1:
            self.bs_menu_1 = MDListBottomSheet()
            self.bs_menu_1.add_item(
                "Here's an item with text only",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with text only"))
            self.bs_menu_1.add_item(
                "Here's an item with an icon",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with an icon"),
                icon='clipboard-account')
            self.bs_menu_1.add_item(
                "Here's another!",
                lambda x: self.callback_for_menu_items(
                    "Here's another!"),
                icon='nfc')
        self.bs_menu_1.open()

    def show_example_grid_bottom_sheet(self):
        """Show menu from the screen BottomSheet."""

        if not self.bs_menu_2:
            from kivymd.bottomsheet import MDGridBottomSheet

            self.bs_menu_2 = MDGridBottomSheet()
            self.bs_menu_2.add_item(
                "Facebook",
                lambda x: self.callback_for_menu_items("Facebook"),
                icon_src='./assets/facebook-box.png')
            self.bs_menu_2.add_item(
                "YouTube",
                lambda x: self.callback_for_menu_items("YouTube"),
                icon_src='./assets/youtube-play.png')
            self.bs_menu_2.add_item(
                "Twitter",
                lambda x: self.callback_for_menu_items("Twitter"),
                icon_src='./assets/twitter.png')
            self.bs_menu_2.add_item(
                "Da Cloud",
                lambda x: self.callback_for_menu_items("Da Cloud"),
                icon_src='./assets/cloud-upload.png')
            self.bs_menu_2.add_item(
                "Camera",
                lambda x: self.callback_for_menu_items("Camera"),
                icon_src='./assets/camera.png')
        self.bs_menu_2.open()

    def set_title_toolbar(self, title):
        """Set string title in MDToolbar for the whole application."""

        self.main_widget.ids.toolbar.title = title

    def set_appbar(self):
        """Create MDBottomAppBar for the screen BottomAppBar."""

        from kivymd.toolbar import MDBottomAppBar

        def press_button(inctance):
            toast('Press Button')

        self.md_app_bar = MDBottomAppBar(
            md_bg_color=self.theme_cls.primary_color,
            left_action_items=[
                ['menu', lambda x: x],
                ['clock', lambda x: x],
                ['dots-vertical', lambda x: x]],
            anchor='right', callback=press_button)

    def move_item_menu(self, anchor):
        """Sets icons in MDBottomAppBar for the screen BottomAppBar."""

        md_app_bar = self.md_app_bar
        if md_app_bar.anchor != anchor:
            if len(md_app_bar.right_action_items):
                md_app_bar.left_action_items.append(
                    md_app_bar.right_action_items[0])
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
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'

    def set_error_message(self, *args):
        """Checks text of TextField with type "on_error"
        for the screen TextFields."""

        text_field_error = args[0]
        if len(text_field_error.text) == 2:
            text_field_error.error = True
        else:
            text_field_error.error = False

    def set_list_md_icons(self, text='', search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.main_widget.ids.scr_mngr.get_screen(
                'md icons').ids.rv.data.append(
                {
                    'viewclass': 'MDIconItemForMdIconsList',
                    'icon': name_icon,
                    'text': name_icon,
                    'callback': self.callback_for_menu_items
                }
            )

        self.main_widget.ids.scr_mngr.get_screen('md icons').ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def set_menu_for_demo_apps(self):
        if not len(self.menu_for_demo_apps):
            for name_item in self.demo_apps_list:
                self.menu_for_demo_apps.append(
                    {'viewclass': 'OneLineListItem',
                     'text': name_item,
                     'on_release': lambda x=name_item: self.show_demo_apps(x)})

    def show_demo_apps(self, name_item):
        self.show_screens_demo(name_item)
        self.main_widget.ids.scr_mngr.current = name_item.lower()
        self.instance_menu_demo_apps.dismiss()

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def open_settings(self, *args):
        return False


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


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class PopupScreen(MDPopupScreen):
    pass


class ImageTouch(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class ItemForListRefreshLayout(OneLineIconListItem):
    icon = StringProperty()


class MyCard(MDCard):
    text = StringProperty('')


if __name__ == '__main__':
    KitchenSink().run()
