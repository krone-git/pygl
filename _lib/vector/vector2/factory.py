

class Vector2DFactory:
    create = lambda x, y: [x + 0.0, y + 0.0]
    empty = lambda: [0.0, 0.0]
    copy = lambda vec: vec.copy()
    def icopy(vec, other):
        other[0] = vec[0]
        other[1] = vec[1]
        return other

    ihat = lambda: [1.0, 0.0]
    jhat = lambda: [0.0, 1.0]

create_vector2d = create_vec2 = Vector2DFactory.create
empty_vector2d = empty_vec2 = Vector2DFactory.empty
copy_vector2d = copy_vec2 = Vector2DFactory.copy
icopy_vector2d = icopy_vec2 = Vector2DFactory.icopy

ihat_vector2d = ihat_vec2 = Vector2DFactory.ihat
jhat_vector2d = jhat_vec2 = Vector2DFactory.jhat
