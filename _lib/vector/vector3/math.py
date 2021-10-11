from numbers import Number


class Vector3DXYZMath:
    length = lambda x, y, z: (x **2 + y ** 2 + z ** 2) ** 0.5
    def normalize(x, y, z):
        vec_len = (x **2 + y ** 2 + z ** 2) ** 0.5
        return (
            x / vec_len,
            y / vec_len,
            z / vec_len
            )
    add = lambda vec, x, y, z: (
        vec[0] + x,
        vec[1] + y,
        vec[2] + z
        )
    sub = lambda vec, x, y, z: (
        vec[0] - x,
        vec[1] - y,
        vec[2] - z
        )
    mul = lambda vec, x, y, z: (
        vec[0] * x,
        vec[1] * y,
        vec[2] * z
        )
    truediv = lambda vec, x, y, z: (
        vec[0] / x,
        vec[1] / y,
        vec[2] / z
        )
    floordiv = lambda vec, x, y, z: (
        vec[0] // x,
        vec[1] // y,
        vec[2] // z
        )
    mod = lambda vec, x, y, z: (
        vec[0] % x,
        vec[1] % y,
        vec[2] % z
        )
    pow = lambda vec, x, y, z: (
        vec[0] ** x,
        vec[1] ** y,
        vec[2] ** z
        )

    def iadd(vec, x, y, z):
        vec[0] += x
        vec[1] += y
        vec[2] += z
        return vec

    def isub(vec, x, y, z):
        vec[0] -= x
        vec[1] -= y
        vec[2] -= z
        return vec

    def imul(vec, x, y, z):
        vec[0] *= x
        vec[1] *= y
        vec[2] *= z
        return vec

    def itruediv(vec, x, y, z):
        vec[0] /= x
        vec[1] /= y
        vec[2] /= z
        return vec

    def ifloordiv(vec, x, y, z):
        vec[0] //= x
        vec[1] //= y
        vec[2] //= z
        return vec

    def imod(vec, x, y, z):
        vec[0] %= x
        vec[1] %= y
        vec[2] %= z
        return vec

    def ipow(vec, x, y, z):
        vec[0] **= x
        vec[1] **= y
        vec[2] **= z
        return vec


length_xyz_vector3d = len_xyz_vec3 = Vector3DXYZMath.length
normalize_xyz_vector3d = norm_xyz_vec3 = Vector3DXYZMath.normalize
add_xyz_vector3d = add_xyz_vec3 = Vector3DXYZMath.add
sub_xyz_vector3d = sub_xyz_vec3 = Vector3DXYZMath.sub
mul_xyz_vector3d = mul_xyz_vec3 = Vector3DXYZMath.mul
truediv_xyz_vector3d = truediv_xyz_vec3 = Vector3DXYZMath.truediv
floordiv_xyz_vector3d = floordiv_xyz_vec3 = Vector3DXYZMath.floordiv
mod_xyz_vector3d = mod_xyz_vec3 = Vector3DXYZMath.mod
pow_xyz_vector3d = pow_xyz_vec3 = Vector3DXYZMath.pow

iadd_xyz_vector3d = iadd_xyz_vec3 = Vector3DXYZMath.iadd
isub_xyz_vector3d = isub_xyz_vec3 = Vector3DXYZMath.isub
imul_xyz_vector3d = imul_xyz_vec3 = Vector3DXYZMath.imul
itruediv_xyz_vector3d = itruediv_xyz_vec3 = Vector3DXYZMath.itruediv
ifloordiv_xyz_vector3d = ifloordiv_xyz_vec3 = Vector3DXYZMath.ifloordiv
imod_xyz_vector3d = imod_xyz_vec3 = Vector3DXYZMath.imod
ipow_xyz_vector3d = ipow_xyz_vec3 = Vector3DXYZMath.ipow


class Vector3DScalarMath:
    add = lambda vec, scalar: (
        vec[0] + scalar,
        vec[1] + scalar,
        vec[2] + scalar
        )
    sub = lambda vec, scalar: (
        vec[0] - scalar,
        vec[1] - scalar,
        vec[2] - scalar
        )
    mul = lambda vec, scalar: (
        vec[0] * scalar,
        vec[1] * scalar,
        vec[2] * scalar
        )
    truediv = lambda vec, scalar: (
        vec[0] / scalar,
        vec[1] / scalar,
        vec[2] / scalar
        )
    floordiv = lambda vec, scalar: (
        vec[0] // scalar,
        vec[1] // scalar,
        vec[2] // scalar
        )
    mod = lambda vec, scalar: (
        vec[0] % scalar,
        vec[1] % scalar,
        vec[2] % scalar
        )
    pow = lambda vec, scalar: (
        vec[0] ** scalar,
        vec[1] ** scalar,
        vec[2] ** scalar
        )

    def iadd(vec, scalar):
        vec[0] += scalar
        vec[1] += scalar
        vec[2] += scalar
        return vec

    def isub(vec, scalar):
        vec[0] -= scalar
        vec[1] -= scalar
        vec[2] -= scalar
        return vec

    def imul(vec, scalar):
        vec[0] *= scalar
        vec[1] *= scalar
        vec[2] *= scalar
        return vec

    def itruediv(vec, scalar):
        vec[0] /= scalar
        vec[1] /= scalar
        vec[2] /= scalar
        return vec

    def ifloordiv(vec, scalar):
        vec[0] //= scalar
        vec[1] //= scalar
        vec[2] //= scalar
        return vec

    def imod(vec, scalar):
        vec[0] %= scalar
        vec[1] %= scalar
        vec[2] %= scalar
        return vec

    def ipow(vec, scalar):
        vec[0] **= scalar
        vec[1] **= scalar
        vec[2] **= scalar
        return vec

add_scalar_vector3d = add_scl_vec3 = Vector3DScalarMath.add
sub_scalar_vector3d = sub_scl_vec3 = Vector3DScalarMath.sub
mul_scalar_vector3d = mul_scl_vec3 = Vector3DScalarMath.mul
truediv_scalar_vector3d = truediv_scl_vec3 = Vector3DScalarMath.truediv
floordiv_scalar_vector3d = floordiv_scl_vec3 = Vector3DScalarMath.floordiv
mod_scalar_vector3d = mod_scl_vec3 = Vector3DScalarMath.mod
pow_scalar_vector3d = pow_scl_vec3 = Vector3DScalarMath.pow

iadd_scalar_vector3d = iadd_scl_vec3 = Vector3DScalarMath.iadd
isub_scalar_vector3d = isub_scl_vec3 = Vector3DScalarMath.isub
imul_scalar_vector3d = imul_scl_vec3 = Vector3DScalarMath.imul
itruediv_scalar_vector3d = itruediv_scl_vec3 = Vector3DScalarMath.itruediv
ifloordiv_scalar_vector3d = ifloordiv_scl_vec3 = Vector3DScalarMath.ifloordiv
imod_scalar_vector3d = imod_scl_vec3 = Vector3DScalarMath.imod
ipow_scalar_vector3d = ipow_scl_vec3 = Vector3DScalarMath.ipow


class Vector3DVectorMath:
    dot = lambda vec, other: (
        vec[0] * other[0] + vec[1] * other[1] + vec[2] * other[2]
        )
    cross = lambda vec, other: (
        vec[1] * other[2] - vec[2] * other[1],
        vec[2] * other[0] - vec[0] * other[2],
        vec[0] * other[1] - vec[1] * other[0]
        )

    length = lambda vec: (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2) ** 0.5
    def normalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2) ** 0.5
        return (
            vec[0] / vec_len,
            vec[1] / vec_len,
            vec[2] / vec_len
            )
    add = lambda vec, other: (
        vec[0] + other[0],
        vec[1] + other[1],
        vec[2] + other[2]
        )
    sub = lambda vec, other: (
        vec[0] - other[0],
        vec[1] - other[1],
        vec[2] - other[2]
        )
    mul = lambda vec, other: (
        vec[0] * other[0],
        vec[1] * other[1],
        vec[2] * other[2]
        )
    truediv = lambda vec, other: (
        vec[0] / other[0],
        vec[1] / other[1],
        vec[2] / other[2]
        )
    floordiv = lambda vec, other: (
        vec[0] // other[0],
        vec[1] // other[1],
        vec[2] // other[2]
        )
    mod = lambda vec, other: (
        vec[0] % other[0],
        vec[1] % other[1],
        vec[2] % other[2]
        )
    pow = lambda vec, other: (
        vec[0] ** other[0],
        vec[1] ** other[1],
        vec[2] ** other[2]
        )

    def inormalize(vec):
        vec_len = (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2) ** 0.5
        vec[0] /= vec_len
        vec[1] /= vec_len
        vec[2] /= vec_len
        return vec

    def iadd(vec, other):
        vec[0] += other[0]
        vec[1] += other[1]
        vec[2] += other[2]
        return vec

    def isub(vec, other):
        vec[0] -= other[0]
        vec[1] -= other[1]
        vec[2] -= other[2]
        return vec

    def imul(vec, other):
        vec[0] *= other[0]
        vec[1] *= other[1]
        vec[2] *= other[2]
        return vec

    def itruediv(vec, other):
        vec[0] /= other[0]
        vec[1] /= other[1]
        vec[2] /= other[2]
        return vec

    def ifloordiv(vec, other):
        vec[0] //= other[0]
        vec[1] //= other[1]
        vec[2] //= other[2]
        return vec

    def imod(vec, other):
        vec[0] %= other[0]
        vec[1] %= other[1]
        vec[2] %= other[2]
        return vec

    def ipow(vec, other):
        vec[0] **= other[0]
        vec[1] **= other[1]
        vec[2] **= other[2]
        return vec


dot_product_vector3d = dot_vec3 = Vector3DVectorMath.dot
cross_product_vector3d = cross_vec3 = Vector3DVectorMath.cross
length_vector3d = len_vec3 = Vector3DVectorMath.length
normalize_vector3d = norm_vec3 = Vector3DVectorMath.normalize
inormalize_vector3d = inorm_vec3 = Vector3DVectorMath.inormalize

add_vector_vector3d = add_vec_vec3 = Vector3DVectorMath.add
sub_vector_vector3d = sub_vec_vec3 = Vector3DVectorMath.sub
mul_vector_vector3d = mul_vec_vec3 = Vector3DVectorMath.mul
truediv_vector_vector3d = truediv_vec_vec3 = Vector3DVectorMath.truediv
floordiv_vector_vector3d = floordiv_vec_vec3 = Vector3DVectorMath.floordiv
mod_vector_vector3d = mod_vec_vec3 = Vector3DVectorMath.mod
pow_vector_vector3d = pow_vec_vec3 = Vector3DVectorMath.pow

iadd_vector_vector3d = iadd_vec_vec3 = Vector3DVectorMath.iadd
isub_vector_vector3d = isub_vec_vec3 = Vector3DVectorMath.isub
imul_vector_vector3d = imul_vec_vec3 = Vector3DVectorMath.imul
itruediv_vector_vector3d = itruediv_vec_vec3 = Vector3DVectorMath.itruediv
ifloordiv_vector_vector3d = ifloordiv_vec_vec3 = Vector3DVectorMath.ifloordiv
imod_vector_vector3d = imod_vec_vec3 = Vector3DVectorMath.imod
ipow_vector_vector3d = ipow_vec_vec3 = Vector3DVectorMath.ipow


class Vector3DMatrixMath:
    mul = lambda vec, mat: (
         vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2],
         vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2],
         vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2]
        )

    def imul(vec, mat):
        x = vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2]
        y = vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2]
        z = vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2]
        vec[0] = x
        vec[1] = y
        vec[2] = z
        return vec

    def xmul(vec4, mat4):
        w = vec4[0] * mat4[3][0] + vec4[1] * mat4[3][1] + vec4[2] * mat4[3][2] + vec4[3] * mat4[3][3]
        w = 1.0 if w == 0.0 else w
        return (
            (vec4[0] * mat4[0][0] + vec4[1] * mat4[0][1] + vec4[2] * mat4[0][2] + vec4[3] * mat4[0][3]) / w,
            (vec4[0] * mat4[1][0] + vec4[1] * mat4[1][1] + vec4[2] * mat4[1][2] + vec4[3] * mat4[1][3]) / w,
            (vec4[0] * mat4[2][0] + vec4[1] * mat4[2][1] + vec4[2] * mat4[2][2] + vec4[3] * mat4[2][3]) / w,
            1.0
            )

    def ximul(vec4, mat4):
        w = vec4[0] * mat4[3][0] + vec4[1] * mat4[3][1] + vec4[2] * mat4[3][2] + vec4[3] * mat4[3][3]
        w = 1.0 if w == 0.0 else w

        x = (vec4[0] * mat4[0][0] + vec4[1] * mat4[0][1] + vec4[2] * mat4[0][2] + vec4[3] * mat4[0][3]) / w
        y = (vec4[0] * mat4[1][0] + vec4[1] * mat4[1][1] + vec4[2] * mat4[1][2] + vec4[3] * mat4[1][3]) / w
        z = (vec4[0] * mat4[2][0] + vec4[1] * mat4[2][1] + vec4[2] * mat4[2][2] + vec4[3] * mat4[2][3]) / w
        vec4[0] = x
        vec4[1] = y
        vec4[2] = z
        vec4[3] = 1.0
        return vec4


mul_matrix_vector3d = mul_mat_vec3 = Vector3DMatrixMath.mul
imul_matrix_vector3d = imul_mat_vec3 = Vector3DMatrixMath.imul
xmul_matrix_vector3d = xmul_mat_vec3 = Vector3DMatrixMath.xmul
ximul_matrix_vector3d = ximul_mat_vec3 = Vector3DMatrixMath.ximul
