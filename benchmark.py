import sys, timeit

from lib.vector import BaseVector2D, MutableVector2D
from lib.vertex import Vertex2D

if __name__ == "__main__":
    b = BaseVector2D(1, 2)
    v = Vertex2D(1, 2)

    print(sys.getsizeof(b), sys.getsizeof(v), end="\n")

    print(timeit.timeit(lambda: BaseVector2D(1, 2)))
    print(timeit.timeit(lambda: Vertex2D(1, 2)), end="\n")

    b1, b2 = BaseVector2D(1, 2), BaseVector2D(1, 2)
    v1, v2 = Vertex2D(1, 2), Vertex2D(1, 2)

    def f(x, y):
        x += y
    print(timeit.timeit(lambda: MutableVector2D.__iadd__(b1, b2)))
    print(timeit.timeit(lambda: f(v1, v2)), end="\n")

    print(b1)
    print(v1)
