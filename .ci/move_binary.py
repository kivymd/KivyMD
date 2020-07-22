#!/bin/python3
import os
import shutil
import subprocess
import sys
from os import environ as env

binary_filename = os.path.abspath(sys.argv[1])
master_repository_directory = os.path.abspath(sys.argv[2])
data_repository = sys.argv[3]
data_repository_directory = os.path.abspath(data_repository)
demo_name = sys.argv[4]
directory = f"demo_{demo_name}"

os.chdir(master_repository_directory)

filename = os.path.basename(binary_filename)
commit_hash = (
    subprocess.check_output(["git", "rev-parse", "--verify", "--short", "HEAD"])
    .decode("utf-8")
    .strip()
)
commit_subject = (
    subprocess.check_output(["git", "log", "-1", "--pretty=format:'%s'"])
    .decode("utf-8")
    .strip()
)

is_tag = env["GITHUB_EVENT_NAME"] == "push" and env["GITHUB_REF"].startswith(
    "refs/tags"
)
if not is_tag:
    directory = os.path.join(directory, "bin")
    is_pr = env["GITHUB_REF"].startswith("refs/pull")
    if is_pr:
        # Pull Request - prN (pr1)
        middle = "pr" + env["GITHUB_REF"].split("/")[2]
        directory = os.path.join(directory, "prs")
    else:
        # Latest commit - short hash (20f2448)
        middle = commit_hash
    filename_split = filename.split("-")
    filename = "-".join([*filename_split[:2], middle, *filename_split[2:]])

# Set author info to the latest commit author
author_name = subprocess.check_output(
    ["git", "log", "-1", "--pretty=format:'%an'"]
).decode("utf-8")
author_email = subprocess.check_output(
    ["git", "log", "-1", "--pretty=format:'%ae'"]
).decode("utf-8")
files_to_commit = []

# Move file
os.chdir(data_repository_directory)
os.makedirs(directory, exist_ok=True)
if is_tag:
    # Move old release file
    try:
        old_file = [
            file
            for file in os.listdir(directory)
            if os.path.isfile(file)
            and os.path.splitext(file)[1] == os.path.splitext(filename)[1]
        ][0]
        shutil.move(
            os.path.join(directory, old_file),
            os.path.join(directory, "bin", old_file),
        )
        files_to_commit.append(os.path.join(directory, "bin", old_file))
    except (IndexError, FileNotFoundError):
        pass
shutil.copy(binary_filename, os.path.join(directory, filename))
files_to_commit.append(os.path.join(directory, filename))

# Push changes
subprocess.check_call(["git", "config", "user.name", author_name])
subprocess.check_call(["git", "config", "user.email", author_email])
subprocess.check_call(
    ["git", "pull", "--ff-only"]
)  # Ensure that there is no changes
subprocess.check_call(["git", "add", *files_to_commit])
subprocess.check_call(
    ["git", "commit", "-m", f'Add binary for {commit_hash}: "{commit_subject}"']
)
subprocess.check_call(["git", "push"])

print(
    f"Binary file: {env['GITHUB_SERVER_URL']}/{env['GITHUB_REPOSITORY']}/blob/"
    f"{data_repository}/{directory}/{filename}"
)
