from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = (
    "FadeOutAnimator",
    "FadeOutDownAnimator",
    "FadeOutLeftAnimator",
    "FadeOutRightAnimator",
    "FadeOutUpAnimator",
)


class FadeOutAnimator(Animator):
    def start_(self, tmp=None):
        props = [
            "opacity",
        ]
        vals = [
            1,
        ]
        self._initialize(**dict(zip(props, vals)))

        vals = [
            0,
        ]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeOutDownAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeOutLeftAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeOutRightAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeOutUpAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)
