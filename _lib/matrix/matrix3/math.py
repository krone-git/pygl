from .factory import identity_matrix3, copy_matrix3


class Matrix3x3ScalarMath:
    add = lambda mat, scalar: (
        (mat[0][0] + scalar, mat[0][1] + scalar, mat[0][2] + scalar),
        (mat[1][0] + scalar, mat[1][1] + scalar, mat[1][2] + scalar),
        (mat[2][0] + scalar, mat[2][1] + scalar, mat[2][2] + scalar)
        )
    sub = lambda mat, scalar: (
        (mat[0][0] - scalar, mat[0][1] - scalar, mat[0][2] - scalar),
        (mat[1][0] - scalar, mat[1][1] - scalar, mat[1][2] - scalar),
        (mat[2][0] - scalar, mat[2][1] - scalar, mat[2][2] - scalar)
        )
    mul = lambda mat, scalar: (
        (mat[0][0] * scalar, mat[0][1] * scalar, mat[0][2] * scalar),
        (mat[1][0] * scalar, mat[1][1] * scalar, mat[1][2] * scalar),
        (mat[2][0] * scalar, mat[2][1] * scalar, mat[2][2] * scalar)
        )
    truediv = lambda mat, scalar: (
        (mat[0][0] / scalar, mat[0][1] / scalar, mat[0][2] / scalar),
        (mat[1][0] / scalar, mat[1][1] / scalar, mat[1][2] / scalar),
        (mat[2][0] / scalar, mat[2][1] / scalar, mat[2][2] / scalar)
        )
    floordiv = lambda mat, scalar: (
        (mat[0][0] // scalar, mat[0][1] // scalar, mat[0][2] // scalar),
        (mat[1][0] // scalar, mat[1][1] // scalar, mat[1][2] // scalar),
        (mat[2][0] // scalar, mat[2][1] // scalar, mat[2][2] // scalar)
        )
    mod = lambda mat, scalar: (
        (mat[0][0] % scalar, mat[0][1] % scalar, mat[0][2] % scalar),
        (mat[1][0] % scalar, mat[1][1] % scalar, mat[1][2] % scalar),
        (mat[2][0] % scalar, mat[2][1] % scalar, mat[2][2] % scalar)
        )
    pow = lambda mat, scalar: (
        (mat[0][0] ** scalar, mat[0][1] ** scalar, mat[0][2] ** scalar),
        (mat[1][0] ** scalar, mat[1][1] ** scalar, mat[1][2] ** scalar),
        (mat[2][0] ** scalar, mat[2][1] ** scalar, mat[2][2] ** scalar)
        )

    def iadd(mat, scalar):
        mat[0][0] += scalar
        mat[0][1] += scalar
        mat[0][2] += scalar
        mat[1][0] += scalar
        mat[1][1] += scalar
        mat[1][2] += scalar
        mat[2][0] += scalar
        mat[2][1] += scalar
        mat[2][2] += scalar
        return mat

    def isub(mat, scalar):
        mat[0][0] -= scalar
        mat[0][1] -= scalar
        mat[0][2] -= scalar
        mat[1][0] -= scalar
        mat[1][1] -= scalar
        mat[1][2] -= scalar
        mat[2][0] -= scalar
        mat[2][1] -= scalar
        mat[2][2] -= scalar
        return mat

    def imul(mat, scalar):
        mat[0][0] *= scalar
        mat[0][1] *= scalar
        mat[0][2] *= scalar
        mat[1][0] *= scalar
        mat[1][1] *= scalar
        mat[1][2] *= scalar
        mat[2][0] *= scalar
        mat[2][1] *= scalar
        mat[2][2] *= scalar
        return mat

    def itruediv(mat, scalar):
        mat[0][0] /= scalar
        mat[0][1] /= scalar
        mat[0][2] /= scalar
        mat[1][0] /= scalar
        mat[1][1] /= scalar
        mat[1][2] /= scalar
        mat[2][0] /= scalar
        mat[2][1] /= scalar
        mat[2][2] /= scalar
        return mat

    def ifloordiv(mat, scalar):
        mat[0][0] //= scalar
        mat[0][1] //= scalar
        mat[0][2] //= scalar
        mat[1][0] //= scalar
        mat[1][1] //= scalar
        mat[1][2] //= scalar
        mat[2][0] //= scalar
        mat[2][1] //= scalar
        mat[2][2] //= scalar
        return mat

    def imod(mat, scalar):
        mat[0][0] %= scalar
        mat[0][1] %= scalar
        mat[0][2] %= scalar
        mat[1][0] %= scalar
        mat[1][1] %= scalar
        mat[1][2] %= scalar
        mat[2][0] %= scalar
        mat[2][1] %= scalar
        mat[2][2] %= scalar
        return mat

    def ipow(mat, scalar):
        mat[0][0] **= scalar
        mat[0][1] **= scalar
        mat[0][2] **= scalar
        mat[1][0] **= scalar
        mat[1][1] **= scalar
        mat[1][2] **= scalar
        mat[2][0] **= scalar
        mat[2][1] **= scalar
        mat[2][2] **= scalar
        return mat


add_scalar_matrix3 = add_s_mat3 = Matrix3x3ScalarMath.add
sub_scalar_matrix3 = sub_s_mat3 = Matrix3x3ScalarMath.sub
mul_scalar_matrix3 = mul_s_mat3 = Matrix3x3ScalarMath.mul
truediv_scalar_matrix3 = truediv_s_mat3 = Matrix3x3ScalarMath.truediv
floordiv_scalar_matrix3 = floordiv_s_mat3 = Matrix3x3ScalarMath.floordiv
mod_scalar_matrix3 = mod_s_mat3 = Matrix3x3ScalarMath.mod
pow_scalar_matrix3 = pow_s_mat3 = Matrix3x3ScalarMath.pow

iadd_scalar_matrix3 = iadd_s_mat3 = Matrix3x3ScalarMath.iadd
isub_scalar_matrix3 = isub_s_mat3 = Matrix3x3ScalarMath.isub
imul_scalar_matrix3 = imul_s_mat3 = Matrix3x3ScalarMath.imul
itruediv_scalar_matrix3 = itruediv_s_mat3 = Matrix3x3ScalarMath.itruediv
ifloordiv_scalar_matrix3 = ifloordiv_s_mat3 = Matrix3x3ScalarMath.ifloordiv
imod_scalar_matrix3 = imod_s_mat3 = Matrix3x3ScalarMath.imod
ipow_scalar_matrix3 = ipow_s_mat3 = Matrix3x3ScalarMath.ipow


class Matrix3x3XYZMath:
    mul = lambda vec, x, y, z: (
        x * mat[0][0] + y * mat[0][1] + z * mat[0][2],
        x * mat[1][0] + y * mat[1][1] + z * mat[1][2],
        x * mat[2][0] + y * mat[2][1] + z * mat[2][2]
        )


mul_xyz_matrix3 = mul_xyz_mat3 = Matrix3x3XYZMath.mul


class Matrix3x3VectorMath:
    mul = lambda mat, vec: (
        vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2],
        vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2],
        vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2]
        )


mul_vector_matrix3 = mul_vec_mat3 = Matrix3x3VectorMath.mul


class Matrix3x3MatrixMath:
    add = lambda mat, other: (
        (mat[0][0] + other[0][0], mat[0][1] + other[0][1], mat[0][2] + other[0][2]),
        (mat[1][0] + other[1][0], mat[1][1] + other[1][1], mat[1][2] + other[1][2]),
        (mat[2][0] + other[2][0], mat[2][1] + other[2][1], mat[2][2] + other[2][2])
        )
    sub = lambda mat, other: (
        (mat[0][0] - other[0][0], mat[0][1] - other[0][1], mat[0][2] - other[0][2]),
        (mat[1][0] - other[1][0], mat[1][1] - other[1][1], mat[1][2] - other[1][2]),
        (mat[2][0] - other[2][0], mat[2][1] - other[2][1], mat[2][2] - other[2][2])
        )
    mul = lambda mat, other: (
        (
            mat[0][0] * other[0][0] + mat[0][1] * other[1][0] + mat[0][2] * other[2][0],
            mat[0][0] * other[0][1] + mat[0][1] * other[1][1] + mat[0][2] * other[2][1],
            mat[0][0] * other[0][2] + mat[0][1] * other[1][2] + mat[0][2] * other[2][2],
            ),
        (
            mat[1][0] * other[0][0] + mat[1][1] * other[1][0] + mat[1][2] * other[2][0],
            mat[1][0] * other[0][1] + mat[1][1] * other[1][1] + mat[1][2] * other[2][1],
            mat[1][0] * other[0][2] + mat[1][1] * other[1][2] + mat[1][2] * other[2][2],
            ),
        (
            mat[2][0] * other[0][0] + mat[2][1] * other[1][0] + mat[2][2] * other[2][0],
            mat[2][0] * other[0][1] + mat[2][1] * other[1][1] + mat[2][2] * other[2][1],
            mat[2][0] * other[0][2] + mat[2][1] * other[1][2] + mat[2][2] * other[2][2]
            )
        )

    def iadd(mat, other):
        mat[0][0] += other[0][0]
        mat[0][1] += other[0][1]
        mat[0][2] += other[0][2]
        mat[1][0] += other[1][0]
        mat[1][1] += other[1][1]
        mat[1][2] += other[1][2]
        mat[2][0] += other[2][0]
        mat[2][1] += other[2][1]
        mat[2][2] += other[2][2]
        return mat

    def isub(mat, other):
        mat[0][0] -= other[0][0]
        mat[0][1] -= other[0][1]
        mat[0][2] -= other[0][2]
        mat[1][0] -= other[1][0]
        mat[1][1] -= other[1][1]
        mat[1][2] -= other[1][2]
        mat[2][0] -= other[2][0]
        mat[2][1] -= other[2][1]
        mat[2][2] -= other[2][2]
        return mat

    def imul(mat, other):
        s0 = mat[0][0] * other[0][0] + mat[0][1] * other[1][0] + mat[0][2] * other[2][0]
        s1 = mat[0][0] * other[0][1] + mat[0][1] * other[1][1] + mat[0][2] * other[2][1]
        s2 = mat[0][0] * other[0][2] + mat[0][1] * other[1][2] + mat[0][2] * other[2][2]
        s3 = mat[1][0] * other[0][0] + mat[1][1] * other[1][0] + mat[1][2] * other[2][0]
        s4 = mat[1][0] * other[0][1] + mat[1][1] * other[1][1] + mat[1][2] * other[2][1]
        s5 = mat[1][0] * other[0][2] + mat[1][1] * other[1][2] + mat[1][2] * other[2][2]
        s6 = mat[2][0] * other[0][0] + mat[2][1] * other[1][0] + mat[2][2] * other[2][0]
        s7 = mat[2][0] * other[0][1] + mat[2][1] * other[1][1] + mat[2][2] * other[2][1]
        s8 = mat[2][0] * other[0][2] + mat[2][1] * other[1][2] + mat[2][2] * other[2][2]
        mat[0][0] = s0
        mat[0][1] = s1
        mat[0][2] = s2
        mat[1][0] = s3
        mat[1][1] = s4
        mat[1][2] = s5
        mat[2][0] = s6
        mat[2][1] = s7
        mat[2][2] = s8
        return mat


add_matrix3 = add_mat3 = Matrix3x3MatrixMath.add
sub_matrix3 = sub_mat3 = Matrix3x3MatrixMath.sub
mul_matrix3 = mul_mat3 = Matrix3x3MatrixMath.mul

iadd_matrix3 = iadd_mat3 = Matrix3x3MatrixMath.iadd
isub_matrix3 = isub_mat3 = Matrix3x3MatrixMath.isub
imul_matrix3 = imul_mat3 = Matrix3x3MatrixMath.imul


class Matrix3x3Math:
    def pow(mat, power):
        m = identity_matrix3()
        for _ in range(power):
            imul_matrix(m, mat)
        return m

    def ipow(mat, power):
        m = identity_matrix3()
        for _ in range(power):
            imul_matrix(m, mat)
        mat[0][0] = m[0][0]
        mat[0][1] = m[0][1]
        mat[0][2] = m[0][2]
        mat[1][0] = m[1][0]
        mat[1][1] = m[1][1]
        mat[1][2] = m[1][2]
        mat[2][0] = m[2][0]
        mat[2][1] = m[2][1]
        mat[2][2] = m[2][2]
        return mat


pow_matrix3 = pow_mat3 = Matrix3x3Math.pow
ipow_matrix3 = ipow_mat3 = Matrix3x3Math.ipow
