from collections.abc import Iterable


class EventDispatch:
    def __init__(self, handlers):
        self._handlers = tuple(handlers) if isinstance(handlers, Iterable) \
            else (handlers,)

    def dispatch(self, event):
        for handler in self._handlers:
            resp = handler(event)
            if not resp:
                break
        return self

    def dispatch_test(self, event):
        for handler in self._handlers:
            handler(event)
        return self

    dispatch_lambda = lambda self, e: [h(e) for h in self._handlers]


if __name__ == "__main__":
    import timeit

    t = lambda e: True
    h = [t] * 1000
    h[int(len(h) * 0.89) - 1] = lambda e: False
    e = None

    d = EventDispatch(h)

    print(
        timeit.timeit(lambda: d.dispatch(e)),
        timeit.timeit(lambda: d.dispatch_test(e)),
        timeit.timeit(lambda: d.dispatch_lambda(e)),
        sep="\n",
        end="\n\n"
        )
