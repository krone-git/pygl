

if __name__ == "__main__":
    import tkinter as tk
    from itertools import cycle, chain, count
    from collections import defaultdict

    from _lib.vector.vector3.math import xmul_mat_vec3, cross_vec3, sub_vec_vec3, \
                                        dot_vec3, len_vec3, truediv_scl_vec3, \
                                        mul_scl_vec3, norm_xyz_vec3
    from _lib.vector.vector3.factory import xcreate_vec3, xcopy_vec3

    from _lib.matrix.matrix4.factory import id_mat4

    from _lib.face.face3 import Triangle3DMath, Triangle3DFactory, Rectangle3DFactory
    from _lib.shape.shape3 import Cube3DFactory

    from _lib.transform.transform4 import Transform4D
    from _lib.transform.vector3 import Vector3DTransform
    from _lib.transform.face3 import Triangle3DTransform
    from _lib.transform.shape3 import Shape3DTransform

    from _lib.projection.factory import ProjectionMatrixFactory

    from _lib.color.rgb import RGBHexString


    plane_colors = ["red", "green", "blue", "purple", "orange", "gray"]

    draw_tri = lambda canvas, tri, **kwargs: canvas.create_polygon(
        *tri[0][:2], *tri[1][:2], *tri[2][:2], **kwargs
        )
    def redraw_tri(canvas, tag, tri, **kwargs):
        canvas.tag_raise(tag)
        canvas.coords(tag, *tri[0][:2], *tri[1][:2], *tri[2][:2])
        canvas.itemconfig(tag, **kwargs)

    draw_shape_map = lambda canvas, shape, **kwargs: {
        draw_tri(canvas, t, **kwargs): t for i, t in enumerate(shape)
        }

    update_shapemap = lambda shape_map, trans_mats: {
        k: Triangle3DTransform.transforms(v, trans_mats)
        for k, v in shape_map.items()
        }

    def update_view(canvas, camera, light, shape_map, **kwargs):
        offset_camera = Transform4D.translate_mat(
            camera[1][0], camera[1][1] * -1, camera[1][2] * -1
            )
        projection_mat = ProjectionMatrixFactory.create(
            canvas.winfo_width(),
            canvas.winfo_height(),
            90,
            0.1,
            1000
            )
        center_mat = Transform4D.translate_mat(
            canvas.winfo_width() * 0.5,
            canvas.winfo_height() * 0.5,
            0.0
            )
        tri_map, visible, brightness = {}, {}, {}
        distance_map = defaultdict(list)
        for k, v in shape_map.items():
            tri = Triangle3DTransform.transform(v, offset_camera)
            tri_center = Triangle3DMath.center(tri)
            dist_vec = sub_vec_vec3(tri_center, camera[1])
            dist_len = len_vec3(dist_vec)
            distance_map[dist_len].append(k)

            norm = Triangle3DMath.normal(tri)
            visible[k] = dot_vec3(norm, sub_vec_vec3(tri[0], camera[0])) < 0 \
                and tri_center[2] > camera[1][2]

            brightness[k] = (dot_vec3(norm, light) + 1) * 127

            tri_map[k] = Triangle3DTransform.transforms(
                tri, [projection_mat, center_mat]
                )

        for k in reversed(sorted(distance_map)):
            for t in distance_map[k]:
                fill = outline = RGBHexString.from_rgb(
                    brightness[t], brightness[t], brightness[t]
                    ) if visible[t] else ""

                redraw_tri(
                    canvas, t, tri_map[t], fill=fill, outline=outline, **kwargs
                    )

    def update_loop(delay, canvas, camera, light, shape_maps, transform_callbacks, repeat=None):
        def _loop(n):
            trans_mats = [c() for c in transform_callbacks]
            print(trans_mats)
            maps = {}
            [maps.update(update_shapemap(map, trans_mats)) for map in shape_maps]
            update_view(canvas, camera, light, maps)
            if n is None or n > 0:
                canvas.after(delay, lambda: _loop(n if n is None else n-1))
        _loop(repeat)

    root = tk.Tk()
    canvas = tk.Canvas(root, bg="light blue")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.update()

    canvas_height = canvas.winfo_height()
    canvas_width = canvas.winfo_width()


    shapes = [
        Cube3DFactory.unit(),
        # Shape3DTransform.transform(
        #     Cube3DFactory.unit(),
        #     Transform4D.translate_mat(0, 1.1, 0)
        #     ),
        # Shape3DTransform.transform(
        #     Cube3DFactory.unit(),
        #     Transform4D.translate_mat(1.1, 0.0, 0)
        #     ),
        # Shape3DTransform.transform(
        #     Cube3DFactory.unit(),
        #     Transform4D.translate_mat(1.1, 1.1, 0)
        #     ),
        ]

    shape_maps = [draw_shape_map(canvas, shape) for shape in shapes]

    camera = [
        xcreate_vec3(0.0, 0.0, 0.0),
        xcreate_vec3(0.0, 0.3, -3.0)
        ]
    light = xcopy_vec3(norm_xyz_vec3(-1.0, 0.0, 0.0))

    theta_x = cycle(range(0, 360, 10))
    theta_y = cycle(range(0, 360, 1))
    theta_z = cycle(range(0, 360, 5))

    zoom = cycle(chain(range(1, 50), range(-50, -1)))
    loop_tracker = count()

    def engine_loop():
        loop_num = next(loop_tracker)
        return id_mat4()

    def move_camera(camera, x, y, z):
        camera[1][0] += x
        camera[1][1] += y
        camera[1][2] += z

    transform_callbacks = [
        lambda: engine_loop(),
        lambda: Transform4D.scale_xyz_mat(
            canvas.winfo_width() * 0.05, canvas.winfo_height() * 0.05, 1
            ),
        ]

    root.bind("<Up>", lambda e: move_camera(camera, 0, 0, 0.1))
    root.bind("<Down>", lambda e: move_camera(camera, 0, 0, -0.1))
    root.bind("<Left>", lambda e: move_camera(camera, -1, 0, 0))
    root.bind("<Right>", lambda e: move_camera(camera, 1, 0, 0))

    update_loop(100, canvas, camera, light, shape_maps, transform_callbacks)

    root.mainloop()
