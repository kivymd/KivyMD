Getting Started
===============

In order to start using `KivyMD`, you must first `install the Kivy framework <https://kivy.org/doc/stable/gettingstarted/installation.html>`_
on your computer. Once you have installed `Kivy`, you can install `KivyMD`.

.. warning:: `KivyMD` depends on `Kivy`!
    Therefore, before using `KivyMD`, first `learn how to work <https://kivy.org/doc/stable/>`_ with `Kivy`.

Installation
------------

    pip install kivymd

Command above will install latest release version of KivyMD from `PyPI <https://pypi.org/project/kivymd>`_.
If you want to install development version from `master <https://github.com/kivymd/KivyMD/tree/master/>`_
branch, you should specify link to zip archive:

    pip install https://github.com/kivymd/KivyMD/archive/master.zip

.. note:: Replace `master.zip` with `<commit hash>.zip` (eg `51b8ef0.zip`) to
    download KivyMD from specific commit.

Also you can install manually from sources. Just clone the project and run pip::

    git clone https://github.com/kivymd/KivyMD.git --depth 1
    cd KivyMD
    pip install .

.. note:: If you don't need full commit history (about 320 MiB), you can use a
    shallow clone (`git clone https://github.com/kivymd/KivyMD.git --depth 1`)
    to save time. If you need full commit history, then remove `--depth 1`.

First KivyMD application
------------------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel


    class MainApp(MDApp):
        def build(self):
            return MDLabel(text="Hello, World", halign="center")


    MainApp().run()

.. rubric:: And the equivalent with `Kivy`:

.. code-block:: python

    from kivy.app import App
    from kivy.uix.label import Label


    class MainApp(App):
        def build(self):
            return Label(text="Hello, World")


    MainApp().run()

.. rubric:: To left - `Kivy`, to right - `KivyMD`:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hello-world.png
    :align: center

At first glance, the `KivyMD` example contains more code...
However, the following example already demonstrates how difficult it is to
create a custom button in `Kivy`:

.. code-block:: python

    from kivy.app import App
    from kivy.metrics import dp
    from kivy.uix.behaviors import TouchRippleBehavior
    from kivy.uix.button import Button
    from kivy.lang import Builder
    from kivy.utils import get_color_from_hex

    KV = """
    #:import get_color_from_hex kivy.utils.get_color_from_hex


    <RectangleFlatButton>:
        ripple_color: 0, 0, 0, .2
        background_color: 0, 0, 0, 0
        color: root.primary_color

        canvas.before:
            Color:
                rgba: root.primary_color
            Line:
                width: 1
                rectangle: (self.x, self.y, self.width, self.height)

    Screen:
        canvas:
            Color:
                rgba: get_color_from_hex("#0F0F0F")
            Rectangle:
                pos: self.pos
                size: self.size
    """


    class RectangleFlatButton(TouchRippleBehavior, Button):
        primary_color = get_color_from_hex("#EB8933")

        def on_touch_down(self, touch):
            collide_point = self.collide_point(touch.x, touch.y)
            if collide_point:
                touch.grab(self)
                self.ripple_show(touch)
                return True
            return False

        def on_touch_up(self, touch):
            if touch.grab_current is self:
                touch.ungrab(self)
                self.ripple_fade()
                return True
            return False


    class MainApp(App):
        def build(self):
            screen = Builder.load_string(KV)
            screen.add_widget(
                RectangleFlatButton(
                    text="Hello, World",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint=(None, None),
                    size=(dp(110), dp(35)),
                    ripple_color=(0.8, 0.8, 0.8, 0.5),
                )
            )
            return screen


    MainApp().run()

.. rubric:: And the equivalent with `KivyMD`:

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.button import MDButton, MDButtonText


    class MainApp(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"

            return (
                MDScreen(
                    MDButton(
                        MDButtonText(
                            text="Hello, World",
                        ),
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                )
            )


    MainApp().run()

.. rubric:: `KivyMD`:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/kivymd-ripple-rectangle-button.gif
    :align: center

.. rubric:: `Kivy`:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/kivy-ripple-rectangle-button.gif
    :align: center