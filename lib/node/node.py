from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, replace
from typing import Any


class NodeType(metaclass=ABCMeta):
    pass


@dataclass
class Node(NodeType):
    master: Any


@dataclass
class Node2D(Node):
    x: int
    y: int


@dataclass
class Node3D(Node):
    x: int
    y: int
    z: int
