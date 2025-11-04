"""
Components/DatePicker
=====================

.. seealso::

    `Material Design spec, Date picker <https://m3.material.io/components/date-pickers/overview>`_

.. rubric:: Date pickers let people select a date, or a range of dates.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/date-picker.png
    :align: center

- Date pickers can display past, present, or future dates
- Three types: docked, modal, modal input
- Clearly indicate important dates, such as current and selected days
- Follow common patterns, like a calendar view

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/date-picker-types.png
    :align: center

1. Docked date picker
2. Modal date picker
3. Modal date input

KivyMD provides the following date pickers classes for use:

- MDDockedDatePicker_
- MDModalDatePicker_
- MDModalInputDatePicker_

.. _MDDockedDatePicker:

MDDockedDatePicker
------------------

Docked datepickers allow the selection of a specific date and year. The docked
datepicker displays a date input field by default, and a dropdown calendar
appears when the user taps on the input field. Either form of date entry can
be interacted with.

Docked date pickers are ideal for navigating dates in both the near future or
past and the distant future or past, as they provide multiple ways to select
dates.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/docked-data-picker-preview.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDDockedDatePicker

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDTextField:
                    id: field
                    mode: "outlined"
                    pos_hint: {'center_x': .5, 'center_y': .85}
                    size_hint_x: .5
                    on_focus: app.show_date_picker(self.focus)

                    MDTextFieldHintText:
                        text: "Docked date picker"

                    MDTextFieldHelperText:
                        text: "MM/DD/YYYY"
                        mode: "persistent"

                    MDTextFieldTrailingIcon:
                        icon: "calendar"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def show_date_picker(self, focus):
                    if not focus:
                        return

                    date_dialog = MDDockedDatePicker()
                    # You have to control the position of the date picker dialog yourself.
                    date_dialog.pos = [
                        self.root.ids.field.center_x - date_dialog.width / 2,
                        self.root.ids.field.y - (date_dialog.height + dp(32)),
                    ]
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDDockedDatePicker
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.textfield import (
                MDTextFieldHintText,
                MDTextField,
                MDTextFieldHelperText,
                MDTextFieldTrailingIcon,
            )


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDTextField(
                                MDTextFieldHintText(
                                    text="Docked date picker"
                                ),
                                MDTextFieldHelperText(
                                    text="MM/DD/YYYY",
                                    mode="persistent",
                                ),
                                MDTextFieldTrailingIcon(
                                    icon="calendar"
                                ),
                                id="field",
                                mode="outlined",
                                pos_hint={'center_x': .5, 'center_y': 0.85},
                                size_hint_x=0.5,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def on_start(self):
                    self.root.get_ids().field.bind(focus=self.show_date_picker)

                def show_date_picker(self, field, focus):
                    if focus:
                        date_dialog = MDDockedDatePicker()
                        # You have to control the position of the date picker dialog
                        # yourself.
                        date_dialog.pos = [
                            field.center_x - date_dialog.width / 2,
                            field.y - (date_dialog.height + dp(32)),
                        ]
                        date_dialog.open()


            Example().run()

.. _MDModalDatePicker:

MDModalDatePicker
-----------------

Modal date pickers navigate across dates in several ways:

- To navigate across months, swipe horizontally (not implemented in KivyMD)
- To navigate across years, scroll vertically (not implemented in KivyMD)
- To access the year picker, tap the year

Don’t use a modal date picker to prompt for dates in the distant past or
future, such as a date of birth. In these cases, use a modal input picker or
a docked datepicker instead.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-preview.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDModalDatePicker

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def show_date_picker(self):
                    date_dialog = MDModalDatePicker()
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.pickers import MDModalDatePicker
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open modal date picker dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_date_picker,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def show_date_picker(self, args):
                    date_dialog = MDModalDatePicker()
                    date_dialog.open()


            Example().run()

.. _MDModalInputDatePicker:

MDModalInputDatePicker
----------------------

Modal date inputs allow the manual entry of dates using the numbers on a
keyboard. Users can input a date or a range of dates in a dialog.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-input-data-picker-preview.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDModalInputDatePicker

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def show_date_picker(self):
                    date_dialog = MDModalInputDatePicker()
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.pickers import MDModalInputDatePicker
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open modal date picker dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_date_picker,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def show_date_picker(self, args):
                    date_dialog = MDModalInputDatePicker()
                    date_dialog.open()


            Example().run()

The range of available dates
============================

To display only the selected date range, use the `min_date` and `max_date`
parameters:

.. code-block:: python

    def show_modal_date_picker(self, *args):
        MDModalDatePicker(
            mark_today=False,
            min_date=datetime.date.today(),
            max_date=datetime.date(
                datetime.date.today().year,
                datetime.date.today().month,
                datetime.date.today().day + 4,
            ),
        ).open()

Only dates in the specified range will be available for selection:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-min-max-date.gif
    :align: center

Select the date range
=====================

To select the date range, use the `mode` parameter with the value "range":

.. code-block:: python

    def show_modal_date_picker(self, *args):
        MDModalDatePicker(mode="range").open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-range.gif
    :align: center

Setting the date range manually
===============================

.. code-block:: python

    def show_modal_date_picker(self, *args):
        MDModalInputDatePicker(mode="range").open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-input-data-picker-range.gif
    :align: center

Events
======

**on_edit** event
-----------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-edit.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.clock import Clock
            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDModalInputDatePicker, MDModalDatePicker

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_modal_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def show_modal_input_date_picker(self, *args):
                    def on_edit(*args):
                        date_dialog.dismiss()
                        Clock.schedule_once(self.show_modal_date_picker, 0.2)

                    date_dialog = MDModalInputDatePicker()
                    date_dialog.bind(on_edit=on_edit)
                    date_dialog.open()

                def on_edit(self, instance_date_picker):
                    instance_date_picker.dismiss()
                    Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker()
                    date_dialog.bind(on_edit=self.on_edit)
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivy.clock import Clock

            from kivymd.app import MDApp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.pickers import MDModalInputDatePicker, MDModalDatePicker
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open modal date picker dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_modal_date_picker,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def show_modal_input_date_picker(self, *args):
                    def on_edit(*args):
                        date_dialog.dismiss()
                        Clock.schedule_once(self.show_modal_date_picker, 0.2)

                    date_dialog = MDModalInputDatePicker()
                    date_dialog.bind(on_edit=on_edit)
                    date_dialog.open()

                def on_edit(self, instance_date_picker):
                    instance_date_picker.dismiss()
                    Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker()
                    date_dialog.bind(on_edit=self.on_edit)
                    date_dialog.open()


            Example().run()

**on_select_day** event
-----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-select-day.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDModalDatePicker
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_modal_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def on_select_day(self, instance_date_picker, number_day):
                    instance_date_picker.dismiss()
                    MDSnackbar(
                        MDSnackbarSupportingText(
                            text=f"The selected day is {number_day}",
                        ),
                        y=dp(24),
                        orientation="horizontal",
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                        background_color="olive"
                    ).open()

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker()
                    date_dialog.bind(on_select_day=self.on_select_day)
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.material_resources import dp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.pickers import MDModalDatePicker
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open modal date picker dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_modal_date_picker,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def on_select_day(self, instance_date_picker, number_day):
                    instance_date_picker.dismiss()
                    MDSnackbar(
                        MDSnackbarSupportingText(
                            text=f"The selected day is {number_day}",
                        ),
                        y=dp(24),
                        orientation="horizontal",
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                        background_color="olive"
                    ).open()

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker()
                    date_dialog.bind(on_select_day=self.on_select_day)
                    date_dialog.open()


            Example().run()

**on_select_month** event
-------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-select-month.gif
    :align: center

.. code-block:: python

    def on_select_month(self, instance_date_picker, number_month):
        [...]

    def show_modal_date_picker(self, *args):
        [...]
        date_dialog.bind(on_select_month=self.on_select_month)
        [...]

**on_select_year** event
------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-select-year.gif
    :align: center

.. code-block:: python

    def on_select_year(self, instance_date_picker, number_year):
        [...]

    def show_modal_date_picker(self, *args):
        [...]
        date_dialog.bind(on_select_month=self.on_select_year)
        [...]

**on_cancel** event
-------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-cancel.gif
    :align: center

.. code-block:: python

    def on_cancel(self, instance_date_picker):
        [...]

    def show_modal_date_picker(self, *args):
        [...]
        date_dialog.bind(on_cancel=self.on_cancel)
        [...]

**on_ok** event
---------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-ok.gif
    :align: center

.. code-block:: python

    def on_ok(self, instance_date_picker):
        print(instance_date_picker.get_date()[0])

    def show_modal_date_picker(self, *args):
        [...]
        date_dialog.bind(on_ok=self.on_ok)
        [...]

**on_ok** with range event
--------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/modal-data-picker-event-on-ok-with-range.gif
    :align: center

.. tabs::

    .. tab:: Declarative python style with KV

        .. code-block:: python

            import datetime

            from kivy.lang import Builder
            from kivy.metrics import dp

            from kivymd.app import MDApp
            from kivymd.uix.pickers import MDModalDatePicker
            from kivymd.uix.snackbar import (
                MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
            )

            KV = '''
            MDScreen:
                md_bg_color: self.theme_cls.backgroundColor

                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_modal_date_picker()

                    MDButtonText:
                        text: "Open modal date picker dialog"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return Builder.load_string(KV)

                def on_ok(self, instance_date_picker):
                    MDSnackbar(
                        MDSnackbarText(
                            text="Selected dates is:",
                        ),
                        MDSnackbarSupportingText(
                            text="\\n".join(str(date) for date in instance_date_picker.get_date()),
                            padding=[0, 0, 0, dp(12)],
                        ),
                        y=dp(124),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                        padding=[0, 0, "8dp", "8dp"],
                    ).open()

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker(
                        mode="range",
                        min_date=datetime.date.today(),
                        max_date=datetime.date(
                            datetime.date.today().year,
                            datetime.date.today().month,
                            datetime.date.today().day + 4,
                        ),
                    )
                    date_dialog.bind(on_ok=self.on_ok)
                    date_dialog.open()


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            import datetime

            from kivymd.app import MDApp
            from kivymd.material_resources import dp
            from kivymd.uix.button import MDButton, MDButtonText
            from kivymd.uix.pickers import MDModalDatePicker
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.snackbar import (
                MDSnackbar, MDSnackbarSupportingText, MDSnackbarText
            )


            class Example(MDApp):
                def build(self):
                    self.theme_cls.primary_palette = "Olive"
                    return (
                        MDScreen(
                            MDButton(
                                MDButtonText(
                                    text="Open modal date picker dialog"
                                ),
                                id="button",
                                pos_hint={'center_x': .5, 'center_y': 0.5},
                                on_release=self.show_modal_date_picker,
                            ),
                            md_bg_color=self.theme_cls.backgroundColor
                        )
                    )

                def on_ok(self, instance_date_picker):
                    MDSnackbar(
                        MDSnackbarText(
                            text="Selected dates is:",
                        ),
                        MDSnackbarSupportingText(
                            text="\\n".join(
                                str(date) for date in instance_date_picker.get_date()),
                            padding=[0, 0, 0, dp(12)],
                        ),
                        y=dp(124),
                        pos_hint={"center_x": 0.5},
                        size_hint_x=0.5,
                        padding=[0, 0, "8dp", "8dp"],
                    ).open()

                def show_modal_date_picker(self, *args):
                    date_dialog = MDModalDatePicker(
                        mode="range",
                        min_date=datetime.date.today(),
                        max_date=datetime.date(
                            datetime.date.today().year,
                            datetime.date.today().month,
                            datetime.date.today().day + 4,
                        ),
                    )
                    date_dialog.bind(on_ok=self.on_ok)
                    date_dialog.open()


            Example().run()

API break
=========

1.2.0 version
-------------

.. code-block:: python

    date_dialog = MDDatePicker()
    date_dialog.open()

2.0.0 version
-------------

.. code-block:: python

    # date_dialog = MDModalDatePicker()
    # date_dialog = MDModalInputDatePicker()

    date_dialog = MDDockedDatePicker()
    date_dialog.open()
"""

# TODO: Should we implement a full-screen date picker dialog?
#  Implement a tooltip for time picker elements.
#  Should we implement the feature to settings custom colors for the
#  date picker dialogs?

from __future__ import annotations

__all__ = (
    "MDBaseDatePicker",
    "MDDockedDatePicker",
    "MDModalDatePicker",
    "MDModalInputDatePicker",
)

import calendar
import datetime
import os
from datetime import date
from itertools import zip_longest

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget

from kivymd import uix_path
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    CircularRippleBehavior,
    CommonElevationBehavior,
    RotateBehavior,
    ScaleBehavior,
)
from kivymd.uix.behaviors.motion_behavior import MotionDatePickerBehavior
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldHelperText,
    MDTextFieldHintText,
)

with open(
    os.path.join(uix_path, "pickers", "datepicker", "datepicker.kv"),
    encoding="utf-8",
) as kv_file:
    Builder.load_string(kv_file.read())


class MDDatePickerTypeDateError(Exception):
    pass


class MDBaseDatePicker(ThemableBehavior, MotionDatePickerBehavior, BoxLayout):
    """
    Implements the base class of the date picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivymd.uix.behaviors.motion_behavior.MotionDatePickerBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout` and
    classes documentation.

    :Events:
        :attr:`on_select_day`
            Fired when a day is selected.
        :attr:`on_select_month`
            Fired when a month is selected.
        :attr:`on_select_year`
            Fired when a year is selected.
        :attr:`on_cancel`
            Fired when the 'Cancel' button is pressed.
        :attr:`on_ok`
            Fired when the 'Ok' button is pressed.
        :attr:`on_edit`
            Fired when you click on the date editing icon.
        :attr:`on_dismiss`
            Fired when a date picker closes.
    """

    day = NumericProperty()
    """
    The day of the month to be opened by default. If not specified,
    the current number will be used.

    :attr:`day` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    month = NumericProperty()
    """
    The number of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`month` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    year = NumericProperty()
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    min_year = NumericProperty(1914)
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`min_year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `1914`.
    """

    max_year = NumericProperty(2121)
    """
    The year of month to be opened by default. If not specified,
    the current number will be used.

    :attr:`max_year` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `2121`.
    """

    mode = OptionProperty("picker", options=["picker", "range"])
    """
    Dialog type.
    Available options are: `'picker'`, `'range'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `picker`.
    """

    min_date = ObjectProperty(allownone=True)
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.


    :attr:`min_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    max_date = ObjectProperty(allownone=True)
    """
    The minimum value of the date range for the `'mode`' parameter.
    Must be an object <class 'datetime.date'>.

    :attr:`max_date` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    radius = VariableListProperty([dp(16)], length=4)
    """
    Container radius.

    :attr:`radius` is an :class:`~kivy.properties.VariableListProperty`
    and defaults to `[dp(16), dp(16), dp(16), dp(16)]`.
    """

    scrim_color = ColorProperty([0, 0, 0, 0.5])
    """
    Color for scrim in (r, g, b, a) or string format.

    :attr:`scrim_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[0, 0, 0, 0.5]`.
    """

    supporting_text = StringProperty("Select date")
    """
    Supporting text.

    :attr:`supporting_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Select date'`.
    """

    text_button_ok = StringProperty("Ok")
    """
    The text of the confirmation button.

    :attr:`text_button_ok` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Ok'`.
    """

    text_button_cancel = StringProperty("Cancel")
    """
    The text of the cancel button.

    :attr:`text_button_cancel` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Cancel'`.
    """

    mark_today = BooleanProperty(True)
    """
    Highlights the current day.

    :attr:`mark_today` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    is_open = BooleanProperty(False)
    """
    Is the date picker dialog open.

    :attr:`is_open` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    sel_year = NumericProperty()
    sel_month = NumericProperty()
    sel_day = NumericProperty()
    calendar_layout = ObjectProperty()

    _calendar_list = None
    _current_month_name = StringProperty()
    _current_full_month_name = StringProperty()
    _input_date_dialog_open = BooleanProperty(False)
    _select_year_dialog_open = False
    _date_label_text = StringProperty()

    __events__ = (
        "on_select_day",
        "on_select_month",
        "on_select_year",
        "on_cancel",
        "on_ok",
        "on_edit",
        "on_dismiss",
    )

    def __init__(
        self,
        year=None,
        month=None,
        day=None,
        firstweekday=0,
        **kwargs,
    ):
        self.today = date.today()
        self.calendar = calendar.Calendar(firstweekday)
        self.sel_year = year if year else self.today.year
        self.sel_month = month if month else self.today.month
        self.sel_day = day if day else self.today.day
        self.month = self.sel_month
        self.year = self.sel_year
        self.day = self.sel_day
        super().__init__(**kwargs)
        self.opacity = 0

        if self.max_date and self.min_date:
            if self.min_date and not isinstance(self.min_date, date):
                raise MDDatePickerTypeDateError(
                    "'min_date' must be of class <class 'datetime.date'>"
                )
            if self.max_date and not isinstance(self.max_date, date):
                raise MDDatePickerTypeDateError(
                    "'max_date' must be of class <class 'datetime.date'>"
                )
            self.compare_date_range()

        self.generate_list_widgets_days()
        self.update_calendar(self.sel_year, self.sel_month)

    def get_date(self, *args) -> list:
        """
        Returns a list of dates in the format
        [datetime.date(yyyy, mm, dd), ...].
        The list has two dates if you use a date interval.
        """

        if self.mode == "range":
            return self._get_date_range()
        else:
            return [date(self.sel_year, self.sel_month, self.sel_day)]

    def set_text_full_date(self) -> str:
        """Returns a string like  "Tue, Feb 2"."""

        def date_repr(date):
            return date.strftime("%b").capitalize() + " " + str(date.day)

        input_dates = (
            self._get_dates_from_fields()
            if hasattr(self, "_get_dates_from_fields")
            else None
        )
        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            if input_dates:
                selected_date = input_dates[0] or selected_date
            weekday_repr = selected_date.strftime("%a").capitalize()
            separator = ", "
            return weekday_repr + separator + date_repr(selected_date)
        elif self.mode == "range" and self.min_date and self.max_date:
            start, end = self.min_date, self.max_date
            if input_dates:
                start, end = input_dates[0] or start, input_dates[1] or end
            ends = [end for end in (start, end) if end]
            if len(ends) == 0:
                start_repr, end_repr = "Start", "End"
            else:
                start, end = min(ends), max(ends)
                start_repr, end_repr = date_repr(start), date_repr(end)
            separator = " — "
            return start_repr + separator + end_repr
        elif self.mode == "range" and not self.min_date and not self.max_date:
            dates = input_dates
            if not dates:
                return "Start - End"
            elif len(dates) == 1:
                return (
                    f"{date_repr(dates[0])}, "
                    f"{dates[0].strftime('%Y')} - "
                    f"End"
                )
            elif len(dates) == 2:
                return (
                    f"{date_repr(dates[0])}, {dates[0].strftime('%Y')} - "
                    f"{date_repr(dates[1])}, {dates[1].strftime('%Y')}"
                )

    def compare_date_range(self) -> None:
        # TODO: Add behavior if the minimum date range exceeds the maximum
        #  date range. Use toast?
        if self.max_date <= self.min_date:
            raise MDDatePickerTypeDateError(
                "`max_date` value cannot be less than or equal "
                "to 'min_date' value"
            )

    def change_month(self, operation: str) -> None:
        """
        Called when "chevron-left" and "chevron-right" buttons are pressed.
        Switches the calendar to the previous/next month.
        """

        month_delta = 1 if operation == "next" else -1
        year = self.year + (self.month - 1 + month_delta) // 12
        month = (self.month - 1 + month_delta) % 12 + 1

        if year <= 0:
            year, month = 1, 1
        self.update_calendar(year, month)
        self.dispatch("on_select_month", month)

    def generate_list_widgets_days(self) -> None:
        calendar_list = []

        for day in self.calendar.iterweekdays():
            weekday_label = MDDatePickerWeekdayLabel(
                text=calendar.day_name[day][0].upper(),
                date_picker=self,
            )
            self.calendar_layout.add_widget(weekday_label)
        for i in range(6 * 7):  # 6 weeks, 7 days a week
            day_selectable_item = MDDatePickerDaySelectableItem(
                is_week_end=i % 7 == 6,
                date_picker=self,
            )
            calendar_list.append(day_selectable_item)
            self.calendar_layout.add_widget(day_selectable_item)

        self._calendar_list = calendar_list

    def update_calendar(self, year, month) -> None:
        self.year, self.month = year, month
        if self.mode == "picker":
            selected_date = date(self.sel_year, self.sel_month, self.sel_day)
            selected_dates = {selected_date}
        else:
            selected_dates = {self.min_date, self.max_date}

        # The label text depends on the selected date or date range.
        self._update_date_label_text()
        month_end = date(year, month, calendar.monthrange(year, month)[1])
        dates = self.calendar.itermonthdates(year, month)

        for widget, widget_date in zip_longest(self._calendar_list, dates):
            # Only widgets whose dates are in the displayed month are visible.
            visible = (
                widget_date is not None
                and widget_date.month == month
                and widget_date.year == year
            )
            widget.text = str(widget_date.day) if visible else ""
            widget.is_today = visible and widget_date == self.today
            widget.is_selected = visible and (widget_date in selected_dates)

            if self.min_date and self.max_date and self.mode != "range":
                widget.disabled = True

            widget.is_in_range = (
                visible
                and self.min_date is not None
                and self.max_date is not None
                and self.min_date <= widget_date <= self.max_date
            )
            widget.is_range_start = (
                visible
                and self.min_date is not None
                and widget_date == self.min_date
            )
            widget.is_range_end = (
                visible
                and self.max_date is not None
                and widget_date == self.max_date
            )
            widget.is_month_end = widget_date == month_end

            if self.min_date and self.max_date and self.mode != "range":
                if widget.is_in_range:
                    widget.disabled = False

    def set_selected_widget(self, widget) -> None:
        if self._select_year_dialog_open or self._input_date_dialog_open:
            return

        try:
            widget_date = date(self.year, self.month, int(widget.text))
        except ValueError:
            return

        if self.mode == "picker":
            self.sel_year = widget_date.year
            self.sel_month = widget_date.month
            self.sel_day = widget_date.day
            self.update_calendar(self.sel_year, self.sel_month)
            self.dispatch("on_select_day", widget_date.day)
        elif self.mode == "range":
            ends = [end for end in (self.min_date, self.max_date) if end]
            if widget_date in ends:
                ends = [end for end in ends if end != widget_date]
            elif len(ends) < 2:
                ends.append(widget_date)
            else:
                start, end = min(ends), max(ends)
                if abs(widget_date - start).days < abs(widget_date - end).days:
                    start = widget_date
                else:
                    end = widget_date
                ends = [start, end]
            if len(ends) == 0:
                self.min_date, self.max_date = None, None
            else:
                self.min_date, self.max_date = min(ends), max(ends)
            self.update_calendar(self.year, self.month)

    def restore_calendar_layout_properties(self) -> None:
        self.ids.calendar_layout.padding = [dp(12), 0, dp(12), 0]
        Animation(opacity=1, d=0.2, t="out_quad").start(
            self.ids.calendar_layout
        )

    def set_calendar_layout_properties(self, method) -> None:
        anim = Animation(
            padding=[dp(18), 0, 0, 0], opacity=0, d=0.2, t="in_quad"
        )
        anim.bind(on_complete=method)
        anim.start(self.ids.calendar_layout)

    def dismiss(self, *args) -> None:
        """Dismiss the dialog date picker."""

        super().on_dismiss()
        self.is_open = False

    def open(self) -> None:
        """Show the dialog date picker."""

        if not self.is_open:
            Window.add_widget(self)
            super().on_open()
            self.is_open = True

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            self.dismiss()
            return True
        super().on_touch_down(touch)
        return True

    def on_select_day(self, *args) -> None:
        """Fired when a day is selected."""

    def on_select_month(self, *args) -> None:
        """Fired when a month is selected."""

    def on_select_year(self, *args) -> None:
        """Fired when a year is selected."""

    def on_cancel(self, *args) -> None:
        """Fired when the 'Cancel' button is pressed."""

    def on_ok(self, *args) -> None:
        """Fired when the 'Ok' button is pressed."""

    def on_edit(self, *args) -> None:
        """Fired when you click on the date editing icon."""

    def on_dismiss(self, *args) -> None:
        """Fired when a date picker closes."""

    def _update_date_label_text(self):
        self._current_month_name = (
            date(self.sel_year, self.sel_month, self.sel_day)
            .strftime("%b")
            .capitalize()
        )

    def _get_date_range(self) -> list:
        if not self.min_date or not self.max_date:
            return []
        date_range = [
            self.min_date + datetime.timedelta(days=x)
            for x in range((self.max_date - self.min_date).days + 1)
        ]
        return date_range


class MDDatePickerButtonsContainer(BoxLayout):
    """
    Implements a container with buttons for date picker dialogs.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """


class MDDatePickerBaseMenuSelectionButton(
    RotateBehavior, ButtonBehavior, MDIcon
):
    """
    Implements a button to switch the month/year selection menu for
    :class:`~MDDatePickerMonthSelectionButton` and
    :class:`~MDDatePickerYearSelectionButton` classes.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.rotate_behavior.RotateBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDIcon`
    classes documentation.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """


class MDDatePickerWeekdayLabel(MDLabel):
    """
    Implements labels for the names of the days of the week.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """


class MDCalendarLayout(ScaleBehavior, ThemableBehavior, GridLayout):
    """
    Implements a grid for calendar dates.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivymd.uix.behaviors.ThemableBehavior` and
    :class:`~kivy.uix.gridlayout.GridLayout`
    classes documentation.
    """


class MDDatePickerDaySelectableItem(
    CircularRippleBehavior, ButtonBehavior, MDLabel
):
    """
    Implements an element for a grid of calendar dates.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.ripple_behavior.CircularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.label.MDLabel`
    classes documentation.
    """

    date_picker = ObjectProperty()
    is_today = BooleanProperty(False)
    is_selected = BooleanProperty(False)
    is_in_range = BooleanProperty(False)
    is_range_start = BooleanProperty(False)
    is_range_end = BooleanProperty(False)
    is_month_end = BooleanProperty(False)
    is_week_end = BooleanProperty(False)

    def on_release(self):
        self.date_picker.set_selected_widget(self)


###############################################################################
#
#                                DOCKED CLASSES
#
###############################################################################


class MDDockedDatePickerBaseSelectionContainer(BoxLayout):
    """
    Implements a basic container for switching month/year items and selecting
    the month/year list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.boxlayout.BoxLayout` class documentation.
    """

    text = StringProperty()
    """
    The current name of the month or the current year.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    __events__ = ("on_release", "on_open_menu")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_open_menu(self, *args) -> None:
        """Fired when the 'menu-right' button are pressed."""

    def on_release(self, *args) -> None:
        """
        Fired when the 'chevron-left' and `chevron-right` buttons are pressed.
        """


class MDDockedDatePickerMonthSelectionItem(
    MDDockedDatePickerBaseSelectionContainer
):
    """
    Implements a container with buttons for switching months and selecting
    the month list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~MDDockedDatePickerBaseSelectionContainer` class documentation.
    """

    def on_open_menu(self, *args) -> None:
        """Fired when the 'menu-right' button are pressed."""

        if not self.date_picker._menu_month_year_selection_is_open:
            self.date_picker.generate_menu_month_year_selection(
                menu_type="month"
            )
            self.date_picker.open_close_menu_month_year_selection(
                state=True, menu_type="month"
            )
            self.date_picker._menu_month_year_selection_is_open = True
        else:
            self.date_picker.open_close_menu_month_year_selection(
                state=False, menu_type="month"
            )
            self.date_picker._menu_month_year_selection_is_open = False

    def on_release(self, direction: str) -> None:
        """
        Fired when the 'chevron-left' and chevron-right buttons are pressed.
        """

        def set_month(*args):
            self.date_picker.change_month(direction)
            self.date_picker._update_date_label_text()
            self.date_picker.restore_calendar_layout_properties()

        self.date_picker.set_calendar_layout_properties(set_month)


class MDDockedDatePickerYearSelectionItem(
    MDDockedDatePickerBaseSelectionContainer
):
    """
    Implements a container with buttons for switching years and selecting
    the year list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~MDDockedDatePickerBaseSelectionContainer` class documentation.
    """

    def on_open_menu(self, *args) -> None:
        """Fired when the 'menu-right' button are pressed."""

        if not self.date_picker._menu_month_year_selection_is_open:
            self.date_picker.generate_menu_month_year_selection(
                menu_type="year"
            )
            self.date_picker.open_close_menu_month_year_selection(
                state=True, menu_type="year"
            )
            self.date_picker._menu_month_year_selection_is_open = True
        else:
            self.date_picker.open_close_menu_month_year_selection(
                state=False, menu_type="year"
            )
            self.date_picker._menu_month_year_selection_is_open = False

    def on_release(self, direction: str) -> None:
        """
        Fired when the 'chevron-left' and chevron-right buttons are pressed.
        """

        def set_year(*args):
            self.date_picker.update_calendar(year, self.date_picker.month)
            self.date_picker.restore_calendar_layout_properties()

        year = self.date_picker.year
        if direction == "prev":
            year -= 1
        elif direction == "next":
            year += 1

        if year < self.date_picker.min_year or year > self.date_picker.max_year:
            raise MDDatePickerTypeDateError(
                "The maximum/minimum value of the year is exceeded or less "
                "than the set value"
            )
            return

        self.date_picker.set_calendar_layout_properties(set_year)


class MDDockedDatePickerMenuMonthYearSelection(ScaleBehavior, RecycleView):
    """
    Implements a menu with a list of months/years.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.recycleview.RecycleView` and
    classes documentation.
    """


class MDDockedDatePickerContainerMenuMonthYearSelection(
    FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout
):
    """
    Implements a container for the month/year list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.behaviors.FocusBehavior` and
    :class:`~kivy.uix.recycleview.layout.LayoutSelectionBehavior and
    :class:`~kivy.uix.recycleboxlayout.RecycleBoxLayout and
    classes documentation.
    """


class MDDockedDatePickerMenuSelectionItem(RecycleDataViewBehavior, BoxLayout):
    """
    Implements an item for the month selection list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.recycleview.views.RecycleDataViewBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    month_index = NumericProperty()
    """
    Month index.

    :attr:`month_index` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `0`.
    """

    month_year_name = StringProperty()
    """
    Full name of the month.

    :attr:`month_year_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            if self.menu_type == "month":
                self.date_picker.update_calendar(
                    self.date_picker.year, self.month_index
                )
                self.date_picker.dispatch("on_select_month", self.month_index)
            else:
                self.date_picker.update_calendar(
                    int(self.month_year_name), self.date_picker.month
                )
                self.date_picker.dispatch(
                    "on_select_year", int(self.month_year_name)
                )
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.data[index]["selected"] = is_selected


class MDDockedDatePicker(CommonElevationBehavior, MDBaseDatePicker):
    """
    Implements docked date picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseDatePicker`
    classes documentation.
    """

    _menu_month_year_selection_is_open = BooleanProperty(False)

    def generate_menu_month_year_selection(
        self, menu_type: str = "month"
    ) -> None:
        """Generates a list for the month or year selection menu."""

        self.ids.month_year_selection_layout.data = []

        if menu_type == "month":
            for month in range(1, 13):
                month_name = datetime.date(1, month, 1).strftime("%B")
                self.ids.month_year_selection_layout.data.append(
                    {
                        "height": dp(48),
                        "date_picker": self,
                        "menu_type": menu_type,
                        "month_year_name": month_name,
                        "month_index": month,
                        "viewclass": "MDDockedDatePickerMenuSelectionItem",
                    }
                )
        else:
            for year_name in range(self.min_year, self.max_year):
                self.ids.month_year_selection_layout.data.append(
                    {
                        "height": dp(48),
                        "date_picker": self,
                        "menu_type": menu_type,
                        "month_year_name": str(year_name),
                        "month_index": 0,
                        "viewclass": "MDDockedDatePickerMenuSelectionItem",
                    }
                )

    def open_close_menu_month_year_selection(
        self, state: bool = True, menu_type: str = "month"
    ) -> None:
        """
        Hides the calendar layout and opens the list to select the month or
        year.
        """

        opacity = 0 if state else 1
        scale = 1 if state else 0
        disabled = True if state else 0
        rotate = -90 if state else 0

        month_selection_items = self.ids.month_selection_items
        year_selection_items = self.ids.year_selection_items
        calendar_layout = self.ids.calendar_layout
        button_container = self.ids.button_container
        month_year_selection_layout = self.ids.month_year_selection_layout

        Animation(rotate_value_angle=rotate, d=0.2).start(
            month_selection_items.ids.menu_selection_button
            if menu_type == "month"
            else self.ids.year_selection_items.ids.menu_selection_button
        )

        month_selection_items.ids.chevron_left.disabled = disabled
        month_selection_items.ids.chevron_left.opacity = opacity
        month_selection_items.ids.chevron_right.disabled = disabled
        month_selection_items.ids.chevron_right.opacity = opacity

        year_selection_items.ids.chevron_left.disabled = disabled
        year_selection_items.ids.chevron_left.opacity = opacity
        year_selection_items.ids.chevron_right.disabled = disabled
        year_selection_items.ids.chevron_right.opacity = opacity

        calendar_layout.disabled = disabled
        calendar_layout.opacity = opacity
        if state:
            calendar_layout.scale_value_x = 1.1
            calendar_layout.scale_value_y = 1.1

        if menu_type == "month":
            year_selection_items.ids.label.disabled = disabled
            year_selection_items.ids.menu_selection_button.opacity = opacity
        else:
            month_selection_items.ids.label.disabled = disabled
            month_selection_items.ids.menu_selection_button.opacity = opacity

        month_year_selection_layout.size = (
            (
                self.width,
                self.height
                - (
                    self.ids.month_year_selection_items_container.height
                    + dp(56)
                ),
            )
            if state
            else (0, 0)
        )

        button_container.opacity = opacity
        button_container.disabled = disabled

        Animation(scale_value_x=scale, scale_value_y=scale, d=0.2).start(
            month_year_selection_layout
        )
        if not state:
            Animation(scale_value_x=1, scale_value_y=1, d=0.1).start(
                calendar_layout
            )


###############################################################################
#
#                                 MODAL CLASSES
#
###############################################################################


class MDModalDatePicker(CommonElevationBehavior, MDBaseDatePicker):
    """
    Implements modal date picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseDatePicker`
    classes documentation.
    """

    _menu_year_selection_is_open = BooleanProperty(False)

    def open(self) -> None:
        """Show the dialog date picker."""

        if not self.is_open:
            if not self._scrim:
                self._scrim = MDModalDatePickerScrim(color=self.scrim_color)

            Window.add_widget(self._scrim)
            Window.add_widget(self)
            super().on_open()
            self.is_open = True

    def generate_list_widgets_years(self) -> None:
        self.ids.year_selection_layout.data = []
        for i, number_year in enumerate(range(self.min_year, self.max_year)):
            self.ids.year_selection_layout.data.append(
                {
                    "date_picker": self,
                    "text": str(number_year),
                    "index": i,
                    "viewclass": "MDModalDatePickerYearSelectableItem",
                }
            )

    def open_menu_year_selection(self, *args) -> None:
        self._menu_year_selection_is_open = (
            not self._menu_year_selection_is_open
        )
        state = self._menu_year_selection_is_open
        opacity = 0 if state else 1
        disabled = True if state else 0
        rotate = -90 if state else 0

        calendar_layout = self.ids.calendar_layout
        year_selection_items = self.ids.year_selection_items
        year_selection_layout = self.ids.year_selection_layout
        chevron_left = year_selection_items.ids.chevron_left
        chevron_right = year_selection_items.ids.chevron_right
        chevron_left.disabled = disabled
        chevron_left.opacity = opacity
        chevron_right.disabled = disabled
        chevron_right.opacity = opacity
        calendar_layout.disabled = disabled
        calendar_layout.opacity = opacity

        Animation(rotate_value_angle=rotate, d=0.2).start(
            self.ids.year_selection_items.ids.menu_selection_button
        )

        year_selection_layout.size = (
            (calendar_layout.width - dp(36), calendar_layout.height)
            if state
            else (0, 0)
        )

        if state:
            year_selection_layout.disabled = False
            calendar_layout.scale_value_x = 1.1
            calendar_layout.scale_value_y = 1.1
            Animation(
                scale_value_x=1, scale_value_y=1, t="out_expo", d=0.4
            ).start(year_selection_layout)
        else:
            Animation(scale_value_x=1, scale_value_y=1, d=0.1).start(
                calendar_layout
            )
            year_selection_layout.scale_value_x = 1.2
            year_selection_layout.scale_value_y = 1.2
            year_selection_layout.disabled = True

    def _update_date_label_text(self):
        self._current_month_name = self.set_text_full_date()
        self._current_full_month_name = (
            f'{datetime.date(1, self.month, 1).strftime("%B")} {self.year}'
        )


class MDModalDatePickerYearSelectableItem(RecycleDataViewBehavior, MDLabel):
    """Implements an item for a pick list of the year."""

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            self.date_picker.update_calendar(
                int(self.text), self.date_picker.sel_month
            )
            self.date_picker.dispatch("on_select_year", int(self.text))
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.data[index]["selected"] = is_selected


class MDModalDatePickerYearSelectionItem(ScaleBehavior, BoxLayout):
    """
    Implements a container for switching month items.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivymd.uix.boxlayout.BoxLayout`
    classes documentation.
    """

    text = StringProperty()
    """
    The current name of the month or the current year.

    :attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    __events__ = ("on_release", "on_open_menu")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_open_menu(self, *args) -> None:
        """Fired when the 'menu-right' button are pressed."""

        self.date_picker.open_menu_year_selection()
        self.date_picker.generate_list_widgets_years()

    def on_release(self, direction: str) -> None:
        """
        Fired when the 'chevron-left' and `chevron-right` buttons are pressed.
        """

        def set_month(*args):
            self.date_picker.change_month(direction)
            self.date_picker._update_date_label_text()
            self.date_picker.restore_calendar_layout_properties()

        self.date_picker.set_calendar_layout_properties(set_month)


class MDModalDatePickerScrim(Widget):
    """
    Implements scrim for the modal date picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.widget.Widget` and class documentation.
    """

    color = ColorProperty(None)
    alpha = NumericProperty(0)


class MDModalDatePickerMenuYearSelection(ScaleBehavior, RecycleView):
    """
    Implements a menu with a list of years.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.scale_behavior.ScaleBehavior` and
    :class:`~kivy.uix.recycleview.RecycleView` and
    classes documentation.
    """


class MDModalDatePickerContainerMenuYearSelection(
    FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout
):
    """
    Implements a container for the year list menu.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.behaviors.FocusBehavior` and
    :class:`~kivy.uix.recycleview.layout.LayoutSelectionBehavior and
    :class:`~kivy.uix.recyclegridlayout.RecycleGridLayout and
    classes documentation.
    """


###############################################################################
#
#                              MODAL INPUT CLASSES
#
###############################################################################


class MDModalInputDatePicker(CommonElevationBehavior, MDBaseDatePicker):
    """
    Implements modal input date picker.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.behaviors.elevation.CommonElevationBehavior` and
    :class:`~MDBaseDatePicker`
    classes documentation.
    """

    date_format = OptionProperty(
        "mm/dd/yyyy",
        options=[
            "dd/mm/yyyy",
            "mm/dd/yyyy",
            "yyyy/mm/dd",
        ],
    )

    """
    Format of date strings that will be entered.
    Available options are: `'dd/mm/yyyy'`, `'mm/dd/yyyy'`, `'yyyy/mm/dd'`.

    :attr:`date_format` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `None`.
    """

    default_input_date = BooleanProperty(True)
    """
    If true, the current date will be set in the input field.

    :attr:`default_input_date` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    error_text = StringProperty("Invalid date format")
    """
    Error text when the date entered by the user is not valid.

    :attr:`error_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Invalid date format'`.
    """

    supporting_input_text = StringProperty("Enter date")
    """
    Auxiliary text when entering the date manually.

    :attr:`supporting_input_text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `'Enter date'`.
    """

    _date_format_strftime = {
        "dd/mm/yyyy": "%d/%m/%Y",
        "mm/dd/yyyy": "%m/%d/%Y",
        "yyyy/mm/dd": "%Y/%m/%d",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self._check_range, 0.1)

    def generate_list_widgets_days(self) -> None: ...

    def update_calendar(self, *args) -> None: ...

    def set_input_date(self, input_date: str) -> None:
        split_date = [d for d in input_date.split("/") if d]
        mask_date = self.date_format
        split_mask_date = mask_date.split("/")

        month_index = split_mask_date.index("mm")
        day_index = split_mask_date.index("dd")
        year_index = split_mask_date.index("yyyy")

        self.sel_month = int(split_date[month_index])
        self.sel_day = int(split_date[day_index])
        self.sel_year = int(split_date[year_index])

        month = self.sel_month
        day = self.sel_day
        year = self.sel_year
        full_month_name = datetime.datetime(year, month, day).strftime(
            "%d %B, %Y"
        )

        self._current_month_name = self.set_text_full_date()
        self._current_full_month_name = f"{full_month_name} {year}"

    def get_date(self, *args) -> list:
        """
        Returns a list of dates in the format
        [datetime.date(yyyy, mm, dd), ...].
        The list has two dates if you use a date interval.
        """

        return self._get_dates_from_fields()

    def get_current_date_from_format(self) -> str:
        """
        Returns the date according to the set format in :attr:`date_format`.
        """

        date_from_format = ""
        data_date = {
            "mm": self.sel_month,
            "dd": self.sel_day,
            "yyyy": self.sel_year,
        }
        split_mask_date = self.date_format.split("/")
        for mask in split_mask_date:
            date_from_format += f"{str(data_date[mask])}/"

        return date_from_format[:-1]

    def open(self) -> None:
        """Show the dialog date picker."""

        if not self.is_open:
            if not self._scrim:
                self._scrim = MDModalDatePickerScrim(color=self.scrim_color)

            Window.add_widget(self._scrim)
            Window.add_widget(self)
            super().on_open()
            self.is_open = True

    def _set_current_date(self):
        self.ids.input_date_field.text = self.today.strftime(
            self._date_format_strftime[self.date_format]
        )

    def _check_range(self, *args):
        if self.mode == "picker":
            self._set_current_date()
            return

        field_start = self.ids.input_date_field

        if self.min_date:
            field_start.text = self.min_date.strftime(
                self._date_format_strftime[self.date_format]
            )

        if self.max_date or self.mode == "range":
            input_date_container = self.ids.input_date_container
            input_date_container.spacing = "12dp"

            field_end = MDModalInputDatePickerInputField(
                MDTextFieldHintText(
                    text=self.date_format,
                ),
                MDTextFieldHelperText(
                    text=self.error_text,
                    mode="on_error",
                ),
                id="fffffff",
                date_picker=self,
                date_format=self.date_format,
                text=(
                    self.max_date.strftime(
                        self._date_format_strftime[self.date_format]
                    )
                    if self.max_date
                    else ""
                ),
            )
            input_date_container.add_widget(field_end)

    def _get_dates_from_fields(self) -> list:
        dates = []
        # Widgets are arranged in the reverse order of their addition.
        for field in reversed(self.ids.input_date_container.children):
            try:
                dates.append(
                    datetime.datetime.strptime(
                        field.text,
                        self._date_format_strftime[self.date_format],
                    ).date()
                )
            except ValueError:
                pass

        return dates


class MDModalInputDatePickerInputDateFieldContainer(BoxLayout):
    """
    Implements a text field for entering the date manually.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """


class MDModalInputDatePickerInputField(MDTextField):
    """
    Implements date input.

    .. versionadded:: 2.0.0

    For more information, see in the
    :class:`~kivymd.uix.textfield.textfield.MDTextField` class documentation.
    """

    date_picker: MDBaseDatePicker = ObjectProperty()
    """
    Date picker object -

    :attr:`date_picker` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def on_error(self, instance, value) -> None:
        """Fired when the `error` value changes."""

        super().on_error(instance, value)

        if not value:
            self.date_picker.set_input_date(self.text)
        else:
            self.date_picker._current_month_name = (
                self.date_picker.supporting_input_text
            )
