from ..vector.vector2.factory import create_vec2, copy_vec2


class Triangle2DFactory:
    from_vecs = lambda veca, vecb, vecc: [veca, vecb, vecc]
    @classmethod
    def from_coords(cls, x1, y1, x2, y2, x3, y3):
        return cls.from_vecs(
            create_vec2(x1, y1),
            create_vec2(x2, y2),
            create_vec2(x3, y3)
            )

    @classmethod
    def unita(cls):
        return cls.from_vecs(
            create_vec2(0.0, 0.0),
            create_vec2(0.0, 1.0),
            create_vec2(1.0, 1.0)
            )
    @classmethod
    def unitb(cls):
        return cls.from_vecs(
            create_vec2(0.0, 1.0),
            create_vec2(1.0, 1.0),
            create_vec2(1.0, 0.0)
            )
    @classmethod
    def unitc(cls):
        return cls.from_vecs(
            create_vec2(1.0, 1.0),
            create_vec2(1.0, 0.0),
            create_vec2(0.0, 0.0)
            )
    @classmethod
    def unitd(cls):
        return cls.from_vecs(
            create_vec2(1.0, 0.0),
            create_vec2(0.0, 0.0),
            create_vec2(0.0, 1.0)
            )

    unit = unita


class Rectangle2DFactory:
    from_tris = lambda tria, trib: [tria, trib]
    @classmethod
    def from_vecs(cls, veca, vecb, vecc, vecd):
        return cls.from_tris(
            Triangle2DFactory.from_vec(veca, vecb, vecc),
            Triangle2DFactory.from_vec(copy_vec2(veca), copy_vec2(vecc), vecd)
            )
    @classmethod
    def from_coords(cls, x1, y1, x2, y2, x3, y3, x4, y4):
        return cls.from_vecs(
            create_vec2(x1, y1),
            create_vec2(x2, y2),
            create_vec2(x3, y3),
            create_vec2(x4, y4)
            )
    @classmethod
    def unit(cls):
        return cls.from_tris(
            Triangle2DFactory.unita(),
            Triangle2DFactory.unitc()
            )


class Polygon2DFactory:
    from_tris = lambda *tris: [*tris]
    from_vecs = lambda *vecs: [
        Triangle2DFactory.from_vecs(*vecs[i : i + 3]) for i in range(0, vecs, 3)
        ]
    from_coords = lambda: None
