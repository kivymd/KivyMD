"""
Components/Progress Bar
=======================

.. rubric:: Progress indicators express an unspecified wait time or display
    the length of a process.

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    BoxLayout:
        padding: "10dp"

        MDProgressBar:
            value: 50
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar.png
    :align: center

Vertical orientation
--------------------

.. code-block:: kv

    MDProgressBar:
        orientation: "vertical"
        value: 50

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar-vertical.png
    :align: center

With custom color
-----------------

.. code-block:: kv

    MDProgressBar:
        value: 50
        color: app.theme_cls.accent_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/progress-bar-custom-color.png
    :align: center
"""

from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, OptionProperty
from kivy.uix.progressbar import ProgressBar

from kivymd.theming import ThemableBehavior

Builder.load_string(
    """
<MDProgressBar>
    canvas:
        Clear
        Color:
            rgba: self.theme_cls.divider_color
        Rectangle:
            size:
                (self.width , dp(4)) if self.orientation == 'horizontal'\
                else (dp(4),self.height)
            pos:
                (self.x, self.center_y - dp(4))\
                if self.orientation == 'horizontal'\
                else (self.center_x - dp(4),self.y)
        Color:
            rgba:
                self.theme_cls.primary_color if not self.color else self.color
        Rectangle:
            size:
                (self.width * self.value_normalized, sp(4))\
                if self.orientation == 'horizontal' else (sp(4),\
                self.height*self.value_normalized)
            pos:
                (self.width*(1 - self.value_normalized) + self.x\
                if self.reversed else self.x, self.center_y - dp(4))\
                if self.orientation == 'horizontal'\
                else (self.center_x - dp(4),self.height\
                * (1 - self.value_normalized) + self.y if self.reversed\
                else self.y)
"""
)


class MDProgressBar(ThemableBehavior, ProgressBar):
    reversed = BooleanProperty(False)
    """Reverse the direction the progressbar moves.

    :attr:`reversed` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    orientation = OptionProperty(
        "horizontal", options=["horizontal", "vertical"]
    )
    """Orientation of progressbar. Available options are: `'horizontal '`,
    `'vertical'`.

    :attr:`orientation` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'horizontal'`.
    """

    color = ListProperty()
    """
    Progress bar color in ``rgba`` format.

    :attr:`color` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `[]`.
    """
