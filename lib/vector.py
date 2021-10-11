from random import random
from math import acos, atan2

from .matrix import MatrixMath


class VectorUtility:
    def clear(vector):
        vector[0] = 0.0
        vector[1] = 0.0
        vector[2] = 0.0
        vector[3] = 1.0
        return vector

    def set(vector, x=None, y=None, z=None):
        if x != None:
            vector[0] = x
        if y != None:
            vector[1] = y
        if z != None:
            vector[2] = z
        vector[3] = 1.0
        return vector


class VectorFactory:
    create = lambda x=0.0, y=0.0, z=0.0: [
        x / 1, y / 1, z / 1, 1.0,
        ]
    empty = lambda: [
        0.0, 0.0, 0.0, 1.0,
        ]
    random = lambda scale=1, function=(lambda: random() * 2 - 1): [
        function() * scale, function() * scale, function() * scale, 1.0
        ]
    def from_vector(vector):
        x, y, z = vector[:3]
        return [x / 1, y / 1, z / 1, 1.0]
    copy1 = lambda vector: [
        vector[0], vector[1], vector[2], 1.0,
        ]
    def copy2(vector):
        x, y, z, _ = vector
        return [x, y, z, 1.0]
    def copy3(vector):
        return [*vector[:3], 1.0]
    def copy4(vector):
        return vector[:3] + [1.0]
    copy5 = lambda vector: vector.copy()
    copy = copy5

    def icopy(vector, other):
        other[0] = vector[0]
        other[1] = vector[1]
        other[2] = vector[2]
        other[0] = 0.1
        return other

    origin = lambda: [0.0, 0.0, 0.0, 1.0]
    ihat = lambda: [1.0, 0.0, 0.0, 1.0]
    jhat = lambda: [0.0, 1.0, 0.0, 1.0]
    khat = lambda: [0.0, 0.0, 1.0, 1.0]

    ORIGIN = (0.0, 0.0, 0.0, 1.0)
    IHAT = (1.0, 0.0, 0.0, 1.0)
    JHAT = (0.0, 1.0, 0.0, 1.0)
    KHAT = (0.0, 0.0, 1.0, 1.0)


class VectorMath:
    length_values = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** 0.5
    def normalize_values(x, y, z):
        length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        length = 1.0 if length == 0 else length
        return [
            x / length,
            y / length,
            z / length,
            1.0
            ]

    dot_product_values1 = lambda vector, x, y, z: (
        vector[0] * x + vector[1] * y + vector[2] * z
        )
    def dot_product_values2(vector, x, y, z):
        vector_x, vector_y, vector_z, _ = vector
        return vector_x * x + vector_y * y + vector_z * z
        dot_product_values = dot_product_values2

    cross_product_values1 = lambda vector, x, y, z: [
        vector[1] * z - vector[2] * y,
        vector[2] * x - vector[0] * z,
        vector[0] * y - vector[1] * x,
        1.0
        ]
    def cross_product_values2(vector, x, y, z):
         vector_x, vector_y, vector_z, _ = vector
         return [
             vector_y * z - vector_z * y,
             vector_z * x - vector_x * z,
             vector_x * y - vector_y * x,
             1.0
             ]
    cross_product_values = cross_product_values2

    length1 = lambda vector: (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
    def length2(vector):
        x, y, z, _ = vector
        return (x ** 2 + y ** 2 + z ** 2) ** 0.5
    length = length1

    inverse1 = lambda vector: [
        vector[0] * -1, vector[1] * -1, vector[2] * -1, 1.0
        ]
    inverse2 = lambda vector: [
        -vector[0], -vector[1], -vector[2], 1.0
        ]
    def inverse3(vector):
        x, y, z, _ = vector
        return [x * -1, y * -1, z * -1, 1.0]
    def inverse4(vector):
        x, y, z, _ = vector
        return [-x, -y, -z, 1.0]
    inverse = inverse4

    def invert(vector):
        vector[0] *= -1
        vector[1] *= -1
        vector[2] *= -1
        return vector
    def normalize1(vector):
        length = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
        length = 1.0 if length == 0.0 else length
        return [
            vector[0] / length,
            vector[1] / length,
            vector[2] / length,
            1.0,
            ]
    def normalize2(vector):
        x, y, z, _ = vector
        length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        length = 1.0 if length == 0.0 else length
        return [
            x / length,
            y / length,
            z / length,
            1.0,
            ]
    normalize = normalize2

    def inormalize(vector):
        length = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
        length = 1.0 if length == 0.0 else length
        vector[0] /= length
        vector[1] /= length
        vector[2] /= length
        return vector
    round = lambda vector, ndigits=None: [
        round(vector[0], ndigits) / 1,
        round(vector[1], ndigits) / 1,
        round(vector[2], ndigits) / 1,
        1.0
        ]
    def iround(vector,ndigits=None):
        vector[0] = round(vector[0], ndigits) / 1
        vector[1] = round(vector[1], ndigits) / 1
        vector[2] = round(vector[2], ndigits) / 1
        return vector
    def floor(vector, ndigits=None):
        step = 1 / 10 ** ndigits if ndigits else 0
        return [
            vector[0] // step,
            vector[1] // step,
            vector[2] // step,
            1.0
            ]
    def ifloor(vector, ndigits=None):
        step = 1 / 10 ** ndigits if ndigits else 0
        vector[0] //= step
        vector[1] //= step
        vector[2] //= step
        return vector
    def ceiling(vector, ndigits=None):
        step = 1 / 10 ** ndigits if ndigits else 0
        return [
            vector[0] // step + step,
            vector[1] // step + step,
            vector[2] // step + step,
            1.0
            ]
    def iceiling(vector, ndigits=None):
        step = 1 / 10 ** ndigits if ndigits else 0
        vector[0] = vector[0] // step + step
        vector[1] = vector[1] // step + step
        vector[2] = vector[2] // step + step
        return vector


    def angle1(vector, other):
        dot = vector[0] * other[0] + vector[1] * other[1] + vector[2] * other[2]
        vector_length = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
        other_length = (other[0] ** 2 + other[1] ** 2 + other[2] ** 2) ** 0.5
        return acos(dot / (vector_length * other_length)) / 0.01745329252

    def angle2(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, __ = other
        dot = vector_x * other_x + vector_y * other_y + vector_z * other_z
        vector_length = (vector_x ** 2 + vector_y ** 2 + vector_z ** 2) ** 0.5
        other_length = (other_x ** 2 + other_y ** 2 + other_z ** 2) ** 0.5
        return acos(dot / (vector_length * other_length)) / 0.01745329252

    def unit_angles(vector):
        length = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
        return (
            acos(vector[0] / length) / 0.01745329252,
            acos(vector[1] / length) / 0.01745329252,
            acos(vector[2] / length) / 0.01745329252,
            )

    dot_product1 = lambda vector, other: (
        vector[0] * other[0] + vector[1] * other[1] + vector[2] * other[2]
        )
    def dot_product2(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, _ = other
        return (
            vector_x * other_x + vector_y * other_y + vector_z * other_z
            )
    dot_product = dot_product2

    cross_product1 = lambda vector, other: [
        vector[1] * other[2] - vector[2] * other[1],
        vector[2] * other[0] - vector[0] * other[2],
        vector[0] * other[1] - vector[1] * other[0],
        1.0
        ]
    def cross_product2(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, _ = other
        return [
            vector_y * other_z - vector_z * other_y,
            vector_z * other_x - vector_x * other_z,
            vector_x * other_y - vector_y * other_x,
            1.0
            ]
    cross_product = cross_product2

    def normal1(vector, other):
        normal = [
            vector[1] * other[2] - vector[2] * other[1],
            vector[2] * other[0] - vector[0] * other[2],
            vector[0] * other[1] - vector[1] * other[0],
            1.0
            ]
        length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
        length = length if length != 0.0 else 1.0
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal
    def normal2(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, __ = other
        normal = [
            vector_y * other_z - vector_z * other_y,
            vector_z * other_x - vector_x * other_z,
            vector_x * other_y - vector_y * other_x,
            1.0
            ]
        length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
        length = length if length != 0.0 else 1.0
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal
    def normal3(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, __ = other
        normal = [
            vector_y * other_z - vector_z * other_y,
            vector_z * other_x - vector_x * other_z,
            vector_x * other_y - vector_y * other_x,
            1.0
            ]
        x, y, z, ___ = normal
        length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        length = length if length != 0.0 else 1.0
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal
    normal = normal2

    def x_normal(vector):
        normal = [0.0, vector[2], -vector[1], 1.0]
        length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal

    def y_normal(vector):
        normal = [-vector[2], 0.0, vector[0], 1.0]
        length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal

    def z_normal(vector):
        normal = [vector[1], -vector[0], 0.0, 1.0]
        length = (normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2) ** 0.5
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length
        return normal

    project = lambda vector, plane: [
        0.0 if plane == 0 else vector[0],
        0.0 if plane == 1 else vector[1],
        0.0 if plane == 2 else vector[2],
        1.0
        ]

    add_values = lambda vector, x=0.0, y=0.0, z=0.0: [
        vector[0] + x,
        vector[1] + y,
        vector[2] + z,
        1.0,
        ]
    sub_values = lambda vector, x=0.0, y=0.0, z=0.0: [
        vector[0] - x,
        vector[1] - y,
        vector[2] - z,
        1.0,
        ]
    mul_values = lambda vector, x=1.0, y=1.0, z=1.0: [
        vector[0] * x,
        vector[1] * y,
        vector[2] * z,
        1.0,
        ]
    truediv_values = lambda vector, x=1.0, y=1.0, z=1.0: [
        vector[0] / x,
        vector[1] / y,
        vector[2] / z,
        1.0,
        ]

    def iadd_values(vector, x=0.0, y=0.0, z=0.0):
        vector[0] += x
        vector[1] += y
        vector[2] += z
        return vector

    def isub_values(vector, x=0.0, y=0.0, z=0.0):
        vector[0] -= x
        vector[1] -= y
        vector[2] -= z
        return vector

    def imul_values(vector, x=1.0, y=1.0, z=1.0):
        vector[0] *= x
        vector[1] *= y
        vector[2] *= z
        return vector

    def itruediv_values(vector, x=1.0, y=1.0, z=1.0):
        vector[0] /= x
        vector[1] /= y
        vector[2] /= z
        return vector

    add_value1 = lambda vector, value: [
        vector[0] + value,
        vector[1] + value,
        vector[2] + value,
        1.0,
        ]
    def add_value2(vector, value):
        x, y, z, _ = vector
        return [x + value, y + value, z + value, 1.0]
    add_value = add_value2

    sub_value = lambda vector, value: [
        vector[0] - value,
        vector[1] - value,
        vector[2] - value,
        1.0,
        ]
    mul_value = lambda vector, value: [
        vector[0] * value,
        vector[1] * value,
        vector[2] * value,
        1.0,
        ]
    truediv_value = lambda vector, value: [
        vector[0] / value,
        vector[1] / value,
        vector[2] / value,
        1.0,
        ]

    def iadd_value(vector, value):
        vector[0] += value
        vector[1] += value
        vector[2] += value
        return vector

    def isub_value(vector, value):
        vector[0] -= value
        vector[1] -= value
        vector[2] -= value
        return vector

    def imul_value(vector, value):
        vector[0] *= value
        vector[1] *= value
        vector[2] *= value
        return vector

    def itruediv_value(vector, value):
        vector[0] /= value
        vector[1] /= value
        vector[2] /= value
        return vector

    add_vector1 = lambda vector, other: [
        vector[0] + other[0],
        vector[1] + other[1],
        vector[2] + other[2],
        1.0,
        ]
    def add_vector2(vector, other):
        vector_x, vector_y, vector_z, _ = vector
        other_x, other_y, other_z, __ = other
        return [
            vector_x + other_x,
            vector_y + other_y,
            vector_z + other_z,
            1.0
            ]
    add_vector = add_vector2
    sub_vector = lambda vector, other: [
        vector[0] - other[0],
        vector[1] - other[1],
        vector[2] - other[2],
        1.0,
        ]
    mul_vector = lambda vector, other: [
        vector[0] * other[0],
        vector[1] * other[1],
        vector[2] * other[2],
        1.0,
        ]

    def iadd_vector1(vector, other):
        vector[0] += other[0]
        vector[1] += other[1]
        vector[2] += other[2]
        return vector
    def iadd_vector2(vector, other):
        other_x, other_y, other_z, _ = other
        vector[0] += other_x
        vector[1] += other_y
        vector[2] += other_z
        return vector
    iadd_vector = iadd_vector2

    def isub_vector(vector, other):
        vector[0] -= other[0]
        vector[1] -= other[1]
        vector[2] -= other[2]
        return vector

    def imul_vector(vector, other):
        vector[0] *= other[0]
        vector[1] *= other[1]
        vector[2] *= other[2]
        return vector

    mul_matrix = lambda vector, matrix: MatrixMath.mul_vector(matrix, vector)
    imul_matrix = lambda vector, matrix: MatrixMath.imul_vector(matrix, vector)
    xmul_matrix = lambda vector, matrix: MatrixMath.xmul_vector(matrix, vector)
    ximul_matrix = lambda vector, matrix: MatrixMath.ximul_vector(matrix, vector)


class VectorTransform:
    transform = VectorMath.xmul_matrix
    def transforms(vector, transforms):
        transformed = VectorFactory.copy(vector)
        [VectorMath.ximul_matrix(transformed, transform) for transform in transforms]
        return transformed

    itransform = VectorMath.ximul_matrix
    def itransforms(vector, transforms):
        [VectorMath.ximul_matrix(vector, transform) for transform in transforms]
        return vector
