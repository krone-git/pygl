from math import sin, cos, tan
from sys import maxsize
from random import random

from .vector import VectorFactory, VectorMath
from .matrix import MatrixMath, MatrixFactory


class Transform:
    def __init__(self, function, duration=None):
        self._active = True
        self._returns = MatrixFactory.identity()
        self._function = function
        self._duration = duration if duration != None else maxsize
        self._elapsed = 0.0

    is_active = lambda self: self._active
    def returns(self):
        return self._returns

    def activate(self):
        self._active = True
        return self

    def deactivate(self):
        self._active = False
        return self

    def set_elapsed(self, seconds):
        self._elapsed = seconds
        return self

    reset = lambda self: self.set_elapsed(0.0)

    def update(self, seconds):
        if self._active:
            self._elapsed += seconds

            elapsed = self._elapsed
            duration = self._duration
            finished = elapsed >= duration

            self._returns = self._function(
                seconds - (elapsed - duration) if finished else seconds,
                duration if finished else elapsed
                )

            if finished:
                self.deactivate()
        else:
            self._returns = MatrixFactory.identity()

        return self.returns()


class TransformMatrix:
    identity = MatrixFactory.identity
    x_reflection = lambda origin=0.0: [
        [-1.0, 0.0, 0.0, -(origin ** 2)],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]
    y_reflection = lambda origin=0.0: [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, -1.0, 0.0, -(origin ** 2)],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]
    z_reflection = lambda origin=0.0: [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, -1.0, -(origin ** 2)],
        [0.0, 0.0, 0.0, 1.0],
        ]

    def reflection(*axes, origin=(0.0, 0.0, 0.0)):
        matrix = MatrixFactory.identity()
        for axis in axes:
            matrix[axis][axis] = -1
            matrix[axis][3] = 2 * origin[axis]
        return matrix

    inversion = lambda origin=(0.0, 0.0, 0.0): [
        [-1.0, 0.0, 0.0, -(origin[0] ** 2)],
        [0.0, -1.0, 0.0, -(origin[1] ** 2)],
        [0.0, 0.0, -1.0, -(origin[2] ** 2)],
        [0.0, 0.0, 0.0, 1.0],
        ]


    def scale(x=1.0, y=1.0, z=1.0, origin=(0.0, 0.0, 0.0)):
        origin_x = origin[0]
        origin_y = origin[1]
        origin_z = origin[2]
        return [
            [x, 0.0, 0.0, -origin_x * x + origin_x],
            [0.0, y, 0.0, -origin_y * y + origin_y],
            [0.0, 0.0, z, -origin_z * z + origin_z],
            [0.0, 0.0, 0.0, 1.0],
            ]

    random_scale = lambda scale=1, function=(lambda: random() * 2 - 1): [
        [function() * scale, 0.0, 0.0, 0.0],
        [0.0, function() * scale, 0.0, 0.0],
        [0.0, 0.0, function() * scale, 0.0],
        [0.0, 0.0, 0.0, function() * scale],
        ]

    def x_rotation(degrees, origin=(0.0, 0.0, 0.0)):
        radians = degrees * 0.01745329252
        s = sin(radians)
        c = cos(radians)
        y = origin[1]
        z = origin[2]
        return [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, c, -s, -c * y + s * z + y],
            [0.0, s, c, -s * y - c * z + z],
            [0.0, 0.0, 0.0, 1.0],
            ]

    def y_rotation(degrees, origin=(0.0, 0.0, 0.0)):
        radians = degrees * 0.01745329252
        s = sin(radians)
        c = cos(radians)
        x = origin[0]
        z = origin[2]
        return [
            [c, 0.0, s, -c * x - s * z + x],
            [0.0, 1.0, 0.0, 0.0],
            [-s, 0.0, c, s * x - c * z + z],
            [0.0, 0.0, 0.0, 1.0],
            ]

    def z_rotation(degrees, origin=(0.0, 0.0, 0.0)):
        radians = degrees * 0.01745329252
        s = sin(radians)
        c = cos(radians)
        x = origin[0]
        y = origin[1]
        return [
            [c, -s, 0.0, -c * x + s * y + x],
            [s, c, 0.0, -s * x - c * y + y],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
            ]

    @classmethod
    def rotation(cls, x=0.0, y=0.0, z=0.0, origin=(0.0, 0.0, 0.0)):
        x *= 0.01745329252
        y *= 0.01745329252
        z *= 0.01745329252

        sin_x = sin(x)
        cos_x = cos(x)
        sin_y = sin(y)
        cos_y = cos(y)
        sin_z = sin(z)
        cos_z = cos(z)

        x = origin[0]
        y = origin[1]
        z = origin[2]

        a = cos_y * cos_z
        b = -cos_x * sin_z + cos_z * sin_x * sin_y
        c = sin_x * sin_z + cos_x * cos_z * sin_y
        d = cos_y * sin_z
        e = cos_x * cos_z + sin_x * sin_y * sin_z
        f = -cos_z * sin_x + cos_x * sin_y * sin_z
        g = -sin_y
        h = cos_y * sin_x
        i = cos_x * cos_y

        return [
            [a, b, c, -a * x - b * y - c * z + x],
            [d, e, f, -d * x - e * y - f * z + y],
            [g, h, i, -g * x - h * y - i * z + z],
            [0.0, 0.0, 0.0, 1.0],
            ]

    def directional_rotation(vector, target, axis=VectorFactory.jhat()):
        direction = VectorMath.normalize(
            VectorMath.sub_vector(target, vector)
            )
        dot = VectorMath.dot_product(axis, direction)
        y_axis = VectorMath.normalize(
            VectorMath.sub_vector(
                direction,
                VectorMath.mul_values(
                    direction, x=dot, y=dot, z=dot
                    )
                )
            )
        x_axis = VectorMath.normalize(
            VectorMath.cross_product(y_axis, direction)
            )
        return [
            [x_axis[0], x_axis[1], x_axis[2], 0.0],
            [y_axis[0], y_axis[1], y_axis[2], 0.0],
            [direction[0], direction[1], direction[2], 0.0],
            [0.0, 0.0, 0.0, 1.0],
            ]

    translation = lambda x=0.0, y=0.0, z=0.0: [
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, z],
        [0.0, 0.0, 0.0, 1.0],
        ]

    x_shear = lambda y=0.0, z=0.0: [
        [1.0, 0.0, 0.0, 0.0],
        [y, 1.0, 0.0, 0.0],
        [z, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]
    y_shear = lambda x=0.0, z=0.0: [
        [1.0, x, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, z, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]
    z_shear = lambda x=0.0, y=0.0: [
        [1.0, 0.0, x, 0.0],
        [0.0, 1.0, y, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]

    shear = lambda xy=0.0, xz=0.0, yx=0.0, yz=0.0, zx=0.0, zy=0.0: [
        [1.0, yx, zx, 0.0],
        [xy, 1.0, zy, 0.0],
        [xz, yz, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]

    def perspective(width, height, fov, znear, zfar):
        view_scale = 1 / tan(fov * 0.01745329252 / 2)
        z_scale = zfar / (zfar - znear)

        matrix = MatrixFactory.empty()
        matrix[0][0] = view_scale * height / width
        matrix[1][1] = view_scale
        matrix[2][2] = z_scale
        matrix[2][3] = 1.0
        matrix[3][2] = z_scale * -znear

        return matrix
