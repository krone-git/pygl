from ..projection.factory import ProjectionMatrixFactory
from ..transform.face3 import Triangle3DTransform
from ..transform.transform4 import Transform4D
from ..matrix.matrix4.factory import id_mat4


class View:
    def  __init__(self, camera, dimensions=(0, 0), shader=None):
        self._dimensions = list(dimensions)
        self._camera = camera
        self._shader = shader
        self._active = True

    is_active = lambda self: self._active

    width = lambda self: self._dimensions[0]
    height = lambda self: self._dimensions[1]
    camera = lambda self: self._camera

    def set_height(self, height):
        self._dimensions[1] = height + 0.0
        return self

    def set_width(self, width):
        self._dimensions[0] = width + 0.0
        return self

    def set_active(self):
        self._active = True
        return self

    def set_inactive(self):
        self._active = False
        return self

    projection_matrix = lambda self: ProjectionMatrixFactory.create(
        self.width(),
        self.height(),
        self._camera.fov(),
        self._camera.znear(),
        self._camera.zfar(),
        )

    def camera_offset_matrix(self):
        camera = self._camera.transformed()
        return Transform4D.translate_mat(
            camera[0],
            camera[1] * -1,
            camera[2] * -1
            )

    view_scale_matrix = lambda self: Transform4D.scale_xyz_mat(
        self.width() * 0.5,
        self.height() * 0.5,
        1.0,
        )
    view_offset_matrix = lambda self: id_mat4()

    def render_face(self, face, projected):
        raise NotImplementedError

    def update(self, timedelay, faces):
        if self._active:
            transforms = [
                self.camera_offset_matrix(),
                self.view_scale_matrix(),
                self.projection_matrix(),
                self.view_offset_matrix()
                ]
            [
                self.render_face(
                    face,
                    Triangle3DTransform.transforms(face.transformed(), transforms)
                    ) for face in faces
                ]
        return self
