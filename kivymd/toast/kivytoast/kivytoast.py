"""
KivyToast
=========

.. rubric:: Implementation of toasts for desktop.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.toast import toast

    KV = '''
    MDScreen:

        MDTopAppBar:
            title: 'Test Toast'
            pos_hint: {'top': 1}
            left_action_items: [['menu', lambda x: x]]

        MDRaisedButton:
            text: 'TEST KIVY TOAST'
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_toast()
    '''


    class Test(MDApp):
        def show_toast(self):
            '''Displays a toast on the screen.'''

            toast('Test Kivy Toast')

        def build(self):
            return Builder.load_string(KV)

    Test().run()
"""

from typing import List

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.label import Label

from kivymd.uix.dialog import BaseDialog

Builder.load_string(
    """
<Toast>:
    size_hint: (None, None)
    pos_hint: {"center_x": 0.5, "center_y": 0.1}
    opacity: 0
    auto_dismiss: True
    overlay_color: [0, 0, 0, 0]
    canvas:
        Color:
            rgba: root._md_bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius
"""
)


class Toast(BaseDialog):
    duration = NumericProperty(2.5)
    """
    The amount of time (in seconds) that the toast is visible on the screen.

    :attr:`duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.5`.
    """

    _md_bg_color = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_toast = Label(size_hint=(None, None), markup=True, opacity=0)
        self.label_toast.bind(texture_size=self.label_check_texture_size)
        self.add_widget(self.label_toast)

    def label_check_texture_size(
        self, instance_label: Label, texture_size: List[int]
    ) -> None:
        """
        Resizes the text if the text texture is larger than the screen size.
        Sets the size of the toast according to the texture size of the toast
        text.
        """

        texture_width, texture_height = texture_size
        if texture_width > Window.width:
            instance_label.text_size = (Window.width - dp(10), None)
            instance_label.texture_update()
            texture_width, texture_height = instance_label.texture_size
        self.size = (texture_width + 25, texture_height + 25)

    def toast(self, text_toast: str) -> None:
        """Displays a toast."""

        self.label_toast.text = text_toast
        self.open()

    def on_open(self) -> None:
        """Default open event handler."""

        self.fade_in()
        Clock.schedule_once(self.fade_out, self.duration)

    def fade_in(self) -> None:
        """Animation of opening toast on the screen."""

        anim = Animation(opacity=1, duration=0.4)
        anim.start(self.label_toast)
        anim.start(self)

    def fade_out(self, *args) -> None:
        """Animation of hiding toast on the screen."""

        anim = Animation(opacity=0, duration=0.4)
        anim.bind(on_complete=lambda *x: self.dismiss())
        anim.start(self.label_toast)
        anim.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            if self.auto_dismiss:
                self.fade_out()
                return False
        super().on_touch_down(touch)
        return True


def toast(
    text: str = "", background: list = None, duration: float = 2.5
) -> None:
    """
    Displays a toast.

    :param text: text to be displayed in the toast;
    :param duration: the amount of time (in seconds) that the toast is visible on the screen
    :param background: toast background color in ``rgba`` format;
    """

    if background is None:
        background = [0.2, 0.2, 0.2, 1]
    Toast(duration=duration, _md_bg_color=background).toast(text)
