#!/bin/python3
# Generates matrix for GitHub Actions
# For workflow https://github.com/kivymd/KivyMD/blob/master/.github/workflows/build-demos.yml
# See https://stackoverflow.com/a/62953566/11948346

import json
import os
import sys
from pathlib import Path

diff = sys.argv[1]
all_demos = ["kitchen_sink", "crane", "fortnightly", "rally", "shrine"]
demos_android = []

for filename in diff.split("\n"):
    filename = Path(filename)
    if str(filename).split(os.sep, 1)[0] in ("kivymd",) or filename in (
        ".github/workflows/build-demos.yml",
        "setup.py",
        "setup.cfg",
        ".ci/move_binary",
    ):
        demos_android = all_demos
        break
    if str(filename).startswith("demos"):
        demo_name = str(filename).split(os.sep, 2)[1]
        demos_android.extend([demo_name])

matrix_android = {"include": []}
for demo_name in demos_android:
    matrix_android["include"].append({"demo-name": demo_name})

print("matrix-android:", json.dumps(matrix_android))
print("::set-output name=matrix-android::" + json.dumps(matrix_android))
print("::set-output name=empty-matrix-android::" + str(len(demos_android) == 0))
