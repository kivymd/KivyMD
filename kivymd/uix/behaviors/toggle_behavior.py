"""
Behaviors/ToggleButton
======================

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
    from kivymd.uix.button import MDRectangleFlatButton

    KV = '''
    Screen:

        MDBoxLayout:
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .5}

            MyToggleButton:
                text: "Show ads"
                group: "x"

            MyToggleButton:
                text: "Do not show ads"
                group: "x"

            MyToggleButton:
                text: "Does not matter"
                group: "x"
    '''


    class MyToggleButton(MDRectangleFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toggle-button-1.gif
    :align: center

.. code-block:: python

    class MyToggleButton(MDFillRoundFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.primary_dark
        super().__init__(**kwargs)

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/toggle-button-2.gif
    :align: center

You can inherit the ``MyToggleButton`` class only from the following classes
----------------------------------------------------------------------------

- :class:`~kivymd.uix.button.MDRaisedButton`
- :class:`~kivymd.uix.button.MDFlatButton`
- :class:`~kivymd.uix.button.MDRectangleFlatButton`
- :class:`~kivymd.uix.button.MDRectangleFlatIconButton`
- :class:`~kivymd.uix.button.MDRoundFlatButton`
- :class:`~kivymd.uix.button.MDRoundFlatIconButton`
- :class:`~kivymd.uix.button.MDFillRoundFlatButton`
- :class:`~kivymd.uix.button.MDFillRoundFlatIconButton`
"""

__all__ = ("MDToggleButton",)

from kivy.properties import ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior

from kivymd.app import MDApp
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDFlatButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRectangleFlatIconButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
)


class MDToggleButton(ToggleButtonBehavior):
    background_normal = ListProperty()
    """
    Color of the button in the ``rgba`` format in the 'normal' state.

    :attr:`background_normal` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    background_down = ListProperty()
    """
    Color of the button in the ``rgba`` format in the 'down' state.

    :attr:`background_down` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        classinfo = (
            MDRaisedButton,
            MDFlatButton,
            MDRectangleFlatButton,
            MDRectangleFlatIconButton,
            MDRoundFlatButton,
            MDRoundFlatIconButton,
            MDFillRoundFlatButton,
            MDFillRoundFlatIconButton,
        )
        if not issubclass(self.__class__, classinfo):
            raise ValueError(
                f"Class {self.__class__} must be inherited from one of the classes in the list {classinfo}"
            )
        if not self.background_normal:
            self.background_normal = (
                MDApp.get_running_app().theme_cls.primary_color
            )
        if not self.background_down:
            self.background_down = (
                MDApp.get_running_app().theme_cls.primary_dark
            )

    def on_release(self):
        for button in self.get_widgets(self.group):
            if button.state == "down":
                button.md_bg_color = self.background_down
            else:
                if isinstance(button, MDFlatButton):
                    background_normal = (0, 0, 0, 0)
                else:
                    background_normal = self.background_normal
                button.md_bg_color = background_normal
