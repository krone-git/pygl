from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, astuple
from math import dist, hypot, acos, atan, tan


class VectorType(metaclass=ABCMeta):
    @abstractmethod
    def copy(self):
        raise NotImplementedError

    @abstractmethod
    def to_tuple(self):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError


class UnitVectorType(metaclass=ABCMeta):
    @abstractmethod
    def magnitude(self):
        raise NotImplementedError

    @abstractmethod
    def is_unit_vector(self):
        raise NotImplementedError

    @abstractmethod
    def unit_vector(self):
        raise NotImplementedError

    @abstractmethod
    def radians(self, other):
        raise NotImplementedError

    @abstractmethod
    def dot_product(self, other):
        raise NotImplementedError


class MutableVectorType(metaclass=ABCMeta):
    def normalize(self, scale):
        return self / scale

    def scale(self, scale):
        return self * scale

    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __sub__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __mul__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __truediv__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __iadd__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __isub__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __imul__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __itruediv__(self, other):
        raise NotImplementedError


@dataclass
class BaseVector2D:
    x: float
    y: float


class Vector2D(BaseVector2D, VectorType):
    def copy(self, **kwargs):
        return replace(self, **kwargs)

    def to_tuple(self):
        return astuple(self)

    def __iter__(self):
        return iter(
            astuple(self)
            )


class UnitVector2D(UnitVectorType):
    def magnitude(self):
        return hypot(self.x, self.y)

    def is_unit_vector(self):
        return self.magnitude() == 1

    def unit_vector(self):
        m = self.magnitude()
        return self.__class__(
            self.x / m,
            self.y / m
            )

    def radians(self, other):
        return acos(
            self.dot_product(other)
            )

    def dot_product(self, other):
        return (self.x * other.x) + (self.y * other.y)


class MutableVector2D(MutableVectorType):
    def __add__(self, other):
        return self.__class__(
            self.x + other.x,
            self.y + other.y
            )

    def __sub__(self, other):
        return self.__class__(
            self.x - other.x,
            self.y - other.y
            )

    def __mul__(self, other):
        return self.__class__(
            self.x * other.x,
            self.y * other.y
            )

    def __truediv__(self, other):
        return self.__class__(
            self.x / other.x,
            self.y / other.y
            )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self


@dataclass
class BaseVector3D:
    x: float
    y: float
    z: float

class Vector3D(BaseVector3D, VectorType):
    def copy(self, **kwargs):
        return replace(self, **kwargs)

    def to_tuple(self):
        return astuple(self)

    def __iter__(self):
        return iter(
            astuple(self)
            )


class UnitVector3D(UnitVectorType):
    pass


class MutableVector3D(MutableVectorType):
    def __add__(self, other):
        return self.__class__(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )

    def __sub__(self, other):
        return self.__class__(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
            )

    def __mul__(self, other):
        return self.__class__(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
            )

    def __truediv__(self, other):
        return self.__class__(
            self.x / other.x,
            self.y / other.y,
            self.z / other.z
            )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
        return self


if __name__ == "__main__":
    class TestVector2D(Vector2D, UnitVector2D, MutableVector2D):
        pass

    v = TestVector2D(1, 2)
    v2 = TestVector2D(1, 2)
    v /= v2
    print(v)
    print(
        tuple(v)
        )
