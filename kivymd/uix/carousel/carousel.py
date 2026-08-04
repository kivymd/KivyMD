"""
Components/Carousel
===================

.. versionadded:: 2.0.0

.. seealso::

    `Material Design spec, Carousel <https://m3.material.io/components/carousel/overview>`_

.. rubric:: Carousels show a collection of items that can be scrolled on and
    off the screen.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-preview.png
    :align: center

- Contain visual items like images or video, along with optional label text
- Six layouts: Multi-browse, uncontained,  uncontained multi-aspect ratio, hero, center-aligned hero and full-screen
- Layouts can be start-aligned or center-aligned
- Item visuals have a parallax effect when scrolled
- Items change size as they move through the carousel

Usage
-----

.. tabs::

    .. tab:: Imperative python style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.carousel import MDCarouselItem
            from kivymd.uix.fitimage import FitImage


            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDCarousel:
                    id: carousel
                    layouts: "multi-browse"
            '''


            class ExampleApp(MDApp):
                def on_start(self):
                    for i in range(1, 20):
                        carousel_item = MDCarouselItem()
                        image = FitImage(
                            source=f"https://picsum.photos/800/600?random={i}",
                            radius=[dp(28)],
                        )

                        carousel_item.add_widget(image)
                        self.root.ids.carousel.add_widget(carousel_item)

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    return Builder.load_string(KV)


            if __name__ == "__main__":
                ExampleApp().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.carousel import MDCarousel, MDCarouselItem
            from kivymd.uix.fitimage import FitImage
            from kivymd.uix.screen import MDScreen


            class MyCarousel(MDCarousel):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    images = [
                        f"https://picsum.photos/800/600?random={i}" for i in range(1, 20)
                    ]
                    self.widgets = [
                        MDCarouselItem(
                            FitImage(source=img_url, radius=[dp(28)])
                        ) for img_url in images
                    ]


            class ExampleApp(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"

                    return MDScreen(
                        MyCarousel(
                            layouts="multi-browse",
                        ),
                        md_bg_color=self.theme_cls.backgroundColor,
                    )


            if __name__ == "__main__":
                ExampleApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-usage.gif
    :align: center

Anatomy
-------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-anatomy.png
    :align: center
"""

import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics.stencil_instructions import (
    StencilPop,
    StencilPush,
    StencilUse,
)
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    VariableListProperty,
)

from kivymd import uix_path
from kivymd.uix.card import MDCard
from kivymd.uix.widget import MDWidget

with open(
    os.path.join(uix_path, "carousel", "carousel.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())

__all__ = (
    "MDCarouselItem",
    "MDCarousel",
)


class MDCarouselItem(MDCard):
    """
    Implements a item for :class:`~MDCarousel` class.

    For more information, see in the :class:`~kivymd.uix.card.MDCard`
    class documentation.

    :Events:
        `on_slide_left`
            Fired when user slides/swipes to the left.

        `on_slide_right`
            Fired when user slides/swipes to the right.

        `on_slide_up`
            Fired when user slides/swipes up.

        `on_slide_down`
            Fired when user slides/swipes down.

        `on_index`
            Fired when the active slide index changes.
    """

    full_screen_radius = NumericProperty(dp(16))
    """
    Corner radius used during scrolling for items in full-screen layout modes.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-full-screen-radius.png
        :align: center

    :attr:`full_screen_radius` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `dp(16)`.
    """

    radius = VariableListProperty([dp(28), dp(28), dp(28), dp(28)])
    """
    Item radius by default.

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-radius.png
        :align: center

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(28), dp(28), dp(28), dp(28)]`.
    """

    def add_widget(self, widget, index=0, canvas=None):
        if hasattr(widget, "radius"):
            widget.radius = self.radius

        return super().add_widget(widget, index, canvas)


class MDCarousel(MDWidget):
    """
    Implements a custom Material Design 3 carousel.

    For more information, see in the :class:`~kivymd.uix.widget.MDWidget`
    class documentation.
    """

    padding = ListProperty([dp(16), dp(16), dp(16), dp(16)])
    """
    Padding of the carousel view in the format ``[left, top, right, bottom]``.

    :attr:`padding` is an :class:`~kivy.properties.ListProperty`
    and defaults to ``[dp(16), dp(16), dp(16), dp(16)]``.
    """

    spacing = NumericProperty(dp(12))
    """
    Distance between items in the carousel.

    :attr:`spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to ``dp(12)``.
    """

    shrink_extent = NumericProperty(dp(56))
    """
    Size of the collapsed or shrinked extent for trailing items.

    :attr:`shrink_extent` is an :class:`~kivy.properties.NumericProperty`
    and defaults to ``dp(56)``.
    """

    item_snapping = BooleanProperty(True)
    """
    If ``True``, enables automatic snapping of items to the closest slot upon touch release.

    :attr:`item_snapping` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to ``True``.
    """

    scroll_offset = NumericProperty(0)
    """
    Current scroll offset value of the carousel.

    :attr:`scroll_offset` is an :class:`~kivy.properties.NumericProperty`
    and defaults to ``0``.
    """

    layouts = OptionProperty(
        "multi-browse",
        options=[
            "multi-browse",
            "uncontained",
            "hero",
            "center-aligned",
            "full-screen-horizontal",
            "full-screen-vertical",
        ],
    )
    """
    Layout type of the carousel view.

    Available options are:
    - ``"multi-browse"``: Standard layout displaying multiple items of varying sizes.
    - ``"uncontained"``: Items maintain a fixed width and overflow beyond the carousel edge.
    - ``"hero"``: Highlights a single large hero item aligned to the start.
    - ``"center-aligned"``: Displays a centered hero item flanked by smaller preview items.
    - ``"full-screen-horizontal"``: Items occupy the full width and height of the carousel, scrolling horizontally.
    - ``"full-screen-vertical"``: Items occupy the full width and height of the carousel, scrolling vertically.

    :attr:`layouts` is an :class:`~kivy.properties.OptionProperty`
    and defaults to ``"multi-browse"``.

    Multi-browse
    ------------

    .. code-block:: kv

        MDCarousel:
            layouts: "multi-browse"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-usage.gif
        :align: center

    Uncontained
    -----------

    .. code-block:: kv

        MDCarousel:
            layouts: "uncontained"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-uncontained.gif
        :align: center

    Hero
    ----

    .. code-block:: kv

        MDCarousel:
            layouts: "hero"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-hero.gif
        :align: center

    Center-aligned
    --------------

    .. code-block:: kv

        MDCarousel:
            layouts: "center-aligned"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-center-aligned.gif
        :align: center

    Full-screen-vertical
    ----------------------

    .. code-block:: kv

        MDCarousel:
            layouts: "full-screen-vertical"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-full-screen-vertical.gif
        :align: center
        :scale: 50%

    Full-screen-horizontal
    ----------------------

    .. code-block:: kv

        MDCarousel:
            layouts: "full-screen-horizontal"

    .. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/carousel-full-screen-horizontal.gif
        :align: center
        :scale: 50%
    """

    uncontained_item_width = NumericProperty(dp(280))
    """
    Width of individual items when using the ``"uncontained"`` layout mode.

    :attr:`uncontained_item_width` is an :class:`~kivy.properties.NumericProperty`
    and defaults to ``dp(280)``.
    """

    index = NumericProperty(0)
    """
    Index of the currently active item.

    :attr:`index` is an :class:`~kivy.properties.NumericProperty`
    and defaults to ``0``.
    """

    __events__ = (
        "on_slide_left",
        "on_slide_right",
        "on_slide_up",
        "on_slide_down",
    )

    def __init__(self, **kwargs):
        self._items = []
        self._touch_start_pos = 0
        self._touch_start_offset = 0
        self._anim = None

        super().__init__(**kwargs)

        with self.canvas.before:
            StencilPush()
            self._stencil_rect = Rectangle(pos=self.pos, size=self.size)
            StencilUse()

        with self.canvas.after:
            StencilPop()

        self.bind(
            size=self._update_stencil_and_layout,
            pos=self._update_stencil_and_layout,
            scroll_offset=self._apply_layout,
            layouts=self._apply_layout,
        )

    def _update_stencil_and_layout(self, *args):
        # For full-screen modes, we disable padding to avoid gaps.
        if self.layouts in ("full-screen-horizontal", "full-screen-vertical"):
            crop_x, crop_y = self.x, self.y
            crop_w, crop_h = max(0, self.width), max(0, self.height)
        elif self.layouts == "uncontained":
            pad_t = self.padding[1]
            pad_b = (
                self.padding[3] if len(self.padding) >= 4 else self.padding[1]
            )

            # Stencil from the VERY EDGE of the widget (self.x) to the right
            # edge (self.width). Nothing is clipped on the left; the card is
            # only clipped when overflowing the window.
            crop_x = self.x
            crop_y = self.y + pad_b
            crop_w = max(0, self.width)
            crop_h = max(0, self.height - pad_t - pad_b)
        else:
            pad_l = self.padding[0]
            pad_r = (
                self.padding[2] if len(self.padding) >= 3 else self.padding[0]
            )
            pad_t = self.padding[1]
            pad_b = (
                self.padding[3] if len(self.padding) >= 4 else self.padding[1]
            )

            crop_x = self.x + pad_l
            crop_y = self.y + pad_b
            crop_w = max(0, self.width - pad_l - pad_r)
            crop_h = max(0, self.height - pad_t - pad_b)

        self._stencil_rect.pos = (crop_x, crop_y)
        self._stencil_rect.size = (crop_w, crop_h)

        self._apply_layout()

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, MDCarouselItem):
            item = widget
        else:
            item = MDCarouselItem()
            item.add_widget(widget)

        self._items.append(item)
        super().add_widget(item, index, canvas)
        Clock.schedule_once(self._apply_layout, 0)

    def _update_index_from_scroll(self):
        """Updates the active index property based on current scroll offset."""

        step = self._get_step_size()

        if step > 0:
            new_index = int(round(self.scroll_offset / step))
            new_index = max(0, min(len(self._items) - 1, new_index))

            if self.index != new_index:
                self.index = new_index

    def _get_available_width(self):
        """
        Returns the layout area width available for rendering items after
        applying horizontal padding.
        """

        if self.layouts in ("full-screen-horizontal", "full-screen-vertical"):
            return max(0, self.width)

        pad_l = self.padding[0]
        pad_r = self.padding[2] if len(self.padding) >= 3 else self.padding[0]

        return max(0, self.width - pad_l - pad_r)

    def _get_available_height(self):
        """
        Returns the layout area height available for rendering items after
        applying vertical padding.
        """

        if self.layouts in ("full-screen-horizontal", "full-screen-vertical"):
            return max(0, self.height)

        pad_t = self.padding[1]
        pad_b = self.padding[3] if len(self.padding) >= 4 else self.padding[1]
        return max(0, self.height - pad_t - pad_b)

    def _get_medium_width(self):
        """Calculates the width of medium-sized preview items."""

        return max(dp(70), self._get_available_width() * 0.20)

    def _get_hero_large_width(self):
        """
        Calculates the width of the primary large item in the "hero" layout.
        """

        avail_w = self._get_available_width()
        small_w = self.shrink_extent
        sp = self.spacing
        hero_w = avail_w - small_w - sp

        return max(dp(150), hero_w)

    def _get_center_hero_large_width(self):
        """
        Calculates the width of the main center item in the "center-aligned"
        layout.
        """

        avail_w = self._get_available_width()
        small_w = self.shrink_extent
        sp = self.spacing
        hero_w = avail_w - 2 * small_w - 2 * sp

        return max(dp(120), hero_w)

    def _get_large_width(self):
        """
        Calculates the width of the primary large item in the "multi-browse"
        layout.
        """

        avail_w = self._get_available_width()
        sp = self.spacing
        med_w = self._get_medium_width()
        small_w = self.shrink_extent
        large_w = avail_w - med_w - small_w - (sp * 2)

        return max(dp(150), large_w)

    def _get_step_size(self):
        """
        Returns the distance offset required to advance to the next item slot
        based on the active layout.
        """

        if self.layouts == "uncontained":
            return self.uncontained_item_width + self.spacing
        elif self.layouts == "hero":
            return self._get_hero_large_width() + self.spacing
        elif self.layouts == "center-aligned":
            return self._get_center_hero_large_width() + self.spacing
        elif self.layouts == "full-screen-horizontal":
            return self._get_available_width() + self.spacing
        elif self.layouts == "full-screen-vertical":
            return self._get_available_height() + self.spacing

        return self._get_large_width() + self.spacing

    def _get_max_scroll(self):
        """
        Computes the maximum allowable scroll offset for the total number of
        items.
        """

        if not self._items or self.width <= 0 or self.height <= 0:
            return 0

        if self.layouts == "uncontained":
            total_items_width = (
                len(self._items) * self.uncontained_item_width
                + (len(self._items) - 1) * self.spacing
            )
            max_s = total_items_width - self._get_available_width()

            return max(0.0, max_s)

        return max(0.0, (len(self._items) - 1) * self._get_step_size())

    def _apply_layout(self, *args):
        """
        Positions, resizes, and manages opacity for all carousel items
        according to the selected layout mode.
        """

        if not self._items or self.width <= 0 or self.height <= 0:
            return

        self._update_index_from_scroll()

        num_items = len(self._items)
        pad_v = self.padding[1] + (
            self.padding[3] if len(self.padding) >= 4 else self.padding[1]
        )
        item_h = max(0, self.height - pad_v)
        item_y = self.y + self.padding[1]
        start_x = self.x + self.padding[0]
        max_scroll = self._get_max_scroll()
        offset = max(0.0, min(float(max_scroll), float(self.scroll_offset)))

        # Full-Screen Vertical.
        if self.layouts == "full-screen-vertical":
            avail_w = self.width
            avail_h = self.height
            sp = self.spacing
            start_y = self.y
            start_x = self.x

            for i in range(num_items):
                item = self._items[i]
                y = start_y + i * (avail_h + sp) - offset
                x = start_x

                if y + avail_h < start_y or y > start_y + avail_h:
                    item.opacity = 0
                else:
                    item.opacity = 1

                # При скролле: 28dp на отошедших краях, 0dp на тех, что у границы
                top_r = (
                    item.full_screen_radius
                    if (y + avail_h < start_y + avail_h)
                    else 0
                )
                bottom_r = item.full_screen_radius if (y > start_y) else 0
                card_radius = [top_r, top_r, bottom_r, bottom_r]

                item.radius = card_radius
                item.md_bg_color = (0, 0, 0, 0)
                item.padding = [0, 0, 0, 0]

                item.size = (avail_w, avail_h)
                item.pos = (x, y)

                if item.children:
                    child = item.children[0]
                    child.size = (avail_w, avail_h)
                    child.pos = (x, y)
                    if hasattr(child, "radius"):
                        child.radius = card_radius

        # Full-Screen Horizontal.
        elif self.layouts == "full-screen-horizontal":
            avail_w = self.width
            avail_h = self.height
            sp = self.spacing
            start_x = self.x
            start_y = self.y

            for i in range(num_items):
                item = self._items[i]
                x = start_x + i * (avail_w + sp) - offset
                y = start_y

                if x + avail_w < start_x or x > start_x + avail_w:
                    item.opacity = 0
                else:
                    item.opacity = 1

                # When scrolling horizontally: round the left/right edges that
                # break away.
                left_r = item.full_screen_radius if (x > start_x) else 0
                right_r = (
                    item.full_screen_radius
                    if (x + avail_w < start_x + avail_w)
                    else 0
                )
                # Kivy radius: [top_left, top_right, bottom_right, bottom_left]
                card_radius = [left_r, right_r, right_r, left_r]

                item.radius = card_radius
                item.md_bg_color = (0, 0, 0, 0)
                item.padding = [0, 0, 0, 0]

                item.size = (avail_w, avail_h)
                item.pos = (x, y)

                if item.children:
                    child = item.children[0]
                    child.size = (avail_w, avail_h)
                    child.pos = (x, y)

                    if hasattr(child, "radius"):
                        child.radius = card_radius

        # Full-Screen Horizontal.
        elif self.layouts == "full-screen-horizontal":
            avail_w = self.width
            avail_h = self.height
            sp = self.spacing
            start_x = self.x
            start_y = self.y

            for i in range(num_items):
                item = self._items[i]
                x = start_x + i * (avail_w + sp) - offset
                y = start_y

                if x + avail_w < start_x or x > start_x + avail_w:
                    item.opacity = 0
                else:
                    item.opacity = 1

                left_r = item.full_screen_radius if (x > start_x) else 0
                right_r = (
                    item.full_screen_radius
                    if (x + avail_w < start_x + avail_w)
                    else 0
                )
                card_radius = [left_r, right_r, right_r, left_r]

                item.radius = card_radius
                item.md_bg_color = (0, 0, 0, 0)
                item.padding = [0, 0, 0, 0]

                item.size = (avail_w, avail_h)
                item.pos = (x, y)

                if item.children:
                    child = item.children[0]
                    child.size = (avail_w, avail_h)
                    child.pos = (x, y)

                    if hasattr(child, "radius"):
                        child.radius = card_radius

        # Uncontained.
        elif self.layouts == "uncontained":
            item_w = self.uncontained_item_width
            sp = self.spacing

            for i in range(num_items):
                item = self._items[i]
                x = start_x + i * (item_w + sp) - offset
                w = item_w

                # FIXME: If the right edge of the card has moved past start_x
                #  (into the left padding zone) or the left edge has moved past
                #  the right edge of the screen — hide it.
                if x + w <= start_x or x >= self.x + self.width:
                    opacity = 0
                else:
                    opacity = 1

                Animation(
                    opacity=opacity,
                    duration=1.25,
                    transition="easing_decelerated",
                ).start(item)

                # -------------------------------------------------------------

                item.size = (w, item_h)
                item.pos = (x, item_y)

                if item.children:
                    child = item.children[0]
                    child.size = (item_w, item_h)
                    child.pos = (x, item_y)

        # Hero.
        elif self.layouts == "hero":
            large_w = self._get_hero_large_width()
            small_w = self.shrink_extent
            sp = self.spacing

            step_size = self._get_step_size()
            idx = int(offset // step_size)
            p = (offset % step_size) / step_size if step_size > 0 else 0.0

            slot0_x = start_x
            slot1_x = slot0_x + large_w + sp
            offscreen_right_x = self.x + self.width + dp(100)

            for i in range(num_items):
                item = self._items[i]
                rel_i = i - idx

                if rel_i < 0:
                    w = small_w
                    shift_count = abs(rel_i) - 1 + p
                    x = slot0_x - sp - small_w - (small_w + sp) * shift_count
                elif rel_i == 0:
                    w = large_w - (large_w - small_w) * p
                    target_x = slot0_x - (small_w + sp)
                    x = slot0_x + (target_x - slot0_x) * p
                elif rel_i == 1:
                    w = small_w + (large_w - small_w) * p
                    x = slot1_x + (slot0_x - slot1_x) * p
                elif rel_i == 2:
                    w = small_w
                    x = offscreen_right_x + (slot1_x - offscreen_right_x) * p
                else:
                    w = small_w
                    x = offscreen_right_x + (small_w + sp) * (rel_i - 2)

                w = max(small_w, w)

                if x < slot0_x:
                    overflow = slot0_x - x
                    w = max(0, w - overflow)
                    x = slot0_x
                    item.opacity = 0 if w <= dp(2) else 1
                else:
                    item.opacity = 1

                item.size = (w, item_h)
                item.pos = (x, item_y)

                if item.children:
                    child = item.children[0]
                    child.size = (w, item_h)
                    child.pos = (x, item_y)

        # Center-Aligned (Hero centered).
        elif self.layouts == "center-aligned":
            large_w = self._get_center_hero_large_width()
            small_w = self.shrink_extent
            sp = self.spacing

            step_size = self._get_step_size()
            idx = int(offset // step_size)
            p = (offset % step_size) / step_size if step_size > 0 else 0.0

            slot_left_x = start_x
            slot_center_x = slot_left_x + small_w + sp
            slot_right_x = slot_center_x + large_w + sp

            for i in range(num_items):
                item = self._items[i]
                rel_i = i - idx

                if rel_i < -1:
                    w = small_w
                    shift_count = abs(rel_i) - 2 + p
                    x = (
                        slot_left_x
                        - sp
                        - small_w
                        - (small_w + sp) * shift_count
                    )
                elif rel_i == -1:
                    w = small_w
                    target_x = slot_left_x - sp - small_w
                    x = slot_left_x + (target_x - slot_left_x) * p
                elif rel_i == 0:
                    w = large_w - (large_w - small_w) * p
                    x = slot_center_x + (slot_left_x - slot_center_x) * p
                elif rel_i == 1:
                    w = small_w + (large_w - small_w) * p
                    x = slot_right_x + (slot_center_x - slot_right_x) * p
                elif rel_i == 2:
                    w = small_w
                    target_x = slot_right_x
                    start_off_x = self.x + self.width + dp(50)
                    x = start_off_x + (target_x - start_off_x) * p
                else:
                    w = small_w
                    start_off_x = self.x + self.width + dp(50)
                    x = start_off_x + (small_w + sp) * (rel_i - 2)

                w = max(small_w, w)

                if x < start_x:
                    overflow = start_x - x
                    w = max(0, w - overflow)
                    x = start_x
                    item.opacity = 0 if w <= dp(2) else 1
                else:
                    item.opacity = 1

                item.size = (w, item_h)
                item.pos = (x, item_y)

                if item.children:
                    child = item.children[0]
                    child.size = (w, item_h)
                    child.pos = (x, item_y)

        # Multi-browse (default).
        else:
            large_w = self._get_large_width()
            medium_w = self._get_medium_width()
            small_w = self.shrink_extent
            sp = self.spacing

            step_size = self._get_step_size()
            idx = int(offset // step_size)
            p = (offset % step_size) / step_size if step_size > 0 else 0.0

            slot0_x = start_x
            slot1_x = slot0_x + large_w + sp
            slot2_x = slot1_x + medium_w + sp
            offscreen_right_x = self.x + self.width + dp(100)

            for i in range(num_items):
                item = self._items[i]
                rel_i = i - idx

                if rel_i < 0:
                    w = small_w
                    shift_count = abs(rel_i) - 1 + p
                    x = slot0_x - sp - small_w - (small_w + sp) * shift_count
                elif rel_i == 0:
                    w = large_w - (large_w - small_w) * p
                    target_x = slot0_x - (small_w + sp)
                    x = slot0_x + (target_x - slot0_x) * p
                elif rel_i == 1:
                    w = medium_w + (large_w - medium_w) * p
                    x = slot1_x + (slot0_x - slot1_x) * p
                elif rel_i == 2:
                    w = small_w + (medium_w - small_w) * p
                    x = slot2_x + (slot1_x - slot2_x) * p
                elif rel_i == 3:
                    w = small_w
                    x = offscreen_right_x + (slot2_x - offscreen_right_x) * p
                else:
                    w = small_w
                    x = offscreen_right_x + (small_w + sp) * (rel_i - 3)

                w = max(small_w, w)

                if x < slot0_x:
                    overflow = slot0_x - x
                    w = max(0, w - overflow)
                    x = slot0_x
                    item.opacity = 0 if w <= dp(2) else 1
                else:
                    item.opacity = 1

                item.size = (w, item_h)
                item.pos = (x, item_y)

                if item.children:
                    child = item.children[0]
                    child.size = (w, item_h)
                    child.pos = (x, item_y)

    def _flatten_corners_on_stop(self, *args):
        """
        Animates the straightening of angles (to 0) upon stopping.
        Works ONLY for `full-screen-vertical` and `full-screen-horizontal`.
        """

        if self.layouts not in (
            "full-screen-vertical",
            "full-screen-horizontal",
        ):
            return

        if self.layouts == "full-screen-vertical":
            start_y = self.y
            avail_h = self.height

            for item in self._items:
                if item.opacity == 0:
                    continue

                y = item.y
                # If the edge aligns perfectly with the screen boundary,
                # set to 0; otherwise, 12dp.
                top_r = (
                    0
                    if abs((y + avail_h) - (start_y + avail_h)) < 2
                    else item.full_screen_radius
                )
                bottom_r = (
                    0 if abs(y - start_y) < 2 else item.full_screen_radius
                )

                target_radius = [top_r, top_r, bottom_r, bottom_r]

                if item.radius != target_radius:
                    anim = Animation(
                        radius=target_radius, d=0.2, t="easing_decelerated"
                    )
                    anim.start(item)

                    if item.children:
                        child = item.children[0]

                        if hasattr(child, "radius"):
                            anim_child = Animation(
                                radius=target_radius,
                                d=0.2,
                                t="easing_decelerated",
                            )
                            anim_child.start(child)

        elif self.layouts == "full-screen-horizontal":
            start_x = self.x
            avail_w = self.width

            for item in self._items:
                if item.opacity == 0:
                    continue

                x = item.x
                left_r = 0 if abs(x - start_x) < 2 else item.full_screen_radius
                right_r = (
                    0
                    if abs((x + avail_w) - (start_x + avail_w)) < 2
                    else item.full_screen_radius
                )

                target_radius = [left_r, right_r, right_r, left_r]

                if item.radius != target_radius:
                    anim = Animation(
                        radius=target_radius, d=0.2, t="easing_decelerated"
                    )
                    anim.start(item)

                    if item.children:
                        child = item.children[0]

                        if hasattr(child, "radius"):
                            anim_child = Animation(
                                radius=target_radius,
                                d=0.2,
                                t="easing_decelerated",
                            )
                            anim_child.start(child)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self._anim:
                self._anim.stop(self)
                self._anim = None

            if self.layouts == "full-screen-vertical":
                self._touch_start_pos = touch.y
            else:
                self._touch_start_pos = touch.x

            self._touch_start_offset = self.scroll_offset
            touch.grab(self)

            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if self.layouts == "full-screen-vertical":
                # Swiping up (touch.y increases) decreases the y-value relative
                # to the start, so we increase scroll_offset to scroll down the
                # feed.
                delta = self._touch_start_pos - touch.y
            else:
                delta = self._touch_start_pos - touch.x

            max_scroll = self._get_max_scroll()
            new_offset = self._touch_start_offset + delta
            self.scroll_offset = max(0.0, min(max_scroll, new_offset))

            return True

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            threshold = dp(10)

            if self.layouts == "full-screen-vertical":
                delta_y = touch.y - self._touch_start_pos
                if delta_y > threshold:
                    self.dispatch("on_slide_up")
                elif delta_y < -threshold:
                    self.dispatch("on_slide_down")
            else:
                delta_x = touch.x - self._touch_start_pos
                if delta_x > threshold:
                    self.dispatch("on_slide_right")
                elif delta_x < -threshold:
                    self.dispatch("on_slide_left")

            if self.item_snapping and self._items:
                step = self._get_step_size()
                max_scroll = self._get_max_scroll()

                if step > 0:
                    target_idx = round(self.scroll_offset / step)
                    target_offset = max(0.0, min(max_scroll, target_idx * step))

                    if self._anim:
                        self._anim.stop(self)

                    self._anim = Animation(
                        scroll_offset=target_offset,
                        duration=0.3,
                        transition="easing_decelerated",
                    )
                    # Once the fine-tuning animation is complete, smoothly
                    # straighten the corners.
                    self._anim.bind(on_complete=self._flatten_corners_on_stop)
                    self._anim.start(self)

                return True

            return super().on_touch_up(touch)

    def on_index(self, instance, value):
        """Fired when the active slide index changes."""

    def on_slide_left(self):
        """Fired when user slides/swipes to the left."""

    def on_slide_right(self):
        """Fired when user slides/swipes to the right."""

    def on_slide_up(self):
        """Fired when user slides/swipes up."""

    def on_slide_down(self):
        """Fired when user slides/swipes down."""
