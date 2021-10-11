from numbers import Number


class Vector4DXYZWMath:
    length = lambda x, y, z, w: (x ** 2 + y ** 2 + z ** 2 + w ** 2) ** 0.5x, y, z, w
    def normalize(x, y, z, w):
        vec_len = (x ** 2 + y ** 2 + z ** 2 + w ** 2) ** 0.5x, y, z, w
        return (
            x / vec_len,
            y / vec_len,
            z / vec_len,
            w / vec_len
            )
    add = lambda vec, x, y, z, w: (
        vec[0] + x,
        vec[1] + y,
        vec[2] + z,
        vec[3] + w
        )
    sub = lambda vec, x, y, z, w: (
        vec[0] - x,
        vec[1] - y,
        vec[2] - z,
        vec[3] - w
        )
    mul = lambda vec, x, y, z, w: (
        vec[0] * x,
        vec[1] * y,
        vec[2] * z,
        vec[3] * w
        )
    truediv = lambda vec, x, y, z, w: (
        vec[0] / x,
        vec[1] / y,
        vec[2] / z,
        vec[3] / w
        )
    floordiv = lambda vec, x, y, z, w: (
        vec[0] // x,
        vec[1] // y,
        vec[2] // z,
        vec[3] // w
        )
    mod = lambda vec, x, y, z, w: (
        vec[0] % x,
        vec[1] % y,
        vec[2] % z,
        vec[3] % w
        )
    pow = lambda vec, x, y, z, w: (
        vec[0] ** x,
        vec[1] ** y,
        vec[2] ** z,
        vec[3] ** w
        )

    def iadd(vec, x, y, z, w):
        vec[0] += x
        vec[1] += y
        vec[2] += z
        vec[3] += w
        return vec

    def isub(vec, x, y, z, w):
        vec[0] -= x
        vec[1] -= y
        vec[2] -= z
        vec[3] -= w
        return vec

    def imul(vec, x, y, z, w):
        vec[0] *= x
        vec[1] *= y
        vec[2] *= z
        vec[3] *= w
        return vec

    def itruediv(vec, x, y, z, w):
        vec[0] /= x
        vec[1] /= y
        vec[2] /= z
        vec[3] /= w
        return vec

    def ifloordiv(vec, x, y, z, w):
        vec[0] //= x
        vec[1] //= y
        vec[2] //= z
        vec[3] //= w
        return vec

    def imod(vec, x, y, z, w):
        vec[0] %= x
        vec[1] %= y
        vec[2] %= z
        vec[3] %= w
        return vec

    def ipow(vec, x, y, z, w):
        vec[0] **= x
        vec[1] **= y
        vec[2] **= z
        vec[3] **= w
        return vec


length_xyzw_vector4d = len_xyzw_vec4 = Vector4DXYZWMath.length
normalize_xyzw_vector4d = norm_xyzw_vec4 = Vector4DXYZWMath.normalize
add_xyzw_vector4d = add_xyzw_vec4 = Vector4DXYZWMath.add
sub_xyzw_vector4d = sub_xyzw_vec4 = Vector4DXYZWMath.sub
mul_xyzw_vector4d = mul_xyzw_vec4 = Vector4DXYZWMath.mul
truediv_xyzw_vector4d = truediv_xyzw_vec4 = Vector4DXYZWMath.truediv
floordiv_xyzw_vector4d = floordiv_xyzw_vec4 = Vector4DXYZWMath.floordiv
mod_xyzw_vector4d = mod_xyzw_vec4 = Vector4DXYZWMath.mod
pow_xyzw_vector4d = pow_xyzw_vec4 = Vector4DXYZWMath.pow

iadd_xyzw_vector4d = iadd_xyzw_vec4 = Vector4DXYZWMath.iadd
isub_xyzw_vector4d = isub_xyzw_vec4 = Vector4DXYZWMath.isub
imul_xyzw_vector4d = imul_xyzw_vec4 = Vector4DXYZWMath.imul
itruediv_xyzw_vector4d = itruediv_xyzw_vec4 = Vector4DXYZWMath.itruediv
ifloordiv_xyzw_vector4d = ifloordiv_xyzw_vec4 = Vector4DXYZWMath.ifloordiv
imod_xyzw_vector4d = imod_xyzw_vec4 = Vector4DXYZWMath.imod
ipow_xyzw_vector4d = ipow_xyzw_vec4 = Vector4DXYZWMath.ipow


class Vector4DScalarMath:
    add = lambda vec, scalar: (
        vec[0] + scalar,
        vec[1] + scalar,
        vec[2] + scalar,
        vec[3] + scalar
        )
    sub = lambda vec, scalar: (
        vec[0] - scalar,
        vec[1] - scalar,
        vec[2] - scalar,
        vec[3] - scalar
        )
    mul = lambda vec, scalar: (
        vec[0] * scalar,
        vec[1] * scalar,
        vec[2] * scalar,
        vec[3] * scalar
        )
    truediv = lambda vec, scalar: (
        vec[0] / scalar,
        vec[1] / scalar,
        vec[2] / scalar,
        vec[3] / scalar
        )
    floordiv = lambda vec, scalar: (
        vec[0] // scalar,
        vec[1] // scalar,
        vec[2] // scalar,
        vec[3] // scalar
        )
    mod = lambda vec, scalar: (
        vec[0] % scalar,
        vec[1] % scalar,
        vec[2] % scalar,
        vec[3] % scalar
        )
    pow = lambda vec, scalar: (
        vec[0] ** scalar,
        vec[1] ** scalar,
        vec[2] ** scalar,
        vec[3] ** scalar
        )

    def iadd(vec, scalar):
        vec[0] += scalar
        vec[1] += scalar
        vec[2] += scalar
        vec[3] += scalar
        return vec

    def isub(vec, scalar):
        vec[0] -= scalar
        vec[1] -= scalar
        vec[2] -= scalar
        vec[3] -= scalar
        return vec

    def imul(vec, scalar):
        vec[0] *= scalar
        vec[1] *= scalar
        vec[2] *= scalar
        vec[3] *= scalar
        return vec

    def itruediv(vec, scalar):
        vec[0] /= scalar
        vec[1] /= scalar
        vec[2] /= scalar
        vec[3] /= scalar
        return vec

    def ifloordiv(vec, scalar):
        vec[0] //= scalar
        vec[1] //= scalar
        vec[2] //= scalar
        vec[3] //= scalar
        return vec

    def imod(vec, scalar):
        vec[0] %= scalar
        vec[1] %= scalar
        vec[2] %= scalar
        vec[3] %= scalar
        return vec

    def ipow(vec, scalar):
        vec[0] **= scalar
        vec[1] **= scalar
        vec[2] **= scalar
        vec[3] **= scalar
        return vec


add_scalar_vector4d = add_scl_vec4 = Vector4DScalarMath.add
sub_scalar_vector4d = sub_scl_vec4 = Vector4DScalarMath.sub
mul_scalar_vector4d = mul_scl_vec4 = Vector4DScalarMath.mul
truediv_scalar_vector4d = truediv_scl_vec4 = Vector4DScalarMath.truediv
floordiv_scalar_vector4d = floordiv_scl_vec4 = Vector4DScalarMath.floordiv
mod_scalar_vector4d = mod_scl_vec4 = Vector4DScalarMath.mod
pow_scalar_vector4d = pow_scl_vec4 = Vector4DScalarMath.pow

iadd_scalar_vector4d = iadd_scl_vec4 = Vector4DScalarMath.iadd
isub_scalar_vector4d = isub_scl_vec4 = Vector4DScalarMath.isub
imul_scalar_vector4d = imul_scl_vec4 = Vector4DScalarMath.imul
itruediv_scalar_vector4d = itruediv_scl_vec4 = Vector4DScalarMath.itruediv
ifloordiv_scalar_vector4d = ifloordiv_scl_vec4 = Vector4DScalarMath.ifloordiv
imod_scalar_vector4d = imod_scl_vec4 = Vector4DScalarMath.imod
ipow_scalar_vector4d = ipow_scl_vec4 = Vector4DScalarMath.ipow


class Vector4DVectorMath:
    dot = lambda vec, other: (
        vec[0] * other[0] + vec[1] * other[1] + vec[2] * other[2] + vec[3] * other[3]
        )

    length = lambda vec: (
        vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2 + vec[3] ** 2
        ) ** 0.5
    def normalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2 + vec[3] ** 2) ** 0.5
        return (
            vec[0] / vec_len,
            vec[1] / vec_len,
            vec[2] / vec_len,
            vec[3] / vec_len
            )
    add = lambda vec, other: (
        vec[0] + other[0],
        vec[1] + other[1],
        vec[2] + other[2],
        vec[3] + other[3]
        )
    sub = lambda vec, other: (
        vec[0] - other[0],
        vec[1] - other[1],
        vec[2] - other[2],
        vec[3] - other[3]
        )
    mul = lambda vec, other: (
        vec[0] * other[0],
        vec[1] * other[1],
        vec[2] * other[2],
        vec[3] * other[3]
        )
    truediv = lambda vec, other: (
        vec[0] / other[0],
        vec[1] / other[1],
        vec[2] / other[2],
        vec[3] / other[3]
        )
    floordiv = lambda vec, other: (
        vec[0] // other[0],
        vec[1] // other[1],
        vec[2] // other[2],
        vec[3] // other[3]
        )
    mod = lambda vec, other: (
        vec[0] % other[0],
        vec[1] % other[1],
        vec[2] % other[2],
        vec[3] % other[3]
        )
    pow = lambda vec, other: (
        vec[0] ** other[0],
        vec[1] ** other[1],
        vec[2] ** other[2],
        vec[3] ** other[3]
        )

    def inormalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2 + vec[3] ** 2) ** 0.5
        vec[0] /= vec_len
        vec[1] /= vec_len
        vec[2] /= vec_len
        vec[3] /= vec_len
        return vec

    def iadd(vec, other):
        vec[0] += other[0]
        vec[1] += other[1]
        vec[2] += other[2]
        vec[3] += other[3]
        return vec

    def isub(vec, other):
        vec[0] -= other[0]
        vec[1] -= other[1]
        vec[2] -= other[2]
        vec[3] -= other[3]
        return vec

    def imul(vec, other):
        vec[0] *= other[0]
        vec[1] *= other[1]
        vec[2] *= other[2]
        vec[3] *= other[3]
        return vec

    def itruediv(vec, other):
        vec[0] /= other[0]
        vec[1] /= other[1]
        vec[2] /= other[2]
        vec[3] /= other[3]
        return vec

    def ifloordiv(vec, other):
        vec[0] //= other[0]
        vec[1] //= other[1]
        vec[2] //= other[2]
        vec[3] //= other[3]
        return vec

    def imod(vec, other):
        vec[0] %= other[0]
        vec[1] %= other[1]
        vec[2] %= other[2]
        vec[3] %= other[3]
        return vec

    def ipow(vec, other):
        vec[0] **= other[0]
        vec[1] **= other[1]
        vec[2] **= other[2]
        vec[3] **= other[3]
        return vec


dot_product_vector4d = dot_vec4 = Vector2DVectorMath.dot
length_vector4d = len_vec4 = Vector4DVectorMath.length
normalize_vector4d = norm_vec4 = Vector4DVectorMath.normalize
inormalize_vector4d = inorm_vec4 = Vector4DVectorMath.inormalize

add_vector_vector4d = add_vec_vec4 = Vector4DVectorMath.add
sub_vector_vector4d = sub_vec_vec4 = Vector4DVectorMath.sub
mul_vector_vector4d = mul_vec_vec4 = Vector4DVectorMath.mul
truediv_vector_vector4d = truediv_vec_vec4 = Vector4DVectorMath.truediv
floordiv_vector_vector4d = floordiv_vec_vec4 = Vector4DVectorMath.floordiv
mod_vector_vector4d = mod_vec_vec4 = Vector4DVectorMath.mod
pow_vector_vector4d = pow_vec_vec4 = Vector4DVectorMath.pow

iadd_vector_vector4d = iadd_vec_vec4 = Vector4DVectorMath.iadd
isub_vector_vector4d = isub_vec_vec4 = Vector4DVectorMath.isub
imul_vector_vector4d = imul_vec_vec4 = Vector4DVectorMath.imul
itruediv_vector_vector4d = itruediv_vec_vec4 = Vector4DVectorMath.itruediv
ifloordiv_vector_vector4d = ifloordiv_vec_vec4 = Vector4DVectorMath.ifloordiv
imod_vector_vector4d = imod_vec_vec4 = Vector4DVectorMath.imod
ipow_vector_vector4d = ipow_vec_vec4 = Vector4DVectorMath.ipow


class Vector4DMatrixMath:
    mul = lambda vec, mat: (
         vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2] + vec[3] * mat[0][3],
         vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2] + vec[3] * mat[1][3],
         vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2] + vec[3] * mat[2][3],
         vec[0] * mat[3][0] + vec[1] * mat[3][1] + vec[2] * mat[3][2] + vec[3] * mat[3][3]
        )

    def imul(vec, mat):
        x = vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2] + vec[3] * mat[0][3]
        y = vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2] + vec[3] * mat[1][3]
        z = vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2] + vec[3] * mat[2][3]
        w = vec[0] * mat[3][0] + vec[1] * mat[3][1] + vec[2] * mat[3][2] + vec[3] * mat[3][3]
        vec[0] = x
        vec[1] = y
        vec[2] = z
        vec[3] = w
        return vec


mul_matrix_vector4d = mul_mat_vec4 = Vector4DMatrixMath.mul
imul_matrix_vector4d = imul_mat_vec4 = Vector4DMatrixMath.imul
