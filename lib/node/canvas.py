from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any


class CanvasNodeObjectType(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        raise NotImplementedError

    @abtsractmethod
    def update(self):
        raise NotImplementedError

    @abtsractmethod
    def erase(self):
        raise NotImplementedError

    @bstractmethod
    def move_to(self, *args):
        raise NotImplementedError

    @abtsractmethod
    def move_center_to(self, *args):
        raise NotImplementedError

    @astractmethod
    def shift_to(self, *args):
        raise NotImplementedError

    @abstractmethod
    def drag_to(self, *args):
        raise NotImplementedError


@dataclass
class CanvasNode(CanvasNodeObjectType):
    canvas: Any


@dataclass
class CanvasNodeLine(CanvasNodeObjectType):
    canvas: Any


@dataclass
class CanvasNodeShape(CanvasNodeObjectType):
    canvas: Any
