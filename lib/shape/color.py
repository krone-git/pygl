from dataclasses import dataclass, field


@dataclass
class ColoredShape:
    _fill: str = field(default="", init=False)
    _outline: str = field(default="", init=False)
    _border: int = field(default=1, init=False)

    def __init__(self, *, fill="", outline="", border=1):
        self._fill, self._outline, self._border = fill, outline, border

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = value
        return self

    @property
    def outline(self):
        return self._outline

    @outline.setter
    def outline(self, value):
        self._outline = value
        return self

    @property
    def border(self):
        return self._border

    @border.setter
    def border(self, value):
        self._border = value
        return self
