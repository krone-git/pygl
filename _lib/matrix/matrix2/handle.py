

class Matrix2x2Handler:
    column0 = lambda mat: (
        mat[0][0],
        mat[1][0]
    )
    column1 = lambda mat: (
        mat[0][1],
        mat[1][1]
    )

    def clear(mat):
        mat[0][0] = 0.0
        mat[0][1] = 0.0
        mat[1][0] = 0.0
        mat[1][0] = 0.0
        return mat

    def to_identity(mat):
        mat[0][0] = 1.0
        mat[0][1] = 0.0
        mat[1][0] = 0.0
        mat[1][1] = 1.0
        return mat


column0_matrix2 = column0_mat2 = Matrix2x2Handler.column0
column1_matrix2 = column1_mat2 = Matrix2x2Handler.column1

clear_matrix2 = clear_mat2 = Matrix2x2Handler.clear
to_identity_matrix2 = to_id_mat2 = Matrix2x2Handler.to_identity
