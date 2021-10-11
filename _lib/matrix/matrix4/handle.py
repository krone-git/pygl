

class Matrix4x4Handler:
    column0 = lambda matrix: (
        matrix[0][0],
        matrix[1][0],
        matrix[2][0],
        matrix[3][0]
    )
    column1 = lambda matrix: (
        matrix[0][1],
        matrix[1][1],
        matrix[2][1],
        matrix[3][1]
    )
    column2 = lambda matrix: (
        matrix[0][2],
        matrix[1][2],
        matrix[2][2],
        matrix[3][2]
    )
    column3 = lambda matrix: (
        matrix[0][3],
        matrix[1][3],
        matrix[2][3],
        matrix[3][3]
    )

    def clear(mat):
        mat[0][0] = 0.0
        mat[0][1] = 0.0
        mat[0][2] = 0.0
        mat[0][3] = 0.0
        mat[1][0] = 0.0
        mat[1][1] = 0.0
        mat[1][2] = 0.0
        mat[1][3] = 0.0
        mat[2][0] = 0.0
        mat[2][1] = 0.0
        mat[2][2] = 0.0
        mat[2][3] = 0.0
        mat[3][0] = 0.0
        mat[3][1] = 0.0
        mat[3][2] = 0.0
        mat[3][3] = 0.0
        return mat

    def to_identity(mat):
        mat[0][0] = 1.0
        mat[0][1] = 0.0
        mat[0][2] = 0.0
        mat[0][3] = 0.0
        mat[1][0] = 0.0
        mat[1][1] = 1.0
        mat[1][2] = 0.0
        mat[1][3] = 0.0
        mat[2][0] = 0.0
        mat[2][1] = 0.0
        mat[2][2] = 1.0
        mat[2][3] = 0.0
        mat[3][0] = 0.0
        mat[3][1] = 0.0
        mat[3][2] = 0.0
        mat[3][3] = 1.0
        return mat


column0_matrix4 = column4_mat0 = Matrix4x4Handler.column0
column1_matrix4 = column1_mat4 = Matrix4x4Handler.column1
column2_matrix4 = column2_mat4 = Matrix4x4Handler.column2
column3_matrix4 = column3_mat4 = Matrix4x4Handler.column3

clear_matrix4 = clear_mat4 = Matrix4x4Handler.clear
to_identity_matrix4 = to_id_mat4 = Matrix4x4Handler.to_identity
