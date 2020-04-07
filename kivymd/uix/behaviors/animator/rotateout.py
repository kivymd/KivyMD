from kivy.animation import Animation
from functools import partial

from base import Animator

__all__ = (
    "RotateOutAnimator",
    "RotateOutDownLeftAnimator",
    "RotateOutDownRightAnimator",
    "RotateOutUpLeftAnimator",
    "RotateOutUpRightAnimator",
)


class RotateOutAnimator(Animator):
    def start_(self, tmp=None):
        props = ["angle", "opacity"]

        vals = [-200, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)


class RotateOutDownLeftAnimator(Animator):
    def start_(self, tmp=None):
        pivot = (self.widget.x - self.widget.width / 2, self.widget.y)
        self.widget.origin_ = pivot

        props = ["angle", "opacity"]
        vals = [-90, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)


class RotateOutDownRightAnimator(Animator):
    def start_(self, tmp=None):
        pivot = (self.widget.x + 3 * self.widget.width / 2, self.widget.y)
        self.widget.origin_ = pivot

        props = ["angle", "opacity"]
        vals = [90, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)


class RotateOutUpLeftAnimator(Animator):
    def start_(self, tmp=None):
        pivot = (self.widget.x - self.widget.width / 2, self.widget.y)
        self.widget.origin_ = pivot

        props = ["angle", "opacity"]
        vals = [90, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)


class RotateOutUpRightAnimator(Animator):
    def start_(self, tmp=None):
        pivot = (self.widget.x + 3 * self.widget.width / 2, self.widget.y)
        self.widget.origin_ = pivot

        props = ["angle", "opacity"]
        vals = [-90, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)
