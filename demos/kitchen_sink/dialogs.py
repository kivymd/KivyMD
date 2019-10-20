from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.modalview import ModalView

from kivymd.theming import ThemableBehavior


Builder.load_string(
    """
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import Window kivy.core.window.Window
#:import images_path kivymd.images_path
#:import environ os.environ


<BaseDialogForLoadKvFiles>:
    background: '{}/transparent.png'.format(images_path)

    canvas.before:
        Color:
            rgba: root.canvas_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]


<DialogLoadKvFiles>:
    size_hint: None, None
    height: Window.height * 20 / 100
    width: Window.width * 80 / 100
    auto_dismiss: False

    BoxLayout:
        spacing: dp(20)
        padding: dp(10)

        Image:
            size_hint: None, None
            size: Window.height * 12 / 100, Window.height * 12 / 100
            source: f"{environ['KITCHEN_SINK_ASSETS']}kivy-logo-white-512.png"
            pos_hint: {'center_y': .5}

        Label:
            size_hint: None, None
            size: self.texture_size
            text:
                'Load screen: {}%\\n' \
                '[color={}]{}[/color]'.format(\
                root.percent, get_hex_from_color(app.theme_cls.primary_color), root.name_kv_file)
            bold: True
            markup: True
            color: 1, 1, 1, 1
            pos_hint: {'center_y': .5}
"""
)


class BaseDialogForLoadKvFiles(ThemableBehavior, ModalView):
    canvas_color = ListProperty()
    callback = ObjectProperty(lambda x: None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas_color = self.theme_cls.primary_color
        self.canvas_color[3] = 0.75


class DialogLoadKvFiles(BaseDialogForLoadKvFiles):
    """Dialogue to wait for the completion of some action."""

    name_kv_file = StringProperty()
    percent = StringProperty("0")
