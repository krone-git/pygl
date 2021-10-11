

if __name__ == "__main__":
    import tkinter as tk

    from _lib.engine.engine import Engine
    from _lib.view.tk import TkinterView
    from _lib.camera.camera import Camera
    from _lib.shape.shape import Shape

    from _lib.shape.shape3 import Cube3DFactory
    from _lib.transform.transform4 import Transform4D


    root = tk.Tk()
    canvas = tk.Canvas(root, bg="gray")
    canvas.pack(expand=True, fill=tk.BOTH)

    camera = Camera(origin=[0, 0, -10.0], fov=90)

    jump_tracker = dict(fallduration=0)
    def jump_transform(tracker, duration, height):
        def _transform(timedelay):
            tracker["fallduration"] += timedelay
            fallduration = tracker["fallduration"]
            if fallduration >= duration:
                tracker["fallduration"] = 0
                return None
            else:
                y = height - height * (2 * fallduration / duration - 1) ** 2
                return Transform4D.translate_mat(0.0, y, 0.0)

        return _transform

    def jump(camera, height, duration):
        if jump_tracker["fallduration"] == 0:
            camera.add_transform(jump_transform(jump_tracker, duration, height))

    walk_tracker = dict(
        forwardduration=0,
        backwardduration=0,
        leftduration=0,
        rightduration=0
        )
    def walk_transform(tracker, key, direction, speed, duration):
        def _transform(timedelay):
            tracker[key] += timedelay
            walkduration = tracker[key]
            if walkduration >= duration and jump_tracker["fallduration"] == 0:
                tracker[key] = 0
                return None
            else:
                directions = [0.0, 0.0, 0.0]
                distance = speed * timedelay
                directions[direction] = distance
                return Transform4D.translate_mat(
                    directions[0],
                    directions[1],
                    directions[2]
                    )

        return _transform

    def walk_forward(camera, speed, duration):
        if walk_tracker["forwardduration"] == 0:
            camera.add_transform(
                walk_transform(
                    walk_tracker,
                    "forwardduration",
                    2,
                    speed,
                    duration
                    )
                )
    def walk_backward(camera, speed, duration):
        if walk_tracker["backwardduration"] == 0:
            camera.add_transform(
                walk_transform(
                    walk_tracker,
                    "backwardduration",
                    2,
                    speed * -1,
                    duration
                    )
                )
    def walk_left(camera, speed, duration):
        if walk_tracker["leftduration"] == 0:
            camera.add_transform(
                walk_transform(
                    walk_tracker,
                    "leftduration",
                    0,
                    speed * -1,
                    duration
                    )
                )
    def walk_right(camera, speed, duration):
        if walk_tracker["rightduration"] == 0:
            camera.add_transform(
                walk_transform(
                    walk_tracker,
                    "rightduration",
                    0,
                    speed,
                    duration
                    )
                )


    view = TkinterView(
        canvas,
        camera=camera,
        shader=lambda *args: {"fill":"", "outline":"white"}
        )

    thetas = [0.0, 0.0, 0.0]

    def rotate_x(timedelay):
        thetas[0] = (thetas[0] + timedelay * 10) % 360
        return Transform4D.rotate_x_mat(thetas[0])

    def rotate_y(timedelay):
        thetas[1] = (thetas[1] + timedelay * 10) % 360
        return Transform4D.rotate_y_mat(thetas[1])

    def rotate_z(timedelay):
        thetas[2] = (thetas[2] + timedelay * 10) % 360
        return Transform4D.rotate_z_mat(thetas[2])

    cube = Shape.from_tris(Cube3DFactory.unit())
    # cube.add_transform(rotate_x)
    # cube.add_transform(rotate_y)
    # cube.add_transform(rotate_z)

    shapes = [
        cube,
        # cube2,
        # cube3
        ]

    engine = Engine(shapes=shapes, views=[view])
    engine.start()

    fps_tracker = dict(timedelay=0, cycles=0, text="--")
    def update_fps_tracker(timedelay):
        if fps_tracker["timedelay"] >= 1:
            fps_tracker["text"] = fps_tracker["cycles"]
            fps_tracker["timedelay"] = fps_tracker["cycles"] = 0
        else:
            fps_tracker["timedelay"] += timedelay
            fps_tracker["cycles"] += 1

    readout_text = f"%s fps\nx: %s\ny: %s\nz: %s"
    readout_tag = canvas.create_text(
        10,10, text=readout_text % (("--",) * 4), fill="white", anchor=tk.NW
        )
    def update_readout(timedelay):
        camera_location = camera.transformed()
        update_fps_tracker(timedelay)

        canvas.itemconfig(
            readout_tag,
            text=readout_text % (
                fps_tracker["text"],
                camera_location[0],
                camera_location[1],
                camera_location[2]
                )
            )

    engine.open_updatehook = update_readout


    def update_loop(delay, root, func):
        def _loop(_delay):
            func()
            root.after(_delay, lambda: _loop(delay))
        return _loop(delay)

    update_loop(1, root, engine.update)

    root.bind("<Up>", lambda e: walk_forward(camera, 1, 0.1))
    root.bind("<Down>", lambda e: walk_backward(camera, 1, 0.1))
    root.bind("<Left>", lambda e: walk_left(camera, 1, 0.1))
    root.bind("<Right>", lambda e: walk_right(camera, 1, 0.1))
    root.bind("<space>", lambda e: jump(camera, 1, 1))

    root.mainloop()
