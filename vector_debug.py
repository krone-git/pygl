import tkinter as tk

from lib.vector import VectorFactory, VectorMath, VectorTransform, VectorUtility
from lib.matrix import MatrixMath
from lib.transform import Transform, TransformMatrix

from lib.obj import ObjectFileReader, ObjectFileHandler

from lib.engine import Engine
from lib.camera import Camera
from lib.tk import TkinterView
from lib.line import LineFactory
from lib.face import Face
from lib.shape import Shape

from lib.debug import TkinterCanvasReadout


root = tk.Tk()
canvas = tk.Canvas(root, bg="black")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.update()


engine = Engine()

camera = Camera(location=(0.2,0.1,-20.0))
view = TkinterView(canvas, camera)
engine.add_view(view)

axes = ObjectFileReader.read_triangles(
    ObjectFileHandler.source_path("unit_axes.obj")
    )
axes = Shape([
    Face(axes[0], shader=lambda *args, **kwargs:{"outline": "red"}),
    Face(axes[1], shader=lambda *args, **kwargs:{"outline": "blue"}),
    Face(axes[2], shader=lambda *args, **kwargs:{"outline": "green"})
    ])
engine.add_shape(axes)
engine.add_transform(
    Transform(lambda *args, **kwargs: TransformMatrix.rotation(x=-12, y=22, z=-1))
    )

direction_line = LineFactory.from_vector(VectorFactory.random())
direction_shape = Shape.from_triangles(
    [direction_line],
    face_kwargs=dict(shader=lambda *args, **kwargs: {"outline":"purple"})
    )
ghost_shape = Shape.from_triangles(
    [direction_line],
    face_kwargs=dict(shader=lambda *args, **kwargs: {"outline":"gray"})
    )
target_shape = Shape.from_triangles(
    [LineFactory.from_vector(VectorFactory.random())],
    face_kwargs=dict(shader=lambda *args, **kwargs: {"outline":"orange"})
    )

engine.add_shape(direction_shape)
engine.add_shape(ghost_shape)
engine.add_shape(target_shape)

def update_loop(delay, root, function):
    def _loop(delay):
        function()
        root.after(delay, lambda: _loop(delay))
    return _loop(delay)

direction = list(direction_shape.iterate_faces())[0].triangle()[1]
_direction = list(direction_shape.iterate_faces())[0].triangle()[2]
target = list(target_shape.iterate_faces())[0].triangle()[1]

direction_transform = [0.0] * 3
direction_shape.add_transform(
    Transform(lambda *args, **kwargs: TransformMatrix.rotation(*direction_transform))
    )
direction_shape.add_transform(
    Transform(lambda *args, **kwargs: TransformMatrix.rotation(*direction_transform))
    )

def set_direction(axis, value):
    direction_transform[axis] = value



scale_frame = tk.Frame(root)
scale_frame.pack(side=tk.RIGHT)
scale_x = tk.Scale(scale_frame, to=360, command=lambda e: set_direction(0, float(e)))
scale_y = tk.Scale(scale_frame, to=360, command=lambda e: set_direction(1, float(e)))
scale_z = tk.Scale(scale_frame, to=360, command=lambda e: set_direction(2, float(e)))

scale_x.pack(side=tk.LEFT)
scale_y.pack(side=tk.LEFT)
scale_z.pack(side=tk.LEFT)

debug = TkinterCanvasReadout(canvas, fill="white")
debug.set_field("direction x", lambda: round(direction[0], 3))
debug.set_field("direction y", lambda: round(direction[1], 3))
debug.set_field("direction z", lambda: round(direction[2], 3))
debug.set_field("target x", lambda: round(target[0], 3))
debug.set_field("target y", lambda: round(target[1], 3))
debug.set_field("target z", lambda: round(target[2], 3))

def update(*args, **kwargs):
    engine.update(*args, **kwargs)
    # print(direction)


engine.start()
update_loop(2, root, update)

root.mainloop()
