

class Matrix3x3Factory:
    empty = lambda: [
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0]
        ]
    identity = lambda: [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
        ]
    create = empty

    copy = lambda mat: mat.copy()
    def icopy(mat, other):
        other[0][0] = mat[0][0]
        other[0][1] = mat[0][1]
        other[0][2] = mat[0][2]
        other[1][0] = mat[1][0]
        other[1][1] = mat[1][1]
        other[1][2] = mat[1][2]
        other[2][0] = mat[2][0]
        other[2][1] = mat[2][1]
        other[2][2] = mat[2][2]
        return other


create_matrix3 = create_mat3 = Matrix3x3Factory.create
empty_matrix3 = empty_mat3 = Matrix3x3Factory.empty
identity_matrix3 = id_mat3 = Matrix3x3Factory.identity

copy_matrix3 = copy_mat3 = Matrix3x3Factory.copy
icopy_matrix3 = icopy_mat3 = Matrix3x3Factory.icopy
