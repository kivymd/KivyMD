# Of course, "very flexible Python" allows you to do without an abstract
# superclass at all or use the clever exception `NotImplementedError`. In my
# opinion, this can negatively affect the architecture of the application.
# I would like to point out that using Kivy, one could use the on-signaling
# model. In this case, when the state changes, the model will send a signal
# that can be received by all attached observers. This approach seems less
# universal - you may want to use a different library in the future.


class Observer:
    """Abstract superclass for all observers."""

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """
