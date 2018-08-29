# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker

main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
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
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Navigation Drawer"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Accordion"
            on_release: app.root.ids.scr_mngr.current = 'accordion'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Bottom Navigation"
            on_release: app.root.ids.scr_mngr.current = 'bottom_navigation'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Bottom Sheets"
            on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Buttons"
            on_release: app.root.ids.scr_mngr.current = 'button'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Cards"
            on_release: app.root.ids.scr_mngr.current = 'card'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Dialogs"
            on_release: app.root.ids.scr_mngr.current = 'dialog'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Grid lists"
            on_release: app.root.ids.scr_mngr.current = 'grid'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Labels"
            on_release: app.root.ids.scr_mngr.current = 'labels'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Lists"
            on_release: app.root.ids.scr_mngr.current = 'list'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Menus"
            on_release: app.root.ids.scr_mngr.current = 'menu'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Navigation Drawer Widgets"
            on_release: app.root.ids.scr_mngr.current = 'nav_drawer'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Pickers"
            on_release: app.root.ids.scr_mngr.current = 'pickers'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Progress & activity"
            on_release: app.root.ids.scr_mngr.current = 'progress'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Progress bars"
            on_release: app.root.ids.scr_mngr.current = 'progressbars'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Selection controls"
            on_release: app.root.ids.scr_mngr.current = 'selectioncontrols'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Sliders"
            on_release: app.root.ids.scr_mngr.current = 'slider'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Snackbars"
            on_release: app.root.ids.scr_mngr.current = 'snackbar'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Tabs"
            on_release: app.root.ids.scr_mngr.current = 'tabs'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Text fields"
            on_release: app.root.ids.scr_mngr.current = 'textfields'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Themes"
            on_release: app.root.ids.scr_mngr.current = 'theming'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Toolbars"
            on_release: app.root.ids.scr_mngr.current = 'toolbar'
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            id: toolbar
            title: 'KivyMD Kitchen Sink'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
        ScreenManager:
            id: scr_mngr
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
            Screen:
                name: 'button'
                BoxLayout:
                    size_hint: None, None
                    size: '88dp', '48dp'
                    padding: '12dp'
                    pos_hint: {'center_x': 0.75, 'center_y': 0.8}
                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                        text: "Disable buttons"
                        size_hint_x:None
                        width: '56dp'
                    MDCheckbox:
                        id: disable_the_buttons
                MDIconButton:
                    icon: 'sd'
                    pos_hint: {'center_x': 0.25, 'center_y': 0.8}
                    disabled: disable_the_buttons.active
                MDFlatButton:
                    text: 'MDFlatButton'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    disabled: disable_the_buttons.active
                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    disabled: disable_the_buttons.active
                MDFloatingActionButton:
                    id:                    float_act_btn
                    icon:                'plus'
                    opposite_colors:    True
                    elevation_normal:    8
                    pos_hint:            {'center_x': 0.5, 'center_y': 0.2}
                    disabled: disable_the_buttons.active
            Screen:
                name: 'card'
                MDCard:
                    size_hint: None, None
                    size:     dp(320), dp(180)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                MDCard:
                    size_hint: None, None
                    size: dp(320), dp(180)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    BoxLayout:
                        orientation:'vertical'
                        padding: dp(8)
                        MDLabel:
                            text: 'Title'
                            theme_text_color: 'Secondary'
                            font_style:"Title"
                            size_hint_y: None
                            height: dp(36)
                        MDSeparator:
                            height: dp(1)
                        MDLabel:
                            text: 'Body'
                            theme_text_color: 'Primary'
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
            Screen:
                name: 'dialog'
                MDRaisedButton:
                    text: "Open dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                    opposite_colors: True
                    on_release: app.show_example_dialog()
                MDRaisedButton:
                    text: "Open lengthy dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    opposite_colors: True
                    on_release: app.show_example_long_dialog()
            Screen:
                name: 'grid'
                ScrollView:
                    do_scroll_x: False
                    GridLayout:
                        cols: 3
                        row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
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
                            secondary_text: "This is a multi-line label where you can fit more text than usual"
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
                            secondary_text: "...with avatar..." + '\\n' + "and third line!"
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
                            secondary_text: "...with left icon..." + '\\n' + "and third line!"
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
                            secondary_text: "...with avatar&icon..." + '\\n' + "and third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
            Screen:
                name: 'menu'
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.1, 'center_y': 0.9}
                    on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.1, 'center_y': 0.1}
                    on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.9, 'center_y': 0.1}
                    on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.9, 'center_y': 0.9}
                    on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)

            Screen:
                name: 'progress'
                MDCheckbox:
                    id:            chkbox
                    size_hint:    None, None
                    size:        dp(48), dp(48)
                    pos_hint:    {'center_x': 0.5, 'center_y': 0.4}
                    active: True
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    active: True if chkbox.active else False
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

            Screen:
                name: 'selectioncontrols'
                MDCheckbox:
                    id:            grp_chkbox_1
                    group:        'test'
                    size_hint:    None, None
                    size:        dp(48), dp(48)
                    pos_hint:    {'center_x': 0.25, 'center_y': 0.5}
                MDCheckbox:
                    id:            grp_chkbox_2
                    group:        'test'
                    size_hint:    None, None
                    size:        dp(48), dp(48)
                    pos_hint:    {'center_x': 0.5, 'center_y': 0.5}
                MDSwitch:
                    size_hint:    None, None
                    size:        dp(36), dp(48)
                    pos_hint:    {'center_x': 0.75, 'center_y': 0.5}
                    _active:        False

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

            Screen:
                name: 'textfields'
                ScrollView:
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(48)
                        spacing: 10
                        MDTextField:
                            hint_text: "No helper text"
                        MDTextField:
                            hint_text: "Helper text on focus"
                            helper_text: "This will disappear when you click off"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            hint_text: "Persistent helper text"
                            helper_text: "Text is always here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            id: text_field_error
                            hint_text: "Helper text on error (Hit Enter with two characters here)"
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
                            helper_text: "Color is defined by \'line_color_focus\' property"
                            line_color_focus: self.theme_cls.opposite_bg_normal  # This is the color used by the textfield
                        MDTextField:
                            hint_text: "disabled = True"
                            disabled: True

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
                        on_release: MDThemePicker().open()
                        opposite_colors: True
                        pos_hint: {'center_x': 0.5}
                    MDLabel:
                        text: "Current: " + app.theme_cls.theme_style + ", " + app.theme_cls.primary_palette
                        theme_text_color: 'Primary'
                        pos_hint: {'center_x': 0.5}
                        halign: 'center'

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
                    md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                    background_palette: 'DeepPurple'
                    background_hue: 'A400'
                    left_action_items: [['arrow-left', lambda x: None]]
                    right_action_items: [['lock', lambda x: None], \
                        ['camera', lambda x: None], \
                        ['play', lambda x: None]]
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
                        on_state: tab_panel.tab_display_mode = 'icons' if tab_panel.tab_display_mode=='text' else 'text'
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
                        theme_text_color: 'Primary'
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
            Screen:
                name: 'nav_drawer'
                HackedDemoNavDrawer:
                    # NavigationDrawerToolbar:
                    #     title: "Navigation Drawer Widgets"
                    NavigationDrawerIconButton:
                        icon: 'checkbox-blank-circle'
                        text: "Badge text ---->"
                        badge_text: "99+"
                    NavigationDrawerIconButton:
                        active_color_type: 'accent'
                        text: "Accent active color"
                    NavigationDrawerIconButton:
                        active_color_type: 'custom'
                        text: "Custom active color"
                        active_color: [1, 0, 1, 1]
                    NavigationDrawerIconButton:
                        use_active: False
                        text: "Use active = False"
                    NavigationDrawerIconButton:
                        text: "Different icon"
                        icon: 'alarm'
                    NavigationDrawerDivider:
                    NavigationDrawerSubheader:
                        text: "NavigationDrawerSubheader"
                    NavigationDrawerIconButton:
                        text: "NavigationDrawerDivider \/"
                    NavigationDrawerDivider:

'''


class HackedDemoNavDrawer(MDNavigationDrawer):
    # DO NOT USE
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            # widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class KitchenSink(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "KivyMD Kitchen Sink"

    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
    ]

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'

        main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(main_widget)
        return main_widget

    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_1)

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def show_example_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="This is a test dialog",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_example_long_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Lorem ipsum dolor sit amet, consectetur "
                               "adipiscing elit, sed do eiusmod tempor "
                               "incididunt ut labore et dolore magna aliqua. "
                               "Ut enim ad minim veniam, quis nostrud "
                               "exercitation ullamco laboris nisi ut aliquip "
                               "ex ea commodo consequat. Duis aute irure "
                               "dolor in reprehenderit in voluptate velit "
                               "esse cillum dolore eu fugiat nulla pariatur. "
                               "Excepteur sint occaecat cupidatat non "
                               "proident, sunt in culpa qui officia deserunt "
                               "mollit anim id est laborum.",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="This is a long test dialog",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.bind(time=self.get_time_picker_data)
        if self.root.ids.time_picker_use_previous_time.active:
            try:
                self.time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        self.time_dialog.open()

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
        bs = MDListBottomSheet()
        bs.add_item("Here's an item with text only", lambda x: x)
        bs.add_item("Here's an item with an icon", lambda x: x,
                    icon='clipboard-account')
        bs.add_item("Here's another!", lambda x: x, icon='nfc')
        bs.open()

    def show_example_grid_bottom_sheet(self):
        bs = MDGridBottomSheet()
        bs.add_item("Facebook", lambda x: x,
                    icon_src='./assets/facebook-box.png')
        bs.add_item("YouTube", lambda x: x,
                    icon_src='./assets/youtube-play.png')
        bs.add_item("Twitter", lambda x: x,
                    icon_src='./assets/twitter.png')
        bs.add_item("Da Cloud", lambda x: x,
                    icon_src='./assets/cloud-upload.png')
        bs.add_item("Camera", lambda x: x,
                    icon_src='./assets/camera.png')
        bs.open()

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


if __name__ == '__main__':
    KitchenSink().run()
