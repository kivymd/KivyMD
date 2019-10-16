# Change Log


## [v0.101.8]() - *Alpha*

### setup.py:
* Added `uix` and `behaviors` folder to `package_data`


## [v0.101.7]() - *Alpha*

### demos/kitchen_sink/screens.py:
* Fixed colors and position of the buttons in the `Buttons` example
* Resource paths now use the variable `demos_assets_path`

### demos/kitchen_sink/main.py:
* Resource paths now use the variable `demos_assets_path`
* Added to display percent download kv-files

### demos/kitchen_sink/demo_apps:
* Resource paths now use the variable `demos_assets_path`

### demos/kitchen_sink/dialogs.py:
* Added to display percent download kv-files


## [v0.101.6]() - *Alpha*

### kivymd/uix/picker.py:
* Fixed `NameError: name 'MDThemePicker' is not defined`


## [v0.101.5]() - *Alpha*

### demos/kitchen_sink/screens.py:
* Added the ability to change color in the `MDIconItemForMdIconsList` class
* A context menu has been added to the `Toolbar` to show the source code of the current example

#### demos/kitchen_sink/main.py:
* Added names of authors of this fork in the description on the start screen
* Description text on the start screen has been added to `ScrollView`
* Changed the theme of the application to white style
* Now a window with a list of demo applications is created only once.
In the previous version, the window was always created when it was opened.
* A context menu has been added to the `Toolbar` to show the source code of the current example


* Edited with `Black` utility


## [v0.101.4]() - *Alpha*

#### demos/kitchen_sink/main.py:
* Fixed `ModuleNotFoundError: No module named 'kivymd.dialog'`

#### kivymd/uix/dropdownitem.py:
* Text color fixed - previously the text was white on a white background


## [v0.101.3]() - *Alpha*

#### kivymd/uix/bottomnavigation.py:
* Code updated to changes in version 0.101.0

### demos/kitchen_sink/screens.py:
* Changed the icons to `language-python` in the `Buttons` example

### demos/kitchen_sink/dialogs.py:
* Renamed `BaseDialog` to `BaseDialogForLoadKvFiles` class (Fixed AttributeError: `'MDDialog' object has no attribute 'canvas_color'`)


## [v0.101.2]() - *Alpha*

#### demos/kitchen_sink/main.py:
* Fixed `AttributeError: 'KitchenSink' object has no attribute 'bs_menu_2'`

#### kivymd/uix/bottomsheet.py:
* Fixed Fixed `Unable to import package 'kivymd.label.MDLabel'`


## [v0.101.1]() - *Alpha*

#### kivymd/uix/bottomnavigation.py:
* Fixed  `ModuleNotFoundError: No module named 'kivymd.uix.elevation'`
* Fixed `ModuleNotFoundError: No module named 'kivymd.uix.backgroundcolorbehavior'`


## [v0.101.0]() - *Alpha*

#### kivymd/textfields.py:
* Added ability to resize text field in `MDTextFieldRound` class
* Added values `icon_left_color` and `icon_right_color` in `MDTextFieldRound` class
* Fixed `ReferenceError` in `MDTextFieldRound` class

#### kivymd/cards.py:
* Added doc string to `MDCard` class
* Added color property to `MDSeparator` class

#### kivymd/button.py:
* Added new doc in buttons
* Fixed: the text color in the button did not change
* Added the ability to change the font size in the `MDIconButton`

#### demos/kitchen_sink/screens.py:
* Methods for loading kv-files moved to the `main.py` file
* Added new example for `bottom navigation` screen
* Added new example for `popup screen` screen
* Added new example with `MDTextField`
* Added new example with `MDDropDownItem`
* Removed `Accordion List` screen
* Updated example for `buttons` screen
* Updated `BottomNavigation` example
* Deleted imports inside kv-files
* Edited imports

#### demos/kitchen_sink/main.py:
* Added dialog for preloading kv-files in the `Kitchen Sink` application
* Edited method `show_popup_screen` for new example `popup screen` screen
* Added new example with `MDDropDownItem`
* Removed `Accordion List` screen
* Corrected image proportions in the `MDCard` example
* Corrected image proportions in the `MDUserAnimationCard` example

#### kivymd/bottomnavigation.py:
* Added new doc
* Added the ability to set the color of the `MDBottomNavigation` panel

#### kivymd/popupscreen.py:
* Fixed the behavior of `MDPopupScreen`, which was closed when own events
* Added the ability to close `MDPopupScreen` with swipe down
* Added the ability to set the color and background image for `MDPopupScreen`
* Added new example in doc string

#### kivymd/managerswiper.py:
* Added `return super().on_touch_down(touch)` to `on_touch_down` method

#### setup.py
* Added `requests` to requires section

#### kivymd/menus.py:
* Added `on_dismiss` method - same behavior as `ModalView`

#### kivymd/behaviors/hover_behavior.py:
* Added Hoverable Behaviour (changing when the mouse is on the widget by O. Poyen

#### kivymd/context_menu.py:
* Added new module context_menu.py

#### kivymd/toast/kivytoast/kivytoast.py:
* Added doc-string
* Added `duration` value for to control the timing of the toast



* Removed `accordion.py`, `accordionlistitem.py` modules - see `expansionpanel.py` module


## [v0.100.2](https://github.com/HeaTTheatR/KivyMD/tree/1fa2e59) - *Alpha*

* Formatted code using [Black](https://github.com/psf/black) utility


## [v0.100.1]() - *Alpha*

* Fixed "Due to the use of `AsyncImage`, the Toolbar did not accept the color of the installed color theme"


## [v0.100.0]() - *Alpha*

* Fixed "In `MDNavigationDrawer` I used use_logo='all' it's showing image only not the drawer_title text"


## [v0.99.98]() - *Alpha*

* Added new `MDFillRoundFlatIconButton` class


## [v0.99.97]() - *Alpha*

* Fixed "Spinner closes after updating the screen"


## [v0.99.96]() - *Alpha*

* Added asynchronous call to list update method in RefreshLayout example in main.py file
* Added `asynckivy.py` module for using asynchronous function calls in `Kivy`


## [v0.99.95]() - *Alpha*

* Added function to create a round image in `kivymd/utils/cropimage.py` module
* Added new `MDCustomRoundIconButton` class in `kivymd/button.py` module
* Added demo application [Account Page](https://www.youtube.com/watch?v=dfUOwqtYoYg)


## [v0.99.94]() - *Alpha*

* Added property `_no_ripple_effect` to `BaseListItem` class
* [Banned](https://www.youtube.com/watch?v=P_9oSx0Pz_U) use `ripple effect` in `MDAccordionListItem` class
* Added check to use `ripple effect` in RectangularRippleBehavior class


## [v0.99.93]() - *Alpha*

* Updated Material Design Iconic font (v3.6.95)


## [v0.99.92]() - *Alpha*

* Removed automatic change of text field length in the `MDTextFieldRound` class
