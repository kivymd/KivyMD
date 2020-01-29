KivyToast
========

A package for working with messages like Toast on Android. It is intended for use in applications written using the Kivy framework.

This package is an improved version of the package https://github.com/knappador/kivy-toaster in which human toasts are written, written on Kivy.

<img src="https://raw.githubusercontent.com/HeaTTheatR/KivyToast/master/Screenshot.png" align="center"/>

The package modules are written using the framework for cross-platform development of <Kivy>.
Information about the <Kivy> framework is available at http://kivy.org.

An example of usage (note that with this import the native implementation of toasts will be used for the Android platform and implementation on Kivy for others:

```python
from toast import toast

...

# And then in the code, toasts are available
# by calling the toast function:
toast ('Your message')
```

To force the Kivy implementation on the Android platform, use the import of the form:

```python
from toast.kivytoast import toast
```

PROGRAMMING LANGUAGE
--------------------
Python 2.7 +

DEPENDENCE
----------
The [Kivy] framework (http://kivy.org/docs/installation/installation.html)

LICENSE
-------
MIT