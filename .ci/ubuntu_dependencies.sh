# See https://github.com/kivy/kivy/blob/master/.github/workflows/test_ubuntu_python.yml

# Environment variables
echo "DISPLAY=:99.0" >> $GITHUB_ENV

# System dependencies
sudo apt-get update
sudo apt-get -y install \
  libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev \
  libgstreamer1.0-dev gstreamer1.0-alsa gstreamer1.0-plugins-base \
  libsmpeg-dev libswscale-dev libavformat-dev libavcodec-dev libjpeg-dev libtiff5-dev libx11-dev libmtdev-dev \
  build-essential libgl1-mesa-dev libgles2-mesa-dev \
  xvfb pulseaudio xsel

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

# Start X-Server
/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background \
  --exec /usr/bin/Xvfb -- :99 -screen 0 1280x720x24 -ac +extension GLX
