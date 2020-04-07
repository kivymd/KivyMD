from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = (
    "FadeInAnimator",
    "FadeInDownAnimator",
    "FadeInLeftAnimator",
    "FadeInRightAnimator",
    "FadeInUpAnimator",
)


class FadeInAnimator(Animator):
    def start_(self, tmp=None):
        props = [
            "opacity",
        ]
        vals = [
            0,
        ]
        self._initialize(**dict(zip(props, vals)))

        vals = [
            1,
        ]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeInDownAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        self._initialize(**dict(zip(props, vals)))

        vals = [1, self._original["pos_hint"]]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeInLeftAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        self._initialize(**dict(zip(props, vals)))

        vals = [1, self._original["pos_hint"]]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeInRightAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        self._initialize(**dict(zip(props, vals)))

        vals = [1, self._original["pos_hint"]]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)


class FadeInUpAnimator(Animator):
    def start_(self, tmp=None):
        props = ["opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val

        vals = [0, __tmp]
        self._initialize(**dict(zip(props, vals)))

        vals = [1, self._original["pos_hint"]]
        anim = Animation(d=self.duration, **dict(zip(props, vals)),)

        self._animate(anim)
