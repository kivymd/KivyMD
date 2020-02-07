![textfieldrect.gif](https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/md-text-field-round.gif)

## Example of using MDTextFieldRound:

```python
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.theming import ThemeManager

Builder.load_string('''
#:set color_shadow [0, 0, 0, .2980392156862745]
#:set color_lilac [.07058823529411765, .07058823529411765, .14901960784313725, .8]


<MyMDTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: color_shadow
    active_color: color_shadow
    pos_hint: {'center_x': .5}


<Example@Screen>
    canvas:
        Color:
            rgba: color_lilac
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        spacing: dp(15)
        pos_hint: {'center_x': .5, 'center_y': .5}

        MyMDTextFieldRound:
            icon_type: 'without'
            hint_text: 'Field with `normal_color`'
            normal_color: [0, 0, 0, .1]

        MyMDTextFieldRound:
            icon_type: 'without'
            hint_text: 'Field without icon'

        MyMDTextFieldRound:
            icon_type: 'without'
            hint_text: 'Field with `require_text_error`'
            require_text_error: 'Field must be not empty!'

        MyMDTextFieldRound:
            icon_left: 'email'
            icon_type: 'left'
            hint_text: 'Field with left icon'

        MyMDTextFieldRound:
            icon_left: 'email'
            icon_right: 'account-box'
            icon_right_disabled: True
            hint_text: 'Field with left and right disabled icons'

        MyMDTextFieldRound:
            icon_type: 'all'
            icon_left: 'key-variant'
            icon_right: 'eye-off'
            icon_right_disabled: False
            icon_callback: app.show_password
            password: True
            hint_text: 'Field width type `password = True`'
''')


class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'

    def build(self):
        return Factory.Example()

    def show_password(self, field, button):
        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'


if __name__ == '__main__':
    Example().run()
```

## Parameters:

```python
    width = NumericProperty(Window.width - dp(100))
    '''Text field width.'''

    icon_left = StringProperty('email-outline')
    '''Left icon.'''

    icon_right = StringProperty('email-outline')
    '''Right icon.'''

    icon_type = OptionProperty(
        'none', options=['right', 'left', 'all', 'without'])
    '''Use one (left) or two (left and right) icons in the text field.'''

    hint_text = StringProperty()
    '''Hint text in the text field.'''

    hint_text_color = ListProperty()
    '''Color of hint text in the text field.'''

    icon_color = ListProperty([1, 1, 1, 1])
    '''Color of icons.'''

    active_color = ListProperty([1, 1, 1, .2])
    '''The color of the text field when it is in focus.'''

    normal_color = ListProperty([1, 1, 1, .5])
    '''The color of the text field when it not in focus.'''

    foreground_color = ListProperty([1, 1, 1, 1])
    '''Text color.'''

    hint_text_color = ListProperty([0.5, 0.5, 0.5, 1.0])
    '''Text field hint color.'''

    cursor_color = ListProperty()
    '''Color of cursor'''

    selection_color = ListProperty()
    '''Text selection color.'''

    icon_callback = ObjectProperty()
    '''The function that is called when you click on the icon
    in the text field.'''

    text = StringProperty()
    '''Text of field.'''

    icon_left_dasabled = BooleanProperty(False)
    '''Disable the left icon.'''

    icon_right_disabled = BooleanProperty(False)
    '''Disable the right icon.'''

    password = BooleanProperty(False)
    '''Hide text or notю'''

    password_mask = StringProperty('*')
    '''Characters on which the text will be replaced
    if the `password` is True.'''

    require_text_error = StringProperty()
    '''Error text if the text field requires mandatory text.'''

    require_error_callback = ObjectProperty()
    '''The function that will be called when the unfocus.
    if `require_text_error` != ''
    '''

    event_focus = ObjectProperty()
    '''The function is called at the moment of focus/unfocus of the text field.
    '''
```
