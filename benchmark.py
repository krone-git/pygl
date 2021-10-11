from timeit import timeit
from random import randint

from lib.rgba import RGBAFactory, RGBAMath, RGBAUtility
from lib.vector import VectorFactory, VectorMath
from lib.matrix import MatrixFactory, MatrixMath, MatrixUtility
from lib.triangle import TriangleFactory, TriangleMath, TriangleTransform, TriangleUtility


v = VectorFactory.random(function=lambda: randint(0, 10))
e = VectorFactory.empty()

m = MatrixFactory.random(function=lambda: randint(0, 10))
m2 = MatrixFactory.copy(m)

t = TriangleFactory.clockwise()

rgba = RGBAFactory.random()
hexcode = RGBAUtility.to_hexcode(rgba)


# --- Triangle Functions --------------
# print(
#     timeit(lambda: TriangleFactory.create1(v, v, v)), # slowest: 0.61
#     timeit(lambda: TriangleFactory.create2(v, v, v)), # fastest: 0.60
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleTransform.transform1(t, m)), # slowest:        4.10
#     timeit(lambda: TriangleTransform.transform2(t, m)),
#     timeit(lambda: TriangleTransform.transform3(t, m)),
#     timeit(lambda: TriangleTransform.transform4(t, m)),
#     timeit(lambda: TriangleTransform.transform5(t, m)),
#     timeit(lambda: TriangleTransform.transform6(t, m)), # fastest:        2.62
#     timeit(lambda: TriangleTransform.transform7(t, m)), # second fastest: 2.64
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleMath.center1(t)), # slowest: 0.64
#     timeit(lambda: TriangleMath.center2(t)), # fastest: 0.56
#     timeit(lambda: TriangleMath.center3(t)),
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleMath.normal1(t)), # slowest: 1.55
#     timeit(lambda: TriangleMath.normal2(t)), # fastest: 1.50
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleMath.round1(t)), # slowest: 1.88
#     timeit(lambda: TriangleMath.round2(t)),
#     timeit(lambda: TriangleMath.round3(t)), # fastest: 1.68
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleFactory.copy1(t)), # slowest: 0.58
#     timeit(lambda: TriangleFactory.copy2(t)), # fastest: 0.55
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleUtility.invert_normal1(t)), # slowest: 0.17
#     timeit(lambda: TriangleUtility.invert_normal2(t)), # fastest: 0.16
#     sep="\n"
#     )

# print(
#     timeit(lambda: TriangleUtility.unpack1(t)), # slowest:        0.34
#     timeit(lambda: TriangleUtility.unpack2(t)),
#     timeit(lambda: TriangleUtility.unpack3(t)), # second fastest: 0.23
#     timeit(lambda: TriangleUtility.unpack4(t)), # fastest:        0.20
#     timeit(lambda: TriangleUtility.unpack5(t)),
#     sep="\n"
#     )



# --- Matrix Functions ----------------
# print(
#     timeit(lambda: MatrixMath.xmul_vector1(m, v)), # slowest: 1.12
#     timeit(lambda: MatrixMath.xmul_vector2(m, v)), # fastest: 0.80
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixMath.mul_vector1(m, v)), # slowest: 0.97
#     timeit(lambda: MatrixMath.mul_vector2(m, v)), # fastest: 0.68
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixMath.mul_matrix1(m, m2)), # slowest:        3.86
#     timeit(lambda: MatrixMath.mul_matrix2(m, m2)),
#     timeit(lambda: MatrixMath.mul_matrix3(m, m2)), # second fastest: 1.74
#     timeit(lambda: MatrixMath.mul_matrix4(m, m2)), # fastest:        1.70
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixMath.determinant1(m)), # slowest: 2.24
#     timeit(lambda: MatrixMath.determinant2(m)), # third fastest: 1.14
#     timeit(lambda: MatrixMath.determinant3(m)), # fastest: 1.13
#     timeit(lambda: MatrixMath.determinant4(m)),
#     timeit(lambda: MatrixMath.determinant5(m)), # second fastest: 1.14
#     timeit(lambda: MatrixMath.determinant6(m)),
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixFactory.copy1(m)),  # slowest:        0.60
#     timeit(lambda: MatrixFactory.copy2(m)),
#     timeit(lambda: MatrixFactory.copy3(m)),  # fastest:        0.30
#     timeit(lambda: MatrixFactory.copy4(m)),  # second fastest: 0.35
#     timeit(lambda: MatrixFactory.copy5(m)),
#     timeit(lambda: MatrixFactory.copy5_(m)),
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixUtility.set_scale1(m)),  # fastest: 0.18
#     timeit(lambda: MatrixUtility.set_scale2(m2)), # slowest: 0.20
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixUtility.get_scale1(m)),  # slowest: 0.20
#     timeit(lambda: MatrixUtility.get_scale2(m2)), # fastest: 0.18
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixUtility.to_identity1(m)),  # slowest: 0.57
#     timeit(lambda: MatrixUtility.to_identity2(m2)), # fastest: 0.44
#     sep="\n"
#     )

# print(
#     timeit(lambda: MatrixUtility.clear1(m)),  # slowest: 0.52
#     timeit(lambda: MatrixUtility.clear2(m2)), # fastest: 0.42
#     sep="\n"
#     )



# --- Vector Functions ----------------
# print(
#     timeit(lambda: VectorMath.iadd_vector1(v, e)), # slowest: 0.31
#     timeit(lambda: VectorMath.iadd_vector2(v, e)), # fastest: 0.27
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.add_vector1(v, v)), # slowest: 0.28
#     timeit(lambda: VectorMath.add_vector2(v, v)), # fastest: 0.25
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.add_value1(v, 1)), # slowest: 0.24
#     timeit(lambda: VectorMath.add_value2(v, 1)), # fastest: 0.21
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.normal1(v, VectorFactory.IHAT)),
#     timeit(lambda: VectorMath.normal2(v, VectorFactory.IHAT)), # fastest: 1.95 - 2.15
#     timeit(lambda: VectorMath.normal3(v, VectorFactory.IHAT)), # slowest: 2.00 - 2.22
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.normalize1(v)), # slowest: 1.05
#     timeit(lambda: VectorMath.normalize2(v)), # fastest: 1.03
#     sep="\n",
#     end="\n\n"
#     )

# print(
#     timeit(lambda: VectorMath.inverse1(v)), # slowest:        0.23
#     timeit(lambda: VectorMath.inverse2(v)), # second fastest: 0.20
#     timeit(lambda: VectorMath.inverse3(v)),
#     timeit(lambda: VectorMath.inverse4(v)), # fastest:      < 0.20
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.length1(v)),  # tied: 1.59 - 1.97
#     timeit(lambda: VectorMath.length2(v)),  # tied: 1.64 - 1.91
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.dot_product_values1(v, 1.0, 2.0, 3.0)), # slowest: 0.24 - 0.26
#     timeit(lambda: VectorMath.dot_product_values2(v, 1.0, 2.0, 3.0)), # fastest: 0.23 - 0.24
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.dot_product1(v, v)), # slowest: 0.30
#     timeit(lambda: VectorMath.dot_product2(v, v)), # fastest: 0.29
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.cross_product_values1(v, 1.0, 2.0, 3.0)), # slowest: 0.39 - 0.44
#     timeit(lambda: VectorMath.cross_product_values2(v, 1.0, 2.0, 3.0)), # fastest: 0.37 - 0.39
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorMath.cross_product1(v, v)), # slowest: 0.47
#     timeit(lambda: VectorMath.cross_product2(v, v)), # fastest: 0.36
#     sep="\n"
#     )

# print(
#     timeit(lambda: VectorFactory.copy1(v)),
#     timeit(lambda: VectorFactory.copy2(v)), # second fastest: 0.21
#     timeit(lambda: VectorFactory.copy3(v)), # slowest:        0.30
#     timeit(lambda: VectorFactory.copy4(v)),
#     timeit(lambda: VectorFactory.copy5(v)), # fastest:        0.19
#     sep="\n"
#     )



# --- RGBA Functions ------------------
# print(
#     timeit(lambda: RGBAMath.most_significant1(rgba)),
#     timeit(lambda: RGBAMath.most_significant2(rgba)), # fastest: 0.36
#     timeit(lambda: RGBAMath.most_significant3(rgba)), # slowest: 0.39
#     sep="\n"
#     )

# print(
#     timeit(lambda: RGBAMath.overlay1(rgba, rgba)),
#     timeit(lambda: RGBAMath.overlay2(rgba, rgba)), # fastest: 1.11
#     timeit(lambda: RGBAMath.overlay3(rgba, rgba)), # slowest: 1.19
#     sep="\n"
#     )

# print(
#     timeit(lambda: RGBAMath.normalize1(rgba)), # slowest: 0.51
#     timeit(lambda: RGBAMath.normalize2(rgba)), # fastest: 0.43
#     sep="\n"
#     )

# print(
#     timeit(lambda: RGBAFactory.create1(1, 2, 3)), # slowest: 0.48
#     timeit(lambda: RGBAFactory.create2(1, 2, 3)), # fastest: 0.46
#     sep="\n"
#     )

# print(
#     timeit(lambda: RGBAUtility.is_hexcode1(hexcode)), # slowest: 1.40
#     timeit(lambda: RGBAUtility.is_hexcode2(hexcode)), # fastest: 0.98
#     sep="\n"
#     )

# print(
#     timeit(lambda: RGBAFactory.icopy1(rgba, rgba)), # slowest: 0.53
#     timeit(lambda: RGBAFactory.icopy2(rgba, rgba)), # fastest: 0.51
#     timeit(lambda: RGBAFactory.icopy3(rgba, rgba)),
#     sep="\n"
#     )


# --- General Functions ---------------
