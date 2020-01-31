"""
KivyToast
=========

.. rubric:: Implementation of toasts for desktop.

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.toast import toast

    KV = '''
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            id: toolbar
            title: 'Test Toast'
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: '']]

        FloatLayout:

            MDRaisedButton:
                text: 'TEST KIVY TOAST'
                on_release: app.show_toast()
                pos_hint: {'center_x': .5, 'center_y': .5}

    '''


    class Test(MDApp):
        def show_toast(self):
            '''Displays a toast on the screen.'''

            toast('Test Kivy Toast')

        def build(self):
            return Builder.load_string(KV)

    Test().run()
"""

from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder

from kivymd import images_path

Builder.load_string(
    """
<Toast>:
    canvas:
        Color:
            rgba: .2, .2, .2, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
"""
)


class Toast(ModalView):
    duration = NumericProperty(2.5)
    """
    The amount of time (in seconds) that the toast is visible on the screen.

    :attr:`duration` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2.5`.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.1}
        self.background_color = [0, 0, 0, 0]
        self.background = f"{images_path}transparent.png"
        self.opacity = 0
        self.auto_dismiss = True
        self.label_toast = Label(size_hint=(None, None), opacity=0)
        self.label_toast.bind(texture_size=self.label_check_texture_size)
        self.add_widget(self.label_toast)

    def label_check_texture_size(self, instance, texture_size):
        texture_width, texture_height = texture_size
        if texture_width > Window.width:
            instance.text_size = (Window.width - dp(10), None)
            instance.texture_update()
            texture_width, texture_height = instance.texture_size
        self.size = (texture_width + 25, texture_height + 25)

    def toast(self, text_toast):
        self.label_toast.text = text_toast
        self.open()

    def on_open(self):
        self.fade_in()
        Clock.schedule_once(self.fade_out, self.duration)

    def fade_in(self):
        Animation(opacity=1, duration=0.4).start(self.label_toast)
        Animation(opacity=1, duration=0.4).start(self)

    def fade_out(self, interval):
        Animation(opacity=0, duration=0.4).start(self.label_toast)
        anim_body = Animation(opacity=0, duration=0.4)
        anim_body.bind(on_complete=lambda *x: self.dismiss())
        anim_body.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            if self.auto_dismiss:
                self.dismiss()
                return False
        super(ModalView, self).on_touch_down(touch)
        return True


def toast(text: str, duration=2.5):
    """Displays a toast.

    :duration: The amount of time (in seconds) that the toast is visible on the screen.
    """

    Toast(duration=duration).toast(text)
