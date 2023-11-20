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

from __future__ import annotations

__all__ = ("MDTabs", "MDTabsItem", "MDTabsItemIcon", "MDTabsItemLabel")

import os

from kivy.utils import boundary
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ObjectProperty,
    BooleanProperty,
    OptionProperty,
    ColorProperty,
    AliasProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    DeclarativeBehavior,
    RectangularRippleBehavior,
    CommonElevationBehavior,
)
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.label import MDLabel, MDIcon

with open(os.path.join(uix_path, "tab", "tab.kv"), encoding="utf-8") as kv_file:
    Builder.load_string(kv_file.read())


class MDTabsScrollView(ScrollView):
    def goto(self, scroll_x: float | None, scroll_y: float | None) -> None:
        """Update event value along with scroll_*."""

        def _update(e, x):
            if e:
                e.value = (e.max + e.min) * x

        if not (scroll_x is None):
            Animation(scroll_x=scroll_x, d=0.2).start(self)
            # self.scroll_x = scroll_x
            _update(self.effect_x, scroll_x)

        if not (scroll_y is None):
            self.scroll_y = scroll_y
            _update(self.effect_y, scroll_y)


class MDTabsItemLabel(MDLabel):
    """
    Implements an label for the :class:`~MDTabsItem` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.

    .. versionchanged:: 2.0.0
    """

    _active = BooleanProperty(False)


class MDTabsItemIcon(MDIcon):
    """
    Implements an icon for the :class:`~MDTabsItem` class.

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDIcon` class documentation.

    .. versionchanged:: 2.0.0
    """


class MDTabsItem(
    DeclarativeBehavior,
    ThemableBehavior,
    RectangularRippleBehavior,
    FocusBehavior,
    ButtonBehavior,
    BoxLayout,
):
    """
    Implements a menu item with an icon and text.

    .. versionchanged:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.behaviors.ripple_behavior.RectangularRippleBehavior` and
    :class:`~kivymd.uix.behaviors.behaviors.focus_behavior.FocusBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    active = BooleanProperty(False)
    """
    Is the tab active.

    :attr:`active` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _tabs = ObjectProperty()

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, (MDTabsItemLabel, MDTabsItemIcon)):
            if len(self.children) <= 1:
                Clock.schedule_once(lambda x: self._set_width(widget))

    def on_release(self):
        print(self._tabs.ids.container.width)
        # self._tabs.ids.tab_scroll.goto(x, None)

        # Automatic scroll animation of the tab bar.
        bound_left = self._tabs.center_x - self._tabs.x
        bound_right = self._tabs.ids.container.width - bound_left
        dt = self.center_x - bound_left
        sx, sy = self._tabs.ids.tab_scroll.convert_distance_to_scroll(dt, 0)
        lsx = self._tabs.ids.tab_scroll.scroll_x  # ast scroll x of the tab bar
        scroll_is_late = lsx < sx  # determine scroll direction
        dst = abs(lsx - sx) * 0.5  # distance to run

        if not dst:
            return
        if scroll_is_late and self.center_x > bound_left:
            x = lsx + dst
        elif not scroll_is_late and self.center_x < bound_right:
            x = lsx - dst
        else:
            return
        x = boundary(x, 0.0, 1.0)
        self._tabs.ids.tab_scroll.goto(x, None)

    def _set_width(self, widget):
        def set_width(*args):
            self.width = widget.texture_size[0] + widget.padding_x + 2

        if not self._tabs.allow_stretch and isinstance(widget, MDTabsItemLabel):
            Clock.schedule_once(set_width)

        super().add_widget(widget)


class MDTabs(
    DeclarativeBehavior,
    ThemableBehavior,
    CommonElevationBehavior,
    BoxLayout,
):
    """
    Tabs class.
    You can use this class to create your own tabbed panel.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.

    :Events:
        `on_tab_switch`
            Called when switching tabs.
    """

    md_bg_color = ColorProperty(None)
    """
    The background color of the widget.

    :attr:`md_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    type = OptionProperty("primary", options=["primary", "secondary"])
    """
    Panel type.
    Available options are: `'primary'`, `'secondary'`.

    .. versionchanged:: 2.0.0

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'primary'`.
    """

    label_only = BooleanProperty(False)
    """
    Tabs with a label only or with an icon and a label.

    .. versionchanged:: 2.0.0

    :attr:`label_only` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    allow_stretch = BooleanProperty(False)
    """
    Whether to stretch tabs to the width of the panel.

    :attr:`allow_stretch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._check_panel_height)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, MDTabsItem):
            widget._tabs = self
            widget.bind(on_release=self.set_active_item)
            self.ids.container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def set_active_item(self, item: MDTabsItem) -> None:
        """Sets the active tab item."""

        for widget in self.ids.container.children:
            if item is widget:
                widget.active = not widget.active

                for widget_item in item.children:
                    if isinstance(widget_item, MDTabsItemLabel):
                        widget_item._active = widget.active
                        Animation(
                            text_color=self.theme_cls.primaryColor
                            if widget.active
                            else self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)
                    if isinstance(widget_item, MDTabsItemIcon):
                        widget_item._active = widget.active
                        Animation(
                            icon_color=self.theme_cls.primaryColor
                            if widget.active
                            else self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)
            else:
                widget.active = False
                for widget_item in widget.children:
                    widget_item._active = widget.active
                    if isinstance(widget_item, MDTabsItemLabel):
                        Animation(
                            text_color=self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)
                    if isinstance(widget_item, MDTabsItemIcon):
                        Animation(
                            icon_color=self.theme_cls.onSurfaceVariantColor,
                            d=0.2,
                        ).start(widget_item)

    def on_size(self, instance, size) -> None:
        """Fired when the application screen size changes."""

        width, height = size
        number_tabs = len(self.ids.container.children)

        if self.allow_stretch:
            for tab in self.ids.container.children:
                tab.width = width / number_tabs

    def _check_panel_height(self, *args):
        if self.label_only:
            self.height = dp(48)
        else:
            self.height = dp(64)
