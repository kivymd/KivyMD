"""An Effect to be used with ScrollView to prevent scrolling beyond
the bounds, but politely.

A ScrollView constructed with StiffScrollEffect,
eg. ScrollView(effect_cls=StiffScrollEffect), will get harder to
scroll as you get nearer to its edges. You can scroll all the way to
the edge if you want to, but it will take more finger-movement than
usual.

Unlike DampedScrollEffect, it is impossible to overscroll with
StiffScrollEffect. That means you cannot push the contents of the
ScrollView far enough to see what's beneath them. This is appropriate
if the ScrollView contains, eg., a background image, like a desktop
wallpaper. Overscrolling may give the impression that there is some
reason to overscroll, even if just to take a peek beneath, and that
impression may be misleading.

StiffScrollEffect was written by Zachary Spector. His other stuff is at:
https://github.com/LogicalDash/
He can be reached, and possibly hired, at:
zacharyspector@gmail.com

"""

from time import time

from kivy.animation import AnimationTransition
from kivy.effects.kinetic import KineticEffect
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget


class StiffScrollEffect(KineticEffect):
    drag_threshold = NumericProperty("20sp")
    """Minimum distance to travel before the movement is considered as a
    drag."""

    min = NumericProperty(0)
    """Minimum boundary to stop the scrolling at."""

    max = NumericProperty(0)
    """Maximum boundary to stop the scrolling at."""

    max_friction = NumericProperty(1)
    """How hard should it be to scroll, at the worst?"""

    body = NumericProperty(0.7)
    """Proportion of the range in which you can scroll unimpeded."""

    scroll = NumericProperty(0.0)
    """Computed value for scrolling"""

    transition_min = ObjectProperty(AnimationTransition.in_cubic)
    """The AnimationTransition function to use when adjusting the friction
    near the minimum end of the effect.

    """

    transition_max = ObjectProperty(AnimationTransition.in_cubic)
    """The AnimationTransition function to use when adjusting the friction
    near the maximum end of the effect.

    """

    target_widget = ObjectProperty(None, allownone=True, baseclass=Widget)
    """The widget to apply the effect to."""

    displacement = NumericProperty(0)
    """The absolute distance moved in either direction."""

    scroll = NumericProperty(0.0)
    """The distance to be used for scrolling."""

    def __init__(self, **kwargs):
        """Set ``self.base_friction`` to the value of ``self.friction`` just
        after instantiation, so that I can reset to that value later.

        """

        super().__init__(**kwargs)
        self.base_friction = self.friction

    def update_velocity(self, dt):
        """Before actually updating my velocity, meddle with ``self.friction``
        to make it appropriate to where I'm at, currently.

        """

        hard_min = self.min
        hard_max = self.max
        if hard_min > hard_max:
            hard_min, hard_max = hard_max, hard_min

        margin = (1.0 - self.body) * (hard_max - hard_min)
        soft_min = hard_min + margin
        soft_max = hard_max - margin

        if self.value < soft_min:
            try:
                prop = (soft_min - self.value) / (soft_min - hard_min)
                self.friction = self.base_friction + abs(
                    self.max_friction - self.base_friction
                ) * self.transition_min(prop)
            except ZeroDivisionError:
                pass
        elif self.value > soft_max:
            try:
                # normalize how far past soft_max I've gone as a
                # proportion of the distance between soft_max and hard_max
                prop = (self.value - soft_max) / (hard_max - soft_max)
                self.friction = self.base_friction + abs(
                    self.max_friction - self.base_friction
                ) * self.transition_min(prop)
            except ZeroDivisionError:
                pass
        else:
            self.friction = self.base_friction

        return super().update_velocity(dt)

    def on_value(self, *args):
        """Prevent moving beyond my bounds, and update ``self.scroll``"""

        if self.value < self.min:
            self.velocity = 0
            self.scroll = self.min
        elif self.value > self.max:
            self.velocity = 0
            self.scroll = self.max
        else:
            self.scroll = self.value

    def start(self, val, t=None):
        """Start movement with ``self.friction`` = ``self.base_friction``"""

        self.is_manual = True
        t = t or time()
        self.velocity = self.displacement = 0
        self.friction = self.base_friction
        self.history = [(t, val)]

    def update(self, val, t=None):
        """Reduce the impact of whatever change has been made to me, in
        proportion with my current friction.

        """

        t = t or time()
        hard_min = self.min
        hard_max = self.max
        if hard_min > hard_max:
            hard_min, hard_max = hard_max, hard_min

        gamut = hard_max - hard_min
        margin = (1.0 - self.body) * gamut
        soft_min = hard_min + margin
        soft_max = hard_max - margin
        distance = val - self.history[-1][1]
        reach = distance + self.value

        if (distance < 0 and reach < soft_min) or (distance > 0 and soft_max < reach):
            distance -= distance * self.friction
        self.apply_distance(distance)
        self.history.append((t, val))

        if len(self.history) > self.max_history:
            self.history.pop(0)
        self.displacement += abs(distance)
        self.trigger_velocity_update()

    def stop(self, val, t=None):
        """Work out whether I've been flung."""

        self.is_manual = False
        self.displacement += abs(val - self.history[-1][1])
        if self.displacement <= self.drag_threshold:
            self.velocity = 0

        return super().stop(val, t)
