# -*- coding: utf-8 -*-

import os
import sys

from kivy.metrics import dp
from kivy.uix.widget import Widget

sys.path.append(os.path.abspath(__file__).split('demos')[0])

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color

from kivymd.fanscreenmanager import MDFanScreen
from kivymd.popupscreen import MDPopupScreen
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDInputDialog, MDDialog
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.material_resources import DEVICE_TYPE
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theme_picker import MDThemePicker
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.card import MDCardPost
from kivymd.filemanager import MDFileManager
from kivymd.progressloader import MDProgressLoader
from kivymd.stackfloatingbuttons import MDStackFloatingButtons
from kivymd.useranimationcard import MDUserAnimationCard
from kivymd.accordionlistitem import MDAccordionListItem
# FIXME: crush with Python3.
try:
    from kivymd.toast import toast
except TypeError:
    from kivymd.toast.kivytoast import toast

main_widget_kv = """
#:import Clock kivy.clock.Clock
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import get_color_from_hex kivy.utils.get_color_from_hex

#:import images_path kivymd.images_path
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDTextFieldClear kivymd.textfields.MDTextFieldClear
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton
#:import MDRectangleFlatIconButton kivymd.button.MDRectangleFlatIconButton
#:import MDTextButton kivymd.button.MDTextButton
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import MDUpdateSpinner kivymd.updatespinner.MDUpdateSpinner
#:import MDFanScreenManager kivymd.fanscreenmanager.MDFanScreenManager
#:import MDChip kivymd.chips.MDChip


<ContentPopup@BoxLayout>:
    orientation: 'vertical'
    padding: dp(1)
    spacing: dp(30)

    Image:
        id: image
        source: 'assets/guitar-1139397_1280.jpg'
        size_hint: 1, None
        height: dp(Window.height * 35 // 100)
        allow_stretch: True
        keep_ratio: False

    MDRoundFlatButton:
        text: 'Open Menu'
        pos_hint: {'center_x': .5}
        on_release: root.parent.show()

    Widget:


<BaseFanScreen>:
    orientation: 'vertical'

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: root.path_to_image
        size_hint: 1, None
        height: Window.height * 40 // 100
        y: Window.height - self.height
        allow_stretch: True
        keep_ratio: False

    ContentForAnimCard:


<ContentForAnimCard>:
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


<MyNavigationDrawerIconButton@NavigationDrawerIconButton>:
    icon: 'checkbox-blank-circle'


<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: './assets/drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu of Examples:"
    MyNavigationDrawerIconButton:
        text: "Accordion"
        on_release: app.root.ids.scr_mngr.current = 'accordion'
    MyNavigationDrawerIconButton:
        text: "Accordion List"
        on_release: app.root.ids.scr_mngr.current = 'accordion list'
    MyNavigationDrawerIconButton:
        text: "Bottom Navigation"
        on_release: app.root.ids.scr_mngr.current = 'bottom_navigation'
    MyNavigationDrawerIconButton:
        text: "Bottom Sheets"
        on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
    MyNavigationDrawerIconButton:
        text: "Buttons"
        on_release: app.root.ids.scr_mngr.current = 'button'
    MyNavigationDrawerIconButton:
        text: "Cards"
        on_release: app.root.ids.scr_mngr.current = 'card'
    MyNavigationDrawerIconButton:
        text: "Chips"
        on_release: app.root.ids.scr_mngr.current = 'chips'
    MyNavigationDrawerIconButton:
        text: "Dialogs"
        on_release: app.root.ids.scr_mngr.current = 'dialog'
    MyNavigationDrawerIconButton:
        text: "Download File"
        on_release: app.root.ids.scr_mngr.current = 'download file'
    MyNavigationDrawerIconButton:
        text: "Files Manager"
        on_release: app.root.ids.scr_mngr.current = 'files manager'
    MyNavigationDrawerIconButton:
        text: "Fan Manager"
        on_release: app.root.ids.scr_mngr.current = 'fan manager'
    MyNavigationDrawerIconButton:
        text: "Grid lists"
        on_release: app.root.ids.scr_mngr.current = 'grid'
    MyNavigationDrawerIconButton:
        text: "Labels"
        on_release: app.root.ids.scr_mngr.current = 'labels'
    MyNavigationDrawerIconButton:
        text: "Lists"
        on_release: app.root.ids.scr_mngr.current = 'list'
    MyNavigationDrawerIconButton:
        text: "Menus"
        on_release: app.root.ids.scr_mngr.current = 'menu'
    MyNavigationDrawerIconButton:
        text: "Pickers"
        on_release: app.root.ids.scr_mngr.current = 'pickers'
    MyNavigationDrawerIconButton:
        text: "Progress & activity"
        on_release: app.root.ids.scr_mngr.current = 'progress'
    MyNavigationDrawerIconButton:
        text: "Popup Screen"
        on_release: app.root.ids.scr_mngr.current = 'popup screen'
    MyNavigationDrawerIconButton:
        text: "Progress bars"
        on_release: app.root.ids.scr_mngr.current = 'progressbars'
    MyNavigationDrawerIconButton:
        text: "Selection controls"
        on_release: app.root.ids.scr_mngr.current = 'selectioncontrols'
    MyNavigationDrawerIconButton:
        text: "Sliders"
        on_release: app.root.ids.scr_mngr.current = 'slider'
    MyNavigationDrawerIconButton:
        text: "Stack Floating Buttons"
        on_release: app.root.ids.scr_mngr.current = 'stack buttons'
    MyNavigationDrawerIconButton:
        text: "Snackbars"
        on_release: app.root.ids.scr_mngr.current = 'snackbar'
    MyNavigationDrawerIconButton:
        text: "Tabs"
        on_release: app.root.ids.scr_mngr.current = 'tabs'
    MyNavigationDrawerIconButton:
        text: "Text fields"
        on_release: app.root.ids.scr_mngr.current = 'textfields'
    MyNavigationDrawerIconButton:
        text: "Themes"
        on_release: app.root.ids.scr_mngr.current = 'theming'
    MyNavigationDrawerIconButton:
        text: "Toolbars"
        on_release: app.root.ids.scr_mngr.current = 'toolbar'
    MyNavigationDrawerIconButton:
        text: "Update Screen Widget"
        on_release: app.root.ids.scr_mngr.current = 'update spinner'
    MyNavigationDrawerIconButton:
        text: "User Animation Card"
        on_release: app.root.ids.scr_mngr.current = 'user animation card'


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: 'vertical'

        Toolbar:
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

            Screen:
                name: 'previous'

                FloatLayout:
                    Image:
                        source: '{}kivymd_logo.png'.format(images_path)
                        opacity: .3

                MDLabel:
                    text: app.previous_text
                    size_hint_y: None
                    font_style: 'Subhead'
                    theme_text_color: 'Primary'
                    markup: True
                    halign: 'center'
                    text_size: self.width - 20, None
                    pos_hint: {'center_x': .5, 'center_y': .6}

            ###################################################################
            #
            #                          BOTTOM SHEET
            #
            ###################################################################

            Screen:
                name: 'bottomsheet'

                MDRaisedButton:
                    text: "Open list bottom sheet"
                    opposite_colors: True
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    on_release: app.show_example_bottom_sheet()

                MDRaisedButton:
                    text: "Open grid bottom sheet"
                    opposite_colors: True
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: app.show_example_grid_bottom_sheet()

            ###################################################################
            #
            #                            BUTTONS
            #
            ###################################################################

            Screen:
                name: 'button'

                BoxLayout:
                    size_hint_y: None
                    height: '56'
                    spacing: '10dp'
                    pos_hint: {'center_y': .9}

                    Widget:

                    MDIconButton:
                        icon: 'sd'

                    MDFloatingActionButton:
                        icon: 'plus'
                        opposite_colors: True
                        elevation_normal: 8

                    MDFloatingActionButton:
                        icon: 'check'
                        opposite_colors: True
                        elevation_normal: 8
                        md_bg_color: app.theme_cls.primary_color

                    MDIconButton:
                        icon: 'sd'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color

                    Widget:

                MDFlatButton:
                    text: 'MDFlatButton'
                    pos_hint: {'center_x': 0.5, 'center_y': .75}

                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': .65}

                MDRectangleFlatButton:
                    text: "MDRectangleFlatButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .55}

                MDRectangleFlatIconButton:
                    text: "MDRectangleFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': 0.5, 'center_y': .45}
                    width: dp(230)

                MDRoundFlatButton:
                    text: "MDROUNDFLATBUTTON"
                    pos_hint: {'center_x': 0.5, 'center_y': .35}

                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': 0.5, 'center_y': .25}
                    width: dp(200)

                MDFillRoundFlatButton:
                    text: "MDFillRoundFlatButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .15}

                MDTextButton:
                    text: "MDTextButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .05}

            ###################################################################
            #
            #                            CARDS
            #
            ###################################################################

            Screen:
                name: 'card'
                on_enter: app.add_cards(grid_card)

                ScrollView:
                    id: scroll
                    size_hint: 1, 1
                    do_scroll_x: False

                    GridLayout:
                        id: grid_card
                        cols: 1
                        spacing: dp(5)
                        padding: dp(5)
                        size_hint_y: None
                        height: self.minimum_height

                        # See how to add a card with the menu and others
                        # in the add_cards function.

            ###################################################################
            #
            #                        DOWNLOAD FILE
            #
            ###################################################################

            Screen:
                name: 'download file'

                FloatLayout:
                    id: box_flt

                    MDRaisedButton:
                        text: "Download file"
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        opposite_colors: True
                        on_release:
                            Clock.schedule_once(\
                            app.show_example_download_file, .1)

            ###################################################################
            #
            #                            DIALOGS
            #
            ###################################################################

            Screen:
                name: 'dialog'

                MDRaisedButton:
                    text: "Open lengthy dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                    opposite_colors: True
                    on_release: app.show_example_long_dialog()

                MDRaisedButton:
                    text: "Open input dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    opposite_colors: True
                    on_release: app.show_example_input_dialog()

                MDRaisedButton:
                    text: "Open Alert Dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    opposite_colors: True
                    on_release: app.show_example_alert_dialog()

                MDRaisedButton:
                    text: "Open Ok Cancel Dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    opposite_colors: True
                    on_release: app.show_example_ok_cancel_dialog()

            ###################################################################
            #
            #                             GRID
            #
            ###################################################################

            Screen:
                name: 'grid'

                ScrollView:
                    do_scroll_x: False

                    GridLayout:
                        cols: 3
                        row_default_height:
                            (self.width - self.cols*self.spacing[0])/self.cols
                        row_force_default: True
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(4), dp(4)
                        spacing: dp(4)

                        SmartTileWithLabel:
                            mipmap: True
                            source: './assets/african-lion-951778_1280.jpg'
                            text: "African Lion"
                        SmartTile:
                            mipmap: True
                            source: './assets/beautiful-931152_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/african-lion-951778_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/guitar-1139397_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/robin-944887_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/kitten-1049129_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/light-bulb-1042480_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/tangerines-1111529_1280.jpg'

            ###################################################################
            #
            #                             LABELS
            #
            ###################################################################

            Screen:
                name: 'labels'

                ScrollView:
                    do_scroll_x: False

                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(1000)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Body1 label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body2'
                                theme_text_color: 'Primary'
                                text: "Body2 label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Caption'
                                theme_text_color: 'Primary'
                                text: "Caption label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Subhead'
                                theme_text_color: 'Primary'
                                text: "Subhead label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Title'
                                theme_text_color: 'Primary'
                                text: "Title label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Headline'
                                theme_text_color: 'Primary'
                                text: "Headline label"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Display1'
                            theme_text_color: 'Primary'
                            text: "Display1 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display2'
                            theme_text_color: 'Primary'
                            text: "Display2 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display3'
                            theme_text_color: 'Primary'
                            text: "Display3 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display4'
                            theme_text_color: 'Primary'
                            text: "Display4 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Primary color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Secondary'
                                text: "Secondary color"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Hint'
                                text: "Hint color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Error'
                                text: "Error color"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Custom'
                            text_color: (0,1,0,.4)
                            text: "Custom"
                            halign: 'center'

            ###################################################################
            #
            #                             LISTS
            #
            ###################################################################

            Screen:
                name: 'list'

                ScrollView:
                    do_scroll_x: False

                    MDList:
                        id: ml
                        OneLineListItem:
                            text: "One-line item"
                        TwoLineListItem:
                            text: "Two-line item"
                            secondary_text: "Secondary text here"
                        ThreeLineListItem:
                            text: "Three-line item"
                            secondary_text:
                                "This is a multi-line label where you can " \
                                "fit more text than usual"
                        OneLineAvatarListItem:
                            text: "Single-line item with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        TwoLineAvatarListItem:
                            type: "two-line"
                            text: "Two-line item..."
                            secondary_text: "with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        ThreeLineAvatarListItem:
                            type: "three-line"
                            text: "Three-line item..."
                            secondary_text:
                                "...with avatar..." + '\\n' + "and third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        OneLineIconListItem:
                            text: "Single-line item with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_1
                                icon: 'star-circle'
                        TwoLineIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_2
                                icon: 'comment-text'
                        ThreeLineIconListItem:
                            text: "Three-line item..."
                            secondary_text:
                                "...with left icon..." + '\\n' + "and " \
                                "third line!"
                            IconLeftSampleWidget:
                                id: li_icon_3
                                icon: 'sd'
                        OneLineAvatarIconListItem:
                            text: "Single-line + avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        TwoLineAvatarIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        ThreeLineAvatarIconListItem:
                            text: "Three-line item..."
                            secondary_text:
                                "...with avatar&icon..." + '\\n' + "and " \
                                "third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:

            ###################################################################
            #
            #                        ACCORDION LIST
            #
            ###################################################################

            Screen:
                name: 'accordion list'
                on_enter: app.set_accordion_list()
                on_leave: anim_list.clear_widgets()

                ScrollView:
                
                    GridLayout:
                        id: anim_list
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

            ###################################################################
            #
            #                         FILES MANAGER
            #
            #       See the help on using the file in the file filemanager.py
            #
            ###################################################################

            Screen:
                name: 'files manager'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open files manager'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.file_manager_open()

            ###################################################################
            #
            #                             MENUS
            #
            ###################################################################

            Screen:
                name: 'menu'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.2, 'center_y': 0.9}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.2, 'center_y': 0.1}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.8, 'center_y': 0.1}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.8, 'center_y': 0.9}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=4).open(self)

            ###################################################################
            #
            #                              CHIPS
            #
            ###################################################################

            Screen:
                name: 'chips'

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)

                    Image:
                        source: 'assets/guitar-1139397_1280.jpg'
                        size_hint: 1, None
                        height: dp(Window.height * 35 // 100)
                        allow_stretch: True
                        keep_ratio: False

                    StackLayout:
                        padding: dp(5)
                        spacing: dp(5)

                        MDChip:
                            label: 'Coffee'
                            color: .4470588235294118, .19607843137254902, 0, 1
                            icon: 'coffee'
                            callback: app.callback_for_menu_items

                        MDChip:
                            label: 'Duck'
                            color: .9215686274509803, 0, 0, 1
                            icon: 'duck'
                            callback: app.callback_for_menu_items

                        MDChip:
                            label: 'Earth'
                            color: .21176470588235294, .09803921568627451, 1, 1
                            icon: 'earth'
                            callback: app.callback_for_menu_items

                        MDChip:
                            label: 'Face'
                            color: .2039215698, .48235297606, .435764705883, 1
                            icon: 'face'
                            callback: app.callback_for_menu_items

                        MDChip:
                            label: 'Facebook'
                            color: .56078431374902, .4823529706, .43529483, 1
                            icon: 'facebook'
                            callback: app.callback_for_menu_items

                        MDChip:
                            label: 'Without icon'
                            icon: ''
                            callback: app.callback

                        MDChip:
                            label: 'Check'
                            icon: ''
                            check: True
                            callback: app.callback

                        MDChip:
                            label: 'Check with icon'
                            icon: 'city'
                            check: True
                            callback: app.callback

                    Widget:

            ###################################################################
            #
            #                             CHECKBOX
            #
            ###################################################################

            Screen:
                name: 'progress'

                MDCheckbox:
                    id: chkbox
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    active: True
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    active: True if chkbox.active else False

            ###################################################################
            #
            #                           FAN MANAGER
            #
            ###################################################################

            Screen:
                name: 'fan manager'
                on_enter:
                    toolbar.left_action_items = \
                    [['menu', lambda x: fan_screen_manager.open_fan()]]
                on_leave: app.set_chevron_menu()

                MDFanScreenManager:
                    id: fan_screen_manager
    
                    canvas:
                        Color:
                            rgba: 0, 0, 0, .2
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    ScreenOne:
                        name: 'Screen One'
                        path_to_image: 'assets/african-lion-951778_1280.jpg'
                        on_enter: toolbar.title = self.name

                    ScreenTwo:
                        name: 'Screen Two'
                        path_to_image: 'assets/beautiful-931152_1280.jpg'
                        on_enter: toolbar.title = self.name

                    ScreenTree:
                        name: 'Screen Tree'
                        path_to_image: 'assets/kitten-1049129_1280.jpg'
                        on_enter: toolbar.title = self.name

                    ScreenFour:
                        name: 'Screen Four'
                        path_to_image: 'assets/tangerines-1111529_1280.jpg'
                        on_enter: toolbar.title = self.name

            ###################################################################
            #
            #                          POPUP SCREEN
            #
            ###################################################################

            Screen:
                name: 'popup screen'
                on_enter: app.set_popup_screen(content_popup)

                PopupScreen:
                    id: popup_screen

                    ContentPopup:
                        id: content_popup

            ###################################################################
            #
            #                          PROGRESS BAR
            #
            ###################################################################

            Screen:
                name: 'progressbars'

                BoxLayout:
                    orientation:'vertical'
                    padding: '8dp'

                    MDSlider:
                        id:progress_slider
                        min:0
                        max:100
                        value: 40

                    MDProgressBar:
                        value: progress_slider.value
                    MDProgressBar:
                        reversed: True
                        value: progress_slider.value

                    BoxLayout:
                        MDProgressBar:
                            orientation:"vertical"
                            reversed: True
                            value: progress_slider.value

                        MDProgressBar:
                            orientation:"vertical"
                            value: progress_slider.value

            ###################################################################
            #
            #                         UPDATE SPINNER
            #
            ###################################################################

            Screen:
                name: 'update spinner'
                on_enter: upd_lbl.text = "Pull to string update"
                on_leave: upd_lbl.text = ""

                MDLabel:
                    id: upd_lbl
                    font_style: 'Display2'
                    theme_text_color: 'Primary'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    size_hint_y: None
                    height: self.texture_size[1] + dp(4)

                MDUpdateSpinner:
                    event_update: lambda x: app.update_screen(self)

            ###################################################################
            #
            #                     STACK FLOATING BUTTONS
            #
            ###################################################################

            Screen:
                name: 'stack buttons'
                on_enter: app.example_add_stack_floating_buttons()

            ###################################################################
            #
            #                          SLIDER
            #
            ###################################################################

            Screen:
                name: 'slider'

                BoxLayout:
                    MDSlider:
                        id: hslider
                        min:0
                        max:100
                        value: 10
                    MDSlider:
                        id: vslider
                        orientation:'vertical'
                        min:0
                        max:100
                        value: hslider.value

            ###################################################################
            #
            #                      USER ANIMATION CARD
            #
            ###################################################################

            Screen:
                name: 'user animation card'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open card'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    on_release: app.show_user_example_animation_card()

            ###################################################################
            #
            #                      SELECTION CONTROLS
            #
            ###################################################################

            Screen:
                name: 'selectioncontrols'

                MDCheckbox:
                    id: grp_chkbox_1
                    group: 'test'
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.25, 'center_y': 0.5}
                MDCheckbox:
                    id: grp_chkbox_2
                    group: 'test'
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDSwitch:
                    size_hint: None, None
                    size: dp(36), dp(48)
                    pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                    _active: False

            ###################################################################
            #
            #                           SNACKBAR
            #
            ###################################################################

            Screen:
                name: 'snackbar'

                MDRaisedButton:
                    text: "Create simple snackbar"
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('simple')
                MDRaisedButton:
                    text: "Create snackbar with button"
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('button')
                MDRaisedButton:
                    text: "Create snackbar with a lot of text"
                    size_hint: None, None
                    size: 5 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('verylong')

            ###################################################################
            #
            #                         TEXTFIELDS
            #
            ###################################################################

            Screen:
                name: 'textfields'

                ScrollView:

                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(48)
                        spacing: dp(10)

                        MDTextField:
                            hint_text: "No helper text"
                        MDTextField:
                            hint_text: "Helper text on focus"
                            helper_text:
                                "This will disappear when you click off"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            hint_text: "Persistent helper text"
                            helper_text: "Text is always here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            id: text_field_error
                            hint_text:
                                "Helper text on error (Hit Enter with " \
                                "two characters here)"
                            helper_text: "Two is my least favorite number"
                            helper_text_mode: "on_error"
                        MDTextField:
                            hint_text: "Max text length = 10"
                            max_text_length: 10
                        MDTextField:
                            hint_text: "required = True"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            multiline: True
                            hint_text: "Multi-line text"
                            helper_text: "Messages are also supported here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            hint_text: "color_mode = \'accent\'"
                            color_mode: 'accent'
                        MDTextField:
                            hint_text: "color_mode = \'custom\'"
                            color_mode: 'custom'
                            helper_text_mode: "on_focus"
                            helper_text:
                                "Color is defined by \'line_color_focus\' " \
                                "property"
                            line_color_focus:
                                # This is the color used by the textfield
                                self.theme_cls.opposite_bg_normal
                        MDTextField:
                            hint_text: "disabled = True"
                            disabled: True
                        MDTextFieldRect:
                            size_hint: None, None
                            size: app.Window.width - dp(40), dp(30)
                            pos_hint: {'center_y': .5, 'center_x': .5}
                        MDTextFieldClear:
                            hint_text: "Text field with clearing type"

            ###################################################################
            #
            #                          THEMING
            #
            ###################################################################

            Screen:
                name: 'theming'

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(80)
                    center_y: self.parent.center_y

                    MDRaisedButton:
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        center_x: self.parent.center_x
                        text: 'Change theme'
                        on_release: app.theme_picker_open()
                        opposite_colors: True
                        pos_hint: {'center_x': 0.5}
                    MDLabel:
                        text:
                            "Current: " + app.theme_cls.theme_style + \
                            ", " + app.theme_cls.primary_palette
                        theme_text_color: 'Primary'
                        pos_hint: {'center_x': 0.5}
                        halign: 'center'

            ###################################################################
            #
            #                         TOOLBARS
            #
            ###################################################################

            Screen:
                name: 'toolbar'

                Toolbar:
                    title: "Simple toolbar"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                    md_bg_color: get_color_from_hex(colors['Teal']['500'])
                    background_palette: 'Teal'
                    background_hue: '500'

                Toolbar:
                    title: "Toolbar with right buttons"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: get_color_from_hex(colors['Amber']['700'])
                    background_palette: 'Amber'
                    background_hue: '700'
                    right_action_items: [['content-copy', lambda x: None]]
    
                Toolbar:
                    title: "Toolbar with left and right buttons"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                    md_bg_color:
                        get_color_from_hex(colors['DeepPurple']['A400'])
                    background_palette: 'DeepPurple'
                    background_hue: 'A400'
                    left_action_items: [['arrow-left', lambda x: None]]
                    right_action_items: [['lock', lambda x: None], \
                        ['camera', lambda x: None], \
                        ['play', lambda x: None]]

            ###################################################################
            #
            #                              TABS
            #
            ###################################################################

            Screen:
                name: 'tabs'

                MDTabbedPanel:
                    id: tab_panel
                    tab_display_mode:'text'

                    MDTab:
                        name: 'music'
                        text: "Music" # Why are these not set!!!
                        icon: "playlist-play"
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Here is my music list :)"
                            halign: 'center'
                    MDTab:
                        name: 'movies'
                        text: 'Movies'
                        icon: "movie"

                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Show movies here :)"
                            halign: 'center'

                BoxLayout:
                    size_hint_y:None
                    height: '48dp'
                    padding: '12dp'

                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                        text: "Use icons"
                        size_hint_x:None
                        width: '64dp'
                    MDCheckbox:
                        on_state:
                            tab_panel.tab_display_mode = 'icons' \
                            if tab_panel.tab_display_mode=='text' else 'text'

            ###################################################################
            #
            #                            ACCORDION
            #
            ###################################################################

            Screen:
                name: 'accordion'

                BoxLayout:

                    MDAccordion:
                        orientation: 'vertical'
                        size_hint_x: None
                        width: '240dp'

                        MDAccordionItem:
                            title:'Item 1'
                            icon: 'home'
                            MDAccordionSubItem:
                                text: "Subitem 1"
                            MDAccordionSubItem:
                                text: "Subitem 2"
                            MDAccordionSubItem:
                                text: "Subitem 3"
                        MDAccordionItem:
                            title:'Item 2'
                            icon: 'earth'
                            MDAccordionSubItem:
                                text: "Subitem 4"
                            MDAccordionSubItem:
                                text: "Subitem 5"
                            MDAccordionSubItem:
                                text: "Subitem 6"
                        MDAccordionItem:
                            title:'Item 3'
                            icon: 'account'
                            MDAccordionSubItem:
                                text: "Subitem 7"
                            MDAccordionSubItem:
                                text: "Subitem 8"
                            MDAccordionSubItem:
                                text: "Subitem 9"

                    MDLabel:
                        text: 'Content'
                        halign: 'center'
                        theme_text_color: 'Primary'

            ###################################################################
            #
            #                           PICKERS
            #
            ###################################################################

            Screen:
                name: 'pickers'

                BoxLayout:
                    spacing: dp(40)
                    orientation: 'vertical'
                    size_hint_x: None
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    BoxLayout:
                        orientation: 'vertical'
                        # size_hint: (None, None)

                        MDRaisedButton:
                            text: "Open time picker"
                            size_hint: None, None
                            size: 3 * dp(48), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            opposite_colors: True
                            on_release: app.show_example_time_picker()
                        MDLabel:
                            id: time_picker_label
                            theme_text_color: 'Primary'
                            size_hint: None, None
                            size: dp(48)*3, dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        BoxLayout:
                            size: dp(48)*3, dp(48)
                            size_hint: (None, None)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            MDLabel:
                                theme_text_color: 'Primary'
                                text: "Start on previous time"
                                size_hint: None, None
                                size: dp(130), dp(48)
                            MDCheckbox:
                                id: time_picker_use_previous_time
                                size_hint: None, None
                                size: dp(48), dp(48)

                    BoxLayout:
                        orientation: 'vertical'

                        MDRaisedButton:
                            text: "Open date picker"
                            size_hint: None, None
                            size: 3 * dp(48), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            opposite_colors: True
                            on_release: app.show_example_date_picker()
                        MDLabel:
                            id: date_picker_label
                            theme_text_color: 'Primary'
                            size_hint: None, None
                            size: dp(48)*3, dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        BoxLayout:
                            size: dp(48)*3, dp(48)
                            size_hint: (None, None)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            MDLabel:
                                theme_text_color: 'Primary'
                                text: "Start on previous date"
                                size_hint: None, None
                                size: dp(130), dp(48)
                            MDCheckbox:
                                id: date_picker_use_previous_date
                                size_hint: None, None
                                size: dp(48), dp(48)

            ###################################################################
            #
            #                       BOTTOM NAVIGATION
            #
            ###################################################################

            Screen:
                name: 'bottom_navigation'

                MDBottomNavigation:
                    id: bottom_navigation_demo

                    MDBottomNavigationItem:
                        name: 'octagon'
                        text: "Warning"
                        icon: "alert-octagon"
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Warning!"
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'banking'
                        text: "Bank"
                        icon: 'bank'
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: dp(48)
                            spacing: 10
                            MDTextField:
                                hint_text: "You can put any widgets here"
                                helper_text: "Hello :)"
                                helper_text_mode: "on_focus"

                    MDBottomNavigationItem:
                        name: 'bottom_navigation_desktop_1'
                        text: "Hello"
                        icon: 'alert'
                        id: bottom_navigation_desktop_1
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: dp(48)
                            spacing: 10
                            MDTextField:
                                hint_text: "Hello again"

                    MDBottomNavigationItem:
                        name: 'bottom_navigation_desktop_2'
                        text: "Food"
                        icon: 'food'
                        id: bottom_navigation_desktop_2
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Cheese!"
                            halign: 'center'
"""


class KitchenSink(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    previous_date = ObjectProperty()
    title = "Kitchen Sink"

    def __init__(self, **kwargs):
        super(KitchenSink, self).__init__(**kwargs)

        self.menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': self.callback_for_menu_items}
            for i in range(15)
        ]
        self.Window = Window
        self.manager = False
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.user_animation_card = None
        self.manager_open = False
        self.cards_created = False
        self.file_manager = None
        self.bs_menu_1 = None
        self.bs_menu_2 = None
        self.tick = 0
        self.create_stack_floating_buttons = False
        self.previous_text = \
            "Welcome to the application [b][color={COLOR}]Kitchen Sink" \
            "[/color][/b].\nTo see [b][color={COLOR}]KivyMD[/color][/b] " \
            "examples, open the menu and select from the list the desired " \
            "example\n\n" \
            "" \
            "" \
            "Author - [b][color={COLOR}]Andrés Rodríguez[/color][/b]\n" \
            "[u][b][color={COLOR}]andres.rodriguez@lithersoft.com[/color]" \
            "[/b][/u]\n\n" \
            "Author this Fork - [b][color={COLOR}]Ivanov Yuri[/color][/b]\n" \
            "[u][b][color={COLOR}]kivydevelopment@gmail.com[/color]" \
            "[/b][u]".format(COLOR=get_hex_from_color(
                self.theme_cls.primary_color))
        self.names_contacts = (
            'Alexandr Taylor', 'Yuri Ivanov', 'Robert Patric', 'Bob Marley',
            'Magnus Carlsen', 'Jon Romero', 'Anna Bell', 'Maxim Kramerer',
            'Sasha Gray', 'Vladimir Ivanenko'
        )
        Window.bind(on_keyboard=self.events)

    def theme_picker_open(self):
        if not self.md_theme_picker:
            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open()

    def example_add_stack_floating_buttons(self):
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
        def callback(text):
            toast('{} to {}'.format(text, content.name_item))

        content = ContentForAnimCard(callback=callback)

        for name_contact in self.names_contacts:
            self.main_widget.ids.anim_list.add_widget(
                MDAccordionListItem(content=content,
                                    icon='assets/kivymd_logo.png',
                                    title=name_contact))

    def set_chevron_back_screen(self):
        """Sets the return chevron to the previous screen in ToolBar."""

        self.main_widget.ids.toolbar.right_action_items = [
            ['dots-vertical', lambda x: self.root.toggle_nav_drawer()]]

    def download_progress_hide(self, instance_progress, value):
        """Hides progress progress."""

        self.main_widget.ids.toolbar.right_action_items = \
            [['download',
              lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port))
                return True
            except Exception:
                return False

        if get_connect():
            link = 'https://www.python.org/ftp/python/3.5.1/' \
                   'python-3.5.1-embed-win32.zip'
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide
            )
            progress.start(self.main_widget.ids.box_flt)
        else:
            toast('Connect error!')

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')

    def file_manager_open(self):
        def file_manager_open(text_item):
            previous = False if text_item == 'List' else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path,
                                              previous=previous)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title='Title', size_hint=(.8, .4), text_button_ok='List',
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel='Previous',
            events_callback=file_manager_open).open()

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
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def callback_for_menu_items(self, text_item):
        toast(text_item)

    def add_cards(self, instance_grid_card):
        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                toast('Delete post %s' % str(instance))

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
                    source="./assets/kitten-1049129_1280.jpg",
                    tile_text="Little Baby",
                    tile_font_style="Headline",
                    text_post="This is my favorite cat. He's only six months "
                              "old. He loves milk and steals sausages :) "
                              "And he likes to play in the garden.",
                    with_image=True, swipe=True, callback=callback,
                    buttons=buttons))

    def update_screen(self, instance):
        def update_screen(interval):
            self.tick += 1
            if self.tick > 2:
                instance.update = True
                self.tick = 0
                self.main_widget.ids.upd_lbl.text = "New string"
                Clock.unschedule(update_screen)

        Clock.schedule_interval(update_screen, 1)

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'

        self.main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(self.main_widget)
        return self.main_widget

    def set_popup_screen(self, content_popup):
        popup_menu = ContentForAnimCard()
        popup_menu.add_widget(Widget(size_hint_y=None, height=dp(150)))
        popup_screen = self.main_widget.ids.popup_screen
        popup_screen.screen = popup_menu
        popup_screen.background_color = [.3, .3, .3, 1]
        popup_screen.max_height = content_popup.ids.image.height + dp(5)

    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_1)

    def show_user_example_animation_card(self):
        def main_back_callback():
            toast('Close card')

        if not self.user_animation_card:
            self.user_animation_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar="./assets/guitar-1139397_1280.jpg",
                callback=main_back_callback)
            self.user_animation_card.box_content.add_widget(
                ContentForAnimCard())
        self.user_animation_card.open()

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()

    def show_example_input_dialog(self):
        if not self.input_dialog:
            self.input_dialog = MDInputDialog(
                title='Title', hint_text='Hint text', size_hint=(.8, .4),
                text_button_ok='Ok', events_callback=lambda x: None)
        self.input_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Alert dialog",
                events_callback=self.callback_for_menu_items)
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            self.ok_cancel_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Ok Cancel dialog", text_button_cancel='Cancel',
                events_callback=self.callback_for_menu_items)
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
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

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_data)

        if self.root.ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.root.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        if self.root.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def show_example_bottom_sheet(self):
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
        if not self.bs_menu_2:
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

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

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


if __name__ == '__main__':
    KitchenSink().run()
