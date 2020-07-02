# Copyright (c) 2019 Artem S. Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

"""
Script Before release
=====================

Run this script before release (before deploying).

What this script does:

* Undo all local changes in repository
* Update version in __init__.py, README
* Black files
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


def command(cmd: list):
    print("Command:", " ".join(cmd))
    return subprocess.check_output(cmd)


def get_previous_version():
    """Returns latest tag in git."""
    command(["git", "checkout", "master"])
    old_version = command(["git", "describe", "--abbrev=0", "--tags"])
    old_version = str(old_version, encoding="utf-8")[:-1]  # Remove \n
    return old_version


def git_clean():
    """Clean git repository from untracked and changed files."""
    # Check what files will be removed
    clean = str(
        command(["git", "clean", "-dx", "--force", "--dry-run"]),
        encoding="utf-8",
    )
    # Ask before removing
    if not clean == "\n":
        print(clean)
        while True:
            ans = input("Do you want to remove these files? (yes/no)").lower()
            if ans == "y" or ans == "yes":
                break
            elif ans == "n" or ans == "no":
                print("git clean is required. Exit")
                exit(0)

    # Remove all untracked files
    command(["git", "clean", "-dx", "--force"])
    command(["git", "reset", "--hard"])


def git_commit(message: str, allow_error: bool = False):
    """Make commit."""
    command(["git", "add", "-A"])
    try:
        command(["git", "commit", "--all", "-m", message])
    except subprocess.CalledProcessError as e:
        if not allow_error:
            raise e


def git_tag(name: str):
    """Create tag."""
    command(["git", "tag", name])


def git_push(branches_to_push: list):
    """Push all changes."""
    if input("Do you want to push changes? (y)") in ("", "y", "yes"):
        command(
            ["git", "push", "--tags", "origin", "master", *branches_to_push]
        )
    else:
        print(
            "Changes are not pushed. Command for manual pushing:"
            " git push --tags origin master " + " ".join(branches_to_push)
        )


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
    file_content = re.sub(pattern, repl, file_content, 1, re.M)
    open(file, "wt", encoding="utf-8").write(file_content)


def update_init_py(version):
    """Change version in `kivymd/__init__.py`."""
    init_file = os.path.abspath("kivymd/__init__.py")
    init_version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    replace_in_file(init_version_regex, version, init_file)


def update_readme(previous_version, version):
    """Change version in README."""
    readme_file = os.path.abspath("README.md")
    readme_version_regex = rf"(?<=\[)v{previous_version}[ \-*\w^\]\n]*(?=\])"
    replace_in_file(readme_version_regex, version, readme_file)


def move_changelog(
    index_file, unreleased_file, previous_version, version_file, version
):
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
        r"(?<=pip install )git\+https[\S]*@master(?=\n)",
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
    replace_in_file(
        "/changelog/unreleased.rst", f"/changelog/{version}.rst", index_file
    )


def create_unreleased_changelog(index_file, unreleased_file, previous_version):
    # Check if unreleased file exists
    if os.path.exists(unreleased_file):
        if input(f'Do you want to rewrite "{unreleased_file}"? (y)') not in (
            "",
            "y",
            "yes",
        ):
            exit(0)
    # Generate unreleased changelog
    changelog = f"""Unreleased
----------

    See on GitHub: `branch master <https://github.com/HeaTTheatR/KivyMD/tree/master>`_ | `compare {previous_version}/master <https://github.com/HeaTTheatR/KivyMD/compare/{previous_version}...master>`_

    .. code-block:: bash

       pip install git+https://github.com/HeaTTheatR/KivyMD.git@master

* Bug fixes and other minor improvements.
"""
    # Create unreleased file
    open(unreleased_file, "wt", encoding="utf-8").write(changelog)
    # Update index file
    replace_in_file(
        r"(?<=Change Log\n==========\n\n)",
        ".. include:: /changelog/unreleased.rst\n",
        index_file,
    )


def main():
    # Change directory to repository root
    os.chdir(os.path.join(os.path.dirname(__file__), "../../.."))

    # Get version
    if len(sys.argv) > 3:
        print("Usage:\npython make_release.py version")
        return
    elif len(sys.argv) == 2:
        version = sys.argv[1]
    else:
        version = input("Type version: ")

    if not re.match(r"[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}", version):
        print(f'Version "{version}" doesn\'t match template.')
        return

    previous_version = get_previous_version()

    # Print info
    print(f"Previous version: {previous_version}")
    print(f"New version: {version}")

    git_clean()
    run_pre_commit()
    update_init_py(version)
    update_readme(previous_version, version)

    changelog_index_file = os.path.abspath(
        f"docs{os.sep}sources{os.sep}" f"changelog{os.sep}index.rst"
    )
    changelog_unreleased_file = os.path.abspath(
        f"docs{os.sep}sources{os.sep}" f"changelog{os.sep}unreleased.rst"
    )
    changelog_version_file = os.path.abspath(
        f"docs{os.sep}sources{os.sep}" f"changelog{os.sep}{version}.rst"
    )
    move_changelog(
        changelog_index_file,
        changelog_unreleased_file,
        previous_version,
        changelog_version_file,
        version,
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
        changelog_index_file, changelog_unreleased_file, previous_version
    )
    git_commit("Add section Unreleased to Change Log")
    git_push(branches_to_push)


if __name__ == "__main__":
    main()
