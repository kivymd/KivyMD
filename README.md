# KivyMD [0.104.1](https://kivymd.readthedocs.io/en/latest/changelog/index.html)

<img align="left" width="256" src="https://github.com/kivymd/internal/raw/main/logo/kivymd.png"/>

KivyMD is a collection of Material Design compliant widgets for use with [Kivy](http://kivy.org), a framework for cross-platform, touch-enabled graphical applications.

The project's goal is to approximate Google's [Material Design spec](https://material.io/design/introduction/) as close as possible without sacrificing ease of use or application performance.

This library is a fork of the [KivyMD project](https://gitlab.com/kivymd/KivyMD) the author of which stopped supporting this project three years ago. We found the strength and brought this project to a new level.

Currently we're in **beta** status, so things are changing all the time and we cannot promise any kind of API stability. However it is safe to vendor now and make use of what's currently available.

Join the project! Just fork the project, branch out and submit a pull request when your patch is ready. If any changes are necessary, we'll guide you through the steps that need to be done via PR comments or access to your for may be requested to outright submit them.

If you wish to become a project developer (permission to create branches on the project without forking for easier collaboration), have at least one PR approved and ask for it. If you contribute regularly to the project the role may be offered to you without asking too.

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/kivymd)](https://pepy.tech/project/kivymd)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Discord](https://img.shields.io/discord/566880874789076992?logo=discord)](https://discord.gg/wu3qBST)
[![Twitter](https://img.shields.io/twitter/follow/KivyMD?label=follow&logo=twitter&style=flat&color=brightgreen)](https://twitter.com/KivyMD)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=1k)](https://www.youtube.com/c/KivyMD)
[![Habr](https://img.shields.io/static/v1?label=habr&message=ru&logo=habr&color=brightgreen)](https://habr.com/ru/users/kivymd/posts)
[![StackOverflow](https://img.shields.io/static/v1?label=stackoverflow%20tag&logo=stackoverflow&logoColor=fe7a16&color=brightgreen&message=kivymd)](https://stackoverflow.com/tags/kivymd)
[![Open Collective](https://img.shields.io/opencollective/all/kivymd?label=financial%20contributors&logo=open-collective)](https://opencollective.com/kivymd)

[![Coverage status](https://coveralls.io/repos/github/kivymd/KivyMD/badge.svg)](https://coveralls.io/github/kivymd/KivyMD)
[![Build workflow](https://github.com/kivymd/KivyMD/workflows/Build/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ABuild)
[![Test workflow](https://github.com/kivymd/KivyMD/workflows/Test/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3ATest)
[![Build demos workflow](https://github.com/kivymd/KivyMD/workflows/Build%20demos/badge.svg?branch=master)](https://github.com/kivymd/KivyMD/actions?query=workflow%3A"Build+demos")
[![Documentation status](https://readthedocs.org/projects/kivymd/badge/?version=latest)](https://kivymd.readthedocs.io)
[![Documentation status](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)

## Installation

```bash
pip install kivymd==0.104.1
```

### Dependencies:

- [Kivy](https://github.com/kivy/kivy) >= 1.10.1 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)

### How to install

Command [above](#installation) will install latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd).

If you want to install development version from [master](https://github.com/kivymd/KivyMD/tree/master/)
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

**_Speed Tip_**: If you don't need full commit history (about 160 MiB), you can
use a shallow clone (`git clone https://github.com/kivymd/KivyMD.git --depth 1`)
to save time. If you need full commit history, then remove `--depth 1`.

### How to use with [Buildozer](https://github.com/kivy/buildozer)

```ini
requirements = kivy==1.11.1, kivymd==0.104.1
```

This will download latest release version of KivyMD from [PyPI](https://pypi.org/project/kivymd).

If you want to use development version from [master](https://github.com/kivymd/KivyMD/tree/master/)
branch, you should specify link to zip archive:

```ini
requirements = kivy==1.11.1, https://github.com/kivymd/KivyMD/archive/master.zip
```

Do not forget to run `buildozer android clean` or remove `.buildozer` directory
before building if version was updated (Buildozer doesn't update already
downloaded packages).

#### On Linux

Use Buildozer [directly](https://github.com/kivy/buildozer#installing-buildozer-with-target-python-3-default)
or via [Docker](https://github.com/kivy/buildozer/blob/master/Dockerfile).

#### On Windows 10

Install [Ubuntu WSL](https://ubuntu.com/wsl) and follow [Linux steps](#On-Linux).

#### On Windows without WSL

Install VirtualBox and follow steps from [here](https://github.com/kivymd/KivyMD/blob/9b969f39d8bb03c73de105b82e66de3820020eb9/README.md#building-with-vm).

#### Build automatically via GitHub Actions

Use [ArtemSBulgakov/buildozer-action@v1](https://github.com/ArtemSBulgakov/buildozer-action)
to build your packages automatically on push or pull request.
See [full workflow example](https://github.com/ArtemSBulgakov/buildozer-action#full-workflow).


## Documentation

See documentation at https://kivymd.readthedocs.io

Wiki with examples of using KivyMD widgets: https://github.com/kivymd/KivyMD/wiki

[Kitchen sink](https://github.com/kivymd/KivyMD/tree/master/demos/kitchen_sink) app demonstrates every KivyMD widget. You can see how to use widget in code of app. You can download apk for your smartphone (Android 6.0 and higher): [kivymd/storage (binaries branch)](https://github.com/kivymd/storage/tree/binaries/demo_kitchen_sink).

### Tutorials on YouTube

<p align="center">
  <a href="https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1">
    <img width="400" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/tutorial.png" title="Click to watch KivyMD Tutorials on YouTube">
  </a>
</p>

[Tutorials](https://www.youtube.com/watch?v=kRWtSkIYPFI&list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell&index=1) by [Erik Sandberg](https://github.com/Dirk-Sandberg) show you how to create application with KivyMD and use its widgets.

### Comparison of Flutter & KivyMD

<p align="center">
  <a href="https://www.youtube.com/watch?v=P-ylDDm4TJM">
    <img width="600" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/preview-youtube-2.png" title="Click to watch it on YouTube">
  </a>
</p>

## Support

If you need assistance or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/wu3qBST (English #support, Russian #ru-support)
- _StackOverflow tag:_ [kivymd](https://stackoverflow.com/tags/kivymd)
- _Email:_ kivydevelopment@gmail.com

## Settings

#### [Syntax highlighting and auto-completion for Kivy/KivyMD .kv files in PyCharm/Intellij IDEA](https://github.com/noembryo/KV4Jetbrains)

## API Breaking changes

- [Changed MDExpansionPanel panel creation](https://kivymd.readthedocs.io/en/latest/components/expansion-panel/index.html)
- [Changed the use of the MDDropdownMenu](https://kivymd.readthedocs.io/en/latest/components/menu/index.html)
- [Changed the use of the MDDropDownItem](https://kivymd.readthedocs.io/en/latest/components/dropdown-item/index.html)
- [Changed the use of the MDDialog](https://kivymd.readthedocs.io/en/latest/components/dialog/index.html)

## Video preview

<p align="center">
  <a href="https://www.youtube.com/watch?v=HCa8zij69kY">
    <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/prevideo.png" title='Click to watch video on YouTube'>
  </a>
</p>

## Image preview

<p align="center">
  <img src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/previous.png">
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
pytest kivymd/tests --timeout=300 --cov=kivymd --cov-report=term
```

pre-commit will format modified files with Black and sort imports with isort.

## Sister projects

<img align="left" width="128" src="https://github.com/kivymd/internal/raw/main/logo/kivymd_extensions.png"/>

## KivyMD Extensions

Additional extensions for the KivyMD library.

https://github.com/kivymd-extensions


## License

KivyMD is released under the terms of the [MIT License](https://github.com/kivymd/KivyMD/blob/master/LICENSE), same as [Kivy](https://github.com/kivy/kivy/blob/master/LICENSE).

[Roboto font](https://fonts.google.com/specimen/Roboto) is licensed and distributed under the terms of the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

[Iconic font](https://github.com/Templarian/MaterialDesign-Webfont) by the [Material Design Icons](https://materialdesignicons.com/) community covered by [SIL Open Font License 1.1](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web)

## Contributors

### KivyMD Team

They spent a lot of time to improve KivyMD.

- Yuri Ivanov [@HeaTTheatR](https://github.com/HeaTTheatR) - Core developer
- Artem Bulgakov [@ArtemSBulgakov](https://github.com/ArtemSBulgakov) - Technical administrator, contributor
- Andrés Rodríguez [@mixedCase](https://github.com/mixedCase) - First author of KivyMD project, contributor

### Code Contributors

This project exists thanks to all the people who contribute.
*[How to contribute](#Contributing)*

<a href="https://github.com/kivymd/KivyMD/graphs/contributors"><img src="https://opencollective.com/kivymd/contributors.svg?width=890&button=false" /></a>

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
<a href="https://opencollective.com/kivymd/gold-sponsor/20/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/20/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/21/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/21/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/22/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/22/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/23/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/23/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/24/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/24/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/25/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/25/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/26/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/26/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/27/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/27/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/28/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/28/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/gold-sponsor/29/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/gold-sponsor/29/avatar.svg?requireActive=false"></a>

#### Backers

[Become a Backer](https://opencollective.com/kivymd/contribute/backer-16159)
and get your image on our Readme with a link to your website. Also you will get
a gift in the future.

<a href="https://opencollective.com/kivymd/backer/0/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/0/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/1/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/1/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/2/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/2/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/3/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/3/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/4/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/4/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/5/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/5/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/6/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/6/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/7/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/7/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/8/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/8/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/9/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/9/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/10/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/10/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/11/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/11/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/12/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/12/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/13/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/13/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/14/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/14/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/15/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/15/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/16/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/16/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/17/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/17/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/18/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/18/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/19/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/19/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/20/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/20/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/21/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/21/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/22/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/22/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/23/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/23/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/24/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/24/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/25/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/25/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/26/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/26/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/27/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/27/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/28/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/28/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/29/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/29/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/30/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/30/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/31/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/31/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/32/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/32/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/33/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/33/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/34/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/34/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/35/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/35/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/36/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/36/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/37/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/37/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/38/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/38/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/39/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/39/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/40/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/40/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/41/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/41/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/42/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/42/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/43/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/43/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/44/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/44/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/45/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/45/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/46/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/46/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/47/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/47/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/48/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/48/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/49/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/49/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/50/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/50/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/51/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/51/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/52/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/52/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/53/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/53/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/54/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/54/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/55/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/55/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/56/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/56/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/57/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/57/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/58/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/58/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/59/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/59/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/60/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/60/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/61/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/61/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/62/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/62/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/63/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/63/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/64/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/64/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/65/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/65/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/66/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/66/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/67/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/67/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/68/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/68/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/69/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/69/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/70/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/70/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/71/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/71/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/72/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/72/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/73/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/73/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/74/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/74/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/75/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/75/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/76/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/76/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/77/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/77/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/78/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/78/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/79/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/79/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/80/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/80/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/81/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/81/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/82/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/82/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/83/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/83/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/84/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/84/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/85/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/85/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/86/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/86/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/87/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/87/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/88/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/88/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/89/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/89/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/90/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/90/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/91/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/91/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/92/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/92/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/93/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/93/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/94/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/94/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/95/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/95/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/96/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/96/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/97/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/97/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/98/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/98/avatar.svg?requireActive=false"></a>
<a href="https://opencollective.com/kivymd/backer/99/website?requireActive=false" target="_blank"><img src="https://opencollective.com/kivymd/backer/99/avatar.svg?requireActive=false"></a>
