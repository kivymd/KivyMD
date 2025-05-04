"""
Components/ResponsiveLayout
===========================

.. versionadded:: 1.0.0

.. rubric:: Responsive design is a graphic user interface (GUI) design
    approach used to create content that adjusts smoothly to various screen
    sizes.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe
            src="https://www.youtube.com/embed/HMK1UZbSyeo"
            frameborder="0"
            allowfullscreen
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
        </iframe>
    </div>

The :class:`~MDResponsiveLayout` class does not reorganize your UI. Its task
is to track the size of the application screen and, depending on this size,
the :class:`~MDResponsiveLayout` class selects which UI layout should be
displayed at the moment: mobile, tablet or desktop. Therefore, if you want to
have a responsive view some kind of layout in your application, you should
have three KV files with UI markup for three platforms.

You need to set three parameters for the :class:`~MDResponsiveLayout` class
:attr:`~MDResponsiveLayout.mobile_view`,
:attr:`~MDResponsiveLayout.tablet_view` and
:attr:`~MDResponsiveLayout.desktop_view`. These should be Kivy or KivyMD
widgets.

Usage responsive
----------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.responsivelayout import MDResponsiveLayout
    from kivymd.uix.screen import MDScreen

    KV = '''
    <CommonComponentLabel>
        halign: "center"


    <MobileView>
        CommonComponentLabel:
            text: "Mobile"


    <TabletView>
        CommonComponentLabel:
            text: "Table"


    <DesktopView>
        CommonComponentLabel:
            text: "Desktop"


    ResponsiveView:
    '''


    class CommonComponentLabel(MDLabel):
        pass


    class MobileView(MDScreen):
        pass


    class TabletView(MDScreen):
        pass


    class DesktopView(MDScreen):
        pass


    class ResponsiveView(MDResponsiveLayout, MDScreen):
        def __init__(self, **kw):
            super().__init__(**kw)
            self.mobile_view = MobileView()
            self.tablet_view = TabletView()
            self.desktop_view = DesktopView()


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/responsive-usage.gif
    :align: center

.. note:: Use common components for platform layouts (mobile, tablet, desktop views).
    As shown in the example above, such a common component is the
    `CommonComponentLabel` widget.

Perhaps you expected more from the :class:`~MDResponsiveLayout` widget, but
even `Flutter` uses a similar approach to creating a responsive UI.

You can also use the `commands <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/#create-project-with-responsive-view>`_
provided to you by the developer tools to create a project with an responsive
design.
"""

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

from kivymd.uix.controllers import WindowController


class MDResponsiveLayout(EventDispatcher, WindowController):
    """
    :Events:
        :attr:`on_change_screen_type`
            Called when the screen type changes.
    """

    mobile_view = ObjectProperty()
    """
    Mobile view. Must be a Kivy or KivyMD widget.

    :attr:`mobile_view` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    tablet_view = ObjectProperty()
    """
    Tablet view. Must be a Kivy or KivyMD widget.

    :attr:`tablet_view` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    desktop_view = ObjectProperty()
    """
    Desktop view. Must be a Kivy or KivyMD widget.

    :attr:`desktop_view` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    _current_device_type = ""

    __events__ = ("on_change_screen_type",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_change_screen_type(self, *args):
        """Called when the screen type changes."""

    def on_size(self, *args) -> None:
        """Called when the application screen size changes."""

        super().on_size(*args)
        self.set_screen()

        if self._current_device_type != self.real_device_type:
            self._current_device_type = self.real_device_type

    def set_screen(self) -> None:
        """
        Sets the screen according to the type of application screen size:
        mobile/tablet or desktop view.
        """

        if self.real_device_type != self._current_device_type:
            self.clear_widgets()

            if self.mobile_view and self.tablet_view and self.desktop_view:
                if self.real_device_type == "mobile":
                    self.add_widget(self.mobile_view)
                elif self.real_device_type == "tablet":
                    self.add_widget(self.tablet_view)
                elif self.real_device_type == "desktop":
                    self.add_widget(self.desktop_view)

            self.dispatch("on_change_screen_type", self.real_device_type)
