Unreleased
----------

    See on GitHub: `branch master <https://github.com/HeaTTheatR/KivyMD/tree/master>`_ | `compare 0.103.0/master <https://github.com/HeaTTheatR/KivyMD/compare/0.103.0...master>`_

    .. code-block:: bash

       pip install git+https://github.com/HeaTTheatR/KivyMD.git@master

* Fixed bug in :class:`kivymd.uix.expansionpanel.MDExpansionPanel` if, with the panel open, without closing it, try to open another panel, then the chevron of the first panel remained open.
* The :class:`kivymd.uix.textfield.MDTextFieldRound` class is now directly inherited from the :class:`kivy.uix.textinput.TextInput` class.
* Removed :class:`kivymd.uix.textfield.MDTextFieldClear` class.
* :class:`kivymd.uix.navigationdrawer.NavigationLayout` allowed to add :class:`kivymd.uix.toolbar.MDToolbar` class.
* Added ability to control range of dates to be active in :class:`kivymd.uix.picker.MDDatePicker` class.
* Updated :class:`kivymd.uix.navigationdrawer.MDNavigationDrawer` realization.
