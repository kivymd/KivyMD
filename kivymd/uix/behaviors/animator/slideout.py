from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = (
    "SlideOutDownAnimator",
    "SlideOutLeftAnimator",
    "SlideOutRightAnimator",
    "SlideOutUpAnimator",
)


class SlideOutDownAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = -0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class SlideOutLeftAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = -0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class SlideOutRightAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = 1.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class SlideOutUpAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = 1.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)
