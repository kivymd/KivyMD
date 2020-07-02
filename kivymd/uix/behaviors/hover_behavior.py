"""
Behaviors/Hover
===============

.. rubric:: Changing when the mouse is on the widget.

To apply hover behavior, you must create a new class that is inherited from the
widget to which you apply the behavior and from the :attr:`HoverBehavior` class.

In `KV file`:

.. code-block:: kv

    <HoverItem@MDBoxLayout+ThemableBehavior+HoverBehavior>

In `python file`:

.. code-block:: python

    class HoverItem(MDBoxLayout, ThemableBehavior, HoverBehavior):
        '''Custom item implementing hover behavior.'''

After creating a class, you must define two methods for it:
:attr:`HoverBehavior.on_enter` and :attr:`HoverBehavior.on_leave`, which will be automatically called
when the mouse cursor is over the widget and when the mouse cursor goes beyond
the widget.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import HoverBehavior
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.theming import ThemableBehavior

    KV = '''
    Screen

        MDBoxLayout:
            id: box
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .8, .8
            md_bg_color: app.theme_cls.bg_darkest
    '''


    class HoverItem(MDBoxLayout, ThemableBehavior, HoverBehavior):
        '''Custom item implementing hover behavior.'''

        def on_enter(self, *args):
            '''The method will be called when the mouse cursor
            is within the borders of the current widget.'''

            self.md_bg_color = (1, 1, 1, 1)

        def on_leave(self, *args):
            '''The method will be called when the mouse cursor goes beyond
            the borders of the current widget.'''

            self.md_bg_color = self.theme_cls.bg_darkest


    class Test(MDApp):
        def build(self):
            self.screen = Builder.load_string(KV)
            for i in range(5):
                self.screen.ids.box.add_widget(HoverItem())
            return self.screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hover-behavior.gif
   :width: 250 px
   :align: center
"""

__all__ = ("HoverBehavior",)

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import BooleanProperty, ObjectProperty


class HoverBehavior(object):
    """
    :Events:
        :attr:`on_enter`
            Fired when mouse enter the bbox of the widget.
        :attr:`on_leave`
            Fired when the mouse exit the widget.
    """

    hovered = BooleanProperty(False)
    """
    `True`, if the mouse cursor is within the borders of the widget.

    :attr:`hovered` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    border_point = ObjectProperty(None)
    """Contains the last relevant point received by the Hoverable.
    This can be used in :attr:`on_enter` or :attr:`on_leave` in order
    to know where was dispatched the event.

    :attr:`border_point` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch("on_enter")
        else:
            self.dispatch("on_leave")

    def on_enter(self):
        """Fired when mouse enter the bbox of the widget."""

    def on_leave(self):
        """Fired when the mouse exit the widget."""


Factory.register("HoverBehavior", HoverBehavior)
