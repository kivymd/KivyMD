"""
Behaviors/Focus
===============

.. rubric:: Changing the background color when the mouse is on the widget.

To apply focus behavior, you must create a new class that is inherited from the
widget to which you apply the behavior and from the :class:`FocusBehavior` class.

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    MDScreen:
        md_bg_color: 1, 1, 1, 1

        FocusWidget:
            size_hint: .5, .3
            pos_hint: {"center_x": .5, "center_y": .5}
            md_bg_color: app.theme_cls.bg_light

            MDLabel:
                text: "Label"
                theme_text_color: "Primary"
                pos_hint: {"center_y": .5}
                halign: "center"
    '''


    class FocusWidget(MDBoxLayout, RectangularElevationBehavior, FocusBehavior):
        pass


    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/focus-widget.gif
    :align: center

Color change at focus/defocus

.. code-block:: kv

    FocusWidget:
        focus_color: 1, 0, 1, 1
        unfocus_color: 0, 0, 1, 1

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/focus-defocus-color.gif
    :align: center
"""

__all__ = ("FocusBehavior",)

from kivy.app import App
from kivy.properties import BooleanProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd.uix.behaviors import HoverBehavior


class FocusBehavior(HoverBehavior, ButtonBehavior):

    focus_behavior = BooleanProperty(True)
    """
    Using focus when hovering over a widget.

    :attr:`focus_behavior` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    focus_color = ListProperty()
    """
    The color of the widget when the mouse enters the bbox of the widget.

    :attr:`focus_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    unfocus_color = ListProperty()
    """
    The color of the widget when the mouse exits the bbox widget.

    :attr:`unfocus_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    def on_enter(self):
        """Fired when mouse enter the bbox of the widget."""

        if hasattr(self, "md_bg_color") and self.focus_behavior:
            if hasattr(self, "theme_cls") and not self.focus_color:
                self.md_bg_color = self.theme_cls.bg_normal
            else:
                if not self.focus_color:
                    self.md_bg_color = App.get_running_app().theme_cls.bg_normal
                else:
                    self.md_bg_color = self.focus_color

    def on_leave(self):
        """Fired when the mouse exit the widget."""

        if hasattr(self, "md_bg_color") and self.focus_behavior:
            if hasattr(self, "theme_cls") and not self.unfocus_color:
                self.md_bg_color = self.theme_cls.bg_light
            else:
                if not self.unfocus_color:
                    self.md_bg_color = App.get_running_app().theme_cls.bg_light
                else:
                    self.md_bg_color = self.unfocus_color
