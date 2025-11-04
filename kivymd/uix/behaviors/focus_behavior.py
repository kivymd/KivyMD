"""
Behaviors/Focus
===============

.. rubric:: Changing the background color when the mouse is on the widget.

To apply focus behavior, you must create a new class that is inherited from the
widget to which you apply the behavior and from the :class:`StateFocusBehavior` class.

Usage
-----

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.behaviors.focus_behavior import StateFocusBehavior

            KV = '''
            MDScreen:
                md_bg_color: app.theme_cls.backgroundColor

                FocusWidget:
                    size_hint: .5, .3
                    pos_hint: {"center_x": .5, "center_y": .5}
                    md_bg_color: self.theme_cls.surfaceContainerHighestColor

                    MDLabel:
                        text: "Label"
                        pos_hint: {"center_y": .5}
                        halign: "center"
            '''


            class FocusWidget(MDBoxLayout, CommonElevationBehavior, StateFocusBehavior):
                def on_enter(self):
                    '''Fired when mouse enter the bbox of the widget.'''

                    self.md_bg_color = self.theme_cls.surfaceVariantColor

                def on_leave(self):
                    '''Fired when the mouse goes outside the widget border.'''

                    self.md_bg_color = self.theme_cls.surfaceContainerHighestColor


            class Exmple(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            Exmple().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CommonElevationBehavior
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.behaviors.focus_behavior import StateFocusBehavior
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class FocusWidget(MDBoxLayout, CommonElevationBehavior, StateFocusBehavior):
                def on_enter(self):
                    '''Fired when mouse enter the bbox of the widget.'''

                    self.md_bg_color = self.theme_cls.surfaceVariantColor

                def on_leave(self):
                    '''Fired when the mouse goes outside the widget border.'''

                    self.md_bg_color = self.theme_cls.surfaceContainerHighestColor


            class Exmple(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return (
                        MDScreen(
                            FocusWidget(
                                MDLabel(
                                    text="Label",
                                    pos_hint={"center_y": .5},
                                    halign="center",
                                ),
                                size_hint=(.5, .3),
                                pos_hint={"center_x": .5, "center_y": .5},
                                md_bg_color=self.theme_cls.surfaceContainerHighestColor,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor,
                        )
                    )


            Exmple().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/focus-widget.gif
    :align: center

Color change at focus/defocus

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: kv

            FocusWidget:
                focus_color: 1, 0, 1, 1
                unfocus_color: 0, 0, 1, 1

    .. tab:: Declarative Python style

        .. code-block:: python

            FocusWidget(
                focus_color=[1, 0, 1, 1],
                unfocus_color=[0, 0, 1, 1],
            )

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/focus-defocus-color.gif
    :align: center
"""

__all__ = ("FocusBehavior", "StateFocusBehavior")

from kivy import Logger
from kivy.properties import BooleanProperty, ColorProperty

from kivymd.uix.behaviors import HoverBehavior


class StateFocusBehavior(HoverBehavior):
    """
    Focus behavior class.

    :Events:
        :attr:`on_enter`
            Fired when mouse enters the bbox of the widget AND the widget is
            visible.
        :attr:`on_leave`
            Fired when the mouse exits the widget AND the widget is visible.

    For more information, see in the
    :class:`~kivymd.uix.behavior.HoverBehavior` class documentation.

    .. versionadded:: 2.0.0
    """

    focus_behavior = BooleanProperty(True)
    """
    Using focus when hovering over a widget.

    :attr:`focus_behavior` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    focus_color = ColorProperty(None)
    """
    The color of the widget when the mouse enters the bbox of the widget.

    :attr:`focus_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    unfocus_color = ColorProperty(None)
    """
    The color of the widget when the mouse exits the bbox widget.

    :attr:`unfocus_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """


class FocusBehavior(StateFocusBehavior):
    """
    Focus behavior class.

    For more information, see in the
    :class:`~kivymd.uix.behavior.focus_behavior.StateFocusBehavior`
    class documentation.

    .. deprecated:: 2.0.0
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Logger.warning(
            "KivyMD: "
            "The `FocusBehavior` class is deprecated. It is recommended to "
            "use `StateFocusBehavior` instead of `FocusBehavior`."
        )
