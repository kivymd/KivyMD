"""
Bottom Sheets
=============

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, Sheets: bottom <https://material.io/design/components/sheets-bottom.html>`_

In this module there's the :class:`MDBottomSheet` class
which will let you implement your own Material Design Bottom Sheets,
and there are two classes called :class:`MDListBottomSheet`
and :class:`MDGridBottomSheet` implementing the ones mentioned in the spec.

Example
-------

.. note::

    These widgets are designed to be called from Python code only.

For :class:`MDListBottomSheet`:

.. code-block:: python

    bs = MDListBottomSheet()
    bs.add_item("Here's an item with text only", lambda x: x)
    bs.add_item("Here's an item with an icon", lambda x: x, icon='md-cast')
    bs.add_item("Here's another!", lambda x: x, icon='md-nfc')
    bs.open()

For :class:`MDListBottomSheet`:

.. code-block:: python

    bs = MDGridBottomSheet()
    bs.add_item("Facebook", lambda x: x, icon_src='./assets/facebook-box.png')
    bs.add_item("YouTube", lambda x: x, icon_src='./assets/youtube-play.png')
    bs.add_item("Twitter", lambda x: x, icon_src='./assets/twitter.png')
    bs.add_item("Da Cloud", lambda x: x, icon_src='./assets/cloud-upload.png')
    bs.add_item("Camera", lambda x: x, icon_src='./assets/camera.png')
    bs.open()
"""

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    NumericProperty,
    ListProperty,
    BooleanProperty,
    OptionProperty,
)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView

from kivymd.uix.behaviors import BackgroundColorBehavior
from kivymd.uix.label import MDIcon
from kivymd.uix.list import (
    MDList,
    OneLineListItem,
    ILeftBody,
    OneLineIconListItem,
)
from kivymd.theming import ThemableBehavior
from kivymd import images_path

Builder.load_string(
    """
#:import Animation kivy.animation.Animation


<MDBottomSheet>
    md_bg_color: root.value_transparent
    _upper_padding: _upper_padding
    _gl_content: _gl_content

    BoxLayout:
        size_hint_y: None
        orientation: "vertical"
        padding: 0, 1, 0, 0
        height: self.minimum_height

        BsPadding:
            id: _upper_padding
            size_hint_y: None
            height: root.height - min(root.width * 9 / 16, root._gl_content.height)
            on_release: root.dismiss()

        BottomSheetContent:
            id: _gl_content
            size_hint_y: None
            cols: 1
            md_bg_color: 0, 0, 0, 0
            
            canvas:
                Color:
                    rgba: root.theme_cls.bg_normal if not root.bg_color else root.bg_color  
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: 
                        [
                        (root.radius, root.radius) if root.radius_from == "top_left" or root.radius_from == "top" else (0, 0),
                        (root.radius, root.radius) if root.radius_from == "top_right" or root.radius_from == "top" else (0, 0),
                        (root.radius, root.radius) if root.radius_from == "bottom_right" or root.radius_from == "bottom" else (0, 0),
                        (root.radius, root.radius) if root.radius_from == "bottom_left" or root.radius_from == "bottom" else (0, 0)
                        ]
                       
"""
)


class BsPadding(ButtonBehavior, FloatLayout):
    pass


class BottomSheetContent(BackgroundColorBehavior, GridLayout):
    pass


class MDBottomSheet(ThemableBehavior, ModalView):
    background = f"{images_path}transparent.png"
    """Private attribute."""

    duration_opening = NumericProperty(0.15)
    """Duration of animation."""

    radius = NumericProperty(25)
    """The value of the rounding of the corners of the dialog."""

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
    """Sets which corners to cut from the dialog."""

    animation = BooleanProperty(False)
    """Use window opening animation or not."""

    bg_color = ListProperty()
    """Dialog background color."""

    value_transparent = ListProperty([0, 0, 0, 0.8])
    """Background transparency value when opening a dialog."""

    fixed_height = NumericProperty()
    """Sets the exact height of the dialog.
    Otherwise, it is calculated automatically."""

    _upper_padding = ObjectProperty()
    _gl_content = ObjectProperty()
    _position_content = NumericProperty(Window.height)

    def open(self, *largs):
        super().open(*largs)

    def add_widget(self, widget, index=0, canvas=None):
        super().add_widget(widget, index, canvas)

    def on_dismiss(self):
        self._gl_content.clear_widgets()

    def resize_content_layout(self, content, layout, interval=0):
        if layout.height < dp(100):
            layout.height = Window.height
        if self.animation:
            Animation(height=layout.height, d=self.duration_opening).start(
                content
            )
        else:
            content.height = layout.height


Builder.load_string(
    """
<ListBottomSheetIconLeft>
    halign: "center"
    theme_text_color: "Primary"
    valign: "middle"
"""
)


class ListBottomSheetIconLeft(ILeftBody, MDIcon):
    pass


class MDCustomBottomSheet(MDBottomSheet):
    screen = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._gl_content.add_widget(self.screen)
        Clock.schedule_once(
            lambda x: self.resize_content_layout(
                self._gl_content, self.screen
            ),
            0,
        )


class MDListBottomSheet(MDBottomSheet):
    mlist = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mlist = MDList()
        self._gl_content.add_widget(self.mlist)
        Clock.schedule_once(
            lambda x: self.resize_content_layout(
                self._gl_content, self.mlist
            ),
            0,
        )

    def add_item(self, text, callback, icon=None):
        if icon:
            item = OneLineIconListItem(text=text, on_release=callback)
            item.add_widget(ListBottomSheetIconLeft(icon=icon))
        else:
            item = OneLineListItem(text=text, on_release=callback)
        item.bind(on_release=lambda x: self.dismiss())
        self.mlist.add_widget(item)


Builder.load_string(
    """
<GridBottomSheetItem>
    orientation: "vertical"
    padding: 0, dp(24), 0, 0
    size_hint_y: None
    size: dp(64), dp(96)

    BoxLayout:
        padding: dp(8), 0, dp(8), dp(8)
        size_hint_y: None
        height: dp(48)

        Image:
            source: root.source

    MDLabel:
        font_style: "Caption"
        theme_text_color: "Secondary"
        text: root.caption
        halign: "center"
"""
)


class GridBottomSheetItem(ButtonBehavior, BoxLayout):
    source = StringProperty()
    caption = StringProperty()


class MDGridBottomSheet(MDBottomSheet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._gl_content.padding = (dp(16), 0, dp(16), dp(24))
        self._gl_content.height = dp(24)
        self._gl_content.cols = 3

    def add_item(self, text, callback, icon_src):
        item = GridBottomSheetItem(
            caption=text, on_release=callback, source=icon_src
        )
        item.bind(on_release=lambda x: self.dismiss())
        if len(self._gl_content.children) % 3 == 0:
            self._gl_content.height += dp(96)
        self._gl_content.add_widget(item)
