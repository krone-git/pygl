from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

from .vertex import Vertex2D, Vertex3D


class EdgeType(metaclass=ABCMeta):
    pass


@dataclass
class Edge2D(EdgeType):
    vertex1: Vertex2D
    vertex2: Vertex2D


@dataclass
class Edge3D(EdgeType):
    vertex1: Vertex3D
    vertex2: Vertex3D
