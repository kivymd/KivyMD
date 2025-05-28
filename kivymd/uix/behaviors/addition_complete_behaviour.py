from abc import ABC, abstractmethod

from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, ObjectProperty


class AdditionComplete(EventDispatcher):
    """
    A mixin to provide an 'on_fully_added' event that fires after a widget
    has been added to a parent and the parent's children list is updated.
    """

    __events__ = ("on_fully_added",)

    _internal_parent_ref_for_mixin = ObjectProperty(None, allownone=True)
    _is_waiting_for_fully_added = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Using fbind for a slightly more direct binding to the parent property.
        # This will call _mixin_on_parent_change when self.parent changes.
        self.parent = None
        self.fbind("parent", self._mixin_on_parent_change)

    def _mixin_on_parent_change(self, instance, new_parent):
        """
        Called when the widget's parent property changes.
        """
        if new_parent and not self._is_waiting_for_fully_added:
            # Widget is being added to a new parent (or parent is changing)
            # and we are not already waiting to dispatch on_fully_added.
            self._internal_parent_ref_for_mixin = new_parent
            self._is_waiting_for_fully_added = True
            Clock.schedule_once(
                self._mixin_dispatch_fully_added, 0
            )  # 0 = next frame
        elif not new_parent:
            self._internal_parent_ref_for_mixin = None

    def _mixin_dispatch_fully_added(self, dt):
        """
        Dispatches the 'on_fully_added' event.
        """
        # Reset the flag regardless of whether we dispatch.
        self._is_waiting_for_fully_added = False

        if (
            hasattr(self, "parent")
            and self.parent == self._internal_parent_ref_for_mixin
        ):
            self.dispatch("on_fully_added", self.parent)

    def on_fully_added(self, parent_widget):
        """
        Default handler for the 'on_fully_added' event.
        Override this method in your widget class that uses this mixin,
        or bind to the event using `instance.bind(on_fully_added=your_handler)`.

        This method is called when the widget has been added to 'parent_widget'
        and Kivy's internal processing for `add_widget` (like updating the
        parent's `children` list) is expected to be complete.

        :param parent_widget: The parent widget to which this widget was added.
        """
        pass
