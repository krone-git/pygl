from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class ColoredNodeType(metaclass=ABCMeta):
    pass


@dataclass
class ColorNode(ColorNodeType):
    fill: str
    outline: str
    width: int


@dataclass
class ColorNodeLine(ColorNodeType):
    outline: str
    width: int


@dataclass
class ColorNodeShape(ColorNodeType):
    fill: str
    outline: str
    width: int
