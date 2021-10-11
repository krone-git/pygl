from .vector import VectorFactory, VectorMath, VectorTransform
from .transform import TransformMatrix


class Vertex:
    def __init__(self, vector=(0.0, 0.0, 0.0)):
        self._vector = VectorFactory.empty()
        self._transform = TransformMatrix.translation_matrix(
            location[0], location[1], location[2]
            )

    vector = lambda self: self._vector

    def update(self):
        vector = self._vector
        VectorTransform.clear(vector)
        VectorMath.imul_matrix(vector, self._transform)
        return vector
