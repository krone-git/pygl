

class Matrix4x4Factory:
    empty = lambda: [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0]
        ]
    identity = lambda: [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
        ]
    create = identity

    copy = lambda mat: mat.copy()
    def icopy(mat, other):
        other[0][0] = mat[0][0]
        other[0][1] = mat[0][1]
        other[0][2] = mat[0][2]
        other[0][3] = mat[0][3]
        other[1][0] = mat[1][0]
        other[1][1] = mat[1][1]
        other[1][2] = mat[1][2]
        other[1][3] = mat[1][3]
        other[2][0] = mat[2][0]
        other[2][1] = mat[2][1]
        other[2][2] = mat[2][2]
        other[2][3] = mat[2][3]
        other[3][0] = mat[3][0]
        other[3][1] = mat[3][1]
        other[3][2] = mat[3][2]
        other[3][3] = mat[3][3]
        return other


create_matrix4 = create_mat4 = Matrix4x4Factory.create
empty_matrix4 = empty_mat4 = Matrix4x4Factory.empty
identity_matrix4 = id_mat4 = Matrix4x4Factory.identity

copy_matrix4 = copy_mat4 = Matrix4x4Factory.copy
icopy_matrix4 = icopy_mat4 = Matrix4x4Factory.icopy
