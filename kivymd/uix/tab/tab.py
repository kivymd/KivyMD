"""
Components/Tabs
===============

.. seealso::

    `Material Design spec, Tabs <https://material.io/components/tabs>`_

.. rubric:: Tabs organize content across different screens, data sets,
    and other interactions.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs.png
    :align: center

.. Note:: Module provides tabs in the form of icons or text.

Usage
-----

To create a tab, you must create a new class that inherits from the
:class:`~MDTabsBase` class and the `Kivy` container, in which you will create
content for the tab.

.. code-block:: python

    class Tab(MDFloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''

.. code-block:: kv

    <Tab>

        MDLabel:
            text: root.content_text
            pos_hint: {"center_x": .5, "center_y": .5}

All tabs must be contained inside a :class:`~MDTabs` widget:

.. code-block:: kv

    Root:

        MDTabs:

            Tab:
                title: "Tab 1"
                content_text: f"This is an example text for {self.title}"

            Tab:
                title: "Tab 2"
                content_text: f"This is an example text for {self.title}"

            ...

Example with tab icon
---------------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.tab import MDTabsBase
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.icon_definitions import md_icons

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs
                    on_tab_switch: app.on_tab_switch(*args)


            <Tab>

                MDIconButton:
                    id: icon
                    icon: root.icon
                    icon_size: "48sp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    for tab_name in self.icons:
                        self.root.ids.tabs.add_widget(Tab(icon=tab_name))

                def on_tab_switch(
                    self, instance_tabs, instance_tab, instance_tab_label, tab_text
                ):
                    '''
                    Called when switching tabs.

                    :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                    :param instance_tab: <__main__.Tab object>;
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                    :param tab_text: text or name icon of tab;
                    '''

                    count_icon = instance_tab.icon  # get the tab icon
                    print(f"Welcome to {count_icon}' tab'")


            Example().run()

    .. tab:: Declarative python styles

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    self.root.ids.tabs.bind(on_tab_switch=self.on_tab_switch)

                    for tab_name in self.icons:
                        self.root.ids.tabs.add_widget(
                            Tab(
                                MDIconButton(
                                    icon=tab_name,
                                    icon_size="48sp",
                                    pos_hint={"center_x": .5, "center_y": .5},
                                ),
                                icon=tab_name,
                            )
                        )

                def on_tab_switch(
                    self, instance_tabs, instance_tab, instance_tab_label, tab_text
                ):
                    '''
                    Called when switching tabs.

                    :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                    :param instance_tab: <__main__.Tab object>;
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                    :param tab_text: text or name icon of tab;
                    '''

                    count_icon = instance_tab.icon  # get the tab icon
                    print(f"Welcome to {count_icon}' tab'")


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example.gif
    :align: center

Example with tab text
---------------------

.. Note:: The :class:`~MDTabsBase` class has an icon parameter and, by default,
    tries to find the name of the icon in the file
    ``kivymd/icon_definitions.py``.

    If the name of the icon is not found, the class will send a message
    stating that the icon could not be found.

    if the tab has no icon, title or tab_label_text, the class will raise a
    ValueError.

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.tab import MDTabsBase

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs
                    on_tab_switch: app.on_tab_switch(*args)


            <Tab>

                MDLabel:
                    id: label
                    text: "Tab 0"
                    halign: "center"
            '''


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    for i in range(20):
                        self.root.ids.tabs.add_widget(Tab(title=f"Tab {i}"))

                def on_tab_switch(
                    self, instance_tabs, instance_tab, instance_tab_label, tab_text
                ):
                    '''Called when switching tabs.

                    :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                    :param instance_tab: <__main__.Tab object>;
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                    :param tab_text: text or name icon of tab;
                    '''

                    instance_tab.ids.label.text = tab_text


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.label import MDLabel
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    self.root.ids.tabs.bind(on_tab_switch=self.on_tab_switch)
                    for i in range(20):
                        self.root.ids.tabs.add_widget(
                            Tab(
                                MDLabel(id="label", text="Tab 0", halign="center"),
                                title=f"Tab {i}",
                            )
                        )

                def on_tab_switch(
                    self, instance_tabs, instance_tab, instance_tab_label, tab_text
                ):
                    '''
                    Called when switching tabs.

                    :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                    :param instance_tab: <__main__.Tab object>;
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                    :param tab_text: text or name icon of tab;
                    '''

                    instance_tab.ids.label.text = tab_text


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example-text.gif
    :align: center

Example with tab icon and text
------------------------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.tab import MDTabsBase
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.icon_definitions import md_icons

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs
            '''


            class Tab(MDFloatLayout, MDTabsBase):
                pass


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    for name_tab in list(md_icons.keys())[15:30]:
                        self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDFloatLayout, MDTabsBase):
                pass


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    for name_tab in list(md_icons.keys())[15:30]:
                        self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example-icon-text.gif
    :align: center

Dynamic tab management
----------------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.uix.scrollview import MDScrollView
            from kivymd.app import MDApp
            from kivymd.uix.tab import MDTabsBase

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs


            <Tab>

                MDList:

                    MDBoxLayout:
                        adaptive_height: True

                        MDFlatButton:
                            text: "ADD TAB"
                            on_release: app.add_tab()

                        MDFlatButton:
                            text: "REMOVE LAST TAB"
                            on_release: app.remove_tab()

                        MDFlatButton:
                            text: "GET TAB LIST"
                            on_release: app.get_tab_list()
            '''


            class Tab(MDScrollView, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                index = 0

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    self.add_tab()

                def get_tab_list(self):
                    '''Prints a list of tab objects.'''

                    print(self.root.ids.tabs.get_tab_list())

                def add_tab(self):
                    self.index += 1
                    self.root.ids.tabs.add_widget(Tab(title=f"{self.index} tab"))

                def remove_tab(self):
                    if self.index > 1:
                        self.index -= 1
                    self.root.ids.tabs.remove_widget(
                        self.root.ids.tabs.get_tab_list()[-1]
                    )


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.button import MDFlatButton
            from kivymd.uix.list import MDList
            from kivymd.uix.scrollview import MDScrollView
            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDScrollView, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                index = 0

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    self.add_tab()

                def get_tab_list(self, *args):
                    '''Prints a list of tab objects.'''

                    print(self.root.ids.tabs.get_tab_list())

                def add_tab(self, *args):
                    self.index += 1
                    self.root.ids.tabs.add_widget(
                        Tab(
                            MDList(
                                MDBoxLayout(
                                    MDFlatButton(
                                        text="ADD TAB",
                                        on_release=self.add_tab,
                                    ),
                                    MDFlatButton(
                                        text="REMOVE LAST TAB",
                                        on_release=self.remove_tab,
                                    ),
                                    MDFlatButton(
                                        text="GET TAB LIST",
                                        on_release=self.get_tab_list,
                                    ),
                                    adaptive_height=True,
                                ),
                            ),
                            title=f"{self.index} tab",
                        )
                    )

                def remove_tab(self, *args):
                    if self.index > 1:
                        self.index -= 1
                    self.root.ids.tabs.remove_widget(
                        self.root.ids.tabs.get_tab_list()[-1]
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-dynamic-managmant.gif
    :align: center

Use on_ref_press method
-----------------------

You can use markup for the text of the tabs and use the ``on_ref_press``
method accordingly:

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.font_definitions import fonts
            from kivymd.uix.tab import MDTabsBase
            from kivymd.icon_definitions import md_icons

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs
                    on_ref_press: app.on_ref_press(*args)


            <Tab>

                MDIconButton:
                    id: icon
                    icon: app.icons[0]
                    icon_size: "48sp"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    for name_tab in self.icons:
                        self.root.ids.tabs.add_widget(
                            Tab(
                                title=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {name_tab}"
                            )
                        )

                def on_ref_press(
                    self,
                    instance_tabs,
                    instance_tab_label,
                    instance_tab,
                    instance_tab_bar,
                    instance_carousel,
                ):
                    '''
                    The method will be called when the ``on_ref_press`` event
                    occurs when you, for example, use markup text for tabs.

                    :param instance_tabs: <kivymd.uix.tab.MDTabs object>
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
                    :param instance_tab: <__main__.Tab object>
                    :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
                    :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
                    '''

                    # Removes a tab by clicking on the close icon on the left.
                    for instance_tab in instance_carousel.slides:
                        if instance_tab.title == instance_tab_label.text:
                            instance_tabs.remove_widget(instance_tab_label)
                            break


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.font_definitions import fonts
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    self.root.ids.tabs.bind(on_ref_press=self.on_ref_press)
                    for name_tab in self.icons:
                        self.root.ids.tabs.add_widget(
                            Tab(
                                MDIconButton(
                                    icon=self.icons[0],
                                    icon_size="48sp",
                                    pos_hint={"center_x": .5, "center_y": .5}
                                ),
                                title=(
                                    f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]"
                                    f"{md_icons['close']}[/font][/ref]  {name_tab}"
                                ),
                            )
                        )

                def on_ref_press(
                        self,
                        instance_tabs,
                        instance_tab_label,
                        instance_tab,
                        instance_tab_bar,
                        instance_carousel,
                ):
                    '''
                    The method will be called when the ``on_ref_press`` event
                    occurs when you, for example, use markup text for tabs.

                    :param instance_tabs: <kivymd.uix.tab.MDTabs object>
                    :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
                    :param instance_tab: <__main__.Tab object>
                    :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
                    :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
                    '''

                    # Removes a tab by clicking on the close icon on the left.
                    for instance_tab in instance_carousel.slides:
                        if instance_tab.title == instance_tab_label.text:
                            instance_tabs.remove_widget(instance_tab_label)
                            break


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-on-ref-press.gif
    :align: center

Switching the tab by name
-------------------------

.. tabs::

    .. tab:: Declarative KV and imperative python styles

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.tab import MDTabsBase

            KV = '''
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Example Tabs"

                MDTabs:
                    id: tabs


            <Tab>

                MDBoxLayout:
                    orientation: "vertical"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    spacing: dp(48)

                    MDIconButton:
                        id: icon
                        icon: "arrow-right"
                        icon_size: "48sp"
                        on_release: app.switch_tab_by_name()

                    MDIconButton:
                        id: icon2
                        icon: "page-next"
                        icon_size: "48sp"
                        on_release: app.switch_tab_by_object()
            '''


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    self.iter_list_names = iter(list(self.icons))
                    return Builder.load_string(KV)

                def on_start(self):
                    for name_tab in list(self.icons):
                        self.root.ids.tabs.add_widget(Tab(tab_label_text=name_tab))
                    self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))

                def switch_tab_by_object(self):
                    try:
                        x = next(self.iter_list_objects)
                        print(f"Switch slide by object, next element to show: [{x}]")
                        self.root.ids.tabs.switch_tab(x)
                    except StopIteration:
                        # reset the iterator an begin again.
                        self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
                        self.switch_tab_by_object()

                def switch_tab_by_name(self):
                    '''Switching the tab by name.'''

                    try:
                        x = next(self.iter_list_names)
                        print(f"Switch slide by name, next element to show: [{x}]")
                        self.root.ids.tabs.switch_tab(x)
                    except StopIteration:
                        # Reset the iterator an begin again.
                        self.iter_list_names = iter(list(self.icons))
                        self.switch_tab_by_name()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.tab import MDTabsBase, MDTabs
            from kivymd.uix.toolbar import MDTopAppBar


            class Tab(MDFloatLayout, MDTabsBase):
                '''Class implementing content for a tab.'''


            class Example(MDApp):
                icons = list(md_icons.keys())[15:30]

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    self.iter_list_names = iter(list(self.icons))
                    return (
                        MDBoxLayout(
                            MDTopAppBar(title="Example Tabs"),
                            MDTabs(id="tabs"),
                            orientation="vertical",
                        )
                    )

                def on_start(self):
                    for name_tab in list(self.icons):
                        self.root.ids.tabs.add_widget(
                            Tab(
                                MDBoxLayout(
                                    MDIconButton(
                                        id="icon",
                                        icon="arrow-right",
                                        icon_size="48sp",
                                        on_release=self.switch_tab_by_name,
                                    ),
                                    MDIconButton(
                                        id="icon2",
                                        icon="arrow-left",
                                        icon_size="48sp",
                                        on_release=self.switch_tab_by_object,
                                    ),
                                    orientation="vertical",
                                    pos_hint={"center_x": .5, "center_y": .5},
                                    adaptive_size=True,
                                    spacing=dp(48),
                                ),
                                tab_label_text=name_tab,
                            )
                        )

                    self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))

                def switch_tab_by_object(self, *args):
                    try:
                        x = next(self.iter_list_objects)
                        print(f"Switch slide by object, next element to show: [{x}]")
                        self.root.ids.tabs.switch_tab(x)
                    except StopIteration:
                        # reset the iterator an begin again.
                        self.iter_list_objects = iter(
                            list(self.root.ids.tabs.get_tab_list()))
                        self.switch_tab_by_object()

                def switch_tab_by_name(self, *args):
                    '''Switching the tab by name.'''

                    try:
                        x = next(self.iter_list_names)
                        print(f"Switch slide by name, next element to show: [{x}]")
                        self.root.ids.tabs.switch_tab(x)
                    except StopIteration:
                        # Reset the iterator an begin again.
                        self.iter_list_names = iter(list(self.icons))
                        self.switch_tab_by_name()


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switching-tab-by-name.gif
    :align: center
"""

__all__ = ("MDTabs", "MDTabsBase")

import os
from typing import Union

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.scrollview import ScrollView
from kivy.utils import boundary

from kivymd import uix_path
from kivymd.font_definitions import fonts, theme_font_styles
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior, ThemeManager
from kivymd.uix.behaviors import (
    DeclarativeBehavior,
    RectangularRippleBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.label import MDLabel

with open(os.path.join(uix_path, "tab", "tab.kv"), encoding="utf-8") as kv_file:
    Builder.load_string(kv_file.read())


class MDTabsException(Exception):
    pass


class MDTabsLabel(ToggleButtonBehavior, RectangularRippleBehavior, MDLabel):
    """This class it represent the label of each tab."""

    text_color_normal = ColorProperty(None)
    text_color_active = ColorProperty(None)
    tab = ObjectProperty()
    tab_bar = ObjectProperty()
    font_name = StringProperty("Roboto")

    def __init__(self, **kwargs):
        self.split_str = " ,-"
        super().__init__(**kwargs)
        self.max_lines = 2
        self.size_hint_x = None
        self.size_hint_min_x = dp(90)
        self.min_space = dp(98)
        self.bind(
            text=self._update_text_size,
        )

    def on_release(self) -> None:
        try:
            self.tab_bar.parent.dispatch(
                "on_tab_switch", self.tab, self, self.text
            )
            # If the label is selected load the relative tab from carousel.
            if self.state == "down":
                self.tab_bar.parent.carousel.load_slide(self.tab)
        except KeyError:
            pass

    def on_texture(self, instance_tabs_label, texture: Texture) -> None:
        # Just save the minimum width of the label based of the content.
        if texture:
            max_width = dp(360)
            min_width = dp(90)
            if texture.width > max_width:
                self.width = max_width
                self.text_size = (max_width, None)
            elif texture.width < min_width:
                self.width = min_width
            else:
                self.width = texture.width

    def _update_text_size(self, *args):
        if not self.tab_bar:
            return
        if self.tab_bar.parent.allow_stretch is True:
            self.text_size = (None, None)
        else:
            self.width = self.tab_bar.parent.fixed_tab_label_width
            self.text_size = (self.width, None)
        Clock.schedule_once(self.tab_bar._label_request_indicator_update, 0)


class MDTabsBase:
    """
    This class allow you to create a tab.
    You must create a new class that inherits from MDTabsBase.
    In this way you have total control over the views of your tabbed panel.
    """

    icon = StringProperty()
    """
    This property will set the Tab's Label Icon.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title_icon_mode = OptionProperty("Lead", options=["Lead", "Top"])
    """
    This property sets the mode in wich the tab's title and icon are shown.

    :attr:`title_icon_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Lead'`.
    """

    title = StringProperty()
    """
    This property will set the Name of the tab.

    .. note::
        As a side note.

        All tabs have set `markup = True`.
        Thanks to this, you can use the kivy markup language to set a colorful
        and fully customizable tabs titles.

    .. warning::
        The material design requires that every title label is written in
        capital letters, because of this, the `string.upper()` will be applied
        to it's contents.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title_is_capital = BooleanProperty(False)
    """
    This value controls wether if the title property should be converted to
    capital letters.

    :attr:`title_is_capital` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    tab_label_text = StringProperty()
    """
    This property is the actual title's Label of the tab.
    use the property :attr:`icon` and :attr:`title` to set this property
    correctly.

    This property is kept public for specific and backward compatibility
    purposes.

    :attr:`tab_label_text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    tab_label = ObjectProperty()
    """
    It is the label object reference of the tab.

    :attr:`tab_label` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def _get_label_font_style(self):
        if self.tab_label:
            return self.tab_label.font_style

    def _set_label_font_style(self, value):
        if self.tab_label:
            if value in theme_font_styles:
                self.tab_label.font_style = value
            else:
                raise ValueError(
                    "tab_label_font_style:\n\t"
                    "font_style not found in theme_font_styles\n\t"
                    f"font_style = {value}"
                )
        else:
            Clock.schedule_once(lambda x: self._set_label_font_style(value))
            return True

    tab_label_font_style = AliasProperty(
        _get_label_font_style,
        _set_label_font_style,
        cache=True,
    )
    """
    :attr:`tab_label_font_style` is an :class:`~kivy.properties.AliasProperty`
    that behavies similar to an :class:`~kivy.properties.OptionProperty`.

    This property's behavior allows the developer to use any new label style
    registered to the app.

    This property will affect the Tab's Title Label widget.
    """

    def __init__(self, *args, **kwargs):
        self.tab_label = MDTabsLabel(tab=self)
        super().__init__(*args, **kwargs)
        self.bind(
            icon=self._update_text,
            title=self._update_text,
            title_icon_mode=self._update_text,
            tab_label_text=self.update_label_text,
            title_is_capital=self.update_label_text,
        )
        Clock.schedule_once(
            self._update_text
        )  # this will ensure the text is correct

    def _update_text(self, *args):
        # Ensures that the title is in capital letters.
        if self.title and self.title_is_capital is True:
            if self.title != self.title.upper():
                self.title = self.title.upper()
                # Avoids event recursion.
                return
        # Add the icon.
        if self.icon and self.icon in md_icons:
            self.tab_label_text = f"[size=24sp][font={fonts[-1]['fn_regular']}]{md_icons[self.icon]}[/size][/font]"
            if self.title:
                self.tab_label_text = (
                    self.tab_label_text
                    + (" " if self.title_icon_mode == "Lead" else "\n")
                    + self.title
                )
        # Add the title.
        else:
            if self.icon:
                Logger.error(
                    f"{self}: [UID] = [{self.uid}]:\n\t"
                    f"Icon '{self.icon}' not found in md_icons"
                )
            if self.title:
                self.tab_label_text = self.title
            else:
                if not self.tab_label_text:
                    raise ValueError(
                        f"{self}: [UID] = [{self.uid}]:\n\t"
                        "No valid Icon was found.\n\t"
                        "No valid Title was found.\n\t"
                        f"Icon\t= '{self.icon}'\n\t"
                        f"Title\t= '{self.title}'\n\t"
                    )

        self.tab_label.padding = dp(16), 0
        self.update_label_text(None, self.tab_label_text)

    def update_label_text(self, instance_user_tab, text_tab: str) -> None:
        self.tab_label.text = text_tab


class MDTabsMain(MDBoxLayout):
    """
    This class is just a boxlayout that contain the carousel.
    It allows you to have control over the carousel.
    """


class MDTabsCarousel(MDCarousel):
    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def on_touch_move(self, touch):
        if self.lock_swiping:  # lock a swiping
            return
        if not self.touch_mode_change:
            if self.ignore_perpendicular_swipes and self.direction in (
                "top",
                "bottom",
            ):
                if abs(touch.oy - touch.y) < self.scroll_distance:
                    if abs(touch.ox - touch.x) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True
            elif self.ignore_perpendicular_swipes and self.direction in (
                "right",
                "left",
            ):
                if abs(touch.ox - touch.x) < self.scroll_distance:
                    if abs(touch.oy - touch.y) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True

        if self._get_uid("cavoid") in touch.ud:
            return
        if self._touch is not touch:
            super().on_touch_move(touch)
            return self._get_uid() in touch.ud
        if touch.grab_current is not self:
            return True

        ud = touch.ud[self._get_uid()]
        direction = self.direction[0]

        if ud["mode"] == "unknown":
            if direction in "rl":
                distance = abs(touch.ox - touch.x)
            else:
                distance = abs(touch.oy - touch.y)
            if distance > self.scroll_distance:
                ev = self._change_touch_mode_ev
                if ev is not None:
                    ev.cancel()
                ud["mode"] = "scroll"
        else:
            if direction in "rl":
                self._offset += touch.dx
            if direction in "tb":
                self._offset += touch.dy
        return True


class MDTabsScrollView(ScrollView):
    """This class hacked version to fix scroll_x manual setting."""

    def goto(
        self, scroll_x: Union[float, None], scroll_y: Union[float, None]
    ) -> None:
        """Update event value along with scroll_*."""

        def _update(e, x):
            if e:
                e.value = (e.max + e.min) * x

        if not (scroll_x is None):
            self.scroll_x = scroll_x
            _update(self.effect_x, scroll_x)

        if not (scroll_y is None):
            self.scroll_y = scroll_y
            _update(self.effect_y, scroll_y)


class MDTabsBar(MDCard):
    """
    This class is just a boxlayout that contains the scroll view for tabs.
    It is also responsible for resizing the tab shortcut when necessary.
    """

    target = ObjectProperty(None, allownone=True)
    """
    It is the carousel reference of the next tab / slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab / slide of the carousel.

    :attr:`target` is an :class:`~kivy.properties.ObjectProperty`
    and default to `None`.
    """

    def get_rect_instruction(self):
        canvas_instructions = self.layout.canvas.before.get_group(
            "Indicator_line"
        )
        return canvas_instructions[0]

    indicator = AliasProperty(get_rect_instruction, cache=True)
    """
    It is the :class:`~kivy.graphics.vertex_instructions.RoundedRectangle`
    instruction reference of the tab indicator.

    :attr:`indicator` is an :class:`~kivy.properties.AliasProperty`.
    """

    def get_last_scroll_x(self):
        return self.scrollview.scroll_x

    last_scroll_x = AliasProperty(
        get_last_scroll_x, bind=("target",), cache=True
    )
    """
    Is the carousel reference of the next tab/slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab/slide of the carousel.

    :attr:`last_scroll_x` is an :class:`~kivy.properties.AliasProperty`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_indicator(
        self, x: Union[float, int], w: Union[float, int], radius=None
    ) -> None:
        # Update position and size of the indicator.
        if self.parent.tab_indicator_type == "line-round":
            self.parent._line_x = x
            self.parent._line_width = w
            self.parent._line_height = self.parent.tab_indicator_height
            self.parent._line_radius = self.parent.tab_indicator_height / 2
        elif self.parent.tab_indicator_type == "line-rect":
            self.parent._line_x = x
            self.parent._line_width = w
            self.parent._line_height = self.parent.tab_indicator_height
        else:
            self.indicator.pos = (x, 0)
            self.indicator.size = (w, self.parent.tab_indicator_height)
            if radius:
                self.indicator.radius = radius

    def tab_bar_autoscroll(self, instance_tab_label: MDTabsLabel, step: float):
        # Automatic scroll animation of the tab bar.
        bound_left = self.center_x - self.x
        bound_right = self.layout.width - bound_left
        dt = instance_tab_label.center_x - bound_left
        sx, sy = self.scrollview.convert_distance_to_scroll(dt, 0)
        lsx = self.last_scroll_x  # ast scroll x of the tab bar
        scroll_is_late = lsx < sx  # determine scroll direction
        dst = abs(lsx - sx) * step  # distance to run

        if not dst:
            return
        if scroll_is_late and instance_tab_label.center_x > bound_left:
            x = lsx + dst
        elif not scroll_is_late and instance_tab_label.center_x < bound_right:
            x = lsx - dst
        else:
            return
        x = boundary(x, 0.0, 1.0)
        self.scrollview.goto(x, None)

    def android_animation(
        self, instance_carousel: MDTabsCarousel, offset: Union[float, int]
    ):
        # Try to reproduce the android animation effect.
        if offset != 0 and abs(offset) < instance_carousel.width:
            forward = offset < 0
            offset = abs(offset)
            step = offset / float(instance_carousel.width)
            indicator_animation = self.parent.tab_indicator_anim

            skip_slide = (
                instance_carousel.slides[instance_carousel._skip_slide]
                if instance_carousel._skip_slide is not None
                else None
            )
            next_slide = (
                instance_carousel.next_slide
                if forward
                else instance_carousel.previous_slide
            )
            self.target = skip_slide if skip_slide else next_slide

            if not self.target:
                return

            a = instance_carousel.current_slide.tab_label
            b = self.target.tab_label
            self.tab_bar_autoscroll(b, step)

            # Avoids the animation if `indicator_animation` is True.
            if indicator_animation is False:
                return
            gap_x = abs((a.x) - (b.x))
            gap_w = (b.width) - (a.width)
            if forward:
                x_step = a.x + (gap_x * step)
            else:
                x_step = a.x - gap_x * step
            w_step = a.width + (gap_w * step)
            self.update_indicator(x_step, w_step)

    def _label_request_indicator_update(self, *args):
        widget = self.carousel.current_slide.tab_label
        self.update_indicator(widget.x, widget.width)


class MDTabs(
    DeclarativeBehavior,
    ThemableBehavior,
    SpecificBackgroundColorBehavior,
    AnchorLayout,
):
    """
    Tabs class.
    You can use this class to create your own tabbed panel.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.SpecificBackgroundColorBehavior` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout`
    classes documentation.

    :Events:
        `on_tab_switch`
            Called when switching tabs.
        `on_slide_progress`
            Called while the slide is scrolling.
        `on_ref_press`
            The method will be called when the ``on_ref_press`` event
            occurs when you, for example, use markup text for tabs.
    """

    tab_bar_height = NumericProperty("48dp")
    """
    Height of the tab bar.

    :attr:`tab_bar_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'48dp'`.
    """

    tab_padding = ListProperty([0, 0, 0, 0])
    """
    Padding of the tab bar.

    :attr:`tab_padding` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    tab_indicator_anim = BooleanProperty(False)
    """
    Tab indicator animation. If you want use animation set it to ``True``.

    :attr:`tab_indicator_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    tab_indicator_height = NumericProperty("2dp")
    """
    Height of the tab indicator.

    :attr:`tab_indicator_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'2dp'`.
    """

    tab_indicator_type = OptionProperty(
        "line", options=["line", "fill", "round", "line-round", "line-rect"]
    )
    """
    Type of tab indicator. Available options are: `'line'`, `'fill'`,
    `'round'`, `'line-rect'` and `'line-round'`.

    :attr:`tab_indicator_type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    tab_hint_x = BooleanProperty(False)
    """
    This option affects the size of each child. if it's `True`, the size of
    each tab will be ignored and will use the size available by the container.

    :attr:`tab_hint_x` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    anim_duration = NumericProperty(0.2)
    """
    Duration of the slide animation.

    :attr:`anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    anim_threshold = BoundedNumericProperty(
        0.8, min=0.0, max=1.0, errorhandler=lambda x: 0.0 if x < 0.0 else 1.0
    )
    """
    Animation threshold allow you to change the tab indicator animation effect.

    :attr:`anim_threshold` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.8`.
    """

    allow_stretch = BooleanProperty(True)
    """
    If `True`, the tab will update dynamically (if :attr:`tab_hint_x` is `True`)
    to it's content width, and wrap any text if the widget is wider than `"360dp"`.

    If `False`, the tab won't update to it's maximum texture width.
    this means that the `fixed_tab_label_width` will be used as the label
    width. this will wrap any text inside to fit the fixed value.

    :attr:`allow_stretch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    fixed_tab_label_width = NumericProperty("140dp")
    """
    If :attr:`allow_stretch` is `False`, the class will set this value as the
    width to all the tabs title label.

    :attr:`fixed_tab_label_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `140dp`.
    """

    background_color = ColorProperty(None)
    """
    Background color of tabs in (r, g, b, a) or string format.

    :attr:`background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    underline_color = ColorProperty([0, 0, 0, 0])
    """
    Underline color of tabs in (r, g, b, a) or string format.

    :attr:`underline_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    text_color_normal = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format of the label when it is not selected.

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_active = ColorProperty(None)
    """
    Text color in (r, g, b, a) or string format of the label when it is selected.

    :attr:`text_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    shadow_softness = NumericProperty(12)
    """
    See :attr:`kivymd.uix.behaviors.CommonElevationBehavior.shadow_softness`
    attribute.

    .. versionadded:: 1.1.0

    :attr:`shadow_softness` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `12`.
    """

    shadow_color = ColorProperty([0, 0, 0, 0.6])
    """
    See :attr:`kivymd.uix.behaviors.CommonElevationBehavior.shadow_color`
    attribute.

    .. versionadded:: 1.1.0

    :attr:`shadow_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.6]`.
    """

    shadow_offset = ListProperty((0, 0))
    """
    See :attr:`kivymd.uix.behaviors.CommonElevationBehavior.shadow_offset`
    attribute.

    .. versionadded:: 1.1.0

    :attr:`shadow_offset` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.
    """

    elevation = NumericProperty(0)
    """
    See :attr:`kivymd.uix.behaviors.CommonElevationBehavior.elevation`
    attribute.

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    indicator_color = ColorProperty(None)
    """
    Color indicator in (r, g, b, a) or string format.

    :attr:`indicator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    font_name = StringProperty("Roboto")
    """
    Font name for tab text.

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    ripple_duration = NumericProperty(2)
    """
    Ripple duration when long touching to tab.

    :attr:`ripple_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    no_ripple_effect = BooleanProperty(True)
    """
    Whether to use the ripple effect when tapping on a tab.

    :attr:`no_ripple_effect` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    title_icon_mode = OptionProperty("Lead", options=["Lead", "Top"])
    """
    This property sets the mode in wich the tab's title and icon are shown.

    :attr:`title_icon_mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'Lead'`.
    """

    force_title_icon_mode = BooleanProperty(True)
    """
    If this property is se to `True`, it will force the class to update every
    tab inside the scroll view to the current `title_icon_mode`

    :attr:`force_title_icon_mode` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type("on_tab_switch")
        self.register_event_type("on_ref_press")
        self.register_event_type("on_slide_progress")
        Clock.schedule_once(self._carousel_bind, 1)
        self.theme_cls.bind(
            primary_palette=self.update_icon_color,
            theme_style=self.update_icon_color,
        )
        self.bind(
            force_title_icon_mode=self._parse_icon_mode,
            title_icon_mode=self._parse_icon_mode,
        )
        self.bind(tab_hint_x=self._update_tab_hint_x)

    def update_icon_color(
        self,
        instance_theme_manager: ThemeManager,
        name_theme_style_name_palette: str,
    ) -> None:
        """
        Called when the app's color scheme or style has changed
        (dark theme/light theme).
        """

        for tab_label in self.get_tab_list():
            if not self.text_color_normal:
                tab_label.text_color_normal = self.theme_cls.text_color
            if not self.text_color_active:
                tab_label.text_color_active = self.specific_secondary_text_color

    def switch_tab(self, name_tab: Union[MDTabsLabel, str], search_by="text"):
        """
        This method switch between tabs
        name_tab can be either a String or a :class:`~MDTabsBase`.

        `search_by` will look up through the properties of every tab.

        If the value doesnt match, it will raise a ValueError.

        Search_by options:
            text : will search by the raw text of the label (`tab_label_text`)
            icon : will search by the `icon` property
            title : will search by the `title` property
        """

        if isinstance(name_tab, str):
            if search_by == "title":
                for tab_instance in self.tab_bar.parent.carousel.slides:
                    if tab_instance.title_is_capital is True:
                        _name_tab = name_tab.upper()
                    else:
                        _name_tab = name_tab
                    if tab_instance.title == _name_tab:
                        self.carousel.load_slide(tab_instance)
                        return
            # Search by icon.
            elif search_by == "icon":
                for tab_instance in self.tab_bar.parent.carousel.slides:
                    if tab_instance.icon == name_tab:
                        self.carousel.load_slide(tab_instance)
                        return
            # Search by title.
            else:
                for tab_instance in self.tab_bar.parent.carousel.slides:
                    if tab_instance.tab_label_text == name_tab:
                        self.carousel.load_slide(tab_instance)
                        return
            raise ValueError(
                "switch_tab:\n\t"
                "name_tab not found in the tab list\n\t"
                f"search_by = {repr(search_by)} \n\t"
                f"name_tab = {repr(name_tab)} \n\t"
            )
        else:
            self.carousel.load_slide(name_tab.tab)

    def get_tab_list(self) -> list:
        """Returns a list of :class:`~MDTabsLabel` objects."""

        return self.tab_bar.layout.children[::-1]

    def get_slides(self) -> list:
        """Returns a list of user tab objects."""

        return self.carousel.slides

    def get_current_tab(self):
        """
        Returns current tab object.

        .. versionadded:: 1.0.0
        """

        return self.carousel.current_slide

    def add_widget(self, widget, index=0, canvas=None):
        # You can add only subclass of MDTabsBase.
        if not isinstance(widget, (MDTabsBase, MDTabsMain, MDTabsBar)):
            raise ValueError(
                f"MDTabs[{self.uid}].add_widget:\n\t"
                "The widget provided is not a subclass of MDTabsBase."
            )
        if len(self.children) >= 2:
            try:
                # FIXME: Can't set the value of the `no_ripple_effect`
                #  and `ripple_duration` properties for widget.tab_label.
                widget.tab_label._no_ripple_effect = self.no_ripple_effect
                widget.tab_label.ripple_duration_in_slow = self.ripple_duration
                widget.tab_label.group = str(self)
                widget.tab_label.tab_bar = self.tab_bar
                widget.tab_label.font_name = self.font_name
                widget.tab_label.text_color_normal = (
                    self.text_color_normal
                    if self.text_color_normal
                    else self.specific_secondary_text_color
                )
                widget.tab_label.text_color_active = (
                    self.text_color_active
                    if self.text_color_active
                    else self.specific_text_color
                )
                self.bind(
                    allow_stretch=widget.tab_label._update_text_size,
                    fixed_tab_label_width=widget.tab_label._update_text_size,
                    font_name=widget.tab_label.setter("font_name"),
                    text_color_active=widget.tab_label.setter(
                        "text_color_active"
                    ),
                    text_color_normal=widget.tab_label.setter(
                        "text_color_normal"
                    ),
                )
                Clock.schedule_once(widget.tab_label._update_text_size, 0)
                self.tab_bar.layout.add_widget(widget.tab_label)
                self.carousel.add_widget(widget)
                if self.force_title_icon_mode is True:
                    widget.title_icon_mode = self.title_icon_mode
                Clock.schedule_once(
                    self.tab_bar._label_request_indicator_update, 0
                )
                return
            except AttributeError:
                pass
        if isinstance(widget, (MDTabsMain, MDTabsBar)):
            return super().add_widget(widget)

    def remove_widget(self, widget):
        # You can remove only subclass of MDTabsLabel or MDTabsBase.
        if not issubclass(widget.__class__, (MDTabsLabel, MDTabsBase)):
            raise MDTabsException(
                "MDTabs can remove only subclass of MDTabsLabel or MDTabsBase"
            )
        # If the widget is an instance of MDTabsBase, then the widget is
        # set as the widget's tab_label object.
        if issubclass(widget.__class__, MDTabsBase):
            slide = widget
            title_label = widget.tab_label
        else:
            # We already got the label, so we set the slide reference.
            slide = widget.tab
            title_label = widget
        # Set memory.
        # Search object next tab.
        # Clean all bindings to allow the widget to be collected.
        self.unbind(
            allow_stretch=title_label._update_text_size,
            fixed_tab_label_width=title_label._update_text_size,
            font_name=title_label.setter("font_name"),
            text_color_active=title_label.setter("text_color_active"),
            text_color_normal=title_label.setter("text_color_normal"),
        )
        self.carousel.remove_widget(slide)
        self.tab_bar.layout.remove_widget(title_label)
        # Clean the references.
        slide = None
        title_label = None
        widget = None

    def on_slide_progress(self, *args) -> None:
        """
        This event is deployed every available frame while the tab is scrolling.
        """

    def on_carousel_index(self, instance_tabs_carousel, index: int) -> None:
        """
        Called when the Tab index have changed.

        This event is deployed by the built in carousel of the class.
        """

        # When the index of the carousel change, update tab indicator,
        # select the current tab and reset threshold data.
        if instance_tabs_carousel.current_slide:
            current_tab_label = instance_tabs_carousel.current_slide.tab_label
            if current_tab_label.state == "normal":
                # current_tab_label._do_press()
                current_tab_label.dispatch("on_release")
                current_tab_label._release_group(self)
                current_tab_label.state = "down"

            if self.tab_indicator_type == "round":
                self.tab_indicator_height = self.tab_bar_height
                if index == 0:
                    radius = [
                        0,
                        self.tab_bar_height / 2,
                        self.tab_bar_height / 2,
                        0,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
                elif index == len(self.get_tab_list()) - 1:
                    radius = [
                        self.tab_bar_height / 2,
                        0,
                        0,
                        self.tab_bar_height / 2,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
                else:
                    radius = [
                        self.tab_bar_height / 2,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
            elif (
                self.tab_indicator_type == "fill"
                or self.tab_indicator_type == "line-round"
                or self.tab_indicator_type == "line-rect"
            ):
                self.tab_indicator_height = self.tab_bar_height
                self.tab_bar.update_indicator(
                    current_tab_label.x, current_tab_label.width
                )
            else:
                self.tab_bar.update_indicator(
                    current_tab_label.x, current_tab_label.width
                )

    def on_ref_press(self, *args) -> None:
        """
        This event will be launched every time the user press a markup enabled
        label with a link or reference inside.
        """

    def on_tab_switch(self, *args) -> None:
        """This event is launched every time the current tab is changed."""

    def on_size(self, instance_tab, size: list) -> None:
        """Called when the application screen is resized."""

        if self.carousel.current_slide:
            self._update_indicator(self.carousel.current_slide.tab_label)

    def _update_tab_hint_x(self, *args):
        if not self.ids.layout.children:
            return
        if self.tab_hint_x is True:
            self.fixed_tab_label_width = self.width // len(
                self.ids.layout.children
            )
            self.allow_stretch = False
        else:
            self.allow_stretch = True

    def _parse_icon_mode(self, *args):
        if self.force_title_icon_mode is True:
            for slide in self.carousel.slides:
                slide.title_icon_mode = self.title_icon_mode
                if self.title_icon_mode == "Top":
                    self.tab_bar_height = dp(72)
                else:
                    self.tab_bar_height = dp(48)

    def _carousel_bind(self, interval):
        self.carousel.bind(on_slide_progress=self._on_slide_progress)

    def _on_slide_progress(self, *args):
        self.dispatch("on_slide_progress", args)

    def _update_indicator(self, current_tab_label):
        def update_indicator(interval):
            self.tab_bar.update_indicator(
                current_tab_label.x, current_tab_label.width
            )

        if not current_tab_label:
            current_tab_label = self.tab_bar.layout.children[-1]
        Clock.schedule_once(update_indicator)

    def _update_padding(self, layout, *args):
        if self.tab_hint_x is True:
            layout.padding = [0, 0]
            Clock.schedule_once(self._update_tab_hint_x)
            return True
        padding = [0, 0]
        # FIXME: It's not entirely clear why the `padding = [dp (52), 0]`
        #  instruction is needed? This creates an extra 52px left padding and
        #  looks like a bug. This instruction was added by the contributors in
        #  previous commits and I have not yet figured out why this was done.
        # This is more efficient than to use sum([layout.children]).
        # width = layout.width - (layout.padding[0] * 2)
        # Forces the padding of the tab_bar when the tab_bar is scrollable.
        # if width > self.width:
        #     padding = [dp(52), 0]
        # Set the new padding.
        layout.padding = padding
        # Update the indicator.
        if self.carousel.current_slide:
            self._update_indicator(self.carousel.current_slide.tab_label)
            Clock.schedule_once(
                lambda x: setattr(
                    self.carousel.current_slide.tab_label, "state", "down"
                ),
                -1,
            )
        return True
