"""
Components/BottomSheet
======================

.. seealso::

    `Material Design spec, Sheets: bottom <https://material.io/components/sheets-bottom>`_

.. rubric:: Bottom sheets are surfaces containing supplementary content that are anchored to the bottom of the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet.png
    :align: center

Two classes are available to you :class:`~MDListBottomSheet` and :class:`~MDGridBottomSheet`
for standard bottom sheets dialogs:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/grid-list-bottomsheets.png
    :align: center

Usage :class:`~MDListBottomSheet`
=================================

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.toast import toast
    from kivymd.uix.bottomsheet import MDListBottomSheet
    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDTopAppBar:
            title: "Example BottomSheet"
            pos_hint: {"top": 1}
            elevation: 4

        MDRaisedButton:
            text: "Open list bottom sheet"
            on_release: app.show_example_list_bottom_sheet()
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def callback_for_menu_items(self, *args):
            toast(args[0])

        def show_example_list_bottom_sheet(self):
            bottom_sheet_menu = MDListBottomSheet()
            for i in range(1, 11):
                bottom_sheet_menu.add_item(
                    f"Standart Item {i}",
                    lambda x, y=i: self.callback_for_menu_items(
                        f"Standart Item {y}"
                    ),
                )
            bottom_sheet_menu.open()


    Example().run()

The :attr:`~MDListBottomSheet.add_item` method of the :class:`~MDListBottomSheet`
class takes the following arguments:

``text`` - element text;

``callback`` - function that will be called when clicking on an item;

There is also an optional argument ``icon``,
which will be used as an icon to the left of the item:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/icon-list-bottomsheets.png
    :align: center

.. rubric:: Using the :class:`~MDGridBottomSheet` class is similar
    to using the :class:`~MDListBottomSheet` class:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.toast import toast
    from kivymd.uix.bottomsheet import MDGridBottomSheet
    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDTopAppBar:
            title: 'Example BottomSheet'
            pos_hint: {"top": 1}
            elevation: 4

        MDRaisedButton:
            text: "Open grid bottom sheet"
            on_release: app.show_example_grid_bottom_sheet()
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def callback_for_menu_items(self, *args):
            toast(args[0])

        def show_example_grid_bottom_sheet(self):
            bottom_sheet_menu = MDGridBottomSheet()
            data = {
                "Facebook": "facebook-box",
                "YouTube": "youtube",
                "Twitter": "twitter-box",
                "Da Cloud": "cloud-upload",
                "Camera": "camera",
            }
            for item in data.items():
                bottom_sheet_menu.add_item(
                    item[0],
                    lambda x, y=item[0]: self.callback_for_menu_items(y),
                    icon_src=item[1],
                )
            bottom_sheet_menu.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/grid-bottomsheet.png
    :align: center

.. rubric:: You can use custom content for bottom sheet dialogs:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.factory import Factory

    from kivymd.uix.bottomsheet import MDCustomBottomSheet
    from kivymd.app import MDApp

    KV = '''
    <ItemForCustomBottomSheet@OneLineIconListItem>
        on_press: app.custom_sheet.dismiss()
        icon: ""

        IconLeftWidget:
            icon: root.icon


    <ContentCustomSheet@BoxLayout>:
        orientation: "vertical"
        size_hint_y: None
        height: "400dp"

        MDTopAppBar:
            title: 'Custom bottom sheet:'

        ScrollView:

            MDGridLayout:
                cols: 1
                adaptive_height: True

                ItemForCustomBottomSheet:
                    icon: "page-previous"
                    text: "Preview"

                ItemForCustomBottomSheet:
                    icon: "exit-to-app"
                    text: "Exit"


    MDScreen:

        MDTopAppBar:
            title: 'Example BottomSheet'
            pos_hint: {"top": 1}
            elevation: 4

        MDRaisedButton:
            text: "Open custom bottom sheet"
            on_release: app.show_example_custom_bottom_sheet()
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        custom_sheet = None

        def build(self):
            return Builder.load_string(KV)

        def show_example_custom_bottom_sheet(self):
            self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
            self.custom_sheet.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/custom-bottomsheet.png
    :align: center

.. note:: When you use the :attr:`~MDCustomBottomSheet` class, you must specify
    the height of the user-defined content exactly, otherwise ``dp(100)``
    heights will be used for your ``ContentCustomSheet`` class:

.. code-block:: kv

    <ContentCustomSheet@BoxLayout>:
        orientation: "vertical"
        size_hint_y: None
        height: "400dp"

.. note:: The height of the bottom sheet dialog will never exceed half
    the height of the screen!
"""

__all__ = (
    "MDGridBottomSheet",
    "GridBottomSheetItem",
    "MDListBottomSheet",
    "MDCustomBottomSheet",
    "MDBottomSheet",
)

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView

from kivymd import images_path, uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import BackgroundColorBehavior
from kivymd.uix.label import MDIcon
from kivymd.uix.list import ILeftBody, OneLineIconListItem, OneLineListItem

with open(
    os.path.join(uix_path, "bottomsheet", "bottomsheet.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class SheetList(ScrollView):
    pass


class BsPadding(ButtonBehavior, FloatLayout):
    pass


class BottomSheetContent(BackgroundColorBehavior, GridLayout):
    pass


class MDBottomSheet(ThemableBehavior, ModalView):
    background = f"{images_path}transparent.png"
    """Private attribute."""

    duration_opening = NumericProperty(0.15)
    """
    The duration of the bottom sheet dialog opening animation.

    :attr:`duration_opening` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    duration_closing = NumericProperty(0.15)
    """
    The duration of the bottom sheet dialog closing animation.

    :attr:`duration_closing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.15`.
    """

    radius = NumericProperty(25)
    """
    The value of the rounding of the corners of the dialog.

    :attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `25`.
    """

    radius_from = OptionProperty(
        None,
        options=[
            "top_left",
            "top_right",
            "top",
            "bottom_right",
            "bottom_left",
            "bottom",
        ],
        allownone=True,
    )
    """
    Sets which corners to cut from the dialog. Available options are:
    (`"top_left"`, `"top_right"`, `"top"`, `"bottom_right"`, `"bottom_left"`, `"bottom"`).

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/bottomsheet-radius-from.png
        :align: center

    :attr:`radius_from` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    animation = BooleanProperty(False)
    """
    Whether to use animation for opening and closing of the bottomsheet or not.

    :attr:`animation` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    bg_color = ColorProperty(None)
    """
    Dialog background color in ``rgba`` format.

    :attr:`bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[]`.
    """

    value_transparent = ColorProperty([0, 0, 0, 0.8])
    """
    Background transparency value when opening a dialog.

    :attr:`value_transparent` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.8]`.
    """

    _upper_padding = ObjectProperty()
    _gl_content = ObjectProperty()
    _position_content = NumericProperty()

    def open(self, *args):
        super().open(*args)

    def add_widget(self, widget, index=0, canvas=None):
        super().add_widget(widget, index, canvas)

    def dismiss(self, *args, **kwargs):
        def dismiss(*args):
            self.dispatch("on_pre_dismiss")
            self._gl_content.clear_widgets()
            self._real_remove_widget()
            self.dispatch("on_dismiss")

        if self.animation:
            a = Animation(height=0, d=self.duration_closing)
            a.bind(on_complete=dismiss)
            a.start(self._gl_content)
        else:
            dismiss()

    def resize_content_layout(self, content, layout, interval=0):
        if not layout.ids.get("box_sheet_list"):
            _layout = layout
        else:
            _layout = layout.ids.box_sheet_list

        if _layout.height > Window.height / 2:
            height = Window.height / 2
        else:
            height = _layout.height

        if self.animation:
            Animation(height=height, d=self.duration_opening).start(_layout)
            Animation(height=height, d=self.duration_opening).start(content)
        else:
            layout.height = height
            content.height = height


class ListBottomSheetIconLeft(ILeftBody, MDIcon):
    pass


class MDCustomBottomSheet(MDBottomSheet):
    screen = ObjectProperty()
    """
    Custom content.

    :attr:`screen` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._gl_content.add_widget(self.screen)
        Clock.schedule_once(
            lambda x: self.resize_content_layout(self._gl_content, self.screen),
            0,
        )


class MDListBottomSheet(MDBottomSheet):
    sheet_list = ObjectProperty()
    """
    :attr:`sheet_list` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sheet_list = SheetList(size_hint_y=None)
        self._gl_content.add_widget(self.sheet_list)
        Clock.schedule_once(
            lambda x: self.resize_content_layout(
                self._gl_content, self.sheet_list
            ),
            0,
        )

    def add_item(self, text, callback, icon=None):
        """
        :arg text: element text;
        :arg callback: function that will be called when clicking on an item;
        :arg icon: which will be used as an icon to the left of the item;
        """

        if icon:
            item = OneLineIconListItem(text=text, on_release=callback)
            item.add_widget(ListBottomSheetIconLeft(icon=icon))
        else:
            item = OneLineListItem(text=text, on_release=callback)
        item.bind(on_release=lambda x: self.dismiss())
        self.sheet_list.ids.box_sheet_list.add_widget(item)


class GridBottomSheetItem(ButtonBehavior, BoxLayout):
    source = StringProperty()
    """
    Icon path if you use a local image or icon name
    if you use icon names from a file ``kivymd/icon_definitions.py``.

    :attr:`source` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    caption = StringProperty()
    """
    Item text.

    :attr:`caption` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon_size = NumericProperty("24sp")
    """
    Icon size.

    :attr:`caption` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'24sp'`.
    """


class MDGridBottomSheet(MDBottomSheet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sheet_list = SheetList(size_hint_y=None)
        self.sheet_list.ids.box_sheet_list.cols = 3
        self.sheet_list.ids.box_sheet_list.padding = (dp(16), 0, dp(16), dp(96))
        self._gl_content.add_widget(self.sheet_list)
        Clock.schedule_once(
            lambda x: self.resize_content_layout(
                self._gl_content, self.sheet_list
            ),
            0,
        )

    def add_item(self, text, callback, icon_src):
        """
        :arg text: element text;
        :arg callback: function that will be called when clicking on an item;
        :arg icon_src: icon item;
        """

        def tap_on_item(instance):
            callback(instance)
            self.dismiss()

        item = GridBottomSheetItem(
            caption=text, on_release=tap_on_item, source=icon_src
        )
        if len(self._gl_content.children) % 3 == 0:
            self._gl_content.height += dp(96)
        self.sheet_list.ids.box_sheet_list.add_widget(item)
