# KivyMD [2.0.0](https://kivymd.readthedocs.io/en/latest/changelog/index.html)

<img align="right" height="256" src="https://github.com/kivymd/internal/raw/main/logo/kivymd_logo_blue.png"/>

KivyMD is a collection of Material Design compliant widgets for use with
[Kivy](http://kivy.org), a framework for cross-platform, touch-enabled
graphical applications.

The project's goal is to approximate Google's
[Material Design spec](https://material.io/design/introduction/) as close as
possible without sacrificing ease of use. This library is a fork of the
[KivyMD project](https://gitlab.com/kivymd/KivyMD). We found the strength and
brought this project to a new level.

Join the project! Just fork the project, branch out and submit a pull request
when your patch is ready. If any changes are necessary, we'll guide you through
the steps that need to be done via PR comments or access to your for may be
requested to outright submit them.

If you wish to become a project developer (permission to create branches on the
project without forking for easier collaboration), have at least one PR
approved and ask for it. If you contribute regularly to the project the role
may be offered to you without asking too.

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/kivymd)](https://pepy.tech/project/kivymd)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Discord](https://img.shields.io/discord/566880874789076992?logo=discord)](https://discord.gg/wu3qBST)
[![Twitter](https://img.shields.io/twitter/follow/KivyMD?label=follow&logo=twitter&style=flat&color=brightgreen)](https://twitter.com/KivyMD)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=5k)](https://www.youtube.com/c/KivyMD)
[![Habr](https://img.shields.io/static/v1?label=habr&message=ru&logo=habr&color=brightgreen)](https://habr.com/ru/users/kivymd/posts)
[![StackOverflow](https://img.shields.io/static/v1?label=stackoverflow%20tag&logo=stackoverflow&logoColor=fe7a16&color=brightgreen&message=kivymd)](https://stackoverflow.com/tags/kivymd)
[![Open Collective](https://img.shields.io/opencollective/all/kivymd?label=financial%20contributors&logo=open-collective)](https://opencollective.com/kivymd)

[![Coverage status](https://coveralls.io/repos/github/kivymd/KivyMD/badge.svg)](https://coveralls.io/github/kivymd/KivyMD)
[![Build workflow](https://github.com/kivymd/KivyMD/workflows/Build/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ABuild)
[![Test workflow](https://github.com/kivymd/KivyMD/workflows/Test/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ATest)
[![Documentation status](https://readthedocs.org/projects/kivymd/badge/?version=latest)](https://kivymd.readthedocs.io)
[![Repository size](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://github.com/kivymd/KivyMD)

## Installation

```bash
pip install kivymd==2.0.0
```

### Dependencies:

- [Kivy](https://github.com/kivy/kivy) >= 2.3.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.7+](https://www.python.org/)
- [Pillow](https://github.com/python-pillow/Pillow/)
- [MaterialColor](https://github.com/T-Dynamos/materialyoucolor-python)
- [asynckivy](https://github.com/asyncgui/asynckivy)

### How to install

Command [above](#installation) will install latest release version of KivyMD from 
[PyPI](https://pypi.org/project/kivymd).

If you want to install development version from 
[master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```bash
pip install https://github.com/kivymd/KivyMD/archive/master.zip
```

**_Tip_**: Replace `master.zip` with `<commit hash>.zip` (eg `51b8ef0.zip`) to
download KivyMD from specific commit.

Also you can install manually from sources. Just clone the project and run pip:

```bash
git clone https://github.com/kivymd/KivyMD.git --depth 1
cd KivyMD
pip install .
```

**_Speed Tip_**: If you don't need full commit history (about 1.14 GiB), you can
use a shallow clone (`git clone https://github.com/kivymd/KivyMD.git --depth 1`)
to save time. If you need full commit history, then remove `--depth 1`.

### How to use with [Buildozer](https://github.com/kivy/buildozer)

```ini
requirements = python3,
    kivy,
    https://github.com/kivymd/KivyMD/archive/master.zip,
    materialyoucolor,
    exceptiongroup,
    asyncgui,
    asynckivy,
    android
```

This will download latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd).

If you want to use development version from [master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```ini
requirements = kivy, https://github.com/kivymd/KivyMD/archive/master.zip
```

Do not forget to run `buildozer android clean` or remove `.buildozer` directory
before building if version was updated (Buildozer doesn't update already
downloaded packages).

#### On Linux

- Use Buildozer [directly](https://github.com/kivy/buildozer#installing-buildozer-with-target-python-3-default) 
  or via [Docker](https://github.com/kivy/buildozer/blob/master/Dockerfile).

#### On Windows 10

- Install [Ubuntu WSL](https://ubuntu.com/wsl) and follow [Linux steps](#On-Linux).

#### Build automatically via GitHub Actions

- Use [ArtemSBulgakov/buildozer-action@v1](https://github.com/ArtemSBulgakov/buildozer-action)
  to build your packages automatically on push or pull request.
- See [full workflow example](https://github.com/ArtemSBulgakov/buildozer-action#full-workflow).

### How to use with [kivy-ios](https://github.com/kivy/kivy-ios)

```bash
toolchain build python3 kivy pillow
toolchain pip install --no-deps kivymd
```

## Documentation

- See documentation at https://kivymd.readthedocs.io
- Wiki with examples of using KivyMD widgets: https://github.com/kivymd/KivyMD/wiki

### Demos

<p align="center">
  <a href="https://www.youtube.com/watch?v=4er9b6TH_TA">
    <img 
        width="600" 
        src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-kitchen-sink.png" 
        title="Click to watch demo application of the KivyMD library widgets"
    >
  </a>
</p>

[Kitchen sink](https://github.com/kivymd/KitchenSink) app demonstrates every KivyMD widget.
You can see how to use widget in code of app.

### Comparison of Flutter & KivyMD

| Sky View Concept | Healthy Food Delivery |
:-------------------------:|:-------------------------:
<a href="https://www.youtube.com/watch?v=xvi2D1c4mfQ"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-youtube-1.png" title="Click to watch it on YouTube"></a>  |  <a href="https://www.youtube.com/watch?v=P-ylDDm4TJM"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-youtube-2.png" title="Click to watch it on YouTube"></a>
| Asics Shoes Concept | Facebook Desktop Redesign |
<a href="https://www.youtube.com/watch?v=ehuXPgun0k0"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-youtue.png" title="Click to watch it on YouTube"></a>  |  <a href="https://www.youtube.com/watch?v=ZNBQib6Hk4s"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-youtue-3.png" title="Click to watch it on YouTube"></a>

## Use MVC and Hot Reload

<p align="center">
  <a href="https://www.youtube.com/watch?v=JLBrgoSSeTU&t">
    <img 
        img width="600" 
        src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/hot-reload-preview-youtube.png" 
        title='Click to watch video on YouTube'
    >
  </a>
</p>

## Support

If you need assistance or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/wu3qBST (English #support, Russian #ru-support)
- **StackOverflow tag:** [kivymd](https://stackoverflow.com/tags/kivymd)
- **Email:** KivyMD-library@yandex.com

## Settings

#### [Syntax highlighting and auto-completion for Kivy/KivyMD .kv files in PyCharm/Intellij IDEA](https://github.com/noembryo/KV4Jetbrains)

## Promo Video

<p align="center">
  <a href="https://www.youtube.com/watch?v=crt8wA4Q5eU">
    <img 
        img width="600" 
        src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/prevideo.png" 
        title='Click to watch video on YouTube'
    >
  </a>
</p>

## Contributing

We always welcome your [Bug reports](https://github.com/kivymd/KivyMD/issues/new?template=bug_report.md),
[Feature requests](https://github.com/kivymd/KivyMD/issues/new?template=feature_request.md)
and [Pull requests](https://github.com/kivymd/KivyMD/pulls)!
Check out [CONTRIBUTING.md](https://github.com/kivymd/.github/blob/master/.github/CONTRIBUTING.md)
and feel free to improve KivyMD.

### Setup environment

We recommend you to use PyCharm to work with KivyMD code. Install
[Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html) and
development dependencies to your virtual environment:

```bash
pip install -e .[dev,docs]
pre-commit install
```

Format all files and run tests:

```bash
pre-commit run --all-files
pytest kivymd/tests --timeout=600 --cov=kivymd --cov-report=term
```

pre-commit will format modified files with Black and sort imports with isort.

## Sister projects

<img align="left" width="128" src="https://github.com/kivymd/internal/raw/main/logo/kivymd_extensions.png"/>

## KivyMD Extensions

Additional extensions for the KivyMD library.

https://github.com/kivymd-extensions

<img align="left" width="128" src="https://github.com/kivymd/internal/raw/main/logo/kivymdbuilder.png"/>

## KivyMDBuilder

Build apps visually.

https://github.com/kivymd/KivyMDBuilder


## License

- KivyMD is released under the terms of the 
  [MIT License](https://github.com/kivymd/KivyMD/blob/master/LICENSE), 
  same as [Kivy](https://github.com/kivy/kivy/blob/master/LICENSE).
- [Roboto font](https://fonts.google.com/specimen/Roboto) 
  is licensed and distributed under the terms of the 
  [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
- [Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) by the 
  [Material Design Icons](https://materialdesignicons.com/) community covered by 
  [SIL Open Font License 1.1](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web)

## Contributors

### KivyMD Team

They spent a lot of time to improve KivyMD.

- Yuri Ivanov [@HeaTTheatR](https://github.com/HeaTTheatR) - Core developer
- Artem Bulgakov [@ArtemSBulgakov](https://github.com/ArtemSBulgakov) - Technical administrator, contributor
- Andrés Rodríguez [@mixedCase](https://github.com/mixedCase) - First author of KivyMD project, contributor

### Code Contributors

This project exists thanks to all the people who contribute.
*[How to contribute](#Contributing)*

<a href="https://github.com/kivymd/KivyMD/graphs/contributors">
    <img src="https://opencollective.com/kivymd/contributors.svg?width=890&button=false"/>
</a>

### Financial Contributors

[Become a financial contributor](https://opencollective.com/kivymd#section-contribute) 
on OpenCollective and help us sustain our community.

#### Gold Sponsors

[Become a Gold Sponsor](https://opencollective.com/kivymd/contribute/gold-sponsor-16160)
and get your logo on our Readme with a link to your website.

| Peter Šurda | Route4Me Route Planner |
:-------------------------:|:-------------------------:
<a href="https://opencollective.com/peter-surda"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/gold-sponsor-1-1.png" title="Peter Šurda"></a> |  <a href="https://opencollective.com/route4me"><img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/gold-sponsor-1-2.png" title="Route4Me Route Planner"></a>
<!-- FIXME: sponsors are not displayed -->

<a href="https://route4me.com" target="_blank" style="display: inline-block; text-align: center;">
    <div style="text-align: center;">
        <img width="280" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/route4me.png" alt="Best Route Planner"><br>
        Best Route Planner - Route Optimization Software
    </div>
</a>

#### Backers

[Become a Backer](https://opencollective.com/kivymd/contribute/backer-16159) if you want to help develop this project.

<a href="https://opencollective.com/kivymd#backers" target="_blank">
    <img src="https://opencollective.com/kivymd/backers.svg?width=890">
</a>
