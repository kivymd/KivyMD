import gettext

from kivy.lang import Observable


class Translation(Observable):
    """Original source - https://github.com/tito/kivy-gettext-example."""

    observers = []

    def __init__(self, defaultlang, domian, resource_dir):
        super().__init__()
        self.ugettext = None
        self.lang = defaultlang
        self.domian = domian
        self.resource_dir = resource_dir
        self.switch_lang(self.lang)

    def _(self, text):
        return self.ugettext(text)

    def fbind(self, name, func, args, **kwargs):
        if name == "_":
            self.observers.append((func, args, kwargs))
        else:
            return super().fbind(name, func, *args, **kwargs)

    def funbind(self, name, func, args, **kwargs):
        if name == "_":
            key = (func, args, kwargs)
            if key in self.observers:
                self.observers.remove(key)
        else:
            return super().funbind(name, func, *args, **kwargs)

    def switch_lang(self, lang):
        locales = gettext.translation(
            self.domian, self.resource_dir, languages=[lang]
        )
        try:
            self.ugettext = locales.ugettext
        except AttributeError:
            self.ugettext = locales.gettext

        for func, largs, kwargs in self.observers:
            try:
                func(largs, None, None)
            except ReferenceError:
                pass
