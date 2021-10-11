from numbers import Number


class Vector2DXYMath:
    length = lambda x, y: (x ** 2 + y ** 2) ** 0.5
    def normalize(x, y):
        vec_len = (x ** 2 + y ** 2) ** 0.5
        return (
            x / vec_len,
            y / vec_len
            )
    add = lambda vec, x, y: (
        vec[0] + x,
        vec[1] + y
        )
    sub = lambda vec, x, y: (
        vec[0] - x,
        vec[1] - y
        )
    mul = lambda vec, x, y: (
        vec[0] * x,
        vec[1] * y
        )
    truediv = lambda vec, x, y: (
        vec[0] / x,
        vec[1] / y
        )
    floordiv = lambda vec, x, y: (
        vec[0] // x,
        vec[1] // y
        )
    mod = lambda vec, x, y: (
        vec[0] % x,
        vec[1] % y
        )
    pow = lambda vec, x, y: (
        vec[0] ** x,
        vec[1] ** y
        )

    def iadd(vec, x, y):
        vec[0] += x
        vec[1] += y
        return vec

    def isub(vec, x, y):
        vec[0] -= x
        vec[1] -= y
        return vec

    def imul(vec, x, y):
        vec[0] *= x
        vec[1] *= y
        return vec

    def itruediv(vec, x, y):
        vec[0] /= x
        vec[1] /= y
        return vec

    def ifloordiv(vec, x, y):
        vec[0] //= x
        vec[1] //= y
        return vec

    def imod(vec, x, y):
        vec[0] %= x
        vec[1] %= y
        return vec

    def ipow(vec, x, y):
        vec[0] **= x
        vec[1] **= y
        return vec


length_xy_vector2d = len_xy_vec2 = Vector2DXYMath.length
normalize_xy_vecto2d = norm_xy_vec2 = Vector2DXYMath.normalize
add_xy_vector2d = add_xy_vec2 = Vector2DXYMath.add
sub_xy_vector2d = sub_xy_vec2 = Vector2DXYMath.sub
mul_xy_vector2d = mul_xy_vec2 = Vector2DXYMath.mul
truediv_xy_vector2d = truediv_xy_vec2 = Vector2DXYMath.truediv
floordiv_xy_vector2d = floordiv_xy_vec2 = Vector2DXYMath.floordiv
mod_xy_vector2d = mod_xy_vec2 = Vector2DXYMath.mod
pow_xy_vector2d = pow_xy_vec2 = Vector2DXYMath.pow

iadd_xy_vector2d = iadd_xy_vec2 = Vector2DXYMath.iadd
isub_xy_vector2d = isub_xy_vec2 = Vector2DXYMath.isub
imul_xy_vector2d = imul_xy_vec2 = Vector2DXYMath.imul
itruediv_xy_vector2d = itruediv_xy_vec2 = Vector2DXYMath.itruediv
ifloordiv_xy_vector2d = ifloordiv_xy_vec2 = Vector2DXYMath.ifloordiv
imod_xy_vector2d = imod_xy_vec2 = Vector2DXYMath.imod
ipow_xy_vector2d = ipow_xy_vec2 = Vector2DXYMath.ipow


class Vector2DScalarMath:
    add = lambda vec, scalar: (
        vec[0] + scalar,
        vec[1] + scalar
        )
    sub = lambda vec, scalar: (
        vec[0] - scalar,
        vec[1] - scalar
        )
    mul = lambda vec, scalar: (
        vec[0] * scalar,
        vec[1] * scalar
        )
    truediv = lambda vec, scalar: (
        vec[0] / scalar,
        vec[1] / scalar
        )
    floordiv = lambda vec, scalar: (
        vec[0] // scalar,
        vec[1] // scalar
        )
    mod = lambda vec, scalar: (
        vec[0] % scalar,
        vec[1] % scalar
        )
    pow = lambda vec, scalar: (
        vec[0] ** scalar,
        vec[1] ** scalar
        )

    def iadd(vec, scalar):
        vec[0] += scalar
        vec[1] += scalar
        return vec

    def isub(vec, scalar):
        vec[0] -= scalar
        vec[1] -= scalar
        return vec

    def imul(vec, scalar):
        vec[0] *= scalar
        vec[1] *= scalar
        return vec

    def itruediv(vec, scalar):
        vec[0] /= scalar
        vec[1] /= scalar
        return vec

    def ifloordiv(vec, scalar):
        vec[0] //= scalar
        vec[1] //= scalar
        return vec

    def imod(vec, scalar):
        vec[0] %= scalar
        vec[1] %= scalar
        return vec

    def ipow(vec, scalar):
        vec[0] **= scalar
        vec[1] **= scalar
        return vec


add_scalar_vector2d = add_scl_vec2 = Vector2DScalarMath.add
sub_scalar_vector2d = sub_scl_vec2 = Vector2DScalarMath.sub
mul_scalar_vector2d = mul_scl_vec2 = Vector2DScalarMath.mul
truediv_scalar_vector2d = truediv_scl_vec2 = Vector2DScalarMath.truediv
floordiv_scalar_vector2d = floordiv_scl_vec2 = Vector2DScalarMath.floordiv
mod_scalar_vector2d = mod_scl_vec2 = Vector2DScalarMath.mod
pow_scalar_vector2d = pow_scl_vec2 = Vector2DScalarMath.pow

iadd_scalar_vector2d = iadd_scl_vec2 = Vector2DScalarMath.iadd
isub_scalar_vector2d = isub_scl_vec2 = Vector2DScalarMath.isub
imul_scalar_vector2d = imul_scl_vec2 = Vector2DScalarMath.imul
itruediv_scalar_vector2d = itruediv_scl_vec2 = Vector2DScalarMath.itruediv
ifloordiv_scalar_vector2d = ifloordiv_scl_vec2 = Vector2DScalarMath.ifloordiv
imod_scalar_vector2d = imod_scl_vec2 = Vector2DScalarMath.imod
ipow_scalar_vector2d = ipow_scl_vec2 = Vector2DScalarMath.ipow


class Vector2DVectorMath:
    dot = lambda vec, other: vec[0] * other[0] + vec[1] * other[1]

    length = lambda vec: (vec[0] ** 2 + vec[1] ** 2) ** 0.5
    def normalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2) ** 0.5
        return (
            vec[0] / vec_len,
            vec[1] / vec_len
            )
    add = lambda vec, other: (
        vec[0] + other[0],
        vec[1] + other[1]
        )
    sub = lambda vec, other: (
        vec[0] - other[0],
        vec[1] - other[1]
        )
    mul = lambda vec, other: (
        vec[0] * other[0],
        vec[1] * other[1]
        )
    truediv = lambda vec, other: (
        vec[0] / other[0],
        vec[1] / other[1]
        )
    floordiv = lambda vec, other: (
        vec[0] // other[0],
        vec[1] // other[1]
        )
    mod = lambda vec, other: (
        vec[0] % other[0],
        vec[1] % other[1]
        )
    pow = lambda vec, other: (
        vec[0] ** other[0],
        vec[1] ** other[1]
        )

    def inormalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2) ** 0.5
        vec[0] /= vec_len
        vec[1] /= vec_len
        return vec

    def iadd(vec, other):
        vec[0] += other[0]
        vec[1] += other[1]
        return vec

    def isub(vec, other):
        vec[0] -= other[0]
        vec[1] -= other[1]
        return vec

    def imul(vec, other):
        vec[0] *= other[0]
        vec[1] *= other[1]
        return vec

    def itruediv(vec, other):
        vec[0] /= other[0]
        vec[1] /= other[1]
        return vec

    def ifloordiv(vec, other):
        vec[0] //= other[0]
        vec[1] //= other[1]
        return vec

    def imod(vec, other):
        vec[0] %= other[0]
        vec[1] %= other[1]
        return vec

    def ipow(vec, other):
        vec[0] **= other[0]
        vec[1] **= other[1]
        return vec


dot_product_vector2d = dot_vec2 = Vector2DVectorMath.dot
length_vector2d = len_vec2 = Vector2DVectorMath.length
normalize_vector2d = norm_vec2 = Vector2DVectorMath.normalize
inormalize_vector2d = inorm_vec2 = Vector2DVectorMath.inormalize

add_vector_vector2d = add_vec_vec2 = Vector2DVectorMath.add
sub_vector_vector2d = sub_vec_vec2 = Vector2DVectorMath.sub
mul_vector_vector2d = mul_vec_vec2 = Vector2DVectorMath.mul
truediv_vector_vector2d = truediv_vec_vec2 = Vector2DVectorMath.truediv
floordiv_vector_vector2d = floordiv_vec_vec2 = Vector2DVectorMath.floordiv
mod_vector_vector2d = mod_vec_vec2 = Vector2DVectorMath.mod
pow_vector_vector2d = pow_vec_vec2 = Vector2DVectorMath.pow

iadd_vector_vector2d = iadd_vec_vec2 = Vector2DVectorMath.iadd
isub_vector_vector2d = isub_vec_vec2 = Vector2DVectorMath.isub
imul_vector_vector2d = imul_vec_vec2 = Vector2DVectorMath.imul
itruediv_vector_vector2d = itruediv_vec_vec2 = Vector2DVectorMath.itruediv
ifloordiv_vector_vector2d = ifloordiv_vec_vec2 = Vector2DVectorMath.ifloordiv
imod_vector_vector2d = imod_vec_vec2 = Vector2DVectorMath.imod
ipow_vector_vector2d = ipow_vec_vec2 = Vector2DVectorMath.ipow


class Vector2DMatrixMath:
    mul = lambda vec, mat: (
         vec[0] * mat[0][0] + vec[1] * mat[0][1],
         vec[0] * mat[1][0] + vec[1] * mat[1][1]
        )

    def imul(vec, mat):
        x = vec[0] * mat[0][0] + vec[1] * mat[0][1]
        y = vec[0] * mat[1][0] + vec[1] * mat[1][1]
        vec[0] = x
        vec[1] = y
        return vec


mul_matrix_vector2d = mul_mat_vec2 = Vector2DMatrixMath.mul
imul_matrix_vector2d = imul_mat_vec2 = Vector2DMatrixMath.imul
