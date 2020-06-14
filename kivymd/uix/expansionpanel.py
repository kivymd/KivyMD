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

.. code-block:: python

    self.add_widget(
        MDExpansionPanel(
            icon="logo.png",  # panel icon
            content=Content(),  # panel content
            panel_cls=MDExpansionPanelOneLine(text="Secondary text"),  # panel class
        )
    )

To use :class:`~MDExpansionPanel` you must pass one of the following classes
to the :attr:`~MDExpansionPanel.panel_cls` parameter:

- :class:`~MDExpansionPanelOneLine`
- :class:`~MDExpansionPanelTwoLine`
- :class:`~MDExpansionPanelThreeLine`

These classes are inherited from the following classes:

- :class:`~kivymd.uix.list.OneLineAvatarIconListItem`
- :class:`~kivymd.uix.list.TwoLineAvatarIconListItem`
- :class:`~kivymd.uix.list.ThreeLineAvatarIconListItem`

.. code-block:: python

    self.root.ids.box.add_widget(
        MDExpansionPanel(
            icon="logo.png",
            content=Content(),
            panel_cls=MDExpansionPanelThreeLine(
                text="Text",
                secondary_text="Secondary text",
                tertiary_text="Tertiary text",
            )
        )
    )

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
    from kivymd import images_path

    KV = '''
    <Content>
        adaptive_height: True

        TwoLineIconListItem:
            text: "(050)-123-45-67"
            secondary_text: "Mobile"

            IconLeftWidget:
                icon: 'phone'


    ScrollView:

        MDGridLayout:
            id: box
            cols: 1
            adaptive_height: True
    '''


    class Content(MDBoxLayout):
        '''Custom content.'''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(10):
                self.root.ids.box.add_widget(
                    MDExpansionPanel(
                        icon=f"{images_path}kivymd_logo.png",
                        content=Content(),
                        panel_cls=MDExpansionPanelThreeLine(
                            text="Text",
                            secondary_text="Secondary text",
                            tertiary_text="Tertiary text",
                        )
                    )
                )


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.gif
    :align: center

Two events are available for :class:`~MDExpansionPanel`
------------------------------------------------------

- :attr:`~MDExpansionPanel.on_open`
- :attr:`~MDExpansionPanel.on_close`

.. code-block:: kv

        MDExpansionPanel:
            on_open: app.on_panel_open(args)
            on_close: app.on_panel_close(args)

The user function takes one argument - the object of the panel:

.. code-block:: python

    def on_panel_open(self, instance_panel):
        print(instance_panel)

.. seealso:: `See Expansion panel example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Expansion-Panel>`_

    `Expansion panel and MDCard <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Expansion-Panel-and-MDCard>`_
"""

__all__ = (
    "MDExpansionPanel",
    "MDExpansionPanelOneLine",
    "MDExpansionPanelTwoLine",
    "MDExpansionPanelThreeLine",
)

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import WidgetException

from kivymd.uix.button import MDIconButton
from kivymd.uix.list import (
    ImageLeftWidget,
    IRightBodyTouch,
    OneLineAvatarIconListItem,
    ThreeLineAvatarIconListItem,
    TwoLineAvatarIconListItem,
)

Builder.load_string(
    """
<MDExpansionChevronRight>:
    icon: 'chevron-right'
    disabled: True

    canvas.before:
        PushMatrix
        Rotate:
            angle: self._angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix


<MDExpansionPanel>
    size_hint_y: None
    #height: dp(68)
"""
)


class MDExpansionChevronRight(IRightBodyTouch, MDIconButton):
    """Chevron icon on the right panel."""

    _angle = NumericProperty(0)


class MDExpansionPanelOneLine(OneLineAvatarIconListItem):
    """Single line panel."""


class MDExpansionPanelTwoLine(TwoLineAvatarIconListItem):
    """Two-line panel."""


class MDExpansionPanelThreeLine(ThreeLineAvatarIconListItem):
    """Three-line panel."""


class MDExpansionPanel(RelativeLayout):
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

    opening_transition = StringProperty("out_cubic")
    """
    The name of the animation transition type to use when animating to
    the :attr:`state` `'open'`.

    :attr:`opening_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_cubic'`.
    """

    opening_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'open'`.

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    closing_transition = StringProperty("out_sine")
    """The name of the animation transition type to use when animating to
    the :attr:`state` 'close'.

    :attr:`closing_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_sine'`.
    """

    closing_time = NumericProperty(0.2)
    """
    The time taken for the panel to slide to the :attr:`state` `'close'`.

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    panel_cls = ObjectProperty()
    """
    Panel object. The object must be one of the classes
    :class:`~MDExpansionPanelOneLine`, :class:`~MDExpansionPanelTwoLine` or
    :class:`~MDExpansionPanelThreeLine`.

    :attr:`panel_cls` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")

        if self.panel_cls and isinstance(
            self.panel_cls,
            (
                MDExpansionPanelOneLine,
                MDExpansionPanelTwoLine,
                MDExpansionPanelThreeLine,
            ),
        ):
            self.panel_cls.pos_hint = {"top": 1}
            self.panel_cls._no_ripple_effect = True
            self.panel_cls.bind(
                on_release=lambda x: self.check_open_panel(self.panel_cls)
            )
            self.chevron = MDExpansionChevronRight()
            self.panel_cls.add_widget(self.chevron)
            self.panel_cls.add_widget(ImageLeftWidget(source=self.icon))
            self.add_widget(self.panel_cls)
        else:
            raise ValueError(
                "KivyMD: `panel_cls` object must be must be one of the "
                "objects from the list\n"
                "[MDExpansionPanelOneLine, MDExpansionPanelTwoLine, "
                "MDExpansionPanelThreeLine]"
            )

    def on_open(self, *args):
        """Called when a panel is opened."""

    def on_close(self, *args):
        """Called when a panel is closed."""

    def check_open_panel(self, instance):
        """
        Called when you click on the panel. Called methods to open or close
        a panel.
        """

        press_current_panel = False
        for panel in self.parent.children:
            if isinstance(panel, MDExpansionPanel):
                if len(panel.children) == 2:
                    if instance is panel.children[1]:
                        press_current_panel = True
                    panel.remove_widget(panel.children[0])
                    chevron = panel.children[0].children[0].children[0]
                    self.set_chevron_up(chevron)
                    self.close_panel(panel)
                    self.dispatch("on_close")
                    break
        if not press_current_panel:
            self.set_chevron_down()

    def set_chevron_down(self):
        """Sets the chevron down."""

        Animation(_angle=-90, d=self.opening_time).start(self.chevron)
        self.open_panel()
        self.dispatch("on_open")

    def set_chevron_up(self, instance_chevron):
        """Sets the chevron up."""

        Animation(_angle=0, d=self.closing_time).start(instance_chevron)

    def close_panel(self, instance_panel):
        """Method closes the panel."""

        Animation(
            height=self.panel_cls.height,
            d=self.closing_time,
            t=self.closing_transition,
        ).start(instance_panel)

    def open_panel(self, *args):
        """Method opens a panel."""

        anim = Animation(
            height=self.content.height + self.height,
            d=self.opening_time,
            t=self.opening_transition,
        )
        anim.bind(on_complete=self._add_content)
        anim.start(self)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(
            widget,
            (
                MDExpansionPanelOneLine,
                MDExpansionPanelTwoLine,
                MDExpansionPanelThreeLine,
            ),
        ):
            self.height = widget.height
        return super().add_widget(widget)

    def _add_content(self, *args):
        if self.content:
            try:
                self.add_widget(self.content)
            except WidgetException:
                pass
