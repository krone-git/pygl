from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

from .face import Face2D, Face3D


class MeshType(metaclass=ABCMeta):
    pass


@dataclass
class Mesh2D(MeshType):
    faces: list[Face2D]


@dataclass
class Mesh3D(MeshType):
    faces: list[Face3D] = field(default_factory=list)
