# Copyright (c) 2019-2020 Artem Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

import subprocess


def command(cmd: list) -> bytes:
    """Run system command."""
    print("Command:", " ".join(cmd))
    return subprocess.check_output(cmd)


def get_previous_version() -> str:
    """Returns latest tag in git."""
    command(["git", "checkout", "master"])
    old_version = command(["git", "describe", "--abbrev=0", "--tags"])
    old_version = str(old_version, encoding="utf-8")[:-1]  # Remove \n
    return old_version


def git_clean(ask: bool = True):
    """Clean git repository from untracked and changed files."""
    # Check what files will be removed
    clean = str(
        command(["git", "clean", "-dx", "--force", "--dry-run"]),
        encoding="utf-8",
    )
    # Ask before removing
    if ask or not clean == "\n":
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


def git_push(branches_to_push: list, ask: bool = True):
    """Push all changes."""
    if not ask or input("Do you want to push changes? (y)") in (
        "",
        "y",
        "yes",
    ):
        command(
            ["git", "push", "--tags", "origin", "master", *branches_to_push]
        )
    else:
        print(
            "Changes are not pushed. Command for manual pushing:"
            " git push --tags origin master " + " ".join(branches_to_push)
        )
