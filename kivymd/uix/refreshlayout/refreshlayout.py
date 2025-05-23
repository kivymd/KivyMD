"""
Components/RefreshLayout
========================

Example
-------

.. tabs::

    .. tab:: Declarative Python style with KV

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.list import (
                MDListItem, MDListItemHeadlineText, MDListItemTrailingIcon
            )

            import asynckivy

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:

                        MDTopAppBarLeadingButtonContainer:

                            MDActionTopAppBarButton:
                                icon: 'menu'

                        MDTopAppBarTitle:
                            text: 'Example Refresh Layout'

                    MDScrollViewRefreshLayout:
                        id: refresh_layout
                        refresh_callback: app.refresh_callback
                        root_layout: root
                        spinner_color: "brown"
                        circle_color: "white"

                        MDGridLayout:
                            id: box
                            adaptive_height: True
                            cols: 1
            '''


            class Example(MDApp):
                x = 0
                y = 15

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)

                def on_start(self):
                    self.set_list()

                def set_list(self):
                    async def set_list():
                        names_icons_list = list(md_icons.keys())[self.x:self.y]
                        for name_icon in names_icons_list:
                            await asynckivy.sleep(0)
                            self.root.ids.box.add_widget(
                                MDListItem(
                                    MDListItemHeadlineText(
                                        text=name_icon
                                    ),
                                    MDListItemTrailingIcon(
                                        icon=name_icon
                                    )
                                )
                            )

                    asynckivy.start(set_list())

                def refresh_callback(self, *args):
                    '''
                    A method that updates the state of your application
                    while the spinner remains on the screen.
                    '''

                    def refresh_callback(interval):
                        self.root.ids.box.clear_widgets()
                        if self.x == 0:
                            self.x, self.y = 15, 30
                        else:
                            self.x, self.y = 0, 15
                        self.set_list()
                        self.root.ids.refresh_layout.refresh_done()
                        self.tick = 0

                    Clock.schedule_once(refresh_callback, 1)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.icon_definitions import md_icons
            from kivymd.uix.floatlayout import MDFloatLayout
            from kivymd.uix.gridlayout import MDGridLayout
            from kivymd.uix.refreshlayout import MDScrollViewRefreshLayout
            from kivymd.uix.list import (
                MDListItem, MDListItemHeadlineText, MDListItemTrailingIcon
            )
            from kivymd.uix.appbar import (
                MDTopAppBar,
                MDTopAppBarLeadingButtonContainer,
                MDActionTopAppBarButton,
                MDTopAppBarTitle,
            )

            import asynckivy


            class Example(MDApp):
                x = 0
                y = 15

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDFloatLayout(
                            MDBoxLayout(
                                MDTopAppBar(
                                    MDTopAppBarLeadingButtonContainer(
                                        MDActionTopAppBarButton(
                                            icon='menu'
                                        )
                                    ),
                                    MDTopAppBarTitle(
                                        text='Example Refresh Layout'
                                    )
                                ),
                                MDScrollViewRefreshLayout(
                                    MDGridLayout(
                                        id="box",
                                        adaptive_height=True,
                                        cols=1,
                                    ),
                                    id="refresh_layout",
                                    refresh_callback=self.refresh_callback,
                                    spinner_color="red",
                                    circle_color="white",
                                ),
                                orientation='vertical'
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def on_start(self):
                    self.root.get_ids().refresh_layout.root_layout = self.root
                    self.set_list()

                def set_list(self):
                    async def set_list():
                        names_icons_list = list(md_icons.keys())[self.x:self.y]
                        for name_icon in names_icons_list:
                            await asynckivy.sleep(0)
                            self.root.get_ids().box.add_widget(
                                MDListItem(
                                    MDListItemHeadlineText(
                                        text=name_icon
                                    ),
                                    MDListItemTrailingIcon(
                                        icon=name_icon
                                    )
                                )
                            )
                    asynckivy.start(set_list())

                def refresh_callback(self, *args):
                    '''
                    A method that updates the state of your application
                    while the spinner remains on the screen.
                    '''

                    def refresh_callback(interval):
                        self.root.get_ids().box.clear_widgets()
                        if self.x == 0:
                            self.x, self.y = 15, 30
                        else:
                            self.x, self.y = 0, 15
                        self.set_list()
                        self.root.get_ids().refresh_layout.refresh_done()
                        self.tick = 0

                    Clock.schedule_once(refresh_callback, 1)


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/refresh-layout-example.gif
    :align: center
"""

__all__ = ("MDScrollViewRefreshLayout",)

import os
from typing import Union

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
)
from kivy.uix.floatlayout import FloatLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.scrollview import MDScrollView

with open(
    os.path.join(uix_path, "refreshlayout", "refreshlayout.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class _RefreshScrollEffect(DampedScrollEffect):
    """
    This class is simply based on DampedScrollEffect.
    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """

    min_scroll_to_reload = NumericProperty("-100dp")
    """
    Minimum overscroll value to reload.

    :attr:`min_scroll_to_reload` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'-100dp'`.
    """

    def on_overscroll(
        self, instance_refresh_scroll_effect, overscroll: Union[int, float]
    ) -> bool:
        if overscroll < self.min_scroll_to_reload:
            scroll_view = self.target_widget.parent
            scroll_view._did_overscroll = True
            return True
        else:
            return False


class MDScrollViewRefreshLayout(MDScrollView, ThemableBehavior):
    """
    Refresh layout class.

    For more information, see in the
    :class:`~kivymd.uix.scrollview.MDScrollView` and
    :class:`~kivymd.theming.ThemableBehavior` class documentation.
    """

    root_layout = ObjectProperty()
    """
    The spinner will be attached to this layout.

    :attr:`root_layout` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    refresh_callback = ObjectProperty()
    """
    The method that will be called at the on_touch_up event,
    provided that the overscroll of the list has been registered.

    :attr:`refresh_callback` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    spinner_color = ColorProperty([1, 1, 1, 1])
    """
    Color of the spinner in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`spinner_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    circle_color = ColorProperty(None)
    """
    Color of the ellipse around the spinner in (r, g, b, a) or string format.

    .. versionadded:: 1.2.0

    :attr:`circle_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    show_transition = StringProperty("out_elastic")
    """
    Transition of the spinner's opening.

    .. versionadded:: 1.2.0

    :attr:`show_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_elastic'`.
    """

    show_duration = NumericProperty(0.8)
    """
    Duration of the spinner display.

    .. versionadded:: 1.2.0

    :attr:`show_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    hide_transition = StringProperty("out_elastic")
    """
    Transition of hiding the spinner.

    .. versionadded:: 1.2.0

    :attr:`hide_transition` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'out_elastic'`.
    """

    hide_duration = NumericProperty(0.8)
    """
    Duration of hiding the spinner.

    .. versionadded:: 1.2.0

    :attr:`hide_duration` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `0.8`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.circle_color:
            self.circle_color = self.theme_cls.primaryColor
        self.effect_cls = _RefreshScrollEffect
        self._work_spinner = False
        self._did_overscroll = False
        self.refresh_spinner = None

    def on_touch_up(self, *args):
        if self._did_overscroll and not self._work_spinner:
            if self.refresh_callback:
                self.refresh_callback()
            if not self.refresh_spinner:
                self.refresh_spinner = RefreshSpinner(
                    _refresh_layout=self,
                    spinner_color=self.spinner_color,
                    circle_color=self.circle_color,
                    show_transition=self.show_transition,
                    show_duration=self.show_duration,
                    hide_transition=self.hide_transition,
                    hide_duration=self.hide_duration,
                )
                self.root_layout.add_widget(self.refresh_spinner)
            self.refresh_spinner.start_anim_spinner()
            self._work_spinner = True
            self._did_overscroll = False
            return True

        return super().on_touch_up(*args)

    def refresh_done(self) -> None:
        if self.refresh_spinner:
            self.refresh_spinner.hide_anim_spinner()


class RefreshSpinner(ThemableBehavior, FloatLayout):
    # Color of the spinner in (r, g, b, a) or string format.
    spinner_color = ColorProperty([1, 1, 1, 1])
    # Color of the ellipse around the spinner in (r, g, b, a) or string format.
    circle_color = ColorProperty()
    # Transition of the spinner's opening.
    show_transition = StringProperty()
    # The duration of the spinner display.
    show_duration = NumericProperty(0.8)
    # Transition of hiding the spinner.
    hide_transition = StringProperty()
    # Duration of hiding the spinner.
    hide_duration = NumericProperty(0.8)

    # kivymd.refreshlayout.MDScrollViewRefreshLayout object
    _refresh_layout = ObjectProperty()

    def start_anim_spinner(self) -> None:
        spinner = self.ids.body_spinner
        Animation(
            y=spinner.y - dp(48) * 2 + dp(10),
            d=self.show_duration,
            t=self.show_transition,
        ).start(spinner)

    def hide_anim_spinner(self) -> None:
        spinner = self.ids.body_spinner
        anim = Animation(
            y=Window.height, d=self.hide_duration, t=self.hide_transition
        )
        anim.bind(on_complete=self.set_spinner)
        anim.start(spinner)

    def set_spinner(self, *args) -> None:
        body_spinner = self.ids.body_spinner
        body_spinner.size = (dp(46), dp(46))
        body_spinner.y = Window.height
        body_spinner.opacity = 1
        spinner = self.ids.spinner
        spinner.size = (dp(30), dp(30))
        spinner.opacity = 1
        self._refresh_layout._work_spinner = False
        self._refresh_layout._did_overscroll = False
