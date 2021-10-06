# KivyMD [0.104.2](https://kivymd.readthedocs.io/en/latest/changelog/index.html)

<img align="center" height=240 src="https://github.com/kivymd/internal/raw/main/logo/github_readme_logo.png"/>

KivyMD is a collection of Material Design compliant widgets for use with [Kivy](http://kivy.org), a framework for cross-platform, touch-enabled graphical applications.

The project's goal is to approximate Google's [Material Design spec](https://material.io/design/introduction/) as close as possible without sacrificing ease of use or application performance.

This library is a fork of the [KivyMD project](https://gitlab.com/kivymd/KivyMD) the author of which stopped supporting this project four years ago. We found the strength and brought this project to a new level.

Currently we're in **beta** status, so things are changing all the time and we cannot promise any kind of API stability. However it is safe to vendor now and make use of what's currently available.

Join the project! Just fork the project, branch out and submit a pull request when your patch is ready. If any changes are necessary, we'll guide you through the steps that need to be done via PR comments or access to your for may be requested to outright submit them.

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too.

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/kivymd)](https://pepy.tech/project/kivymd)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Discord](https://img.shields.io/discord/566880874789076992?logo=discord)](https://discord.gg/wu3qBST)
[![Twitter](https://img.shields.io/twitter/follow/KivyMD?label=follow&logo=twitter&style=flat&color=brightgreen)](https://twitter.com/KivyMD)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=3k)](https://www.youtube.com/c/KivyMD)
[![Habr](https://img.shields.io/static/v1?label=habr&message=ru&logo=habr&color=brightgreen)](https://habr.com/ru/users/kivymd/posts)
[![StackOverflow](https://img.shields.io/static/v1?label=stackoverflow%20tag&logo=stackoverflow&logoColor=fe7a16&color=brightgreen&message=kivymd)](https://stackoverflow.com/tags/kivymd)
[![Open Collective](https://img.shields.io/opencollective/all/kivymd?label=financial%20contributors&logo=open-collective)](https://opencollective.com/kivymd)

[![Coverage status](https://coveralls.io/repos/github/kivymd/KivyMD/badge.svg)](https://coveralls.io/github/kivymd/KivyMD)
[![Build workflow](https://github.com/kivymd/KivyMD/workflows/Build/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ABuild)
[![Test workflow](https://github.com/kivymd/KivyMD/workflows/Test/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ATest)
[![Build demos workflow](https://github.com/kivymd/KivyMD/workflows/Build%20demos/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3A"Build+demos")
[![Documentation status](https://readthedocs.org/projects/kivymd/badge/?version=latest)](https://kivymd.readthedocs.io)
[![Repository size](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://github.com/kivymd/KivyMD)

## Installation

```bash
pip install kivymd==0.104.2
```

### Dependencies:

- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)
- [Pillow](https://github.com/python-pillow/Pillow/)

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
requirements = kivy==2.0.0, kivymd==0.104.2, sdl2_ttf == 2.0.15, pillow
```

This will download latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd).

If you want to use development version from [master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```ini
requirements = kivy==2.0.0, https://github.com/kivymd/KivyMD/archive/master.zip
```

---
**NOTE**

Until the release of the KivyMD library version 1.0.0 has been released, use
```ini
requirements = https://github.com/kivymd/KivyMD/archive/master.zip
```
---

Do not forget to run `buildozer android clean` or remove `.buildozer` directory
before building if version was updated (Buildozer doesn't update already
downloaded packages).

#### On Linux

- Use Buildozer [directly](https://github.com/kivy/buildozer#installing-buildozer-with-target-python-3-default) 
  or via [Docker](https://github.com/kivy/buildozer/blob/master/Dockerfile).

#### On Windows 10

- Install [Ubuntu WSL](https://ubuntu.com/wsl) and follow [Linux steps](#On-Linux).

#### On Windows without WSL

- Install VirtualBox and follow steps from 
[here](https://github.com/kivymd/KivyMD/blob/9b969f39d8bb03c73de105b82e66de3820020eb9/README.md#building-with-vm).

#### Build automatically via GitHub Actions

- Use [ArtemSBulgakov/buildozer-action@v1](https://github.com/ArtemSBulgakov/buildozer-action)
  to build your packages automatically on push or pull request.
- See [full workflow example](https://github.com/ArtemSBulgakov/buildozer-action#full-workflow).


## Documentation

- See documentation at https://kivymd.readthedocs.io
- Wiki with examples of using KivyMD widgets: https://github.com/kivymd/KivyMD/wiki

### Demos

[Kitchen sink](https://github.com/kivymd/KivyMD/tree/master/demos/kitchen_sink) 
app demonstrates every KivyMD widget. You can see how to use widget in code of app. 
You can download apk for your smartphone (Android 6.0 and higher): 
[kivymd/storage (binaries branch)](https://github.com/kivymd/storage/tree/binaries/demo_kitchen_sink).

Also we have Material Studies:

- [Crane](https://github.com/kivymd/KivyMD/tree/master/demos/crane)
- [Fortnightly](https://github.com/kivymd/KivyMD/tree/master/demos/fortnightly)
- [Rally](https://github.com/kivymd/KivyMD/tree/master/demos/rally)
- [Shrine](https://github.com/kivymd/KivyMD/tree/master/demos/shrine).

You can download apks for your smartphone: [kivymd/storage (binaries branch)](https://github.com/kivymd/storage/tree/binaries).

### Tutorials on YouTube

<p align="center">
  <a href="https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1">
    <img 
        width="400" 
        src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tutorial.png" 
        title="Click to watch KivyMD Tutorials on YouTube"
    >
  </a>
</p>

[Tutorials](https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1) by [Erik Sandberg](https://github.com/Dirk-Sandberg) show you how to create application with KivyMD and use its widgets.

---
**NOTE**

Some of the code examples in the video tutorials may be out of date, so if you have a problem,
check the code from the official documentation.

---

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
- **Email:** kivydevelopment@gmail.com

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

<a href="https://opencollective.com/kivymd/gold-sponsor/0/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/0/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/1/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/1/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/2/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/2/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/3/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/3/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/4/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/4/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/5/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/5/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/6/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/6/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/7/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/7/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/8/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/8/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/9/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/9/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/10/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/10/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/11/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/11/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/12/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/12/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/13/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/13/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/14/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/14/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/15/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/15/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/16/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/16/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/17/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/17/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/18/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/18/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/19/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/19/avatar.svg?requireActive=false"></a>

#### Backers

[Become a Backer](https://opencollective.com/kivymd/contribute/backer-16159) if you want to help develop this project.

<a href="https://opencollective.com/kivymd#backers" target="_blank">
    <img src="https://opencollective.com/kivymd/backers.svg?width=890">
</a>
