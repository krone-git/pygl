from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .node import Node


class NodeLineType(metaclass=ABCMeta):
    pass


@dataclass
class NodeLine(NodeLineType):
    node1: Node
    node2: Node
