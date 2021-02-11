from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

from ..shape.shape import MutableShape2D, MutableCompoundShape2D
from ..shape.canvas import CanvasShape2D
from ..shape.color import ColoredShape


@dataclass
class TkCanvasShapeType(metaclass=ABCMeta):
    _tag: str = field(init=False)


class TkCanvasShape2D(MutableShape2D, CanvasShape2D, ColoredShape, TkCanvasShapeType):
    def __init__(self, canvas, x, y, width, height, *, fill=None, outline=None,
                    border=None, bd=1):
        MutableShape2D.__init__(self, x, y, width, height)
        CanvasShape2D.__init__(self, canvas)
        ColoredShape.__init__(
            self,
            fill=fill,
            outline=outline,
            border=border if border is not None else bd
            )

    def move_to(self, x, y):
        MutableShape2D.move_to(self, x, y)
        self.update()
        return self

    def erase(self):
        pass

    def update(self):
        self.canvas.coords(self._tag, self.bbox())
        return self


class TkCanvasCompoundShape2D(MutableCompoundShape2D, CanvasShape2D,
                                ColoredShape, TkCanvasShapeType):
    def __init__(self, canvas, x, y, width, height, *, fill=None, outline=None,
                    border=None, bd=1):
        MutableCompoundShape2D.__init__(self, x, y, width, height)
        CanvasShape2D.__init__(self, canvas)
        ColoredShape.__init__(
            self,
            fill=fill,
            outline=outline,
            border=border if border is not None else bd
            )

    def draw(self):
        for s in self.shapes:
            s.draw()
        return self

    def erase(self):
        for s in self.shapes:
            s.erase()
        return self

    def update(self):
        for s in self.shapes:
            s.update()
        return self

    def move_to(self, x, y):
        offsetx, offsety = x - self.x, y - self.y
        MutableCompoundShape2D.move_to(self, x, y)
        for s in self.shapes:
            s.shift(offsetx, offsety)
        return self

    def scale(self, scalex, scaley):
        x, y = self.x, self.y
        for s in self.shapes:
            s.scale(scalex, scaley)
            s.move_to(
                x + (s.x - x) * scalex,
                y + (s.y - y) * scaley
                )
        MutableCompoundShape2D.scale(self, scalex, scaley)
        return self
