"""
Behaviors/Hover
===============

.. rubric:: Changing when the mouse is on the widget and the widget is visible.

To apply hover behavior, you must create a new class that is inherited from the
widget to which you apply the behavior and from the :attr:`HoverBehavior` class.

In `KV file`:

.. code-block:: kv

    <HoverItem@MDBoxLayout+HoverBehavior>

In `python file`:

.. code-block:: python

    class HoverItem(MDBoxLayout, HoverBehavior):
        '''Custom item implementing hover behavior.'''

After creating a class, you must define two methods for it:
:attr:`HoverBehavior.on_enter` and :attr:`HoverBehavior.on_leave`, which will be automatically called
when the mouse cursor is over the widget and when the mouse cursor goes beyond
the widget.

.. note::

    :class:`~HoverBehavior` will by default check to see if the current Widget
    is visible (i.e. not covered by a modal or popup and not a part of a
    RelativeLayout, MDTab or Carousel that is not currently visible etc)
    and will only issue events if the widget is visible.

    To get the legacy behavior that the events are always triggered, you can
    set `detect_visible` on the Widget to `False`.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import HoverBehavior
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    MDScreen
        md_bg_color: self.theme_cls.backgroundColor

        MDBoxLayout:
            id: box
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .8, .8
            md_bg_color: self.theme_cls.secondaryContainerColor
    '''


    class HoverItem(MDBoxLayout, HoverBehavior):
        '''Custom item implementing hover behavior.'''

        def on_enter(self, *args):
            '''
            The method will be called when the mouse cursor
            is within the borders of the current widget.
            '''

            self.md_bg_color = "white"

        def on_leave(self, *args):
            '''
            The method will be called when the mouse cursor goes beyond
            the borders of the current widget.
            '''

            self.md_bg_color = self.theme_cls.secondaryContainerColor


    class Example(MDApp):
        def build(self):
            self.screen = Builder.load_string(KV)
            for i in range(5):
                self.screen.ids.box.add_widget(HoverItem())
            return self.screen


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hover-behavior.gif
   :align: center
"""

__all__ = ("HoverBehavior",)

from kivy.core.window import Window
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget


class HoverBehavior:
    """
    :Events:
        :attr:`on_enter`
            Fired when mouse enters the bbox of the widget and the widget is
            visible.
        :attr:`on_leave`
            Fired when the mouse exits the widget and the widget is visible.
    """

    hovering = BooleanProperty(False)
    """
    `True`, if the mouse cursor is within the borders of the widget.

    Note that this is set and cleared even if the widget is not visible.

    :attr:`hover` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    hover_visible = BooleanProperty(False)
    """
    `True` if hovering is `True` and is the current widget is visible.

    :attr:`hover_visible` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    enter_point = ObjectProperty(allownone=True)
    """
    Holds the last position where the mouse pointer crossed into the Widget
    if the Widget is visible and is currently in a hovering state.

    :attr:`enter_point` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    detect_visible = BooleanProperty(True)
    """
    Should this widget perform the visibility check?

    :attr:`detect_visible` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to  `True`.
    """

    def __init__(self, *args, **kwargs):
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")
        Window.bind(mouse_pos=self.on_mouse_update)
        super().__init__(*args, **kwargs)

    def on_mouse_update(self, *args):
        #  If the Widget currently has no parent, do nothing.
        if not self.get_root_window():
            return
        pos = args[1]
        # Is the pointer in the same position as the widget?
        # If not - then issue an on_exit event if needed.
        if not self.collide_point(
            *self.to_widget(*pos)
            if not isinstance(self, RelativeLayout)
            else (pos[0], pos[1])
        ):
            self.hovering = False
            self.enter_point = None
            if self.hover_visible:
                self.hover_visible = False
                self.dispatch("on_leave")
            return

        # The pointer is in the same position as the widget.
        if self.hovering:
            # Nothing to do here. Not - this does not handle the case where
            # a popup comes over an existing hover event.
            # This seems reasonable.
            return

        # Otherwise - set the hovering attribute
        self.hovering = True

        # We need to traverse the tree to see if the Widget is visible.
        # This is a two stage process - first go up the tree to the root.
        # Window. At each stage - check that the Widget is actually visible.
        # Second - at the root Window check that there is not another branch
        # covering the Widget.
        self.hover_visible = True

        if self.detect_visible:
            widget: Widget = self
            while True:
                # Walk up the Widget tree from the target Widget.
                parent = widget.parent
                try:
                    # See if the mouse point collides with the parent
                    # using both local and global coordinates to cover absolute
                    # and relative layouts.
                    pinside = parent.collide_point(
                        *parent.to_widget(*pos)
                    ) or parent.collide_point(*pos)
                except Exception:
                    # The collide_point will error when you reach the root
                    # Window.
                    break
                if not pinside:
                    self.hover_visible = False
                    break
                # Iterate upwards.
                widget = parent

            #  parent = root window
            #  widget = first Widget on the current branch
            children = parent.children
            for child in children:
                # For each top level widget - check if is current branch.
                # If it is - then break.
                # If not then - since we start at 0 - this widget is visible.
                # Check to see if it should take the hover.
                if child == widget:
                    # This means that the current widget is visible.
                    break
                if child.collide_point(*pos):
                    # This means that the current widget is covered by a modal
                    # or popup.
                    self.hover_visible = False
                    break
        if self.hover_visible:
            self.enter_point = pos
            self.dispatch("on_enter")

    def on_enter(self):
        """Fired when mouse enter the bbox of the widget."""

    def on_leave(self):
        """Fired when the mouse goes outside the widget border."""
