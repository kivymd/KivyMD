# TODO: Add doc strings.

import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ColorProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd import uix_path

with open(
    os.path.join(uix_path, "divider", "divider.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDDivider(BoxLayout):
    """
    A separator line.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    color = ColorProperty(None)
    """
    Separator color in (r, g, b, a) or string format.

    :attr:`color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_orientation()

    def on_orientation(self, *args) -> None:
        """Fired when the values of :attr:`orientation` change."""

        self.size_hint = (
            (1, None) if self.orientation == "horizontal" else (None, 1)
        )
        if self.orientation == "horizontal":
            self.height = dp(1)
        else:
            self.width = dp(1)
