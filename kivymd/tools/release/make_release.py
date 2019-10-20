# Copyright (c) 2019 Artem S. Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

"""
Script Before release
=====================

Run this script before release (before deploying).

* Undo all local changes in repository
* Update version in __init__.py, README
* Rename "Unreleased" to version in CHANGELOG.md
* Commit "Version ..."
* Tag
* Add "Unreleased" to CHANGELOG.md
* Force push repository
"""

import sys
import os
import subprocess
import re

if not len(sys.argv) in (3, 5):
    print(
        "Usage:\n"
        "python before_release.py new_version new_version_status"
        " next_version next_version_status\n"
        "Example: python3 before_release.py 1.9.3 alpha 1.9.4 alpha\n"
        "Example: python3 before_release.py 1.9.3 1.9.4"
    )
    exit(0)


def command(cmd):
    print("Command:", " ".join(cmd))
    return subprocess.check_output(cmd)


os.chdir(os.path.join(os.path.dirname(__file__), "../../.."))

# Get new version
new_version = sys.argv[1]
new_version_status = sys.argv[2] if len(sys.argv) == 5 else None
postfix_new_version = (
    f" - *{new_version_status.capitalize()}*"
    if new_version_status is not None
    else ""
)
full_new_version = f"v{new_version}{postfix_new_version}"

# Get next version
next_version = sys.argv[3]
next_version_status = sys.argv[4] if len(sys.argv) == 5 else None
postfix_next_version = (
    f" - *{next_version_status.capitalize()}*"
    if next_version_status is not None
    else ""
)
full_next_version = f"v{next_version}{postfix_next_version}"

# Get old version
command(["git", "checkout", "master"])
old_version = command(["git", "describe", "--abbrev=0", "--tags"])
old_version = str(old_version, encoding="utf-8")[:-1]  # Remove \n

# Print info
print(f"Old version: {old_version}")
print(f"New version: {new_version} ({full_new_version})")
print(f"Next version: {next_version} ({full_next_version})\n")

# Check what files will be removed
clean = str(
    command(["git", "clean", "-dx", "--force", "--dry-run"]), encoding="utf-8"
)
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

# Black all files
# command(["black", "."])
# command(["git", "commit", "--all", "-m", f"Black formatting"])


def replace_in_file(pattern, repl, file):
    # Replace one `pattern` match to `repl` in file `file`
    file_content = open(file, "rt", encoding="utf-8").read()
    file_content = re.sub(pattern, repl, file_content, 1, re.M)
    open(file, "wt", encoding="utf-8").write(file_content)


# Change version in kivymd/__init__.py
init = os.path.abspath("kivymd/__init__.py")
init_version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
init_version_info_regex = r"(?<=^__version_info__ = \()[^\)]+(?=\)$)"
replace_in_file(init_version_regex, new_version, init)
replace_in_file(init_version_info_regex, new_version.replace(".", ", "), init)

# Change version in README.md
readme = os.path.abspath("README.md")
readme_version_regex = rf"(?<=\[)v{old_version}[ \-*\w^\]\n]*(?=\])"
replace_in_file(readme_version_regex, full_new_version, readme)

# Change version in CHANGELOG.md
changelog = os.path.abspath("CHANGELOG.md")
changelog_new_version_regex = r"(?<=\> )[^\n]*(?=\n\n)"
changelog_new_version_line_regex = r"\> [^\n]*\n\n"
changelog_unreleased_regex = r"(?<=## )[^\n]*(?=\n\n)"
changelog_see_changes_regex = rf"{old_version}\.\.\.master"
changelog_see_changes_string = f"{old_version}...{new_version}"
changelog_install_regex = r"git\+https[\S]*@master(?=\n)"
changelog_install_string = f"kivymd=={new_version}"

try:
    # Rename Unreleased section with new version
    changelog_file_content = open(changelog, "rt", encoding="utf-8").read()
    new_version_in_changelog = re.findall(
        changelog_new_version_regex, changelog_file_content, re.M
    )[0]
    changelog_file_content = re.sub(
        changelog_new_version_line_regex, "", changelog_file_content, 1, re.M
    )
    changelog_file_content = re.sub(
        changelog_see_changes_regex,
        changelog_see_changes_string,
        changelog_file_content,
        1,
        re.M,
    )
    changelog_file_content = re.sub(
        changelog_install_regex,
        changelog_install_string,
        changelog_file_content,
        1,
        re.M,
    )
    changelog_file_content = re.sub(
        changelog_unreleased_regex,
        new_version_in_changelog,
        changelog_file_content,
        1,
        re.M,
    )
    open(changelog, "wt", encoding="utf-8").write(changelog_file_content)
except IndexError:
    pass

# Black all files
command(["black", "."])

# Make commit and tag
command(["git", "commit", "--all", "-m", f"Version {new_version}"])
command(["git", "tag", new_version])

# Create branch `stable` and `stable-{old_version}` (not tested)
branches_to_push = []
# command(["git", "branch", "-m", "stable", f"stable-{old_version}"])
# branches_to_push.append(f"stable-{old_version}")
# command(["git", "branch", "stable"])
# command(["git", "push", "--force", "origin", "master:stable"])
# branches_to_push.append("stable")

# Regex where to place Unreleased section
changelog_unreleased_place_regex = f"(?<=Change Log\n==========\n\n)"
# Unreleased section to place in top of CHANGELOG.md
changelog_unreleased_string = f"""\
## [Unreleased](https://github.com/HeaTTheatR/KivyMD/tree/master)

> [v{next_version}](https://github.com/HeaTTheatR/KivyMD/tree/{next_version})\
{postfix_next_version}

* 
* 
* 

[See changes](https://github.com/HeaTTheatR/KivyMD/compare/{new_version}...master)
```bash
pip install git+https://github.com/HeaTTheatR/KivyMD.git@master
```


"""
replace_in_file(
    changelog_unreleased_place_regex, changelog_unreleased_string, changelog
)
command(
    ["git", "commit", "--all", "-m", f"Add section Unreleased to Change Log"]
)

# Push all changes
if input("Do you want to push changes? (y)") in ("", "y", "yes"):
    command(["git", "push", "--tags", "origin", "master", *branches_to_push])
else:
    print(
        "Changes did not pushed. Command for manual pushing:"
        " git push --tags origin master " + " ".join(branches_to_push)
    )
