from .vector import VectorFactory, VectorTransform
from .triangle import TriangleFactory, TriangleMath, TriangleTransform


class Face:
    def __init__(self, triangle=(), shader=None):
        triangle = TriangleFactory.unit() if not triangle \
            else TriangleFactory.from_line(triangle) if len(triangle) == 2 \
            else TriangleFactory.copy(triangle)

        self._unit = TriangleFactory.copy(triangle)
        self._triangle = triangle
        self._shader = shader

    unit = lambda self: self._unit
    triangle = lambda self: self._triangle
    shader = lambda self: self._shader

    unpack = lambda self: TriangleUtility.unpack(self._triangle)

    center = lambda self: TriangleMath.center(self._triangle)
    normal = lambda self: TriangleMath.normal(self._triangle)

    def invert_normal(self):
        TriangleTransform.invert_normal(self._unit)
        TriangleTransform.invert_normal(self._triangle)
        return self

    transform = lambda self, transform: TriangleTransform.transform(self._triangle, transform)
    transforms = lambda self, transforms: TriangleTransform.transforms(self._triangle, transforms)
    def itransform(self, transform):
        TriangleTransform.itransform(self._triangle, transform)
        return self
    def itransforms(self, transforms):
        TriangleTransform.itransforms(self._triangle, transforms)
        return self

    def update(self, transforms):
        TriangleFactory.icopy(self._unit, self._triangle)
        TriangleTransform.itransforms(self._triangle, transforms)
        return self

    def copy(self):
        face = self.__class__(
            TriangleFactory.copy(self._unit),
            shader=self._shader
            )
        face._triangle = TriangleFactory.copy(self._triangle)
        return face

    @classmethod
    def from_vectors(cls, vector1, vector2, vector3, *args, **kwargs):
        triangle = TriangleFactory.create(vector1, vector2, vector3)
        return cls(triangle, *args, **kwargs)

    @classmethod
    def from_vector_references(cls, vector1, vector2, vector3, *args, **kwargs):
        triangle = TriangleFactory.from_vector_references(vector1, vector2, vector3)
        return cls(triangle, *args, **kwargs)

    @classmethod
    def from_coordinates(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3, *args, **kwargs):
        triangle = TriangleFactory.from_coordinates(
            x1, y1, z1, x2, y2, z2, x3, y3, z3
            )
        return cls(triangle, *args, **kwargs)
