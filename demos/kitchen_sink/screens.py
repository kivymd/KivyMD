import os

from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window

from kivymd.utils.cropimage import crop_image

bottom_app_bar = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<BottomAppBar@Screen>:
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
"""

accordion_list = """
<AccordionList@Screen>:
    name: 'accordion list'
    on_enter: app.set_accordion_list()
    on_leave: anim_list.clear_widgets()

    ScrollView:

        GridLayout:
            id: anim_list
            cols: 1
            size_hint_y: None
            height: self.minimum_height
"""

bottom_sheet = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<BottomSheet@Screen>:
    name: 'bottom sheet'

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
"""

accordion = """
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem


<Accord@Screen>:
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
"""

grid = """
#:import SmartTileWithStar kivymd.grid.SmartTileWithStar
#:import SmartTileWithLabel kivymd.grid.SmartTileWithLabel


<Grid@Screen>:
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
                font_style: 'Subhead'
            SmartTileWithLabel:
                id: tile_4
                mipmap: True
                text: "Robin\\n[size=12]robin-944887_1280.png[/size]"
                font_style: 'Subhead'
            SmartTileWithLabel:
                id: tile_5
                mipmap: True
                text: "Kitten\\n[size=12]kitten-1049129_1280.png[/size]"
                font_style: 'Subhead'
            SmartTileWithLabel:
                id: tile_6
                mipmap: True
                text: "Light-Bulb\\n[size=12]light-bulb-1042480_1280.png[/size]"
                font_style: 'Subhead'
            SmartTileWithLabel:
                id: tile_7
                mipmap: True
                text: "Tangerines\\n[size=12]tangerines-1111529_1280.png[/size]"
                font_style: 'Subhead'
"""

bottom_navigation = """
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDLabel kivymd.label.MDLabel


<BottomNavigation@Screen>:
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
"""

tabs = """
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDLabel kivymd.label.MDLabel
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox


<Tabs@Screen>:
    name: 'tabs'

    MDTabbedPanel:
        id: tab_panel
        tab_display_mode: 'text'
        tab_width_mode: 'stacked'

        MDTab:
            name: 'music'
            text: "Music"
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

        MDTab:
            name: 'python'
            text: 'Python'
            icon: "language-python"

            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love Python language"
                halign: 'center'

        MDTab:
            name: 'cpp'
            text: 'C++'
            icon: "language-cpp"

            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love C++ language"
                halign: 'center'

        MDTab:
            name: 'php'
            text: 'PHP'
            icon: "language-php"

            MDLabel:
                font_style: 'Body1'
                theme_text_color: 'Primary'
                text: "I love PHP language"
                halign: 'center'

    BoxLayout:
        size_hint_y: None
        height: dp(72)
        padding: dp(12)

        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: "Use icons"
            size_hint_x:None
            width: dp(64)

        MDCheckbox:
            on_state:
                tab_panel.tab_display_mode = 'icons' \
                if tab_panel.tab_display_mode=='text' else 'text'

        MDLabel:
            font_style: 'Body1'
            theme_text_color: 'Primary'
            text: "Use fixed"
            size_hint_x:None
            width: dp(64)

        MDCheckbox:
            on_state:
                tab_panel.tab_width_mode = 'fixed' \
                if tab_panel.tab_width_mode =='stacked' else 'stacked'
                
        Widget:
"""

pickers = """
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDLabel kivymd.label.MDLabel
#:import MDRaisedButton kivymd.button.MDRaisedButton


<Pickers@Screen>:
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
"""

buttons = """
#:import MDIconButton kivymd.button.MDIconButton
#:import MDFloatingActionButton kivymd.button.MDFloatingActionButton
#:import MDFlatButton kivymd.button.MDFlatButton
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRectangleFlatIconButton kivymd.button.MDRectangleFlatIconButton
#:import MDTextButton kivymd.button.MDTextButton
#:import MDFillRoundFlatButton kivymd.button.MDFillRoundFlatButton
#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton


<Buttons@Screen>:
    name: 'buttons'

    BoxLayout:
        size_hint_y: None
        height: dp(56)
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
"""

cards = """
<Cards@Screen>:
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
"""
toolbars = """
#:import Toolbar kivymd.toolbar.Toolbar


<Toolbars@Screen>:
    name: 'toolbars'

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
"""

dialogs = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<Dialogs@Screen>:
    name: 'dialogs'

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
"""

theming = """
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDLabel kivymd.label.MDLabel


<Theming@Screen>:
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
"""

textfields = """
#:import MDTextFieldRect kivymd.textfields.MDTextFieldRect
#:import MDTextFieldClear kivymd.textfields.MDTextFieldClear
#:import MDTextField kivymd.textfields.MDTextField


<TextFields@Screen>:
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
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"
            MDTextField:
                hint_text: "Persistent helper text"
                helper_text: "Text is always here"
                helper_text_mode: "persistent"
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
            MDTextFieldClear:
                hint_text: "Text field with clearing type"
"""

file_manager = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<FileManager@Screen>:
    name: 'file manager'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open files manager'
        opposite_colors: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.file_manager_open()
"""

lists = """
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem


<Lists@Screen>:
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
"""

snackbar = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<SnackBar@Screen>:
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
"""

download_file = """
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import Clock kivy.clock.Clock


<DownloadFile@Screen>:
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
                Clock.schedule_once(app.show_example_download_file, .1)
"""

user_animation_card = """
#:import MDRaisedButton kivymd.button.MDRaisedButton


<UserCard@Screen>:
    name: 'user animation card'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open card'
        opposite_colors: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_release: app.show_user_example_animation_card()
"""

selection_controls = """
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch


<SelectionControls@Screen>:
    name: 'selection controls'

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
"""

sliders = """
#:import MDSlider kivymd.slider.MDSlider


<Sliders@Screen>:
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
"""

stack_buttons = """
<StackButtons@Screen>:
    name: 'stack buttons'
    on_enter: app.example_add_stack_floating_buttons()
"""

update_spinner = """
#:import MDLabel kivymd.label.MDLabel
#:import MDUpdateSpinner kivymd.updatespinner.MDUpdateSpinner


<UpdateSpinner@Screen>:
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
"""

progress_bar = """
#:import MDSlider kivymd.slider.MDSlider
#:import MDProgressBar kivymd.progressbar.MDProgressBar


<ProgressBars@Screen>:
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
"""

labels = """
#:import MDLabel kivymd.label.MDLabel


<Labels@Screen>:
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
"""

menu = """
#:import MDRaisedButton kivymd.button.MDRaisedButton
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu


<Menu@Screen>:
    name: 'menu'

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': 0.2, 'center_y': 0.9}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': 0.2, 'center_y': 0.1}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': 0.8, 'center_y': 0.1}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': 0.8, 'center_y': 0.9}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)

    MDRaisedButton:
        size_hint: None, None
        size: 3 * dp(48), dp(48)
        text: 'Open menu'
        opposite_colors: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release:
            MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)
"""

chips = """
#:import MDSeparator kivymd.card.MDSeparator
#:import MDChip kivymd.chips.MDChip
#:import MDChooseChip kivymd.chips.MDChooseChip


<Chips@Screen>:
    name: 'chips'

    ScrollView:

        GridLayout:
            padding: dp(10)
            spacing: dp(10)
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
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

            MDLabel:
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

            MDLabel:
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

            MDLabel:
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
"""

progress = """
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSpinner kivymd.spinner.MDSpinner


<Progress@Screen>:
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
"""

fan_manager = """
#:import MDFanScreenManager kivymd.fanscreenmanager.MDFanScreenManager


<FanManager@Screen>:
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
"""

popup_screen = """
<PopupScreenWidget@Screen>:
    name: 'popup screen'
    on_enter: app.set_popup_screen(content_popup)

    PopupScreen:
        id: popup_screen

        ContentPopup:
            id: content_popup
"""

manager_swiper = """
#:import images_path kivymd.images_path
#:import Toolbar kivymd.toolbar.Toolbar
#:import MDLabel kivymd.label.MDLabel
#:import MDSwiperManager kivymd.managerswiper.MDSwiperManager


<MyCard>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(300)
    pos_hint: {'top': 1}

    Image:
        source:
            '{}/assets/guitar-1139397_1280_swiper_crop.png'.format(app.directory)
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


<MySwiperManager@Screen>:
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
"""

md_icon_item = """
#:import OneLineIconListItem kivymd.list.OneLineIconListItem


<MDIconItem@OneLineIconListItem>:
    icon: 'android'

    IconLeftSampleWidget:
        icon: root.icon
"""

md_icons = """
<MDIcons@Screen>:
    name: 'md icons'

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
"""


class Screens(object):
    manager_swiper = None

    def show_manager_swiper(self):
        from kivymd.managerswiper import MDSwiperPagination

        if not self.manager_swiper:
            path_to_crop_image = \
                '{}/assets/' \
                'guitar-1139397_1280_swiper_crop.png'.format(self.directory)
            if not os.path.exists(path_to_crop_image):
                crop_image(
                    (int(Window.width - dp(10)), int(dp(250))),
                    '{}/assets/guitar-1139397_1280.png'.format(
                        self.directory), path_to_crop_image)

            Builder.load_string(manager_swiper)
            self.manager_swiper = Factory.MySwiperManager()
            self.main_widget.ids.scr_mngr.add_widget(self.manager_swiper)
            paginator = MDSwiperPagination()
            paginator.screens = \
                self.manager_swiper.ids.swiper_manager.screen_names
            paginator.manager = self.manager_swiper.ids.swiper_manager
            self.manager_swiper.ids.swiper_manager.paginator = paginator
            self.manager_swiper.ids.box.add_widget(paginator)

        self.main_widget.ids.scr_mngr.current = 'manager swiper'

    bottom_navigation = None

    def show_bottom_navigation(self):
        if not self.bottom_navigation:
            Builder.load_string(bottom_navigation)
            self.bottom_navigation = Factory.BottomNavigation()
            self.main_widget.ids.scr_mngr.add_widget(self.bottom_navigation)
        self.main_widget.ids.scr_mngr.current = 'bottom navigation'

    md_icons = None

    def show_md_icons(self):
        def set_list_md_icons():
            from kivymd.icon_definitions import md_icons

            Builder.load_string(md_icon_item)
            for icon in md_icons.keys():
                self.md_icons.ids.rv.data.append(
                    {
                        'viewclass': 'MDIconItem',
                        'icon': icon,
                        'text': icon
                    }
                )

        if not self.md_icons:
            Builder.load_string(md_icons)
            self.md_icons = Factory.MDIcons()
            self.main_widget.ids.scr_mngr.add_widget(self.md_icons)
            set_list_md_icons()
        self.main_widget.ids.scr_mngr.current = 'md icons'

    bottom_sheet = None

    def show_bottom_sheet(self):
        if not self.bottom_sheet:
            Builder.load_string(bottom_sheet)
            self.bottom_sheet = Factory.BottomSheet()
            self.main_widget.ids.scr_mngr.add_widget(self.bottom_sheet)
        self.main_widget.ids.scr_mngr.current = 'bottom sheet'

    popup_screen = None

    def show_popup_screen(self):
        if not self.popup_screen:
            Builder.load_string(popup_screen)
            self.popup_screen = Factory.PopupScreenWidget()
            self.main_widget.ids.scr_mngr.add_widget(self.popup_screen)
        self.main_widget.ids.scr_mngr.current = 'popup screen'

    fan_manager = None

    def show_fan_manager(self):
        if not self.fan_manager:
            Builder.load_string(fan_manager)
            self.fan_manager = Factory.FanManager()
            self.main_widget.ids.scr_mngr.add_widget(self.fan_manager)
        self.main_widget.ids.scr_mngr.current = 'fan manager'

    progress_bar = None

    def show_progress_bar(self):
        if not self.progress_bar:
            Builder.load_string(progress_bar)
            self.progress_bar = Factory.ProgressBars()
            self.main_widget.ids.scr_mngr.add_widget(self.progress_bar)
        self.main_widget.ids.scr_mngr.current = 'progress bar'

    progress = None

    def show_progress(self):
        if not self.progress:
            Builder.load_string(progress)
            self.progress = Factory.Progress()
            self.main_widget.ids.scr_mngr.add_widget(self.progress)
        self.main_widget.ids.scr_mngr.current = 'progress'

    update_spinner = None

    def show_update_spinner(self):
        if not self.update_spinner:
            Builder.load_string(update_spinner)
            self.update_spinner = Factory.UpdateSpinner()
            self.main_widget.ids.scr_mngr.add_widget(self.update_spinner)
        self.main_widget.ids.scr_mngr.current = 'update spinner'

    theming = None

    def show_theming(self):
        if not self.theming:
            Builder.load_string(theming)
            self.theming = Factory.Theming()
            self.main_widget.ids.scr_mngr.add_widget(self.theming)
        self.main_widget.ids.scr_mngr.current = 'theming'

    selection_controls = None

    def show_selection_controls(self):
        if not self.selection_controls:
            Builder.load_string(selection_controls)
            self.selection_controls = Factory.SelectionControls()
            self.main_widget.ids.scr_mngr.add_widget(self.selection_controls)
        self.main_widget.ids.scr_mngr.current = 'selection controls'

    menu = None

    def show_menu(self):
        if not self.menu:
            Builder.load_string(menu)
            self.menu = Factory.Menu()
            self.main_widget.ids.scr_mngr.add_widget(self.menu)
        self.main_widget.ids.scr_mngr.current = 'menu'

    bottom_app_bar = None

    def show_app_bar(self):
        if not self.bottom_app_bar:
            Builder.load_string(bottom_app_bar)
            self.set_appbar()
            self.bottom_app_bar = Factory.BottomAppBar()
            self.bottom_app_bar.add_widget(self.md_app_bar)
            self.main_widget.ids.scr_mngr.add_widget(self.bottom_app_bar)
        self.main_widget.ids.scr_mngr.current = 'bottom app bar'

    accordion_list = None

    def show_accordion_list(self):
        if not self.accordion_list:
            Builder.load_string(accordion_list)
            self.accordion_list = Factory.AccordionList()
            self.main_widget.ids.scr_mngr.add_widget(self.accordion_list)
        self.main_widget.ids.scr_mngr.current = 'accordion list'

    grid = None

    def show_grid(self):
        if not self.grid:
            Builder.load_string(grid)
            self.grid = Factory.Grid()
            self.main_widget.ids.scr_mngr.add_widget(self.grid)
        self.main_widget.ids.scr_mngr.current = 'grid'

    accordion = None

    def show_accordion(self):
        if not self.accordion:
            Builder.load_string(accordion)
            self.accordion = Factory.Accord()
            self.main_widget.ids.scr_mngr.add_widget(self.accordion)
        self.main_widget.ids.scr_mngr.current = 'accordion'

    labels = None

    def show_labels(self):
        if not self.labels:
            Builder.load_string(labels)
            self.labels = Factory.Labels()
            self.main_widget.ids.scr_mngr.add_widget(self.labels)
        self.main_widget.ids.scr_mngr.current = 'labels'

    chips = None

    def show_chips(self):
        if not self.chips:
            Builder.load_string(chips)
            self.chips = Factory.Chips()
            self.main_widget.ids.scr_mngr.add_widget(self.chips)
        self.main_widget.ids.scr_mngr.current = 'chips'

    lists = None

    def show_lists(self):
        if not self.lists:
            Builder.load_string(lists)
            self.lists = Factory.Lists()
            self.main_widget.ids.scr_mngr.add_widget(self.lists)
        self.main_widget.ids.scr_mngr.current = 'lists'

    buttons = None

    def show_buttons(self):
        if not self.buttons:
            Builder.load_string(buttons)
            self.buttons = Factory.Buttons()
            self.main_widget.ids.scr_mngr.add_widget(self.buttons)
        self.main_widget.ids.scr_mngr.current = 'buttons'

    file_manager = None

    def show_file_manager(self):
        if not self.file_manager:
            Builder.load_string(file_manager)
            self.file_manager = Factory.FileManager()
            self.main_widget.ids.scr_mngr.add_widget(self.file_manager)
        self.main_widget.ids.scr_mngr.current = 'file manager'

    tabs = None

    def show_tabs(self):
        if not self.tabs:
            Builder.load_string(tabs)
            self.tabs = Factory.Tabs()
            self.main_widget.ids.scr_mngr.add_widget(self.tabs)
        self.main_widget.ids.scr_mngr.current = 'tabs'

    textfields = None

    def show_textfields(self):
        if not self.textfields:
            Builder.load_string(textfields)
            self.textfields = Factory.TextFields()
            self.main_widget.ids.scr_mngr.add_widget(self.textfields)
            self.textfields.ids.text_field_error.bind(
                on_text_validate=self.set_error_message,
                on_focus=self.set_error_message)
        self.main_widget.ids.scr_mngr.current = 'textfields'

    pickers = None

    def show_pickers(self):
        if not self.pickers:
            Builder.load_string(pickers)
            self.pickers = Factory.Pickers()
            self.main_widget.ids.scr_mngr.add_widget(self.pickers)
        self.main_widget.ids.scr_mngr.current = 'pickers'

    cards = None

    def show_cards(self):
        if not self.cards:
            Builder.load_string(cards)
            self.cards = Factory.Cards()
            self.main_widget.ids.scr_mngr.add_widget(self.cards)
        self.main_widget.ids.scr_mngr.current = 'cards'

    dialogs = None

    def show_dialogs(self):
        if not self.dialogs:
            Builder.load_string(dialogs)
            self.dialogs = Factory.Dialogs()
            self.main_widget.ids.scr_mngr.add_widget(self.dialogs)
        self.main_widget.ids.scr_mngr.current = 'dialogs'

    toolbars = None

    def show_toolbars(self):
        if not self.toolbars:
            Builder.load_string(toolbars)
            self.toolbars = Factory.Toolbars()
            self.main_widget.ids.scr_mngr.add_widget(self.toolbars)
        self.main_widget.ids.scr_mngr.current = 'toolbars'

    snackbar = None

    def show_snackbar(self):
        if not self.snackbar:
            Builder.load_string(snackbar)
            self.snackbar = Factory.SnackBar()
            self.main_widget.ids.scr_mngr.add_widget(self.snackbar)
        self.main_widget.ids.scr_mngr.current = 'snackbar'

    download_file = None

    def show_download_file(self):
        if not self.download_file:
            Builder.load_string(download_file)
            self.download_file = Factory.DownloadFile()
            self.main_widget.ids.scr_mngr.add_widget(self.download_file)
        self.main_widget.ids.scr_mngr.current = 'download file'

    user_animation_card = None

    def show_user_animation_card(self):
        if not self.user_animation_card:
            Builder.load_string(user_animation_card)
            self.user_animation_card = Factory.UserCard()
            self.main_widget.ids.scr_mngr.add_widget(self.user_animation_card)
        self.main_widget.ids.scr_mngr.current = 'user animation card'

    sliders = None

    def show_sliders(self):
        if not self.sliders:
            Builder.load_string(sliders)
            self.sliders = Factory.Sliders()
            self.main_widget.ids.scr_mngr.add_widget(self.sliders)
        self.main_widget.ids.scr_mngr.current = 'sliders'

    stack_buttons = None

    def show_stack_buttons(self):
        if not self.stack_buttons:
            Builder.load_string(stack_buttons)
            self.stack_buttons = Factory.StackButtons()
            self.main_widget.ids.scr_mngr.add_widget(self.stack_buttons)
        self.main_widget.ids.scr_mngr.current = 'stack buttons'
