import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from time import time

from setuptools import find_packages, setup

assert sys.version_info >= (3, 7, 0), "KivyMD requires Python 3.7+"

try:
    # __version__ is defined in _version.py, imported by exec() below
    # this is just so linter doesn't complain
    __version__ = ""
    with open(
        Path(__file__).parent / "kivymd" / "_version.py", encoding="utf-8"
    ) as f:
        exec(f.read())
except FileNotFoundError:
    raise


def get_version() -> str:
    """Return version string."""

    # keeping this for compatibility with previous versions of KivyMD
    return __version__


def update_version_info():
    """Create _version.py file with git revision and date."""

    filename = os.path.join(os.path.dirname(__file__), "kivymd", "_version.py")
    epoch = int(os.environ.get("SOURCE_DATE_EPOCH", time()))
    date = datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d")
    try:
        git_revision = (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .strip()
            .decode("ascii")
        )
    except (
        subprocess.CalledProcessError,
        OSError,
        IOError,
        FileNotFoundError,
    ) as e:
        # CalledProcessError has no errno
        errno = getattr(e, "errno", None)
        if errno != 2 and "CalledProcessError" not in repr(e):
            raise
        git_revision = "Unknown"

    version_info = (
        "\n".join(
            [
                "release = False",
                f'__version__ = "{__version__}"',
                f'__hash__ = "{git_revision}"',
                f'__short_hash__ = "{git_revision[:7]}"',
                f'__date__ = "{date}"',
            ]
        )
        + "\n"
    )

    open(filename, "wt", encoding="utf-8").write(version_info)


def glob_paths(pattern):
    out_files = []
    src_path = os.path.join(os.path.dirname(__file__), "kivymd")

    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith(pattern):
                filepath = os.path.join(str(Path(*Path(root).parts[1:])), file)

                try:
                    out_files.append(filepath.split(f"kivymd{os.sep}")[1])
                except IndexError:
                    out_files.append(filepath)

    return out_files


if __name__ == "__main__":
    # Static strings are in setup.cfg
    update_version_info()
    setup(
        version=__version__,
        packages=find_packages(
            include=["kivymd", "kivymd.*"], exclude=["kivymd.tools.release"]
        ),
        package_dir={"kivymd": "kivymd"},
        package_data={
            "kivymd": [
                "images/*.png",
                "images/logo/*.png",
                "fonts/*.ttf",
                *glob_paths(".kv"),
                *glob_paths(".pot"),
                *glob_paths(".po"),
            ]
        },
        extras_require={
            "dev": [
                "pre-commit",
                "black",
                "isort[pyproject]",
                "flake8",
                "pytest",
                "pytest-cov",
                "pytest_asyncio",
                "pytest-timeout",
                "coveralls",
                "pyinstaller[hook_testing]",
            ],
            "docs": [
                "sphinx",
                "sphinx-autoapi",
                "furo",
                "sphinx-notfound-page",
                "sphinx-copybutton",
                "sphinx-tabs",
            ],
        },
        install_requires=[
            "kivy>=2.3.0",
            "pillow",
            "materialyoucolor>=2.0.7",
            "asynckivy>=0.6,<0.7",
        ],
        setup_requires=[],
        python_requires=">=3.7",
        entry_points={
            "pyinstaller40": [
                "hook-dirs = kivymd.tools.packaging.pyinstaller:get_hook_dirs",
                "tests = kivymd.tools.packaging.pyinstaller:get_pyinstaller_tests",
            ],
            "console_scripts": [
                "kivymd.add_view = kivymd.tools.patterns.add_view:main",
                "kivymd.create_project = kivymd.tools.patterns.create_project:main",
                "kivymd.make_release = kivymd.tools.release.make_release:main",
            ],
        },
    )
