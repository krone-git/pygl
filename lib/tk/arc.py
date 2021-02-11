
from .shape import TkCanvasShape2D
from..shape.arc import ArcShape


class TkCanvasArc(TkCanvasShape2D, ArcShape):
    def __init__(self, *args, start=0, extent=90, **kwargs):
        TkCanvasShape2D.__init__(self, *args, **kwargs)
        ArcShape.__init__(self, start=start, extent=extent)

    def draw(self):
        self._tag = self.canvas.create_arc(
            self.bbox(),
            start=self.start,
            extent=self.extent,
            fill=self.fill,
            outline=self.outline,
            width=self.border
            )
