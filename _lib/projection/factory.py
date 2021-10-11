from math import tan

from ..matrix.matrix4.factory import empty_mat4


class ProjectionMatrixFactory:
    def create(width, height, fov, znear, zfar):
        vscale = 1 / tan(fov * 0.01745329252 / 2)
        zscale = zfar / (zfar - znear)

        proj_mat = empty_mat4()
        proj_mat[0][0] = vscale * height / width
        proj_mat[1][1] = vscale
        proj_mat[2][2] = zscale
        proj_mat[2][3] = 1.0
        proj_mat[3][2] = zscale * znear * -1

        return proj_mat
