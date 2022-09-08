# See https://github.com/kivy/kivy/blob/master/.github/workflows/test_osx_python.yml

# Environment variables
echo "KIVY_GL_BACKEND=mock" >> $GITHUB_ENV
echo "CC=clang" >> $GITHUB_ENV
echo "CXX=clang" >> $GITHUB_ENV
echo "FFLAGS=-ff2c" >> $GITHUB_ENV
echo "USE_SDL2=1" >> $GITHUB_ENV
echo "USE_GSTREAMER=1" >> $GITHUB_ENV

# System dependencies
source .ci/macos_versions.sh

download_cache_curl() {
  fname="$1"
  key="$2"
  url_prefix="$3"

  if [ ! -f $key/$fname ]; then
    if [ ! -d $key ]; then
      mkdir "$key"
    fi
    curl -O -L "$url_prefix/$fname"
    cp "$fname" "$key"
  else
    cp "$key/$fname" .
  fi
}

download_cache_aria2() {
  fname="$1"
  key="$2"
  url_prefix="$3"

  if [ ! -f $key/$fname ]; then
    if [ ! -d $key ]; then
      mkdir "$key"
    fi
    /usr/local/aria2/bin/aria2c -x 10 "$url_prefix/$fname"
    cp "$fname" "$key"
  else
    cp "$key/$fname" .
  fi
}

download_cache_curl "aria2-$ARIAL2-osx-darwin.dmg" "macos-cache" "https://github.com/aria2/aria2/releases/download/release-$ARIAL2"
hdiutil attach aria2-$ARIAL2-osx-darwin.dmg
sudo installer -package "/Volumes/aria2 $ARIAL2 Intel/aria2.pkg" -target /

download_cache_curl "SDL2-$SDL2.dmg" "macos-cache" "https://www.libsdl.org/release"
download_cache_curl "SDL2_image-$SDL2_IMAGE.dmg" "macos-cache" "https://www.libsdl.org/projects/SDL_image/release"
download_cache_curl "SDL2_mixer-$SDL2_MIXER.dmg" "macos-cache" "https://www.libsdl.org/projects/SDL_mixer/release"
download_cache_curl "SDL2_ttf-$SDL2_TTF.dmg" "macos-cache" "https://www.libsdl.org/projects/SDL_ttf/release"

hdiutil attach SDL2-$SDL2.dmg
sudo cp -a /Volumes/SDL2/SDL2.framework /Library/Frameworks/
hdiutil attach SDL2_image-$SDL2_IMAGE.dmg
sudo cp -a /Volumes/SDL2_image/SDL2_image.framework /Library/Frameworks/
hdiutil attach SDL2_ttf-$SDL2_TTF.dmg
sudo cp -a /Volumes/SDL2_ttf/SDL2_ttf.framework /Library/Frameworks/
hdiutil attach SDL2_mixer-$SDL2_MIXER.dmg
sudo cp -a /Volumes/SDL2_mixer/SDL2_mixer.framework /Library/Frameworks/

download_cache_aria2 "gstreamer-1.0-$GSTREAMER-x86_64.pkg" "macos-cache" "https://gstreamer.freedesktop.org/data/pkg/osx/$GSTREAMER"
download_cache_aria2 "gstreamer-1.0-devel-$GSTREAMER-x86_64.pkg" "macos-cache-gst-devel" "https://gstreamer.freedesktop.org/data/pkg/osx/$GSTREAMER"

sudo installer -package gstreamer-1.0-$GSTREAMER-x86_64.pkg -target /
sudo installer -package gstreamer-1.0-devel-$GSTREAMER-x86_64.pkg -target /

# Pip dependencies
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user

python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade \
  cython \
  pytest pytest-cov pytest_asyncio pytest-timeout coveralls \
  pillow docutils pygments pyinstaller[hook_testing] \
  sphinx sphinxcontrib-blockdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-nwdiag
python -m pip install --upgrade kivy==$KIVY_VERSION
