"""
Script creates a project with the MVC pattern
=============================================

.. versionadded:: 1.0.0

.. seealso::

    `MVC pattern <https://en.wikipedia.org/wiki/Model–view–controller>`_

.. rubric:: Use a clean architecture for your applications.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/preview-mvc.png
    :align: center

Project creation
----------------

.. code-block:: bash

    python -m kivymd.tools.patterns.create_project name_pattern path_to_project name_project

For example:
------------

.. code-block:: bash

    python -m kivymd.tools.patterns.create_project MVC /Users/macbookair/Projects MyProject

This command will by default create a project with an MVC pattern that uses
the Firebase library:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mvc-firebase.png
    :align: center

There is only one screen available in the project. The application will ask the
user for a login and password, check this data with the data in the database
and report the result:

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/mvc-firebase-preview.gif
    :align: center

To create a project without using the Firebase library, run the command:

.. code-block:: bash

    python -m kivymd.tools.patterns.create_project name_pattern path_to_project name_project --use_firebase no

.. note:: For more information on arguments, run the command:
    ``python -m kivymd.tools.patterns.create_project -h``
"""

import os
import re
import shutil
from typing import NoReturn, Union

from kivymd import path as kivymd_path
from kivymd.tools.argument_parser import ArgumentParserWithHelp

_firebase_model = '''
import multitasking


multitasking.set_max_threads(10)


class %s:
    """
    Implements the logic of the
    :class:`~View.%s.%s.%sView` class.
    """

    def __init__(self, base):
        self.base = base
        # Data:
        #  {
        #      'login': 'User Login',
        #      'password': '12345',
        #  }
        self.user_data = {}
        self._data_validation_status = None
        self._observers = []

    @property
    def data_validation_status(self):
        return self._data_validation_status

    @data_validation_status.setter
    def data_validation_status(self, value):
        self._data_validation_status = value
        # We notify the View -
        # :class:`~View.%s.%s.%s` about the
        # changes that have occurred in the data model.
        self.notify_observers()

    @multitasking.task
    def chek_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """

        data = self.base.get_data_from_base_users()
        data_validation_status = False

        for key in data:
            if data[key] == self.user_data:
                data_validation_status = True
                break
        self.data_validation_status = data_validation_status

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.user_data[key] = value

    def reset_data_validation_status(self):
        self.data_validation_status = None
'''

_without_firebase_model = '''
class %s:
    """
    Implements the logic of the
    :class:`~View.%s.%s.%s` class.
    """

    def __init__(self):
        self._observers = []
'''

_firebase_controller = '''from typing import NoReturn

from View.%s.%s import %s


class %s:
    """
    The `%s` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.%s.%s
        self.view = %s(controller=self, model=self.model)

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

        self.model.set_user_data(key, value)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

        self.view.show_dialog_wait()
        self.model.chek_data()

    def reset_data_validation_status(self, *args) -> NoReturn:
        self.model.reset_data_validation_status()
'''

_without_firebase_controller = '''from typing import NoReturn

from View.%s.%s import %s


class %s:
    """
    The `%s` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.%s.%s
        self.view = %s(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""
'''

_firebase_view_import = """
from typing import Union, NoReturn

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.theming import ThemableBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from Utility.observer import Observer
"""

_without_firebase_view_import = """
from typing import NoReturn

from kivy.properties import ObjectProperty

from kivymd.uix.screen import MDScreen

from Utility.observer import Observer
"""

_firebase_view_methods = '''
        self.dialog = MDDialog()
        self.dialog.bind(on_dismiss=self.controller.reset_data_validation_status)

    def show_dialog_wait(self) -> NoReturn:
        """Displays a wait dialog while the model is processing data."""

        self.dialog.auto_dismiss = False
        self.dialog.text = "Data validation..."
        self.dialog.open()

    def show_toast(self, interval: Union[int, float]) -> NoReturn:
        Snackbar(
            text="You have passed the verification successfully!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.8,
            bg_color=self.theme_cls.primary_color,
        ).open()
'''

_firebase_view_model_is_changed_method = """if self.model.data_validation_status:
            self.dialog.dismiss()
            Clock.schedule_once(self.show_toast, 1)
        if self.model.data_validation_status is False:
            self.dialog.text = "Wrong data!"
            self.dialog.auto_dismiss = True
"""

_firebase_requirements = """kivy==2.0.0
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

_without_firebase_requirements = """kivy==2.0.0
kivymd==1.0.0
"""

available_patterns = ["MVC"]


def main():
    parser = create_argument_parser()
    args = parser.parse_args()

    pattern_name = args.pattern
    project_directory = args.directory
    project_name = "".join(args.name.split(" "))
    name_screen = "".join(args.name_screen.split(" "))
    path_to_project = os.path.join(project_directory, project_name)
    use_firebase = args.use_firebase

    # Check arguments.
    if name_screen[-6:] != "Screen":
        parser.error(
            "Name of the screen must contain the word 'Screen' at the end. "
            "\nFor example - '... --name_screen MyFirstScreen'"
        )
    module_name = chek_camel_case_name_project(name_screen)
    if not module_name:
        parser.error(
            "The name of the screen should be written in camel case style. "
            "\nFor example - 'MyFirstScreen'"
        )
    module_name = "_".join([name.lower() for name in module_name])
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
        create_main(use_firebase, path_to_project, project_name)
        create_model(use_firebase, name_screen, module_name, path_to_project)
        create_controller(
            use_firebase, name_screen, module_name, path_to_project
        )
        create_view(use_firebase, name_screen, module_name, path_to_project)
        create_requirements(use_firebase, path_to_project)
        os.makedirs(os.path.join(path_to_project, "assets", "images"))
        os.mkdir(os.path.join(path_to_project, "assets", "fonts"))
        rename_ext_py_tmp_to_py(path_to_project)
        move_init(path_to_project, name_screen)
    else:
        parser.error(f"The {path_to_project} project already exists")


def create_main(
    use_firebase: str, path_to_project: str, project_name: str
) -> NoReturn:
    replace_in_file(
        os.path.join(path_to_project, "main.py_tmp"),
        (
            "from Model.base import Base\n" if use_firebase else "",
            project_name,
            "self.base = Base()\n" if use_firebase else "",
            "self.base" if use_firebase else "",
            project_name,
        ),
    )


def create_model(
    use_firebase: str, name_screen: str, module_name: str, path_to_project: str
) -> NoReturn:
    if use_firebase == "yes":
        firebase_model = _firebase_model % (
            f"{name_screen}Model",
            name_screen,
            module_name,
            name_screen,
            name_screen,
            module_name,
            f"{name_screen}View",
        )
        replace_in_file(
            os.path.join(path_to_project, "Model", "first_screen.py_tmp"),
            (firebase_model),
        )
    else:
        without_firebase_model = _without_firebase_model % (
            f"{name_screen}Model",
            module_name,
            name_screen,
            f"{name_screen}View",
        )
        replace_in_file(
            os.path.join(path_to_project, "Model", "first_screen.py_tmp"),
            (without_firebase_model),
        )
        os.remove(os.path.join(path_to_project, "Model", "base.py_tmp"))
    os.rename(
        os.path.join(path_to_project, "Model", "first_screen.py_tmp"),
        os.path.join(path_to_project, "Model", f"{module_name}.py_tmp"),
    )


def create_controller(
    use_firebase: str, name_screen: str, module_name: str, path_to_project: str
) -> NoReturn:
    if use_firebase == "yes":
        firebase_controller = _firebase_controller
    else:
        firebase_controller = _without_firebase_controller
    firebase_controller = firebase_controller % (
        name_screen,
        module_name,
        f"{name_screen}View",
        f"{name_screen}Controller",
        f"{name_screen}Controller",
        module_name,
        f"{name_screen}Model",
        f"{name_screen}View",
    )
    replace_in_file(
        os.path.join(path_to_project, "Controller", "first_screen.py_tmp"),
        (firebase_controller, f"{name_screen}View"),
    )
    os.rename(
        os.path.join(path_to_project, "Controller", "first_screen.py_tmp"),
        os.path.join(path_to_project, "Controller", f"{module_name}.py_tmp"),
    )


def create_view(
    use_firebase: str, name_screen: str, module_name: str, path_to_project: str
) -> NoReturn:
    replace_in_file(
        os.path.join(path_to_project, "View", "screens.py_tmp"),
        (
            module_name,
            f"{name_screen}Model",
            module_name,
            f"{name_screen}Controller",
            f'"{" ".join(module_name.split("_"))}"',
            f"{name_screen}Model",
            f"{name_screen}Controller",
        ),
    )
    replace_in_file(
        os.path.join(path_to_project, "View", "FirstScreen", "first_screen.kv"),
        (f"{name_screen}View", name_screen),
    )
    replace_in_file(
        os.path.join(
            path_to_project, "View", "FirstScreen", "first_screen.py_tmp"
        ),
        (
            _firebase_view_import
            if use_firebase == "yes"
            else _without_firebase_view_import,
            f"{name_screen}View",
            "ThemableBehavior, " if use_firebase == "yes" else "",
            module_name,
            f"{name_screen}Model",
            module_name,
            f"{name_screen}Controller",
            module_name,
            f"{name_screen}Model",
            _firebase_view_methods if use_firebase == "yes" else "",
            _firebase_view_model_is_changed_method
            if use_firebase == "yes"
            else "",
        ),
    )
    os.rename(
        os.path.join(path_to_project, "View", "FirstScreen", "first_screen.kv"),
        os.path.join(
            path_to_project, "View", "FirstScreen", f"{module_name}.kv"
        ),
    )
    os.rename(
        os.path.join(
            path_to_project, "View", "FirstScreen", "first_screen.py_tmp"
        ),
        os.path.join(
            path_to_project, "View", "FirstScreen", f"{module_name}.py_tmp"
        ),
    )
    os.rename(
        os.path.join(path_to_project, "View", "FirstScreen"),
        os.path.join(path_to_project, "View", name_screen),
    )


def create_requirements(use_firebase: str, path_to_project: str) -> NoReturn:
    with open(
        os.path.join(path_to_project, "requirements.txt"), "w", encoding="utf-8"
    ) as requirements:
        requirements.write(
            _firebase_requirements
            if use_firebase == "yes"
            else _without_firebase_requirements
        )


def rename_ext_py_tmp_to_py(path_to_project: str) -> NoReturn:
    for path_to_dir, dirs, files in os.walk(path_to_project):
        for name_file in files:
            if os.path.splitext(name_file)[1] == ".py_tmp":
                os.rename(
                    os.path.join(path_to_dir, name_file),
                    os.path.join(
                        path_to_dir, f"{os.path.splitext(name_file)[0]}.py"
                    ),
                )


def move_init(path_to_project: str, name_screen: str) -> NoReturn:
    path_to_init_file = __file__.replace("create_project", "__init__")
    for name_dir in ("Controller", "Model", "Utility", "View"):
        shutil.copy(
            path_to_init_file,
            os.path.join(path_to_project, name_dir, "__init__.py"),
        )
    shutil.copy(
        path_to_init_file,
        os.path.join(path_to_project, "View", name_screen, "__init__.py"),
    )
    path_to_components = os.path.join(
        path_to_project, "View", name_screen, "components"
    )
    os.mkdir(path_to_components)
    shutil.copy(
        path_to_init_file, os.path.join(path_to_components, "__init__.py")
    )


def chek_camel_case_name_project(name_project) -> Union[bool, list]:
    result = re.findall("[A-Z][a-z]*", name_project)
    if len(result) == 1:
        return False
    return result


def replace_in_file(path_to_file: str, args) -> NoReturn:
    with open(path_to_file, "rt", encoding="utf-8") as file_content:
        new_file_content = file_content.read() % (args)
        with open(path_to_file, "wt", encoding="utf-8") as original_file:
            original_file.write(new_file_content)


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
        "--name_screen",
        default="MainScreen",
        help="the name of the class wich be used when creating the project pattern.",
    )
    parser.add_argument(
        "--use_firebase",
        default="yes",
        help="use a basic template to work with the 'firebase' library.",
    )
    return parser


if __name__ == "__main__":
    main()
