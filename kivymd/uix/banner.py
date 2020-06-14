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

        MDToolbar:
            id: toolbar
            title: "Example Banners"
            elevation: 10
            pos_hint: {'top': 1}

        BoxLayout:
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
            ["One line string text example without actions.", "This is the second line of the banner message." "and this is the third line of the banner message."]

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
        icon: f"{images_path}/kivymd_logo.png"
        text: ["One line string text example without actions."]

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/banner-icon.png
    :align: center

.. Note:: `See full example <https://github.com/HeaTTheatR/KivyMD/wiki/Components-Banner>`_
"""

__all__ = ("MDBanner",)

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.widget import Widget

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

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import Clock kivy.clock.Clock


<ThreeLineIconBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    tertiary_text: root.text_message[2]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<TwoLineIconBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<OneLineIconBanner>
    text: root.text_message[0]
    divider: None
    _no_ripple_effect: True

    ImageLeftWidget:
        source: root.icon


<ThreeLineBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    tertiary_text: root.text_message[2]
    divider: None
    _no_ripple_effect: True


<TwoLineBanner>
    text: root.text_message[0]
    secondary_text: root.text_message[1]
    divider: None
    _no_ripple_effect: True


<OneLineBanner>
    text: root.text_message[0]
    divider: None
    _no_ripple_effect: True


<MDBanner>
    size_hint_y: None
    height: self.minimum_height
    banner_y: 0
    orientation: "vertical"
    y: Window.height - self.banner_y

    canvas:
        Color:
            rgba: 0, 0, 0, 0
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        id: container_message
        size_hint_y: None
        height: self.minimum_height

    BoxLayout:
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {"right": 1}
        padding: 0, 0, "8dp", "8dp"
        spacing: "8dp"

        BoxLayout:
            id: left_action_box
            size_hint: None, None
            size: self.minimum_size

        BoxLayout:
            id: right_action_box
            size_hint: None, None
            size: self.minimum_size
"""
)


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
    """Icon banner.

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
    """List of lines for banner text.
    Must contain no more than three lines for a
    `'one-line'`, `'two-line'` and `'three-line'` banner, respectively.

    :attr:`text` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    left_action = ListProperty()
    """The action of banner.

    To add one action, make a list [`'name_action'`, callback]
    where `'name_action'` is a string that corresponds to an action name and
    ``callback`` is the function called on a touch release event.

    :attr:`left_action` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action = ListProperty()
    """Works the same way as :attr:`left_action`.

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
    """Banner type. . Available options are: (`"one-line"`, `"two-line"`,
    `"three-line"`, `"one-line-icon"`, `"two-line-icon"`, `"three-line-icon"`).

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'one-line'`.
    """

    _type_message = None
    _progress = False

    def add_actions_buttons(self, box, data):
        if data:
            name_action_button, function_action_button = data
            action_button = MDFlatButton(
                text=f"[b]{name_action_button}[/b]",
                theme_text_color="Custom",
                text_color=self.theme_cls.primary_color,
                on_release=function_action_button,
            )
            action_button.markup = True
            box.add_widget(action_button)

    def set_left_action(self):
        self.add_actions_buttons(self.ids.left_action_box, self.left_action)

    def set_right_action(self):
        self.add_actions_buttons(self.ids.right_action_box, self.right_action)

    def set_type_banner(self):
        self._type_message = {
            "three-line-icon": ThreeLineIconBanner,
            "two-line-icon": TwoLineIconBanner,
            "one-line-icon": OneLineIconBanner,
            "three-line": ThreeLineBanner,
            "two-line": TwoLineBanner,
            "one-line": OneLineBanner,
        }[self.type]

    def add_banner_to_container(self):
        self.ids.container_message.add_widget(
            self._type_message(text_message=self.text, icon=self.icon)
        )

    def show(self):
        def show(interval):
            self.set_type_banner()
            self.set_left_action()
            self.set_right_action()
            self.add_banner_to_container()
            Clock.schedule_once(self.animation_display_banner, 0.1)

        if self._progress:
            return
        self._progress = True
        if self.ids.container_message.children:
            self.hide()
        Clock.schedule_once(show, 0.7)

    def animation_display_banner(self, i):
        Animation(
            banner_y=self.height + self.vertical_pad,
            d=0.15,
            t=self.opening_transition,
        ).start(self)
        anim = Animation(
            y=self.over_widget.y - self.height,
            d=0.15,
            t=self.opening_transition,
        )
        anim.bind(on_complete=self._reset_progress)
        anim.start(self.over_widget)

    def hide(self):
        def hide(interval):
            anim = Animation(banner_y=0, d=0.15)
            anim.bind(on_complete=self._remove_banner)
            anim.start(self)
            Animation(y=self.over_widget.y + self.height, d=0.15).start(
                self.over_widget
            )

        Clock.schedule_once(hide, 0.5)

    def _remove_banner(self, *args):
        self.ids.container_message.clear_widgets()
        self.ids.left_action_box.clear_widgets()
        self.ids.right_action_box.clear_widgets()

    def _reset_progress(self, *args):
        self._progress = False


class BaseBanner(Widget):
    text_message = ListProperty(["", "", ""])
    icon = StringProperty()

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
