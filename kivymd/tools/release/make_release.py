# Copyright (c) 2019-2020 Artem Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

"""
Script to make release
======================

Run this script before release (before deploying).

What this script does:

* Undo all local changes in repository
* Update version in __init__.py, README
* Format files
* Rename file "unreleased.rst" to version, add to index.rst
* Commit "Version ..."
* Create tag
* Add "unreleased.rst" to Change Log, add to index.rst
* Commit
* Git push
"""

import os
import re
import subprocess
import sys

from kivymd.tools.release.argument_parser import ArgumentParserWithHelp
from kivymd.tools.release.git_commands import (
    command,
    get_previous_version,
    git_clean,
    git_commit,
    git_push,
    git_tag,
)
from kivymd.tools.release.update_icons import update_icons


def run_pre_commit():
    """Run pre-commit."""
    try:
        command(["pre-commit", "run", "--all-files"])
    except subprocess.CalledProcessError:
        pass
    git_commit("Run pre-commit", allow_error=True)


def replace_in_file(pattern, repl, file):
    """Replace one `pattern` match to `repl` in file `file`."""
    file_content = open(file, "rt", encoding="utf-8").read()
    new_file_content = re.sub(pattern, repl, file_content, 1, re.M)
    open(file, "wt", encoding="utf-8").write(new_file_content)
    return not file_content == new_file_content


def update_init_py(version, test: bool = False):
    """Change version in `kivymd/__init__.py`."""
    init_file = os.path.abspath("kivymd/__init__.py")
    init_version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    success = replace_in_file(init_version_regex, version, init_file)
    if test and not success:
        print("Couldn't update __init__.py file.", file=sys.stderr)


def update_readme(previous_version, version, test: bool = False):
    """Change version in README."""
    readme_file = os.path.abspath("README.md")
    readme_version_regex = rf"(?<=\[v){previous_version}[ \-*\w^\]\n]*(?=\])"
    success = replace_in_file(readme_version_regex, version, readme_file)
    if test and not success:
        print("Couldn't update README.md file.", file=sys.stderr)
    readme_install_version_regex = (
        rf"(?<=pip install kivymd==){previous_version}(?=\n```)"
    )
    success = replace_in_file(
        readme_install_version_regex, version, readme_file
    )
    if test and not success:
        print("Couldn't update README.md file.", file=sys.stderr)
    readme_buildozer_version_regex = (
        rf"(?<=, kivymd==){previous_version}(?=\n```)"
    )
    success = replace_in_file(
        readme_buildozer_version_regex, version, readme_file
    )
    if test and not success:
        print("Couldn't update README.md file.", file=sys.stderr)


def move_changelog(
    index_file,
    unreleased_file,
    previous_version,
    version_file,
    version,
    test: bool = False,
):
    """Edit unreleased.rst and rename to <version>.rst."""
    # Read unreleased changelog
    changelog = open(unreleased_file, "rt", encoding="utf-8").read()

    # Edit changelog
    changelog = re.sub(
        r"Unreleased\n----------",
        f"v{version}\n{'-' * (1 + len(version))}",
        changelog,
        1,
        re.M,
    )
    changelog = re.sub(
        r"(?<=See on GitHub: `)branch master",
        f"tag {version}",
        changelog,
        1,
        re.M,
    )
    changelog = re.sub(r"(?<=/tree/)master", f"{version}", changelog, 1, re.M)
    changelog = re.sub(
        rf"(?<=compare {previous_version}/)master",
        f"{version}",
        changelog,
        1,
        re.M,
    )
    changelog = re.sub(
        rf"(?<=compare/{previous_version}...)master",
        f"{version}",
        changelog,
        1,
        re.M,
    )
    changelog = re.sub(
        r"(?<=pip install )https[\S]*/master.zip(?=\n)",
        f"kivymd=={version}",
        changelog,
        1,
        re.M,
    )

    # Write changelog
    open(version_file, "wt", encoding="utf-8").write(changelog)
    # Remove unreleased changelog
    os.remove(unreleased_file)
    # Update index file
    success = replace_in_file(
        "/changelog/unreleased.rst", f"/changelog/{version}.rst", index_file
    )
    if test and not success:
        print("Couldn't update changelog file.", file=sys.stderr)


def create_unreleased_changelog(
    index_file,
    unreleased_file,
    previous_version,
    ask: bool = True,
    test: bool = False,
):
    """Create unreleased.rst by template."""
    # Check if unreleased file exists
    if os.path.exists(unreleased_file):
        if ask and input(
            f'Do you want to rewrite "{unreleased_file}"? (y)'
        ) not in ("", "y", "yes",):
            exit(0)
    # Generate unreleased changelog
    changelog = f"""Unreleased
----------

    See on GitHub: `branch master <https://github.com/kivymd/KivyMD/tree/master>`_ | `compare {previous_version}/master <https://github.com/kivymd/KivyMD/compare/{previous_version}...master>`_

    .. code-block:: bash

       pip install https://github.com/kivymd/KivyMD/archive/master.zip

* Bug fixes and other minor improvements.
"""
    # Create unreleased file
    open(unreleased_file, "wt", encoding="utf-8").write(changelog)
    # Update index file
    success = replace_in_file(
        r"(?<=Change Log\n==========\n\n)",
        ".. include:: /changelog/unreleased.rst\n",
        index_file,
    )
    if test and not success:
        print("Couldn't update changelog index file.", file=sys.stderr)


def main():
    parser = create_argument_parser()
    args = parser.parse_args()

    release = args.command == "release"
    version = args.version or "0.0.0"
    prepare = args.command == "prepare"
    test = args.command == "test"
    ask = args.yes is not True
    push = args.push is True

    if release and version == "0.0.0":
        parser.error("Please specify new version.")
    if not re.match(r"[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}", version):
        parser.error('Version "{version}" doesn\'t match template.')
    if test and push:
        parser.error("Don't use --push with test.")

    repository_root = os.path.normpath(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        )
    )

    # Change directory to repository root
    os.chdir(repository_root)

    previous_version = get_previous_version()

    # Print info
    print(f"Previous version: {previous_version}")
    print(f"New version: {version}")

    update_icons(make_commit=True)
    git_clean(ask=ask)
    run_pre_commit()

    if prepare:
        git_push([], ask=ask, push=push)
        return

    update_init_py(version, test=test)
    update_readme(previous_version, version, test=test)

    changelog_index_file = os.path.join(
        repository_root, "docs", "sources", "changelog", "index.rst"
    )
    changelog_unreleased_file = os.path.join(
        repository_root, "docs", "sources", "changelog", "unreleased.rst"
    )
    changelog_version_file = os.path.join(
        repository_root, "docs", "sources", "changelog", f"{version}.rst"
    )
    move_changelog(
        changelog_index_file,
        changelog_unreleased_file,
        previous_version,
        changelog_version_file,
        version,
        test=test,
    )

    git_commit(f"Version {version}")
    git_tag(version)

    branches_to_push = []
    # Move branch stable to stable-x.x.x
    # command(["git", "branch", "-m", "stable", f"stable-{old_version}"])
    # branches_to_push.append(f"stable-{old_version}")
    # Create branch stable
    # command(["git", "branch", "stable"])
    # command(["git", "push", "--force", "origin", "master:stable"])
    # branches_to_push.append("stable")

    create_unreleased_changelog(
        changelog_index_file,
        changelog_unreleased_file,
        previous_version,
        test=test,
    )
    git_commit("Add section Unreleased to Change Log")
    git_push(branches_to_push, ask=ask, push=push)


def create_argument_parser():
    parser = ArgumentParserWithHelp(
        prog="make_release.py",
        allow_abbrev=False,
        # usage="%(prog)s command [options] extensions [--exclude extensions]",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="remove and modify files without asking.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="push changes to remote repository. Use only with release and prepare.",
    )
    parser.add_argument(
        "command",
        choices=["release", "prepare", "test"],
        help="release will update icons, modify files and make tag.\n"
        "prepare will update icons and format files.\n"
        "test will check if script can modify each file correctly.",
    )
    parser.add_argument(
        "version",
        type=str,
        nargs="?",
        help="new version in format n.n.n (1.111.11).",
    )
    return parser


if __name__ == "__main__":
    main()
