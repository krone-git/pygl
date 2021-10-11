

class Vector3DFactory:
    create = lambda x, y, z: [x + 0.0, y + 0.0, z + 0.0]
    xcreate = lambda x, y, z: [x + 0.0, y + 0.0, z + 0.0, 1.0]

    empty = lambda: [0.0, 0.0, 0.0]
    xempty = lambda: [0.0, 0.0, 0.0, 1.0]

    copy = lambda vec: [vec[0] + 0.0, vec[1] + 0.0, vec[2] + 0.0]
    def icopy(vec, other):
        other[0] = vec[0]
        other[1] = vec[1]
        other[2] = vec[2]
        return other

    xcopy = lambda vec: [vec[0] + 0.0, vec[1] + 0.0, vec[2] + 0.0, 1.0]
    def xicopy(vec, other):
        other[0] = vec[0]
        other[1] = vec[1]
        other[2] = vec[2]
        other[3] = 1.0
        return other

    ihat = lambda: [1.0, 0.0, 0.0, 1.0]
    jhat = lambda: [0.0, 1.0, 0.0, 1.0]
    khat = lambda: [0.0, 0.0, 1.0, 1.0]


create_vector3d = create_vec3 = Vector3DFactory.create
xcreate_vector3d = xcreate_vec3 = Vector3DFactory.xcreate

empty_vector3d = empty_vec3 = Vector3DFactory.empty
xempty_vector3d = xempty_vec3 = Vector3DFactory.xempty

copy_vector3d = copy_vec3 = Vector3DFactory.copy
icopy_vector3d = icopy_vec3 = Vector3DFactory.icopy
xcopy_vector3d = xcopy_vec3 = Vector3DFactory.xcopy
xicopy_vector3d = xicopy_vec3 = Vector3DFactory.xicopy

ihat_vector3d = ihat_vec3 = Vector3DFactory.ihat
jhat_vector3d = jhat_vec3 = Vector3DFactory.jhat
khat_vector3d = khat_vec3 = Vector3DFactory.khat
