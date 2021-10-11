from .factory import identity_matrix2, copy_matrix2


class Matrix2x2ScalarMath:
    add = lambda mat, scalar: (
        (mat[0][0] + scalar, mat[0][1] + scalar),
        (mat[1][0] + scalar, mat[1][1] + scalar)
        )
    sub = lambda mat, scalar: (
        (mat[0][0] - scalar, mat[0][1] - scalar),
        (mat[1][0] - scalar, mat[1][1] - scalar)
        )
    mul = lambda mat, scalar: (
        (mat[0][0] * scalar, mat[0][1] * scalar),
        (mat[1][0] * scalar, mat[1][1] * scalar)
        )
    truediv = lambda mat, scalar: (
        (mat[0][0] / scalar, mat[0][1] / scalar),
        (mat[1][0] / scalar, mat[1][1] / scalar)
        )
    floordiv = lambda mat, scalar: (
        (mat[0][0] // scalar, mat[0][1] // scalar),
        (mat[1][0] // scalar, mat[1][1] // scalar)
        )
    mod = lambda mat, scalar: (
        (mat[0][0] % scalar, mat[0][1] % scalar),
        (mat[1][0] % scalar, mat[1][1] % scalar)
        )
    pow = lambda mat, scalar: (
        (mat[0][0] ** scalar, mat[0][1] ** scalar),
        (mat[1][0] ** scalar, mat[1][1] ** scalar)
        )

    def iadd(mat, scalar):
        mat[0][0] += scalar
        mat[0][1] += scalar
        mat[1][0] += scalar
        mat[1][1] += scalar
        return mat

    def isub(mat, scalar):
        mat[0][0] -= scalar
        mat[0][1] -= scalar
        mat[1][0] -= scalar
        mat[1][1] -= scalar
        return mat

    def imul(mat, scalar):
        mat[0][0] *= scalar
        mat[0][1] *= scalar
        mat[1][0] *= scalar
        mat[1][1] *= scalar
        return mat

    def itruediv(mat, scalar):
        mat[0][0] /= scalar
        mat[0][1] /= scalar
        mat[1][0] /= scalar
        mat[1][1] /= scalar
        return mat

    def ifloordiv(mat, scalar):
        mat[0][0] //= scalar
        mat[0][1] //= scalar
        mat[1][0] //= scalar
        mat[1][1] //= scalar
        return mat

    def imod(mat, scalar):
        mat[0][0] %= scalar
        mat[0][1] %= scalar
        mat[1][0] %= scalar
        mat[1][1] %= scalar
        return mat

    def ipow(mat, scalar):
        mat[0][0] **= scalar
        mat[0][1] **= scalar
        mat[1][0] **= scalar
        mat[1][1] **= scalar
        return mat


add_scalar_matrix2 = add_s_mat2 = Matrix2x2ScalarMath.add
sub_scalar_matrix2 = sub_s_mat2 = Matrix2x2ScalarMath.sub
mul_scalar_matrix2 = mul_s_mat2 = Matrix2x2ScalarMath.mul
truediv_scalar_matrix2 = truediv_s_mat2 = Matrix2x2ScalarMath.truediv
floordiv_scalar_matrix2 = floordiv_s_mat2 = Matrix2x2ScalarMath.floordiv
mod_scalar_matrix2 = mod_s_mat2 = Matrix2x2ScalarMath.mod
pow_scalar_matrix2 = pow_s_mat2 = Matrix2x2ScalarMath.pow

iadd_scalar_matrix2 = iadd_s_mat2 = Matrix2x2ScalarMath.iadd
isub_scalar_matrix2 = isub_s_mat2 = Matrix2x2ScalarMath.isub
imul_scalar_matrix2 = imul_s_mat2 = Matrix2x2ScalarMath.imul
itruediv_scalar_matrix2 = itruediv_s_mat2 = Matrix2x2ScalarMath.itruediv
ifloordiv_scalar_matrix2 = ifloordiv_s_mat2 = Matrix2x2ScalarMath.ifloordiv
imod_scalar_matrix2 = imod_s_mat2 = Matrix2x2ScalarMath.imod
ipow_scalar_matrix2 = ipow_s_mat2 = Matrix2x2ScalarMath.ipow


class Matrix2x2XYMath:
    mul = lambda vec, x, y: (
        x * mat[0][0] + y * mat[0][1],
        x * mat[1][0] + y * mat[1][1]
        )


mul_xy_matrix2 = mul_xy_mat2 = Matrix2x2XYMath.mul


class Matrix2x2VectorMath:
    mul = lambda mat, vec: (
        vec[0] * mat[0][0] + vec[1] * mat[0][1],
        vec[0] * mat[1][0] + vec[1] * mat[1][1]
        )


mul_vector_matrix2 = mul_vec_mat2 = Matrix2x2VectorMath.mul


class Matrix2x2MatrixMath:
    add = lambda mat, other: (
        (mat[0][0] + other[0][0], mat[0][1] + other[0][1]),
        (mat[1][0] + other[1][0], mat[1][1] + other[1][1])
        )
    sub = lambda mat, other: (
        (mat[0][0] - other[0][0], mat[0][1] - other[0][1]),
        (mat[1][0] - other[1][0], mat[1][1] - other[1][1])
        )
    mul = lambda mat, other: (
        (
            mat[0][0] * other[0][0] + mat[0][1] * other[1][0],
            mat[0][0] * other[0][1] + mat[0][1] * other[1][1]
            ),
        (
            mat[1][0] * other[0][0] + mat[1][1] * other[1][0],
            mat[1][0] * other[0][1] + mat[1][1] * other[1][1]
            )
        )

    def iadd(mat, other):
        mat[0][0] += other[0][0]
        mat[0][1] += other[0][1]
        mat[1][0] += other[1][0]
        mat[1][1] += other[1][1]
        return mat

    def isub(mat, other):
        mat[0][0] -= other[0][0]
        mat[0][1] -= other[0][1]
        mat[1][0] -= other[1][0]
        mat[1][1] -= other[1][1]
        return mat

    def imul(mat, other):
        s0 = mat[0][0] * other[0][0] + mat[0][1] * other[1][0]
        s1 = mat[0][0] * other[0][1] + mat[0][1] * other[1][1]
        s2 = mat[1][0] * other[0][0] + mat[1][1] * other[1][0]
        s3 = mat[1][0] * other[0][1] + mat[1][1] * other[1][1]
        mat[0][0] = s0
        mat[0][1] = s1
        mat[1][0] = s2
        mat[1][1] = s3
        return mat


add_matrix2 = add_mat2 = Matrix2x2MatrixMath.add
sub_matrix2 = sub_mat2 = Matrix2x2MatrixMath.sub
mul_matrix2 = mul_mat2 = Matrix2x2MatrixMath.mul

iadd_matrix2 = iadd_mat2 = Matrix2x2MatrixMath.iadd
isub_matrix2 = isub_mat2 = Matrix2x2MatrixMath.isub
imul_matrix2 = imul_mat2 = Matrix2x2MatrixMath.imul


class Matrix2x2Math:
    def pow(mat, power):
        m = identity_matrix2()
        for _ in range(power):
            imul_matrix(m, mat)
        return m

    def ipow(mat, power):
        m = identity_matrix2()
        for _ in range(power):
            imul_matrix(m, mat)
        mat[0][0] = m[0][0]
        mat[0][1] = m[0][1]
        mat[1][0] = m[1][0]
        mat[1][1] = m[1][1]
        return mat


pow_matrix2 = pow_mat2 = Matrix2x2Math.pow
ipow_matrix2 = ipow_mat2 = Matrix2x2Math.ipow
