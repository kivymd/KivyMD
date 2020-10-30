"""
Components
==========

Components is a project to centralize addons for KivyMD maintained by users.
All the components packages are centralized on the `kivymd-components Github
<https://github.com/kivymd-components>`_ repository.

.. warning::
    The components are contributed by regular users such as yourself.
    The KivyMD developers do not take any responsibility for the code
    hosted in the component organization repositories - we do not actively
    monitor these repos. Please use at your own risk.

Legacy components tool instructions
-----------------------------------

Component is now distributed as a separate Python module, kivymd-components.
You can install it with pip::

    pip install kivymd-components

The components does not initially include any packages. You can download
them with the component tool installed by the pip package::

    # Installing a components
    components install SweetAlert

    # Upgrade a components
    components install --upgrade SweetAlert

    # Uninstall a components
    components uninstall SweetAlert

    # List all the components installed
    components list

    # Show the help
    components --help

All the components are installed by default in `~/.kivymd/components`.

Packaging
~~~~~~~~~

If you want to include components in your application, you can add `--app`
to the `install` command. This will create a `libs/components` directory in your
current directory which will be used by `kivymd.components`.

For example::

    cd myapp
    components install --app SweetAlert
"""

__path__ = "kivymd.components"

import imp
import sys
from os.path import abspath, dirname, exists, join, realpath, sep

from kivy.utils import platform

import kivymd
from kivymd import kivymd_home_dir

components_system_dir = kivymd_home_dir
components_kivymd_dir = abspath(dirname(kivymd.__file__))

# Application path where components modules can be installed.
if getattr(sys, "frozen", False) and getattr(sys, "_MEIPASS", False):
    components_app_dir = sys._MEIPASS
else:
    components_app_dir = realpath(dirname(sys.argv[0]))
components_app_dir = join(components_app_dir, "libs")

# Fixes issue #4030 in kivy where components path is incorrect on iOS.
if platform == "ios":
    import __main__

    main_py_file = __main__.__file__
    components_app_dir = dirname(main_py_file)


class ComponentsImporter:
    def find_module(self, fullname, path):
        if path == "kivymd.components":
            return self

    def load_module(self, fullname):
        assert fullname.startswith("kivymd")

        moddir = join(components_kivymd_dir, fullname.split(".", 2)[-1])
        if exists(moddir):
            return self._load_module(fullname, moddir)

        modname = fullname.split(".", 1)[-1]
        modname = sep.join(modname.split("."))

        for directory in (components_app_dir, components_system_dir):
            moddir = join(directory, modname)
            if exists(moddir):
                return self._load_module(fullname, moddir)

    def _load_module(self, fullname, moddir):
        mod = imp.load_module(
            fullname, None, moddir, ("", "", imp.PKG_DIRECTORY)
        )
        return mod


# Insert the components importer as ultimate importer.
sys.meta_path.append(ComponentsImporter())
