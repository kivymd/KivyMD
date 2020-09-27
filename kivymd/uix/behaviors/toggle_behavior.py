"""
Behaviors/ToggleButton
======================

This behavior must always be inherited after the button's Widget class since it
works with the inherited properties of the button class.

it will also require to excecute the button's __after_init__ function.
since it's the base for the property management.

example:

.. code-block:: python

    class MyToggleButtonWidget(MDFlatButton, MDToggleButton):
        # [...]
        pass


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
            super().__init__(**kwargs)
            self.background_down = self.theme_cls.primary_light


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

from kivy.logger import Logger
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    ListProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ToggleButtonBehavior

from kivymd.uix.button import (
    BaseButton,
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDFlatButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRectangleFlatIconButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
    icon_behavior,
)


class MDToggleButton(BaseButton, ToggleButtonBehavior):
    background_normal = ListProperty(None, allownone=False)
    """
    Background button's Color in ``rgba`` format applied then the button state
    is `'normal'`.

    :attr:`background_normal` is a :class:`~kivy.properties.ListProperty`
    and is defaults to `None` and it doesn't allow None after being set.

    This property will only take effect if theme button color is set to cutom.

    """

    background_down = ListProperty(None, allownone=False)
    """
    Background button's Color in ``rgba`` format applied then the button state
    is `'down'`.

    :attr:`background_down` is a :class:`~kivy.properties.ListProperty`
    and is defaults to `None` and it doesn't allow None after being set.

    This property will only take effect if theme button color is set to cutom.

    """
    theme_background_normal = OptionProperty(
        None,
        options=["Primary", "Accent", "Custom", "Error"],
    )
    """
    This property will be set to the icon when the state of the togglebutton's
    `state` is set to `"normal"` (`active` is `False`).

    :attr:`theme_color_normal` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you don't set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will be settled to "Primary"
    """

    theme_background_down = OptionProperty(
        None,
        options=["Primary", "Accent", "Custom", "Error"],
    )
    """
    This property will be set to the icon when the state of the togglebutton's
    `state` is set to `"down"` (`active` is `True`).

    :attr:`theme_color_normal` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you don't set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will be settled to "Primary"
    """

    # New properties.
    color_normal = ListProperty(None, allownone=False)
    """
    This property sets the text color when the button is not pressed.
    it only works when the `theme_color_normal` is set to `"Custom"`.

    :attr:`color_normal` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will make the class to change `theme_color_normal` to
        `"Custom"`.

    after the new instance is created this property won't affect
    `theme_color_normal` property.
    """

    theme_color_normal = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )
    """
    This property will be set to the icon when the state of the ToggleButton's
    `state` is set to `"normal"` (`active` is `False`).

    :attr:`theme_color_normal` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you don't set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will be settled to "Primary"

    """

    color_down = ListProperty(None, allownone=False)
    """
    This property sets the text color when the button is pressed.
    it only works when the `theme_color_down` is set to `"Custom"`.

    :attr:`color_down` is a :class:`~kivy.properties.ListProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will make the class to change `theme_color_down` to
        `"Custom"`.

        after the new instance is created this property won't affect
        `theme_color_down` property.
    """

    theme_color_down = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )
    """
    This property will be set to the icon when the state of the ToggleButton's
    `state` is set to `"down"` (`active` is `True`).

    :attr:`theme_color_down` is a :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.

    .. note:: Special Behavior on new instances.
        If you don't set this property inside a widget definition in kvlang or as a kwarg
        in python code, it will be settled to "Primary_color"

    """

    text_color_normal = ListProperty()
    """
    Color of the font's button in ``rgba`` format for the 'normal' state.

    :attr:`text_color_normal` is a :class:`~kivy.properties.ListProperty`
    and is defaults to `[]`.
    """

    text_color_down = ListProperty([1, 1, 1, 1])
    """
    Color of the font's button in ``rgba`` format for the 'down' state.

    :attr:`text_color_down` is a :class:`~kivy.properties.ListProperty`
    and is defaults to `[1, 1, 1, 1]`.
    """
    theme_text_color_normal = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )

    theme_text_color_down = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
        ],
    )

    text_normal = StringProperty(None)
    """
    Text displayed when the button's state is `"normal"`.

    if this property is not set, there will be no change.
    """

    text_down = StringProperty(None)
    """
    Text displayed when the button's state is `"down"`.

    if this property is not set, there will be no change.
    """
    __change_text = BooleanProperty(False)
    # internal property, if there's a different text when on state,
    # this oprtion will be True, thus updating the text depending on state

    icon_normal = StringProperty(None)
    """
    icon displayed when the button's state is `"normal"`
    if the icon is not set, there will be no change.

    """

    theme_icon_color_normal = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
            "Text",
        ],
    )
    """
    This property will be applied once the state is normal
    and self._has_icon is True
    """

    icon_down = StringProperty(None)
    """
    icon displayed when the button's state is `"down"`
    if the icon is not set, there will be no change.

    """
    theme_icon_color_down = OptionProperty(
        None,
        options=[
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "Custom",
            "ContrastParentBackground",
            "Primary_color",
            "Accent_color",
            "White",
            "Text",
        ],
    )
    """
    This property will be applied once the state is down
    and self._has_icon is True
    """
    __change_icon = BooleanProperty(False)

    animate = BooleanProperty(None)
    # internal property, if there's a different text when on state,
    # this oprtion will be True, thus updating the text depending on state

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
            icon_behavior,
        )
        # Do the object inherited from the "supported" buttons?
        if not issubclass(self.__class__, classinfo):
            raise ValueError(
                f"Class {self.__class__} must be inherited from one of the classes in the list {classinfo}"
            )
        # Clock.schedule_once(self.toggle_config, 0)

    def __after_init__(self, *dt):
        # execute button __after_init__
        Logger.debug("I exists!!!")
        Logger.debug(f"self.type = {self.__class__}!!!\n\n")
        # text color state
        if self._has_text is True:
            if self.text is not None and self.text_normal is None:
                self.text_normal = self.text
            if self.text_down is None and self.text_normal is not None:
                self.text_down = "Selected"
            # Text Color Behavior
            if self.text_color not in [None, []]:
                self.theme_text_color_normal = "Custom"
                self.text_color_normal = self.text_color
            else:
                self.theme_text_color_normal = "Primary_color"
                self.theme_text_color = "Primary_color"
            # Text Theme behavior
            if (
                self.theme_text_color is not None
                and self.theme_text_color_normal is None
            ):
                self.theme_text_color_normal = self.theme_text_color
            if (
                self.theme_text_color_down is None
                and self.theme_text_color_normal is not None
            ):
                self.theme_text_color_down = self.theme_text_color_normal
        # icon color state
        if self._has_icon is True:
            # Animation behavior
            if self.animate is None:
                self.animate = True
            # Selected Icon
            if self.icon is not None and self.icon_normal is None:
                self.icon_normal = self.icon
            if self.icon_down is None and self.icon_normal is not None:
                self.icon_down = (
                    "checkbox-marked-circle-outline"
                    if self.group
                    else "checkbox-marked-outline"
                )
            # Icon Theme behavior
            if self.theme_icon_color_normal is None:
                if self.theme_icon_color is not None:
                    self.theme_icon_color_normal = self.theme_icon_color
                else:
                    if self._has_text:
                        self.theme_icon_color_normal = "Text"
                        self.theme_icon_color_down = "Text"
                pass
            if self.theme_icon_color_down is None:
                if self.theme_icon_color_normal is not None:
                    self.theme_icon_color_down = self.theme_icon_color_normal
                pass
        # Background color state
        if self._is_filled:
            if self.background_normal is not None:
                self.theme_background_normal = "Custom"
            else:
                if self.md_bg_color != [None, None, None, None]:
                    self.background_normal = self.md_bg_color
                    self.theme_background_normal = "Custom"

            if self.theme_background_normal is None:
                if self.theme_button_color is not None:
                    self.theme_background_normal = self.theme_button_color
                else:
                    self.theme_background_normal = "Primary"
            #
            if self.theme_background_down is None:
                self.theme_background_down = "Accent"
        #
        super().__after_init__(*dt)
        self.memview()
        self.bind(
            state=self.update_state,
            #
            icon_normal=self.update_state,
            icon_down=self.update_state,
            #
            text_normal=self.update_state,
            text_down=self.update_state,
            #
            theme_text_color_normal=self.toggle_theme,
            theme_text_color_down=self.toggle_theme,
            #
            background_down=self.toggle_theme,
            theme_background_normal=self.toggle_theme,
            #
            color_down=self.toggle_theme,
            color_normal=self.toggle_theme,
            #
        )
        # complement
        self.bind(
            state=self.toggle_theme,
        )
        self.update_state(skip=True)
        self.toggle_theme()

    def memview(self, *dt):
        Logger.debug(
            "__after_init__:\n"
            f"{self.__class__}\n"
            "\nSETTINGS: \n"
            f"\t _has_icon = {self._has_icon} \n"
            f"\t _is_filled = {self._is_filled} \n"
            f"\t _has_text = {self._has_text} \n"
            "\nCHANGING PROPERTIES : ICON \n"
            f"\t icon_normal = {self.icon_normal} \n"
            f"\t icon_down = {self.icon_down} \n"
            "\nCHANGING PROPERTIES : TEXT \n"
            f"\t text_normal = {self.text_normal} \n"
            f"\t text_down = {self.text_down} \n"
            "\n"
            "\nCOLORS - BACKGROUND \n"
            f"\t background_normal = {self.background_normal} \n"
            f"\t background_down = {self.background_down} \n"
            "\nTHEMING - BACKGROUND \n"
            f"\t theme_background_normal = {self.theme_background_normal} \n"
            f"\t theme_background_down = {self.theme_background_down} \n"
            "\nTHEMING - TEXT \n"
            f"\t theme_text_color_normal = {self.theme_text_color_normal} \n"
            f"\t theme_text_color_down = {self.theme_text_color_down} \n"
            "COMMON BUTTON SETTINGS \n"
            f"\t _md_bg_color = {self.md_bg_color} \n"
            f"\t text_color = {self.text_color} \n"
            f"\t icon_color = {self.icon_color} \n"
            "\nTHEMES \n"
            f"\t theme_button_color = {self.theme_button_color} \n"
            f"\t theme_text_color = {self.theme_text_color} \n"
            f"\t theme_icon_color = {self.theme_icon_color} \n"
            "\n"
        )

    def toggle_theme(self, *dt):
        """
        This function is in charge to update the colors and themes of the
        displayed MDIcon.
        """
        if self.state == "down":
            # Background theme
            if self._is_filled is True:
                self.theme_button_color = self.theme_background_down
                # only for custom background colors
                if self.theme_color_down == "Custom":
                    self.md_bg_color = self.color_down

            # Text
            if self._has_text:
                self.theme_text_color = self.theme_text_color_down
                if self.theme_text_color_down == "Custom":
                    self.text_color = self.text_color_down
                # changing content
                if self.text_down is not None:
                    self.text = self.text_down
            # icon
            if self._has_icon:
                self.theme_icon_color = self.theme_icon_color_down
                if self.icon_down is not None:
                    self.icon = self.icon_down
        else:
            # Background theme
            if self._is_filled is True:
                self.theme_button_color = self.theme_background_normal
                # only for custom background colors
                if self.theme_color_normal == "Custom":
                    self.md_bg_color = self.color_normal

            # Text
            if self._has_text:
                self.theme_text_color = self.theme_text_color_normal
                if self.theme_text_color_normal == "Custom":
                    self.text_color = self.text_color_normal
                # changing content
                if self.text_normal is not None:
                    self.text = self.text_normal
            # icon
            if self._has_icon:
                self.theme_icon_color = self.theme_icon_color_normal
                if self.icon_normal is not None:
                    self.icon = self.icon_normal

    def on_group(self, instance, value):
        """
        This function ensures that the toggle button group updates every time a
        button group is pressed.

        it also ensures that the icon shown inside the button is the correct
        type.
        """
        super().on_group(instance, value)
        self.update_state()

    # @property
    def get_active(self):
        return True if self.state == "down" else False

    # @active.setter
    def set_active(self, value):
        if value is True:
            self.state = "down"
        elif value is False:
            self.state = "normal"
        else:
            raise ValueError(f"Active is a bool property, got {type(value)}")
        return True

    active = AliasProperty(get_active, set_active, bind=["state"], cache=True)
    """
    Indicates if the checkbox is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.AliasProperty` that acts as a
    common BooleanProperty and by default is set to `False` .
    it uses get_active as a getter and set_active as a setter.
    its binded to the ToggleButtonBehavior.state and it's cached.
    """

    def update_state(self, *dt, skip=False):
        """
        This funciton is in charge of updating the icon when it's needed.
        it will force the update of the icon to the respective behavior
        either be as a group icon or as a selection icon.
        """
        # if we have a theme
        if isinstance(self, icon_behavior) and self._has_icon is True:
            if (
                hasattr(self, "zoom_in_animation")
                and self.animate is True
                and skip is False
            ):
                self.zoom_in_animation(
                    next_icon=self.icon_down
                    if self.state == "down"
                    else self.icon_normal
                )
            else:
                self.next_icon = (
                    self.icon_down if self.state == "down" else self.icon_normal
                )
        if self._has_text is True:
            if self.text_normal and self.text_down:
                self.text = (
                    self.text_down if self.state == "down" else self.text_normal
                )
