from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
#:import MDIconButton kivymd.button.MDIconButton


<MDChip>:
    size_hint: None,  None
    height: dp(36)
    width: label.texture_size[0] + icon.width + dp(10)

    canvas:
        Color:
            rgba: root.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]
    Label:
        id: label
        text: '     {}'.format(root.label)
    
    MDIconButton:
        id: icon
        icon: root.icon
        size_hint_y: None
        height: dp(36)
        disabled: True

""")


class MDChip(BoxLayout):
    label = StringProperty()
    icon = StringProperty('checkbox-blank-circle')
    color = ListProperty([.4, .4, .4, 1])
    callback = ObjectProperty(lambda x: None)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.callback(self.label)
