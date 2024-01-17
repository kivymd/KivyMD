__all__ = ("MDAdaptiveWidget",)

from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class MDAdaptiveWidget:
    adaptive_height = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:

    .. code-block:: kv

        size_hint_y: None
        height: self.minimum_height

    :attr:`adaptive_height` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    adaptive_width = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:

    .. code-block:: kv

        size_hint_x: None
        width: self.minimum_width

    :attr:`adaptive_width` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    adaptive_size = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:

    .. code-block:: kv

        size_hint: None, None
        size: self.minimum_size

    :attr:`adaptive_size` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def on_adaptive_height(self, md_widget, value: bool) -> None:
        self.size_hint_y = None
        if issubclass(self.__class__, Label):
            self.bind(
                texture_size=lambda *x: self.setter("height")(
                    self, self.texture_size[1]
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_height=self.setter("height"))
                if not self.children:
                    self.height = 0

    def on_adaptive_width(self, md_widget, value: bool) -> None:
        self.size_hint_x = None
        if issubclass(self.__class__, Label):
            self.bind(
                texture_size=lambda *x: self.setter("width")(
                    self, self.texture_size[0]
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_width=self.setter("width"))
                if not self.children:
                    self.width = 0

    def on_adaptive_size(self, md_widget, value: bool) -> None:
        self.size_hint = (None, None)
        if issubclass(self.__class__, Label):
            self.text_size = (None, None)
            self.bind(
                texture_size=lambda *x: self.setter("size")(
                    self, self.texture_size
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_size=self.setter("size"))
                if not self.children:
                    self.size = (0, 0)
