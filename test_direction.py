

if __name__ == "__main__":
    import tkinter as tk

    from lib.vector import VectorFactory, VectorMath, VectorTransform
    from lib.transform import TransformMatrix
    from lib.matrix import MatrixMath


    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.pack()

    length = 30


    direction = VectorFactory.ihat()
    direction_tag = canvas.create_line(0, 0, 0, 0, fill="gray")
    arrow_tag = canvas.create_line(0, 0, 0, 0, fill="red")
    right_tag = canvas.create_line(0, 0, 0, 0, fill="blue")

    def update_loop(delay, root, function):
        def _loop(delay):
            function()
            root.after(delay, lambda: _loop(delay))
        return _loop(delay)

    def update():
        angles = VectorMath.unit_angles(direction)
        rotation = TransformMatrix.rotation(*angles)

        scale = TransformMatrix.scale(x=length, y=-length)
        offset = TransformMatrix.translation(
            x=canvas.winfo_width() / 2, y=canvas.winfo_height() / 2
            )

        origin = VectorTransform.transforms(
            VectorFactory.empty(), [rotation, scale, offset]
            )
        arrow = VectorTransform.transforms(
            VectorFactory.jhat(), [rotation, scale, offset]
            )
        print(arrow)
        right = VectorTransform.transforms(
            VectorFactory.jhat(), [rotation, scale, offset]
            )

        canvas.coords(arrow_tag, origin[0], origin[1], arrow[0], arrow[1])
        canvas.coords(right_tag, origin[0], origin[1], right[0], right[1])
        # canvas.tag_raise(right_tag)

        ghost = VectorTransform.transforms(
            direction, [scale, offset]
            )
        canvas.coords(direction_tag, origin[0], origin[1], ghost[0], ghost[1])

    def move_direction(direction, degrees):
        VectorTransform.itransform(
            direction, TransformMatrix.rotation(z=degrees)
            )

    root.bind("<Left>", lambda e: move_direction(direction, 360 / 36))
    root.bind("<Right>", lambda e: move_direction(direction, -360 / 36))

    update_loop(2, root, update)
    root.mainloop()
