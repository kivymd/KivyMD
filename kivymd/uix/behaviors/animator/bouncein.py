from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = (
    "BounceInAnimator",
    "BounceInDownAnimator",
    "BounceInLeftAnimator",
    "BounceInRightAnimator",
    "BounceInUpAnimator",
)


class BounceInAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity"]

        vals = [
            self._original["height"] * 0.3,
            self._original["width"] * 0.3,
            0,
        ]
        self._initialize(**dict(zip(props, vals)))

        vals = [
            self._original["height"] * 1.05,
            self._original["width"] * 1.05,
            1,
        ]
        anim = Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        vals = [
            self._original["height"] * 0.9,
            self._original["width"] * 0.9,
            1,
        ]
        anim += Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        anim += Animation(d=self.duration / 3, **self._original,)

        self._animate(anim)


class BounceInDownAnimator(Animator):
    def start_(self, tmp=None):
        props = ["pos_hint", "opacity"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val
        vals = [__tmp, 0]
        self._initialize(**dict(zip(props, vals)))

        __tmp = {}
        for _key, _val in self._original["pos_hint"].items():
            if _key in ["center_y", "y", "top"]:
                __tmp[_key] = _val - 0.04
            else:
                __tmp[_key] = _val

        vals = [__tmp, 1]
        anim = Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.02
            else:
                __tmp[key] = val
        vals = [__tmp, 1]

        anim += Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        anim += Animation(d=self.duration / 3, **self._original,)

        self._animate(anim)


class BounceInLeftAnimator(Animator):
    def start_(self, tmp=None):
        props = ["pos_hint", "opacity"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val
        vals = [__tmp, 0]
        self._initialize(**dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.04
            else:
                __tmp[key] = val
        vals = [__tmp, 1]

        anim = Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.02
            else:
                __tmp[key] = val
        vals = [__tmp, 1]

        anim += Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        anim += Animation(d=self.duration / 3, **self._original,)

        self._animate(anim)


class BounceInRightAnimator(Animator):
    def start_(self, tmp=None):
        props = ["pos_hint", "opacity"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.2
            else:
                __tmp[key] = val
        vals = [__tmp, 0]
        self._initialize(**dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.04
            else:
                __tmp[key] = val
        vals = [__tmp, 1]

        anim = Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.02
            else:
                __tmp[key] = val
        vals = [__tmp, 1]
        anim += Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        anim += Animation(d=self.duration / 3, **self._original,)

        self._animate(anim)


class BounceInUpAnimator(Animator):
    def start_(self, tmp=None):
        props = ["pos_hint", "opacity"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val - 0.2
            else:
                __tmp[key] = val
        vals = [__tmp, 0]
        self._initialize(**dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.04
            else:
                __tmp[key] = val
        vals = [__tmp, 1]

        anim = Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val - 0.02
            else:
                __tmp[key] = val
        vals = [__tmp, 1]
        anim += Animation(d=self.duration / 3, **dict(zip(props, vals)),)

        anim += Animation(d=self.duration / 3, **self._original,)

        self._animate(anim)
