from ..face.face3 import Face3D


class Shape:
    def __init__(self, faces=(), transforms=()):
        self._faces = set(faces)
        self._transforms = list(transforms)

    iter_faces = lambda self: iter(self._faces)
    transformed = lambda self: [face.transformed() for face in self._faces]

    def update(self, timedelay):
        matrices, depleted = set(), []
        for transform in self._transforms:
            matrix = transform(timedelay)
            if matrix is not None:
                matrices.add(matrix)
            else:
                depleted.append(transform)
        [self.remove_transforms(t) for t in depleted]

        [face.update(matrices) for face in self._faces]
        return self

    add_face = lambda self, face: self._faces.add(face)
    remove_face = lambda self, face: self._faces.discard(face)

    add_transform = lambda self, transform: self._transforms.append(transform)
    remove_transform = lambda self, transform: self._transforms.remove(transform)

    @classmethod
    def from_tris(cls, tris, **kwargs):
        return cls(faces=(Face3D(tri) for tri in tris), **kwargs)
