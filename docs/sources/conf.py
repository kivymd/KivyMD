# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path setup.
import os
import sys
from pathlib import Path

# Don't allow Kivy to handle args
os.environ["KIVY_NO_ARGS"] = "true"
os.environ["READTHEDOCS"] = "true"

sys.path.insert(0, os.path.abspath("_extensions"))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath("."))))
try:
    kivymd_path = Path(__file__).parent.parent.parent / "kivymd"
    # this is a hack for now, will implement a better solution later
    # __version__ is defined in _version.py, imported by exec() below
    # this is just so linter doesn't complain
    __version__ = ""
    with open(kivymd_path / "_version.py", encoding="utf-8") as f:
        exec(f.read())
except FileNotFoundError:
    raise

import autoapi_kivymd  # NOQA. from _extensions

# Project information.
project = "KivyMD"
copyright = "2022, Andrés Rodríguez, Ivanov Yuri, Artem Bulgakov and KivyMD contributors"
author = "Andrés Rodríguez, Ivanov Yuri, Artem Bulgakov and KivyMD contributors"
version = __version__
release = __version__

# General configuration.
master_doc = "index"
exclude_patterns = []
templates_path = ["_templates"]
locale_dirs = ["_locales"]
language = "Python"

# HTML Theme.
html_theme = "furo"
html_static_path = ["_static"]
html_favicon = "_static/logo-kivymd.png"
html_logo = "_static/logo-kivymd.png"
html_theme_options = {
    "canonical_url": "https://kivymd.readthedocs.io/en/latest/",
    "navigation_depth": 2,
    "collapse_navigation": False,
    "titles_only": True,
}

# Pygments style.
pygments_style = "autumn"
pygments_dark_style = "monokai"

# Extensions.
extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "autoapi_kivymd",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "kivy_lexer",
    "toctree_with_sort",
]

# AutoAPI configuration.
autoapi_dirs = ["../../kivymd"]
autoapi_template_dir = os.path.abspath("_templates")
autoapi_ignore = ["**/kivymd/tests/**"]
autoapi_type = "python"
autoapi_file_patterns = ["*.py"]
autoapi_generate_api_docs = True
autoapi_options = ["members", "undoc-members"]
autoapi_root = "api"
autoapi_add_toctree_entry = False
autoapi_include_inheritance_graphs = False
show_module_summary = True
autoapi_python_class_content = "class"
autoapi_python_use_implicit_namespaces = False
autoapi_keep_files = False  # true for debugging

# InterSphinx configuration.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "kivy": ("https://kivy.org/doc/stable/", None),
}
