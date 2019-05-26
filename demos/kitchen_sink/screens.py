"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

import os

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp

from kivymd.utils.cropimage import crop_image

bottom_app_bar = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton


<BottomAppBar@Screen>
    name: 'bottom app bar'

    MDRaisedButton:
        text: 'Anchor center'
        pos_hint: {'center_y': .7, 'center_x': .5}
        on_release:
            app.md_app_bar.set_pos_action_button('center')
            app.move_item_menu('center')

    MDRaisedButton:
        text: 'Anchor right'
        pos_hint: {'center_y': .5, 'center_x': .5}
        on_release:
            app.md_app_bar.set_pos_action_button('right')
            app.move_item_menu('right')
'''

accordion_list = '''
<AccordionList@Screen>
    name: 'accordion list'
    on_enter: app.set_accordion_list()
    on_leave: anim_list.clear_widgets()

    ScrollView:

        GridLayout:
            id: anim_list
            cols: 1
            size_hint_y: None
            height: self.minimum_height
'''

bottom_sheet = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton


<BottomSheet@Screen>
    name: 'bottom sheet'

    MDRaisedButton:
        text: "Open list bottom sheet"
        opposite_colors: True
        size_hint: None, None
        size: 4 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .6}
        on_release: app.show_example_bottom_sheet()

    MDRaisedButton:
        text: "Open grid bottom sheet"
        opposite_colors: True
        size_hint: None, None
        size: 4 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .3}
        on_release: app.show_example_grid_bottom_sheet()
'''

accordion = '''
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem


<Accord@Screen>
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
'''

grid = '''
#:import SmartTileWithStar kivymd.imagelists.SmartTileWithStar
#:import SmartTileWithLabel kivymd.imagelists.SmartTileWithLabel


<Grid@Screen>
    name: 'grid'

    on_enter:
        app.crop_image_for_tile(tile_1, tile_1.size, 'assets/beautiful-931152_1280_tile_crop.png')
        app.crop_image_for_tile(tile_2, tile_2.size, 'assets/african-lion-951778_1280_tile_crop.png')
        app.crop_image_for_tile(tile_3, tile_3.size, 'assets/guitar-1139397_1280_tile_crop.png')
        app.crop_image_for_tile(tile_4, tile_4.size, 'assets/robin-944887_1280_tile_crop.png')
        app.crop_image_for_tile(tile_5, tile_5.size, 'assets/kitten-1049129_1280_tile_crop.png')
        app.crop_image_for_tile(tile_6, tile_6.size, 'assets/light-bulb-1042480_1280_tile_crop.png')
        app.crop_image_for_tile(tile_7, tile_7.size, 'assets/tangerines-1111529_1280_tile_crop.png')

    ScrollView:
        do_scroll_x: False

        GridLayout:
            cols: 2
            row_default_height: (self.width - self.cols*self.spacing[0])/self.cols
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)

            SmartTileWithStar:
                id: tile_2
                mipmap: True
                stars: 3
            SmartTileWithStar:
                id: tile_3
                mipmap: True
                stars: 3
            SmartTileWithLabel:
                id: tile_1
                mipmap: True
                text: "Beautiful\\n[size=12]beautiful-931152_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_4
                mipmap: True
                text: "Robin\\n[size=12]robin-944887_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_5
                mipmap: True
                text: "Kitten\\n[size=12]kitten-1049129_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_6
                mipmap: True
                text: "Light-Bulb\\n[size=12]light-bulb-1042480_1280.png[/size]"
                font_style: 'Subtitle1'
            SmartTileWithLabel:
                id: tile_7
                mipmap: True
                text: "Tangerines\\n[size=12]tangerines-1111529_1280.png[/size]"
                font_style: 'Subtitle1'
'''

bottom_navigation = '''
#:import MDBottomNavigation kivymd.bottomnavigation.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.bottomnavigation.MDBottomNavigationItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDLabel kivymd.label.MDLabel


<BottomNavigation@Screen>
    name: 'bottom navigation'

    MDBottomNavigation:
        id: bottom_navigation_demo

        MDBottomNavigationItem:
            name: 'banking'
            text: "Bank"
            icon: 'bank'

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                padding: dp(48)
                spacing: dp(10)

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
                spacing: dp(10)

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
'''

tabs = '''
#:import MDLabel kivymd.label.MDLabel
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDTabsBase kivymd.tabs.MDTabsBase
#:import MDTabs kivymd.tabs.MDTabs


<Tabs@Screen>
    name: 'tabs'

    BoxLayout:
        orientation: 'vertical'

        MDTabs:
            id: android_tabs

        BoxLayout:
            size_hint_y: None
            height: dp(58)
            spacing: dp(5)
            padding: dp(5)

            MDCheckbox:
                size_hint: None, None
                size: dp(48), dp(48)
                on_state:
                    app.switch_tabs_to_text(android_tabs) if self.state == 'down' \
                    else app.switch_tabs_to_icon(android_tabs)
            MDLabel:
                theme_text_color: 'Primary'
                text: 'Use text tabs'

            Widget:


<MyTab@BoxLayout+MDTabsBase>

    FloatLayout:

        MDLabel:
            text: 'Content'
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H6'
'''

pickers = '''
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDLabel kivymd.label.MDLabel
#:import MDRaisedButton kivymd.button.MDRaisedButton


<Pickers@Screen>
    name: 'pickers'

    BoxLayout:
        spacing: dp(40)
        orientation: 'vertical'
        size_hint_x: None
        pos_hint: {'center_x': .5, 'center_y': .5}

        BoxLayout:
            orientation: 'vertical'
            # size_hint: (None, None)

            MDRaisedButton:
                text: "Open time picker"
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                pos_hint: {'center_x': .5, 'center_y': .5}
                opposite_colors: True
                on_release: app.show_example_time_picker()
            MDLabel:
                id: time_picker_label
                theme_text_color: 'Primary'
                size_hint: None, None
                size: dp(48)*3, dp(48)
                pos_hint: {'center_x': .5, 'center_y': .5}
            BoxLayout:
                size: dp(48)*3, dp(48)
                size_hint: (None, None)
                pos_hint: {'center_x': .5, 'center_y': .5}
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
                pos_hint: {'center_x': .5, 'center_y': .5}
                opposite_colors: True
                on_release: app.show_example_date_picker()
            MDLabel:
                id: date_picker_label
                theme_text_color: 'Primary'
                size_hint: None, None
                size: dp(48)*3, dp(48)
                pos_hint: {'center_x': .5, 'center_y': .5}
            BoxLayout:
                size: dp(48)*3, dp(48)
                size_hint: (None, None)
                pos_hint: {'center_x': .5, 'center_y': .5}
                MDLabel:
                    theme_text_color: 'Primary'
                    text: "Start on previous date"
                    size_hint: None, None
                    size: dp(130), dp(48)
                MDCheckbox:
                    id: date_picker_use_previous_date
                    size_hint: None, None
                    size: dp(48), dp(48)
'''

buttons = '''
#:import MDIconButton kivymd.button.MDIconButton
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRectangleFlatIconButton kivymd.button.MDRectangleFlatIconButton
#:import MDTextButton kivymd.button.MDTextButton
#:import MDFillRoundFlatButton kivymd.button.MDFillRoundFlatButton
#:import MDFillRoundFlatIconButton kivymd.button.MDFillRoundFlatIconButton
#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton


<Buttons@Screen>
    name: 'buttons'

    ScrollView:
        size_hint_x: None
        width: box.width
        pos_hint: {'center_x': .5}
        bar_width: 0

        BoxLayout:
            id: box
            padding: dp(10)
            size_hint: None, None
            size: self.minimum_size
            spacing: dp(10)
            orientation: 'vertical'
            pos_hint: {'center_x': .5}

            BoxLayout:
                size_hint: None, None
                width: self.minimum_width
                height: dp(56)
                spacing: '10dp'

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
 
            MDFlatButton:
                text: 'MDFlatButton'
                pos_hint: {'center_x': .5}

            MDRaisedButton:
                text: "MDRaisedButton"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': .5}

            MDRectangleFlatButton:
                text: "MDRectangleFlatButton"
                pos_hint: {'center_x': .5}

            MDRectangleFlatIconButton:
                text: "MDRectangleFlatIconButton"
                icon: "language-python"
                width: dp(230)
                pos_hint: {'center_x': .5}

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                pos_hint: {'center_x': .5}

            MDRoundFlatIconButton:
                text: "MDRoundFlatIconButton"
                icon: "language-python"
                width: dp(200)
                pos_hint: {'center_x': .5}

            MDFillRoundFlatButton:
                text: "MDFillRoundFlatButton"
                pos_hint: {'center_x': .5}

            MDRoundFlatIconButton:
                text: "MDRoundFlatIconButton"
                icon: "language-python"
                width: dp(200)
                pos_hint: {'center_x': .5}

            MDFillRoundFlatIconButton:
                text: "MDFillRoundFlatIconButton"
                icon: "language-python"
                pos_hint: {'center_x': .5}

            MDTextButton:
                text: "MDTextButton"
                pos_hint: {'center_x': .5}
'''

cards = '''
<Cards@Screen>
    name: 'cards'
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
'''
toolbars = '''
#:import MDToolbar kivymd.toolbar.MDToolbar


<Toolbars@Screen>
    name: 'toolbars'

    MDToolbar:
        title: "Simple toolbar"
        pos_hint: {'center_x': .5, 'center_y': .75}
        md_bg_color: get_color_from_hex(colors['Teal']['500'])
        background_palette: 'Teal'
        background_hue: '500'

    MDToolbar:
        title: "MDToolbar with right buttons"
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: get_color_from_hex(colors['Amber']['700'])
        background_palette: 'Amber'
        background_hue: '700'
        right_action_items: [['content-copy', lambda x: None]]

    MDToolbar:
        title: "MDToolbar with left and right buttons"
        pos_hint: {'center_x': .5, 'center_y': .25}
        md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
        background_palette: 'DeepPurple'
        background_hue: 'A400'
        left_action_items: [['arrow-left', lambda x: None]]
        right_action_items: [['lock', lambda x: None],\
            ['camera', lambda x: None],\
            ['play', lambda x: None]]
'''

dialogs = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton


<Dialogs@Screen>
    name: 'dialogs'

    MDRaisedButton:
        text: "Open lengthy dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .8}
        opposite_colors: True
        on_release: app.show_example_long_dialog()

    MDRaisedButton:
        text: "Open input dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .6}
        opposite_colors: True
        on_release: app.show_example_input_dialog()

    MDRaisedButton:
        text: "Open Alert Dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        opposite_colors: True
        on_release: app.show_example_alert_dialog()

    MDRaisedButton:
        text: "Open Ok Cancel Dialog"
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .2}
        opposite_colors: True
        on_release: app.show_example_ok_cancel_dialog()
'''

theming = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDLabel kivymd.label.MDLabel


<Theming@Screen>
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
            pos_hint: {'center_x': .5}
        MDLabel:
            text:
                "Current: " + app.theme_cls.theme_style\
                + ", " + app.theme_cls.primary_palette
            theme_text_color: 'Primary'
            pos_hint: {'center_x': .5}
            halign: 'center'
'''

textfields = '''
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDTextFieldClear kivymd.textfields.MDTextFieldClear
#:import MDTextField kivymd.textfields.MDTextField
#:import MDTextFieldRound kivymd.textfields.MDTextFieldRound

#:set color_shadow [0, 0, 0, .2980392156862745]


<MyMDTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: color_shadow
    active_color: color_shadow


<TextFields@Screen>
    name: 'textfields'

    canvas:
        Color:
            rgba: 0, 0, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: dp(48)
            spacing: dp(15)

            MyMDTextFieldRound:
                icon_type: 'without'
                hint_text: 'Field with `normal_color`'
                normal_color: [.432, .124, .8654, .1]

            MyMDTextFieldRound:
                icon_type: 'without'
                hint_text: 'Field without icon'

            MyMDTextFieldRound:
                icon_type: 'without'
                hint_text: 'Field with `require_text_error`'
                require_text_error: 'Field must be not empty!'

            MyMDTextFieldRound:
                icon_left: 'email'
                icon_type: 'left'
                hint_text: 'Field with left icon'
            
            MyMDTextFieldRound:
                icon_left: 'email'
                icon_right: 'account-box'
                icon_right_dasabled: True
                hint_text: 'Field with left and right disabled icons'

            MyMDTextFieldRound:
                icon_type: 'all'
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                icon_right_dasabled: False
                icon_callback: app.show_password
                password: True
                hint_text: 'Field width type `password = True`'

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

            Widget:
                size_hint_y: None
                height: dp(5)

            MDTextField:
                id: text_field_error
                hint_text: "Helper text on error (Hit Enter with  two characters here)"
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
                line_color_focus: self.theme_cls.opposite_bg_normal

            MDTextField:
                hint_text: "disabled = True"
                disabled: True

            MDTextFieldRect:
                size_hint: None, None
                size: app.Window.width - dp(40), dp(30)
                pos_hint: {'center_y': .5, 'center_x': .5}

            Widget:
                size_hint_y: None
                height: dp(5)

            MDTextFieldClear:
                hint_text: "Text field with clearing type"
'''

file_manager = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton


<FileManager@Screen>
    name: 'file manager'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open files manager'
        opposite_colors: True
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.file_manager_open()
'''

lists = '''
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem


<Lists@Screen>
    name: 'lists'

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
                    "This is a multi-line label where you can "\
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
                    "...with left icon..." + '\\n' + "and third line!"
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
                    "...with avatar&icon..." + '\\n' + "and third line!"
                AvatarSampleWidget:
                    source: './assets/avatar.png'
                IconRightSampleWidget:
'''

snackbar = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDLabel kivymd.label.MDLabel


<MySnackBar@Screen>
    name: 'snackbar'

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)

        Widget:

        MDRaisedButton:
            text: "Create simple snackbar"
            pos_hint: {'center_x': .5}
            on_release: app.show_example_snackbar('simple')

        MDRaisedButton:
            text: "Create snackbar with button"
            pos_hint: {'center_x': .5}
            on_release: app.show_example_snackbar('button')

        MDRaisedButton:
            text: "Create snackbar with a lot of text"
            pos_hint: {'center_x': .5}
            on_release: app.show_example_snackbar('verylong')

        MDSeparator:

        MDLabel:
            text: 'Click the MDFloatingActionButton to show the following example...'
            halign: 'center'

        Widget:

    MDFloatingActionButton:
        id: button
        md_bg_color: app.theme_cls.primary_color
        x: Window.width - self.width - dp(10)
        y: dp(10)
        on_release: app.show_example_snackbar('float')
'''

download_file = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import Clock kivy.clock.Clock


<DownloadFile@Screen>
    name: 'download file'

    FloatLayout:
        id: box_flt

        MDRaisedButton:
            text: "Download file"
            size_hint: None, None
            size: 3 * dp(48), dp(48)
            pos_hint: {'center_x': .5, 'center_y': .5}
            opposite_colors: True
            on_release:
                Clock.schedule_once(app.show_example_download_file, .1)
'''

user_animation_card = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton


<UserCard@Screen>
    name: 'user animation card'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open card'
        opposite_colors: True
        pos_hint: {'center_x': .5, 'center_y': .6}
        on_release: app.show_user_example_animation_card()
'''

selection_controls = '''
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch


<SelectionControls@Screen>
    name: 'selection controls'

    MDCheckbox:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .4, 'center_y': .8}

    MDCheckbox:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .6, 'center_y': .8}
        disabled: True

    MDCheckbox:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .4, 'center_y': .7}
        active: True

    MDCheckbox:
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .6, 'center_y': .7}
        active: True
        disabled: True

    MDCheckbox:
        group: 'test'
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .4, 'center_y': .6}

    MDCheckbox:
        group: 'test'
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .6, 'center_y': .6}
        disabled: True

    MDCheckbox:
        group: 'test'
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .4, 'center_y': .5}
        active: True

    MDCheckbox:
        group: 'test'
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .6, 'center_y': .5}
        active: True
        disabled: True

    MDSwitch:
        size_hint: None, None
        size: dp(36), dp(48)
        pos_hint: {'center_x': .3, 'center_y': .4}

    MDSwitch:
        size_hint: None, None
        size: dp(36), dp(48)
        pos_hint: {'center_x': .7, 'center_y': .4}
        disabled: True

    MDSwitch:
        size_hint: None, None
        size: dp(36), dp(48)
        pos_hint: {'center_x': .3, 'center_y': .3}
        active: True

    MDSwitch:
        size_hint: None, None
        size: dp(36), dp(48)
        pos_hint: {'center_x': .7, 'center_y': .3}
        active: True
        disabled: True
'''

sliders = '''
#:import MDSlider kivymd.slider.MDSlider


<Sliders@Screen>
    name: 'sliders'

    BoxLayout:

        MDSlider:
            id: hslider
            min: 0
            max: 100
            value: 10

        MDSlider:
            id: vslider
            orientation: 'vertical'
            min: 0
            max: 100
            value: hslider.value
'''

stack_buttons = '''
<StackButtons@Screen>
    name: 'stack buttons'
    on_enter: app.example_add_stack_floating_buttons()
'''

refresh_layout = '''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDScrollViewRefreshLayout kivymd.refreshlayout.MDScrollViewRefreshLayout


<ItemForListRefreshLayout>
    text: root.text

    IconLeftSampleWidget:
        icon: root.icon


<RefreshLayout@Screen>
    name: 'refresh layout'

    FloatLayout:

        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: app.main_widget.ids.float_box

            GridLayout:
                id: box
                size_hint_y: None
                height: self.minimum_height
                cols: 1
'''

progress_bar = '''
#:import MDSlider kivymd.slider.MDSlider
#:import MDProgressBar kivymd.progressbar.MDProgressBar


<ProgressBars@Screen>
    name: 'progress bar'

    BoxLayout:
        orientation:'vertical'
        padding: '8dp'

        MDSlider:
            id: progress_slider
            min: 0
            max: 100
            value: 40

        MDProgressBar:
            value: progress_slider.value
        MDProgressBar:
            reversed: True
            value: progress_slider.value

        BoxLayout:
            MDProgressBar:
                orientation: "vertical"
                reversed: True
                value: progress_slider.value

            MDProgressBar:
                orientation: "vertical"
                value: progress_slider.value
'''

labels = '''
#:import MDLabel kivymd.label.MDLabel


<MyMDLabel@MDLabel>
    size_hint_y: None
    height: self.texture_size[1]


<MyBoxLayout@BoxLayout>
    size_hint_y: None
    height: self.minimum_height


<Labels@Screen>
    name: 'labels'

    ScrollView:

        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'Overline'
                    theme_text_color: 'Primary'
                    text: "Overline label"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'Caption'
                    theme_text_color: 'Primary'
                    text: "Caption label"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'Button'
                    theme_text_color: 'Primary'
                    text: "Button label"
                    halign: 'center'

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Primary'
                    text: "Body1 label"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'Body2'
                    theme_text_color: 'Primary'
                    text: "Body2 label"
                    halign: 'center'

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'Subtitle1'
                    theme_text_color: 'Primary'
                    text: "Subtitle1 label"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'Subtitle2'
                    theme_text_color: 'Primary'
                    text: "Subtitle2 label"
                    halign: 'center'

            MyMDLabel:
                font_style: 'H1'
                theme_text_color: 'Primary'
                text: "H1 label"
                halign: 'center'
                #size_hint_y: None
                #height: self.texture_size[1] + dp(4)

            MyMDLabel:
                font_style: 'H2'
                theme_text_color: 'Primary'
                text: "H2 label"
                halign: 'center'
                #size_hint_y: None
                #height: self.texture_size[1] + dp(4)

            MyMDLabel:
                font_style: 'H3'
                theme_text_color: 'Primary'
                text: "H3 label"
                halign: 'center'

            MyMDLabel:
                font_style: 'H4'
                theme_text_color: 'Primary'
                text: "H4 label"
                halign: 'center'

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'H5'
                    theme_text_color: 'Primary'
                    text: "H5 label"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'H6'
                    theme_text_color: 'Primary'
                    text: "H6 label"
                    halign: 'center'

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Primary'
                    text: "Primary color"
                    halign: 'center'

                MyMDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Secondary'
                    text: "Secondary color"
                    halign: 'center'

            MyBoxLayout:

                MyMDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Hint'
                    text: "Hint color"
                    halign: 'center'
                MyMDLabel:
                    font_style: 'Body1'
                    theme_text_color: 'Error'
                    text: "Error color"
                    halign: 'center'

            MyMDLabel:
                font_style: 'Body1'
                theme_text_color: 'Custom'
                text_color: (0,1,0,.4)
                text: "Custom"
                halign: 'center'
'''

menu = '''
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDDropdownMenu kivymd.menus.MDDropdownMenu


<Menu@Screen>
    name: 'menu'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': .2, 'center_y': .9}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': .2, 'center_y': .1}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': .8, 'center_y': .1}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': .8, 'center_y': .9}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
'''

chips = '''
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDChip kivymd.chips.MDChip
#:import MDChooseChip kivymd.chips.MDChooseChip
#:import MDLabel kivymd.label.MDLabel


<LabelForChips@MDLabel>
    theme_text_color: 'Primary'


<Chips@Screen>
    name: 'chips'

    ScrollView:

        GridLayout:
            padding: dp(10)
            spacing: dp(10)
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            Widget:
                size_hint_y: None
                height: dp(5)

            LabelForChips:
                text: 'Chips with color:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Coffee'
                    color: .4470588235118, .1960787254902, 0, 1
                    icon: 'coffee'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Duck'
                    color: .9215686274509803, 0, 0, 1
                    icon: 'duck'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Earth'
                    color: .21176470535294, .098039627451, 1, 1
                    icon: 'earth'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Face'
                    color: .2039215698, .4823117606, .435295883, 1
                    icon: 'face'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Facebook'
                    color: .56078431302, .482352906, .435294883, 1
                    icon: 'facebook'
                    callback: app.callback_for_menu_items

            Widget:
                size_hint_y: None
                height: dp(5)

            LabelForChips:
                text: 'Chip without icon:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Without icon'
                    icon: ''
                    callback: app.callback_for_menu_items

            Widget:
                size_hint_y: None
                height: dp(5)

            LabelForChips:
                text: 'Chips with check:'

            MDSeparator:

            StackLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(5)

                MDChip:
                    label: 'Check'
                    icon: ''
                    check: True
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Check with icon'
                    icon: 'city'
                    check: True
                    callback: app.callback_for_menu_items

            Widget:
                size_hint_y: None
                height: dp(5)

            LabelForChips:
                text: 'Choose chip:'

            MDSeparator:

            MDChooseChip:

                MDChip:
                    label: 'Earth'
                    icon: 'earth'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Face'
                    icon: 'face'
                    callback: app.callback_for_menu_items

                MDChip:
                    label: 'Facebook'
                    icon: 'facebook'
                    callback: app.callback_for_menu_items
'''

progress = '''
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSpinner kivymd.spinner.MDSpinner


<Progress@Screen>
    name: 'progress'

    MDCheckbox:
        id: chkbox
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        active: True

    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True if chkbox.active else False
'''

fan_manager = '''
#:import MDFanScreenManager kivymd.fanscreenmanager.MDFanScreenManager


<FanManager@Screen>
    name: 'fan manager'

    on_enter:
        app.main_widget.ids.toolbar.left_action_items = [['menu', lambda x: fan_screen_manager.open_fan()]]
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
            path_to_image: 'assets/african-lion-951778_1280.png'
            on_enter: app.main_widget.ids.toolbar.title = self.name

        ScreenTwo:
            name: 'Screen Two'
            path_to_image: 'assets/beautiful-931152_1280.png'
            on_enter: app.main_widget.ids.toolbar.title = self.name

        ScreenTree:
            name: 'Screen Tree'
            path_to_image: 'assets/kitten-1049129_1280.png'
            on_enter: app.main_widget.ids.toolbar.title = self.name

        ScreenFour:
            name: 'Screen Four'
            path_to_image: 'assets/tangerines-1111529_1280.png'
            on_enter: app.main_widget.ids.toolbar.title = self.name


<BaseFanScreen>
    orientation: 'vertical'

    canvas.before:
        Color:
            rgba: app.theme_cls.bg_light
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
'''

popup_screen = '''
<PopupScreenWidget@Screen>
    name: 'popup screen'
    on_enter: app.set_popup_screen(content_popup)

    PopupScreen:
        id: popup_screen

        ContentPopup:
            id: content_popup
'''

manager_swiper = '''
#:import images_path kivymd.images_path
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDLabel kivymd.label.MDLabel
#:import MDSwiperManager kivymd.managerswiper.MDSwiperManager


<MyCard>
    orientation: 'vertical'
    size_hint_y: None
    height: dp(300)
    pos_hint: {'top': 1}

    Image:
        source:
            f'{app.directory}/assets/guitar-1139397_1280_swiper_crop.png'
        size_hint: None, None
        size: root.width, dp(250)
        pos_hint: {'top': 1}

    MDLabel:
        theme_text_color: 'Custom'
        bold: True
        text_color: app.theme_cls.primary_color
        text: root.text
        size_hint_y: None
        height: dp(60)
        halign: 'center'


<MySwiperManager@Screen>
    name: 'manager swiper'

    BoxLayout:
        orientation: 'vertical'

        canvas:
            Color:
                rgba: 0, 0, 0, .2
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            id: box
            padding: dp(10)
            orientation: 'vertical'

            MDSwiperManager:
                id: swiper_manager

                Screen:
                    name: 'screen one'
                    MyCard:
                        text: 'Swipe to switch to screen one'.upper()

                Screen:
                    name: 'screen two'
                    MyCard:
                        text: 'Swipe to switch to screen two'.upper()

                Screen:
                    name: 'screen three'
                    MyCard:
                        text: 'Swipe to switch to screen three'.upper()

                Screen:
                    name: 'screen four'
                    MyCard:
                        text: 'Swipe to switch to screen four'.upper()

                Screen:
                    name: 'screen five'
                    MyCard:
                        text: 'Swipe to switch to screen five'.upper()
'''

md_icon_item = '''
#:import OneLineIconListItem kivymd.list.OneLineIconListItem


<MDIconItem@OneLineIconListItem>
    icon: 'android'

    IconLeftSampleWidget:
        icon: root.icon
'''

md_icons = '''
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import images_path kivymd.images_path
#:import MDTextFieldRect kivymd.textfields.MDTextField
#:import MDIconButton kivymd.button.MDIconButton


<MDIconItemForMdIconsList@OneLineIconListItem>:
    icon: 'android'
    on_release: root.callback(root.icon)

    IconLeftSampleWidget:
        icon: root.icon


<MDIcons@Screen>
    name: 'md icons'
    on_enter: app.set_list_md_icons()

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: app.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''


class Screens(object):
    manager_swiper = None
    main_widget = None
    directory = None

    data = {
        'Themes':
            {'kv_string': theming,
             'Factory': 'Factory.Theming()',
             'name_screen': 'theming',
             'object': None},

        'Bottom Navigation':
            {'kv_string': bottom_navigation,
             'Factory': 'Factory.BottomNavigation()',
             'name_screen': 'bottom navigation',
             'object': None},

        'Bottom Sheets':
            {'kv_string': bottom_sheet,
             'Factory': 'Factory.BottomSheet()',
             'name_screen': 'bottom sheet',
             'object': None},

        'Popup Screen':
            {'kv_string': popup_screen,
             'Factory': 'Factory.PopupScreenWidget()',
             'name_screen': 'popup screen',
             'object': None},

        'Fan Manager':
            {'kv_string': fan_manager,
             'Factory': 'Factory.FanManager()',
             'name_screen': 'fan manager',
             'object': None},

        'Progress bars':
            {'kv_string': progress_bar,
             'Factory': 'Factory.ProgressBars()',
             'name_screen': 'progress bar',
             'object': None},

        'Progress & activity':
            {'kv_string': progress,
             'Factory': 'Factory.Progress()',
             'name_screen': 'progress',
             'object': None},

        'Refresh Layout':
            {'kv_string': refresh_layout,
             'Factory': 'Factory.RefreshLayout()',
             'name_screen': 'refresh layout',
             'object': None},

        'Sliders':
            {'kv_string': sliders,
             'Factory': 'Factory.Sliders()',
             'name_screen': 'sliders',
             'object': None},

        'Floating Buttons':
            {'kv_string': stack_buttons,
             'Factory': 'Factory.StackButtons()',
             'name_screen': 'stack buttons',
             'object': None},

        'Snackbars':
            {'kv_string': snackbar,
             'Factory': 'Factory.MySnackBar()',
             'name_screen': 'snackbar',
             'object': None},

        'Download File':
            {'kv_string': download_file,
             'Factory': 'Factory.DownloadFile()',
             'name_screen': 'download file',
             'object': None},

        'User Animation Card':
            {'kv_string': user_animation_card,
             'Factory': 'Factory.UserCard()',
             'name_screen': 'user animation card',
             'object': None},

        'Pickers':
            {'kv_string': pickers,
             'Factory': 'Factory.Pickers()',
             'name_screen': 'pickers',
             'object': None},

        'Cards':
            {'kv_string': cards,
             'Factory': 'Factory.Cards()',
             'name_screen': 'cards',
             'object': None},

        'Dialogs':
            {'kv_string': dialogs,
             'Factory': 'Factory.Dialogs()',
             'name_screen': 'dialogs',
             'object': None},

        'Toolbars':
            {'kv_string': toolbars,
             'Factory': 'Factory.Toolbars()',
             'name_screen': 'toolbars',
             'object': None},

        'Buttons':
            {'kv_string': buttons,
             'Factory': 'Factory.Buttons()',
             'name_screen': 'buttons',
             'object': None},

        'Files Manager':
            {'kv_string': file_manager,
             'Factory': 'Factory.FileManager()',
             'name_screen': 'file manager',
             'object': None},

        'Tabs':
            {'kv_string': tabs,
             'Factory': 'Factory.Tabs()',
             'name_screen': 'tabs',
             'object': None},

        'Labels':
            {'kv_string': labels,
             'Factory': 'Factory.Labels()',
             'name_screen': 'labels',
             'object': None},

        'Chips':
            {'kv_string': chips,
             'Factory': 'Factory.Chips()',
             'name_screen': 'chips',
             'object': None},

        'Lists':
            {'kv_string': lists,
             'Factory': 'Factory.Lists()',
             'name_screen': 'lists',
             'object': None},

        'Accordion List':
            {'kv_string': accordion_list,
             'Factory': 'Factory.AccordionList()',
             'name_screen': 'accordion list',
             'object': None},

        'Grid lists':
            {'kv_string': grid,
             'Factory': 'Factory.Grid()',
             'name_screen': 'grid',
             'object': None},

        'Accordion':
            {'kv_string': accordion,
             'Factory': 'Factory.Accord()',
             'name_screen': 'accordion',
             'object': None},

        'Selection controls':
            {'kv_string': selection_controls,
             'Factory': 'Factory.SelectionControls()',
             'name_screen': 'selection controls',
             'object': None},

        'Menus':
            {'kv_string': menu,
             'Factory': 'Factory.Menu()',
             'name_screen': 'menu',
             'object': None},

        'MD Icons':
            {'kv_string': md_icons,
             'Factory': 'Factory.MDIcons()',
             'name_screen': 'md icons',
             'object': None},

        'Bottom App Bar':
            {'kv_string': bottom_app_bar,
             'Factory': 'Factory.BottomAppBar()',
             'name_screen': 'bottom app bar',
             'object': None},

        'Text fields':
            {'kv_string': textfields,
             'Factory': 'Factory.TextFields()',
             'name_screen': 'textfields',
             'object': None}
    }

    data_for_demo = {
        'Shop Window':
            {'class': 'ShopWindow()',
             'object': None},

        'Fitness Club':
            {'class': 'FitnessClub()',
             'object': None},

        'Coffee Menu':
            {'class': 'CoffeeMenu()',
             'object': None},

        'Swipe cards':
            {'class': 'SwipeCards()',
             'object': None},

        'Registration':
            {'class': 'FormOne()',
             'object': None},

        'Account Page':
            {'class': 'AccountPage()',
             'object': None}
    }

    def show_screens_demo(self, name_screen):
        if name_screen == 'Registration' and \
                not self.data_for_demo[name_screen]['object']:
            from demo_apps.formone import registration_form_one, FormOne
            self.data_for_demo[name_screen]['kv_string'] = registration_form_one
        elif name_screen == 'Shop Window' and \
                not self.data_for_demo[name_screen]['object']:
            from demo_apps.shopwindow import screen_shop_window, ShopWindow
            self.data_for_demo[name_screen]['kv_string'] = screen_shop_window
        elif name_screen == 'Coffee Menu' and \
                not self.data_for_demo[name_screen]['object']:
            from demo_apps.coffeemenu import screen_coffee_menu, CoffeeMenu
            self.data_for_demo[name_screen]['kv_string'] = screen_coffee_menu
        elif name_screen == 'Fitness Club' and \
                not self.data_for_demo[name_screen]['object']:
            from demo_apps.fitnessclub import screen_fitness_club, FitnessClub
            self.data_for_demo[name_screen]['kv_string'] = screen_fitness_club
        elif name_screen == 'Account Page' and \
                not self.data_for_demo[name_screen]['object']:
            from demo_apps.accountpage import screen_account_page, AccountPage
            self.data_for_demo[name_screen]['kv_string'] = screen_account_page

        if name_screen == 'Registration':
            self.theme_cls.primary_palette = 'Amber'
        if name_screen != 'Shop Window':
            self.main_widget.ids.toolbar.height = 0
        if not self.data_for_demo[name_screen]['object']:
            Builder.load_string(self.data_for_demo[name_screen]['kv_string'])
            self.data_for_demo[name_screen]['object'] = eval(
                self.data_for_demo[name_screen]['class'])
            self.main_widget.ids.scr_mngr.add_widget(
                self.data_for_demo[name_screen]['object'])

    def show_manager_swiper(self):
        from kivymd.managerswiper import MDSwiperPagination

        if not self.manager_swiper:
            path_to_crop_image = \
                f'{self.directory}/assets/guitar-1139397_1280_swiper_crop.png'
            if not os.path.exists(path_to_crop_image):
                crop_image(
                    (int(Window.width - dp(10)), int(dp(250))),
                    f'{self.directory}/assets/guitar-1139397_1280.png',
                    path_to_crop_image)

            Builder.load_string(manager_swiper)
            self.manager_swiper = Factory.MySwiperManager()
            self.main_widget.ids.scr_mngr.add_widget(self.manager_swiper)
            paginator = MDSwiperPagination()
            paginator.screens =\
                self.manager_swiper.ids.swiper_manager.screen_names
            paginator.manager = self.manager_swiper.ids.swiper_manager
            self.manager_swiper.ids.swiper_manager.paginator = paginator
            self.manager_swiper.ids.box.add_widget(paginator)

        self.main_widget.ids.scr_mngr.current = 'manager swiper'

    def show_screen(self, name_screen):
        if not self.data[name_screen]['object']:
            Builder.load_string(self.data[name_screen]['kv_string'])
            self.data[name_screen]['object'] = \
                eval(self.data[name_screen]['Factory'])
            if name_screen == 'Bottom App Bar':
                self.set_appbar()
                self.data[name_screen]['object'].add_widget(self.md_app_bar)
            self.main_widget.ids.scr_mngr.add_widget(
                self.data[name_screen]['object'])
            if name_screen == 'Text fields':
                self.data[name_screen]['object'].ids.text_field_error.bind(
                    on_text_validate=self.set_error_message,
                    on_focus=self.set_error_message)
            elif name_screen == 'MD Icons':
                self.set_list_md_icons()
            elif name_screen == 'Tabs':
                self.build_tabs()
            elif name_screen == 'Refresh Layout':
                self.set_list_for_refresh_layout()
        self.main_widget.ids.scr_mngr.current = \
            self.data[name_screen]['name_screen']
