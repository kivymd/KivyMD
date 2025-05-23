"""
Behaviors/Declarative
=====================

.. versionadded:: 1.0.0

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe
            src="https://www.youtube.com/embed/_kiaJacLz8o"
            frameborder="0"
            allowfullscreen
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
        </iframe>
    </div>

As you already know, the Kivy framework provides the best/simplest/modern
UI creation tool that allows you to separate the logic of your application
from the description of the properties of widgets/GUI components.
This tool is named `KV Language <https://kivy.org/doc/stable/guide/lang.html>`_.

But in addition to creating a user interface using the KV Language Kivy allows
you to create user interface elements directly in the Python code.
And if you've ever created a user interface in Python code, you know how ugly
it looks. Even in the simplest user interface design, which was created using
Python code it is impossible to trace the widget tree, because in Python code
you build the user interface in an imperative style.

Imperative style
----------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.navigationbar import (
        MDNavigationBar,
        MDNavigationItem,
        MDNavigationItemIcon,
        MDNavigationItemLabel,
    )
    from kivymd.uix.screen import MDScreen


    class Example(MDApp):
        def build(self):
            screen = MDScreen()
            bottom_navigation = MDNavigationBar()

            datas = [
                {"text": "Mail", "icon": "gmail"},
                {"text": "GitHub", "icon": "git"},
                {"text": "LinkedIN", "icon": "linkedin"},
            ]
            for data in datas:
                text = data["text"]
                navigation_item = MDNavigationItem(
                    MDNavigationItemIcon(
                        icon=data["icon"],
                    ),
                    MDNavigationItemLabel(
                        text=text,
                    ),
                )
                bottom_navigation.add_widget(navigation_item)

            screen.add_widget(bottom_navigation)
            return screen


    Example().run()

Take a look at the above code example. This is a very simple UI. But looking
at this code, you will not be able to figure the widget tree and understand
which UI this code implements. This is named imperative programming style,
which is used in Kivy.

Now let's see how the same code is implemented using the KV language,
which uses a declarative style of describing widget properties.

Declarative style with KV language
----------------------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp


    class Example(MDApp):
        def build(self):
            return Builder.load_string(
                '''
    MDScreen:

        MDNavigationBar:

            MDNavigationItem:

                MDNavigationItemIcon:
                    icon: "gmail"

                MDNavigationItemLabel:
                    text: "Mail"

            MDNavigationItem:

                MDNavigationItemIcon:
                    icon: "git"

                MDNavigationItemLabel:
                    text: "GitHub"

            MDNavigationItem:

                MDNavigationItemIcon:
                    icon: "linkedin"

                MDNavigationItemLabel:
                    text: "LinkedIN"
    '''
            )


    Example().run()

Looking at this code, we can now clearly see the widget tree and their properties.
We can quickly navigate through the components of the screen and quickly
change/add new properties/widgets. This is named declarative UI creation style.

But now the KivyMD library allows you to write Python code in a declarative style.
Just as it is implemented in Flutter/Jetpack Compose/SwiftUI.

Declarative style with Python code
----------------------------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.navigationbar import (
        MDNavigationBar,
        MDNavigationItemIcon,
        MDNavigationItem,
        MDNavigationItemLabel,
    )


    class Example(MDApp):
        def build(self):
            return MDNavigationBar(
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="gmail",
                    ),
                    MDNavigationItemLabel(
                        text="Mail",
                    ),
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="twitter",
                    ),
                    MDNavigationItemLabel(
                        text="Twitter",
                    ),
                ),
                MDNavigationItem(
                    MDNavigationItemIcon(
                        icon="linkedin",
                    ),
                    MDNavigationItemLabel(
                        text="LinkedIN",
                    ),
                ),
            )


    Example().run()

.. note:: The KivyMD library does not support creating Kivy widgets in Python
    code in a declarative style.

But you can still use the declarative style of creating Kivy widgets in Python code.
To do this, you need to create a new class that will be inherited from the Kivy
widget and the :class:`~DeclarativeBehavior` class:

.. code-block:: python

    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import DeclarativeBehavior


    class DeclarativeStyleBoxLayout(DeclarativeBehavior, BoxLayout):
        pass


    class Example(MDApp):
        def build(self):
            return (
                DeclarativeStyleBoxLayout(
                    Button(),
                    Button(),
                    orientation="vertical",
                )
            )


    Example().run()

Get objects by identifiers
--------------------------

In the declarative style in Python code, the ids parameter of the specified
widget will return only the id of the child widget/container, ignoring other ids.
Therefore, to get objects by identifiers in declarative style in Python code,
you must specify all the container ids in which the widget is nested until you
get to the desired id:

.. code-block::

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.button import MDButton, MDButtonText
    from kivymd.uix.floatlayout import MDFloatLayout


    class Example(MDApp):
        def build(self):
            return (
                MDBoxLayout(
                    MDFloatLayout(
                        MDButton(
                            MDButtonText(
                                text="Button 1",
                            ),
                            id="button_1",
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        id="box_container_1",
                    ),
                    MDBoxLayout(
                        MDFloatLayout(
                            MDButton(
                                MDButtonText(
                                    text="Button 2",
                                ),
                                id="button_2",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            ),
                            id="float_container",
                        ),
                        id="box_container_2",
                    )
                )
            )

        def on_start(self):
            # {
            #     'button_1': <kivymd.uix.button.button.MDButton object at 0x11d93c9e0>,
            #     'button_2': <kivymd.uix.button.button.MDButton object at 0x11da128f0>,
            #     'float_container': <kivymd.uix.floatlayout.MDFloatLayout object at 0x11da228f0>,
            #     'box_container_1': <kivymd.uix.floatlayout.MDFloatLayout object at 0x11d9fc3c0>,
            #     'box_container_2': <kivymd.uix.boxlayout.MDBoxLayout object at 0x11dbf06d0>,
            # }
            print(self.root.get_ids())


    Example().run()

Yes, this is not a very good solution, but I think it will be fixed soon.

.. warning:: Declarative programming style in Python code in the KivyMD library
    is an experimental feature. Therefore, if you receive errors, do not hesitate
    to create new issue in the KivyMD repository.
"""

from kivy.properties import StringProperty, ListProperty
from kivy.uix.widget import Widget


class _Dict(dict):
    """Implements access to dictionary values via a dot."""

    def __getattr__(self, name):
        return self[name]


# TODO: Add cleaning of the `__ids` collection when removing child widgets
#  from the parent.
class DeclarativeBehavior:
    """
    Implements the creation and addition of child widgets as declarative
    programming style.
    """

    id = StringProperty()
    """
    Widget ID.

    :attr:`id` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    widgets = ListProperty()
    """
    List of child widgets added declaratively.

    .. versionadded:: 2.0.0

    The `widgets` property allows you to define and manage child widgets in
    a declarative way. When assigned, the widgets in the list are automatically
    added to the parent container, and their IDs (if set) are registered
    internally for later reference.

    This property eliminates the need to call `add_widget()` manually for each
    child widget.

    .. tabs::
    
        .. tab:: Declarative Python style
    
            .. code-block:: python

                class CustomListItem(MDListItem):
                    def __init__(self, **kwargs):
                        super().__init__(**kwargs)
                        self.widgets = [
                            MDListItemLeadingIcon(icon="account"),
                            MDListItemHeadlineText(text="Title"),
                            MDListItemSupportingText(text="Subtitle"),
                            MDListItemTertiaryText(text="Tertiary"),
                            MDListItemTrailingIcon(icon="lock"),
                        ]

        .. tab:: Imperative Python style
    
            .. code-block:: python

                class CustomListItem(MDListItem):
                    def __init__(self, **kwargs):
                        super().__init__(**kwargs)
                        self.add_widget(MDListItemLeadingIcon(icon="account"))
                        self.add_widget(MDListItemHeadlineText(text="Title"))
                        self.add_widget(MDListItemSupportingText(text="Subtitle"))
                        self.add_widget(MDListItemTertiaryText(text="Tertiary"))
                        self.add_widget(MDListItemTrailingIcon(icon="lock"))

    Full example
    ------------

    .. code-block:: python

        from kivymd.app import MDApp
        from kivymd.uix.list import (
            MDListItem,
            MDListItemLeadingIcon,
            MDListItemHeadlineText,
            MDListItemSupportingText,
            MDListItemTertiaryText,
            MDListItemTrailingIcon,
        )
        from kivymd.uix.screen import MDScreen


        class CustomListItem(MDListItem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.widgets = [
                    MDListItemLeadingIcon(
                        icon="account"
                    ),
                    MDListItemHeadlineText(
                        text="MDListItemHeadlineText"
                    ),
                    MDListItemSupportingText(
                        text="MDListItemSupportingText"
                    ),
                    MDListItemTertiaryText(
                        text="MDListItemTertiaryText"
                    ),
                    MDListItemTrailingIcon(
                        icon="lock"
                    )
                ]


        class Example(MDApp):
            def build(self):
                return (
                    MDScreen(
                        CustomListItem(
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            size_hint_x=0.5
                        ),
                        md_bg_color=self.theme_cls.backgroundColor
                    )
                )


        Example().run()

    .. warning::

        When using the `widgets` property, it is recommended to only interact
        with child widgets via their registered IDs.

        .. code-block:: python

            class CustomListItem(MDListItem):
                def __init__(self, *args, **kwargs):
                    [...]

                    self.widgets = [
                        MDListItemLeadingIcon(
                            id="icon_account",
                            icon="account"
                        ),

                        [...]
                    ]


            class Example(MDApp):
                def change_icon(self, list_item):
                    # This work.
                    list_item.get_ids().icon_account.icon = "account-alert"
            
                def build(self):
                    return (
                        MDScreen(
                            CustomListItem(
                                [...]
                                on_release=self.change_icon,
                            ),
                            [...]
                        )
                    )

        Adding to or removing items from `self.widgets` directly at runtime 
        may lead to unexpected behavior.

        .. code-block:: python

            class CustomListItem(MDListItem):
                def __init__(self, *args, **kwargs):
                    [...]

                    self.widgets = [
                        MDListItemLeadingIcon(
                            id="icon_account",
                            icon="account"
                        ),

                        [...]
                    ]


            class Example(MDApp):
                def remove_icon(self, list_item):
                    # This won't work.
                    list_item.widgets.remove(list_item.get_ids().icon_account)
            
                def build(self):
                    return (
                        MDScreen(
                            CustomListItem(
                                [...]
                                on_release=self.remove_icon,
                            ),
                            [...]
                        )
                    )

    :attr:`widgets` is a :class:`~kivy.properties.ListProperty`
    and defaults to an empty list `[]`.
    """

    __ids = _Dict()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        for key, value in kwargs.items():
            if (
                value.__class__.__module__ == "kivy.properties"
                and value.__class__.__name__ == "ObservableList"
            ):
                value.obj().bind(
                    **{
                        value.prop.name: lambda *args, k=key: setattr(
                            self, k, args[-1]
                        )
                    }
                )

        for child in args:
            if issubclass(child.__class__, Widget):
                self.add_widget(child)
                self._register_ids(child)

    def on_widgets(self, instance, value) -> None:
        """
        Fired when the values of :attr:`widgets` change.

        .. versionadded:: 2.0.0
        """

        for child in value:
            if not isinstance(child, Widget):
                continue

            # Delete ID of widget if it was registered.
            if hasattr(child, "id") and child.id:
                self.__ids.pop(child.id, None)

            self.add_widget(child)
            self._register_ids(child)

    def get_ids(self) -> dict:
        """
        Returns a dictionary of widget IDs defined in Python
        code that is written in a declarative style.
        """

        return self.__ids

    def _register_ids(self, widget):
        if hasattr(widget, "id") and widget.id:
            self.__ids[widget.id] = widget
