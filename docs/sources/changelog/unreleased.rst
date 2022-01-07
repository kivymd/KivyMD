Unreleased
----------

    See on GitHub: `branch master <https://github.com/kivymd/KivyMD/tree/master>`_ | `compare 0.104.2/master <https://github.com/kivymd/KivyMD/compare/0.104.2...master>`_

    .. code-block:: bash

       pip install https://github.com/kivymd/KivyMD/archive/master.zip

* Bug fixes and other minor improvements.
* Added `ImageLeftWidgetWithoutTouch`, `ImageRightWidgetWithoutTouch`, `IconRightWidgetWithoutTouch`, `IconLeftWidgetWithoutTouch` classes to *kivymd/uix/list.py* module;
* Added `MDStepper <https://kivymd.readthedocs.io/en/latest/components/stepper/>`_ component;
* Added a feature, `show_disks <https://kivymd.readthedocs.io/en/latest/components/filemanager/#kivymd.uix.filemanager.filemanager.MDFileManager.show_disks>`_ to the `MDFileManager <https://kivymd.readthedocs.io/en/latest/components/filemanager/#module-kivymd.uix.filemanager.filemanager>`_ class, that allows you to display the disks and folders contained in them;
* Added `animation_tooltip_dismiss <https://kivymd.readthedocs.io/en/latest/components/tooltip/#kivymd.uix.tooltip.tooltip.MDTooltip.animation_tooltip_dismiss>`_ function and `on_dismiss <https://kivymd.readthedocs.io/en/latest/components/tooltip/#kivymd.uix.tooltip.tooltip.MDTooltip.on_dismiss>`_ event to `MDTooltip <https://kivymd.readthedocs.io/en/latest/components/tooltip/#module-kivymd.uix.tooltip.tooltip>`_ class;
* Added `MDColorPicker <https://kivymd.readthedocs.io/en/latest/components/colorpicker/#module-kivymd.uix.pickers.colorpicker.colorpicker>`_ component;
* Added new `transition <https://github.com/kivymd/KivyMD/tree/master/kivymd/uix/transition>`_ package - a set of classes for implementing transitions between application screens;
* Now all modules from the `uix <https://github.com/kivymd/KivyMD/tree/master/kivymd/uix>`_ directory are packages;
* Type hints have been added to the source code of the KivyMD library;
* Added `divider_color <https://kivymd.readthedocs.io/en/latest/components/list/#kivymd.uix.list.list.BaseListItem.divider_color>`_ attribute to `BaseListItem <https://kivymd.readthedocs.io/en/latest/components/list/#kivymd.uix.list.list.BaseListItem>`_ class;
* Added `load_all_kv_files method <https://kivymd.readthedocs.io/en/latest/themes/material-app/#kivymd.app.MDApp.load_all_kv_files>`_ to `MDApp <https://kivymd.readthedocs.io/en/latest/themes/material-app/#kivymd.app.MDApp>`_ class;
* Added `Templates package <https://kivymd.readthedocs.io/en/latest/templates/>`_ - base classes for controlling the scale, rotation of the widget, etc.;
* Added `kivymd/tools/patterns <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/>`_ package - scripts for creating projects with design patterns;
* `FitImage` widget move from `kivymd.utils` to `kivymd.uix.fitimage`;
* Added `background_color_header <https://kivymd.readthedocs.io/en/latest/components/datatables/#kivymd.uix.datatables.datatables.MDDataTable.background_color_header>`_, `background_color_cell <https://kivymd.readthedocs.io/en/latest/components/datatables/#kivymd.uix.datatables.datatables.MDDataTable.background_color_cell>`_, `background_color_selected_cell <https://kivymd.readthedocs.io/en/latest/components/datatables/#kivymd.uix.datatables.datatables.MDDataTable.background_color_selected_cell>`_, added methods for adding/removing rows to a common table to `MDDataTable <https://kivymd.readthedocs.io/en/latest/components/datatables/#module-kivymd.uix.datatables.datatables>`_ widget;
* Delete `kivymd/utils/hot_reload_viewer.py`;
* Added `kivymd/tools/hotreload <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/hotreload/app/>`_ package;
* Added `top` value to `position <https://kivymd.readthedocs.io/en/latest/components/menu/#kivymd.uix.menu.menu.MDDropdownMenu.position>`_ parameter of `MDDropdownMenu <https://kivymd.readthedocs.io/en/latest/components/menu/#module-kivymd.uix.menu.menu>`_ class;
* Added `get_current_tab <https://kivymd.readthedocs.io/en/latest/components/tabs/#kivymd.uix.tab.tab.MDTabs.get_current_tab>`_ method to `MDTabs <https://kivymd.readthedocs.io/en/latest/components/tabs/>`_ class;
* Added the feature to automatically create a virtual environment when creating a project using the `kivymd.tools.patterns.create_project <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/>`_ tool;
* Added the feature to use the `left_icon <https://kivymd.readthedocs.io/en/latest/components/textfield/#kivymd.uix.textfield.textfield.MDTextField.icon_left>`_ for `MDTextField <https://kivymd.readthedocs.io/en/latest/components/textfield/#kivymd.uix.textfield.textfield.MDTextField>`_ text fields;
* The design and behavior of the `MDChip <https://kivymd.readthedocs.io/en/latest/components/chip/>`_ widget is close to the material design spec;
* Added the feature to set the thickness of the `MDProgressBar <https://kivymd.readthedocs.io/en/latest/components/progressbar/>`_ class;
* Added localization support when creating a project using the `create_project <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/>`_ tool;
* Added support `Material Design v3`;
* Added support badge icon to `MDIcon <https://kivymd.readthedocs.io/en/latest/components/label/#mdicon-with-badge-icon>`_ class;
* Added the feature to use a radius for the `BaseListItem` class;
* `MDFloatingActionButton <https://kivymd.readthedocs.io/en/latest/components/button/#mdfloatingactionbutton>`_ class `configured according to M3 <https://kivymd.readthedocs.io/en/latest/components/button/#material-design-style-3>`_ style;
* Ripple animation for round buttons customized to material design standards;
* `Fix <https://github.com/kivymd/KivyMD/pull/1141>`_ `Warning, too much iteration done before the next frame` for button classes;
* Added `FadingEdgeEffect class <https://kivymd.readthedocs.io/en/latest/effects/fadingedgeeffect/>`_
