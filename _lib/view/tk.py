from .view import View
from ..transform.transform4 import Transform4D


class TkinterView(View):
    def __init__(self, tkcanvas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tkcanvas = tkcanvas
        self._facemap = dict()

    width = lambda self: self._tkcanvas.winfo_width()
    height = lambda self: self._tkcanvas.winfo_height()

    view_offset_matrix = lambda self: Transform4D.translate_mat(
        self.width() * 0.5,
        self.height() * 0.5,
        0.0
        )

    def render_face(self, face, projected):
        face_map = self._facemap
        canvas = self._tkcanvas

        x1 = projected[0][0]
        x2 = projected[1][0]
        x3 = projected[2][0]
        y1 = projected[0][1]
        y2 = projected[1][1]
        y3 = projected[2][1]

        if face not in face_map:
            face_map[face] = canvas.create_polygon(
                x1, y1, x2, y2, x3, y3,
                fill="",
                outline=""
                )

        tag = face_map[face]
        canvas.tag_raise(tag)
        canvas.itemconfig(
            tag, **self._shader(face.transformed())
            )
        canvas.coords(tag, x1, y1, x2, y2, x3, y3)
        return self
