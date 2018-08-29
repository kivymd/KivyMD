# NavigationDrawer

The NavigationDrawer widget provides a hidden panel view designed to
duplicate the popular Android layout.  The user views one main widget
but can slide from the left of the screen to view a second, previously
hidden widget. The transition between open/closed is smoothly
animated, with the parameters (anim time, panel width, touch
detection) all user configurable. If the panel is released without
being fully open or closed, it animates to an appropriate
configuration.

NavigationDrawer supports many different animation properties,
including moving one or both of the side/main panels, darkening
either/both widgets, changing side panel opacity, and changing which
widget is on top. The user can edit these individually to taste (this
is enough rope to hang oneself, it's easy to make a useless or silly
configuration!), or use one of a few preset animations.

The hidden panel might normally a set of navigation buttons (e.g. in a
GridLayout), but the implementation lets the user use any widget(s).

The first widget added to the NavigationDrawer is automatically used
as the side panel, and the second widget as the main panel. No further
widgets can be added, further changes are left to the user via editing
the panel widgets.

# Usage summary

- The first widget added to a NavigationDrawer is used as the hidden
  side panel.
- The second widget added is used as the main panel.
- Both widgets can be removed with remove_widget, or alternatively
  set/removed with set_main_panel and set_side_panel.
- The hidden side panel can be revealed by dragging from the left of
  the NavigationDrawer. The touch detection width is the
  touch_accept_width property.
- Every animation property is user-editable, or default animations
  can be chosen by setting anim_type.

See the example and docstrings for information on individual properties.


# Example::

    from kivy.app import App
    from kivy.base import runTouchApp
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.image import Image
    from kivy.uix.widget import Widget
    from kivy.core.window import Window
    from kivy.metrics import dp

    from kivy.garden.navigationdrawer import NavigationDrawer

    class ExampleApp(App):

        def build(self):
            navigationdrawer = NavigationDrawer()

            side_panel = BoxLayout(orientation='vertical')
            side_panel.add_widget(Label(text='Panel label'))
            side_panel.add_widget(Button(text='A button'))
            side_panel.add_widget(Button(text='Another button'))
            navigationdrawer.add_widget(side_panel)

            label_head = (
                '[b]Example label filling main panel[/b]\n\n[color=ff0000](p'
                'ull from left to right!)[/color]\n\nIn this example, the le'
                'ft panel is a simple boxlayout menu, and this main panel is'
                ' a BoxLayout with a label and example image.\n\nSeveral pre'
                'set layouts are available (see buttons below), but users ma'
                'y edit every parameter for much more customisation.')
            main_panel = BoxLayout(orientation='vertical')
            label_bl = BoxLayout(orientation='horizontal')
            label = Label(text=label_head, font_size='15sp',
                          markup=True, valign='top')
            label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
            label_bl.add_widget(label)
            label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
            main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
            main_panel.add_widget(label_bl)
            main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
            main_panel.add_widget(Image(source='red_pixel.png', allow_stretch=True,
                                        keep_ratio=False, size_hint_y=0.2))
            navigationdrawer.add_widget(main_panel)
            label.bind(size=label.setter('text_size'))

            def set_anim_type(name):
                navigationdrawer.anim_type = name
            modes_layout = BoxLayout(orientation='horizontal')
            modes_layout.add_widget(Label(text='preset\nanims:'))
            slide_an = Button(text='slide_\nabove_\nanim')
            slide_an.bind(on_press=lambda j: set_anim_type('slide_above_anim'))
            slide_sim = Button(text='slide_\nabove_\nsimple')
            slide_sim.bind(on_press=lambda j: set_anim_type('slide_above_simple'))
            fade_in_button = Button(text='fade_in')
            fade_in_button.bind(on_press=lambda j: set_anim_type('fade_in'))
            reveal_button = Button(text='reveal_\nbelow_\nanim')
            reveal_button.bind(on_press=
                               lambda j: set_anim_type('reveal_below_anim'))
            slide_button = Button(text='reveal_\nbelow_\nsimple')
            slide_button.bind(on_press=
                              lambda j: set_anim_type('reveal_below_simple'))
            modes_layout.add_widget(slide_an)
            modes_layout.add_widget(slide_sim)
            modes_layout.add_widget(fade_in_button)
            modes_layout.add_widget(reveal_button)
            modes_layout.add_widget(slide_button)
            main_panel.add_widget(modes_layout)

            button = Button(text='toggle NavigationDrawer state (animate)',
                            size_hint_y=0.2)
            button.bind(on_press=lambda j: navigationdrawer.toggle_state())
            button2 = Button(text='toggle NavigationDrawer state (jump)',
                             size_hint_y=0.2)
            button2.bind(on_press=lambda j: navigationdrawer.toggle_state(False))
            button3 = Button(text='toggle _main_above', size_hint_y=0.2)
            button3.bind(on_press=navigationdrawer.toggle_main_above)
            main_panel.add_widget(button)
            main_panel.add_widget(button2)
            main_panel.add_widget(button3)

            return navigationdrawer

        ExampleApp().run()

