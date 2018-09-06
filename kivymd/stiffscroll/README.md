stiffscroll
===========

A ScrollEffect for use with a Kivy ScrollView. It makes scrolling more
laborious as you reach the edge of the scrollable area.

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