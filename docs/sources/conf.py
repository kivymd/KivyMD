# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path setup
import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath("."))))

import kivymd


# Project information
project = "KivyMD"
copyright = "2019, Andrés Rodríguez, Ivanov Yuri, Artem S. Bulgakov and KivyMD contributors"
author = (
    "Andrés Rodríguez, Ivanov Yuri, Artem S. Bulgakov and KivyMD contributors"
)
version = kivymd.__version__
reelase = kivymd.__version__


# General configuration
master_doc = "index"
exclude_patterns = []
templates_path = ["_templates"]
locale_dirs = ["_locales"]
language = "Python"


# HTML Theme
html_theme = "alabaster"
html_static_path = ["_static"]
html_favicon = "_static/logo-kivymd.png"
html_theme_options = {
    "description": "Material Design widgets for Kivy",
    "logo": "logo-kivymd.png",
    "logo_name": True,
    "github_user": "HeaTTheatR",
    "github_repo": "KivyMD",
    "github_button": True,
    "github_type": "star",
    "github_count": "true",
    "travis_button": True,
}


# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinx.ext.intersphinx",
]

# AutoAPI configuration
autoapi_dirs = ["../../kivymd"]
autoapi_ignore = []
autoapi_type = "python"
autoapi_file_patterns = ["*.py"]
autoapi_generate_api_docs = True
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "special-members",
]
autoapi_root = "api"
autoapi_add_toctree_entry = True
autoapi_include_inheritance_graphs = False
autoapi_include_summaries = True
autoapi_python_class_content = "class"
autoapi_python_use_implicit_namespaces = False
autoapi_keep_files = True  # Debug

# InterSphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "kivy": ("https://kivy.org/docs/", None),
}
