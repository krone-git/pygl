from itertools import chain
from datetime import datetime


class Engine:
    def __init__(self, shapes=(), views=()):
        self._active = False
        self._shapes = set(shapes)
        self._views = set(views)
        self._timestamp = None
        self._timedelay = 0

    is_active = lambda self: self._active
    timestamp = lambda self: self._timestamp

    def set_timestamp(self, time):
        self._timestamp = time
        return self

    def set_timedelay(self, timedelay):
        self._timedelay = timedelay
        return self

    init_updatehook = lambda self: None
    open_updatehook = lambda self, timedelay: None
    main_updatehook = lambda self, timedelay: None
    close_updatehook = lambda self, timedelay: None

    def update(self):
        if self._active:
            self.init_updatehook()
            now = datetime.now()
            timedelay = (now - self.timestamp()).total_seconds()
            self.set_timestamp(now)
            self.set_timedelay(timedelay)

            self.open_updatehook(timedelay)
            self.update_shapes(timedelay)
            self.update_cameras(timedelay)
            self.main_updatehook(timedelay)
            self.update_views(timedelay)
            self.close_updatehook(timedelay)
            return self

    def update_shapes(self, timedelay):
        [shape.update(timedelay) for shape in self._shapes]
        return self

    def update_cameras(self, timedelay):
        [view.camera().update(timedelay) for view in self._views]
        return self

    def update_views(self, timedelay):
        faces = chain(*(shape.iter_faces() for shape in self._shapes))
        [view.update(timedelay, faces) for view in self._views]
        return self

    def start(self):
        self._active = True
        self.set_timestamp(datetime.now())
        self.update()
        return self

    def stop(self):
        self._active = False
        return self


    add_shape = lambda self, shape: self._shapes.add(shape)
    remove_shape = lambda self, shape: self._shapes.discard(shape)

    add_view = lambda self, view: self._views.add(view)
    remove_view = lambda self, view: self._views.discard(view)
