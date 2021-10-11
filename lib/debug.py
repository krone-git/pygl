import tkinter as tk

from .triangle import TriangleFactory, TriangleTransform, TriangleUtility
from .transform import TransformMatrix
from .matrix import MatrixMath
from .vector import VectorFactory, VectorMath, VectorTransform


class TkinterCameraDebugDisplay(tk.Canvas):
    def __init__(self, master, camera, *args, scale=10, **kwargs):
        super().__init__(master, *args, **kwargs)
        super().pack()
        super().update()

        self._camera = camera
        self._scale = scale

        w, h = self.winfo_width(), self.winfo_height()
        self._unit_grid = {}
        for i in range(w // self._scale):
            line = (i, 0, i, h)
            self._unit_grid[self.create_line(*line, fill="black")] = line
        for i in range(h // self._scale):
            line = (0, i, w, i)
            self._unit_grid[self.create_line(*line, fill="black")] = line

        self._unit_triangle = TriangleFactory.from_coordinates(
            -0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.0, 0.0
            )
        self._triangle_tag = self.create_polygon(
            *self._unit_triangle[0:2],
            *self._unit_triangle[4:6],
            *self._unit_triangle[7:9],
            fill="red"
            )

    def update(self, *args, **kwargs):
        result = super().update()

        w, h = self.winfo_width(), self.winfo_height()
        camera = self._camera
        location = camera.location()
        direction = camera.direction()
        direction = VectorFactory.create(
            direction[0], direction[2], 0.0
            )

        for k, v in self._unit_grid.items():
            self.coords(k, *[i * self._scale for i in v])

        triangle = TriangleFactory.copy(self._unit_triangle)
        scale = TransformMatrix.scale(x=self._scale, y=-self._scale)
        offset = TransformMatrix.translation(x=w / 2, y=h / 2)
        rotation = MatrixMath.inverse(
            TransformMatrix.directional_rotation(
                VectorFactory.origin(),
                direction
                )
            )

        TriangleTransform.itransforms(
            triangle, [rotation, scale, offset]
            )
        coordinates = [
            int(v) for i, v in enumerate(TriangleUtility.unpack(triangle)) if i % 3 != 2
            ]
        print(*triangle, sep="\n", end="\n\n")
        self.coords(self._triangle_tag, *coordinates)
        self.tag_raise(self._triangle_tag)

        return result



class TkinterCanvasReadout:
    def __init__(self, tkcanvas, fields={}, coords=(10.0, 10.0), **kwargs):
        self._canvas = tkcanvas
        self._coordinates = list(coords)
        self._fields = fields.copy()

        self._configuration = kwargs.copy()
        self._configuration.setdefault("text", "")
        self._configuration.setdefault("anchor", "nw")

        self._tag = self._canvas.create_text(
            *self._coordinates, **self._configuration
            )

    def set_coordinates(self, x=None, y=None):
        if x != None:
            self._coordinates[0] = x
        if y != None:
            self._coordinates[1] = y
        return self

    def set_field(self, field, callback):
        self._fields[field] = callback
        return self

    remove_field = lambda self, field: self._fields.pop(field)

    def configure(self, **kwargs):
        self._configuration.update(kwargs)
        return self

    def update(self):
        self._configuration["text"] = "\n".join(
            str(k) + ": " + str(v()) for k, v in self._fields.items()
            )
        self._canvas.itemconfig(self._tag, **self._configuration)
        self._canvas.coords(self._tag, *self._coordinates)
        self._canvas.tag_raise(self._tag)
        return self
