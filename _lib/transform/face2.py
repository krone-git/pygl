from ..vector.vector2.math import mul_mat_vec2, imul_mat_vec2


class Triangle2DTransform:
    transform = lambda tri, mat: [mul_mat_vec2(vec, mat) for vec in tri]
    def transforms(tri, mats):
        for mat in mats:
            tri = [mul_mat_vec2(vec, mat) for vec in tri]
        return tri
    itransform = lambda tri, mat: [imul_mat_vec2(vec, mat) for vec in tri]
    itransforms = lambda tri, mats: [
        imul_mat_vec2(vec, mat)
        for vec in tri
        for mat in mats
        ]
