import re
import sys
from os.path import dirname, join

from setuptools import setup

assert sys.version_info >= (3, 6, 0), "KivyMD requires Python 3.6+"


def get_version() -> str:
    version_file = join(dirname(__file__), "kivymd/__init__.py")
    version_file_data = open(version_file, "rt", encoding="utf-8").read()
    version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    try:
        version = re.findall(version_regex, version_file_data, re.M)[0]
        return version
    except IndexError:
        raise ValueError(f"Unable to find version string in {version_file}.")


if __name__ == "__main__":
    # Static strings are in setup.cfg
    setup(
        version=get_version(),
        packages=["kivymd"],
        package_dir={"kivymd": "kivymd"},
        package_data={
            "kivymd": [
                "uix/*.py",
                "uix/behaviors/*.py",
                "utils/*.py",
                "tools/*.py",
                "tools/packaging/*.py",
                "tools/packaging/pyinstaller/*.py",
                "toast/*.py",
                "toast/kivytoast/*.py",
                "toast/androidtoast/*.py",
                "stiffscroll/*.py",
                "vendor/*.py",
                "vendor/circleLayout/*.py",
                "vendor/circularTimePicker/*.py",
                "vendor/navigationdrawer/*.py",
                "images/*.png",
                "images/*.jpg",
                "images/*.atlas",
                "fonts/*.ttf",
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
            ],
            "docs": ["sphinx", "sphinx-autoapi", "sphinx_rtd_theme"],
        },
        install_requires=["kivy", "requests"],
        setup_requires=[],
        python_requires=">=3.6",
    )
