from .face3 import Triangle3DTransform


class Shape3DTransform:
    transform = lambda shape, mat: [
        Triangle3DTransform.transform(tri, mat) for tri in shape
        ]
    transforms = lambda shape, mats: [
        Triangle3DTransform.transforms(tri, mats) for tri in shape
        ]
    transform = lambda shape, mat: [
        Triangle3DTransform.itransform(tri, mat) for tri in shape
        ]
    transforms = lambda shape, mats: [
        Triangle3DTransform.itransforms(tri, mats) for tri in shape
        ]
