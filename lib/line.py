from .vector import VectorFactory, VectorMath
from .triangle import TriangleFactory


class LineUtility:
    unpack = lambda line: [
        line[0][0],
        line[0][1],
        line[0][2],
        line[1][0],
        line[1][1],
        line[1][2],
        ]

    to_vector = lambda line: VectorFactory.create(
        line[0][0] - line[1][0],
        line[0][1] - line[1][1],
        line[0][2] - line[1][2]
        )
    to_triangle = TriangleFactory.from_line


class LineFactory:
    create = lambda vector1, vector2: [
        VectorFactory.copy(vector1),
        VectorFactory.copy(vector2)
        ]
    from_vector = lambda vector: [
        VectorFactory.empty(),
        VectorFactory.copy(vector)
        ]
    from_vector_reference = lambda vector: [
        VectorFactory.empty(), vector
        ]
    from_vector_references = lambda vector1, vector2: [
        vector1, vector2
        ]
    from_coordinates = lambda x1, y1, z1, x2, y2, z2: [
        VectorFactory.create(x1, y1, z1),
        VectorFactory.create(x2, y2, z2),
        ]

    copy = lambda line: [
        VectoryFactory.copy(line[0]),
        VectoryFactory.copy(line[1]),
        ]
    def icopy(line, other):
        other[0] = VectoryFactory.copy(line[0])
        other[1] = VectoryFactory.copy(line[1])
        return other

    unit = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(1.0, 1.0, 0.0),
        ]

    ihat = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(1.0, 0.0, 0.0),
        ]
    jhat = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(0.0, 1.0, 0.0),
        ]
    khat = lambda: [
        VectorFactory.create(0.0, 0.0, 0.0),
        VectorFactory.create(0.0, 0.0, 1.0),
        ]


class LineMath:
    length = lambda line: (
        (line[0][0] - line[1][0]) ** 2 \
        + (line[0][1] - line[1][1]) ** 2 \
        + (line[0][2] - line[1][2]) ** 2
        ) ** 0.5
    center = lambda line: VectorFactory.create(
        (line[0][0] + line[1][0]) / 2,
        (line[0][1] + line[1][1]) / 2,
        (line[0][2] + line[1][2]) / 2
        )
