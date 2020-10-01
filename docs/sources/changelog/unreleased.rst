Unreleased
----------

    See on GitHub: `branch master <https://github.com/kivymd/KivyMD/tree/master>`_ | `compare 0.104.1/master <https://github.com/kivymd/KivyMD/compare/0.104.1...master>`_

    .. code-block:: bash

       pip install https://github.com/kivymd/KivyMD/archive/master.zip

* Bug fixes and other minor improvements.
* Add `HotReloadViewer` class
* Added features to `Snackbar` class: use padding, set custom button color, elevation
* Add `MDToggleButton` class
* Change to `Material Design` `Baseline` dark theme spec
* Fix `ReferenceError: weakly-referenced object no longer exists` when start demo application
* Changed the default value for the `theme_text_color` parameter in the `BaseButton` class (to the value `"Primary"`)
* Fix setting of the `text_color_normal` and `text_color_active` parameters - earlier their values ​​did not affect anything
* Fixed the length of the right edge of the border in relation to the hint text when the `MDTextField` is in the `rectangle` mode
* Add `get_tab_list` method to `MDTabs` class
* Add hover behavior when using `MDDropdownMenu` class
* Added the feature to use the `FitImage` component to download images from the network
* The `elevation` value for `RectangularElevationBehavior` and `CircularElevationBehavior` classes after pressing was always set to `2` - fixed
* Methods that implement the ripple effect have always been called twice - fixed
* The `SmartTile` class now uses the `FitImage` class to display images instead of the `Image` class
* Removed dependency on `PIL` library
* Add `hint_bg_color`, `hint_text_color`, `hint_radius` attributes to `MDSlider` class
* Delete `progressloader.py`
* Delete `context_menu.py`
* Added the feature to control the properties of menu items during creation in `MDDropdownMenu` class
* Added the feature to change the number of buttons after creating the `MDFloatingActionButtonSpeedDial` object
* Added the feature to set the `font_name` property for the `MDTabsLabel` class
* Add `MDCarousel` class
* Delete `kivymd/uix/useranimationcard.py`
