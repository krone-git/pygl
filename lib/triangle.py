from .vector import VectorFactory, VectorMath, VectorTransform
from .matrix import MatrixMath


class TriangleUtility:
    unpack1 = lambda triangle:[
        triangle[0][0],
        triangle[0][1],
        triangle[0][2],
        triangle[1][0],
        triangle[1][1],
        triangle[1][2],
        triangle[2][0],
        triangle[2][1],
        triangle[2][2],
        ]
    def unpack2(triangle):
        vertex1, vertex2, vertex3 = triangle
        return [
            vertex1[0], vertex1[1], vertex1[2],
            vertex2[0], vertex2[1], vertex2[2],
            vertex3[0], vertex3[1], vertex3[2],
            ]
    unpack3 = lambda triangle: [*triangle[0], *triangle[1], *triangle[2]]
    def unpack4(triangle):
        vertex1, vertex2, vertex3 = triangle
        return [*vertex1, *vertex2, *vertex3]
    def unpack5(triangle):
        return [*triangle[0], *triangle[1], *triangle[2]]
    unpack = unpack4

    def invert_normal1(triangle):
        vector = triangle[1]
        triangle[1] = triangle[2]
        triangle[2] = vector
        return triangle
    def invert_normal2(triangle):
        vector1, _, vector3 = triangle
        triangle[1] = vector3
        triangle[2] = vector1
        return triangle
    invert_normal = invert_normal2


class TriangleFactory:
    create1 = lambda vector1, vector2, vector3: [
        VectorFactory.from_vector(vector1),
        VectorFactory.from_vector(vector2),
        VectorFactory.from_vector(vector3),
        ]
    def create2(vector1, vector2, vector3):
        return [
            VectorFactory.from_vector(vector1),
            VectorFactory.from_vector(vector2),
            VectorFactory.from_vector(vector3),
            ]
    create = create2

    from_vector_references = lambda vector1, vector2, vector3: [
        vector1, vector2, vector3
        ]
    from_coordinates = lambda x1, y1, z1, x2, y2, z2, x3, y3, z3: [
        VectorFactory.create(x1, y1, z1),
        VectorFactory.create(x2, y2, z2),
        VectorFactory.create(x3, y3, z3),
        ]
    from_line = lambda line: [
        VectorFactory.copy(line[0]),
        VectorFactory.copy(line[1]),
        VectorFactory.copy(line[1]),
        ]
    from_unit_vectors = lambda: [
        VectorFactory.ihat(),
        VectorFactory.jhat(),
        VectorFactory.khat()
        ]

    copy1 = lambda triangle: [
        VectorFactory.copy(triangle[0]),
        VectorFactory.copy(triangle[1]),
        VectorFactory.copy(triangle[2]),
        ]
    def copy2(triangle):
        vertex1, vertex2, vertex3 = triangle
        return [
            VectorFactory.copy(vertex1),
            VectorFactory.copy(vertex2),
            VectorFactory.copy(vertex3),
            ]
    copy = copy2
    def icopy(triangle, other):
        other[0] = VectorFactory.copy(triangle[0])
        other[1] = VectorFactory.copy(triangle[1])
        other[2] = VectorFactory.copy(triangle[2])
        return other

    clockwise = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(0.0, 1.0, 0.0),
        VectorFactory.create(1.0, 1.0, 0.0),
        ]
    counter_clockwise = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(1.0, 1.0, 0.0),
        VectorFactory.create(0.0, 1.0, 0.0),
        ]


class TriangleMath:
    round1 = lambda triangle, ndigits=None: [
        VectorMath.round(vector, ndigits) for vector in triangle
        ]
    def round2(triangle, ndigits=None):
        return [
            VectorMath.round(triangle[0], ndigits),
            VectorMath.round(triangle[1], ndigits),
            VectorMath.round(triangle[2], ndigits),
            ]
    def round3(triangle, ndigits=None):
        vertex1, vertex2, vertex3 = triangle
        return [
            VectorMath.round(vertex1, ndigits),
            VectorMath.round(vertex2, ndigits),
            VectorMath.round(vertex3, ndigits),
            ]
    round = round3

    def iround(triangle, ndigits=None):
        [VectorMath.iround(vector, ndigits) for vector in triangle]
        return triangle

    floor = lambda triangle, ndigits=None: [
        VectorMath.floor(vector, ndigits) for vector in triangle
        ]
    def ifloor(triangle, ndigits=None):
        [VectorMath.ifloor(vector, ndigits) for vector in triangle]
        return triangle

    ceiling = lambda triangle, ndigits=None: [
        VectorMath.ceiling(vector, ndigits) for vector in triangle
        ]
    def iceiling(triangle, ndigits=None):
        [VectorMath.iceiling(vector, ndigits) for vector in triangle]
        return triangle

    def normal1(triangle):
        normal_vector = VectorMath.cross_product(
            VectorMath.sub_vector(triangle[1], triangle[0]),
            VectorMath.sub_vector(triangle[2], triangle[0])
            )
        length = VectorMath.length(normal_vector)
        length = 1.0 if length == 0.0 else length
        VectorMath.itruediv_values(
            normal_vector, length, length, length
            )
        return normal_vector
    def normal2(triangle):
        vertex1, vertex2, vertex3 = triangle
        normal_vector = VectorMath.cross_product(
            VectorMath.sub_vector(vertex2, vertex1),
            VectorMath.sub_vector(vertex3, vertex1)
            )
        length = VectorMath.length(normal_vector)
        length = 1.0 if length == 0.0 else length
        VectorMath.itruediv_values(
            normal_vector, length, length, length
            )
        return normal_vector
    normal = normal2

    center1 = lambda triangle: VectorFactory.create(
        (triangle[0][0] + triangle[1][0] + triangle[2][0]) / 3,
        (triangle[0][1] + triangle[1][1] + triangle[2][1]) / 3,
        (triangle[0][2] + triangle[1][2] + triangle[2][2]) / 3
        )
    def center2(triangle):
        vertex1, vertex2, vertex3 = triangle
        x1, y1, z1, _1 = vertex1
        x2, y2, z2, _2 = vertex2
        x3, y3, z3, _3 = vertex3
        return VectorFactory.create(
            (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3, (z1 + z2 + z3) / 3
            )
    def center3(triangle):
        vertex1, vertex2, vertex3 = triangle
        return VectorFactory.create(
            (vertex1[0] + vertex2[0] + vertex3[0]) / 3,
            (vertex1[1] + vertex2[1] + vertex3[1]) / 3,
            (vertex1[2] + vertex2[2] + vertex3[2]) / 3
            )
    center = center2


class TriangleTransform:
    transform1 = lambda triangle, transform: [
        VectorTransform.transform(vertex, transform) for vertex in triangle
        ]
    transform2 = lambda triangle, transform: [
        MatrixMath.xmul_vector(transform, vertex) for vertex in triangle
        ]
    def transform3(triangle, transform):
        vertex1, vertex2, vertex3 = triangle
        return [
            VectorTransform.transform(vertex1, transform),
            VectorTransform.transform(vertex2, transform),
            VectorTransform.transform(vertex3, transform),
            ]
    def transform4(triangle, transform):
        vertex1, vertex2, vertex3 = triangle
        return [
            MatrixMath.xmul_vector(transform, vertex1),
            MatrixMath.xmul_vector(transform, vertex2),
            MatrixMath.xmul_vector(transform, vertex3),
            ]
    transform5 = lambda triangle, transform: [
        MatrixMath.xmul_vector2(transform, vertex) for vertex in triangle
        ]
    def transform6(triangle, transform):
        vertex1, vertex2, vertex3 = triangle
        return [
            MatrixMath.xmul_vector2(transform, vertex1),
            MatrixMath.xmul_vector2(transform, vertex2),
            MatrixMath.xmul_vector2(transform, vertex3),
            ]
    def transform7(triangle, transform):
        return [
            MatrixMath.xmul_vector2(transform, triangle[0]),
            MatrixMath.xmul_vector2(transform, triangle[1]),
            MatrixMath.xmul_vector2(transform, triangle[2]),
            ]
    transform = transform6

    transforms = lambda triangle, transforms: [
        VectorTransform.transforms(vertex, transforms) for vertex in triangle
        ]

    def itransform(triangle, transform):
        [VectorTransform.itransform(vertex, transform) for vertex in triangle]
        return triangle

    def itransforms(triangle, transforms):
        [VectorTransform.itransforms(vertex, transforms) for vertex in triangle]
        return triangle
