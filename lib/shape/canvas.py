from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any


class CanvasShapeType(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def erase(self):
        raise NotImplementedError


@dataclass
class CanvasShape:
    canvas: Any


class CanvasShape2D(CanvasShape, CanvasShapeType):
    pass
