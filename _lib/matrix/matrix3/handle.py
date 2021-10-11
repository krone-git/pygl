

class Matrix3x3Handler:
    column0 = lambda mat: (
        mat[0][0],
        mat[1][0],
        mat[2][0]
    )
    column1 = lambda mat: (
        mat[0][1],
        mat[1][1],
        mat[2][1]
    )
    column2 = lambda mat: (
        mat[0][2],
        mat[1][2],
        mat[2][2]
    )

    def clear(mat):
        mat[0][0] = 0.0
        mat[0][1] = 0.0
        mat[0][2] = 0.0
        mat[1][0] = 0.0
        mat[1][1] = 0.0
        mat[1][2] = 0.0
        mat[2][0] = 0.0
        mat[2][1] = 0.0
        mat[2][2] = 0.0
        return mat

    def to_identity(mat):
        mat[0][0] = 1.0
        mat[0][1] = 0.0
        mat[0][2] = 0.0
        mat[1][0] = 0.0
        mat[1][1] = 1.0
        mat[1][2] = 0.0
        mat[2][0] = 0.0
        mat[2][1] = 0.0
        mat[2][2] = 1.0
        return mat


column0_matrix3 = column0_mat3 = Matrix3x3Handler.column0
column1_matrix3 = column1_mat3 = Matrix3x3Handler.column1
column2_matrix3 = column2_mat3 = Matrix3x3Handler.column2

clear_matrix3 = clear_mat3 = Matrix3x3Handler.clear
to_identity_matrix3 = to_id_mat3 = Matrix3x3Handler.to_identity
