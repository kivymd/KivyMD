# Copyright (c) 2019-2022 Artem Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

import subprocess


def command(cmd: list, capture_output: bool = False) -> str:
    """Run system command."""

    print(f"Command: {subprocess.list2cmdline(cmd)}")
    if capture_output:
        out = subprocess.check_output(cmd)
        out = out.decode("utf-8")
        print(out.strip())
        return out
    else:
        subprocess.check_call(cmd)
        return ""


def get_previous_version() -> str:
    """Returns latest tag in git."""

    command(["git", "checkout", "master"])
    old_version = command(
        ["git", "describe", "--abbrev=0", "--tags"], capture_output=True
    )
    old_version = old_version[:-1]  # Remove \n
    return old_version


def git_clean(ask: bool = True):
    """Clean git repository from untracked and changed files."""

    # Check what files will be removed
    files_to_clean = command(
        ["git", "clean", "-dx", "--force", "--dry-run"], capture_output=True
    ).strip()
    # Ask before removing
    if ask and files_to_clean:
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


def git_commit(message: str, allow_error: bool = False, add_files: list = None):
    """Make commit."""

    add_files = add_files if add_files else ["-A"]
    command(["git", "add", *add_files])
    try:
        command(["git", "commit", "--all", "-m", message])
    except subprocess.CalledProcessError as e:
        if not allow_error:
            raise e


def git_tag(name: str):
    """Create tag."""

    command(["git", "tag", name])


def git_push(branches_to_push: list, ask: bool = True, push: bool = False):
    """Push all changes."""

    if ask:
        push = input("Do you want to push changes? (y)") in (
            "",
            "y",
            "yes",
        )

    cmd = ["git", "push", "--tags", "origin", "master", *branches_to_push]
    if push:
        command(cmd)
    else:
        print(
            f"Changes are not pushed. Command for manual pushing: {subprocess.list2cmdline(cmd)}"
        )


if __name__ == "__main__":
    git_clean(ask=True)
