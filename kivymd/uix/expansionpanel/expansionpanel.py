"""
Components/ExpansionPanel
=========================

.. rubric:: Expansion panels contain creation flows and allow lightweight editing of an element.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel.png
    :align: center

Usage
-----

.. code-block:: python

    MDExpansionPanel:

        MDExpansionPanelHeader:

            # Content of header.
            [...]

        MDExpansionPanelContent:

            # Content of panel.
            [...]

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel-anatomy.png
    :align: center

Example
-------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import RotateBehavior
    from kivymd.uix.expansionpanel import MDExpansionPanel
    from kivymd.uix.list import MDListItemTrailingIcon

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDExpansionPanel:
            id: panel
            pos_hint: {"center_x": .5, "center_y": .5}

            MDExpansionPanelHeader:

                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowColor
                    ripple_effect: False

                    MDListItemSupportingText:
                        text: "Supporting text"

                    TrailingPressedIconButton:
                        id: chevron
                        icon: "chevron-right"
                        on_release: app.tap_expansion_chevron(panel, chevron)

            MDExpansionPanelContent:
                orientation: "vertical"
                padding: "12dp", 0, "12dp", 0

                MDLabel:
                    text: "Channel information"
                    adaptive_height: True
                    padding_x: "16dp"
                    padding_y: "12dp"

                MDListItem:

                    MDListItemLeadingIcon:
                        icon: "email"

                    MDListItemHeadlineText:
                        text: "Email"

                    MDListItemSupportingText:
                        text: "kivydevelopment@gmail.com"

                MDListItem:

                    MDListItemLeadingIcon:
                        icon: "instagram"

                    MDListItemHeadlineText:
                        text: "Instagram"

                    MDListItemSupportingText:
                        text: "Account"

                    MDListItemTertiaryText:
                        text: "www.instagram.com/KivyMD"
    '''


    class TrailingPressedIconButton(
        ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
    ):
        ...


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def tap_expansion_chevron(
            self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
        ):
            panel.open() if not panel.is_open else panel.close()
            panel.set_chevron_down(
                chevron
            ) if not panel.is_open else panel.set_chevron_up(chevron)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel-example.gif
    :align: center

Use with ScrollView
-------------------

.. code-block:: python

    import asynckivy
    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.metrics import dp
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import RotateBehavior
    from kivymd.uix.expansionpanel import MDExpansionPanel
    from kivymd.uix.list import MDListItemTrailingIcon

    KV = '''
    <ExpansionPanelItem>

        MDExpansionPanelHeader:

            MDListItem:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.surfaceContainerLowColor
                ripple_effect: False

                MDListItemSupportingText:
                    text: "Supporting text"

                TrailingPressedIconButton:
                    id: chevron
                    icon: "chevron-right"
                    on_release: app.tap_expansion_chevron(root, chevron)

        MDExpansionPanelContent:
            orientation: "vertical"
            padding: "12dp", 0, "12dp", "12dp"
            md_bg_color: self.theme_cls.surfaceContainerLowestColor

            MDLabel:
                text: "Channel information"
                adaptive_height: True
                padding_x: "16dp"
                padding_y: "12dp"

            MDListItem:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.surfaceContainerLowestColor

                MDListItemLeadingIcon:
                    icon: "email"

                MDListItemHeadlineText:
                    text: "Email"

                MDListItemSupportingText:
                    text: "kivydevelopment@gmail.com"

            MDListItem:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.surfaceContainerLowestColor

                MDListItemLeadingIcon:
                    icon: "instagram"

                MDListItemHeadlineText:
                    text: "Instagram"

                MDListItemSupportingText:
                    text: "Account"

                MDListItemTertiaryText:
                    text: "www.instagram.com/KivyMD"


    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        ScrollView:
            size_hint_x: .5
            pos_hint: {"center_x": .5, "center_y": .5}

            MDList:
                id: container
    '''


    class ExpansionPanelItem(MDExpansionPanel):
        ...


    class TrailingPressedIconButton(
        ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
    ):
        ...


    class Example(MDApp):
        def on_start(self):
            async def set_panel_list():
                for i in range(12):
                    await asynckivy.sleep(0)
                    self.root.ids.container.add_widget(ExpansionPanelItem())

            asynckivy.start(set_panel_list())

        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)

        def tap_expansion_chevron(
            self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
        ):
            Animation(
                padding=[0, dp(12), 0, dp(12)]
                if not panel.is_open
                else [0, 0, 0, 0],
                d=0.2,
            ).start(panel)
            panel.open() if not panel.is_open else panel.close()
            panel.set_chevron_down(
                chevron
            ) if not panel.is_open else panel.set_chevron_up(chevron)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/expansion-panel-example-with-scroll-view.gif
    :align: center

API break
=========

1.2.0 version
-------------

.. code-block:: python

    MDExpansionPanel(
        icon="icon.png",
        content=Content(),  # content of panel
        panel_cls=MDExpansionPanelThreeLine(  # content of header
            text="Text",
            secondary_text="Secondary text",
            tertiary_text="Tertiary text",
        )
    )

2.0.0 version
-------------

.. code-block:: python

    MDExpansionPanel:

        MDExpansionPanelHeader:

            # Content of header.
            [...]

        MDExpansionPanelContent:

            # Content of panel.
            [...]
"""

__all__ = (
    "MDExpansionPanel",
    "MDExpansionPanelContent",
    "MDExpansionPanelHeader",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    StringProperty,
    BooleanProperty,
)
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior

with open(
    os.path.join(uix_path, "expansionpanel", "expansionpanel.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDExpansionPanelContent(
    DeclarativeBehavior, ThemableBehavior, BackgroundColorBehavior, BoxLayout
):
    """
    Implements a container for panel content.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """


class MDExpansionPanelHeader(DeclarativeBehavior, BoxLayout):
    """
    Implements a container for the content of the panel header.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """


# TODO: Add a successor from kivymd.uix.behaviors.motion_behavior.MotionBase
#  to the MDExpansionPanel class to control the properties of the panel
#  opening/closing animation.
class MDExpansionPanel(DeclarativeBehavior, BoxLayout):
    """
    Expansion panel class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.

    :Events:
        :attr:`on_open`
            Fired when a panel is opened.
        :attr:`on_close`
            Fired when a panel is closed.
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
    """
    The name of the animation transition type to use when animating to
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

    is_open = BooleanProperty(False)
    """
    The panel is open or closed.

    .. versionadded:: 2.0.0

    :attr:`is_open` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    _header = ObjectProperty()  # MDExpansionPanelHeader object
    _content = ObjectProperty()  # MDExpansionPanelContent object
    # Height of the MDExpansionPanelContent widget.
    _original_content_height = NumericProperty()
    _allow_add_content = False
    _panel_is_process_opening = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_open")
        self.register_event_type("on_close")

    def on_open(self, *args) -> None:
        """Fired when a panel is opened."""

    def on_close(self, *args) -> None:
        """Fired when a panel is closed."""

    def set_chevron_down(self, instance) -> None:
        """Sets the chevron down."""

        Animation(rotate_value_angle=-90, d=self.opening_time).start(instance)

    def set_chevron_up(self, instance) -> None:
        """Sets the chevron up."""

        Animation(rotate_value_angle=0, d=self.closing_time).start(instance)

    def close(self, *args) -> None:
        """
        Method closes the panel.

        .. versionchanged:: 2.0.0

            Rename from `close_panel` to `close` method.
        """

        def set_content_height(*args):
            anim_height = Animation(
                height=0,
                t=self.opening_transition,
                d=self.opening_time,
            )
            anim_height.bind(
                on_complete=lambda *args: self.remove_widget(self._content)
            )
            anim_height.start(self._content)
            self.is_open = False
            self.dispatch("on_close")

        anim_opacity = Animation(
            opacity=0,
            t=self.opening_transition,
            d=self.opening_time,
        )
        anim_opacity.bind(on_complete=set_content_height)
        anim_opacity.start(self._content)

    def open(self, *args) -> None:
        """
        Method opens a panel.

        .. versionchanged:: 2.0.0

            Rename from `open_panel` to `open` method.
        """

        def set_content_opacity(*args):
            Animation(
                opacity=1,
                t=self.opening_transition,
                d=self.opening_time,
            ).start(self._content)
            self.is_open = True
            self._panel_is_process_opening = False
            self.dispatch("on_open")

        if not self._panel_is_process_opening:
            self._allow_add_content = True
            self._panel_is_process_opening = True
            self.add_widget(self._content)

            anim_height = Animation(
                height=self._original_content_height,
                t=self.opening_transition,
                d=self.opening_time,
            )
            anim_height.bind(on_complete=set_content_opacity)
            anim_height.start(self._content)

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDExpansionPanelHeader):
            self._header = widget
            return super().add_widget(widget)
        elif (
            isinstance(widget, MDExpansionPanelContent)
            and not self._allow_add_content
        ):
            self._content = widget
            Clock.schedule_once(self._set_content_height, 0.8)
        elif (
            isinstance(widget, MDExpansionPanelContent)
            and self._allow_add_content
        ):
            return super().add_widget(widget)

    def _set_content_height(self, *args):
        self._original_content_height = self._content.height - dp(88)
        self._content.height = 0
