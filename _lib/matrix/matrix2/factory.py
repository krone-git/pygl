

class Matrix2x2Factory:
    empty = lambda: [
        [0.0, 0.0],
        [0.0, 0.0]
        ]
    identity = lambda: [
        [1.0, 0.0],
        [0.0, 1.0]
        ]
    create = identity

    copy = lambda mat: mat.copy()
    def icopy(mat, other):
        other[0][0] = mat[0][0]
        other[0][1] = mat[0][1]
        other[1][0] = mat[1][0]
        other[1][1] = mat[1][1]
        return other

create_matrix2 = create_mat2 = Matrix2x2Factory.create
empty_matrix2 = empty_mat2 = Matrix2x2Factory.empty
identity_matrix2 = id_mat2 = Matrix2x2Factory.identity

copy_matrix2 = copy_mat2 = Matrix2x2Factory.copy
icopy_matrix2 = icopy_mat2 = Matrix2x2Factory.icopy
