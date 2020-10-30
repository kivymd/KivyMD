# See https://github.com/kivy/kivy/blob/master/.github/workflows/test_windows_python.yml

# Environment variables
echo "::set-env name=GST_REGISTRY::~/registry.bin"
echo "::set-env name=KIVY_GL_BACKEND::angle_sdl2"

# Pip dependencies
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade `
  cython `
  pytest pytest-cov pytest_asyncio pytest-timeout coveralls `
  pillow pyinstaller[hook_testing] `
  pypiwin32 kivy_deps.sdl2 kivy_deps.glew kivy_deps.angle kivy_deps.gstreamer
python -m pip install --upgrade kivy==$Env:KIVY_VERSION
