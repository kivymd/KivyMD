"""
asynckivy
=========

Copyright (c) 2019 Nattōsai Mitō

GitHub -
    https://github.com/gottadiveintopython
GitHub Gist -
    https://gist.github.com/gottadiveintopython/5f4a775849f9277081c396de65dc57c1

"""

__all__ = ("start", "sleep", "event")

import types
from functools import partial
from collections import namedtuple
from kivy.clock import Clock

CallbackParameter = namedtuple("CallbackParameter", ("args", "kwargs"))


def start(coro):
    def step(*args, **kwargs):
        try:
            coro.send(CallbackParameter(args, kwargs))(step)
        except StopIteration:
            pass

    try:
        coro.send(None)(step)
    except StopIteration:
        pass


@types.coroutine
def sleep(duration):
    # The partial() here looks meaningless. But this is needed in order
    # to avoid weak reference.
    param = yield lambda step_coro: Clock.schedule_once(partial(step_coro), duration)
    return param.args[0]


class event:
    def __init__(self, ed, name):
        self.bind_id = None
        self.ed = ed
        self.name = name

    def bind(self, step_coro):
        self.bind_id = bind_id = self.ed.fbind(self.name, self.callback)
        assert bind_id > 0  # check if binding succeeded
        self.step_coro = step_coro

    def callback(self, *args, **kwargs):
        self.parameter = CallbackParameter(args, kwargs)
        ed = self.ed
        ed.unbind_uid(self.name, self.bind_id)
        self.step_coro()

    def __await__(self):
        yield self.bind
        return self.parameter
