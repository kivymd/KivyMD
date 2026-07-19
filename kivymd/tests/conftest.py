"""
Custom pytest collector for running KivyMD application tests.

This module provides a custom pytest collection mechanism that allows
KivyMD tests written as standalone Python scripts to be executed through
pytest. Each test file is collected as a single pytest item and executed
with `runpy.run_path()` using the `__main__` context.
"""

import runpy

import pytest


class KivyMDTestFile(pytest.File):
    """
    Custom pytest file collector for KivyMD standalone test scripts.

    Collects Python test files and creates a single test item that executes
    the file as a standalone application.
    """

    def collect(self):
        """
        Collect a KivyMD test file as a pytest item.

        Yields:
            KivyMDTestItem: Test item responsible for running the script.
        """

        yield KivyMDTestItem.from_parent(
            self,
            name=self.path.name,
        )


class KivyMDTestItem(pytest.Item):
    """
    Pytest item that executes a KivyMD test script.

    The item runs the collected file using `runpy.run_path()` so that
    KivyMD application tests can use the standard
    `if __name__ == "__main__":` entry point.
    """

    def runtest(self):
        """
        Execute the KivyMD test script.

        Runs the test file with `__main__` as the execution context,
        allowing Kivy applications to initialize and run normally.
        """

        runpy.run_path(
            str(self.path),
            run_name="__main__",
        )


def pytest_collect_file(parent, file_path):
    """
    Register custom collection for KivyMD Python test files.

    Args:
        parent: Parent pytest collector.
        file_path: Path to the file being collected.

    Returns:
        KivyMDTestFile | None:
            Custom collector for matching test files, otherwise ``None``.

    Notes:
        Only Python files whose names start with ``test_`` are collected.
    """

    if file_path.name.startswith("test_") and file_path.suffix == ".py":
        return KivyMDTestFile.from_parent(
            parent,
            path=file_path,
        )
