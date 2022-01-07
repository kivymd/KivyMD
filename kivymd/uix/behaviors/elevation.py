"""
Behaviors/Elevation
===================

.. seealso::

    `Material Design spec, Elevation <https://material.io/design/environment/elevation.html>`_

.. rubric:: Elevation is the relative distance between two surfaces along the z-axis.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevation-previous.png
    :align: center

There are 5 classes in KivyMD that can simulate shadow:

     #. :class:`~FakeRectangularElevationBehavior`
     #. :class:`~FakeCircularElevationBehavior`

     #. :class:`~RectangularElevationBehavior`
     #. :class:`~CircularElevationBehavior`
     #. :class:`~RoundedRectangularElevationBehavior`

By default, KivyMD widgets use the elevation behavior implemented in classes
:class:`~FakeRectangularElevationBehavior` and :class:`~FakeCircularElevationBehavior`
for cast shadows. These classes use the old method of rendering shadows and it
doesn't look very aesthetically pleasing. Shadows are harsh, no softness:

The :class:`~RectangularElevationBehavior`, :class:`~CircularElevationBehavior`,
:class:`~RoundedRectangularElevationBehavior` classes use the new shadow
rendering algorithm, based on textures creation using the `Pillow` library.
It looks very aesthetically pleasing and beautiful.

.. warning:: Remember that :class:`~RectangularElevationBehavior`,
    :class:`~CircularElevationBehavior`, :class:`~RoundedRectangularElevationBehavior`
    classes require a lot of resources from the device on which your application will run,
    so you should not use these classes on mobile devices.

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.widget import Widget

    from kivymd.app import MDApp
    from kivymd.uix.card import MDCard
    from kivymd.uix.behaviors import RectangularElevationBehavior
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    <Box@MDBoxLayout>
        adaptive_size: True
        orientation: "vertical"
        spacing: "36dp"


    <BaseShadowWidget>
        size_hint: None, None
        size: 100, 100
        md_bg_color: 0, 0, 1, 1
        elevation: 36
        pos_hint: {'center_x': .5}


    MDFloatLayout:

        MDBoxLayout:
            adaptive_size: True
            pos_hint: {'center_x': .5, 'center_y': .5}
            spacing: "56dp"

            Box:

                MDLabel:
                    text: "Deprecated shadow rendering"
                    adaptive_size: True

                DeprecatedShadowWidget:

                MDLabel:
                    text: "Doesn't require a lot of resources"
                    adaptive_size: True

            Box:

                MDLabel:
                    text: "New shadow rendering"
                    adaptive_size: True

                NewShadowWidget:

                MDLabel:
                    text: "It takes a lot of resources"
                    adaptive_size: True
    '''


    class BaseShadowWidget(Widget):
        pass


    class DeprecatedShadowWidget(MDCard, BaseShadowWidget):
        '''Deprecated shadow rendering. Doesn't require a lot of resources.'''


    class NewShadowWidget(RectangularElevationBehavior, BaseShadowWidget, MDBoxLayout):
        '''New shadow rendering. It takes a lot of resources.'''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/elevation-differential.png
    :align: center


For example, let's create an button with a rectangular elevation effect:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import (
        RectangularRippleBehavior,
        BackgroundColorBehavior,
        FakeRectangularElevationBehavior,
    )

    KV = '''
    <RectangularElevationButton>:
        size_hint: None, None
        size: "250dp", "50dp"


    MDScreen:

        # With elevation effect
        RectangularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .6}
            elevation: 18

        # Without elevation effect
        RectangularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .4}
    '''


    class RectangularElevationButton(
        RectangularRippleBehavior,
        FakeRectangularElevationBehavior,
        ButtonBehavior,
        BackgroundColorBehavior,
    ):
        md_bg_color = [0, 0, 1, 1]


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-effect.gif
    :align: center

Similarly, create a circular button:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.app import MDApp
    from kivymd.uix.behaviors import (
        CircularRippleBehavior,
        FakeCircularElevationBehavior,
    )

    KV = '''
    <CircularElevationButton>:
        size_hint: None, None
        size: "100dp", "100dp"
        radius: self.size[0] / 2
        md_bg_color: 0, 0, 1, 1

        MDIcon:
            icon: "hand-heart"
            halign: "center"
            valign: "center"
            size: root.size
            pos: root.pos
            font_size: root.size[0] * .6
            theme_text_color: "Custom"
            text_color: [1] * 4


    MDScreen:

        CircularElevationButton:
            pos_hint: {"center_x": .5, "center_y": .6}
            elevation: 24
    '''


    class CircularElevationButton(
        FakeCircularElevationBehavior,
        CircularRippleBehavior,
        ButtonBehavior,
        MDBoxLayout,
    ):
        pass



    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-fake-elevation.png
    :align: center

Animating the elevation
-----------------------

.. code-block:: python

    from kivy.animation import Animation
    from kivy.lang import Builder
    from kivy.properties import ObjectProperty
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.theming import ThemableBehavior
    from kivymd.uix.behaviors import FakeRectangularElevationBehavior, RectangularRippleBehavior
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    MDFloatLayout:

        ElevatedWidget:
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None
            size: 100, 100
            md_bg_color: 0, 0, 1, 1
    '''


    class ElevatedWidget(
        ThemableBehavior,
        FakeRectangularElevationBehavior,
        RectangularRippleBehavior,
        ButtonBehavior,
        MDBoxLayout,
    ):
        shadow_animation = ObjectProperty()

        def on_press(self, *args):
            if self.shadow_animation:
                Animation.cancel_all(self, "_elevation")
            self.shadow_animation = Animation(_elevation=self.elevation + 10, d=0.4)
            self.shadow_animation.start(self)

        def on_release(self, *args):
            if self.shadow_animation:
                Animation.cancel_all(self, "_elevation")
            self.shadow_animation = Animation(_elevation=self.elevation, d=0.1)
            self.shadow_animation.start(self)


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-elevation-animation-effect.gif
    :align: center

Lighting position
-----------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.card import MDCard
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.behaviors import RectangularElevationBehavior

    KV = '''
    MDScreen:

        ShadowCard:
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None
            size: 100, 100
            shadow_pos: -10 + slider.value, -10 + slider.value
            elevation: 24
            md_bg_color: 1, 1, 1, 1

        MDSlider:
            id: slider
            max: 20
            size_hint_x: .6
            pos_hint: {'center_x': .5, 'center_y': .3}
    '''


    class ShadowCard(RectangularElevationBehavior, MDBoxLayout):
        pass


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/shadow-pos.gif
    :align: center
"""

__all__ = (
    "CommonElevationBehavior",
    "RectangularElevationBehavior",
    "CircularElevationBehavior",
    "RoundedRectangularElevationBehavior",
    "ObservableShadow",
    "FakeRectangularElevationBehavior",
    "FakeCircularElevationBehavior",
)

from io import BytesIO
from weakref import WeakMethod, ref

from kivy import Logger
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    BoundedNumericProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    ReferenceListProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.widget import Widget
from PIL import Image, ImageDraw, ImageFilter

from kivymd.app import MDApp

Builder.load_string(
    """
#:import InstructionGroup kivy.graphics.instructions.InstructionGroup


<CommonElevationBehavior>
    canvas.before:
        # SOFT SHADOW
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self._shadow_origin
        Color:
            group: "soft_shadow"
            rgba: root.soft_shadow_cl
        Rectangle:
            group: "soft_shadow"
            texture: self._soft_shadow_texture
            size: self.soft_shadow_size
            pos: self.soft_shadow_pos
        PopMatrix

        # HARD SHADOW
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self.center
        Color:
            group: "hard_shadow"
            rgba: root.hard_shadow_cl
        Rectangle:
            group: "hard_shadow"
            texture: self.hard_shadow_texture
            size: self.hard_shadow_size
            pos: self.hard_shadow_pos
        PopMatrix
        Color:
            group: "shadow"
            a: 1
""",
    filename="CommonElevationBehavior.kv",
)


class CommonElevationBehavior(Widget):
    """Common base class for rectangular and circular elevation behavior."""

    elevation = BoundedNumericProperty(0, min=0, errorvalue=0)
    """
    Elevation of the widget.

    .. note::
        Although, this value does not represent the current elevation of the
        widget. :attr:`~CommonElevationBehavior._elevation` can be used to
        animate the current elevation and come back using the
        :attr:`~CommonElevationBehavior.elevation` property directly.

        For example:

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.uix.behaviors import ButtonBehavior

            from kivymd.app import MDApp
            from kivymd.uix.behaviors import CircularElevationBehavior, CircularRippleBehavior
            from kivymd.uix.boxlayout import MDBoxLayout

            KV = '''
            #:import Animation kivy.animation.Animation


            <WidgetWithShadow>
                size_hint: [None, None]
                elevation: 6
                animation_: None
                md_bg_color: [1] * 4
                on_size:
                    self.radius = [self.height / 2] * 4
                on_press:
                    if self.animation_: \
                    self.animation_.cancel(self); \
                    self.animation_ = Animation(_elevation=self.elevation + 6, d=0.08); \
                    self.animation_.start(self)
                on_release:
                    if self.animation_: \
                    self.animation_.cancel(self); \
                    self.animation_ = Animation(_elevation = self.elevation, d=0.08); \
                    self.animation_.start(self)

            MDFloatLayout:

                WidgetWithShadow:
                    size: [root.size[1] / 2] * 2
                    pos_hint: {"center": [0.5, 0.5]}
            '''


            class WidgetWithShadow(
                CircularElevationBehavior,
                CircularRippleBehavior,
                ButtonBehavior,
                MDBoxLayout,
            ):
                def __init__(self, **kwargs):
                    # always set the elevation before the super().__init__ call
                    # self.elevation = 6
                    super().__init__(**kwargs)

                def on_size(self, *args):
                    self.radius = [self.size[0] / 2]


            class Example(MDApp):
                def build(self):
                    return Builder.load_string(KV)


            Example().run()

    :attr:`elevation` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `0`.
    """

    # Shadow rendering properties.
    # Shadow rotation memory - SHARED ACROSS OTHER CLASSES.
    angle = NumericProperty(0)
    """
    Angle of rotation in degrees of the current shadow.
    This value is shared across different widgets.

    .. note::
        This value will affect both, hard and soft shadows.
        Each shadow has his own origin point that's computed every time the
        elevation changes.

    .. warning::
        Do not add `PushMatrix` inside the canvas before and add `PopMatrix`
        in the next layer, this will cause visual errors, because the stack
        used will clip the push and pop matrix already inside the canvas.before
        canvas layer.

        Incorrect:

        .. code-block:: kv

            <TiltedWidget>
                canvas.before:
                    PushMatrix
                    [...]
                canvas:
                    PopMatrix

        Correct:

        .. code-block:: kv

            <TiltedWidget>
                canvas.before:
                    PushMatrix
                    [...]
                    PopMatrix



    :attr:`angle` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    radius = VariableListProperty([0])
    """
    Radius of the corners of the shadow.
    This values represents each corner of the shadow, starting from `top-left`
    corner and going clockwise.

    .. code-block:: python

        radius = [
            "top-left",
            "top-right",
            "bottom-right",
            "bottom-left",
        ]

    This value can be expanded thus allowing this settings to be valid:

    .. code-block:: python

        widget.radius=[0]  # Translates to [0, 0, 0, 0]
        widget.radius=[10, 3]  # Translates to [10, 3, 10, 3]
        widget.radius=[7.0, 8.7, 1.5, 3.0]  # Translates to [7, 8, 1, 3]

    .. note::
        This value will affect both, hard and soft shadows.
        This value only affects :class:`~RoundedRectangularElevationBehavior`
        for now, but can be stored and used by custom shadow draw functions.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    # Position of the shadow.
    _shadow_origin_x = NumericProperty(0)
    """
    Shadow origin `x` position for the rotation origin.

    Managed by `_shadow_origin`.

    :attr:`_shadow_origin_x` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.

    .. note::
        This property is automatically processed. by _shadow_origin.
    """

    _shadow_origin_y = NumericProperty(0)
    """
    Shadow origin y position for the rotation origin.

    Managed by :attr:`_shadow_origin`.

    :attr:`_shadow_origin_y` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.

    .. note::
        This property is automatically processed.
    """

    _shadow_origin = ReferenceListProperty(_shadow_origin_x, _shadow_origin_y)
    """
    Soft shadow rotation origin point.

    :attr:`_shadow_origin` is an :class:`~kivy.properties.ReferenceListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed and relative to the canvas center.
    """

    _shadow_pos = ListProperty([0, 0])  # custom offset
    """
    Soft shadow origin point.

    :attr:`_shadow_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed and relative to the widget's
        canvas center.
    """

    shadow_pos = ListProperty([0, 0])  # bottom left corner
    """
    Custom shadow origin point. If this property is set, :attr:`_shadow_pos`
    will be ommited.

    This property allows users to fake light source.

    :attr:`shadow_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        this value overwrite the :attr:`_shadow_pos` processing.
    """

    # Shadow Group shared memory
    __shadow_groups = {"global": []}

    shadow_group = StringProperty("global")
    """
    Widget's shadow group.
    By default every widget with a shadow is saved inside the memory
    :attr:`__shadow_groups` as a weakref. This means that you can have multiple
    light sources, one for every shadow group.

    To fake a light source use :attr:`force_shadow_pos`.

    :attr:`shadow_group` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"global"`.
    """

    _elevation = BoundedNumericProperty(0, min=0, errorvalue=0)
    """
    Current elevation of the widget.

    .. warning::
        This property is the current elevation of the widget, do not
        use this property directly, instead, use :class:`~CommonElevationBehavior`
        elevation.

    :attr:`_elevation` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    # soft shadow
    _soft_shadow_texture = ObjectProperty()
    """
    Texture of the soft shadow texture for the canvas.

    :attr:`_soft_shadow_texture` is an :class:`~kivy.core.image.Image`
    and defaults to `None`.

    .. note::
        This property is automatically processed.
    """

    soft_shadow_size = ListProperty([0, 0])
    """
    Size of the soft shadow texture over the canvas.

    :attr:`soft_shadow_size` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed.
    """

    soft_shadow_pos = ListProperty([0, 0])
    """
    Position of the hard shadow texture over the canvas.

    :attr:`soft_shadow_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed.
    """

    soft_shadow_cl = ListProperty([0, 0, 0, 0.50])
    """
    Color of the soft shadow.

    :attr:`soft_shadow_cl` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0.15]`.
    """

    # hard shadow
    hard_shadow_texture = ObjectProperty()
    """
    Texture of the hard shadow texture for the canvas.

    :attr:`hard_shadow_texture` is an :class:`~kivy.core.image.Image`
    and defaults to `None`.

    .. note::
        This property is automatically processed when elevation is changed.
    """

    hard_shadow_size = ListProperty([0, 0])
    """
    Size of the hard shadow texture over the canvas.

    :attr:`hard_shadow_size` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed when elevation is changed.
    """

    hard_shadow_pos = ListProperty([0, 0])
    """
    Position of the hard shadow texture over the canvas.

    :attr:`hard_shadow_pos` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0]`.

    .. note::
        This property is automatically processed when elevation is changed.
    """

    hard_shadow_cl = ListProperty([0, 0, 0, 0.15])
    """
    Color of the hard shadow.

    .. note::
        :attr:`hard_shadow_cl` is an :class:`~kivy.properties.ListProperty`
        and defaults to `[0, 0, 0, 0.15]`.
    """

    # Shared property for some calculations.
    # This values are used to improve the gaussain blur and avoid that
    # the blur goes outside the texture.
    hard_shadow_offset = BoundedNumericProperty(
        2, min=0, errorhandler=lambda x: 0 if x < 0 else x
    )
    """
    This value sets a special offset to the shadow canvas, this offset allows a
    correct draw of the canvas size. allowing the effect to correctly blur the
    image in the given space.

    :attr:`hard_shadow_offset` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `2`.
    """

    soft_shadow_offset = BoundedNumericProperty(
        4, min=0, errorhandler=lambda x: 0 if x < 0 else x
    )
    """
    This value sets a special offset to the shadow canvas, this offset allows a
    correct draw of the canvas size. allowing the effect to correctly blur the
    image in the given space.

    :attr:`soft_shadow_offset` is an :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to `4`.
    """

    draw_shadow = ObjectProperty(None)
    """
    This property controls the draw call of the context.

    This property is automatically set to :attr:`__draw_shadow__` inside the
    `super().__init__ call.` unless the property is different of None.

    To set a different drawing instruction function, set this property before the
    `super(),__init__` call inside the `__init__` definition of the new class.

    You can use the source for this classes as example of how to draw over
    with the context:

    Real time shadows:
        #. :class:`~RectangularElevationBehavior`
        #. :class:`~CircularElevationBehavior`
        #. :class:`~RoundedRectangularElevationBehavior`
        #. :class:`~ObservableShadow`


    Fake shadows (d`ont use this property):
        #. :class:`~FakeRectangularElevationBehavior`
        #. :class:`~FakeCircularElevationBehavior`

    :attr:`draw_shadow` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.

    .. note:: If this property is left to `None` the
        :class:`~CommonElevationBehavior` will set to a function that will
        raise a `NotImplementedError` inside `super().__init__`.

    Follow the next example to set a new draw instruction for the class
    inside `__init__`:

    .. code-block:: python

        class RoundedRectangularElevationBehavior(CommonElevationBehavior):
            '''
            Shadow class for the RoundedRectangular shadow behavior.
            Controls the size and position of the shadow.
            '''

            def __init__(self, **kwargs):
                self._draw_shadow = WeakMethod(self.__draw_shadow__)
                super().__init__(**kwargs)

            def __draw_shadow__(self, origin, end, context=None):
                context.draw(...)

    Context is a `Pillow` `ImageDraw` class. For more information check the
    [Pillow official documentation](https://github.com/python-pillow/Pillow/).
    """

    # All classes that uses a fake shadow shall set this value as `True`
    # for performance.
    _fake_elevation = BooleanProperty(False)

    def __init__(self, **kwargs):
        if self.draw_shadow is None:
            self.draw_shadow = WeakMethod(self.__draw_shadow__)
        self.prev_shadow_group = None
        im = BytesIO()
        Image.new("RGBA", (4, 4), color=(0, 0, 0, 0)).save(im, format="png")
        im.seek(0)
        # Setting a empty image as texture, improves performance.
        self._soft_shadow_texture = self.hard_shadow_texture = CoreImage(
            im, ext="png"
        ).texture
        Clock.schedule_once(self.shadow_preset, -1)
        self.on_shadow_group(self, self.shadow_group)

        self.bind(
            pos=self._update_shadow,
            size=self._update_shadow,
            radius=self._update_shadow,
        )
        super().__init__(**kwargs)

    def on_shadow_group(self, instance, value):
        """
        This function controls the shadow group of the widget.
        Do not use Directly to change the group. instead, use the shadow_group
        :attr:`property`.
        """

        groups = CommonElevationBehavior.__shadow_groups
        if self.prev_shadow_group:
            group = groups[self.prev_shadow_group]
            for widget in group[:]:
                if widget() is self:
                    group.remove(widget)
        group = self.prev_shadow_group = self.shadow_group
        if group not in groups:
            groups[group] = []
        r = ref(self, CommonElevationBehavior._clear_shadow_groups)
        groups[group].append(r)

    @staticmethod
    def _clear_shadow_groups(wk):
        # auto flush the element when the weak reference have been deleted
        groups = CommonElevationBehavior.__shadow_groups
        for group in list(groups.values()):
            if not group:
                break
            if wk in group:
                group.remove(wk)
                break

    def force_shadow_pos(self, shadow_pos):
        """
        This property forces the shadow position in every widget inside the
        widget. The argument :attr:`shadow_pos` is expected as a <class 'list'>
        or <class 'tuple'>.
        """

        if self.shadow_group is None:
            return
        group = CommonElevationBehavior.__shadow_groups[self.shadow_group]
        for wk in group[:]:
            widget = wk()
            if widget is None:
                group.remove(wk)
            widget.shadow_pos = shadow_pos
        del group

    def update_group_property(self, property_name, value):
        """
        This functions allows to change properties of every widget inside the
        shadow group.
        """

        if self.shadow_group is None:
            return
        group = CommonElevationBehavior.__shadow_groups[self.shadow_group]
        for wk in group[:]:
            widget = wk()
            if widget is None:
                group.remove(wk)
            setattr(widget, property_name, value)
        del group

    def shadow_preset(self, *args):
        """
        This function is meant to set the default configuration of the
        elevation.

        After a new instance is created, the elevation property will be launched
        and thus this function will update the elevation if the KV lang have not
        done it already.

        Works similar to an `__after_init__` call inside a widget.
        """

        from kivymd.uix.card import MDCard

        if self.elevation is None and not issubclass(self.__class__, MDCard):
            self.elevation = 10
        if self._fake_elevation is False:
            self._update_shadow(self, self.elevation)
        self.bind(
            pos=self._update_shadow,
            size=self._update_shadow,
            _elevation=self._update_shadow,
        )

    def on_elevation(self, instance, value):
        """
        Elevation event that sets the current elevation value to `_elevation`.
        """

        if value is not None:
            self._elevation = value

    def _set_soft_shadow_a(self, value):
        value = 0 if value < 0 else (1 if value > 1 else value)
        self.soft_shadow_cl[-1] = value
        return True

    def _set_hard_shadow_a(self, value):
        value = 0 if value < 0 else (1 if value > 1 else value)
        self.hard_shadow_cl[-1] = value
        return True

    def _get_soft_shadow_a(self):
        return self.soft_shadow_cl[-1]

    def _get_hard_shadow_a(self):
        return self.hard_shadow_cl[-1]

    _soft_shadow_a = AliasProperty(
        _get_soft_shadow_a, _set_soft_shadow_a, bind=["soft_shadow_cl"]
    )
    _hard_shadow_a = AliasProperty(
        _get_hard_shadow_a, _set_hard_shadow_a, bind=["hard_shadow_cl"]
    )

    def on_disabled(self, instance, value):
        """
        This function hides the shadow when the widget is disabled.
        It sets the shadow to `0`.
        """

        if self.disabled is True:
            self._elevation = 0
        else:
            self._elevation = 0 if self.elevation is None else self.elevation
        self._update_shadow(self, self._elevation)
        try:
            super().on_disabled(instance, value)
        except Exception:
            pass

    def _update_elevation(self, instance, value):
        self._elevation = value
        self._update_shadow(instance, value)

    def _update_shadow_pos(self, instance, value):
        if self._elevation > 0:
            self.hard_shadow_pos = [
                self.x - dp(self.hard_shadow_offset),  # + self.shadow_pos[0],
                self.y - dp(self.hard_shadow_offset),  # + self.shadow_pos[1],
            ]
            if self.shadow_pos == [0, 0]:
                self.soft_shadow_pos = [
                    self.x
                    + self._shadow_pos[0]
                    - self._elevation
                    - dp(self.soft_shadow_offset),
                    self.y
                    + self._shadow_pos[1]
                    - self._elevation
                    - dp(self.soft_shadow_offset),
                ]
            else:
                self.soft_shadow_pos = [
                    self.x
                    + self.shadow_pos[0]
                    - self._elevation
                    - dp(self.soft_shadow_offset),
                    self.y
                    + self.shadow_pos[1]
                    - self._elevation
                    - dp(self.soft_shadow_offset),
                ]
            self._shadow_origin = [
                self.soft_shadow_pos[0] + self.soft_shadow_size[0] / 2,
                self.soft_shadow_pos[1] + self.soft_shadow_size[1] / 2,
            ]

    def on__shadow_pos(self, ins, val):
        """
        Updates the shadow with the computed value.

        Call this function every time you need to force a shadow update.
        """

        self._update_shadow_pos(ins, val)

    def on_shadow_pos(self, ins, val):
        """
        Updates the shadow with the fixed value.

        Call this function every time you need to force a shadow update.
        """

        self._update_shadow_pos(ins, val)

    def _update_shadow(self, instance, value):
        self._update_shadow_pos(instance, value)
        if self._elevation > 0 and self._fake_elevation is False:
            # dynamic elevation position for the shadow
            if self.shadow_pos == [0, 0]:
                self._shadow_pos = [0, -self._elevation * 0.4]

            # HARD Shadow
            offset = int(dp(self.hard_shadow_offset))
            size = [
                int(self.size[0] + (offset * 2)),
                int(self.size[1] + (offset * 2)),
            ]
            im = BytesIO()
            # context
            img = Image.new("RGBA", tuple(size), color=(0, 0, 0, 0))
            # draw context
            shadow = ImageDraw.Draw(img)
            self.draw_shadow()(
                [offset, offset],
                [
                    int(size[0] - 1 - offset),
                    int(size[1] - 1 - offset),
                ],
                context=shadow
                # context=ref(shadow)
            )
            img = img.filter(
                ImageFilter.GaussianBlur(
                    radius=int(dp(1 + self.hard_shadow_offset / 3))
                )
            )
            img.save(im, format="png")
            im.seek(0)
            self.hard_shadow_size = size
            self.hard_shadow_texture = CoreImage(im, ext="png").texture

            # soft shadow
            if self.soft_shadow_cl[-1] > 0:
                offset = dp(self.soft_shadow_offset)
                size = [
                    int(self.size[0] + dp(self._elevation * 2) + (offset * 2)),
                    int(self.size[1] + dp(self._elevation * 2) + (offset * 2)),
                    # ((self._elevation)*2) + x + (offset*2)) for x in self.size
                ]
                im = BytesIO()
                img = Image.new("RGBA", tuple(size), color=((0,) * 4))
                shadow = ImageDraw.Draw(img)
                _offset = int(dp(self._elevation + offset))
                self.draw_shadow()(
                    [
                        _offset,
                        _offset,
                    ],
                    [int(size[0] - _offset - 1), int(size[1] - _offset - 1)],
                    context=shadow
                    # context=ref(shadow)
                )
                img = img.filter(
                    ImageFilter.GaussianBlur(radius=self._elevation // 2)
                )
                shadow = ImageDraw.Draw(img)
                img.save(im, format="png")
                im.seek(0)
                self.soft_shadow_size = size
                self._soft_shadow_texture = CoreImage(im, ext="png").texture
        else:
            im = BytesIO()
            Image.new("RGBA", (4, 4), color=(0, 0, 0, 0)).save(im, format="png")
            im.seek(0)
            self._soft_shadow_texture = self.hard_shadow_texture = CoreImage(
                im, ext="png"
            ).texture
            return

    def _get_center(self):
        center = [self.pos[0] + self.width / 2, self.pos[1] + self.height / 2]
        return center

    def __draw_shadow__(self, origin, end, context=None):
        Logger.warning(
            f"KivyMD: "
            f"If you see this error, this means that either youre using "
            f"`CommonElevationBehavio`r directly or your 'shader' dont have a "
            f"`_draw_shadow` instruction, remember to overwrite this function"
            f"to draw over the image context. Тhe figure you would like. "
            f"Or your class {self.__class__.__name__} is not inherited from "
            f"any of the classes {__all__}"
        )


class RectangularElevationBehavior(CommonElevationBehavior):
    """
    Base class for a rectangular elevation behavior.
    """

    def __init__(self, **kwargs):
        self.draw_shadow = WeakMethod(self.__draw_shadow__)
        super().__init__(**kwargs)

    def __draw_shadow__(self, origin, end, context=None):
        context.rectangle(origin + end, fill=tuple([255] * 4))


class CircularElevationBehavior(CommonElevationBehavior):
    """
    Base class for a circular elevation behavior.
    """

    def __init__(self, **kwargs):
        self.draw_shadow = WeakMethod(self.__draw_shadow__)
        super().__init__(**kwargs)

    def __draw_shadow__(self, origin, end, context=None):
        context.ellipse(origin + end, fill=tuple([255] * 4))


class RoundedRectangularElevationBehavior(CommonElevationBehavior):
    """
    Base class for rounded rectangular elevation behavior.
    """

    def __init__(self, **kwargs):
        self.bind(
            radius=self._update_shadow,
        )
        self.draw_shadow = WeakMethod(self.__draw_shadow__)
        super().__init__(**kwargs)

    def __draw_shadow__(self, origin, end, context=None):
        if self.radius == [0, 0, 0, 0]:
            context.rectangle(origin + end, fill=tuple([255] * 4))
        else:
            radius = [x * 2 for x in self.radius]
            context.pieslice(
                [
                    origin[0],
                    origin[1],
                    origin[0] + radius[0],
                    origin[1] + radius[0],
                ],
                180,
                270,
                fill=(255, 255, 255, 255),
            )
            context.pieslice(
                [
                    end[0] - radius[1],
                    origin[1],
                    end[0],
                    origin[1] + radius[1],
                ],
                270,
                360,
                fill=(255, 255, 255, 255),
            )
            context.pieslice(
                [
                    end[0] - radius[2],
                    end[1] - radius[2],
                    end[0],
                    end[1],
                ],
                0,
                90,
                fill=(255, 255, 255, 255),
            )
            context.pieslice(
                [
                    origin[0],
                    end[1] - radius[3],
                    origin[0] + radius[3],
                    end[1],
                ],
                90,
                180,
                fill=(255, 255, 255, 255),
            )
            if all((x == self.radius[0] for x in self.radius)):
                radius = int(self.radius[0])
                context.rectangle(
                    [
                        origin[0] + radius,
                        origin[1],
                        end[0] - radius,
                        end[1],
                    ],
                    fill=(255,) * 4,
                )
                context.rectangle(
                    [
                        origin[0],
                        origin[1] + radius,
                        end[0],
                        end[1] - radius,
                    ],
                    fill=(255,) * 4,
                )
            else:
                radius = [
                    max((self.radius[0], self.radius[1])),
                    max((self.radius[1], self.radius[2])),
                    max((self.radius[2], self.radius[3])),
                    max((self.radius[3], self.radius[0])),
                ]
                context.rectangle(
                    [
                        origin[0] + self.radius[0],
                        origin[1],
                        end[0] - self.radius[1],
                        end[1] - radius[2],
                    ],
                    fill=(255,) * 4,
                )
                context.rectangle(
                    [
                        origin[0] + radius[3],
                        origin[1] + self.radius[1],
                        end[0],
                        end[1] - self.radius[2],
                    ],
                    fill=(255,) * 4,
                )
                context.rectangle(
                    [
                        origin[0] + self.radius[3],
                        origin[1] + radius[0],
                        end[0] - self.radius[2],
                        end[1],
                    ],
                    fill=(255,) * 4,
                )
                context.rectangle(
                    [
                        origin[0],
                        origin[1] + self.radius[0],
                        end[0] - radius[2],
                        end[1] - self.radius[3],
                    ],
                    fill=(255,) * 4,
                )


class ObservableShadow(CommonElevationBehavior):
    """
    ObservableShadow is real time shadow render that it's intended to only
    render a partial shadow of widgets based upon on the window observable
    area, this is meant to improve the performance of bigger widgets.

    .. warning::
        This is an empty class, the name has been reserved for future use.
        if you include this clas in your object, you wil get a
        `NotImplementedError`.
    """

    def __init__(self, **kwargs):
        # self._shadow = MDApp.get_running_app().theme_cls.round_shadow
        # self._fake_elevation=True
        raise NotImplementedError(
            "ObservableShadow:\n\t" "This class is in current development"
        )
        super().__init__(**kwargs)


class FakeRectangularElevationBehavior(CommonElevationBehavior):
    """
    `FakeRectangularElevationBehavio`r is a shadow mockup for widgets. Improves
    performance using cached images inside `kivymd.images` dir

    This class cast a fake Rectangular shadow behaind the widget.

    You can either use this behavior to overwrite the elevation of a prefab
    widget, or use it directly inside a new widget class definition.

    Use this class as follows for new widgets:

    .. code-block:: python

        class NewWidget(
            ThemableBehavior,
            FakeCircularElevationBehavior,
            SpecificBackgroundColorBehavior,
            # here you add the other front end classes for the widget front_end,
        ):
            [...]

    With this method each class can draw it's content in the canvas in the
    correct order, avoiding some visual errors.

    `FakeCircularElevationBehavior` will load prefabricated textures to
    optimize loading times.

    .. note:: About rounded corners:
        be careful, since this behavior is a mockup and will not draw any
        rounded corners.
    """

    def __init__(self, **kwargs):
        # self._shadow = MDApp.get_running_app().theme_cls.round_shadow
        self.draw_shadow = WeakMethod(self.__draw_shadow__)
        self._fake_elevation = True
        self._update_shadow(self, self.elevation)
        super().__init__(**kwargs)

    def _update_shadow(self, *args):
        if self._elevation > 0:
            # Set shadow size.
            ratio = self.width / (self.height if self.height != 0 else 1)
            if -2 < ratio < 2:
                self._shadow = MDApp.get_running_app().theme_cls.quad_shadow
                width = soft_width = self.width * 1.9
                height = soft_height = self.height * 1.9
            elif ratio <= -2:
                self._shadow = MDApp.get_running_app().theme_cls.rec_st_shadow
                ratio = abs(ratio)
                if ratio > 5:
                    ratio = ratio * 22
                else:
                    ratio = ratio * 11.5
                width = soft_width = self.width * 1.9
                height = self.height + dp(ratio)
                soft_height = (
                    self.height + dp(ratio) + dp(self._elevation) * 0.5
                )
            else:
                self._shadow = MDApp.get_running_app().theme_cls.quad_shadow
                width = soft_width = self.width * 1.8
                height = soft_height = self.height * 1.8

            self.soft_shadow_size = (soft_width, soft_height)
            self.hard_shadow_size = (width, height)
            # Set ``soft_shadow`` parameters.
            center_x, center_y = self._get_center()
            self.hard_shadow_pos = self.soft_shadow_pos = (
                center_x - soft_width / 2,
                center_y - soft_height / 2 - dp(self._elevation * 0.5),
            )
            # Set transparency
            self._soft_shadow_a = 0.1 * 1.05 ** self._elevation
            self._hard_shadow_a = 0.4 * 0.8 ** self._elevation
            t = int(round(self._elevation))
            if 0 < t <= 23:
                self._soft_shadow_texture = (
                    self._hard_shadow_texture
                ) = self._shadow.textures[str(t)]
            else:
                self._soft_shadow_texture = (
                    self._hard_shadow_texture
                ) = self._shadow.textures["23"]
        else:
            self._soft_shadow_a = 0
            self._hard_shadow_a = 0

    def __draw_shadow__(self, origin, end, context=None):
        pass


class FakeCircularElevationBehavior(CommonElevationBehavior):
    """
    `FakeCircularElevationBehavior` is a shadow mockup for widgets. Improves
    performance using cached images inside `kivymd.images` dir

    This class cast a fake elliptic shadow behaind the widget.

    You can either use this behavior to overwrite the elevation of a prefab
    widget, or use it directly inside a new widget class definition.

    Use this class as follows for new widgets:

    .. code-block:: python

        class NewWidget(
            ThemableBehavior,
            FakeCircularElevationBehavior,
            SpecificBackgroundColorBehavior,
            # here you add the other front end classes for the widget front_end,
        ):
            [...]

    With this method each class can draw it's content in the canvas in the
    correct order, avoiding some visual errors.

    `FakeCircularElevationBehavior` will load prefabricated textures to optimize
    loading times.

    .. note:: About rounded corners:
        be careful, since this behavior is a mockup and will not draw any rounded
        corners. only perfect ellipses.
    """

    def __init__(self, **kwargs):
        self._shadow = MDApp.get_running_app().theme_cls.round_shadow
        self.draw_shadow = WeakMethod(self.__draw_shadow__)
        self._fake_elevation = True
        self._update_shadow(self, self.elevation)
        super().__init__(**kwargs)

    def _update_shadow(self, *args):
        if self._elevation > 0:
            # set shadow size
            width = self.width * 2
            height = self.height * 2
            center_x, center_y = self._get_center()

            x = center_x - width / 2
            self.soft_shadow_size = (width, height)
            self.hard_shadow_size = (width, height)
            # set ``soft_shadow`` parameters
            y = center_y - height / 2 - dp(0.5 * self._elevation)
            self.soft_shadow_pos = (x, y)

            # set ``hard_shadow`` parameters
            y = center_y - height / 2 - dp(0.5 * self._elevation)
            self.hard_shadow_pos = (x, y)

            # shadow transparency
            self._soft_shadow_a = 0.1 * 1.05 ** self._elevation
            self._hard_shadow_a = 0.4 * 0.8 ** self._elevation
            t = int(round(self._elevation))
            if 0 < t <= 23:
                if hasattr(self, "_shadow"):
                    self._soft_shadow_texture = (
                        self._hard_shadow_texture
                    ) = self._shadow.textures[str(t)]
            else:
                self._soft_shadow_texture = (
                    self._hard_shadow_texture
                ) = self._shadow.textures["23"]
        else:
            self._soft_shadow_a = 0
            self._hard_shadow_a = 0

    def __draw_shadow__(self, origin, end, context=None):
        pass
