from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class ShapeType(metaclass=ABCMeta):
    @abstractmethod
    def bbox(self):
        raise NotImplementedError

    @abstractmethod
    def center(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_bbox(cls, *args):
        raise NotImplementedError


class MutableShapeType(metaclass=ABCMeta):
    @abstractmethod
    def resize(self, *args):
        raise NotImplementedError

    @abstractmethod
    def scale(self, *args):
        raise NotImplementedError

    @abstractmethod
    def move_to(self, *args):
        raise NotImplementedError

    @abstractmethod
    def move_center_to(self, *args):
        raise NotImplementedError

    @abstractmethod
    def shift(self, *args):
        raise NotImplementedError

    @abstractmethod
    def drag_to(self, *args):
        raise NotImplementedError


@dataclass
class CompoundShapeType(ShapeType):
    shapes: list[ShapeType] = field(init=False, default_factory=list)


@dataclass
class Shape2D(ShapeType):
    _x: int
    _y: int

    _width: int
    _height: int

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        return self

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        return self

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        return self

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        return self

    def bbox(self):
        return (
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height
            )

    def center(self):
        return (
            self.x + self.width // 2,
            self.y + self.height // 2
            )

    @classmethod
    def from_bbox(cls, x1, y1, x2, y2, *args, **kwargs):
        return cls(
            *args,
            _x=min(x1, x2),
            _y=min(y1, y2),
            _width=abs(x2 - x1),
            _height=abs(y2 - y1),
            **kwargs
            )


class MutableShape2D(Shape2D, MutableShapeType):
    @abstractmethod
    def move_to(self, x, y):
        self._x, self._y = x, y
        return self

    def move_center_to(self, x, y):
        self.move_to(
            x - self.width // 2,
            y - self.height // 2
            )
        return self

    def shift(self, offsetx, offsety):
        self.move_to(
            self.x + offsetx,
            self.y + offsety
            )
        return self

    def drag_to(self, startx, starty, stopx, stopy):
        self.move_to(
            stopx,
            stopy
            )
        return self

    def resize(self, width, height):
        self._width, self._height = width, height
        return self

    def scale(self, scalex, scaley):
        self._width *= scalex
        self._height *= scaley
        return self


class CompoundShape2D(Shape2D, CompoundShapeType):
    pass


class MutableCompoundShape2D(CompoundShape2D, MutableShapeType):
    @abstractmethod
    def move_to(self, x, y):
        self.x, self.y = x, y
        return self

    def move_center_to(self, x, y):
        self.move_to(
            x - self.width // 2,
            y - self.height // 2
            )
        return self

    def shift(self, offsetx, offsety):
        self.move_to(
            self.x + offsetx,
            self.y + offsety
            )
        return self

    def drag_to(self, startx, starty, stopx, stopy):
        self.move_to(
            stopx,
            stopy
            )
        return self

    @abstractmethod
    def resize(self, width, height):
        self._width, self._height = width, height
        return self

    @abstractmethod
    def scale(self, scalex, scaley):
        self._width *= scalex
        self._height *= scaley
        return self


@dataclass
class Shape3D(ShapeType):
    _x: int
    _y: int
    _z: int

    _width: int
    _height: int
    _depth: int

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        return self

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        return self

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        return self

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        return self

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        return self

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
        return self


class MutableShape3D(Shape3D, MutableShapeType):
    pass


class CompoundShape3D(Shape3D, CompoundShapeType):
    pass


class MutableCompoundShape3D(CompoundShape3D, MutableShapeType):
    pass
