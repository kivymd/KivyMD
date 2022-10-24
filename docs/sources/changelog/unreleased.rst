Unreleased
----------

    See on GitHub: `branch master <https://github.com/kivymd/KivyMD/tree/master>`_ | `compare 1.1.1/master <https://github.com/kivymd/KivyMD/compare/1.1.1...master>`_

    .. code-block:: bash

       pip install https://github.com/kivymd/KivyMD/archive/master.zip

* Bug fixes and other minor improvements.
* `Add <https://github.com/kivymd/KivyMD/pull/1392>`_ icon color property to `right_action_items/left_action_items` in `MDTopAppBar <https://kivymd.readthedocs.io/en/latest/components/toolbar/>`_ class.
* `Add feature for changing the scale of the shadow <https://github.com/kivymd/KivyMD/commit/5b14aea97ca67efbab9bd814ed0a7cc7bcb57863>`_ for `CommonElevationBehavior <https://kivymd.readthedocs.io/en/latest/behaviors/elevation/#kivymd.uix.behaviors.elevation.CommonElevationBehavior>`_ class.
* `Add <https://github.com/kivymd/KivyMD/commit/86d206f4e5122d3af6968a00a8cc2144b2697955>`_ `elevation properties <https://kivymd.readthedocs.io/en/latest/components/datatables/#kivymd.uix.datatables.datatables.MDDataTable.shadow_radius>`_ to `MDDataTable <https://kivymd.readthedocs.io/en/latest/components/datatables/#api-kivymd-uix-datatables-datatables>`_ class.
* `Add <https://kivymd.readthedocs.io/en/latest/components/menu/#kivymd.uix.menu.menu.MDDropdownMenu.shadow_radius>`_ to `MDDropdownMenu <https://kivymd.readthedocs.io/en/latest/components/menu/#api-kivymd-uix-menu-menu>`_ class.
* `Add <https://github.com/kivymd/KivyMD/pull/1394>`_ `on_copy <https://kivymd.readthedocs.io/en/latest/components/label/#kivymd.uix.label.label.MDLabel.on_copy>`_ event to `MDLabel <https://kivymd.readthedocs.io/en/latest/components/label/#api-kivymd-uix-label-label>`_ class.
* `Add <https://github.com/kivymd/KivyMD/commit/6c4484326f8d38aa288bba890c2b4b868909ab6e>`_ feature to highlight a label with a double tap to `MDLabel <https://kivymd.readthedocs.io/en/latest/components/label/#kivymd.uix.label.label.MDLabel>`_ class.
* `Add <https://github.com/kivymd/KivyMD/commit/fbb01d8e54cb9534b2d661be5a64bb8f119d887a>`_ feature to use text markup in the `toast <https://kivymd.readthedocs.io/en/latest/api/kivymd/toast/kivytoast/kivytoast/>`_ label.
* Fix `MDDatePicker <https://kivymd.readthedocs.io/en/latest/components/datepicker/>`_ widget:

  - `Make day widgets non-clickable when another dialog is open <https://github.com/kivymd/KivyMD/pull/1391>`_;
  - `Refactor input fields and fix some bugs <https://github.com/kivymd/KivyMD/pull/1390>`_;
* `Fix <https://github.com/kivymd/KivyMD/commit/e9ec26283fd6ddf5f436168f918797de16f46c79>`_ `MDDropdownMenu position isn't working <https://github.com/kivymd/KivyMD/issues/1333>`_.
* `Fix <https://github.com/kivymd/KivyMD/commit/905611d6c5d8553c4ca6bd5ee1c4d2d7ee726c8d>`_ `switching between a dark and light theme causes most of the MDTextField widget elements not to update their colors when changing the theme <https://github.com/kivymd/KivyMD/pull/740#issuecomment-1287252715>`_.
* `Fix <https://github.com/kivymd/KivyMD/commit/2af018b00ca6897b42ca01bbed687dab62efd7fd>`_ `incorrect md_bd_color behavior <https://github.com/kivymd/KivyMD/issues/1396>`_ of `MDLabel <https://kivymd.readthedocs.io/en/latest/components/label/#mdlabel>`_ class.
* `Fix <https://github.com/kivymd/KivyMD/commit/b4eef1a52a24e540b8a2863fbd9f43c45291cbbe>`_ `changing theme doesn't work as expected with MDDataTable <https://github.com/kivymd/KivyMD/issues/1399>`_.
* `Fix <https://github.com/kivymd/KivyMD/commit/90d7e1b992ea9e4d07abe9f11917141a5980711b>`_ on_long_touch method call for `TouchBehavior <https://kivymd.readthedocs.io/en/latest/behaviors/touch/#api-kivymd-uix-behaviors-touch-behavior>`_ class - the `on_long_touch` method was called at the `on_touch_down` event.
