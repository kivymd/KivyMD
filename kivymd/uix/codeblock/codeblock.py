"""
Components/CodeBlock
====================

Usage
-----

.. code-block:: python

    from kivy.core.window import Window
    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen


    appkv = '''
    MDScreen:
        MDStackLayout:
            size_hint: 1, 1
            
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: [dp(20), dp(20), dp(20), dp(20)]

                MDCodeBlock:
                    size_hint: 1, None
                    adaptive_height: True
                    text: "import os"
                    style_name: "colorful" # pygments builtin styles
                    # icon_color: 
                    # icon_bg_color:
                    # icon_bg_color_active:
    '''


    class MyApp(MDApp):

        def __init__(self, **kwargs):
            super(MyApp, self).__init__(**kwargs)
            Window.clearcolor = self.theme_cls.surfaceColor

        def build(self) -> MDScreen:
            screen = Builder.load_string(appkv)
            return screen

    if __name__=="__main__":
        MyApp().run()

"""

from __future__ import annotations

__all__ = ("MDCodeBLock",)

import os
from pygments import styles
from pygments import lexers

from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.relativelayout import RelativeLayout

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import BackgroundColorBehavior, DeclarativeBehavior

with open(
    os.path.join(uix_path, "codeblock", "codeblock.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read(), filename="MDCodeBlock.kv")


class MDCodeBlock(
    DeclarativeBehavior,
    MDAdaptiveWidget,
    ThemableBehavior,
    BackgroundColorBehavior,
    RelativeLayout,
):
    """
    MDCodeBlock class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.declarative_behavior.DeclarativeBehavior` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.backgroundcolor_behavior.BackgroundColorBehavior` and
    :class:`~kivymd.uix.behaviors.state_layer_behavior.StateLayerBehavior` and
    :class:`~kivy.uix.relativelayout.RelativeLayout` and
    :class:`~kivy.uix.codeinput.CodeInput`
    classes documentation.
    """

    text = StringProperty()
    """
    Text of the CodeBlock.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    lexer = ObjectProperty(lexers.Python3Lexer())
    """
    This holds the selected Lexer used by pygments to highlight the code.


    :attr:`lexer` is an :class:`~kivy.properties.ObjectProperty` and
    defaults to `PythonLexer`.
    """

    style_name = OptionProperty(
        "colorful", options=list(styles.get_all_styles())
    )
    """
    Name of the pygments style to use for formatting.

    :attr:`style_name` is an :class:`~kivy.properties.OptionProperty`
    and defaults to ``'default'``.
    """

    style = ObjectProperty(None)
    """
    The pygments style object to use for formatting.

    When ``style_name`` is set, this will be changed to the
    corresponding style object.

    :attr:`style` is a :class:`~kivy.properties.ObjectProperty` and
    defaults to ``None``
    """

    icon_bg_color = ColorProperty([1, 1, 1, 0])
    """
    Background Color of the copy button to use.

    :attr:`icon_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``[1, 1, 1, 0]``.
    """

    icon_color = ColorProperty(None, allownone=True)
    """
    Color of the copy button icon to use.

    :attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``None``.
    """

    icon_bg_color_active = ColorProperty(None, allownone=True)
    """
    Active Background Color of the copy button to use.

    :attr:`icon_bg_color_active` is an :class:`~kivy.properties.ColorProperty`
    and defaults to ``None``.
    """

    _icon_bg_color_active = ColorProperty()

    def __init__(self, *args, **kwargs):
        super(MDCodeBlock, self).__init__(*args, **kwargs)

    def on_copy(self, text: str = "", *args) -> None:
        """
        Fired when the copy button is pressed.

        For more information, see in the
        :class:`~kivy.clipboard.Clipboard`
        class documentation.
        """

        def set_color(*args):
            self.ids.codeblock_input_copy_button.md_bg_color = [1, 1, 1, 0]

        self.ids.codeblock_input_copy_button.md_bg_color = (
            self._icon_bg_color_active
        )
        Clipboard.copy(text)
        Clock.schedule_once(set_color, 2)
