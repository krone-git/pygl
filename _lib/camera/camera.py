from ..vector.vector3.factory import xcopy_vec3, xicopy_vec3
from ..transform.vector3 import Vector3DTransform


class Camera:
    def __init__(self, origin=(0,0,0), direction=(0,0,0), fov=90, znear=0.1,
                    zfar=1000, transforms=()):
        self._origin = xcopy_vec3(origin)
        self._transformed = xcopy_vec3(self._origin)
        self._direction = xcopy_vec3(direction)
        self._transforms = list(transforms)
        self._fov = fov % 360
        self._znear = znear + 0.0
        self._zfar = zfar + 0.0

    origin = lambda self: self._origin
    transformed = lambda self: self._transformed
    direction = lambda self: self._direction
    fov = lambda self: self._fov
    znear = lambda self: self._znear
    zfar = lambda self: self._zfar

    add_transform = lambda self, transform: self._transforms.append(transform)
    remove_transform = lambda self, transform: self._transforms.remove(transform)

    def update(self, timedelay):
        xicopy_vec3(self._origin, self._transformed)
        matrices, depleted = set(), []
        for transform in self._transforms:
            matrix = transform(timedelay)
            if matrix is not None:
                matrices.add(matrix)
            else:
                depleted.append(transform)
        [self.remove_transform(t) for t in depleted]

        [Vector3DTransform.xitransforms(self._transformed, matrices)]
        return self
