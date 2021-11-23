import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from time import time

from setuptools import find_packages, setup

assert sys.version_info >= (3, 6, 0), "KivyMD requires Python 3.6+"


def get_version() -> str:
    """Get __version__ from __init__.py file."""

    version_file = os.path.join(
        os.path.dirname(__file__), "kivymd", "__init__.py"
    )
    version_file_data = open(version_file, "rt", encoding="utf-8").read()
    version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    try:
        version = re.findall(version_regex, version_file_data, re.M)[0]
        return version
    except IndexError:
        raise ValueError(f"Unable to find version string in {version_file}.")


def write_version_info():
    """Create _version.py file with git revision and date."""

    filename = os.path.join(os.path.dirname(__file__), "kivymd", "_version.py")
    version = get_version()
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
        f"# THIS FILE IS GENERATED FROM KIVYMD SETUP.PY\n"
        f"__version__ = '{version}'\n"
        f"__hash__ = '{git_revision}'\n"
        f"__short_hash__ = '{git_revision[:7]}'\n"
        f"__date__ = '{date}'\n"
    )

    open(filename, "wt", encoding="utf-8").write(version_info)


def glob_paths(pattern):
    out_files = []

    src_path = os.path.join(os.path.dirname(__file__), "kivymd")

    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith(pattern):
                filepath = os.path.join(str(Path(*Path(root).parts[1:])), file)
                out_files.append(filepath)

    return out_files


if __name__ == "__main__":
    # Static strings are in setup.cfg
    write_version_info()
    setup(
        version=get_version(),
        packages=find_packages(
            include=["kivymd", "kivymd.*"], exclude=["kivymd.tools.release"]
        ),
        package_dir={"kivymd": "kivymd"},
        package_data={
            "kivymd": [
                "images/*.png",
                "images/*.atlas",
                "fonts/*.ttf",
                *glob_paths(".kv"),
                *glob_paths(".py_tmp"),
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
                "sphinx-autoapi==1.4.0",
                "sphinx_rtd_theme",
                "sphinx-notfound-page",
            ],
        },
        install_requires=["kivy>=2.0.0", "pillow"],
        setup_requires=[],
        python_requires=">=3.6",
        entry_points={
            "pyinstaller40": [
                "hook-dirs = kivymd.tools.packaging.pyinstaller:get_hook_dirs",
                "tests = kivymd.tools.packaging.pyinstaller:get_pyinstaller_tests",
            ]
        },
    )
