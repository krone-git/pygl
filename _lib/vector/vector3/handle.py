

class Vector3DHandler:
    def clear(vec):
        vec[0] = 0.0
        vec[1] = 0.0
        vec[2] = 0.0
        vec[3] = 1.0
        return vec


clear_vector3d = clear_vec3 = Vector3DHandler.clear
