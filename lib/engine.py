from itertools import chain
from datetime import datetime


class Engine:
    def __init__(self, shapes=(), views=(), lights=(), transforms=()):
        self._active = False
        self._shapes = set(shapes)
        self._views = set(views)
        self._lights = list(lights)
        self._transforms = list(transforms)
        self._timestamp = None
        self._elapsed = 0

    is_active = lambda self: self._active
    timestamp = lambda self: self._timestamp
    elapsed = lambda self: self._elapsed

    def set_timestamp(self, time):
        self._timestamp = time
        return self

    def set_elapsed(self, elapsed):
        self._elapsed = elapsed
        return self

    init_updatehook = lambda self: None
    head_updatehook = lambda self, seconds: None
    body_updatehook = lambda self, seconds: None
    tail_updatehook = lambda self, seconds: None

    def update(self):
        if self._active:
            self.init_updatehook()
            now = datetime.now()
            elapsed = (now - self.timestamp()).total_seconds()
            self.set_timestamp(now)
            self.set_elapsed(elapsed)

            self.head_updatehook(elapsed)
            self.update_shapes(elapsed)
            self.body_updatehook(elapsed)
            self.update_views(elapsed)
            self.tail_updatehook(elapsed)
            return self

    def update_shapes(self, seconds):
        transforms = [
            transform.update(seconds) for transform in self._transforms
            ]
        [shape.update(seconds, transforms) for shape in self._shapes]
        return self

    def update_views(self, seconds):
        faces = chain(*(shape.iterate_faces() for shape in self._shapes))
        [view.update(seconds, faces, self._lights) for view in self._views]
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

    add_light = lambda self, light: self._lights.append(light)
    remove_light = lambda self, light: self._lights.remove(light)

    add_view = lambda self, view: self._views.add(view)
    remove_view = lambda self, view: self._views.discard(view)

    add_transform = lambda self, transform: self._transforms.append(transform)
    remove_transform = lambda self, transform: self._transforms.remove(transform)
