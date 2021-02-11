from tkinter import X as tk_X
from .shape import TkCanvasShape2D, TkCanvasCompoundShape2D
from ..shape.rectangle import RoundedRectangleShape, PillShape
from .arc import TkCanvasArc


class TkCanvasRectangle(TkCanvasShape2D):
    def draw(self):
        self._tag = self.canvas.create_rectangle(
            self.bbox(),
            fill=self.fill,
            outline=self.outline,
            width=self.border
            )


class TkCanvasRoundedRectangle(TkCanvasCompoundShape2D, RoundedRectangleShape):
    def __init__(self, canvas, *args, radius=4, **kwargs):
        TkCanvasCompoundShape2D.__init__(self, canvas, *args, **kwargs)
        RoundedRectangleShape.__init__(self, radius=radius)
        arc_size = radius * 2

        self._vertical = TkCanvasRectangle(
            self.canvas,
            self.x + self.radius,
            self.y,
            self.width - 2 * self.radius,
            self.height,
            fill=self.fill,
            outline="",
            border=self.border
            )
        self._horizontal = TkCanvasRectangle(
            self.canvas,
            self.x,
            self.y + self.radius,
            self.width,
            self.height - 2 * self.radius,
            fill=self.fill,
            outline="",
            border=self.border
            )

        self._topleft = TkCanvasArc(
            self.canvas,
            self.x,
            self.y,
            arc_size,
            arc_size,
            start=90,
            extent=90,
            fill=self.fill,
            outline="",
            border=self.border
            )
        self._topright = TkCanvasArc(
            self.canvas,
            self.x + self.width - arc_size - 1,
            self.y,
            arc_size,
            arc_size,
            start=0,
            extent=90,
            fill=self.fill,
            outline="",
            border=self.border
            )
        self._bottomleft = TkCanvasArc(
            self.canvas,
            self.x,
            self.y + self.height - arc_size - 1,
            arc_size,
            arc_size,
            start=180,
            extent=90,
            fill=self.fill,
            outline="",
            border=self.border
            )
        self._bottomright = TkCanvasArc(
            self.canvas,
            self.x + self.width - arc_size - 1,
            self.y + self.height - arc_size - 1,
            arc_size,
            arc_size,
            start=270,
            extent=90,
            fill=self.fill,
            outline="",
            border=self.border
            )

        self.shapes = [
            self._vertical,
            self._horizontal,
            self._topleft,
            self._topright,
            self._bottomleft,
            self._bottomright,
            ]

    def resize(self, width, height):
        x, y = self.radius + width, self.radius + height
        self._vertical.resize(
            width - 2 * self.radius,
            height
            )
        self._horizontal.resize(
            width,
            height - 2 * self.radius
            )

        self._topright.shift(x, self.y)
        self._bottomleft.shift(self.x, y)
        self._bottomright.shift(x, y)

        TkCanvasCompoundShape2D.resize(self, width, height)
        return self


class TkCanvasPill(TkCanvasCompoundShape2D, PillShape):
    def __init__(self, canvas, *args, radius=4, landscape=True,
                    **kwargs):
        TkCanvasCompoundShape2D.__init__(self, canvas, *args, **kwargs)
        PillShape.__init__(self, landscape=landscape, radius=radius)

        arc_size = self.radius * 2
        self._body = TkCanvasRectangle(
            self.canvas,
            self.x + (self.radius if self.landscape else 0),
            self.y + (0 if self.landscape else self.radius),
            self.width - (2 * self.radius if self.landscape else 0),
            self.height- (0 if self.landscape else 2 * self.radius),
            fill=self.fill,
            outline="",
            border=self.border
            )
        self._left = TkCanvasArc(
            self.canvas,
            self.x,
            self.y,
            arc_size if self.landscape else self.width - 1,
            self.height - 1 if self.landscape else arc_size,
            fill=self.fill,
            outline="",
            border=self.border,
            start=90 if self.landscape else 0,
            extent=180
            )
        self._right = TkCanvasArc(
            self.canvas,
            self.x + (self.width - arc_size if self.landscape else 0),
            self.y + (0 if self.landscape else self.height - arc_size),
            arc_size if self.landscape else self.width - 1,
            self.height - 1 if self.landscape else arc_size,
            fill=self.fill,
            outline="",
            border=self.border,
            start=270 if self.landscape else 180,
            extent=180
            )

        self.shapes = [
            self._body,
            self._left,
            self._right
            ]

    def resize(self, width, height):
        self._body.resize(
            width - 2 * self.radius if self.landscape else self.width,
            self.height if self.landscape else height - 2 * self.radius
            )
        self._left.resize(
            self.radius if self.landscape else width,
            height if self.landscape else self.radius
            )
        self._right.resize(
            self.radius if self.landscape else width,
            height if self.landscape else self.radius
            )

        self._right.shift(
            width - (self.radius if self.landscape else 0),
            height - (0 if self.landscape else self.radius)
            )

        TkCanvasCompoundShape2D.resize(width, height)
        return self
