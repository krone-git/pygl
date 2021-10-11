from .face import Face
from .vector import VectorFactory, VectorMath
from .transform import Transform, TransformMatrix
from .velocity import Velocity, VelocityTransform


class Shape:
    def __init__(self, faces, location=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 1.0)):
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
            Transform(
                lambda seconds, elapsed: TransformMatrix.rotation(
                    self._direction[0], self._direction[1], self._direction[2]
                    )
                ),
            Transform(
                lambda seconds, elapsed: TransformMatrix.translation(
                    self._location[0], self._location[1], self._location[2]
                    )
                ),
            ]

        self._faces = set(faces)

    location = lambda self: self._location
    linear_velocity = lambda self: self._linear_velocity
    direction = lambda self: self._direction
    angular_velocity = lambda self: self._angular_velocity

    iterate_faces = lambda self: iter(self._faces)
    iterate_triangles = lambda self: (face.triangle() for face in self._faces)
    iterate_vectors = lambda self: (
        vector for face in self._faces for vector in face.triangle()
        )

    center = lambda self: ShapeMath.center(self.iterate_triangles())

    add_face = lambda self, face: self._faces.add(face)
    remove_face = lambda self, face: self._faces.discard(face)

    add_transform = lambda self, transform: self._transforms.append(transform)
    remove_transform = lambda self, transform: self._transforms.remove(transform)

    def update(self, seconds, transforms=()):
        transforms = [
            *transforms,
            *[transform.update(seconds) for transform in self._transforms]
            ]
        [face.update(transforms) for face in self._faces]
        return self

    @classmethod
    def from_triangles(cls, triangles, *args, face_args=(), face_kwargs={}, **kwargs):
        return cls(
            [Face(triangle, *face_args, **face_kwargs) for triangle in triangles],
            *args,
            **kwargs
            )


class ShapeMath:
    def center(triangles):
        center = VectorFactory.empty()
        size = 0
        for triangle in triangles:
            for vector in triangle:
                size += 1
                center[0] += vector[0]
                center[1] += vector[1]
                center[2] += vector[2]

        size = 1 if size == 0 else size
        center[0] /= size
        center[1] /= size
        center[2] /= size

        return center
