from random import random
from copy import deepcopy


class MatrixUtility:
    def clear1(matrix):
        matrix[0][0] = 0.0
        matrix[0][1] = 0.0
        matrix[0][2] = 0.0
        matrix[0][3] = 0.0
        matrix[1][0] = 0.0
        matrix[1][1] = 0.0
        matrix[1][2] = 0.0
        matrix[1][3] = 0.0
        matrix[2][0] = 0.0
        matrix[2][1] = 0.0
        matrix[2][2] = 0.0
        matrix[2][3] = 0.0
        matrix[3][0] = 0.0
        matrix[3][1] = 0.0
        matrix[3][2] = 0.0
        matrix[3][3] = 0.0
        return matrix

    def clear2(matrix):
        row1, row2, row3, row4 = matrix
        row1[0] = 0.0
        row1[1] = 0.0
        row1[2] = 0.0
        row1[3] = 0.0
        row2[0] = 0.0
        row2[1] = 0.0
        row2[2] = 0.0
        row2[3] = 0.0
        row3[0] = 0.0
        row3[1] = 0.0
        row3[2] = 0.0
        row3[3] = 0.0
        row4[0] = 0.0
        row4[1] = 0.0
        row4[2] = 0.0
        row4[3] = 0.0
        return matrix
    clear = clear2

    def to_identity1(matrix):
        matrix[0][0] = 1.0
        matrix[0][1] = 0.0
        matrix[0][2] = 0.0
        matrix[0][3] = 0.0
        matrix[1][0] = 0.0
        matrix[1][1] = 1.0
        matrix[1][2] = 0.0
        matrix[1][3] = 0.0
        matrix[2][0] = 0.0
        matrix[2][1] = 0.0
        matrix[2][2] = 1.0
        matrix[2][3] = 0.0
        matrix[3][0] = 0.0
        matrix[3][1] = 0.0
        matrix[3][2] = 0.0
        matrix[3][3] = 1.0
        return matrix

    def to_identity2(matrix):
        row1, row2, row3, row4 = matrix
        row1[0] = 1.0
        row1[1] = 0.0
        row1[2] = 0.0
        row1[3] = 0.0
        row2[0] = 0.0
        row2[1] = 1.0
        row2[2] = 0.0
        row2[3] = 0.0
        row3[0] = 0.0
        row3[1] = 0.0
        row3[2] = 1.0
        row3[3] = 0.0
        row4[0] = 0.0
        row4[1] = 0.0
        row4[2] = 0.0
        row4[3] = 1.0
        return matrix
    to_identity = to_identity2

    def get_scale1(matrix):
        return (
            matrix[0][0],
            matrix[1][1],
            matrix[2][2],
        )

    def get_scale2(matrix):
        row1, row2, row3, _ = matrix
        return (
            row1[0],
            row2[1],
            row3[2],
        )
    get_scale = get_scale2

    def get_shear(matrix):
        return (
            matrix[0][1],
            matrix[0][2],
            matrix[1][0],
            matrix[1][2],
            matrix[2][0],
            matrix[2][1],
        )

    def get_translation(matrix):
        return (
            matrix[3][0],
            matrix[3][1],
            matrix[3][2],
            )

    def set_scale1(matrix, x=None, y=None, z=None):
        if x != None:
            matrix[0][0] = x
        if y != None:
            matrix[1][1] = y
        if z != None:
            matrix[2][2] = z
        return matrix

    def set_scale2(matrix, x=None, y=None, z=None):
        row1, row2, row3, _ = matrix
        if x != None:
            row1[0] = x
        if y != None:
            row2[1] = y
        if z != None:
            row3[2] = z
        return matrix
    set_scale = set_scale2

    def set_shear(matrix, xy=None, xz=None, yx=None, yz=None, zx=None, zy=None):
        if xy != None:
            matrix[0][1] = xy
        if xz != None:
            matrix[0][2] = xz
        if yx != None:
            matrix[1][0] = yx
        if yz != None:
            matrix[1][2] = yz
        if zx != None:
            matrix[2][0] = zx
        if zy != None:
            matrix[2][1] = zy
        return matrix

    def set_translation(matrix, x=None, y=None, z=None):
        if x != None:
            matrix[3][0] = x
        if y != None:
            matrix[3][1] = y
        if z != None:
            matrix[3][2] = z
        return matrix

    def clear_scale(matrix):
        matrix[0][0] = 1.0
        matrix[1][1] = 1.0
        matrix[2][2] = 1.0
        matrix[3][3] = 1.0
        return matrix

    def clear_shear(matrix):
        matrix[0][1] = 0.0
        matrix[0][2] = 0.0
        matrix[1][0] = 0.0
        matrix[1][2] = 0.0
        matrix[2][0] = 0.0
        matrix[2][1] = 0.0
        return matrix

    def clear_translation(matrix):
        matrix[3][0] = 0.0
        matrix[3][1] = 0.0
        matrix[3][2] = 0.0
        return matrix


class MatrixFactory:
    IDENTITY = (
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0)
        )
    empty = lambda: [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        ]
    identity = lambda: [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        ]

    random = lambda scale=1, function=random: [
        [function() * scale, function() * scale, function() * scale, function() * scale],
        [function() * scale, function() * scale, function() * scale, function() * scale],
        [function() * scale, function() * scale, function() * scale, function() * scale],
        [function() * scale, function() * scale, function() * scale, function() * scale],
        ]

    copy1 = lambda matrix: [
        [matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]],
        [matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3]],
        [matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3]],
        [matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3]],
        ]

    def copy2(matrix):
        row1, row2, row3, row4 = matrix
        return [
            [row1[0], row1[1], row1[2], row1[3]],
            [row2[0], row2[1], row2[2], row2[3]],
            [row3[0], row3[1], row3[2], row3[3]],
            [row4[0], row4[1], row4[2], row4[3]],
            ]

    def copy3(matrix):
        row1, row2, row3, row4 = matrix
        return [
            [*row1], [*row2], [*row3], [*row4],
            ]

    def copy4(matrix):
        row1, row2, row3, row4 = matrix
        return [
            row1.copy(), row2.copy(), row3.copy(), row4.copy(),
            ]

    copy5 = lambda matrix: deepcopy(matrix)
    def copy5_(matrix):
        return deepcopy(matrix)
    copy = copy3


    def icopy(matrix, other):
        other[0][0] = matrix[0][0]
        other[0][1] = matrix[0][1]
        other[0][2] = matrix[0][2]
        other[0][3] = matrix[0][3]
        other[1][0] = matrix[1][0]
        other[1][1] = matrix[1][1]
        other[1][2] = matrix[1][2]
        other[1][3] = matrix[1][3]
        other[2][0] = matrix[2][0]
        other[2][1] = matrix[2][1]
        other[2][2] = matrix[2][2]
        other[2][3] = matrix[2][3]
        other[3][0] = matrix[3][0]
        other[3][1] = matrix[3][1]
        other[3][2] = matrix[3][2]
        other[3][3] = matrix[3][3]
        return other


class MatrixMath:
    def determinant1(matrix):
        d1 = matrix[1][1] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) \
            - matrix[1][2] * (matrix[2][3] * matrix[3][1] - matrix[2][1] * matrix[3][3]) \
            + matrix[1][3] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1])

        d2 = matrix[1][0] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) \
            - matrix[1][2] * (matrix[2][3] * matrix[3][0] - matrix[2][0] * matrix[3][3]) \
            + matrix[1][3] * (matrix[2][0] * matrix[3][2] - matrix[2][2] * matrix[3][0])

        d3 = matrix[1][0] * (matrix[2][1] * matrix[3][3] - matrix[2][3] * matrix[3][1]) \
            - matrix[1][1] * (matrix[2][3] * matrix[3][0] - matrix[2][0] * matrix[3][3]) \
            + matrix[1][3] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])

        d4 = matrix[1][0] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1]) \
            - matrix[1][1] * (matrix[2][2] * matrix[3][0] - matrix[2][0] * matrix[3][2]) \
            + matrix[1][2] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])

        return matrix[0][0] * d1 - matrix[0][1] * d2 + matrix[0][2] * d3 - matrix[0][3] * d4

    def determinant2(matrix):
        row1, row2, row3, row4 = matrix
        a, b, c, d = row1
        e, f, g, h = row2
        i, j, k, l = row3
        m, n, o, p = row4

        d1 = f * (k * p - l * o) - g * (l * n - j * p) + h * (j * o - k * n)
        d2 = e * (k * p - l * o) - g * (l * m - i * p) + h * (i * o - k * m)
        d3 = e * (j * p - l * n) - f * (l * m - i * p) + h * (i * n - j * m)
        d4 = e * (j * o - k * n) - f * (k * m - i * o) + g * (i * n - j * m)

        return a * d1 - b * d2 + c * d3 - d * d4

    def determinant3(matrix):
        row1, row2, row3, row4 = matrix
        e, f, g, h = row2
        i, j, k, l = row3
        m, n, o, p = row4

        d1 = f * (k * p - l * o) - g * (l * n - j * p) + h * (j * o - k * n)
        d2 = e * (k * p - l * o) - g * (l * m - i * p) + h * (i * o - k * m)
        d3 = e * (j * p - l * n) - f * (l * m - i * p) + h * (i * n - j * m)
        d4 = e * (j * o - k * n) - f * (k * m - i * o) + g * (i * n - j * m)

        return row1[0] * d1 - row1[1] * d2 + row1[2] * d3 - row1[3] * d4

    def determinant4(matrix):
        a, b, c, d = matrix[0]
        e, f, g, h = matrix[1]
        i, j, k, l = matrix[2]
        m, n, o, p = matrix[3]

        d1 = f * (k * p - l * o) - g * (l * n - j * p) + h * (j * o - k * n)
        d2 = e * (k * p - l * o) - g * (l * m - i * p) + h * (i * o - k * m)
        d3 = e * (j * p - l * n) - f * (l * m - i * p) + h * (i * n - j * m)
        d4 = e * (j * o - k * n) - f * (k * m - i * o) + g * (i * n - j * m)

        return a * d1 - b * d2 + c * d3 - d * d4

    def determinant5(matrix):
        row1 = matrix[0]
        e, f, g, h = matrix[1]
        i, j, k, l = matrix[2]
        m, n, o, p = matrix[3]

        d1 = f * (k * p - l * o) - g * (l * n - j * p) + h * (j * o - k * n)
        d2 = e * (k * p - l * o) - g * (l * m - i * p) + h * (i * o - k * m)
        d3 = e * (j * p - l * n) - f * (l * m - i * p) + h * (i * n - j * m)
        d4 = e * (j * o - k * n) - f * (k * m - i * o) + g * (i * n - j * m)

        return row1[0] * d1 - row1[1] * d2 + row1[2] * d3 - row1[3] * d4

    def determinant6(matrix):
        e, f, g, h = matrix[1]
        i, j, k, l = matrix[2]
        m, n, o, p = matrix[3]

        d1 = f * (k * p - l * o) - g * (l * n - j * p) + h * (j * o - k * n)
        d2 = e * (k * p - l * o) - g * (l * m - i * p) + h * (i * o - k * m)
        d3 = e * (j * p - l * n) - f * (l * m - i * p) + h * (i * n - j * m)
        d4 = e * (j * o - k * n) - f * (k * m - i * o) + g * (i * n - j * m)

        return matrix[0][0] * d1 - matrix[0][1] * d2 + matrix[0][2] * d3 - matrix[0][3] * d4
    determinant = determinant3

    mul_matrix1 = lambda matrix, other: [
        [
            matrix[0][0] * other[0][0] + matrix[0][1] * other[1][0] + matrix[0][2] * other[2][0] + matrix[0][3] * other[3][0],
            matrix[0][0] * other[0][1] + matrix[0][1] * other[1][1] + matrix[0][2] * other[2][1] + matrix[0][3] * other[3][1],
            matrix[0][0] * other[0][2] + matrix[0][1] * other[1][2] + matrix[0][2] * other[2][2] + matrix[0][3] * other[3][2],
            matrix[0][0] * other[0][3] + matrix[0][1] * other[1][3] + matrix[0][2] * other[2][3] + matrix[0][3] * other[3][3],
            ],
        [
            matrix[1][0] * other[0][0] + matrix[1][1] * other[1][0] + matrix[1][2] * other[2][0] + matrix[1][3] * other[3][0],
            matrix[1][0] * other[0][1] + matrix[1][1] * other[1][1] + matrix[1][2] * other[2][1] + matrix[1][3] * other[3][1],
            matrix[1][0] * other[0][2] + matrix[1][1] * other[1][2] + matrix[1][2] * other[2][2] + matrix[1][3] * other[3][2],
            matrix[1][0] * other[0][3] + matrix[1][1] * other[1][3] + matrix[1][2] * other[2][3] + matrix[1][3] * other[3][3],
            ],
        [
            matrix[2][0] * other[0][0] + matrix[2][1] * other[1][0] + matrix[2][2] * other[2][0] + matrix[2][3] * other[3][0],
            matrix[2][0] * other[0][1] + matrix[2][1] * other[1][1] + matrix[2][2] * other[2][1] + matrix[2][3] * other[3][1],
            matrix[2][0] * other[0][2] + matrix[2][1] * other[1][2] + matrix[2][2] * other[2][2] + matrix[2][3] * other[3][2],
            matrix[2][0] * other[0][3] + matrix[2][1] * other[1][3] + matrix[2][2] * other[2][3] + matrix[2][3] * other[3][3],
            ],
        [
            matrix[3][0] * other[0][0] + matrix[3][1] * other[1][0] + matrix[3][2] * other[2][0] + matrix[3][3] * other[3][0],
            matrix[3][0] * other[0][1] + matrix[3][1] * other[1][1] + matrix[3][2] * other[2][1] + matrix[3][3] * other[3][1],
            matrix[3][0] * other[0][2] + matrix[3][1] * other[1][2] + matrix[3][2] * other[2][2] + matrix[3][3] * other[3][2],
            matrix[3][0] * other[0][3] + matrix[3][1] * other[1][3] + matrix[3][2] * other[2][3] + matrix[3][3] * other[3][3],
            ],
        ]

    def mul_matrix2(matrix, other):
        a1 = matrix[0][0]
        a2 = other[0][0]
        b1 = matrix[0][1]
        b2 = other[0][1]
        c1 = matrix[0][2]
        c2 = other[0][2]
        d1 = matrix[0][3]
        d2 = other[0][3]
        e1 = matrix[1][0]
        e2 = other[1][0]
        f1 = matrix[1][1]
        f2 = other[1][1]
        g1 = matrix[1][2]
        g2 = other[1][2]
        h1 = matrix[1][3]
        h2 = other[1][3]
        i1 = matrix[2][0]
        i2 = other[2][0]
        j1 = matrix[2][1]
        j2 = other[2][1]
        k1 = matrix[2][2]
        k2 = other[2][2]
        l1 = matrix[2][3]
        l2 = other[2][3]
        m1 = matrix[3][0]
        m2 = other[3][0]
        n1 = matrix[3][1]
        n2 = other[3][1]
        o1 = matrix[3][2]
        o2 = other[3][2]
        p1 = matrix[3][3]
        p2 = other[3][3]
        return [
            [a1 * a2 + b1 * e2 + c1 * i2 + d1 * m2,
            a1 * b2 + b1 * f2 + c1 * j2 + d1 * n2,
            a1 * c2 + b1 * g2 + c1 * k2 + d1 * o2,
            a1 * d2 + b1 * h2 + c1 * l2 + d1 * p2,],
            [e1 * a2 + f1 * e2 + g1 * i2 + h1 * m2,
            e1 * b2 + f1 * f2 + g1 * j2 + h1 * n2,
            e1 * c2 + f1 * g2 + g1 * k2 + h1 * o2,
            e1 * d2 + f1 * h2 + g1 * l2 + h1 * p2,],
            [i1 * a2 + j1 * e2 + k1 * i2 + l1 * m2,
            i1 * b2 + j1 * f2 + k1 * j2 + l1 * n2,
            i1 * c2 + j1 * g2 + k1 * k2 + l1 * o2,
            i1 * d2 + j1 * h2 + k1 * l2 + l1 * p2,],
            [m1 * a2 + n1 * e2 + o1 * i2 + p1 * m2,
            m1 * b2 + n1 * f2 + o1 * j2 + p1 * n2,
            m1 * c2 + n1 * g2 + o1 * k2 + p1 * o2,
            m1 * d2 + n1 * h2 + o1 * l2 + p1 * p2,]
            ]

    def mul_matrix3(matrix, other):
        a1, b1, c1, d1 = matrix[0]
        a2, b2, c2, d2 = other[0]
        e1, f1, g1, h1 = matrix[1]
        e2, f2, g2, h2 = other[1]
        i1, j1, k1, l1 = matrix[2]
        i2, j2, k2, l2 = other[2]
        m1, n1, o1, p1 = matrix[3]
        m2, n2, o2, p2 = other[3]
        return [
            [a1 * a2 + b1 * e2 + c1 * i2 + d1 * m2,
            a1 * b2 + b1 * f2 + c1 * j2 + d1 * n2,
            a1 * c2 + b1 * g2 + c1 * k2 + d1 * o2,
            a1 * d2 + b1 * h2 + c1 * l2 + d1 * p2,],
            [e1 * a2 + f1 * e2 + g1 * i2 + h1 * m2,
            e1 * b2 + f1 * f2 + g1 * j2 + h1 * n2,
            e1 * c2 + f1 * g2 + g1 * k2 + h1 * o2,
            e1 * d2 + f1 * h2 + g1 * l2 + h1 * p2,],
            [i1 * a2 + j1 * e2 + k1 * i2 + l1 * m2,
            i1 * b2 + j1 * f2 + k1 * j2 + l1 * n2,
            i1 * c2 + j1 * g2 + k1 * k2 + l1 * o2,
            i1 * d2 + j1 * h2 + k1 * l2 + l1 * p2,],
            [m1 * a2 + n1 * e2 + o1 * i2 + p1 * m2,
            m1 * b2 + n1 * f2 + o1 * j2 + p1 * n2,
            m1 * c2 + n1 * g2 + o1 * k2 + p1 * o2,
            m1 * d2 + n1 * h2 + o1 * l2 + p1 * p2,]
            ]

    def mul_matrix4(matrix, other):
        matrix_row1, matrix_row2, matrix_row3, matrix_row4 = matrix
        other_row1, other_row2, other_row3, other_row4 = other
        a1, b1, c1, d1 = matrix_row1
        a2, b2, c2, d2 = other_row1
        e1, f1, g1, h1 = matrix_row2
        e2, f2, g2, h2 = other_row2
        i1, j1, k1, l1 = matrix_row3
        i2, j2, k2, l2 = other_row3
        m1, n1, o1, p1 = matrix_row4
        m2, n2, o2, p2 = other_row4
        return [
            [a1 * a2 + b1 * e2 + c1 * i2 + d1 * m2,
            a1 * b2 + b1 * f2 + c1 * j2 + d1 * n2,
            a1 * c2 + b1 * g2 + c1 * k2 + d1 * o2,
            a1 * d2 + b1 * h2 + c1 * l2 + d1 * p2,],
            [e1 * a2 + f1 * e2 + g1 * i2 + h1 * m2,
            e1 * b2 + f1 * f2 + g1 * j2 + h1 * n2,
            e1 * c2 + f1 * g2 + g1 * k2 + h1 * o2,
            e1 * d2 + f1 * h2 + g1 * l2 + h1 * p2,],
            [i1 * a2 + j1 * e2 + k1 * i2 + l1 * m2,
            i1 * b2 + j1 * f2 + k1 * j2 + l1 * n2,
            i1 * c2 + j1 * g2 + k1 * k2 + l1 * o2,
            i1 * d2 + j1 * h2 + k1 * l2 + l1 * p2,],
            [m1 * a2 + n1 * e2 + o1 * i2 + p1 * m2,
            m1 * b2 + n1 * f2 + o1 * j2 + p1 * n2,
            m1 * c2 + n1 * g2 + o1 * k2 + p1 * o2,
            m1 * d2 + n1 * h2 + o1 * l2 + p1 * p2,]
            ]
    mul_matrix = mul_matrix4

    def imul_matrix(matrix, other):
        x1 = matrix[0][0] * other[0][0] + matrix[0][1] * other[1][0] + matrix[0][2] * other[2][0] + matrix[0][3] * other[3][0]
        y1 = matrix[0][0] * other[0][1] + matrix[0][1] * other[1][1] + matrix[0][2] * other[2][1] + matrix[0][3] * other[3][1]
        z1 = matrix[0][0] * other[0][2] + matrix[0][1] * other[1][2] + matrix[0][2] * other[2][2] + matrix[0][3] * other[3][2]
        w1 = matrix[0][0] * other[0][3] + matrix[0][1] * other[1][3] + matrix[0][2] * other[2][3] + matrix[0][3] * other[3][3]
        x2 = matrix[1][0] * other[0][0] + matrix[1][1] * other[1][0] + matrix[1][2] * other[2][0] + matrix[1][3] * other[3][0]
        y2 = matrix[1][0] * other[0][1] + matrix[1][1] * other[1][1] + matrix[1][2] * other[2][1] + matrix[1][3] * other[3][1]
        z2 = matrix[1][0] * other[0][2] + matrix[1][1] * other[1][2] + matrix[1][2] * other[2][2] + matrix[1][3] * other[3][2]
        w2 = matrix[1][0] * other[0][3] + matrix[1][1] * other[1][3] + matrix[1][2] * other[2][3] + matrix[1][3] * other[3][3]
        x3 = matrix[2][0] * other[0][0] + matrix[2][1] * other[1][0] + matrix[2][2] * other[2][0] + matrix[2][3] * other[3][0]
        y3 = matrix[2][0] * other[0][1] + matrix[2][1] * other[1][1] + matrix[2][2] * other[2][1] + matrix[2][3] * other[3][1]
        z3 = matrix[2][0] * other[0][2] + matrix[2][1] * other[1][2] + matrix[2][2] * other[2][2] + matrix[2][3] * other[3][2]
        w3 = matrix[2][0] * other[0][3] + matrix[2][1] * other[1][3] + matrix[2][2] * other[2][3] + matrix[2][3] * other[3][3]
        x4 = matrix[3][0] * other[0][0] + matrix[3][1] * other[1][0] + matrix[3][2] * other[2][0] + matrix[3][3] * other[3][0]
        y4 = matrix[3][0] * other[0][1] + matrix[3][1] * other[1][1] + matrix[3][2] * other[2][1] + matrix[3][3] * other[3][1]
        z4 = matrix[3][0] * other[0][2] + matrix[3][1] * other[1][2] + matrix[3][2] * other[2][2] + matrix[3][3] * other[3][2]
        w4 = matrix[3][0] * other[0][3] + matrix[3][1] * other[1][3] + matrix[3][2] * other[2][3] + matrix[3][3] * other[3][3]

        matrix[0][0] = x1
        matrix[0][1] = y1
        matrix[0][2] = z1
        matrix[0][3] = w1
        matrix[1][0] = x2
        matrix[1][1] = y2
        matrix[1][2] = z2
        matrix[1][3] = w2
        matrix[2][0] = x3
        matrix[2][1] = y3
        matrix[2][2] = z3
        matrix[2][3] = w3
        matrix[3][0] = x4
        matrix[3][1] = y4
        matrix[3][2] = z4
        matrix[3][3] = w4
        return matrix

    mul_vector1 = lambda matrix, vector: [
        vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2] + vector[3] * matrix[0][3],
        vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2] + vector[3] * matrix[1][3],
        vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2] + vector[3] * matrix[2][3],
        vector[0] * matrix[3][0] + vector[1] * matrix[3][1] + vector[2] * matrix[3][2] + vector[3] * matrix[3][3],
        ]

    def mul_vector2(matrix, vector):
        row1, row2, row3, row4 = matrix
        a, b, c, d = row1
        e, f, g, h = row2
        i, j, k, l = row3
        m, n, o, p = row4

        x, y, z, w = vector
        return [
            x * a + y * b + z * c + w * d,
            x * e + y * f + z * g + w * h,
            x * i + y * j + z * k + w * l,
            x * m + y * n + z * o + w * p,
            ]
    mul_vector = mul_vector2

    def imul_vector(matrix, vector):
        x = vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2] + vector[3] * matrix[0][3]
        y = vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2] + vector[3] * matrix[1][3]
        z = vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2] + vector[3] * matrix[2][3]
        w = vector[0] * matrix[3][0] + vector[1] * matrix[3][1] + vector[2] * matrix[3][2] + vector[3] * matrix[3][3]
        vector[0] = x
        vector[1] = y
        vector[2] = z
        vector[3] = w
        return vector

    mul_values = lambda matrix, x, y, z: [
        x * matrix[0][0] + y * matrix[0][1] + z * matrix[0][2],
        x * matrix[1][0] + y * matrix[1][1] + z * matrix[1][2],
        x * matrix[2][0] + y * matrix[2][1] + z * matrix[2][2],
        1.0,
        ]

    def xmul_vector1(matrix, vector):
        w = vector[0] * matrix[3][0] + vector[1] * matrix[3][1] + vector[2] * matrix[3][2] + vector[3] * matrix[3][3]
        w = 1.0 if w == 0 else w
        return [
            (vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2] + vector[3] * matrix[0][3]) / w,
            (vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2] + vector[3] * matrix[1][3]) / w,
            (vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2] + vector[3] * matrix[2][3]) / w,
            1.0
            ]

    def xmul_vector2(matrix, vector):
        row1, row2, row3, row4 = matrix
        a, b, c, d = row1
        e, f, g, h = row2
        i, j, k, l = row3
        m, n, o, p = row4
        x, y, z, w = vector

        w = x * m + y * n + z * o + w * p
        w = 1.0 if w == 0 else w
        return [
            (x * a + y * b + z * c + w * d) / w,
            (x * e + y * f + z * g + w * h) / w,
            (x * i + y * j + z * k + w * l) / w,
            1.0
            ]
    xmul_vector = xmul_vector2

    def ximul_vector(matrix, vector):
        w = vector[0] * matrix[3][0] + vector[1] * matrix[3][1] + vector[2] * matrix[3][2] + vector[3] * matrix[3][3]
        w = 1.0 if w == 0.0 else w

        x = (vector[0] * matrix[0][0] + vector[1] * matrix[0][1] + vector[2] * matrix[0][2] + vector[3] * matrix[0][3]) / w
        y = (vector[0] * matrix[1][0] + vector[1] * matrix[1][1] + vector[2] * matrix[1][2] + vector[3] * matrix[1][3]) / w
        z = (vector[0] * matrix[2][0] + vector[1] * matrix[2][1] + vector[2] * matrix[2][2] + vector[3] * matrix[2][3]) / w
        vector[0] = x
        vector[1] = y
        vector[2] = z
        vector[3] = 1.0
        return vector

    def xmul_values(matrix, x, y, z):
        w = x * matrix[3][0] + y * matrix[3][1] + z * matrix[3][2] + 1.0 * matrix[3][3]
        w = 1.0 if w == 0.0 else w
        return [
            (x * matrix[0][0] + y * matrix[0][1] + z * matrix[0][2] + 1.0 * matrix[0][3]) / w,
            (x * matrix[1][0] + y * matrix[1][1] + z * matrix[1][2] + 1.0 * matrix[1][3]) / w,
            (x * matrix[2][0] + y * matrix[2][1] + z * matrix[2][2] + 1.0 * matrix[2][3]) / w,
            1.0
            ]

    def inverse(matrix):
        x1 = matrix[0][0]
        y1 = matrix[1][0]
        z1 = matrix[2][0]
        w1 = matrix[3][0]
        x2 = matrix[0][1]
        y2 = matrix[1][1]
        z2 = matrix[2][1]
        w2 = matrix[3][1]
        x3 = matrix[0][2]
        y3 = matrix[1][2]
        z3 = matrix[2][2]
        w3 = matrix[3][2]

        d1 = w1 * x1 + w2 * x2 + w3 * x3
        d2 = w1 * y1 + w2 * y2 + w3 * y3
        d3 = w1 * z1 + w2 * z2 + w3 * z3

        return [
            [x1, y1, z1, 0.0],
            [x2, y2, z2, 0.0],
            [x3, y3, z3, 0.0],
            [-d1, -d2, -d3, 1.0],
            ]


    def invert(matrix):
        x1 = matrix[0][0]
        y1 = matrix[1][0]
        z1 = matrix[2][0]
        w1 = matrix[3][0]
        x2 = matrix[0][1]
        y2 = matrix[1][1]
        z2 = matrix[2][1]
        w2 = matrix[3][1]
        x3 = matrix[0][2]
        y3 = matrix[1][2]
        z3 = matrix[2][2]
        w3 = matrix[3][2]

        d1 = w1 * x1 + w2 * x2 + w3 * x3
        d2 = w1 * y1 + w2 * y2 + w3 * y3
        d3 = w1 * z1 + w2 * z2 + w3 * z3

        matrix[0][0] = x1
        matrix[0][1] = y1
        matrix[0][2] = z1
        matrix[0][3] = 0.0
        matrix[1][0] = x2
        matrix[1][1] = y2
        matrix[1][2] = z2
        matrix[1][3] = 0.0
        matrix[2][0] = x3
        matrix[2][1] = y3
        matrix[2][2] = z3
        matrix[2][3] = 0.0
        matrix[3][0] = -d1
        matrix[3][1] = -d2
        matrix[3][2] = -d3
        matrix[3][3] = 1.0

        return matrix


class MatrixTransform:
    transform = MatrixMath.mul_matrix
    def transforms(matrix, transforms):
        transformed = MatrixFactory.copy(matrix)
        [MatrixMath.imul_matrix(transformed, transform) for transform in transforms]
        return transformed

    itransform = MatrixMath.imul_matrix
    def itransforms(matrix, transforms):
        [MatrixMath.imul_matrix(matrix, transform) for transform in transforms]
        return matrix
