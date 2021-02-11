

class Vertex3D:
    def __init__(x, y, z):
        self.x, self.y, self.z = x, y, z


class Vertex3DFactory:
    @classmethod
    def copy(cls, vertex):
        return Vertex3D(
            vertex.x, vertex.y, vertex.z
            )


class Vertex3DArithmetic:
    @classmethod
    def add(cls, vertex, x, y, z):
        vertex.x += x
        vertex.y += y
        vertex.z += z
        return cls

    @classmethod
    def subtract(cls, vertex, x, y, z):
        vertex.x -= x
        vertex.y -= y
        vertex.z -= z
        return cls

    @classmethod
    def multiply(cls, vertex, x, y, z):
        vertex.x *= x
        vertex.y *= y
        vertex.z *= z
        return cls

    @classmethod
    def divide(cls, vertex, x, y, z):
        vertex.x /= x
        vertex.y /= y
        vertex.z /= z
        return cls

    @classmethod
    def add_vertices(cls, vertex1, vertex2):
        return cls.add(vertex1, vertex2.x, vertex2.y, vertex2.z)

    @classmethod
    def subtract_vertices(cls, vertex1, vertex2):
        return cls.substract(vertex1, vertex2.x, vertex2.y, vertex2.z)

    @classmethod
    def multiply_vertices(cls, vertex1, vertex2):
        return cls.multiply(vertex1, vertex2.x, vertex2.y, vertex2.z)

    @classmethod
    def divide_vertices(cls, vertex1, vertex2):
        return cls.divide(vertex1, vertex2.x, vertex2.y, vertex2.z)
