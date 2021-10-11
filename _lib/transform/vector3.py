from .transform3 import Transform3D
from ..vector.vector3.math import mul_mat_vec3, imul_mat_vec3, xmul_mat_vec3, \
                                    ximul_mat_vec3


class Vector3DTransform:
    transform = mul_mat_vec3
    def transforms(vec, mats):
        for mat in mats:
            vec = mul_mat_vec3(vec, mat)
        return vec

    itransform = imul_mat_vec3
    def itransforms(vec, mats):
        [imul_mat_vec3(vec, mat) for mat in mats]
        return vec

    xtransform = xmul_mat_vec3
    def xtransforms(vec, mats):
        for mat in mats:
            vec = xmul_mat_vec3(vec, mat)
        return vec

    xitransform = ximul_mat_vec3
    def xitransforms(vec, mats):
        [ximul_mat_vec3(vec, mat) for mat in mats]
        return vec

    scale = lambda vec, s: mul_mat_vec3(vec, Transform3D.scale_mat(s))
    scale_xyz = lambda vec, x, y, z: mul_mat_vec3(vec, Transform3D.scale_xyz_mat(x, y, z))
    scale_xy = lambda vec, x, y: mul_mat_vec3(vec, Transform3D.scale_xy_mat(x, y))
    scale_xz = lambda vec, x, z: mul_mat_vec3(vec, Transform3D.scale_xz_mat(x, z))
    scale_x = lambda vec, x: mul_mat_vec3(vec, Transform3D.scale_x_mat(x))
    scale_yz = lambda vec, y, z: mul_mat_vec3(vec, Transform3D.scale_yz_mat(y, z))
    scale_y = lambda vec, y: mul_mat_vec3(vec, Transform3D.scale_y_mat(y))
    scale_z = lambda vec, z: mul_mat_vec3(vec, Transform3D.scale_z_mat(z))

    iscale = lambda vec, s: imul_mat_vec3(vec, Transform3D.scale_mat(s))
    iscale_xyz = lambda vec, x, y, z: imul_mat_vec3(vec, Transform3D.scale_xyz_mat(x, y, z))
    iscale_xy = lambda vec, x, y: imul_mat_vec3(vec, Transform3D.scale_xy_mat(x, y))
    iscale_xz = lambda vec, x, z: imul_mat_vec3(vec, Transform3D.scale_xz_mat(x, z))
    iscale_x = lambda vec, x: imul_mat_vec3(vec, Transform3D.scale_x_mat(x))
    iscale_yz = lambda vec, y, z: imul_mat_vec3(vec, Transform3D.scale_yz_mat(y, z))
    iscale_y = lambda vec, y: imul_mat_vec3(vec, Transform3D.scale_y_mat(y))
    iscale_z = lambda vec, z: imul_mat_vec3(vec, Transform3D.scale_z_mat(z))

    rotate_x = lambda vec, deg: mul_mat_vec3(vec, Transform3D.rotate_x_mat_deg(deg))
    rotate_x_90 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_X_90_MAT)
    rotate_x_180 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_X_180_MAT)
    rotate_x_270 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_X_270_MAT)
    irotate_x = lambda vec, deg: imul_mat_vec3(vec, Transform3D.rotate_x_mat_deg(deg))
    irotate_x_90 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_X_90_MAT)
    irotate_x_180 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_X_180_MAT)
    irotate_x_270 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_X_270_MAT)

    rotate_y = lambda vec, deg: mul_mat_vec3(vec, Transform3D.rotate_y_mat_deg(deg))
    rotate_y_90 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Y_90_MAT)
    rotate_y_180 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Y_180_MAT)
    rotate_y_270 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Y_270_MAT)
    irotate_y = lambda vec, deg: imul_mat_vec3(vec, Transform3D.rotate_y_mat_deg(deg))
    irotate_y_90 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Y_90_MAT)
    irotate_y_180 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Y_180_MAT)
    irotate_y_270 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Y_270_MAT)

    rotate_z = lambda vec, deg: mul_mat_vec3(vec, Transform3D.rotate_z_mat_deg(deg))
    rotate_z_90 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Z_90_MAT)
    rotate_z_180 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Z_180_MAT)
    rotate_z_270 = lambda vec: mul_mat_vec3(vec, Transform3D.ROTATE_Z_270_MAT)
    irotate_z = lambda vec, deg: imul_mat_vec3(vec, Transform3D.rotate_z_mat_deg(deg))
    irotate_z_90 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Z_90_MAT)
    irotate_z_180 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Z_180_MAT)
    irotate_z_270 = lambda vec: imul_mat_vec3(vec, Transform3D.ROTATE_Z_270_MAT)

    reflect_x = lambda vec: mul_mat_vec3(vec, Transform3D.REFLECT_X_MATRIX)
    reflect_y = lambda vec: mul_mat_vec3(vec, Transform3D.REFLECT_Y_MATRIX)
    reflect_z = lambda vec: mul_mat_vec3(vec, Transform3D.REFLECT_Z_MATRIX)
    ireflect_x = lambda vec: imul_mat_vec3(vec, Transform3D.REFLECT_X_MATRIX)
    ireflect_y = lambda vec: imul_mat_vec3(vec, Transform3D.REFLECT_Y_MATRIX)
    ireflect_z = lambda vec: imul_mat_vec3(vec, Transform3D.REFLECT_Z_MATRIX)

    shear_x = lambda vec, y, z: mul_mat_vec3(vec, Transform3D.shear_x_mat(y, z))
    shear_y = lambda vec, x, z: mul_mat_vec3(vec, Transform3D.shear_y_mat(x, z))
    shear_z = lambda vec, x, y: mul_mat_vec3(vec, Transform3D.shear_z_mat(x, y))
    ishear_x = lambda vec, y, z: imul_mat_vec3(vec, Transform3D.shear_x_mat(y, z))
    ishear_y = lambda vec, x, z: imul_mat_vec3(vec, Transform3D.shear_y_mat(x, z))
    ishear_z = lambda vec, x, y: imul_mat_vec3(vec, Transform3D.shear_z_mat(x, y))
