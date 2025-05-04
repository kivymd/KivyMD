"""
Script creates a project with the MVC pattern
=============================================

.. versionadded:: 1.0.0

.. seealso::

    `MVC pattern <https://en.wikipedia.org/wiki/Model–view–controller>`_

.. rubric:: Use a clean architecture for your applications.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/preview-mvc.png
    :align: center

Use a clean architecture for your applications. KivyMD allows you to quickly
create a project template with the MVC pattern. So far, this is the only
pattern that this utility offers. You can also include database support in
your project. At the moment, support for the Firebase database
(the basic implementation of the real time database) and RestDB
(the full implementation) is available.

Project creation
----------------

Template command::

    kivymd.create_project \\
        name_pattern \\
        path_to_project \\
        name_project \\
        python_version \\
        kivy_version

Example command::

    kivymd.create_project \\
        MVC \\
        /Users/macbookair/Projects \\
        MyMVCProject \\
        python3.10 \\
        2.1.0

This command will by default create a project with an MVC pattern.
Also, the project will create a virtual environment with Python 3.10,
Kivy version 2.1.0 and KivyMD master version.

.. note::
    Please note that the Python version you specified must be installed on your
    computer.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mvc-base.png
    :align: center

Creating a project using a database
-----------------------------------

.. note::
    Note that in the following command, you can use one of two database names:
    'firebase' or 'restdb'.

Template command::

    kivymd.create_project \\
        name_pattern \\
        path_to_project \\
        name_project \\
        python_version \\
        kivy_version \\
        --name_database

Example command::

    kivymd.create_project \\
        MVC \\
        /Users/macbookair/Projects \\
        MyMVCProject \\
        python3.10 \\
        2.1.0 \\
        --name_database restdb

This command will create a project with an MVC template by default.
The project will also create a virtual environment with Python 3.10,
Kivy version 2.1.0, KivyMD master version and a wrapper for working with
the database restdb.io.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mvc-database.png
    :align: center

.. code-block:: python

    class DataBase:
        def __init__(self):
            database_url = "https://restdbio-5498.restdb.io"
            api_key = "7ce258d66f919d3a891d1166558765f0b4dbd"

.. note::
    Please note that `database.py` the shell in the `DataBase` class uses the
    `database_url` and `api_key` parameters on the test database (works only in read mode),
    so you should use your data for the database.

Create project with hot reload
------------------------------

Template command::

    kivymd.create_project \\
        name_pattern \\
        path_to_project \\
        name_project \\
        python_version \\
        kivy_version \\
        --use_hotreload

Example command::

    kivymd.create_project \\
        MVC \\
        /Users/macbookair/Projects \\
        MyMVCProject \\
        python3.10 \\
        2.1.0 \\
        --use_hotreload yes

After creating the project, open the file `main.py`, there is a lot of useful
information. Also, the necessary information is in other modules of the project
in the form of comments. So do not forget to look at the source files of the
created project.

Create project with responsive view
-----------------------------------

When creating a project, you can specify which views should use responsive
behavior. To do this, specify the name of the view/views in the
`--use_responsive` argument:

Template command::

    kivymd.create_project \\
        name_pattern \\
        path_to_project \\
        name_project \\
        python_version \\
        kivy_version \\
        --name_screen FirstScreen SecondScreen ThirdScreen \\
        --use_responsive FirstScreen SecondScreen

The `FirstScreen` and `SecondScreen` views will be created with an responsive
architecture. For more detailed information about using the adaptive view, see
the `MDResponsiveLayout <https://kivymd.readthedocs.io/en/latest/components/responsivelayout/>`_
widget.

Others command line arguments
=============================

Required Arguments
------------------

- pattern
    - the name of the pattern with which the project will be created

- directory
    - directory in which the project will be created

- name
    - project name

- python_version
    - the version of Python (specify as `python3.9` or `python3.8`) with
    - which the virtual environment will be created

- kivy_version
    - version of Kivy (specify as `2.1.0` or `master`) that will be used in the project

Optional arguments
------------------

- name_screen
    - the name of the class which be used when creating the project pattern

When you need to create an application template with multiple screens,
use multiple values separated by a space for the `name_screen` parameter,
for example, as shown below:

Template command::

    kivymd.create_project \\
        name_pattern \\
        path_to_project \\
        name_project \\
        python_version \\
        kivy_version \\
        --name_screen FirstScreen SecondScreen ThirdScreen

- name_database
    - provides a basic template for working with the 'firebase' library
    - or a complete implementation for working with a database 'restdb.io'

- use_hotreload
    - creates a hot reload entry point to the application

- use_localization
    - creates application localization files

- use_responsive
    - the name/names of the views to be used by the responsive UI

.. warning:: On Windows, hot reloading of Python files may not work.
    But, for example, there is no such problem in macOS. If you fix this,
    please report it to the KivyMD community.
"""

__all__ = [
    "main",
]

import os
import re
import shutil
from typing import Union

from kivy import Logger, platform

from kivymd import path as kivymd_path
from kivymd.tools.argument_parser import ArgumentParserWithHelp

temp_basemodel = '''# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """

        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed()
                break
'''

temp_database_model = '''import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class {name_screen}Model(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.{name_screen}.{module_name}.{name_screen}View` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.{name_screen}.{module_name}.{name_screen}View` about the
        # changes that have occurred in the data model.
        self.notify_observers({notify_name_screen})

    @multitasking.task
    def check_data(self):
        """Just an example of the method. Use your own code."""

        self.data = ["example item"]
'''

temp_without_database_model = '''from Model.base_model import BaseScreenModel


class {name_screen}Model(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.{module_name}.{name_screen}.{name_screen}View` class.
    """'''

temp_screens_imports = """# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


"""

temp_code_responsive_view = '''from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.{name_screen}.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView


class {name_screen}View(MDResponsiveLayout, BaseScreenView):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
'''

temp_responsive_component_imports = """from .platforms.MobileScreen.mobile_screen import MobileScreenView
from .platforms.TabletScreen.tablet_screen import TabletScreenView
from .platforms.DesktopScreen.desktop_screen import DesktopScreenView
"""

temp_responsive_platform_baseclass = """from kivymd.uix.screen import MDScreen


class {}View(MDScreen):
    pass
"""

temp_code_view = '''from View.base_screen import BaseScreenView


class {name_screen}View(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
'''

temp_code_controller = '''{import_module}


class {name_screen}Controller:
    """
    The `{name_screen}Controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.{module_name}.{name_screen}Model
        self.view = {name_view}(controller=self, model=self.model)

    def get_view(self) -> {get_view}:
        return self.view
'''

temp_base_screen = '''from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from Utility.observer import Observer


class BaseScreenView(MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.controller_screen.ClassScreenControler`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.model_screen.ClassScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
'''

temp_utility = '''
# Of course, "very flexible Python" allows you to do without an abstract
# superclass at all or use the clever exception `NotImplementedError`. In my
# opinion, this can negatively affect the architecture of the application.
# I would like to point out that using Kivy, one could use the on-signaling
# model. In this case, when the state changes, the model will send a signal
# that can be received by all attached observers. This approach seems less
# universal - you may want to use a different library in the future.


class Observer:
    """Abstract superclass for all observers."""

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """
'''

temp_hot_reload_main = '''
"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

import importlib
import os

from kivy import Config

from PIL import ImageGrab

# TODO: You may know an easier way to get the size of a computer display.
resolution = ImageGrab.grab().size

# Change the values of the application window size as you need.
Config.set("graphics", "height", resolution[1])
Config.set("graphics", "width", "400")

from kivy.core.window import Window{}

# Place the application window on the right side of the computer screen.
Window.top = 0
Window.left = resolution[0] - Window.width

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
{}{}

class {}(MDApp):
    KV_DIRS = [os.path.join(os.getcwd(), "View")]{}

    def build_app(self) -> MDScreenManager:
        """
        In this method, you don't need to change anything other than the
        application theme.
        """

        import View.screens

        self.manager_screens = MDScreenManager(){}{}
        Window.bind(on_key_down=self.on_keyboard_down)
        importlib.reload(View.screens)
        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]({})
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

        return self.manager_screens

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        """
        The method handles keyboard events.

        By default, a forced restart of an application is tied to the
        `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
        """

        if "meta" in modifiers or "ctrl" in modifiers and text == "r":
            self.rebuild(){}{}


{}().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.
'''

temp_main = '''"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
{}
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from View.screens import screens{}
{}

class {}(MDApp):{}
    def __init__(self, **kwargs):
        super().__init__(**kwargs){}
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()
        {}
    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]({})
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)
{}{}

{}().run()
'''

temp_makefile = """# FILE TO FIND AND CREATE LOCALIZATION FILES FOR YOUR APPLICATION. \\
\\
In this file, you can specify in which files of your project to search for \\
localization strings. \\
These files should be listed in the below command: \\
\\
\\
xgettext -Lpython --output=messages.pot --from-code=utf-8 \\
    path/to/file-1 \\
    path/to/file-2 \\
    ...

.PHONY: po mo

po:
    xgettext -Lpython --output=messages.pot --from-code=utf-8 \\
{}
    msgmerge --update --no-fuzzy-matching --backup=off data/locales/po/en.po messages.pot
    msgmerge --update --no-fuzzy-matching --backup=off data/locales/po/ru.po messages.pot

mo:
    mkdir -p data/locales/en/LC_MESSAGES
    mkdir -p data/locales/ru/LC_MESSAGES
    msgfmt -c -o data/locales/en/LC_MESSAGES/%s.mo data/locales/po/en.po
    msgfmt -c -o data/locales/ru/LC_MESSAGES/%s.mo data/locales/po/ru.po
"""

firebase_requirements = """kivy==2.1.0
kivymd==1.0.0
multitasking
firebase
firebase-admin
python_jwt
gcloud
sseclient
pycryptodome==3.4.3
requests_toolbelt
"""

without_firebase_requirements = """kivy==2.1.0
kivymd==1.0.0
"""

available_patterns = ["MVC"]
available_databases = ["firebase", "restdb"]

path_to_project = ""
project_name = ""
use_localization = ""
name_database = ""
use_hotreload = ""
temp_makefile_files = ""
temp_screens_data = ""
kivy_version = ""
python_version = ""


def main():
    """Project creation function."""

    global project_name
    global use_localization
    global name_database
    global use_hotreload
    global temp_makefile_files
    global temp_screens_data
    global path_to_project
    global kivy_version
    global python_version

    parser = create_argument_parser()
    args = parser.parse_args()

    pattern_name = args.pattern
    project_directory = args.directory
    project_name = "".join(args.name.split(" "))
    kivy_version = args.kivy_version
    python_version = args.python_version
    if "3" not in python_version:
        parser.error("Python must be at least version 3")
    name_screen = args.name_screen
    path_to_project = os.path.join(project_directory, project_name)
    name_database = args.name_database
    if name_database != "no" and name_database not in available_databases:
        parser.error(
            f"The database name must be one of the {available_databases} list"
        )
    use_hotreload = args.use_hotreload
    use_localization = args.use_localization
    use_responsive = args.use_responsive

    # Check arguments.
    for name in name_screen:
        if name[-6:] != "Screen":
            parser.error(
                f"The name of the {name} screen should contain the word "
                f"'Screen' at the end.\n"
                "For example - '--name_screen MyFirstScreen ...'"
            )
    if not os.path.exists(
        os.path.join(kivymd_path, "tools", "patterns", pattern_name)
    ):
        parser.error(
            f"There is no {pattern_name} pattern.\n"
            f"Only {available_patterns} template is available."
        )

    # Call the functions of creating a project.
    if not os.path.exists(path_to_project):
        shutil.copytree(
            os.path.join(kivymd_path, "tools", "patterns", pattern_name),
            path_to_project,
        )
        create_main()

        for name in name_screen:
            module_name = chek_camel_case_name_project(name)
            if not module_name:
                parser.error(
                    "The name of the screen should be written in camel case style. "
                    "\nFor example - 'MyFirstScreen'"
                )
            module_name = "_".join([name.lower() for name in module_name])

            # Create models module.
            create_model(name, module_name, name_database, path_to_project)
            # Create controllers module.
            create_controller(name, module_name, use_hotreload, path_to_project)
            # Create screens data.
            create_screens_data(name, module_name)
            if use_localization == "yes":
                # Create makefile data.
                create_makefile_data(name, module_name)
            # Create views.
            create_view(name, module_name, use_responsive, path_to_project)

        # Create module `NameProject/View/NameScreen/components/common/__init__.py`.
        create_common_responsive_module(use_responsive, path_to_project)
        # Create module `NameProject/View/screens.py`.
        create_module_screens()
        # Create module `NameProject/Model/base_model.py`.
        create_basemodel()
        # Create module `NameProject/View/base_screen.py`.
        create_module_basescreen()
        # Create package `NameProject/Utility`.
        create_package_utility()
        # Create file `NameProject/Makefile`.
        if use_localization == "yes":
            # Create makefile data.
            create_makefile()

        create_requirements()
        os.makedirs(os.path.join(path_to_project, "assets", "images"))
        os.mkdir(os.path.join(path_to_project, "assets", "fonts"))

        if name_database != "no":
            check_databases()

        if use_hotreload == "yes":
            create_main_with_hotreload()
            with open(
                os.path.join(path_to_project, "requirements.txt"),
                "a",
                encoding="utf-8",
            ) as requirements:
                requirements.write("watchdog")

        if use_localization == "yes":
            Logger.info("KivyMD: Create localization files...")
            os.chdir(path_to_project)
            os.system("make po")
            os.system("make mo")
        else:
            os.remove(os.path.join(path_to_project, "messages.pot"))
            os.remove(os.path.join(path_to_project, "libs", "translation.py"))
            shutil.rmtree(os.path.join(path_to_project, "data"))

        Logger.info(f"KivyMD: Project '{path_to_project}' created")
        Logger.info(
            f"KivyMD: Create a virtual environment for '{path_to_project}' project..."
        )
        create_virtual_environment()
        Logger.info(
            f"KivyMD: Install requirements for '{path_to_project}' project..."
        )
        install_requirements()
        os.remove(os.path.join(path_to_project, "__init__.py"))
        if name_database == "no":
            os.remove(
                os.path.join(path_to_project, "Model", "database_firebase.py")
            )
            os.remove(
                os.path.join(path_to_project, "Model", "database_restdb.py")
            )
    else:
        parser.error(f"The {path_to_project} project already exists")


def create_main_with_hotreload() -> None:
    with open(
        os.path.join(path_to_project, "main.py"), encoding="utf-8"
    ) as main_file:
        main_code = ""
        for string in main_file.readlines():
            main_code += f"# {string}"
    with open(
        os.path.join(path_to_project, "main.py"), "w", encoding="utf-8"
    ) as main_file:
        main_file.write(f"{temp_hot_reload_main}\n{main_code}")

    with open(
        os.path.join(path_to_project, "main.py"), encoding="utf-8"
    ) as main_file:
        main_code = main_file.read()
        main_code = main_code.format(
            (
                "\nfrom kivy.properties import StringProperty\n"
                if use_localization == "yes"
                else ""
            ),
            (
                "\nfrom Model.database import DataBase"
                if name_database != "no"
                else ""
            ),
            (
                "\nfrom libs.translation import Translation\n"
                if use_localization == "yes"
                else ""
            ),
            project_name,
            (
                '\n    lang = StringProperty("en")\n'
                if use_localization == "yes"
                else ""
            ),
            (
                "\n        self.base = DataBase()\n"
                if name_database != "no"
                else ""
            ),
            (
                "\n        self.translation = Translation(\n"
                '            self.lang, "%s", os.path.join(self.directory, "data", "locales")'
                "\n        )" % project_name
                if use_localization == "yes"
                else ""
            ),
            "self.database" if name_database != "no" else "",
            (
                "\n\n    def on_lang(self, instance_app, lang_value: str) -> None:\n"
                "        self.translation.switch_lang(lang_value)\n"
                if use_localization == "yes"
                else ""
            ),
            (
                "\n    def switch_lang(self) -> None:\n"
                '        """Switch lang."""\n\n'
                '        self.lang = "ru" if self.lang == "en" else "en"'
                if use_localization == "yes"
                else ""
            ),
            project_name,
        )
        with open(
            os.path.join(path_to_project, "main.py"), "w", encoding="utf-8"
        ) as main_module:
            main_module.write(main_code)


def create_main() -> None:
    main_code = temp_main.format(
        (
            "\nfrom kivy.properties import StringProperty\n"
            if use_localization == "yes"
            else ""
        ),
        (
            "\nfrom libs.translation import Translation"
            if use_localization == "yes"
            else ""
        ),
        (
            "from Model.database import DataBase\n"
            if name_database != "no"
            else ""
        ),
        project_name,
        (
            '\n    lang = StringProperty("en")\n'
            if use_localization == "yes"
            else ""
        ),
        (
            "\n        self.translation = Translation(\n"
            '            self.lang, "%s", os.path.join(self.directory, "data", "locales")'
            "\n        )" % project_name
            if use_localization == "yes"
            else ""
        ),
        "self.database = DataBase()\n" if name_database != "no" else "",
        "self.database" if name_database != "no" else "",
        (
            "\n    def on_lang(self, instance_app, lang_value: str) -> None:\n"
            "        self.translation.switch_lang(lang_value)\n"
            if use_localization == "yes"
            else ""
        ),
        (
            "\n    def switch_lang(self) -> None:\n"
            '        """Switch lang."""\n\n'
            '        self.lang = "ru" if self.lang == "en" else "en"\n'
            if use_localization == "yes"
            else ""
        ),
        project_name,
    )
    with open(
        os.path.join(path_to_project, "main.py"), "w", encoding="utf-8"
    ) as main_module:
        main_module.write(main_code)


def create_model(
    name_screen: str, module_name: str, name_database: str, path_to_project: str
) -> None:
    if name_database != "no":
        code_model = temp_database_model.format(
            name_screen=name_screen,
            module_name=module_name,
            notify_name_screen=f'"{" ".join(module_name.split("_"))}"',
        )
    else:
        code_model = temp_without_database_model.format(
            module_name=module_name, name_screen=name_screen
        )

    model_module = os.path.join(path_to_project, "Model", module_name)
    with open(f"{model_module}.py", "w", encoding="utf-8") as module:
        module.write(code_model)


def create_basemodel() -> None:
    with open(
        os.path.join(path_to_project, "Model", "base_model.py"),
        "w",
        encoding="utf-8",
    ) as module_basemodel:
        module_basemodel.write(temp_basemodel)


def create_module_basescreen() -> None:
    with open(
        os.path.join(path_to_project, "View", "base_screen.py"),
        "w",
        encoding="utf-8",
    ) as base_screen:
        base_screen.write(temp_base_screen)


def create_controller(
    name_screen: str, module_name: str, use_hotreload: str, path_to_project: str
) -> None:
    name_view = (
        f"View.{name_screen}.{module_name}.{name_screen}View"
        if use_hotreload == "yes"
        else f"{name_screen}View"
    )
    code_controller = temp_code_controller.format(
        name_screen=name_screen,
        module_name=module_name,
        import_module=(
            ""
            f"import importlib\n\n"
            f"import View.{name_screen}.{module_name}\n\n"
            f"# We have to manually reload the view module in order to apply the\n"
            f"# changes made to the code on a subsequent hot reload.\n"
            f"# If you no longer need a hot reload, you can delete this instruction.\n"
            f"importlib.reload(View.{name_screen}.{module_name})\n\n"
            if use_hotreload == "yes"
            else f"\nfrom View.{name_screen}.{module_name} import {name_screen}View"
        ),
        name_view=name_view,
        get_view=(
            f"View.{name_screen}.{module_name}"
            if use_hotreload == "yes"
            else f"{name_screen}View"
        ),
    )

    path_to_controller = os.path.join(path_to_project, "Controller")
    if not os.path.exists(path_to_controller):
        os.mkdir(path_to_controller)
    controller_module = os.path.join(path_to_project, "Controller", module_name)
    with open(f"{controller_module}.py", "w", encoding="utf-8") as module:
        module.write(code_controller)


def create_makefile() -> None:
    makefile = temp_makefile.format(temp_makefile_files[:-2])
    with open(
        os.path.join(path_to_project, "Makefile"), "w", encoding="utf-8"
    ) as make_file:
        make_file.write(makefile)


def create_makefile_data(name_screen: str, module_name: str) -> None:
    global temp_makefile_files

    temp_makefile_files += (
        f"                View/{name_screen}/{module_name}.py \\\n"
    )
    temp_makefile_files += (
        f"                View/{name_screen}/{module_name}.kv \\\n"
    )


def create_screens_data(name_screen: str, module_name: str) -> None:
    global temp_screens_imports
    global temp_screens_data

    temp_screens_imports += (
        f"from Model.{module_name} import {name_screen}Model\n"
        f"from Controller.{module_name} import {name_screen}Controller\n"
    )
    temp_screens_data += (
        '\n    %s: {\n        "model": %s,'
        '\n        "controller": %s,\n    },\n'
        % (
            f'"{" ".join(module_name.split("_"))}"',
            f"{name_screen}Model",
            f"{name_screen}Controller",
        )
    )


def create_module_screens() -> None:
    path_to_module_screens = os.path.join(path_to_project, "View", "screens.py")
    with open(path_to_module_screens, "w", encoding="utf-8") as module_screens:
        module_screens.write(
            "%s\nscreens = {%s}" % (temp_screens_imports, temp_screens_data)
        )


def create_common_responsive_module(
    use_responsive: list, path_to_project: str
) -> None:
    for name_screen in use_responsive:
        path_to_init_common = os.path.join(
            path_to_project, "View", name_screen, "components", "common"
        )
        os.makedirs(path_to_init_common)
        with open(
            os.path.join(path_to_init_common, "__init__.py"),
            "w",
            encoding="utf-8",
        ) as init_common_components:
            init_common_components.write(
                "# This directory is for common responsive design components\n"
            )


def create_view(
    name_screen: str,
    module_name: str,
    use_responsive: list,
    path_to_project: str,
) -> None:
    path_to_view = os.path.join(path_to_project, "View", name_screen)
    path_to_components = os.path.join(path_to_view, "components")
    view_module = os.path.join(path_to_view, module_name)
    os.makedirs(path_to_view)
    os.makedirs(path_to_components)

    with open(
        os.path.join(path_to_view, "__init__.py"), "w", encoding="utf-8"
    ) as init_module:
        init_module.write("")
    with open(f"{view_module}.py", "w", encoding="utf-8") as view_file:
        view_file.write(
            temp_code_view.format(name_screen=name_screen)
            if name_screen not in use_responsive
            else temp_code_responsive_view.format(name_screen=name_screen)
        )

    if name_screen in use_responsive:
        for name_platform in ["DesktopScreen", "MobileScreen", "TabletScreen"]:
            path_to_init_components = os.path.join(
                path_to_project,
                "View",
                name_screen,
                "components",
                "__init__.py",
            )
            path_to_platforms = os.path.join(
                path_to_project, "View", name_screen, "components", "platforms"
            )
            path_to_platform = os.path.join(path_to_platforms, name_platform)
            path_to_platform_components = os.path.join(
                path_to_platform, "components"
            )
            os.makedirs(path_to_platform_components)
            shutil.copy(
                os.path.join(path_to_view, "__init__.py"),
                path_to_platform_components,
            )
            shutil.copy(
                os.path.join(path_to_view, "__init__.py"), path_to_platforms
            )

            name_platform_module = (
                f'{name_platform.split("Screen")[0].lower()}_screen'
            )
            with open(
                os.path.join(path_to_platform, f"{name_platform_module}.kv"),
                "w",
                encoding="utf-8",
            ) as platform_rule:
                platform_rule.write(f"<{name_platform}View>\n")
            with open(
                os.path.join(path_to_platform, f"{name_platform_module}.py"),
                "w",
                encoding="utf-8",
            ) as platform_baseclass:
                platform_baseclass.write(
                    temp_responsive_platform_baseclass.format(name_platform)
                )

        with open(
            path_to_init_components, "w", encoding="utf-8"
        ) as init_components:
            init_components.write(temp_responsive_component_imports)

    with open(f"{view_module}.kv", "w", encoding="utf-8") as view_file:
        view_file.write(f"<{name_screen}View>\n")

    if name_screen not in use_responsive:
        shutil.copy(
            os.path.join(path_to_view, "__init__.py"), path_to_components
        )


def create_package_utility() -> None:
    path_to_utility = os.path.join(path_to_project, "Utility")
    os.mkdir(path_to_utility)

    with open(
        os.path.join(path_to_utility, "__init__.py"), "w", encoding="utf-8"
    ) as init_module:
        init_module.write("")
    with open(
        os.path.join(path_to_utility, "observer.py"), "w", encoding="utf-8"
    ) as observer:
        observer.write(temp_utility)


def create_requirements() -> None:
    with open(
        os.path.join(path_to_project, "requirements.txt"), "w", encoding="utf-8"
    ) as requirements:
        requirements.write(
            firebase_requirements
            if name_database == "firebase"
            else without_firebase_requirements
        )


def create_virtual_environment() -> None:
    os.system(f"{python_version} -m pip install virtualenv")
    os.system(
        f"virtualenv -p {python_version} {os.path.join(path_to_project, 'venv')}"
    )


def install_requirements() -> None:
    python = os.path.join(path_to_project, "venv", "bin", "python3")
    if kivy_version == "master":
        if platform == "macosx":
            os.system(
                f"{python} -m pip install 'kivy[base] @ https://github.com/kivy/kivy/archive/master.zip'"
            )
        else:
            os.system(
                f"{python} -m pip install https://github.com/kivy/kivy/archive/master.zip"
            )
    elif kivy_version == "stable":
        os.system(f"{python} -m pip install kivy")
    else:
        os.system(f"{python} -m pip install kivy=={kivy_version}")
    os.system(
        f"{python} -m pip install https://github.com/kivymd/KivyMD/archive/master.zip"
    )
    os.system(f"{python} -m pip install watchdog")
    if name_database == "firebase":
        os.system(
            f"{python} -m pip install "
            f"multitasking "
            f"firebase "
            f"firebase-admin "
            f"python_jwt "
            f"gcloud "
            f"sseclient "
            f"pycryptodome==3.4.3 "
            f"requests_toolbelt "
            f"watchdog "
        )
    os.system(
        f"{os.path.join(path_to_project, 'venv', 'bin', 'python3')} -m pip list"
    )


def check_databases() -> None:
    databases = {"firebase": "restdb", "restdb": "firebase"}
    os.remove(
        os.path.join(
            path_to_project, "Model", f"database_{databases[name_database]}.py"
        )
    )
    os.rename(
        os.path.join(path_to_project, "Model", f"database_{name_database}.py"),
        os.path.join(path_to_project, "Model", "database.py"),
    )


def chek_camel_case_name_project(name_project) -> Union[bool, list]:
    result = re.findall("[A-Z][a-z]*", name_project)
    if len(result) == 1:
        return False
    return result


def create_argument_parser() -> ArgumentParserWithHelp:
    parser = ArgumentParserWithHelp(
        prog="create_project.py",
        allow_abbrev=False,
    )
    parser.add_argument(
        "pattern",
        help="the name of the pattern with which the project will be created.",
    )
    parser.add_argument(
        "directory",
        help="directory in which the project will be created.",
    )
    parser.add_argument(
        "name",
        help="project name.",
    )
    parser.add_argument(
        "python_version",
        help="the version of Python (specify as `python3.9` or `python3.8`) "
        "with which the virtual environment will be created.",
    )
    parser.add_argument(
        "kivy_version",
        help="version of Kivy (specify as `2.1.0` or `master`) that will be "
        "used in the project.",
    )
    parser.add_argument(
        "--name_screen",
        nargs="*",
        type=str,
        default=["MainScreen"],
        help="the name/names of the class which be used when creating the project pattern.",
    )
    parser.add_argument(
        "--use_responsive",
        nargs="*",
        type=str,
        default=[],
        help="the name/names of the views to be used by the responsive UI.",
    )
    parser.add_argument(
        "--name_database",
        default="no",
        help="name of the database provider ('firebase' or 'restdb').",
    )
    parser.add_argument(
        "--use_hotreload",
        default="no",
        help="creates a hot reload entry point to the application.",
    )
    parser.add_argument(
        "--use_localization",
        default="no",
        help="creates application localization files.",
    )
    return parser


if __name__ == "__main__":
    main()
