# Copyright (c) 2019 Artem S. Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

"""
Tool for updating Iconic font
=============================

Downloads archive from https://github.com/Templarian/MaterialDesign-Webfont and
updates font file with icon_definitions.
"""

import os
import requests
import zipfile
import shutil
import re
import json

os.chdir(os.path.dirname(__file__))
# Paths to files in kivymd repository
font_path = "../fonts/materialdesignicons-webfont.ttf"
icon_definitions_path = "../icon_definitions.py"

font_version = "master"
# URL to download new archive (set None if already downloaded)
url = (
    f"https://github.com/Templarian/MaterialDesign-Webfont"
    f"/archive/{font_version}.zip"
)
# url = None

# Paths to files in loaded archive
temp_path = os.path.abspath("temp")
temp_repo_path = f"{temp_path}/MaterialDesign-Webfont-{font_version}"
temp_font_path = f"{temp_repo_path}/fonts/materialdesignicons-webfont.ttf"
temp_preview_path = f"{temp_repo_path}/preview.html"

# Regex
re_icons_json = re.compile(r"(?<=var icons = )[\S ]+(?=;)")
re_additional_icons = re.compile(r"(?<=icons\.push\()[\S ]+(?=\);)")
re_version = re.compile(r"(?<=<span class=\"version\">)[\d.]+(?=</span>)")
re_quote_keys = re.compile(r"([{\s,])(\w+)(:)")
re_icon_definitions = re.compile(r"md_icons = {\n([ ]{4}[\s\S]*,\n)*}")
re_version_in_file = re.compile(r"(?<=LAST UPDATED: Version )[\d.]+(?=\n)")


def download_file(url, path):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        return False
    with open(path, "wb") as f:
        shutil.copyfileobj(response.raw, f)
    return True


def unzip_archive(archive_path, dir_path):
    with zipfile.ZipFile(archive_path, "r") as zip_ref:
        zip_ref.extractall(dir_path)


def get_icons_list():
    # There is js array with icons in file preview.html
    with open(temp_preview_path, "r") as f:
        preview_file = f.read()
    # Find version
    version = re_version.findall(preview_file)[0]
    # Load icons
    jsons_icons = re_icons_json.findall(preview_file)[0]
    json_icons = re_quote_keys.sub(r'\1"\2"\3', jsons_icons)
    icons = json.loads(json_icons)
    # Find additional icons (like a blank icon)
    # jsons_additional_icons = re_additional_icons.findall(preview_file)
    # for j in jsons_additional_icons:
    #     json_additional_icons = re_quote_keys.sub(r'\1"\2"\3', j)
    #     icons.append(json.loads(json_additional_icons))
    return icons, version


def make_icon_definitions(icons):
    # Make python dict ("name": hex)
    icon_definitions = "md_icons = {\n"
    for i in icons:
        icon_definitions += " " * 4
        if len(i["hex"]) != 4:
            # Some icons has 5-digit unicode
            i["hex"] = "0" * (8 - len(i["hex"])) + i["hex"]
            icon_definitions += f'"{i["name"]}": "\\U{i["hex"].upper()}",\n'
        else:
            icon_definitions += f'"{i["name"]}": "\\u{i["hex"].upper()}",\n'
    icon_definitions += " " * 4 + f'"blank": " ",\n'  # Add blank icon (space)
    icon_definitions += "}"
    return icon_definitions


def export_icon_definitions(icon_definitions, version):
    with open(icon_definitions_path, "r") as f:
        icon_definitions_file = f.read()
    # Change md_icons list
    new_icon_definitions = re_icon_definitions.sub(
        icon_definitions.replace("\\", "\\\\"), icon_definitions_file, 1
    )
    # Change version
    new_icon_definitions = re_version_in_file.sub(
        version, new_icon_definitions, 1
    )
    with open(icon_definitions_path, "w") as f:
        f.write(new_icon_definitions)


def main():
    if url is not None:
        print(f"Downloading Material Design Icons from {url}")
        if download_file(url, "iconic-font.zip"):
            print("Archive downloaded")
        else:
            print("Could not download archive")
    else:
        print("URL is None. Do not download archive")
    if os.path.exists("iconic-font.zip"):
        unzip_archive("iconic-font.zip", temp_path)
        print("Unzip successful")
        os.remove("iconic-font.zip")
    if os.path.exists(temp_repo_path):
        shutil.copy2(temp_font_path, font_path)
        print("Font copied")
        icons, version = get_icons_list()
        print(f"Version {version}. {len(icons)} icons loaded")
        icon_definitions = make_icon_definitions(icons)
        export_icon_definitions(icon_definitions, version)
        print("File icon_definitions.py updated")
        shutil.rmtree(temp_path, ignore_errors=True)
        print(
            f'\nSuccessful. Commit message: "Update Iconic font (v{version})"'
        )
    else:
        print(f"{temp_repo_path} not exists")


if __name__ == "__main__":
    main()
