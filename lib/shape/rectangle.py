from dataclasses import dataclass, field

from .shape import ShapeType, CompoundShapeType


@dataclass
class RoundedRectangleShape(CompoundShapeType):
    _radius: int = field(default=0, init=False)

    def __init__(self, radius=0):
        self._radius=radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        return self


@dataclass
class PillShape(CompoundShapeType):
    _radius: int = field(default=0, init=False)
    _landscape: bool = field(default=True, init=False)

    def __init__(self, radius=0, landscape=True):
        self._radius, self._landscape = radius, bool(landscape)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        return self

    @property
    def landscape(self):
        return self._landscape

    @landscape.setter
    def landscape(self, value):
        self._landscape = value
        return self
