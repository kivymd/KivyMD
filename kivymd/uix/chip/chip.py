"""
Components/Chip
===============

.. seealso::

    `Material Design 3 spec, Chips <https://m3.material.io/components/chips/overview>`_

.. rubric:: Chips can show multiple interactive elements together in the same
    area, such as a list of selectable movie times, or a series of email
    contacts. There are four types of chips: assist, filter, input, and
    suggestion.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chips.png
    :align: center

Usage
-----

.. code-block:: kv

    MDChip:

        MDChipLeadingAvatar:  # MDChipLeadingIcon

        MDChipText:

        MDChipTrailingIcon:

Anatomy
=======

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip-anatomy.png
    :align: center

Example
-------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDChip:
                    pos_hint: {"center_x": .5, "center_y": .5}

                    MDChipText:
                        text: "MDChip"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDChip(
                                MDChipText(
                                    text="MDChip"
                                ),
                                pos_hint={"center_x": .5, "center_y": .5},
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/chip.png
    :align: center

The following types of chips are available:
-------------------------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/available-type-chips.png
    :align: center

- Assist_
- Filter_
- Input_
- Suggestion_

.. Assist:

Assist
------

`Assist chips <https://m3.material.io/components/chips/guidelines#5dd1928c-1476-4029-bdc5-fde66fc0dcb1>`_
represent smart or automated actions that can span multiple apps, such as
opening a calendar event from the home screen. Assist chips function as
though the user asked an assistant to complete the action. They should appear
dynamically and contextually in a UI.

An alternative to assist chips are buttons, which should appear persistently
and consistently.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/assist-chip.png
    :align: center

Example of assist
-----------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            <CommonLabel@MDLabel>
                adaptive_size: True
                theme_text_color: "Custom"
                text_color: "#e6e9df"


            <CommonAssistChip@MDChip>
                # Custom attribute.
                text: ""
                icon: ""

                # Chip attribute.
                type: "assist"
                theme_bg_color: "Custom"
                md_bg_color: "#2a3127"
                theme_line_color: "Custom"
                line_color: "grey"
                theme_elevation_level: "Custom"
                elevation_level: 1
                theme_shadow_softness: "Custom"
                shadow_softness: 2

                MDChipLeadingIcon:
                    icon: root.icon
                    theme_text_color: "Custom"
                    text_color: "#68896c"

                MDChipText:
                    text: root.text
                    theme_text_color: "Custom"
                    text_color: "#e6e9df"


            MDScreen:

                FitImage:
                    source: "bg.png"

                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_size: True
                    pos_hint: {"center_y": .6, "center_x": .5}

                    CommonLabel:
                        text: "in 10 mins"
                        bold: True
                        pos_hint: {"center_x": .5}

                    CommonLabel:
                        text: "Therapy with Thea"
                        font_style: "Display"
                        role: "large"
                        padding_y: "12dp"

                    CommonLabel:
                        text: "Video call"
                        font_style: "Display"
                        role: "small"
                        pos_hint: {"center_x": .5}

                    MDBoxLayout:
                        adaptive_size: True
                        pos_hint: {"center_x": .5}
                        spacing: "12dp"
                        padding: 0, "24dp", 0, 0

                        CommonAssistChip:
                            text: "Home office"
                            icon: "map-marker"

                        CommonAssistChip:
                            text: "Chat"
                            icon: "message"

                    MDWidget:
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Teal"
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.properties import StringProperty
            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.chip import MDChip, MDChipLeadingIcon, MDChipText
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.widget import MDWidget


            class CommonAssistChip(MDChip):
                text = StringProperty()
                icon = StringProperty()

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.type = "assist"
                    self.theme_bg_color = "Custom"
                    self.md_bg_color = "#2a3127"
                    self.theme_line_color = "Custom"
                    self.line_color = "grey"
                    self.theme_elevation_level = "Custom"
                    self.elevation_level = 1
                    self.theme_shadow_softness = "Custom"
                    self.shadow_softness = 2
                    Clock.schedule_once(self._add_widget)

                def _add_widget(self, *args):
                    self.add_widget(
                        MDChipLeadingIcon(
                            icon=self.icon,
                            theme_text_color="Custom",
                            text_color="#68896c",
                        )
                    )
                    self.add_widget(
                        MDChipText(
                            text=self.text,
                            theme_text_color="Custom",
                            text_color="#68896c",
                        )
                    )


            class CommonLabel(MDLabel):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.adaptive_size=True
                    self.theme_text_color="Custom"
                    self.text_color="#e6e9df"


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Teal"
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            FitImage(
                                source="bg.png"
                            ),
                            MDBoxLayout(
                                CommonLabel(
                                    text="in 10 mins",
                                    bold=True,
                                    pos_hint={"center_x": 0.5},
                                ),
                                CommonLabel(
                                    text="Therapy with Thea",
                                    font_style="Display",
                                    role="large",
                                    padding_y="12dp",
                                ),
                                CommonLabel(
                                    text="Video call",
                                    font_style="Display",
                                    role="small",
                                    pos_hint={"center_x": 0.5},
                                ),
                                MDBoxLayout(
                                    CommonAssistChip(
                                        text="Home office",
                                        icon="map-marker",
                                    ),
                                    CommonAssistChip(
                                        text="Chat",
                                        icon="message",
                                    ),
                                    adaptive_size=True,
                                    pos_hint={"center_x": 0.5},
                                    spacing="12dp",
                                    padding=(0, "24dp", 0, 0),
                                ),
                                MDWidget(),
                                orientation="vertical",
                                adaptive_size=True,
                                pos_hint={"center_y": 0.6, "center_x": 0.5},
                            ),
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-assist-chip.png
    :align: center

.. Filter:

Filter
------

`Filter chips <https://m3.material.io/components/chips/guidelines#8d453d50-8d8e-43aa-9ae3-87ed134d2e64>`_
use tags or descriptive words to filter content. They can be a good alternative
to toggle buttons or checkboxes.

Tapping on a filter chip activates it and appends a leading checkmark icon to
the starting edge of the chip label.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/filter-chip.png
    :align: center

Example of filtering
--------------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import StringProperty, ListProperty

            from kivymd.app import MDApp
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.list import MDListItem
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.screen import MDScreen

            import asynckivy

            Builder.load_string(
                '''
            <CustomOneLineIconListItem>

                MDListItemLeadingIcon:
                    icon: root.icon

                MDListItemHeadlineText:
                    text: root.text


            <PreviewIconsScreen>

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "14dp"
                    padding: "20dp"

                    MDTextField:
                        id: search_field
                        mode: "outlined"
                        on_text: root.set_list_md_icons(self.text, True)

                        MDTextFieldLeadingIcon:
                            icon: "magnify"

                        MDTextFieldHintText:
                            text: "Search icon"

                    MDBoxLayout:
                        id: chip_box
                        spacing: "12dp"
                        adaptive_height: True

                    RecycleView:
                        id: rv
                        viewclass: "CustomOneLineIconListItem"
                        key_size: "height"

                        RecycleBoxLayout:
                            padding: dp(10)
                            default_size: None, dp(48)
                            default_size_hint: 1, None
                            size_hint_y: None
                            height: self.minimum_height
                            orientation: "vertical"
                '''
            )


            class CustomOneLineIconListItem(MDListItem):
                icon = StringProperty()
                text = StringProperty()


            class PreviewIconsScreen(MDScreen):
                filter = ListProperty()  # list of tags for filtering icons

                def set_filter_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    async def set_filter_chips():
                        for tag in ["Outline", "Off", "On"]:
                            await asynckivy.sleep(0)
                            chip = MDChip(
                                MDChipText(
                                    text=tag,
                                ),
                                type="filter",
                                selected_color="green",
                                theme_bg_color="Custom",
                                md_bg_color="#303A29",
                            )
                            chip.bind(active=lambda x, y, z=tag: self.set_filter(y, z))
                            self.ids.chip_box.add_widget(chip)

                    asynckivy.start(set_filter_chips())

                def set_filter(self, active: bool, tag: str) -> None:
                    '''Sets a list of tags for filtering icons.'''

                    if active:
                        self.filter.append(tag)
                    else:
                        self.filter.remove(tag)

                def set_list_md_icons(self, text="", search=False) -> None:
                    '''Builds a list of icons.'''

                    def add_icon_item(name_icon):
                        self.ids.rv.data.append(
                            {
                                "icon": name_icon,
                                "text": name_icon,
                            }
                        )

                    self.ids.rv.data = []
                    for name_icon in md_icons.keys():
                        for tag in self.filter:
                            if tag.lower() in name_icon:
                                if search:
                                    if text in name_icon:
                                        add_icon_item(name_icon)
                                else:
                                    add_icon_item(name_icon)


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.screen = PreviewIconsScreen()

                def build(self) -> PreviewIconsScreen:
                    self.theme_cls.theme_style = "Dark"
                    return self.screen

                def on_start(self) -> None:
                    self.screen.set_list_md_icons()
                    self.screen.set_filter_chips()


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-filtering-icons-chip.gif
    :align: center

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp
            from kivy.lang import Builder
            from kivy.properties import StringProperty, ListProperty

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.list import MDListItem
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.recycleboxlayout import MDRecycleBoxLayout
            from kivymd.uix.recycleview import MDRecycleView
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.textfield import (
                MDTextField, MDTextFieldLeadingIcon, MDTextFieldHintText
            )

            import asynckivy

            Builder.load_string(
                '''
            <CustomOneLineIconListItem>

                MDListItemLeadingIcon:
                    icon: root.icon

                MDListItemHeadlineText:
                    text: root.text
            '''
            )


            class CustomOneLineIconListItem(MDListItem):
                icon = StringProperty()
                text = StringProperty()


            class PreviewIconsScreen(MDScreen):
                filter = ListProperty()  # list of tags for filtering icons

                def set_filter_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    async def set_filter_chips():
                        for tag in ["Outline", "Off", "On"]:
                            await asynckivy.sleep(0)
                            chip = MDChip(
                                MDChipText(
                                    text=tag,
                                ),
                                type="filter",
                                selected_color="green",
                                theme_bg_color="Custom",
                                md_bg_color="#303A29",
                            )
                            chip.bind(active=lambda x, y, z=tag: self.set_filter(y, z))
                            self.get_ids().chip_box.add_widget(chip)

                    asynckivy.start(set_filter_chips())

                def set_filter(self, active: bool, tag: str) -> None:
                    '''Sets a list of tags for filtering icons.'''

                    if active:
                        self.filter.append(tag)
                    else:
                        self.filter.remove(tag)

                def set_list_md_icons(self, text="", search=False) -> None:
                    '''Builds a list of icons.'''

                    def add_icon_item(name_icon):
                        self.get_ids().rv.data.append(
                            {
                                "icon": name_icon,
                                "text": name_icon,
                            }
                        )

                    self.get_ids().rv.data = []
                    for name_icon in md_icons.keys():
                        for tag in self.filter:
                            if tag.lower() in name_icon:
                                if search:
                                    if text in name_icon:
                                        add_icon_item(name_icon)
                                else:
                                    add_icon_item(name_icon)


            class Example(MDApp):
                def build(self) -> PreviewIconsScreen:
                    self.theme_cls.theme_style = "Dark"
                    self.screen = PreviewIconsScreen(
                        MDBoxLayout(
                            MDTextField(
                                MDTextFieldLeadingIcon(
                                    icon="magnify"
                                ),
                                MDTextFieldHintText(
                                    text="Search icon"
                                ),
                                id="search_field",
                                mode="outlined",
                            ),
                            MDBoxLayout(
                                id="chip_box",
                                spacing="12dp",
                                adaptive_height=True,
                            ),
                            MDRecycleView(
                                MDRecycleBoxLayout(
                                    padding=dp(10),
                                    default_size=(None, dp(48)),
                                    default_size_hint=(1, None),
                                    adaptive_height=True,
                                    orientation="vertical",
                                ),
                                id="rv",
                            ),
                            orientation="vertical",
                            spacing="14dp",
                            padding="20dp",
                        )
                    )
                    search_field = self.screen.get_ids().search_field
                    search_field.bind(
                        text=lambda *x: self.screen.set_list_md_icons(search_field.text, True)
                    )
                    self.screen.get_ids().rv.key_size = "height"
                    self.screen.get_ids().rv.viewclass = "CustomOneLineIconListItem"
                    return self.screen

                def on_start(self) -> None:
                    self.screen.set_list_md_icons()
                    self.screen.set_filter_chips()


            Example().run()

Tap a chip to select it. Multiple chips can be selected or unselected:

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.screen import MDScreen

            import asynckivy

            Builder.load_string(
                '''
            <ChipScreen>

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "14dp"
                    padding: "20dp"

                    MDLabel:
                        adaptive_height: True
                        text: "Select Type"

                    MDStackLayout:
                        id: chip_box
                        spacing: "12dp"
                        adaptive_height: True

                    MDWidget:

                MDButton:
                    pos: "20dp", "20dp"
                    on_release: root.unchecks_chips()

                    MDButtonText:
                        text: "Uncheck chips"
                '''
            )


            class ChipScreen(MDScreen):
                async def create_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    for tag in ["Extra Soft", "Soft", "Medium", "Hard"]:
                        await asynckivy.sleep(0)
                        self.ids.chip_box.add_widget(
                            MDChip(
                                MDChipText(
                                    text=tag,
                                ),
                                type="filter",
                                selected_color="green",
                                theme_bg_color="Custom",
                                md_bg_color="#303A29",
                                active=True,
                            )
                        )

                def unchecks_chips(self) -> None:
                    '''Removes marks from all chips.'''

                    for chip in self.ids.chip_box.children:
                        if chip.active:
                            chip.active = False


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.screen = ChipScreen()

                def build(self) -> ChipScreen:
                    self.theme_cls.theme_style = "Dark"
                    return self.screen

                def on_start(self) -> None:
                    asynckivy.start(self.screen.create_chips())


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.stacklayout import MDStackLayout
            from kivymd.uix.widget import MDWidget

            import asynckivy


            class ChipScreen(MDScreen):
                async def create_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    for tag in ["Extra Soft", "Soft", "Medium", "Hard"]:
                        await asynckivy.sleep(0)
                        self.get_ids().chip_box.add_widget(
                            MDChip(
                                MDChipText(
                                    text=tag,
                                ),
                                type="filter",
                                selected_color="green",
                                theme_bg_color="Custom",
                                md_bg_color="#303A29",
                                active=True,
                            )
                        )

                def unchecks_chips(self) -> None:
                    '''Removes marks from all chips.'''

                    for chip in self.get_ids().chip_box.children:
                        if chip.active:
                            chip.active = False


            class Example(MDApp):
                def build(self) -> ChipScreen:
                    self.theme_cls.theme_style = "Dark"
                    self.screen = ChipScreen(
                        MDBoxLayout(
                            MDLabel(
                                adaptive_height=True,
                                text="Select Type",
                            ),
                            MDStackLayout(
                                id="chip_box",
                                spacing="12dp",
                                adaptive_height=True,
                            ),
                            MDWidget(),
                            orientation="vertical",
                            spacing="14dp",
                            padding="20dp",
                        ),
                        MDButton(
                            MDButtonText(
                                text="Uncheck chips"
                            ),
                            id="button",
                            pos=("20dp", "20dp"),
                        )
                    )
                    self.screen.get_ids().button.bind(
                        on_release=lambda x: self.screen.unchecks_chips()
                    )
                    return self.screen

                def on_start(self) -> None:
                    asynckivy.start(self.screen.create_chips())


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-filtering-icons-chip-2.gif
    :align: center

Alternatively, a single chip can be selected.
This offers an alternative to toggle buttons, radio buttons, or single select
menus:

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.screen import MDScreen

            import asynckivy

            Builder.load_string(
                '''
            <ChipScreen>

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "14dp"
                    padding: "20dp"

                    MDLabel:
                        adaptive_height: True
                        text: "Select Type"

                    MDStackLayout:
                        id: chip_box
                        spacing: "12dp"
                        adaptive_height: True

                    MDWidget:
                '''
            )


            class ChipScreen(MDScreen):
                async def create_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    for tag in ["Extra Soft", "Soft", "Medium", "Hard"]:
                        await asynckivy.sleep(0)
                        chip = MDChip(
                            MDChipText(
                                text=tag,
                            ),
                            type="filter",
                            selected_color="green",
                            theme_bg_color="Custom",
                            md_bg_color="#303A29",

                        )
                        chip.bind(active=self.uncheck_chip)
                        self.ids.chip_box.add_widget(chip)

                def uncheck_chip(self, current_chip: MDChip, active: bool) -> None:
                    '''Removes a mark from an already marked chip.'''

                    if active:
                        for chip in self.ids.chip_box.children:
                            if current_chip is not chip:
                                if chip.active:
                                    chip.active = False


            class Example(MDApp):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self.screen = ChipScreen()

                def build(self) -> ChipScreen:
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Lightgreen"
                    return self.screen

                def on_start(self) -> None:
                    asynckivy.start(self.screen.create_chips())


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.chip import MDChip, MDChipText
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.stacklayout import MDStackLayout
            from kivymd.uix.widget import MDWidget

            import asynckivy


            class ChipScreen(MDScreen):
                async def create_chips(self):
                    '''Asynchronously creates and adds chips to the container.'''

                    for tag in ["Extra Soft", "Soft", "Medium", "Hard"]:
                        await asynckivy.sleep(0)
                        chip = MDChip(
                            MDChipText(
                                text=tag,
                            ),
                            type="filter",
                            selected_color="green",
                            theme_bg_color="Custom",
                            md_bg_color="#303A29",

                        )
                        chip.bind(active=self.uncheck_chip)
                        self.get_ids().chip_box.add_widget(chip)

                def uncheck_chip(self, current_chip: MDChip, active: bool) -> None:
                    '''Removes a mark from an already marked chip.'''

                    if active:
                        for chip in self.get_ids().chip_box.children:
                            if current_chip is not chip:
                                if chip.active:
                                    chip.active = False


            class Example(MDApp):
                def build(self) -> ChipScreen:
                    self.theme_cls.theme_style = "Dark"
                    self.screen = ChipScreen(
                        MDBoxLayout(
                            MDLabel(
                                adaptive_height=True,
                                text="Select Type",
                            ),
                            MDStackLayout(
                                id="chip_box",
                                spacing="12dp",
                                adaptive_height=True,
                            ),
                            MDWidget(),
                            orientation="vertical",
                            spacing="14dp",
                            padding="20dp",
                        ),
                    )
                    return self.screen

                def on_start(self) -> None:
                    asynckivy.start(self.screen.create_chips())


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-filtering-single-select.gif
    :align: center

.. Input:

Input
-----

`Input chips <https://m3.material.io/components/chips/guidelines#4d2d5ef5-3fcd-46e9-99f2-067747b2393f>`_
represent discrete pieces of information entered by a user, such as Gmail
contacts or filter options within a search field.

They enable user input and verify that input by converting text into chips.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/input-chip.png
    :align: center

Example of input
----------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDChip:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    type: "input"
                    theme_line_color: "Custom"
                    line_color: "grey"
                    ripple_effect: False

                    MDChipLeadingAvatar:
                        source: "data/logo/kivy-icon-128.png"

                    MDChipText:
                        text: "MDChip"

                    MDChipTrailingIcon:
                        icon: "close"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.chip import (
                MDChipLeadingAvatar, MDChipText, MDChipTrailingIcon, MDChip
            )
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDChip(
                                MDChipLeadingAvatar(
                                    source="data/logo/kivy-icon-128.png"
                                ),
                                MDChipText(
                                    text="MDChip"
                                ),
                                MDChipTrailingIcon(
                                    icon="close"
                                ),
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                type="input",
                                theme_line_color="Custom",
                                line_color="grey",
                                ripple_effect=False,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-input-chip.png
    :align: center

.. Suggestion:

Suggestion
----------

`Suggestion chips <https://m3.material.io/components/chips/guidelines#36d7bb16-a9bf-4cf6-a73d-8e05510d66a7>`_
help narrow a user’s intent by presenting dynamically generated suggestions,
such as possible responses or search filters.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/suggestion-chip.png
    :align: center

Example of suggestion
---------------------

.. tabs::

    .. tab:: Imperative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDChip:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    type: "suggestion"
                    theme_line_color: "Custom"
                    line_color: "grey"

                    MDChipText:
                        text: "MDChip"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.chip import MDChipText, MDChip
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            MDChip(
                                MDChipText(
                                    text="MDChip"
                                ),
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                type="suggestion",
                                theme_line_color="Custom",
                                line_color="grey",
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/example-suggestion.png
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDChip:
            text: "Portland"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.on_release_chip(self)
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_release_chip(self, instance_check):
            print(instance_check)


    Test().run()

2.0.0 version
-------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDChip:
            pos_hint: {"center_x": .5, "center_y": .5}
            theme_line_color: "Custom"
            line_color: "grey"
            on_release: app.on_release_chip(self)

            MDChipText:
                text: "MDChip"
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_release_chip(self, instance_check):
            print(instance_check)


    Example().run()
"""

from __future__ import annotations

__all__ = (
    "MDChip",
    "MDChipLeadingAvatar",
    "MDChipLeadingIcon",
    "MDChipTrailingIcon",
    "MDChipText",
)

import os

from kivy import Logger
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    OptionProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior

from kivymd import uix_path
from kivymd.material_resources import DEVICE_TYPE
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    CommonElevationBehavior,
    RectangularRippleBehavior,
    ScaleBehavior,
    TouchBehavior,
)
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDIcon, MDLabel

with open(
    os.path.join(uix_path, "chip", "chip.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class BaseChipIcon(
    CircularRippleBehavior, ScaleBehavior, ButtonBehavior, MDIcon
):
    icon_color = ColorProperty(None)
    """
    Button icon color in (r, g, b, a) or string format.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color_disabled = ColorProperty(None)
    """
    The icon color in (r, g, b, a) or string format of the chip when
    the chip is disabled.

    .. versionadded:: 2.0.0

    :attr:`icon_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _type = OptionProperty(
        "suggestion", options=["assist", "filter", "input", "suggestion"]
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_scale = 1.5
        Clock.schedule_once(self.adjust_icon_size)

    def adjust_icon_size(self, *args) -> None:
        # If the user has not changed the icon size, then we set the standard
        # icon size according to the standards of material design version 3.
        if (
            self.font_name == "Icons"
            and self.theme_cls.font_styles["Icon"]["large"]["font-size"]
            == self.font_size
        ):
            self.font_size = (
                "18sp"
                if not self.source and not isinstance(self, MDChipLeadingAvatar)
                else "24sp"
            )
        if self.source and isinstance(self, MDChipLeadingAvatar):
            self.icon = self.source
            self._size = [dp(28), dp(28)]
            self.font_size = "28sp"
            self.padding_x = "6dp"
            self._no_ripple_effect = True


class LabelTextContainer(MDBoxLayout):
    """Implements a container for the chip label."""


class LeadingIconContainer(MDBoxLayout):
    """Implements a container for the leading icon."""


class TrailingIconContainer(MDBoxLayout):
    """Implements a container for the trailing icon."""


class MDChipLeadingAvatar(BaseChipIcon):
    """
    Implements the leading avatar for the chip.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """


class MDChipLeadingIcon(BaseChipIcon):
    """
    Implements the leading icon for the chip.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """


class MDChipTrailingIcon(BaseChipIcon):
    """
    Implements the trailing icon for the chip.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """


class MDChipText(MDLabel):
    """
    Implements the label for the chip.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` classes documentation.
    """

    text_color_disabled = ColorProperty(None)
    """
    The text color in (r, g, b, a) or string format of the chip when
    the chip is disabled.

    .. versionadded:: 2.0.0

    :attr:`text_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _type = OptionProperty(
        "suggestion", options=["assist", "filter", "input", "suggestion"]
    )


class MDChip(
    MDBoxLayout,
    RectangularRippleBehavior,
    ButtonBehavior,
    CommonElevationBehavior,
    TouchBehavior,
    StateLayerBehavior,
):
    """
    Chip class.

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.MDBoxLayout` and
    :class:`~kivymd.uix.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivymd.uix.behaviors.touch_behavior.TouchBehavior`
    classes documentation.
    """

    radius = VariableListProperty([dp(8)], length=4)
    """
    Chip radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(8), dp(8), dp(8), dp(8)]`.
    """

    type = OptionProperty(
        "suggestion", options=["assist", "filter", "input", "suggestion"]
    )
    """
    Type of chip.

    .. versionadded:: 2.0.0

    Available options are: `'assist'`, `'filter'`, `'input'`, `'suggestion'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'suggestion'`.
    """

    active = BooleanProperty(False)
    """
    Whether the check is marked or not.

    .. versionadded:: 1.0.0

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    selected_color = ColorProperty(None)
    """
    The background color of the chip in the marked state in (r, g, b, a)
    or string format.

    .. versionadded:: 2.0.0

    :attr:`selected_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color_disabled = ColorProperty(None)
    """
    The color of the outline in the disabled state

    .. versionadded:: 2.0.0

    :attr:`line_color_disabled` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    _line_color = ColorProperty(None)
    _current_md_bg_color = ColorProperty(None)
    # A flag that disallow ripple animation of the chip
    # at the time of clicking the chip icons.
    _allow_chip_ripple = BooleanProperty(True)
    # The flag signals the end of the ripple animation.
    _anim_complete = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_long_touch(self, *args) -> None:
        """Fired when the widget is pressed for a long time."""

        if self.type == "filter":
            self.active = not self.active

    def on_line_color(self, instance, value) -> None:
        """Fired when the values of :attr:`line_color` change."""

        if not self.disabled:
            self._line_color = value

    def on_type(self, instance, value: str) -> None:
        """Fired when the values of :attr:`type` change."""

        def adjust_padding(*args):
            """
            According to the type of chip, it sets the margins according
            to the specification of the material design version 3.
            """

            self.padding = {
                "input": (
                    (
                        "12dp"
                        if not self.ids.leading_icon_container.children
                        else (
                            "5dp"
                            if not self.ids.leading_icon_container.children[
                                0
                            ].source
                            else "16dp"
                        )
                    ),
                    0,
                    "4dp",
                    0,
                ),
                "assist": (
                    (
                        "16dp"
                        if not self.ids.leading_icon_container.children
                        else "8dp"
                    ),
                    0,
                    (
                        "16dp"
                        if not self.ids.leading_icon_container.children
                        else "8dp"
                    ),
                    0,
                ),
                "suggestion": (
                    (
                        "16dp"
                        if not self.ids.leading_icon_container.children
                        else "8dp"
                    ),
                    0,
                    "16dp",
                    0,
                ),
                "filter": (
                    (
                        "16dp"
                        if not self.ids.leading_icon_container.children
                        else (
                            "8dp"
                            if not self.ids.leading_icon_container.children[
                                0
                            ].source
                            else "4dp"
                        )
                    ),
                    0,
                    (
                        "16dp"
                        if not self.ids.trailing_icon_container.children
                        else "8dp"
                    ),
                    0,
                ),
            }[value]

        Clock.schedule_once(adjust_padding)

    def on_active(self, instance_check, active_value: bool) -> None:
        """Called when the values of :attr:`active` change."""

        if active_value:
            self._current_md_bg_color = self.md_bg_color

        Clock.schedule_once(self.complete_anim_ripple, 0.5)

    def complete_anim_ripple(self, *args) -> None:
        """Called at the end of the ripple animation."""

        if self.active:
            if not self.ids.leading_icon_container.children:
                if self.type == "filter":
                    self.add_marked_icon_to_chip()
            self.set_chip_bg_color(
                self.selected_color
                if self.selected_color
                else (
                    {
                        "filter": self.theme_cls.surfaceContainerLowColor,
                        "suggestion": self.theme_cls.surfaceContainerLowColor,
                        "input": self.theme_cls.surfaceContainerLowColor,
                        "assist": self.theme_cls.surfaceContainerLowColor,
                    }[self.type]
                    if self.theme_bg_color == "Primary"
                    else self.md_bg_color
                )
            )
        else:
            if (
                self.ids.leading_icon_container.children
                and self.ids.leading_icon_container.children[0].icon == "check"
            ):
                if self.type == "filter":
                    self.remove_marked_icon_from_chip()
            self.set_chip_bg_color(self._current_md_bg_color)

    def remove_marked_icon_from_chip(self) -> None:
        def remove_marked_icon_from_chip(*args):
            self.ids.leading_icon_container.clear_widgets()

        if self.ids.leading_icon_container.children:
            anim = Animation(scale_value_x=0, scale_value_y=0, d=0.2)
            anim.bind(on_complete=remove_marked_icon_from_chip)
            anim.start(self.ids.leading_icon_container.children[0])
            Animation(
                padding=[dp(16), 0, dp(16), 0],
                spacing=0,
                d=0.2,
            ).start(self)

    def add_marked_icon_to_chip(self) -> None:
        """Adds and animates a check icon to the chip."""

        icon_check = MDChipLeadingIcon(
            icon="check",
            pos_hint={"center_y": 0.5},
            font_size=dp(18),
            scale_value_x=0,
            scale_value_y=0,
        )
        icon_check.bind(
            on_press=self._set_allow_chip_ripple,
            on_release=self._set_allow_chip_ripple,
        )
        self.ids.leading_icon_container.add_widget(icon_check)
        # Animating the scale of the icon.
        Animation(scale_value_x=1, scale_value_y=1, d=0.2).start(icon_check)
        # Animating the padding of the chip.
        Animation(
            padding=[dp(18), 0, 0, 0],
            spacing=dp(18) if self.type == "filter" else 0,
            d=0.2,
        ).start(self)

    def set_chip_bg_color(self, color: list | str) -> None:
        """Animates the background color of the chip."""

        if color:
            Animation(md_bg_color=color, d=0.2).start(self)
        self._anim_complete = not self._anim_complete

    def on_press(self, *args) -> None:
        """Fired when the button is pressed."""

        if self.active:
            self.active = False

        self._on_press(args)

    def on_release(self, *args) -> None:
        """
        Fired when the button is released
        (i.e. the touch/click that pressed the button goes away).
        """

        self._on_release(args)

    def add_widget(self, widget, *args, **kwargs):
        def set_type(*args):
            widget._type = self.type

        def add_icon_leading_trailing(container):
            if len(container.children):
                type_icon = (
                    "'leading'"
                    if isinstance(
                        widget, (MDChipLeadingIcon, MDChipLeadingAvatar)
                    )
                    else "'trailing'"
                )
                Logger.warning(
                    f"KivyMD: "
                    f"Do not use more than one {type_icon} icon. "
                    f"This is contrary to the material design rules "
                    f"of version 3"
                )
                return
            if isinstance(widget, MDChipTrailingIcon) and self.type in [
                "assist",
                "suggestion",
            ]:
                Logger.warning(
                    f"KivyMD: "
                    f"According to the material design standards of version "
                    f"3, do not use the trailing icon for an '{self.type}' "
                    f"type chip."
                )
                return
            if (
                isinstance(widget, MDChipTrailingIcon)
                and self.type == "filter"
                and DEVICE_TYPE == "mobile"
            ):
                Logger.warning(
                    "KivyMD: "
                    "According to the material design standards of version 3, "
                    "only on desktop computers and tablets, filter chips can "
                    "contain a finishing icon for directly removing the chip "
                    "or opening the options menu."
                )
                return
            if (
                isinstance(widget, (MDChipLeadingIcon, MDChipLeadingAvatar))
                and self.type == "filter"
            ):
                Logger.warning(
                    "KivyMD: "
                    "According to the material design standards of version 3, "
                    "it is better not to use a leading icon for a 'filter' "
                    "type chip."
                )
            if (
                isinstance(widget, MDChipLeadingAvatar)
                and self.type == "suggestion"
            ):
                Logger.warning(
                    "KivyMD: "
                    "According to the material design standards of version 3, "
                    "it is better not to use a leading avatar for a "
                    "'suggestion' type chip."
                )
                return

            widget.bind(
                on_press=self._set_allow_chip_ripple,
                on_release=self._set_allow_chip_ripple,
            )
            widget.pos_hint = {"center_y": 0.5}
            self.padding = ("8dp", 0, "8dp", 0)
            self.spacing = (
                "8dp"
                if isinstance(
                    widget,
                    (
                        MDChipLeadingIcon,
                        MDChipLeadingAvatar,
                        MDChipTrailingIcon,
                    ),
                )
                else 0
            )
            container.add_widget(widget)

        if isinstance(widget, MDChipText):
            Clock.schedule_once(set_type)
            widget.adaptive_size = True
            widget.pos_hint = {"center_y": 0.5}
            if self.type == "suggestion":
                self.padding = ("16dp", 0, "16dp", 0)
            Clock.schedule_once(
                lambda x: self.ids.label_container.add_widget(widget)
            )
        elif isinstance(widget, (MDChipLeadingIcon, MDChipLeadingAvatar)):
            Clock.schedule_once(set_type)
            Clock.schedule_once(
                lambda x: add_icon_leading_trailing(
                    self.ids.leading_icon_container
                )
            )
        elif isinstance(widget, MDChipTrailingIcon):
            Clock.schedule_once(set_type)
            Clock.schedule_once(
                lambda x: add_icon_leading_trailing(
                    self.ids.trailing_icon_container
                )
            )
        elif isinstance(
            widget,
            (LabelTextContainer, LeadingIconContainer, TrailingIconContainer),
        ):
            if isinstance(
                widget, (LeadingIconContainer, TrailingIconContainer)
            ):
                Clock.schedule_once(set_type)
            return super().add_widget(widget)

    def _set_allow_chip_ripple(
        self, instance: MDChipLeadingIcon | MDChipTrailingIcon
    ) -> None:
        self._allow_chip_ripple = not self._allow_chip_ripple
