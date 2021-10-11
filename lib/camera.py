from .vector import VectorFactory, VectorMath, VectorTransform
from .matrix import MatrixMath
from .transform import Transform, TransformMatrix
from .velocity import Velocity, VelocityTransform


class Camera:
    def __init__(self, location=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 1.0),
                    fov=90, znear=0.1, zfar=1000):
        self._location = VectorFactory.from_vector(location)
        self._linear_velocity = Velocity()

        self._direction = VectorMath.normalize(
            VectorFactory.from_vector(direction)
            )
        self._angular_velocity = Velocity(
            transform_matrix=TransformMatrix.rotation
            )

        self._transforms = [
            Transform(
                lambda seconds, elapsed: VelocityTransform.itransform_vector(
                    self._location, self._linear_velocity, seconds, elapsed
                    )
                ),
            Transform(
                lambda seconds, elapsed: VelocityTransform.itransform_vector(
                    self._direction, self._angular_velocity, seconds, elapsed
                    )
                ),
            ]

        self._fov = fov % 360
        self._znear = znear / 1
        self._zfar = zfar / 1

    location = lambda self: self._location
    linear_velocity = lambda self: self._linear_velocity
    direction = lambda self: self._direction
    angular_velocity = lambda self: self._angular_velocity

    fov = lambda self: self._fov
    znear = lambda self: self._znear
    zfar = lambda self: self._zfar

    add_transform = lambda self, transform: self._transforms.append(transform)
    remove_transform = lambda self, transform: self._transforms.remove(transform)

    def update(self, seconds, transforms=()):
        direction = self._direction
        VectorTransform.itransforms(self._location, transforms)
        VectorTransform.itransforms(direction, transforms)
        VectorMath.inormalize(direction)

        [transform.update(seconds) for transform in self._transforms]
        return self
