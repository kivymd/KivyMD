"""
Components/Banner
=================

.. seealso::

    `Material Design spec, Banner <https://material.io/components/banners>`_

.. rubric:: A banner displays a prominent message and related optional actions.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner.png
    :align: center

Usage
=====

.. code-block:: python

    from kivy.lang import Builder
    from kivy.factory import Factory

    from kivymd.app import MDApp

    Builder.load_string('''
    <ExampleBanner@Screen>

        MDBanner:
            id: banner
            text: ["One line string text example without actions."]
            # The widget that is under the banner.
            # It will be shifted down to the height of the banner.
            over_widget: screen
            vertical_pad: toolbar.height

        MDTopAppBar:
            id: toolbar
            title: "Example Banners"
            elevation: 4
            pos_hint: {'top': 1}

        MDBoxLayout:
            id: screen
            orientation: "vertical"
            size_hint_y: None
            height: Window.height - toolbar.height

            OneLineListItem:
                text: "Banner without actions"
                on_release: banner.show()

            Widget:
    ''')


    class Test(MDApp):
        def build(self):
            return Factory.ExampleBanner()


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-example-1.gif
    :align: center

.. rubric:: Banner type.

By default, the banner is of the type ``'one-line'``:

.. code-block:: kv

    MDBanner:
        text: ["One line string text example without actions."]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-one-line.png
    :align: center

To use a two-line banner, specify the ``'two-line'`` :attr:`MDBanner.type` for the banner
and pass the list of two lines to the :attr:`MDBanner.text` parameter:

.. code-block:: kv

    MDBanner:
        type: "two-line"
        text:
            ["One line string text example without actions.", "This is the second line of the banner message."]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-two-line.png
    :align: center

Similarly, create a three-line banner:

.. code-block:: kv

    MDBanner:
        type: "three-line"
        text:
            ["One line string text example without actions.", "This is the second line of the banner message.", "and this is the third line of the banner message."]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-three-line.png
    :align: center

To add buttons to any type of banner,
use the :attr:`MDBanner.left_action` and :attr:`MDBanner.right_action` parameters,
which should take a list ['Button name', function]:

.. code-block:: kv

    MDBanner:
        text: ["One line string text example without actions."]
        left_action: ["CANCEL", lambda x: None]

Or two buttons:

.. code-block:: kv

    MDBanner:
        text: ["One line string text example without actions."]
        left_action: ["CANCEL", lambda x: None]
        right_action: ["CLOSE", lambda x: None]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-actions.png
    :align: center

If you want to use the icon on the left in the banner,
add the prefix `'-icon'` to the banner type:

.. code-block:: kv

    MDBanner:
        type: "one-line-icon"
        icon: f"{images_path}/kivymd.png"
        text: ["One line string text example without actions."]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-icon.png
    :align: center

.. Note:: `See full example <https://github.com/kivymd/KivyMD/wiki/Components-Banner>`_
"""

__all__ = ("MDBanner",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BoundedNumericProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    OneLineAvatarListItem,
    OneLineListItem,
    ThreeLineAvatarListItem,
    ThreeLineListItem,
    TwoLineAvatarListItem,
    TwoLineListItem,
)

with open(
    os.path.join(uix_path, "banner", "banner.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDBanner(MDCard):
    vertical_pad = NumericProperty(dp(68))
    """
    Indent the banner at the top of the screen.

    :attr:`vertical_pad` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(68)`.
    """

    opening_transition = StringProperty("in_quad")
    """
    The name of the animation transition.

    :attr:`opening_transition` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'in_quad'`.
    """

    icon = StringProperty("data/logo/kivy-icon-128.png")
    """
    Icon banner.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'data/logo/kivy-icon-128.png'`.
    """

    over_widget = ObjectProperty()
    """
    The widget that is under the banner.
    It will be shifted down to the height of the banner.

    :attr:`over_widget` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    text = ListProperty()
    """
    List of lines for banner text.
    Must contain no more than three lines for a
    `'one-line'`, `'two-line'` and `'three-line'` banner, respectively.

    :attr:`text` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    left_action = ListProperty()
    """
    The action of banner.

    To add one action, make a list [`'name_action'`, callback]
    where `'name_action'` is a string that corresponds to an action name and
    ``callback`` is the function called on a touch release event.

    :attr:`left_action` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action = ListProperty()
    """
    Works the same way as :attr:`left_action`.

    :attr:`right_action` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    type = OptionProperty(
        "one-line",
        options=[
            "one-line",
            "two-line",
            "three-line",
            "one-line-icon",
            "two-line-icon",
            "three-line-icon",
        ],
        allownone=True,
    )
    """
    Banner type. . Available options are: (`"one-line"`, `"two-line"`,
    `"three-line"`, `"one-line-icon"`, `"two-line-icon"`, `"three-line-icon"`).

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'one-line'`.
    """

    opening_timeout = BoundedNumericProperty(0.7, min=0.7)
    """
    Time interval after which the banner will be shown.

    .. versionadded:: 1.0.0

    :attr:`opening_timeout` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.7`.
    """

    opening_time = NumericProperty(0.15)
    """
    The time taken for the banner to slide to the :attr:`state` `'open'`.

    .. versionadded:: 1.0.0

    :attr:`opening_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    closing_time = NumericProperty(0.15)
    """
    The time taken for the banner to slide to the :attr:`state` `'close'`.

    .. versionadded:: 1.0.0

    :attr:`closing_time` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    _type_message = None
    _progress = False

    def add_actions_buttons(
        self, instance_box: MDBoxLayout, data: list
    ) -> None:
        """
        Adds buttons to the banner.

        :param data: ['NAME BUTTON', <function>];
        """

        if data:
            name_action_button, function_action_button = data
            action_button = MDFlatButton(
                text=f"[b]{name_action_button}[/b]",
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_color,
                on_release=function_action_button,
            )
            action_button.markup = True
            instance_box.add_widget(action_button)

    def show(self) -> None:
        """Displays a banner on the screen."""

        def show(interval: Union[int, float]):
            self.set_type_banner()
            self.add_actions_buttons(self.ids.left_action_box, self.left_action)
            self.add_actions_buttons(
                self.ids.right_action_box, self.right_action
            )
            self._add_banner_to_container()
            Clock.schedule_once(self.animation_display_banner, 0.1)

        if not self._progress:
            self._progress = True
            if self.ids.container_message.children:
                self.hide()
            Clock.schedule_once(show, self.opening_timeout)

    def hide(self) -> None:
        """Hides the banner from the screen."""

        def hide(interval: Union[int, float]):
            anim = Animation(banner_y=0, d=self.closing_time)
            anim.bind(on_complete=self._remove_banner)
            anim.start(self)
            Animation(
                y=self.over_widget.y + self.height, d=self.closing_time
            ).start(self.over_widget)

        if not self._progress:
            self._progress = True
            Clock.schedule_once(hide, 0.5)

    def set_type_banner(self) -> None:
        self._type_message = {
            "three-line-icon": ThreeLineIconBanner,
            "two-line-icon": TwoLineIconBanner,
            "one-line-icon": OneLineIconBanner,
            "three-line": ThreeLineBanner,
            "two-line": TwoLineBanner,
            "one-line": OneLineBanner,
        }[self.type]

    def animation_display_banner(self, interval: Union[int, float]) -> None:
        Animation(
            banner_y=self.height + self.vertical_pad,
            d=self.opening_time,
            t=self.opening_transition,
        ).start(self)
        anim = Animation(
            y=self.over_widget.y - self.height,
            d=self.opening_time,
            t=self.opening_transition,
        )
        anim.bind(on_complete=self._reset_progress)
        anim.start(self.over_widget)

    def _remove_banner(self, *args):
        self.ids.container_message.clear_widgets()
        self.ids.left_action_box.clear_widgets()
        self.ids.right_action_box.clear_widgets()
        self._reset_progress()

    def _reset_progress(self, *args):
        self._progress = False

    def _add_banner_to_container(self) -> None:
        self.ids.container_message.add_widget(
            self._type_message(text_message=self.text, icon=self.icon)
        )


class BaseBanner(Widget):
    """Implements the base banner class."""

    text_message = ListProperty(["", "", ""])
    """
    List of banner strings. First, second and, respectively, third lines.

    :attr:`text_message` is an :class:`~kivy.properties.ListProperty`
    and defaults to `['', '', '']`.
    """

    icon = StringProperty()
    """
    Icon banner.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    def on_touch_down(self, touch):
        self.parent.parent.hide()


class ThreeLineIconBanner(ThreeLineAvatarListItem, BaseBanner):
    pass


class TwoLineIconBanner(TwoLineAvatarListItem, BaseBanner):
    pass


class OneLineIconBanner(OneLineAvatarListItem, BaseBanner):
    pass


class ThreeLineBanner(ThreeLineListItem, BaseBanner):
    pass


class TwoLineBanner(TwoLineListItem, BaseBanner):
    pass


class OneLineBanner(OneLineListItem, BaseBanner):
    pass
