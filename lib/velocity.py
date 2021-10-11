from .vector import VectorFactory, VectorMath, VectorTransform
from .matrix import MatrixFactory
from .transform import TransformMatrix


class Velocity:
    def __init__(self, decay=(0.0, 0.0, 0.0), threshold=0.1,
                    transform_matrix=TransformMatrix.translation):
        self._direction = VectorFactory.empty()
        decay = list(decay) if len(decay) != 2 else list(decay + decay)[:3]
        self._decay = decay
        self._threshold = threshold

        self._matrix = MatrixFactory.identity()
        self._transform_matrix = transform_matrix

    direction = lambda self: self._direction
    decay = lambda self: self._decay
    threshold = lambda self: self._threshold
    matrix = lambda self: self._matrix

    length = lambda self: VectorMath.length(self._direction)

    def set(self, x=None, y=None, z=None):
        direction = self._direction
        if x != None:
            direction[0] = x
        if y != None:
            direction[1] = y
        if z != None:
            direction[2] = z
        return self

    def set_decay(self, x=None, y=None, z=None):
        if x != None:
            self._decay[0] = x
        if y != None:
            self._decay[1] = y
        if z != None:
            self._decay[2] = z
        return self

    def set_threshold(self, threshold):
        self._threshold = threshold
        return self

    reset = lambda self: self.set(0.0, 0.0, 0.0)

    def iadd(self, x=0.0, y=0.0, z=0.0):
        VectorMath.iadd_values(self._direction, x, y, z)
        return self

    def imul(self, x=1.0, y=1.0, z=1.0):
        VectorMath.imul_values(self._direction, x, y, z)
        return self

    def itransform(self, transform):
        VectorTransform.itransform(self._direction, transform)
        return self

    def itransforms(self, transforms):
        VectorTransform.itransforms(self._direction, transforms)
        return self

    def update(self, seconds, elapsed):
        direction = self._direction
        self._matrix = self._transform_matrix(
            direction[0] * seconds,
            direction[1] * seconds,
            direction[2] * seconds
            )
        threshold = self._threshold
        decay = self._decay
        x = direction[0]
        y = direction[1]
        z = direction[2]
        direction[0] = 0.0 if -threshold <= x <= threshold else x - x * decay[0] * seconds
        direction[1] = 0.0 if -threshold <= y <= threshold else y - y * decay[1] * seconds
        direction[2] = 0.0 if -threshold <= z <= threshold else z - z * decay[2] * seconds
        return self.matrix()


class VelocityTransform:
    def transform_vector(vector, velocity, seconds, elapsed):
        VectorMath.xmul_matrix(vector, velocity.update(seconds, elapsed))
        return MatrixFactory.identity()

    def itransform_vector(vector, velocity, seconds, elapsed):
        VectorMath.ximul_matrix(vector, velocity.update(seconds, elapsed))
        return MatrixFactory.identity()
