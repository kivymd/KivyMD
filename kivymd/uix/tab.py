"""
Components/Tabs
===============

.. seealso::

    `Material Design spec, Tabs <https://material.io/components/tabs>`_

.. rubric:: Tabs organize content across different screens, data sets,
    and other interactions.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs.png
    :align: center

.. Note:: Module provides tabs in the form of icons or text.

Usage
-----

To create a tab, you must create a new class that inherits from the
:class:`~MDTabsBase` class and the `Kivy` container, in which you will create
content for the tab.

.. code-block:: python

    class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''

.. code-block:: kv

    <Tab>:

        MDLabel:
            text: "Content"
            pos_hint: {"center_x": .5, "center_y": .5}

Tabs must be placed in the :class:`~MDTabs` container:

.. code-block:: kv

    Root:

        MDTabs:

            Tab:
                text: "Tab 1"

            Tab:
                text: "Tab 1"

            ...

Example with tab icon
---------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsBase
    from kivymd.icon_definitions import md_icons

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs
            on_tab_switch: app.on_tab_switch(*args)


    <Tab>:

        MDIconButton:
            id: icon
            icon: app.icons[0]
            user_font_size: "48sp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        icons = list(md_icons.keys())[15:30]

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for name_tab in self.icons:
                self.root.ids.tabs.add_widget(Tab(text=name_tab))

        def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
        ):
            '''Called when switching tabs.

            :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
            :param instance_tab: <__main__.Tab object>;
            :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
            :param tab_text: text or name icon of tab;
            '''

            count_icon = [k for k, v in md_icons.items() if v == tab_text]
            instance_tab.ids.icon.icon = count_icon[0]


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example.gif
    :align: center

Example with tab text
---------------------

.. Note:: The :class:`~MDTabsBase` class has an icon parameter and, by default,
    tries to find the name of the icon in the file
    ``kivymd/icon_definitions.py``. If the name of the icon is not found,
    then the name of the tab will be plain text, if found, the tab will look
    like the corresponding icon.

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsBase

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs
            on_tab_switch: app.on_tab_switch(*args)


    <Tab>:

        MDLabel:
            id: label
            text: "Tab 0"
            halign: "center"
    '''


    class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for i in range(20):
                self.root.ids.tabs.add_widget(Tab(text=f"Tab {i}"))

        def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
        ):
            '''Called when switching tabs.

            :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
            :param instance_tab: <__main__.Tab object>;
            :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
            :param tab_text: text or name icon of tab;
            '''

            instance_tab.ids.label.text = tab_text


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example-text.gif
    :align: center

Example with tab icon and text
------------------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsBase
    from kivymd.font_definitions import fonts
    from kivymd.icon_definitions import md_icons

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs
    '''


    class Tab(FloatLayout, MDTabsBase):
        pass


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for name_tab in list(md_icons.keys())[15:30]:
                self.root.ids.tabs.add_widget(
                    Tab(
                        text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[name_tab]}[/size][/font] {name_tab}"
                    )
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-simple-example-icon-text.png
    :align: center

Dynamic tab management
----------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.scrollview import ScrollView

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsBase

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs


    <Tab>:

        MDList:

            MDBoxLayout:
                adaptive_height: True

                MDFlatButton:
                    text: "ADD TAB"
                    on_release: app.add_tab()

                MDFlatButton:
                    text: "REMOVE LAST TAB"
                    on_release: app.remove_tab()

                MDFlatButton:
                    text: "GET TAB LIST"
                    on_release: app.get_tab_list()
    '''


    class Tab(ScrollView, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        index = 0

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            self.add_tab()

        def get_tab_list(self):
            '''Prints a list of tab objects.'''

            print(self.root.ids.tabs.get_tab_list())

        def add_tab(self):
            self.index += 1
            self.root.ids.tabs.add_widget(Tab(text=f"{self.index} tab"))

        def remove_tab(self):
            if self.index > 1:
                self.index -= 1
            self.root.ids.tabs.remove_widget(
                self.root.ids.tabs.get_tab_list()[0]
            )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-dynamic-managmant.gif
    :align: center

Use on_ref_press method
-----------------------

You can use markup for the text of the tabs and use the ``on_ref_press``
method accordingly:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.font_definitions import fonts
    from kivymd.uix.tab import MDTabsBase
    from kivymd.icon_definitions import md_icons

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs
            on_ref_press: app.on_ref_press(*args)


    <Tab>:

        MDIconButton:
            id: icon
            icon: app.icons[0]
            user_font_size: "48sp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        icons = list(md_icons.keys())[15:30]

        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            for name_tab in self.icons:
                self.root.ids.tabs.add_widget(
                    Tab(
                        text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {name_tab}"
                    )
                )

        def on_ref_press(
            self,
            instance_tabs,
            instance_tab_label,
            instance_tab,
            instance_tab_bar,
            instance_carousel,
        ):
            '''
            The method will be called when the ``on_ref_press`` event
            occurs when you, for example, use markup text for tabs.

            :param instance_tabs: <kivymd.uix.tab.MDTabs object>
            :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
            :param instance_tab: <__main__.Tab object>
            :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
            :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
            '''

            # Removes a tab by clicking on the close icon on the left.
            for instance_tab in instance_carousel.slides:
                if instance_tab.text == instance_tab_label.text:
                    instance_tabs.remove_widget(instance_tab_label)
                    break


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tabs-on-ref-press.gif
    :align: center

Switching the tab by name
-------------------------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout

    from kivymd.app import MDApp
    from kivymd.uix.tab import MDTabsBase
    from kivymd.icon_definitions import md_icons

    KV = '''
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Example Tabs"

        MDTabs:
            id: tabs


    <Tab>:

        MDIconButton:
            id: icon
            icon: "arrow-right"
            user_font_size: "48sp"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.switch_tab()
    '''


    class Tab(FloatLayout, MDTabsBase):
        '''Class implementing content for a tab.'''


    class Example(MDApp):
        icons = list(md_icons.keys())[15:30]

        def build(self):
            self.iter_list = iter(list(self.icons))
            return Builder.load_string(KV)

        def on_start(self):
            for name_tab in list(self.icons):
                self.root.ids.tabs.add_widget(Tab(text=name_tab))

        def switch_tab(self):
            '''Switching the tab by name.'''

            try:
                self.root.ids.tabs.switch_tab(next(self.iter_list))
            except StopIteration:
                pass


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switching-tab-by-name.gif
    :align: center
"""

__all__ = ("MDTabs", "MDTabsBase")

from kivy.clock import Clock
from kivy.graphics import RoundedRectangle
from kivy.lang import Builder
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.utils import boundary

from kivymd import fonts_path
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    RectangularElevationBehavior,
    RectangularRippleBehavior,
    SpecificBackgroundColorBehavior,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.carousel import MDCarousel

Builder.load_string(
    """
#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect


<MDTabsLabel>
    size_hint: None, 1
    halign: 'center'
    padding: '12dp', 0
    group: 'tabs'
    font: root.font_name
    allow_no_selection: False
    markup: True
    on_ref_press:
        self.tab_bar.parent.dispatch(\
        "on_ref_press",
        self, \
        self.tab, \
        self.tab_bar, \
        self.tab_bar.parent.carousel)
    color:
        self.text_color_active if self.state == 'down' \
        else self.text_color_normal
    on_width: root.tab_bar.parent._update_indicator(self)


<MDTabsScrollView>
    size_hint: 1, 1
    do_scroll_y: False
    bar_color: 0, 0, 0, 0
    bar_inactive_color: 0, 0, 0, 0
    bar_width: 0
    effect_cls: DampedScrollEffect


<MDTabs>
    carousel: carousel
    tab_bar: tab_bar
    anchor_y: 'top'
    background_palette: "Primary"

    _line_x: 0
    _line_width: 0
    _line_height: 0
    _line_radius: 0

    MDTabsMain:
        padding: 0, tab_bar.height, 0, 0

        MDTabsCarousel:
            id: carousel
            lock_swiping: root.lock_swiping
            ignore_perpendicular_swipes: True
            anim_move_duration: root.anim_duration
            on_index: root.on_carousel_index(*args)
            on__offset: tab_bar.android_animation(*args)
            on_slides:
                self.index = root.default_tab
                root.on_carousel_index(self, 0)

    MDTabsBar:
        id: tab_bar
        carousel: carousel
        scrollview: scrollview
        layout: layout
        size_hint: 1, None
        elevation: root.elevation
        height: root.tab_bar_height
        md_bg_color: self.theme_cls.primary_color if not root.background_color else root.background_color

        MDTabsScrollView:
            id: scrollview
            on_width: tab_bar._trigger_update_tab_bar()

            MDGridLayout:
                id: layout
                rows: 1
                size_hint_y: 1
                adaptive_width: True
                on_width: tab_bar._trigger_update_tab_bar()

                canvas.before:
                    Color:
                        rgba: root.theme_cls.accent_color if not root.indicator_color else root.indicator_color
                    RoundedRectangle:
                        pos: self.pos
                        size: 0, root.tab_indicator_height
                        radius: [0,]
                    Line:
                        rounded_rectangle: [root._line_x, self.pos[1], root._line_width, root._line_height, root._line_radius]
                        width: dp(2)
"""
)


class MDTabsException(Exception):
    pass


class MDTabsLabel(ToggleButtonBehavior, RectangularRippleBehavior, Label):
    """This class it represent the label of each tab."""

    text_color_normal = ColorProperty((0, 0, 0, 0))
    text_color_active = ColorProperty((0, 0, 0, 0))
    tab = ObjectProperty()
    tab_bar = ObjectProperty()
    font_name = StringProperty("Roboto")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min_space = 0

    def on_release(self):
        self.tab_bar.parent.dispatch("on_tab_switch", self.tab, self, self.text)
        # if the label is selected load the relative tab from carousel
        if self.state == "down":
            self.tab_bar.parent.carousel.load_slide(self.tab)

    def on_texture(self, widget, texture):
        # just save the minimum width of the label based of the content
        if texture:
            self.width = texture.width
            self.min_space = self.width


class MDTabsBase(Widget):
    """
    This class allow you to create a tab.
    You must create a new class that inherits from MDTabsBase.
    In this way you have total control over the views of your tabbed panel.
    """

    text = StringProperty()
    """
    It will be the label text of the tab.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    tab_label = ObjectProperty()
    """
    It is the label object reference of the tab.

    :attr:`tab_label` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        self.tab_label = MDTabsLabel(tab=self)
        super().__init__(**kwargs)

    def on_text(self, widget, text):
        # Set the icon
        if text in md_icons:
            self.tab_label.font_name = (
                fonts_path + "materialdesignicons-webfont.ttf"
            )
            self.tab_label.text = md_icons[self.text]
            self.tab_label.font_size = "24sp"
        # Set the label text
        else:
            self.tab_label.text = self.text


class MDTabsMain(MDBoxLayout):
    """
    This class is just a boxlayout that contain the carousel.
    It allows you to have control over the carousel.
    """


class MDTabsCarousel(MDCarousel):
    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def on_touch_move(self, touch):
        # lock a swiping
        if self.lock_swiping:
            return
        if not self.touch_mode_change:
            if self.ignore_perpendicular_swipes and self.direction in (
                "top",
                "bottom",
            ):
                if abs(touch.oy - touch.y) < self.scroll_distance:
                    if abs(touch.ox - touch.x) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True
            elif self.ignore_perpendicular_swipes and self.direction in (
                "right",
                "left",
            ):
                if abs(touch.ox - touch.x) < self.scroll_distance:
                    if abs(touch.oy - touch.y) > self.scroll_distance:
                        self._change_touch_mode()
                        self.touch_mode_change = True

        if self._get_uid("cavoid") in touch.ud:
            return
        if self._touch is not touch:
            super().on_touch_move(touch)
            return self._get_uid() in touch.ud
        if touch.grab_current is not self:
            return True
        ud = touch.ud[self._get_uid()]
        direction = self.direction[0]
        if ud["mode"] == "unknown":
            if direction in "rl":
                distance = abs(touch.ox - touch.x)
            else:
                distance = abs(touch.oy - touch.y)
            if distance > self.scroll_distance:
                ev = self._change_touch_mode_ev
                if ev is not None:
                    ev.cancel()
                ud["mode"] = "scroll"
        else:
            if direction in "rl":
                self._offset += touch.dx
            if direction in "tb":
                self._offset += touch.dy
        return True


class MDTabsScrollView(ScrollView):
    """This class hacked version to fix scroll_x manual setting."""

    def goto(self, scroll_x, scroll_y):
        """Update event value along with scroll_*."""

        def _update(e, x):
            if e:
                e.value = (e.max + e.min) * x

        if not (scroll_x is None):
            self.scroll_x = scroll_x
            _update(self.effect_x, scroll_x)

        if not (scroll_y is None):
            self.scroll_y = scroll_y
            _update(self.effect_y, scroll_y)


class MDTabsBar(ThemableBehavior, RectangularElevationBehavior, MDBoxLayout):
    """
    This class is just a boxlayout that contains the scroll view for tabs.
    It is also responsible for resizing the tab shortcut when necessary.
    """

    target = ObjectProperty(None, allownone=True)
    """
    It is the carousel reference of the next tab / slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab / slide of the carousel.

    :attr:`target` is an :class:`~kivy.properties.ObjectProperty`
    and default to `None`.
    """

    def get_rect_instruction(self):
        for i in self.layout.canvas.before.children:
            if isinstance(i, RoundedRectangle):
                return i

    indicator = AliasProperty(get_rect_instruction, cache=True)
    """
    It is the RoundedRectangle instruction reference of the tab indicator.

    :attr:`indicator` is an :class:`~kivy.properties.AliasProperty`.
    """

    def get_last_scroll_x(self):
        return self.scrollview.scroll_x

    last_scroll_x = AliasProperty(
        get_last_scroll_x, bind=("target",), cache=True
    )
    """
    Is the carousel reference of the next tab/slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab/slide of the carousel.

    :attr:`last_scroll_x` is an :class:`~kivy.properties.AliasProperty`.
    """

    def __init__(self, **kwargs):
        self._trigger_update_tab_bar = Clock.schedule_once(
            self._update_tab_bar, 0
        )
        super().__init__(**kwargs)

    def _update_tab_bar(self, *args):
        if self.parent.allow_stretch:
            # update width of the labels when it is needed
            width, tabs = self.scrollview.width, self.layout.children
            tabs_widths = [t.min_space for t in tabs if t.min_space]
            tabs_space = float(sum(tabs_widths))

            if not tabs_space:
                return

            ratio = width / tabs_space
            use_ratio = True in (width / len(tabs) < w for w in tabs_widths)

            for t in tabs:
                t.width = (
                    t.min_space
                    if tabs_space > width
                    else t.min_space * ratio
                    if use_ratio is True
                    else width / len(tabs)
                )

    def update_indicator(self, x, w, radius=None):
        # update position and size of the indicator
        if self.parent.tab_indicator_type == "line-round":
            self.parent._line_x = x
            self.parent._line_width = w
            self.parent._line_height = self.parent.tab_indicator_height
            self.parent._line_radius = self.parent.tab_indicator_height / 2
        elif self.parent.tab_indicator_type == "line-rect":
            self.parent._line_x = x
            self.parent._line_width = w
            self.parent._line_height = self.parent.tab_indicator_height
        else:
            self.indicator.pos = (x, 0)
            self.indicator.size = (w, self.parent.tab_indicator_height)
            if radius:
                self.indicator.radius = radius

    def tab_bar_autoscroll(self, target, step):
        # automatic scroll animation of the tab bar.
        bound_left = self.center_x
        bound_right = self.layout.width - bound_left
        dt = target.center_x - bound_left
        sx, sy = self.scrollview.convert_distance_to_scroll(dt, 0)

        # last scroll x of the tab bar
        lsx = self.last_scroll_x
        # determine scroll direction
        scroll_is_late = lsx < sx
        # distance to run
        dst = abs(lsx - sx) * step

        if not dst:
            return
        if scroll_is_late and target.center_x > bound_left:
            x = lsx + dst
        elif not scroll_is_late and target.center_x < bound_right:
            x = lsx - dst
        else:
            return

        x = boundary(x, 0.0, 1.0)
        self.scrollview.goto(x, None)

    def android_animation(self, carousel, offset):
        # try to reproduce the android animation effect.
        if offset != 0 and abs(offset) < carousel.width:
            forward = offset < 0
            offset = abs(offset)
            step = offset / float(carousel.width)
            distance = abs(offset - carousel.width)
            threshold = self.parent.anim_threshold
            breakpoint = carousel.width - (carousel.width * threshold)
            traveled = distance / breakpoint if breakpoint else 0
            break_step = 1.0 - traveled
            indicator_animation = self.parent.tab_indicator_anim

            skip_slide = (
                carousel.slides[carousel._skip_slide]
                if carousel._skip_slide is not None
                else None
            )
            next_slide = (
                carousel.next_slide if forward else carousel.previous_slide
            )
            self.target = skip_slide if skip_slide else next_slide

            if not self.target:
                return

            a = carousel.current_slide.tab_label
            b = self.target.tab_label
            self.tab_bar_autoscroll(b, step)

            if not indicator_animation:
                return

            if step <= threshold:
                if forward:
                    gap_w = abs((a.x + a.width) - (b.x + b.width))
                    w_step = a.width + (gap_w * step)
                    x_step = a.x
                else:
                    gap = abs((a.x - b.x))
                    x_step = a.x - gap * step
                    w_step = a.width + gap * step
            else:
                if forward:
                    x_step = a.x + abs((a.x - b.x)) * break_step
                    gap_w = abs((a.x + a.width) - (b.x + b.width))
                    ind_width = a.width + gap_w * threshold
                    gap_w = ind_width - b.width
                    w_step = ind_width - (gap_w * break_step)
                else:
                    x_step = a.x - abs((a.x - b.x)) * threshold
                    x_step = x_step - abs(x_step - b.x) * break_step
                    ind_width = (
                        (a.x + a.width) - x_step if threshold else a.width
                    )
                    gap_w = ind_width - b.width
                    w_step = ind_width - (gap_w * break_step)
                    w_step = (
                        w_step
                        if w_step + x_step <= a.x + a.width
                        else ind_width
                    )
            self.update_indicator(x_step, w_step)


class MDTabs(ThemableBehavior, SpecificBackgroundColorBehavior, AnchorLayout):
    """
    You can use this class to create your own tabbed panel..

    :Events:
        `on_tab_switch`
            Called when switching tabs.
        `on_slide_progress`
            Called while the slide is scrolling.
        `on_ref_press`
            The method will be called when the ``on_ref_press`` event
            occurs when you, for example, use markup text for tabs.
    """

    default_tab = NumericProperty(0)
    """
    Index of the default tab.

    :attr:`default_tab` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    tab_bar_height = NumericProperty("48dp")
    """
    Height of the tab bar.

    :attr:`tab_bar_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'48dp'`.
    """

    tab_indicator_anim = BooleanProperty(False)
    """
    Tab indicator animation. If you want use animation set it to ``True``.

    :attr:`tab_indicator_anim` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    tab_indicator_height = NumericProperty("2dp")
    """
    Height of the tab indicator.

    :attr:`tab_indicator_height` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'2dp'`.
    """

    tab_indicator_type = OptionProperty(
        "line", options=["line", "fill", "round", "line-round", "line-rect"]
    )
    """
    Type of tab indicator. Available options are: `'line'`, `'fill'`,
    `'round'`, `'line-rect'` and `'line-round'`.

    :attr:`tab_indicator_type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'line'`.
    """

    anim_duration = NumericProperty(0.2)
    """
    Duration of the slide animation.

    :attr:`anim_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0.2`.
    """

    anim_threshold = BoundedNumericProperty(
        0.8, min=0.0, max=1.0, errorhandler=lambda x: 0.0 if x < 0.0 else 1.0
    )
    """
    Animation threshold allow you to change the tab indicator animation effect.

    :attr:`anim_threshold` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0.8`.
    """

    allow_stretch = BooleanProperty(True)
    """
    If False - tabs will not stretch to full screen.

    :attr:`allow_stretch` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    background_color = ColorProperty(None)
    """
    Background color of tabs in ``rgba`` format.

    :attr:`background_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_normal = ColorProperty(None)
    """
    Text color of the label when it is not selected.

    :attr:`text_color_normal` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    text_color_active = ColorProperty(None)
    """
    Text color of the label when it is selected.

    :attr:`text_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    elevation = NumericProperty(0)
    """
    Tab value elevation.

    .. seealso::

        `Behaviors/Elevation <https://kivymd.readthedocs.io/en/latest/behaviors/elevation/index.html>`_

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    indicator_color = ColorProperty(None)
    """
    Color indicator in ``rgba`` format.

    :attr:`indicator_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    lock_swiping = BooleanProperty(False)
    """
    If True - disable switching tabs by swipe.

    :attr:`lock_swiping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    font_name = StringProperty("Roboto")
    """
    Font name for tab text.

    :attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'Roboto'`.
    """

    ripple_duration = NumericProperty(2)
    """
    Ripple duration when long touching to tab.

    :attr:`ripple_duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2`.
    """

    no_ripple_effect = BooleanProperty(True)
    """
    Whether to use the ripple effect when tapping on a tab.

    :attr:`no_ripple_effect` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_tab_switch")
        self.register_event_type("on_ref_press")
        self.register_event_type("on_slide_progress")
        Clock.schedule_once(self._carousel_bind, 1)
        self.theme_cls.bind(primary_palette=self.update_icon_color)

    def update_icon_color(self, instance, value):
        for tab_label in self.get_tab_list():
            if not self.text_color_normal:
                tab_label.text_color_normal = self.specific_secondary_text_color
            if not self.text_color_active:
                tab_label.text_color_active = self.specific_text_color

    def switch_tab(self, name_tab):
        """Switching the tab by name."""

        for instance_tab in self.tab_bar.parent.carousel.slides:
            if instance_tab.text == name_tab:
                self.tab_bar.parent.carousel.load_slide(instance_tab)
                break
        for tab_label in self.get_tab_list():
            if name_tab == tab_label.text:
                self.ids.scrollview.scroll_to(tab_label)
                break

    def get_tab_list(self):
        """Returns a list of tab objects."""

        return self.tab_bar.layout.children

    def add_widget(self, widget, index=0, canvas=None):
        # You can add only subclass of MDTabsBase.
        if len(self.children) >= 2:
            try:
                # FIXME: Can't set the value of the `no_ripple_effect`
                #  and `ripple_duration` properties for widget.tab_label.
                widget.tab_label._no_ripple_effect = self.no_ripple_effect
                widget.tab_label.ripple_duration_in_slow = self.ripple_duration
                widget.tab_label.group = str(self)
                widget.tab_label.tab_bar = self.tab_bar
                widget.tab_label.text_color_normal = (
                    self.text_color_normal
                    if self.text_color_normal
                    else self.specific_secondary_text_color
                )
                widget.tab_label.text_color_active = (
                    self.text_color_active
                    if self.text_color_active
                    else self.specific_text_color
                )
                self.bind(font_name=widget.tab_label.setter("font_name"))
                self.tab_bar.layout.add_widget(widget.tab_label)
                self.carousel.add_widget(widget)
                return
            except AttributeError:
                pass
        return super().add_widget(widget)

    def remove_widget(self, widget):
        # You can remove only subclass of MDTabsLabel.
        if not issubclass(widget.__class__, MDTabsLabel):
            raise MDTabsException(
                "MDTabs can remove only subclass of MDTabsLabel"
            )
        # The last tab is not deleted.
        if len(self.tab_bar.layout.children) == 1:
            return

        self.tab_bar.layout.remove_widget(widget)

        for tab in self.carousel.slides:
            if tab.text == widget.text:
                self.carousel.remove_widget(tab)
                break

    def on_slide_progress(self, *args):
        """Called while the slide is scrolling."""

    def on_carousel_index(self, carousel, index):
        """Called when the carousel index changes."""

        # When the index of the carousel change, update tab indicator,
        # select the current tab and reset threshold data.
        if carousel.current_slide:
            current_tab_label = carousel.current_slide.tab_label
            if current_tab_label.state == "normal":
                # current_tab_label._do_press()
                current_tab_label.dispatch("on_release")

            if self.tab_indicator_type == "round":
                self.tab_indicator_height = self.tab_bar_height
                if index == 0:
                    radius = [
                        0,
                        self.tab_bar_height / 2,
                        self.tab_bar_height / 2,
                        0,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
                elif index == len(self.get_tab_list()) - 1:
                    radius = [
                        self.tab_bar_height / 2,
                        0,
                        0,
                        self.tab_bar_height / 2,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
                else:
                    radius = [
                        self.tab_bar_height / 2,
                    ]
                    self.tab_bar.update_indicator(
                        current_tab_label.x, current_tab_label.width, radius
                    )
            elif (
                self.tab_indicator_type == "fill"
                or self.tab_indicator_type == "line-round"
                or self.tab_indicator_type == "line-rect"
            ):
                self.tab_indicator_height = self.tab_bar_height
                self.tab_bar.update_indicator(
                    current_tab_label.x, current_tab_label.width
                )
            else:
                self.tab_bar.update_indicator(
                    current_tab_label.x, current_tab_label.width
                )

    def on_ref_press(self, *args):
        """The method will be called when the ``on_ref_press`` event
        occurs when you, for example, use markup text for tabs."""

    def on_tab_switch(self, *args):
        """Called when switching tabs."""

    def on_size(self, *args):
        if self.carousel.current_slide:
            self._update_indicator(self.carousel.current_slide.tab_label)

    def _carousel_bind(self, i):
        self.carousel.bind(on_slide_progress=self._on_slide_progress)

    def _on_slide_progress(self, *args):
        self.dispatch("on_slide_progress", args)

    def _update_indicator(self, current_tab_label):
        if not current_tab_label:
            current_tab_label = self.tab_bar.layout.children[-1]
        self.tab_bar.update_indicator(
            current_tab_label.x, current_tab_label.width
        )
