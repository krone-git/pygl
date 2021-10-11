from .vector3 import Vector3DTransform


class Triangle3DTransform:
    transform = lambda tri, mat: [
        Vector3DTransform.xtransform(vec, mat) for vec in tri
        ]
    transforms = lambda tri, mats: [
        Vector3DTransform.xtransforms(vec, mats) for vec in tri
        ]
    itransform = lambda tri, mat: [
        Vector3DTransform.xitransform(vec, mat) for vec in tri
        ]
    itransforms = lambda tri, mats: [
        Vector3DTransform.xitransforms(vec, mats) for vec in tri
        ]
