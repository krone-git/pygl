from dataclasses import dataclass

from .shape import ShapeType


@dataclass
class ArcShape(ShapeType):
    start: int
    extent: int
