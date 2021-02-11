from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .vertex import Vertex2D, Vertex3D
# from .edge import Edge2D, Edge3D


class FaceType(metaclass=ABCMeta):
    pass


@dataclass
class Face2D(FaceType):
    vertex: Vertex2D
    vertex: Vertex2D


@dataclass
class Face3D(FaceType):
    vertex1: Vertex3D
    vertex2: Vertex3D
    vertex3: Vertex3D

    # edge1: Edge3D
    # edge2: Edge3D
    # edge3: Edge3D
