from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .vertex import Vertex3D


class ViewType(metaclass=ABCMeta):
    pass


@dataclass
class View3D(ViewType):
    origin: Vertex3D
    fov: float
    near: float
    far: float
