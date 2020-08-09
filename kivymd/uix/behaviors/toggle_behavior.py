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
# from kivy.logger import Logger

from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty


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
    #THeming
    theme_cls = ObjectProperty()
    #
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
    __is_filled=BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        classinfo = ( MDRaisedButton,             MDFlatButton,               MDRectangleFlatButton,
                      MDRectangleFlatIconButton,  MDRoundFlatButton,          MDRoundFlatIconButton,
                      MDFillRoundFlatButton,      MDFillRoundFlatIconButton,
        )
        # Verify: Do The app class has theme_cls?
        app=MDApp.get_running_app()                                             # This saves some flops
        if not hasattr(app,"theme_cls"):
            raise ValueError(                                                   # If the app doesn't has the theme_cls, it will raise a ValueError exception with message
                "KivyMD: App object must be inherited from "
                "`kivymd.app.MDApp`. See "
                "https://github.com/kivymd/KivyMD/blob/master/README.md#api-breaking-changes"
            )
        # Verify: Do The object inherited from the "supported" Buttons?
        if not issubclass(self.__class__, classinfo):
            raise ValueError(f"Class {self.__class__} must be inherited from one of the classes in the list {classinfo}")
        else:
            self.theme_cls = app.theme_cls
        # Verify; If no background_normal is setted. then:
        if not self.background_normal:                                          # this means that if the value == [] or None will return True
            # Verify: If the object inherits from buttons with backgroud:
            if isinstance(self,(MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton)):
                self.__is_filled = True
                self.background_normal = self.theme_cls.primary_color
            # if not the background_normal must be the same as the inherited one:
            else:
                self.background_normal = self.md_bg_color[:]
        # Verify; If no background_down is setted. then:
        if not self.background_down:                                            # this means that if the value == [] or None will return True
            self.background_down = self.theme_cls.primary_dark                  # get the primary_color dark from themecls
        # self.bind(state=self._update_bg)                                      # Alternative to bind the function to the property
        self.fbind("state", self._update_bg)
    #
    def _update_bg(self, ins, val):
        # """
        # This function Updates the color of the backgroud
        # """
        if val == "down":
            self.md_bg_color = self.background_down
            if self.__is_filled == False:                                       # if the background is transparent, and the button it toggled, the font color must be withe [1,1,1,1]
                self.text_color = [1,1,1,1]
                # self.update_md_bg_color(self, [1,1,1,1])
            if self.group:
                self._release_group(self)
        else:
            self.md_bg_color = self.background_normal
            if self.__is_filled == False:                                       # if the background is transparent, the font color must be the primary color
                self.text_color = self.theme_cls._get_primary_color()
                # self.update_md_bg_color(self, self.theme_cls._get_primary_color())


# TEST APP
# this test app shows every type of button supported by MDToggleButton
# every row is a different group
# the cols var allows you to increase or decrease the ammount of elements in screen
# to see the changes between the installed module and this one, unmart the import bellows

if __name__ == '__main__':
    from kivy.lang import Builder
    from kivymd.app import MDApp

    # from kivymd.uix.behaviors.toggle_behavior import MDToggleButton # if this import is active, it will override the MDToggleButton of this file

    KV="""
MDGridLayout:
    # cols:3
    # id:container
        """
    # This code block is teh same for every button class supported.
    class MDToggleRaisedButton( MDRaisedButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleFlatButton( MDFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleRectangleFlatButton( MDRectangleFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleRectangleFlatIconButton( MDRectangleFlatIconButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleRoundFlatButton( MDRoundFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleRoundFlatIconButton( MDRoundFlatIconButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleFillRoundFlatButton( MDFillRoundFlatButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    class MDToggleFillRoundFlatIconButton( MDFillRoundFlatIconButton, MDToggleButton):
        def __init__(self, **kwargs):
            self.background_down = MDApp.get_running_app().theme_cls.primary_light
            super().__init__(**kwargs)
    #
    # This is the TEST app class
    class Test(MDApp):
        def build(self):
            cols=5                                                              # Change this value to increase or decrease the elements in the gird
            x=Builder.load_string(KV)
            x.cols=cols
            lista=[
                    MDToggleRaisedButton,           MDToggleFlatButton,
                    MDToggleRectangleFlatButton,    MDToggleRectangleFlatIconButton,
                    MDToggleRoundFlatButton,        MDToggleRoundFlatIconButton,
                    MDToggleFillRoundFlatButton,    MDToggleFillRoundFlatIconButton,
            ]
            for n,i in enumerate(lista):
                for ii in range(cols):
                    # x.ids.container.add_widget(i(text=f"element {ii}",group=str(n)))
                    x.add_widget(
                        i(                                                      # I is the custom toggle button class from the lista list
                            text  = f"element {ii}",
                            group = str(n)
                        )
                    )
            return x



    Test().run()
