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
* `Fix <https://github.com/kivymd/KivyMD/commit/941f52e94c5793eb1c1d02f2c9f6ba284860853b>`_ `MDTextField gets text color to black when disabled using dark theme <https://github.com/kivymd/KivyMD/issues/1410>`_.
* `Fix <https://github.com/kivymd/KivyMD/commit/9f428d88c333f4922fd4d29edd25feb94d589fd5>`_ (`45024f1 <https://github.com/kivymd/KivyMD/commit/4335dfbefb4e4c9677c9b1afc0c41186cdf6a538>`_) `MDLabel not change its color when theme is switched to "Dark" after switching screens <https://github.com/kivymd/KivyMD/issues/1403>`_.
* `Fix right/left icons color <https://github.com/kivymd/KivyMD/commit/04d3ef99ac0c5f0e33d44da02a4bc7e539a38e86>`_ - when the `MDTextField <https://kivymd.readthedocs.io/en/latest/components/textfield/>`_ is in the disabled state, the icon color has not changed.
* `Fix text colors <https://github.com/kivymd/KivyMD/commit/fd444ed2adecaa4bfe5cea1aeebeb9b4c09efcb3>`_ - when the `MDTextField <https://kivymd.readthedocs.io/en/latest/components/textfield/>`_ is in the disabled state nd at the same time in the error state, the colors of the hint text, helper text, max text length have not changed.
* `Fix <https://github.com/kivymd/KivyMD/commit/0aba528c44f5419a04b6f3e5144ac3d7a86e2b61>`_ `Bug on android related to shaders <https://github.com/kivymd/KivyMD/issues/1352>`_.
* `MDBottomSheet <https://kivymd.readthedocs.io/en/latest/components/bottomsheet/>`_ `API break <https://github.com/kivymd/KivyMD/commit/5f3e17017987981ff7a4d05362951c3a924199e2>`_. Now the `MDBottomSheet` class implements only the behavior of the bottom sheet. All custom content must be implemented by self.
* `Fix <https://github.com/kivymd/KivyMD/commit/d1d37df7206ba7dd2565a97b2dd9d1819a7cdf0e>`_ `Cannot set font_size when instantiating MDLabel <https://github.com/kivymd/KivyMD/issues/1435>`_.
* `Fix <https://github.com/kivymd/KivyMD/commit/b7cebbb945c07d7ecee81255b8dd8775d71ccf67>`_ widget size adjustment:

  - When we use the `adaptive_height/adaptive_width/adaptive_size` parameters, if the widget did not contain child widgets, then its size would be 100.
* `Add <https://github.com/kivymd/KivyMD/commit/81cd0bbb19be7bb6b67dfe6c0d0258a862ede1a2>`_ `radius` property to `MDProgressBar <https://kivymd.readthedocs.io/en/latest/components/progressbar/>`_ class.
* The material design style has been `changed <https://github.com/kivymd/KivyMD/commit/fbb087e01eb9fe116f945c717fcac617f792e6aa>`_. By default now `M3 <https://m3.material.io>`_.
* `Add <https://github.com/kivymd/KivyMD/commit/039536de44dc8a20bd280334be9e1a8ed9aa3b60>`_ `MDBottomAppBar <https://kivymd.readthedocs.io/en/latest/components/toolbar/#m3-style-bottom-app-bar>`_ `M3 <https://m3.material.io/components/bottom-app-bar/overview>`_ style.
* `Add <https://github.com/kivymd/KivyMD/commit/c5c1af1beba499644ec6352bede8f89a8914780f>`_ `new <https://github.com/kivymd/KivyMD/pull/1443>`_ properties to `MDScrollViewRefreshLayout <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#module-kivymd.uix.refreshlayout.refreshlayout>`_ class:

  - `spinner_color <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.spinner_color>`_;
  - `circle_color <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.circle_color>`_;
  - `show_transition <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.show_transition>`_;
  - `show_duration <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.show_duration>`_;
  - `hide_transition <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.hide_transition>`_;
  - `hide_duration <https://kivymd.readthedocs.io/en/latest/components/refreshlayout/#kivymd.uix.refreshlayout.refreshlayout.MDScrollViewRefreshLayout.hide_duration>`_;
* `Fix <https://github.com/kivymd/KivyMD/commit/fd40967d0e0bc5ad28bd5883247883870b2ab716>`_ `Adaptive_width and md_bg_color properties of MDLabel are not working correctly <https://github.com/kivymd/KivyMD/issues/1096>`_.
* `Add <https://github.com/kivymd/KivyMD/commit/57bfb2c4cf6026f4683b6a4ceb56c5d4c95ab6b4>`_ rounded corners for a `rectangle` type to `MDTextField <https://kivymd.readthedocs.io/en/latest/components/textfield/>`_ class.
* `Remove <https://github.com/kivymd/KivyMD/commit/e53778a75c9064dae11b5c282c47509a25125e3b>`_ `glsl_path` from `data` from `hook-kivymd.py` module.
* `Add <https://github.com/kivymd/KivyMD/commit/b1a9ae883f42faf09070dfeb1440fd95f45e8af9>`_ `SegmentedButton <https://kivymd.readthedocs.io/en/latest/components/segmentedbutton/>`_ widget.
* `MDSnackbar <https://kivymd.readthedocs.io/en/latest/components/snackbar/>`_ `API break <https://github.com/kivymd/KivyMD/commit/0a99c45c59d5e546f655a81bf225cb54b71aa34e>`_:

    - now the widget has become more customizable and closer to the standards of material design version 3.
* `Improved animation performance <https://github.com/kivymd/KivyMD/commit/528affe35163f7f0b7ede98fcdfade1ca01e6487>`_ for animate the `MDCheckbox <https://kivymd.readthedocs.io/en/latest/components/selectioncontrols/#mdcheckbox>`_ widget.
* `Add <https://github.com/kivymd/KivyMD/commit/9d1be15a4d6362acba4a99a85b2fb7491827d678>`_ the `feature to use parent and child checkboxes <https://kivymd.readthedocs.io/en/latest/components/selectioncontrols/#parent-and-child-checkboxes>`_ for `MDCheckbox <https://kivymd.readthedocs.io/en/latest/components/selectioncontrols/#mdcheckbox>`_.
* `MDChip <https://kivymd.readthedocs.io/en/latest/components/snackbar/>`_ `API break <https://github.com/kivymd/KivyMD/commit/0a99c45c59d5e546f655a81bf225cb54b71aa34e>`_:

    - now the widget has become more customizable and closer to the standards of material design version 3.
* `Fixed <https://github.com/kivymd/KivyMD/commit/d59f8e7112a943ae95c9c1cb4ca081a19b3fc14e>`_ elevation animation for buttons;
* `Improved performance <https://github.com/kivymd/KivyMD/commit/6d61cc70f8e40b15c0cee45ff701da364614ddf7>`_ and behavior of the `MDDropdownMenu <https://kivymd.readthedocs.io/en/latest/components/menu/>`_ class;
* `MDDropdownMenu <https://kivymd.readthedocs.io/en/latest/components/menu/>`_ `API break <>https://kivymd.readthedocs.io/en/latest/components/menu/#api-break`_;
* Added the `motion_behavior <https://kivymd.readthedocs.io/en/latest/behaviors/motion/#api-kivymd-uix-behaviors-motion-behavior>`_ module to the `behaviors` package to control the display/hide behavior of widgets;
* `Fixed <https://github.com/kivymd/KivyMD/commit/9d2e837a161ca45e0ac09d24cad2f22dd032aa4f>`_ scaling and rotation of widgets with elevation behavior;
