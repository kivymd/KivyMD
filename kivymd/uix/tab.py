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
--------------------

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
            id: android_tabs
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
                self.root.ids.android_tabs.add_widget(Tab(text=name_tab))

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
            id: android_tabs
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
                self.root.ids.android_tabs.add_widget(Tab(text=f"Tab {i}"))

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
"""
from kivymd.uix.boxlayout import MDBoxLayout

__all__ = (
    "MDTabs",
    "MDTabsBase",
)

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle
from kivy.utils import boundary
from kivy.properties import (
    ObjectProperty,
    NumericProperty,
    StringProperty,
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ListProperty,
)

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.icon_definitions import md_icons
from kivymd import fonts_path

Builder.load_string(
    """
#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect


<MDTabsLabel>
    size_hint: None, 1
    halign: 'center'
    padding: '12dp', 0
    group: 'tabs'
    allow_no_selection: False
    markup: True
    on_ref_press: if root.callback: root.callback(self)
    text_color_normal:
        (\
        (0, 0, 0, .5) \
        if app.theme_cls.theme_style == 'Dark' and not self.text_color_normal \
        else (1, 1, 1, .6) \
        if app.theme_cls.theme_style == 'White' and not self.text_color_normal \
        else self.text_color_normal \
        )
    text_color_active:
        (\
        (0, 0, 0, .75) \
        if app.theme_cls.theme_style == 'Dark' and not self.text_color_active \
        else (1, 1, 1, 1) \
        if app.theme_cls.theme_style == 'White' and not self.text_color_normal \
        else self.text_color_active
        )
    color:
        self.text_color_active if self.state == 'down' \
        else self.text_color_normal
    on_x: self._trigger_update_tab_indicator()
    on_width: self._trigger_update_tab_indicator()


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

    MDTabsMain:
        padding: 0, tab_bar.height, 0, 0

        MDTabsCarousel:
            id: carousel
            anim_move_duration: root.anim_duration
            on_index: root.on_carousel_index(*args)
            on__offset: tab_bar.android_animation(*args)
            on_slides: self.index = root.default_tab
            on_slides: root.on_carousel_index(self, 0)

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

                canvas.after:
                    Color:
                        rgba: root.theme_cls.accent_color if not root.color_indicator else root.color_indicator
                    Rectangle:
                        pos: self.pos
                        size: 0, root.tab_indicator_height
"""
)


class MDTabsException(Exception):
    pass


class MDTabsLabel(ToggleButtonBehavior, Label):
    """This class it represent the label of each tab."""

    text_color_normal = ListProperty()
    text_color_active = ListProperty()
    tab = ObjectProperty()
    tab_bar = ObjectProperty()
    callback = ObjectProperty()

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

    def _trigger_update_tab_indicator(self):
        # update the position and size of the indicator
        # when the label changes size or position
        if self.state == "down":
            self.tab_bar.update_indicator(self.x, self.width)


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


class MDTabsCarousel(Carousel):
    pass


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
    He is also responsible for resizing the tab shortcut when necessary.
    """

    target = ObjectProperty(None, allownone=True)
    """
    Is the carousel reference of the next tab / slide.
    When you go from `'Tab A'` to `'Tab B'`, `'Tab B'` will be the
    target tab / slide of the carousel.

    :attr:`target` is an :class:`~kivy.properties.ObjectProperty`
    and default to `None`.
    """

    def get_rect_instruction(self):
        for i in self.layout.canvas.after.children:
            if isinstance(i, Rectangle):
                return i

    indicator = AliasProperty(get_rect_instruction, cache=True)
    """
    Is the Rectangle instruction reference of the tab indicator.

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

    def update_indicator(self, x, w):
        # update position and size of the indicator
        self.indicator.pos = (x, 0)
        self.indicator.size = (w, self.indicator.size[1])

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


class MDTabs(ThemableBehavior, AnchorLayout):
    """
    You can use this class to create your own tabbed panel..

    :Events:
        `on_tab_switch`
            Called when switching tabs.
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

    background_color = ListProperty()
    """
    Background color of tabs in ``rgba`` format.

    :attr:`background_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    text_color_normal = ListProperty()
    """
    Text color of the label when it is not selected.

    :attr:`text_color_normal` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    text_color_active = ListProperty()
    """
    Text color of the label when it is selected.

    :attr:`text_color_active` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    elevation = NumericProperty(0)
    """
    Tab value elevation.

    .. seealso::

        `Behaviors/Elevation <https://kivymd.readthedocs.io/en/latest/behaviors/elevation/index.html>`_

    :attr:`elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    color_indicator = ListProperty()
    """
    Color indicator in ``rgba`` format.

    :attr:`color_indicator` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    callback = ObjectProperty()
    """
    User callback. The method will be called when the ``on_ref_press`` event
    occurs in the :class:`~MDTabsLabel` class.

    :attr:`callback` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_tab_switch")

    def on_tab_switch(self, *args):
        """Called when switching tabs."""

    def on_carousel_index(self, carousel, index):
        # when the index of the carousel change, update
        # tab indicator, select the current tab and reset threshold data.
        current_tab_label = carousel.current_slide.tab_label
        if current_tab_label.state == "normal":
            current_tab_label._do_press()
        self.tab_bar.update_indicator(
            current_tab_label.x, current_tab_label.width
        )

    def add_widget(self, widget, index=0, canvas=None):
        # You can add only subclass of MDTabsBase.
        if len(self.children) >= 2:
            try:
                self.background_color = (
                    self.background_color
                    if self.background_color
                    else self.theme_cls.primary_color
                )
                self.text_color_normal = (
                    self.text_color_normal
                    if self.text_color_normal
                    else self.theme_cls.text_color
                )
                self.text_color_active = (
                    self.text_color_active
                    if self.text_color_active
                    else self.theme_cls.bg_dark
                )
                widget.tab_label.callback = self.callback
                widget.tab_label.tab_bar = self.tab_bar
                widget.tab_label.text_color_normal = self.text_color_normal
                widget.tab_label.text_color_active = self.text_color_active
                self.tab_bar.layout.add_widget(widget.tab_label)
                self.carousel.add_widget(widget)
                return
            except AttributeError:
                pass
        return super().add_widget(widget)

    def remove_widget(self, widget):
        # You can remove only subclass of MDTabsBase.
        if not issubclass(widget.__class__, MDTabsBase):
            raise MDTabsException(
                "MDTabs can remove only subclass of MDTabBase"
            )
        if widget.parent.parent == self.carousel:
            self.tab_bar.layout.remove_widget(widget.tab_label)
            self.carousel.remove_widget(widget)
