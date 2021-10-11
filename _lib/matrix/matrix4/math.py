from .factory import identity_matrix4, copy_matrix4


class Matrix4x4ScalarMath:
    add = lambda mat, scalar: (
        (mat[0][0] + scalar, mat[0][1] + scalar, mat[0][2] + scalar, mat[0][3] + scalar),
        (mat[1][0] + scalar, mat[1][1] + scalar, mat[1][2] + scalar, mat[1][3] + scalar),
        (mat[2][0] + scalar, mat[2][1] + scalar, mat[2][2] + scalar, mat[2][3] + scalar),
        (mat[3][0] + scalar, mat[3][1] + scalar, mat[3][2] + scalar, mat[3][3] + scalar)
        )
    sub = lambda mat, scalar: (
        (mat[0][0] - scalar, mat[0][1] - scalar, mat[0][2] - scalar, mat[0][3] - scalar),
        (mat[1][0] - scalar, mat[1][1] - scalar, mat[1][2] - scalar, mat[1][3] - scalar),
        (mat[2][0] - scalar, mat[2][1] - scalar, mat[2][2] - scalar, mat[2][3] - scalar),
        (mat[3][0] - scalar, mat[3][1] - scalar, mat[3][2] - scalar, mat[3][3] - scalar)
        )
    mul = lambda mat, scalar: (
        (mat[0][0] * scalar, mat[0][1] * scalar, mat[0][2] * scalar, mat[0][3] * scalar),
        (mat[1][0] * scalar, mat[1][1] * scalar, mat[1][2] * scalar, mat[1][3] * scalar),
        (mat[2][0] * scalar, mat[2][1] * scalar, mat[2][2] * scalar, mat[2][3] * scalar),
        (mat[3][0] * scalar, mat[3][1] * scalar, mat[3][2] * scalar, mat[3][3] * scalar)
        )
    truediv = lambda mat, scalar: (
        (mat[0][0] / scalar, mat[0][1] / scalar, mat[0][2] / scalar, mat[0][3] / scalar),
        (mat[1][0] / scalar, mat[1][1] / scalar, mat[1][2] / scalar, mat[1][3] / scalar),
        (mat[2][0] / scalar, mat[2][1] / scalar, mat[2][2] / scalar, mat[2][3] / scalar),
        (mat[3][0] / scalar, mat[3][1] / scalar, mat[3][2] / scalar, mat[3][3] / scalar)
        )
    floordiv = lambda mat, scalar: (
        (mat[0][0] // scalar, mat[0][1] // scalar, mat[0][2] // scalar, mat[0][3] // scalar),
        (mat[1][0] // scalar, mat[1][1] // scalar, mat[1][2] // scalar, mat[1][3] // scalar),
        (mat[2][0] // scalar, mat[2][1] // scalar, mat[2][2] // scalar, mat[2][3] // scalar),
        (mat[3][0] // scalar, mat[3][1] // scalar, mat[3][2] // scalar, mat[3][3] // scalar)
        )
    mod = lambda mat, scalar: (
        (mat[0][0] % scalar, mat[0][1] % scalar, mat[0][2] % scalar, mat[0][3] % scalar),
        (mat[1][0] % scalar, mat[1][1] % scalar, mat[1][2] % scalar, mat[1][3] % scalar),
        (mat[2][0] % scalar, mat[2][1] % scalar, mat[2][2] % scalar, mat[2][3] % scalar),
        (mat[3][0] % scalar, mat[3][1] % scalar, mat[3][2] % scalar, mat[3][3] % scalar)
        )
    pow = lambda mat, scalar: (
        (mat[0][0] ** scalar, mat[0][1] ** scalar, mat[0][2] ** scalar, mat[0][3] ** scalar),
        (mat[1][0] ** scalar, mat[1][1] ** scalar, mat[1][2] ** scalar, mat[1][3] ** scalar),
        (mat[2][0] ** scalar, mat[2][1] ** scalar, mat[2][2] ** scalar, mat[2][3] ** scalar),
        (mat[3][0] ** scalar, mat[3][1] ** scalar, mat[3][2] ** scalar, mat[3][3] ** scalar)
        )

    def iadd(mat, scalar):
        mat[0][0] += scalar
        mat[0][1] += scalar
        mat[0][2] += scalar
        mat[0][3] += scalar
        mat[1][0] += scalar
        mat[1][1] += scalar
        mat[1][2] += scalar
        mat[1][3] += scalar
        mat[2][0] += scalar
        mat[2][1] += scalar
        mat[2][2] += scalar
        mat[2][3] += scalar
        mat[3][0] += scalar
        mat[3][1] += scalar
        mat[3][2] += scalar
        mat[3][3] += scalar
        return mat

    def isub(mat, scalar):
        mat[0][0] -= scalar
        mat[0][1] -= scalar
        mat[0][2] -= scalar
        mat[0][3] -= scalar
        mat[1][0] -= scalar
        mat[1][1] -= scalar
        mat[1][2] -= scalar
        mat[1][3] -= scalar
        mat[2][0] -= scalar
        mat[2][1] -= scalar
        mat[2][2] -= scalar
        mat[2][3] -= scalar
        mat[3][0] -= scalar
        mat[3][1] -= scalar
        mat[3][2] -= scalar
        mat[3][3] -= scalar
        return mat

    def imul(mat, scalar):
        mat[0][0] *= scalar
        mat[0][1] *= scalar
        mat[0][2] *= scalar
        mat[0][3] *= scalar
        mat[1][0] *= scalar
        mat[1][1] *= scalar
        mat[1][2] *= scalar
        mat[1][3] *= scalar
        mat[2][0] *= scalar
        mat[2][1] *= scalar
        mat[2][2] *= scalar
        mat[2][3] *= scalar
        mat[3][0] *= scalar
        mat[3][1] *= scalar
        mat[3][2] *= scalar
        mat[3][3] *= scalar
        return mat

    def itruediv(mat, scalar):
        mat[0][0] /= scalar
        mat[0][1] /= scalar
        mat[0][2] /= scalar
        mat[0][3] /= scalar
        mat[1][0] /= scalar
        mat[1][1] /= scalar
        mat[1][2] /= scalar
        mat[1][3] /= scalar
        mat[2][0] /= scalar
        mat[2][1] /= scalar
        mat[2][2] /= scalar
        mat[2][3] /= scalar
        mat[3][0] /= scalar
        mat[3][1] /= scalar
        mat[3][2] /= scalar
        mat[3][3] /= scalar
        return mat

    def ifloordiv(mat, scalar):
        mat[0][0] //= scalar
        mat[0][1] //= scalar
        mat[0][2] //= scalar
        mat[0][3] //= scalar
        mat[1][0] //= scalar
        mat[1][1] //= scalar
        mat[1][2] //= scalar
        mat[1][3] //= scalar
        mat[2][0] //= scalar
        mat[2][1] //= scalar
        mat[2][2] //= scalar
        mat[2][3] //= scalar
        mat[3][0] //= scalar
        mat[3][1] //= scalar
        mat[3][2] //= scalar
        mat[3][3] //= scalar
        return mat

    def imod(mat, scalar):
        mat[0][0] %= scalar
        mat[0][1] %= scalar
        mat[0][2] %= scalar
        mat[0][3] %= scalar
        mat[1][0] %= scalar
        mat[1][1] %= scalar
        mat[1][2] %= scalar
        mat[1][3] %= scalar
        mat[2][0] %= scalar
        mat[2][1] %= scalar
        mat[2][2] %= scalar
        mat[2][3] %= scalar
        mat[3][0] %= scalar
        mat[3][1] %= scalar
        mat[3][2] %= scalar
        mat[3][3] %= scalar
        return mat

    def ipow(mat, scalar):
        mat[0][0] **= scalar
        mat[0][1] **= scalar
        mat[0][2] **= scalar
        mat[0][3] **= scalar
        mat[1][0] **= scalar
        mat[1][1] **= scalar
        mat[1][2] **= scalar
        mat[1][3] **= scalar
        mat[2][0] **= scalar
        mat[2][1] **= scalar
        mat[2][2] **= scalar
        mat[2][3] **= scalar
        mat[3][0] **= scalar
        mat[3][1] **= scalar
        mat[3][2] **= scalar
        mat[3][3] **= scalar
        return mat


add_scalar_matrix4 = add_s_mat4 = Matrix4x4ScalarMath.add
sub_scalar_matrix4 = sub_s_mat4 = Matrix4x4ScalarMath.sub
mul_scalar_matrix4 = mul_s_mat4 = Matrix4x4ScalarMath.mul
truediv_scalar_matrix4 = truediv_s_mat4 = Matrix4x4ScalarMath.truediv
floordiv_scalar_matrix4 = floordiv_s_mat4 = Matrix4x4ScalarMath.floordiv
mod_scalar_matrix4 = mod_s_mat4 = Matrix4x4ScalarMath.mod
pow_scalar_matrix4 = pow_s_mat4 = Matrix4x4ScalarMath.pow

iadd_scalar_matrix4 = iadd_s_mat4 = Matrix4x4ScalarMath.iadd
isub_scalar_matrix4 = isub_s_mat4 = Matrix4x4ScalarMath.isub
imul_scalar_matrix4 = imul_s_mat4 = Matrix4x4ScalarMath.imul
itruediv_scalar_matrix4 = itruediv_s_mat4 = Matrix4x4ScalarMath.itruediv
ifloordiv_scalar_matrix4 = ifloordiv_s_mat4 = Matrix4x4ScalarMath.ifloordiv
imod_scalar_matrix4 = imod_s_mat4 = Matrix4x4ScalarMath.imod
ipow_scalar_matrix4 = ipow_s_mat4 = Matrix4x4ScalarMath.ipow


class Matrix4x4XYZWMath:
    mul = lambda mat, x, y, z, w: (
        x * mat[0][0] + y * mat[0][1] + z * mat[0][2] + w * mat[0][3],
        x * mat[1][0] + y * mat[1][1] + z * mat[1][2] + w * mat[1][3],
        x * mat[2][0] + y * mat[2][1] + z * mat[2][2] + w * mat[2][3],
        x * mat[3][0] + y * mat[3][1] + z * mat[3][2] + w * mat[3][3]
        )


mul_xyzw_matrix4 = mul_xyzw_mat4 = Matrix4x4XYZWMath.mul


class Matrix4x4VectorMath:
    mul = lambda mat, vec: (
        vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2] + vec[3] * mat[0][3],
        vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2] + vec[3] * mat[1][3],
        vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2] + vec[3] * mat[2][3],
        vec[0] * mat[3][0] + vec[1] * mat[3][1] + vec[2] * mat[3][2] + vec[3] * mat[3][3]
        )


mul_vector_matrix4 = mul_vec_mat4 = Matrix4x4VectorMath.mul


class Matrix4x4MatrixMath:
    add = lambda mat, other: (
        (
            mat[0][0] + other[0][0], mat[0][1] + other[0][1],
            mat[0][2] + other[0][2], mat[0][3] + other[0][3]
            ),
        (
            mat[1][0] + other[1][0], mat[1][1] + other[1][1],
            mat[1][2] + other[1][2], mat[1][3] + other[1][3]
            ),
        (
            mat[2][0] + other[2][0], mat[2][1] + other[2][1],
            mat[2][2] + other[2][2], mat[2][3] + other[2][3]
            ),
        (
            mat[3][0] + other[3][0], mat[3][1] + other[3][1],
            mat[3][2] + other[3][2], mat[3][3] + other[3][3]
            )
        )
    sub = lambda mat, other: (
        (
            mat[0][0] - other[0][0], mat[0][1] - other[0][1],
            mat[0][2] - other[0][2], mat[0][3] - other[0][3]
            ),
        (
            mat[1][0] - other[1][0], mat[1][1] - other[1][1],
            mat[1][2] - other[1][2], mat[1][3] - other[1][3]
            ),
        (
            mat[2][0] - other[2][0], mat[2][1] - other[2][1],
            mat[2][2] - other[2][2], mat[2][3] - other[2][3]
            ),
        (
            mat[3][0] - other[3][0], mat[3][1] - other[3][1],
            mat[3][2] - other[3][2], mat[3][3] - other[3][3]
            )
        )
    mul = lambda mat, other: (
        (
            mat[0][0] * other[0][0] + mat[0][1] * other[1][0] + mat[0][2] * other[2][0] + mat[0][3] * other[3][0],
            mat[0][0] * other[0][1] + mat[0][1] * other[1][1] + mat[0][2] * other[2][1] + mat[0][3] * other[3][1],
            mat[0][0] * other[0][2] + mat[0][1] * other[1][2] + mat[0][2] * other[2][2] + mat[0][3] * other[3][2],
            mat[0][0] * other[0][3] + mat[0][1] * other[1][3] + mat[0][2] * other[2][3] + mat[0][3] * other[3][3],
            ),
        (
            mat[1][0] * other[0][0] + mat[1][1] * other[1][0] + mat[1][2] * other[2][0] + mat[1][3] * other[3][0],
            mat[1][0] * other[0][1] + mat[1][1] * other[1][1] + mat[1][2] * other[2][1] + mat[1][3] * other[3][1],
            mat[1][0] * other[0][2] + mat[1][1] * other[1][2] + mat[1][2] * other[2][2] + mat[1][3] * other[3][2],
            mat[1][0] * other[0][3] + mat[1][1] * other[1][3] + mat[1][2] * other[2][3] + mat[1][3] * other[3][3],
            ),
        (
            mat[2][0] * other[0][0] + mat[2][1] * other[1][0] + mat[2][2] * other[2][0] + mat[2][3] * other[3][0],
            mat[2][0] * other[0][1] + mat[2][1] * other[1][1] + mat[2][2] * other[2][1] + mat[2][3] * other[3][1],
            mat[2][0] * other[0][2] + mat[2][1] * other[1][2] + mat[2][2] * other[2][2] + mat[2][3] * other[3][2],
            mat[2][0] * other[0][3] + mat[2][1] * other[1][3] + mat[2][2] * other[2][3] + mat[2][3] * other[3][3],
            ),
        (
            mat[3][0] * other[0][0] + mat[3][1] * other[1][0] + mat[3][2] * other[2][0] + mat[3][3] * other[3][0],
            mat[3][0] * other[0][1] + mat[3][1] * other[1][1] + mat[3][2] * other[2][1] + mat[3][3] * other[3][1],
            mat[3][0] * other[0][2] + mat[3][1] * other[1][2] + mat[3][2] * other[2][2] + mat[3][3] * other[3][2],
            mat[3][0] * other[0][3] + mat[3][1] * other[1][3] + mat[3][2] * other[2][3] + mat[3][3] * other[3][3]
            )
        )

    def iadd(mat, other):
        mat[0][0] += other[0][0]
        mat[0][1] += other[0][1]
        mat[0][2] += other[0][2]
        mat[0][3] += other[0][3]
        mat[1][0] += other[1][0]
        mat[1][1] += other[1][1]
        mat[1][2] += other[1][2]
        mat[1][3] += other[1][3]
        mat[2][0] += other[2][0]
        mat[2][1] += other[2][1]
        mat[2][2] += other[2][2]
        mat[2][3] += other[2][3]
        mat[3][0] += other[3][0]
        mat[3][1] += other[3][1]
        mat[3][2] += other[3][2]
        mat[3][3] += other[3][3]
        return mat

    def isub(mat, other):
        mat[0][0] -= other[0][0]
        mat[0][1] -= other[0][1]
        mat[0][2] -= other[0][2]
        mat[0][3] -= other[0][3]
        mat[1][0] -= other[1][0]
        mat[1][1] -= other[1][1]
        mat[1][2] -= other[1][2]
        mat[1][3] -= other[1][3]
        mat[2][0] -= other[2][0]
        mat[2][1] -= other[2][1]
        mat[2][2] -= other[2][2]
        mat[2][3] -= other[2][3]
        mat[3][0] -= other[3][0]
        mat[3][1] -= other[3][1]
        mat[3][2] -= other[3][2]
        mat[3][3] -= other[3][3]
        return mat

    def imul(mat, other):
        s0 = mat[0][0] * other[0][0] + mat[0][1] * other[1][0] + mat[0][2] * other[2][0] + mat[0][3] * other[3][0]
        s1 = mat[0][0] * other[0][1] + mat[0][1] * other[1][1] + mat[0][2] * other[2][1] + mat[0][3] * other[3][1]
        s2 = mat[0][0] * other[0][2] + mat[0][1] * other[1][2] + mat[0][2] * other[2][2] + mat[0][3] * other[3][2]
        s3 = mat[0][0] * other[0][3] + mat[0][1] * other[1][3] + mat[0][2] * other[2][3] + mat[0][3] * other[3][3]
        s4 = mat[1][0] * other[0][0] + mat[1][1] * other[1][0] + mat[1][2] * other[2][0] + mat[1][3] * other[3][0]
        s5 = mat[1][0] * other[0][1] + mat[1][1] * other[1][1] + mat[1][2] * other[2][1] + mat[1][3] * other[3][1]
        s6 = mat[1][0] * other[0][2] + mat[1][1] * other[1][2] + mat[1][2] * other[2][2] + mat[1][3] * other[3][2]
        s7 = mat[1][0] * other[0][3] + mat[1][1] * other[1][3] + mat[1][2] * other[2][3] + mat[1][3] * other[3][3]
        s8 = mat[2][0] * other[0][0] + mat[2][1] * other[1][0] + mat[2][2] * other[2][0] + mat[2][3] * other[3][0]
        s9 = mat[2][0] * other[0][1] + mat[2][1] * other[1][1] + mat[2][2] * other[2][1] + mat[2][3] * other[3][1]
        s10 = mat[2][0] * other[0][2] + mat[2][1] * other[1][2] + mat[2][2] * other[2][2] + mat[2][3] * other[3][2]
        s11 = mat[2][0] * other[0][3] + mat[2][1] * other[1][3] + mat[2][2] * other[2][3] + mat[2][3] * other[3][3]
        s12 = mat[3][0] * other[0][0] + mat[3][1] * other[1][0] + mat[3][2] * other[2][0] + mat[3][3] * other[3][0]
        s13 = mat[3][0] * other[0][1] + mat[3][1] * other[1][1] + mat[3][2] * other[2][1] + mat[3][3] * other[3][1]
        s14 = mat[3][0] * other[0][2] + mat[3][1] * other[1][2] + mat[3][2] * other[2][2] + mat[3][3] * other[3][2]
        s15 = mat[3][0] * other[0][3] + mat[3][1] * other[1][3] + mat[3][2] * other[2][3] + mat[3][3] * other[3][3]
        mat[0][0] = s0
        mat[0][1] = s1
        mat[0][2] = s2
        mat[0][3] = s3
        mat[1][0] = s4
        mat[1][1] = s5
        mat[1][2] = s6
        mat[1][3] = s7
        mat[2][0] = s8
        mat[2][1] = s9
        mat[2][2] = s10
        mat[2][3] = s11
        mat[3][0] = s12
        mat[3][1] = s13
        mat[3][2] = s14
        mat[3][3] = s15
        return mat


add_matrix4 = add_mat4 = Matrix4x4MatrixMath.add
sub_matrix4 = sub_mat4 = Matrix4x4MatrixMath.sub
mul_matrix4 = mul_mat4 = Matrix4x4MatrixMath.mul

iadd_matrix4 = iadd_mat4 = Matrix4x4MatrixMath.iadd
isub_matrix4 = isub_mat4 = Matrix4x4MatrixMath.isub
imul_matrix4 = imul_mat4 = Matrix4x4MatrixMath.imul


class Matrix4x4Math:
    def pow(mat, power):
        m = identity_matrix4()
        for _ in range(power):
            imul_matrix(m, mat)
        return m

    def ipow(mat, power):
        m = identity_matrix4()
        for _ in range(power):
            imul_matrix(m, mat)
        mat[0][0] = m[0][0]
        mat[0][1] = m[0][1]
        mat[0][2] = m[0][2]
        mat[0][3] = m[0][3]
        mat[1][0] = m[1][0]
        mat[1][1] = m[1][1]
        mat[1][2] = m[1][2]
        mat[1][3] = m[1][3]
        mat[2][0] = m[2][0]
        mat[2][1] = m[2][1]
        mat[2][2] = m[2][2]
        mat[2][3] = m[2][3]
        mat[3][0] = m[3][0]
        mat[3][1] = m[3][1]
        mat[3][2] = m[3][2]
        mat[3][3] = m[3][3]
        return mat


pow_matrix4 = pow_mat4 = Matrix4x4Math.pow
ipow_matrix4 = ipow_mat4 = Matrix4x4Math.ipow
