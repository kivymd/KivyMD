Getting Started
===============

In order to start using `KivyMD`, you must first `install the Kivy framework <https://kivy.org/doc/stable/gettingstarted/installation.html>`_
on your computer. Once you have installed `Kivy`, you can install `KivyMD`.

.. warning:: `KivyMD` depends on `Kivy`!
    Therefore, before using `KivyMD`, first `learn how to work <https://kivy.org/doc/stable/>`_ with `Kivy`.

Installation
------------

You can install latest release version of `KivyMD` from `PyPI`::

    python3 -m pip install kivymd

If you want to install development version from master branch, you should specify git HTTPS address::

    # Master branch:
    python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git
    # Specific branch:
    python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@stable
    # Specific tag:
    python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@0.100.2
    # Specific commit:
    python3 -m pip install git+https://github.com/HeaTTheatR/KivyMD.git@f80d9c8b812d54a724db7eda30c4211d0ba764c2

    # If you already has installed KivyMD::
    python3 -m pip install --force-reinstall git+https://github.com/HeaTTheatR/KivyMD.git

Also you can install manually from sources. Just clone the project and run the ``setup.py`` script::

    python3 ./setup.py install

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

At first glance, the `KivyMD` example contains more code...
However, the following example already demonstrates how difficult it is to create a custom button in `Kivy`:

.. code-block:: python

    from kivy.app import App
    from kivy.metrics import dp
    from kivy.uix.behaviors import TouchRippleBehavior
    from kivy.uix.button import Button
    from kivy.lang import Builder


    KV = """
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
                rgba: 0.9764705882352941, 0.9764705882352941, 0.9764705882352941, 1
            Rectangle:
                pos: self.pos
                size: self.size
    """


    class RectangleFlatButton(TouchRippleBehavior, Button):
        primary_color = [
            0.12941176470588237,
            0.5882352941176471,
            0.9529411764705882,
            1
        ]

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

    from kivy.uix.screenmanager import Screen

    from kivymd.app import MDApp
    from kivymd.uix.button import MDRectangleFlatButton


    class MainApp(MDApp):
        def build(self):
            screen = Screen()
            screen.add_widget(
                MDRectangleFlatButton(
                    text="Hello, World",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
            return screen


    MainApp().run()

.. rubric:: To left - `Kivy`, to right - `KivyMD`:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/kivy-kivymd-rectangle-button-example.gif
