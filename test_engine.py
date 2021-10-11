

if __name__ == "__main__":
    import tkinter as tk

    from lib.obj import ObjectFileHandler, ObjectFileReader

    from lib.engine import Engine
    from lib.tk import TkinterView, TkinterShader, TkinterColor
    from lib.camera import Camera
    from lib.shape import Shape, ShapeMath
    from lib.face import Face
    from lib.line import LineFactory

    from lib.transform import Transform, TransformMatrix

    from lib.matrix import MatrixFactory, MatrixMath
    from lib.vector import VectorFactory, VectorMath, VectorUtility
    from lib.triangle import TriangleFactory, TriangleTransform

    from lib.rgba import RGBAMath, RGBAUtility

    from lib.debug import TkinterCanvasReadout, TkinterCameraDebugDisplay


    CANVAS_BG = "black"
    CUBE_COLOR = "aqua"

    CAMERA_HEIGHT = 0.5
    CAMERA_DEPTH = -50.0
    CAMERA_LATITUDE = 0.5

    HORIZONTAL_DECAY = 5
    VERTICAL_DECAY = 3

    CAMERA_MOVE_SPEED = 1
    CAMERA_ANGLE_SPEED = 1

    root = tk.Tk()
    canvas = tk.Canvas(root, bg=CANVAS_BG)
    canvas.pack(expand=True, fill=tk.BOTH)
    canvas.update()

    engine = Engine()

    camera = Camera((CAMERA_LATITUDE, CAMERA_HEIGHT, CAMERA_DEPTH), fov=90)
    shader = TkinterShader(
        fill=CUBE_COLOR,
        transparent=False,
        fade=False,
        fading_bounds=(1.0, 1.0),
        lighting_bounds=(0.1, 0.9)
        )
    view = TkinterView(canvas, camera)
    engine.add_view(view)

    light = VectorFactory.create(1.0, 1.0, 1.0)
    engine.add_light(light)

    grid_triangles = [
        *[LineFactory.from_coordinates(-5, 0, i*0.1, 5, 0, i*0.1) for i in range(-25, 25)],
        *[LineFactory.from_coordinates(i*0.1, 0, -5, i*0.1, 0, 5) for i in range(-25, 25)],
        ]
    grid = Shape.from_triangles(grid_triangles, face_kwargs={"shader": lambda *args, **kwargs: {"outline":"green"}})


    axes_path = ObjectFileHandler.source_path("unit_axes.obj")
    axes_triangles = ObjectFileReader.read_triangles(axes_path)
    axes = Shape(
        [
            Face(axes_triangles[0], shader=lambda *a, **k: {"outline":"red"}),
            Face(axes_triangles[1], shader=lambda *a, **k: {"outline":"blue"}),
            Face(axes_triangles[2], shader=lambda *a, **k: {"outline":"green"}),
            ]
        )

    shape_path = ObjectFileHandler.source_path("unit_hexahedron.obj")
    shape_triangles = ObjectFileReader.read_triangles(shape_path)
    shape = Shape.from_triangles(shape_triangles, face_kwargs={"shader": shader.callback})

    print(*shape_triangles, sep="\n")

    shapes = [
        shape,
        # grid
        # axes
        ]
    [engine.add_shape(shape) for shape in shapes]

    shape_center = shape.center()
    rotation = Transform(
        lambda seconds, elapsed: TransformMatrix.rotation(
            x=elapsed * 10, y=elapsed * 30, z=elapsed * 60,
            origin=shape_center
            )
        )
    engine.add_transform(rotation)
    VectorUtility.set(camera.location(), x=shape_center[0], y=shape_center[1])

    camera_speed = camera.linear_velocity()
    camera_speed.set_decay(
        x=HORIZONTAL_DECAY,
        y=VERTICAL_DECAY,
        z=HORIZONTAL_DECAY
        )

    camera_angle = camera.angular_velocity()
    camera_angle.set_decay(
        x=HORIZONTAL_DECAY,
        y=HORIZONTAL_DECAY,
        z=HORIZONTAL_DECAY
        )


    root.bind(
        "<Up>", lambda e: camera_speed.set(
            *VectorMath.mul_values(
                VectorMath.normalize(
                    VectorFactory.create(
                        x=camera.direction()[0],
                        z=camera.direction()[2]
                        )
                    ),
                x=CAMERA_MOVE_SPEED,
                z=CAMERA_MOVE_SPEED
                )[:3]
            )
        )
    root.bind(
        "<Down>", lambda e: camera_speed.set(
            *VectorMath.mul_values(
                camera.direction(),
                -CAMERA_MOVE_SPEED,
                0.0,
                -CAMERA_MOVE_SPEED
                )[:3]
            )
        )
    root.bind(
        "<Left>", lambda e: camera_speed.set(
            *VectorMath.mul_values(
                VectorMath.cross_product(
                    camera.direction(),
                    VectorFactory.jhat()
                    ),
                CAMERA_MOVE_SPEED,
                0.0,
                CAMERA_MOVE_SPEED
                )[:3]
            )
        )
    root.bind(
        "<Right>",
        lambda e: camera_speed.set(
            *VectorMath.mul_values(
                VectorMath.cross_product(
                    VectorFactory.jhat(),
                    camera.direction()
                    ),
                CAMERA_MOVE_SPEED,
                0.0,
                CAMERA_MOVE_SPEED
                )[:3]
            )
        )

    root.bind("<space>", lambda e: camera_speed.set(y=CAMERA_MOVE_SPEED))
    root.bind("<Control-space>", lambda e: camera_speed.set(y=-CAMERA_MOVE_SPEED))

    root.bind("<w>", lambda e: camera_angle.set(y=CAMERA_ANGLE_SPEED))
    root.bind("<s>", lambda e: camera_angle.set(y=-CAMERA_ANGLE_SPEED))
    root.bind("<a>", lambda e: camera_angle.set(x=CAMERA_ANGLE_SPEED))
    root.bind("<d>", lambda e: camera_angle.set(x=-CAMERA_ANGLE_SPEED))

    engine.start()

    debug = TkinterCanvasReadout(
        canvas,
        fill=RGBAUtility.to_hexcode(
            RGBAMath.inverse(TkinterColor.to_rgba(CANVAS_BG))
            )
        )
    debug.set_field("locX", lambda: round(camera.location()[0], 3))
    debug.set_field("locY", lambda: round(camera.location()[1], 3))
    debug.set_field("locZ", lambda: round(camera.location()[2], 3))
    debug.set_field("dirX", lambda: round(camera.direction()[0], 3))
    debug.set_field("dirY", lambda: round(camera.direction()[1], 3))
    debug.set_field("dirZ", lambda: round(camera.direction()[2], 3))
    # debug.set_field("cube center", lambda: ShapeMath.center(cube.iterate_triangles()))

    debug_frame = tk.Frame(root)
    debug_frame.pack(side=tk.RIGHT)
    # camera_debug = TkinterCameraDebugDisplay(debug_frame, camera)

    debugs = [
        debug,
        # camera_debug
        ]

    def update_loop(delay, root, function):
        def _loop(delay):
            function()
            [d.update() for d in debugs]
            root.after(delay, lambda: _loop(delay))
        return _loop(delay)

    update_loop(1, root, engine.update)
    root.mainloop()
