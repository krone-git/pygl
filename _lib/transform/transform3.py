from math import cos, sin


class Transform3D:
    ROTATE_X_90_MAT = (
        (1.0, 0.0, 0.0),
        (0.0, 0.0, -1.0),
        (0.0, 1.0, 0.0)
        )
    ROTATE_X_180_MAT = (
        (1.0, 0.0, 0.0),
        (0.0, -1.0, 0.0),
        (0.0, 0.0, -1.0)
        )
    ROTATE_X_270_MAT = (
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0),
        (0.0, -1.0, 0.0)
        )
    ROTATE_Y_90_MAT = (
        (0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0),
        (-1.0, 0.0, 0.0)
        )
    ROTATE_Y_180_MAT = (
        (-1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, -1.0)
        )
    ROTATE_Y_270_MAT = (
        (0.0, 0.0, 1.0),
        (0.0, 1.0, 0.0),
        (-1.0, 0.0, 0.0)
        )
    ROTATE_Z_90_MAT = (
        (0.0, -1.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0)
        )
    ROTATE_Z_180_MAT = (
        (-1.0, 0.0, 0.0),
        (0.0, -1.0, 0.0),
        (0.0, 0.0, 1.0)
        )
    ROTTATE_Z_270_MAT = (
        (0.0, 1.0, 0.0),
        (-1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0)
        )

    REFLECT_X_MATRIX = (
        (-1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0)
        )
    REFLECT_Y_MATRIX = (
        (1.0, 0.0, 0.0),
        (0.0, -1.0, 0.0),
        (0.0, 0.0, 1.0)
        )
    REFLECT_Z_MATRIX = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, -1.0)
        )

    scale_mat = lambda s: (
        (s, 0.0, 0.0),
        (0.0, s, 0.0),
        (0.0, 0.0, s)
        )
    scale_xyz_mat = lambda x, y, z: (
        (x, 0.0, 0.0),
        (0.0, y, 0.0),
        (0.0, 0.0, z)
        )
    scale_xy_mat = lambda x, y: (
        (x, 0.0, 0.0),
        (0.0, y, 0.0),
        (0.0, 0.0, 1.0)
        )
    scale_xz_mat = lambda x, z: (
        (x, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, z)
        )
    scale_x_mat = lambda x: (
        (x, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0)
        )
    scale_yz_mat = lambda y, z: (
        (1.0, 0.0, 0.0),
        (0.0, y, 0.0),
        (0.0, 0.0, z)
        )
    scale_y_mat = lambda y: (
        (1.0, 0.0, 0.0),
        (0.0, y, 0.0),
        (0.0, 0.0, 1.0)
        )
    scale_z_mat = lambda z: (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, z)
        )

    rotate_x_mat_rad = lambda rad: (
        (1.0, 0.0, 0.0),
        (0.0, cos(rad), -sin(rad)),
        (0.0, sin(rad), cos(rad))
        )
    def rotate_x_mat_deg(deg):
        rad = deg * 0.01745329252
        return (
            (1.0, 0.0, 0.0),
            (0.0, cos(rad), -sin(rad)),
            (0.0, sin(rad), cos(rad))
            )
    rotate_x_mat = rotate_x_mat_deg

    rotate_y_mat_rad = lambda rad: (
        (cos(rad), 0.0, sin(rad)),
        (0.0, 1, 0.0),
        (-sin(rad), 0.0, cos(rad))
        )
    def rotate_y_mat_deg(deg):
        rad = deg * 0.01745329252
        return (
            (cos(rad), 0.0, sin(rad)),
            (0.0, 1, 0.0),
            (-sin(rad), 0.0, cos(rad))
            )
    rotate_y_mat = rotate_y_mat_deg

    rotate_z_mat_rad = lambda rad: (
        (cos(rad), -sin(rad), 0.0),
        (sin(rad), cos(rad), 0.0),
        (0.0, 0.0, 1.0)
        )
    def rotate_z_mat_deg(deg):
        rad = deg * 0.01745329252
        return (
            (cos(rad), -sin(rad), 0.0),
            (sin(rad), cos(rad), 0.0),
            (0.0, 0.0, 1.0)
            )
    rotate_z_mat = rotate_z_mat_deg

    shear_x_mat = lambda y, z: (
        (1.0, 0.0, 0.0),
        (y, 1.0, 0.0),
        (z, 0.0, 1.0)
        )
    shear_y_mat = lambda x, z: (
        (1.0, x, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, z, 1.0)
        )
    shear_z_mat = lambda x, y: (
        (1.0, 0.0, x),
        (0.0, 1.0, y),
        (0.0, 0.0, 1.0)
        )