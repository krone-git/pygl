

class Vector3DFactory:
    create = lambda x, y, z, w: [x + 0.0, y + 0.0, z + 0.0, w + 0.0]
    empty = lambda: [0.0, 0.0, 0.0, 0.0]
    copy = lambda vec: vec.copy()
    def icopy(vec, other):
        other[0] = vec[0]
        other[1] = vec[1]
        other[2] = vec[2]
        other[3] = vec[3]
        return other

    ihat = lambda: [1.0, 0.0, 0.0, 0.0]
    jhat = lambda: [0.0, 1.0, 0.0, 0.0]
    khat = lambda: [0.0, 0.0, 1.0, 0.0]
    lhat = lambda: [0.0, 0.0, 0.0, 1.0]


create_vector4d = create_vec4d = Vector4DFactory.create
empty_vector4d = empty_vec4d = Vector4DFactory.empty
copy_vector4d = copy_vec4 = Vector4DFactory.copy
icopy_vector4d = icopy_vec4 = Vector4DFactory.icopy

ihat_vector4d = ihat_vec4 = Vector4DFactory.ihat
jhat_vector4d = jhat_vec4 = Vector4DFactory.jhat
khat_vector4d = khat_vec4 = Vector4DFactory.khat
lhat_vector4d = lhat_vec4 = Vector4DFactory.lhat
