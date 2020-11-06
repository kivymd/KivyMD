from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        title: 'Progress and Slider'

    MDProgressBar:
        min: 0
        max: 100
        value: slider.value

    MDSlider:
        id: slider
"""


class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    Example().run()
