from lib.obj import ObjectFileWriter, ObjectFileHandler
from lib.transform import TransformMatrix
from lib.triangle import TriangleFactory, TriangleMath, TriangleTransform, TriangleUtility
from lib.vector import VectorFactory, VectorMath

v = (1 + 5 ** 0.5) / 2
vertex1 = VectorFactory.create(0.0, 0.0, 0.0)
vertex2 = VectorFactory.create(0.0, v, 0.0)
vertex3 = VectorFactory.create(v, v, 0.0)
vertex4 = VectorFactory.create(v, 0.0, 0.0)
vertex5 = VectorFactory.create(0.0, 0.0, 1.0)
vertex6 = VectorFactory.create(0.0, v, 1.0)
vertex7 = VectorFactory.create(v, v, 1.0)
vertex8 = VectorFactory.create(v, 0.0, 1.0)

vertex9 = VectorFactory.create(0.0, 0.0, 0.0)
vertex10 = VectorFactory.create(0.0, 0.0, 0.0)
vertex11 = VectorFactory.create(0.0, 0.0, 0.0)
vertex12 = VectorFactory.create(0.0, 0.0, 0.0)

vertex13 = VectorFactory.create(0.0, 0.0, 0.0)
vertex14 = VectorFactory.create(0.0, 0.0, 0.0)
vertex15 = VectorFactory.create(0.0, 0.0, 0.0)
vertex16 = VectorFactory.create(0.0, 0.0, 0.0)

vertex17 = VectorFactory.create(0.0, 0.0, 0.0)
vertex18 = VectorFactory.create(0.0, 0.0, 0.0)
vertex19 = VectorFactory.create(0.0, 0.0, 0.0)
vertex20 = VectorFactory.create(0.0, 0.0, 0.0)


face1 = TriangleFactory.create(vertex1, vertex2, vertex3)
face2 = TriangleFactory.create(vertex1, vertex3, vertex6)
face3 = TriangleFactory.create(vertex3, vertex4, vertex6)
face4 = TriangleFactory.create(vertex4, vertex5, vertex6)

triangles = [face1, face2, face3, face4]

unit = 1 / 2
scale = TransformMatrix.scale(unit, unit, unit)
shift = TransformMatrix.translation()
transforms = [scale, shift]
[TriangleTransform.itransforms(tri, transforms) for tri in triangles]

for tri in triangles:
    normal = TriangleMath.normal(tri)
    print(VectorMath.dot_product(normal, VectorFactory.KHAT))

ObjectFileWriter.write_triangles(
    triangles,
    ObjectFileHandler.source_path("unit_hexagon.obj")
    )
