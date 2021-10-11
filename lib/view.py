from collections import defaultdict

from .matrix import MatrixFactory, MatrixMath, MatrixTransform
from .triangle import TriangleMath
from .vector import VectorFactory, VectorMath
from .transform import TransformMatrix


class View:
    def __init__(self, camera, dimensions=(0, 0)):
        self._dimensions = list(dimensions)
        self._distancemap = defaultdict(list)
        self._camera = camera
        # self._shader = shader
        self._active = True

    is_active = lambda self: self._active

    width = lambda self: self._dimensions[0]
    height = lambda self: self._dimensions[1]
    camera = lambda self: self._camera

    def activate(self):
        self._active = True
        return self

    def deactivate(self):
        self._active = False
        return self

    perspective_matrix = lambda self: TransformMatrix.perspective(
        self.width(),
        self.height(),
        self._camera.fov(),
        self._camera.znear(),
        self._camera.zfar(),
        )

    def camera_offset_matrix(self):
        location = self._camera.location()
        return TransformMatrix.translation(
            -location[0],
            -location[1],
            -location[2]
            )

    def camera_rotation_matrix(self):
        direction = self._camera.direction()
        location = self._camera.location()
        return MatrixMath.inverse(
            TransformMatrix.directional_rotation(
                location,
                VectorMath.add_vector(location, direction)
                )
            )

    view_scale_matrix = lambda self: TransformMatrix.scale(
        self.width(), self.height(), 1.0
        )
    view_offset_matrix = lambda self: MatrixFactory.identity()


    def render_face(self, faces, perspective, lights):
        raise NotImplementedError

    def render_faces(self, seconds, lights):
        matrices = [
            self.camera_offset_matrix(),
            # self.camera_rotation_matrix(),
            self.perspective_matrix(),
            self.view_scale_matrix(),
            self.view_offset_matrix(),
            ]
        [
            self.render_face(face, matrices, lights)
            for distance in reversed(sorted(self._distancemap))
            for face in self._distancemap[distance]
            ]
        return self

    def update_map(self, seconds, faces):
        camera = self._camera
        camera_location = camera.location()
        znear = camera.znear()
        zfar = camera.zfar()

        self._distancemap.clear()

        camera_transforms = [
            self.camera_offset_matrix(),
            ]

        for face in faces:
            triangle = face.transforms(camera_transforms)

            triangle_normal = TriangleMath.normal(triangle)
            triangle_center = TriangleMath.center(triangle)

            camera_distance = VectorMath.length(
                VectorMath.sub_vector(triangle_center, camera_location)
                )
            normal_camera_distance = (camera_distance - znear) / (zfar - znear)

            self._distancemap[normal_camera_distance].append(face)

        return self


    def update(self, seconds, faces, lights):
        self.update_map(seconds, faces)
        self.render_faces(seconds, lights)
        return self
