from kivy.clock import Clock

def next_frame(func, *args, **kwargs):
    if time := kwargs.get("t"):
        del kwargs["t"]
        return Clock.schedule_once(lambda _: func(*args, **kwargs), time)
    else:
        return Clock.schedule_once(lambda _: func(*args, **kwargs))
