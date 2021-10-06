"""
HotReload
=========

.. versionadded:: 1.0.0

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/hot-reload.png
    :align: center

.. rubric::
    Hot reload tool - is a fork of the project https://github.com/tito/kaki

.. note::
    Since the project is not developing, we decided to include it in the
    KivvMD library and hope that the further development of the hot reload
    tool in the KivyMD project will develop faster.

.. rubric::
    This library enhance Kivy frameworks with opiniated features such as:

- Auto reloading kv or py (watchdog required, limited to some uses cases);
- Idle detection support;
- Foreground lock (Windows OS only);

Usage
-----

.. note::
    See `create project with hot reload <https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/#create-project-with-hot-reload>`_
    for more information.

TODO
----

- Add automatic reloading of Python classes;
- Add save application state on reloading;

FIXME
-----

- On Windows, hot reloading of Python files may not work;
"""

import os
import sys
import traceback
from fnmatch import fnmatch
from os.path import join, realpath

original_argv = sys.argv

from kivy.base import ExceptionHandler, ExceptionManager  # NOQA E402
from kivy.clock import Clock, mainthread  # NOQA E402
from kivy.factory import Factory  # NOQA E402
from kivy.lang import Builder  # NOQA E402
from kivy.logger import Logger  # NOQA E402
from kivy.properties import (  # NOQA E402
    BooleanProperty,
    DictProperty,
    ListProperty,
    NumericProperty,
)

from kivymd.app import MDApp as BaseApp  # NOQA E402

try:
    from monotonic import monotonic
except ImportError:
    monotonic = None
try:
    from importlib import reload

    PY3 = True
except ImportError:
    PY3 = False

import watchdog  # NOQA


class ExceptionClass(ExceptionHandler):
    def handle_exception(self, inst):
        if isinstance(inst, (KeyboardInterrupt, SystemExit)):
            return ExceptionManager.RAISE
        app = MDApp.get_running_app()
        if not app.DEBUG and not app.RAISE_ERROR:
            return ExceptionManager.RAISE
        app.set_error(inst, tb=traceback.format_exc())
        return ExceptionManager.PASS


ExceptionManager.add_handler(ExceptionClass())


class MDApp(BaseApp):
    """HotReload Application class."""

    DEBUG = BooleanProperty("DEBUG" in os.environ)
    """
    Control either we activate debugging in the app or not.
    Defaults depend if 'DEBUG' exists in os.environ.

    :attr:`DEBUG` is a :class:`~kivy.properties.BooleanProperty`.
    """

    FOREGROUND_LOCK = BooleanProperty(False)
    """
    If `True` it will require the foreground lock on windows.

    :attr:`FOREGROUND_LOCK` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    KV_FILES = ListProperty()
    """
    List of KV files under management for auto reloader.

    :attr:`KV_FILES` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    KV_DIRS = ListProperty()
    """
    List of managed KV directories for autoloader.

    :attr:`KV_DIRS` is a :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    AUTORELOADER_PATHS = ListProperty([(".", {"recursive": True})])
    """
    List of path to watch for auto reloading.

    :attr:`AUTORELOADER_PATHS` is a :class:`~kivy.properties.ListProperty`
    and defaults to `([(".", {"recursive": True})]`.
    """

    AUTORELOADER_IGNORE_PATTERNS = ListProperty(["*.pyc", "*__pycache__*"])
    """
    List of extensions to ignore.

    :attr:`AUTORELOADER_IGNORE_PATTERNS` is a :class:`~kivy.properties.ListProperty`
    and defaults to `['*.pyc', '*__pycache__*']`.
    """

    CLASSES = DictProperty()
    """
    Factory classes managed by hotreload.

    :attr:`CLASSES` is a :class:`~kivy.properties.DictProperty`
    and defaults to `{}`.
    """

    IDLE_DETECTION = BooleanProperty(False)
    """
    Idle detection (if True, event on_idle/on_wakeup will be fired).
    Rearming idle can also be done with `rearm_idle()`.

    :attr:`IDLE_DETECTION` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    IDLE_TIMEOUT = NumericProperty(60)
    """
    Default idle timeout.

    :attr:`IDLE_TIMEOUT` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `60`.
    """

    RAISE_ERROR = BooleanProperty(True)
    """
    Raise error.
    When the `DEBUG` is activated, it will raise any error instead
    of showing it on the screen. If you still want to show the error
    when not in `DEBUG`, put this to `False`.

    :attr:`RAISE_ERROR` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`.
    """

    __events__ = ["on_idle", "on_wakeup"]

    def build(self):
        if self.DEBUG:
            Logger.info("{}: Debug mode activated".format(self.appname))
            self.enable_autoreload()
            self.patch_builder()
            self.bind_key(32, self.rebuild)
        if self.FOREGROUND_LOCK:
            self.prepare_foreground_lock()

        self.state = None
        self.approot = None
        self.root = self.get_root()
        self.rebuild(first=True)

        if self.IDLE_DETECTION:
            self.install_idle(timeout=self.IDLE_TIMEOUT)

        return super().build()

    def get_root(self):
        """
        Return a root widget, that will contains your application.
        It should not be your application widget itself, as it may
        be destroyed and recreated from scratch when reloading.

        By default, it returns a RelativeLayout, but it could be
        a Viewport.
        """

        return Factory.RelativeLayout()

    def get_root_path(self):
        """Return the root file path."""

        return realpath(os.getcwd())

    def build_app(self, first=False):
        """
        Must return your application widget.

        If `first` is set, it means that will be your first time ever
        that the application is built. Act according to it.
        """

        raise NotImplemented()

    def unload_app_dependencies(self):
        """
        Called when all the application dependencies must be unloaded.
        Usually happen before a reload
        """

        for path_to_kv_file in self.KV_FILES:
            path_to_kv_file = realpath(path_to_kv_file)
            Builder.unload_file(path_to_kv_file)

        for name, module in self.CLASSES.items():
            Factory.unregister(name)

        for path in self.KV_DIRS:
            for path_to_dir, dirs, files in os.walk(path):
                for name_file in files:
                    if os.path.splitext(name_file)[1] == ".kv":
                        path_to_kv_file = os.path.join(path_to_dir, name_file)
                        Builder.unload_file(path_to_kv_file)

    def load_app_dependencies(self):
        """
        Load all the application dependencies.
        This is called before rebuild.
        """

        for path_to_kv_file in self.KV_FILES:
            path_to_kv_file = realpath(path_to_kv_file)
            Builder.load_file(path_to_kv_file)

        for name, module in self.CLASSES.items():
            Factory.register(name, module=module)

        for path in self.KV_DIRS:
            for path_to_dir, dirs, files in os.walk(path):
                for name_file in files:
                    if os.path.splitext(name_file)[1] == ".kv":
                        path_to_kv_file = os.path.join(path_to_dir, name_file)
                        Builder.load_file(path_to_kv_file)

    def rebuild(self, *args, **kwargs):
        print("{}: Rebuild the application".format(self.appname))
        first = kwargs.get("first", False)
        try:
            if not first:
                self.unload_app_dependencies()

            # In case the loading fail in the middle of building a widget
            # there will be existing rules context that will break later
            # instanciation.
            # Just clean it.
            Builder.rulectx = {}

            self.load_app_dependencies()
            self.set_widget(None)
            self.approot = self.build_app()
            self.set_widget(self.approot)
            self.apply_state(self.state)
        except Exception as exc:
            import traceback

            Logger.exception("{}: Error when building app".format(self.appname))
            self.set_error(repr(exc), traceback.format_exc())
            if not self.DEBUG and self.RAISE_ERROR:
                raise

    @mainthread
    def set_error(self, exc, tb=None):
        print(tb)
        from kivy.core.window import Window
        from kivy.utils import get_color_from_hex

        Window.clearcolor = get_color_from_hex("#e50000")
        scroll = Factory.ScrollView(scroll_y=0)
        lbl = Factory.Label(
            text_size=(Window.width - 100, None),
            size_hint_y=None,
            text="{}\n\n{}".format(exc, tb or ""),
        )
        lbl.bind(texture_size=lbl.setter("size"))
        scroll.add_widget(lbl)
        self.set_widget(scroll)

    def bind_key(self, key, callback):
        """Bind a key (keycode) to a callback (cannot be unbind)."""

        from kivy.core.window import Window

        def _on_keyboard(window, keycode, *args):
            if key == keycode:
                return callback()

        Window.bind(on_keyboard=_on_keyboard)

    @property
    def appname(self):
        """Return the name of the application class."""

        return self.__class__.__name__

    def enable_autoreload(self):
        """
        Enable autoreload manually. It is activated automatically
        if "DEBUG" exists in environ. It requires the `watchdog` module.
        """

        try:
            from watchdog.events import FileSystemEventHandler
            from watchdog.observers import Observer
        except ImportError:
            Logger.warn(
                "{}: Autoreloader is missing watchdog".format(self.appname)
            )
            return
        Logger.info("{}: Autoreloader activated".format(self.appname))
        rootpath = self.get_root_path()
        self.w_handler = handler = FileSystemEventHandler()
        handler.dispatch = self._reload_from_watchdog
        self._observer = observer = Observer()
        for path in self.AUTORELOADER_PATHS:
            options = {"recursive": True}
            if isinstance(path, (tuple, list)):
                path, options = path
            observer.schedule(handler, join(rootpath, path), **options)
        observer.start()

    def prepare_foreground_lock(self):
        """
        Try forcing app to front permanently to avoid windows
        pop ups and notifications etc.app.

        Requires fake full screen and borderless.

        .. note::
            This function is called automatically if `FOREGROUND_LOCK` is set
        """

        try:
            import ctypes

            LSFW_LOCK = 1
            ctypes.windll.user32.LockSetForegroundWindow(LSFW_LOCK)
            Logger.info("App: Foreground lock activated")
        except Exception:
            Logger.warn("App: No foreground lock available")

    def set_widget(self, wid):
        """
        Clear the root container, and set the new approot widget to `wid`.
        """

        self.root.clear_widgets()
        self.approot = wid
        if wid is None:
            return
        self.root.add_widget(self.approot)
        try:
            wid.do_layout()
        except Exception:
            pass

    # State management.
    def apply_state(self, state):
        """Whatever the current state is, reapply the current state."""

    # Idle management leave.
    def install_idle(self, timeout=60):
        """
        Install the idle detector. Default timeout is 60s.
        Once installed, it will check every second if the idle timer
        expired. The timer can be rearm using :func:`rearm_idle`.
        """

        if monotonic is None:
            Logger.exception(
                "{}: Cannot use idle detector, monotonic is missing".format(
                    self.appname
                )
            )
        self.idle_timer = None
        self.idle_timeout = timeout
        Logger.info(
            "{}: Install idle detector, {} seconds".format(
                self.appname, timeout
            )
        )
        Clock.schedule_interval(self._check_idle, 1)
        self.root.bind(
            on_touch_down=self.rearm_idle, on_touch_up=self.rearm_idle
        )

    def rearm_idle(self, *args):
        """Rearm the idle timer."""

        if not hasattr(self, "idle_timer"):
            return
        if self.idle_timer is None:
            self.dispatch("on_wakeup")
        self.idle_timer = monotonic()

    # Internals.
    def patch_builder(self):
        Builder.orig_load_string = Builder.load_string
        Builder.load_string = self._builder_load_string

    def on_idle(self, *args):
        """Event fired when the application enter the idle mode."""

    def on_wakeup(self, *args):
        """Event fired when the application leaves idle mode."""

    @mainthread
    def _reload_from_watchdog(self, event):
        from watchdog.events import FileModifiedEvent

        if not isinstance(event, FileModifiedEvent):
            return

        for pat in self.AUTORELOADER_IGNORE_PATTERNS:
            if fnmatch(event.src_path, pat):
                return

        if event.src_path.endswith(".py"):
            # source changed, reload it
            try:
                Builder.unload_file(event.src_path)
                self._reload_py(event.src_path)
            except Exception as e:
                import traceback

                self.set_error(repr(e), traceback.format_exc())
                return

        Clock.unschedule(self.rebuild)
        Clock.schedule_once(self.rebuild, 0.1)

    def _builder_load_string(self, string, **kwargs):
        if "filename" not in kwargs:
            from inspect import getframeinfo, stack

            caller = getframeinfo(stack()[1][0])
            kwargs["filename"] = caller.filename
        return Builder.orig_load_string(string, **kwargs)

    def _check_idle(self, *args):
        if not hasattr(self, "idle_timer"):
            return
        if self.idle_timer is None:
            return
        if monotonic() - self.idle_timer > self.idle_timeout:
            self.idle_timer = None
            self.dispatch("on_idle")

    def _reload_py(self, filename):
        # We don't have dependency graph yet, so if the module actually exists
        # reload it.

        filename = realpath(filename)
        # Check if it's our own application file.
        try:
            mod = sys.modules[self.__class__.__module__]
            mod_filename = realpath(mod.__file__)
        except Exception as e:
            mod_filename = None

        # Detect if it's the application class // main.
        if mod_filename == filename:
            return self._restart_app(mod)

        module = self._filename_to_module(filename)
        if module in sys.modules:
            Logger.debug("{}: Module exist, reload it".format(self.appname))
            Factory.unregister_from_filename(filename)
            self._unregister_factory_from_module(module)
            reload(sys.modules[module])

    def _unregister_factory_from_module(self, module):
        # Check module directly.
        to_remove = [
            x for x in Factory.classes if Factory.classes[x]["module"] == module
        ]
        # Check class name.
        for x in Factory.classes:
            cls = Factory.classes[x]["cls"]
            if not cls:
                continue
            if getattr(cls, "__module__", None) == module:
                to_remove.append(x)

        for name in set(to_remove):
            del Factory.classes[name]

    def _filename_to_module(self, filename):
        orig_filename = filename
        rootpath = self.get_root_path()
        if filename.startswith(rootpath):
            filename = filename[len(rootpath) :]
        if filename.startswith("/"):
            filename = filename[1:]
        module = filename[:-3].replace("/", ".")
        Logger.debug(
            "{}: Translated {} to {}".format(
                self.appname, orig_filename, module
            )
        )
        return module

    def _restart_app(self, mod):
        _has_execv = sys.platform != "win32"
        cmd = [sys.executable] + original_argv
        if not _has_execv:
            import subprocess

            subprocess.Popen(cmd)
            sys.exit(0)
        else:
            try:
                os.execv(sys.executable, cmd)
            except OSError:
                os.spawnv(os.P_NOWAIT, sys.executable, cmd)
                os._exit(0)
