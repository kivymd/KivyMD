"""
Components/Expansion Panel
==========================

.. seealso::

    `Material Design spec, Expansion panel <https://material.io/archive/guidelines/components/expansion-panels.html#>`_

.. rubric:: Expansion panels contain creation flows and allow lightweight editing of an element.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.png
    :align: center

Usage
-----

.. code-block:: kv

    Root:

            MDExpansionPanel:
                icon: f"{images_path}kivymd_logo.png"
                # Content of panel. Must be `Kivy` widget.
                content: Content()
                title: "KivyMD"

Example
-------

.. code-block:: python

    from kivy.uix.boxlayout import BoxLayout

    from kivymd.app import MDApp
    from kivy.lang import Builder

    KV = '''
    #:import Content __main__.Content
    #:import images_path kivymd.images_path


    # Content for expansion panel.
    <Content>
        size_hint_y: None
        height: self.minimum_height

        TwoLineIconListItem:
            text: "(050)-123-45-67"
            secondary_text: "Mobile"

            IconLeftWidget:
                icon: 'phone'

    Screen:

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                title: "Expansion panel"
                elevation: 10

            MDExpansionPanel:
                icon: f"{images_path}kivymd_logo.png"
                content: Content()
                title: "KivyMD"

            Widget:
    '''


    class Content(BoxLayout):
        pass


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.gif
    :align: center

.. rubric:: Two events are available for :class:`~MDExpansionPanel`:

:attr:`~MDExpansionPanel.on_open`

:attr:`~MDExpansionPanel.on_close`

.. code-block:: kv

        MDExpansionPanel:
            on_open: app.on_panel_open(args)
            on_close: app.on_panel_close(args)

The user function takes one argument - the object of the panel:

.. code-block:: python

    def on_panel_open(self, instance_panel):
        print(instance_panel)

.. Note:: `See Expansion panel example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Expansion-Panel>`_

    `Expansion panel and MDCard <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Expansion-Panel-and-MDCard>`_
"""

__all__ = ("MDExpansionPanel",)

from kivy.lang import Builder
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivymd.uix.button import MDIconButton
from kivymd.uix.list import (
    IRightBodyTouch,
    OneLineAvatarIconListItem,
    ILeftBody,
)

Builder.load_string(
    """
<ExpansionPanel>
    text: root.title
    _no_ripple_effect: True

    AvatarLeft:
        source: root.icon

    ChevronRight:
        id: chevron
        icon: 'chevron-right'
        disabled: True

        canvas.before:
            PushMatrix
            Rotate:
                angle: self.angle
                axis: (0, 0, 1)
                origin: self.center
        canvas.after:
            PopMatrix


<MDExpansionPanel>
    size_hint_y: None
    height: dp(68)

    BoxLayout:
        id: box_item
        size_hint_y: None
        height: root.height
        orientation: 'vertical'

        ExpansionPanel:
            id: item_anim
            title: root.title
            icon: root.icon
            on_press: root.check_open_box(self)
"""
)


class MDExpansionPanel(BoxLayout):
    """
    :Events:
        :attr:`on_open`
            Called when a panel is opened.
        :attr:`on_close`
            Called when a panel is closed.
    """

    content = ObjectProperty()
    """Content of panel. Must be `Kivy` widget.

    :attr:`content` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    icon = StringProperty()
    """Icon of panel.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    title = StringProperty()
    """Title of panel.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")

    def on_open(self, *args):
        """Called when a panel is opened."""

    def on_close(self, *args):
        """Called when a panel is closed."""

    def check_open_box(self, instance):
        press_current_item = False
        for box in self.parent.children:
            if box.__class__ is MDExpansionPanel:
                if len(box.ids.box_item.children) == 2:
                    if instance is box.ids.item_anim:
                        press_current_item = True
                    box.ids.box_item.remove_widget(box.ids.box_item.children[0])
                    chevron = box.ids.box_item.children[0].ids.chevron
                    self.anim_chevron_up(chevron)
                    self.anim_resize_close(box)
                    self.dispatch("on_close")
                    break

        if not press_current_item:
            self.anim_chevron_down()

    def anim_chevron_down(self):
        chevron = self.ids.item_anim.ids.chevron
        angle = -90
        Animation(angle=angle, d=0.2).start(chevron)
        self.anim_resize_open_item()
        self.dispatch("on_open")

    def anim_chevron_up(self, instance):
        angle = 0
        Animation(angle=angle, d=0.2).start(instance)

    def anim_resize_close(self, box):
        Animation(height=dp(68), d=0.1, t="in_cubic").start(box)

    def anim_resize_open_item(self, *args):
        self.content.name_item = self.title
        anim = Animation(
            height=self.content.height + dp(70), d=0.2, t="in_cubic"
        )
        anim.bind(on_complete=self.add_content)
        anim.start(self)

    def add_content(self, *args):
        if self.content:
            self.ids.box_item.add_widget(self.content)


class AvatarLeft(ILeftBody, Image):
    pass


class ChevronRight(IRightBodyTouch, MDIconButton):
    angle = NumericProperty(0)


class ExpansionPanel(OneLineAvatarIconListItem):
    title = StringProperty()
    icon = StringProperty()
