"""
Components/Carousel
=====================

:class:`~kivy.uix.boxlayout.Carousel` class equivalent. Simplifies working
with some widget properties. For example:


Carousel
---------

.. code-block:: python

    kv='''
        YourCarousel:
            BoxLayout:
                [...]
            BoxLayout:
                [...]
            BoxLayout:
                [...]
    '''
    builder.load_string(kv)

    class YourCarousel(Carousel):
        def __init__(self,*kwargs):
            self.register_event_type("on_slide_progress")
            self.register_event_type("on_slide_complete")

        def on_touch_down(self, *args):
            ["Code to detect when the slide changes"]

        def on_touch_up(self, *args):
            ["Code to detect when the slide changes"]

        def Calculate_slide_pos(self, *args):
            ["Code to calculate the current position of the slide"]

        def do_custom_animation(self, *args)
            ["Code to recreate an animation"]


MDCarousel
-----------

.. code-block:: kv

    MDCarousel:
        on_slide_progress:
            do_something()
        on_slide_complete:
            do_something()

"""
# TODO: Add documentation.

from kivy.animation import Animation
from kivy.uix.carousel import Carousel


class MDCarousel(Carousel):
    """
    based on kivy's carousel.

    .. seealso::
        `kivy.uix.carousel.Carousel <https://kivy.org/doc/stable/api-kivy.uix.carousel.html>`_
    """

    _scrolling = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_slide_progress")
        self.register_event_type("on_slide_complete")

    def on_slide_progress(self, *args):
        """
        Event launched when the Slide animation is progress.
        rememebr to bind and unbid to this method.
        """
        pass

    def on_slide_complete(self, *args):
        """
        Event launched when the Slide animation is complete.
        rememebr to bind and unbid to this method.
        """
        pass

    def _position_visible_slides(self, *args):
        slides, index = self.slides, self.index
        no_of_slides = len(slides) - 1
        if not slides:
            return
        x, y, width, height = self.x, self.y, self.width, self.height
        _offset, direction = self._offset, self.direction
        _prev, _next, _current = self._prev, self._next, self._current
        get_slide_container = self.get_slide_container
        last_slide = get_slide_container(slides[-1])
        first_slide = get_slide_container(slides[0])
        skip_next = False
        _loop = self.loop

        if direction[0] in ["r", "l"]:
            xoff = x + _offset
            x_prev = {"l": xoff + width, "r": xoff - width}
            x_next = {"l": xoff - width, "r": xoff + width}
            if _prev:
                _prev.pos = (x_prev[direction[0]], y)
            elif _loop and _next and index == 0:
                if (_offset > 0 and direction[0] == "r") or (
                    _offset < 0 and direction[0] == "l"
                ):
                    last_slide.pos = (x_prev[direction[0]], y)
                    skip_next = True
            if _current:
                _current.pos = (xoff, y)

                if self._scrolling:
                    self.dispatch("on_slide_progress", (xoff, y))

            if skip_next:
                return
            if _next:
                _next.pos = (x_next[direction[0]], y)
            elif _loop and _prev and index == no_of_slides:
                if (_offset < 0 and direction[0] == "r") or (
                    _offset > 0 and direction[0] == "l"
                ):
                    first_slide.pos = (x_next[direction[0]], y)
        if direction[0] in ["t", "b"]:
            yoff = y + _offset
            y_prev = {"t": yoff - height, "b": yoff + height}
            y_next = {"t": yoff + height, "b": yoff - height}
            if _prev:
                _prev.pos = (x, y_prev[direction[0]])
            elif _loop and _next and index == 0:
                if (_offset > 0 and direction[0] == "t") or (
                    _offset < 0 and direction[0] == "b"
                ):
                    last_slide.pos = (x, y_prev[direction[0]])
                    skip_next = True
            if _current:
                _current.pos = (x, yoff)
            if skip_next:
                return
            if _next:
                _next.pos = (x, y_next[direction[0]])
            elif _loop and _prev and index == no_of_slides:
                if (_offset < 0 and direction[0] == "t") or (
                    _offset > 0 and direction[0] == "b"
                ):
                    first_slide.pos = (x, y_next[direction[0]])

    def on_touch_down(self, touch):
        self._scrolling = True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self._scrolling = False
        return super().on_touch_up(touch)

    def _start_animation(self, *args, **kwargs):
        # compute target offset for ease back, next or prev
        new_offset = 0
        direction = kwargs.get("direction", self.direction)[0]
        is_horizontal = direction in "rl"
        extent = self.width if is_horizontal else self.height
        min_move = kwargs.get("min_move", self.min_move)
        _offset = kwargs.get("offset", self._offset)

        if _offset < min_move * -extent:
            new_offset = -extent
        elif _offset > min_move * extent:
            new_offset = extent

        # if new_offset is 0, it wasnt enough to go next/prev
        dur = self.anim_move_duration
        if new_offset == 0:
            dur = self.anim_cancel_duration

        # detect edge cases if not looping
        len_slides = len(self.slides)
        index = self.index
        if not self.loop or len_slides == 1:
            is_first = index == 0
            is_last = index == len_slides - 1
            if direction in "rt":
                towards_prev = new_offset > 0
                towards_next = new_offset < 0
            else:
                towards_prev = new_offset < 0
                towards_next = new_offset > 0
            if (is_first and towards_prev) or (is_last and towards_next):
                new_offset = 0

        anim = Animation(_offset=new_offset, d=dur, t=self.anim_type)
        anim.cancel_all(self)

        def _cmp(*args):
            self.dispatch(
                "on_slide_complete",
                self.previous_slide,
                self.current_slide,
                self.next_slide,
            )
            if self._skip_slide is not None:
                self.index = self._skip_slide
                self._skip_slide = None

        anim.bind(on_complete=_cmp)
        anim.start(self)
