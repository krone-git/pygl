from ..vector.vector3.factory import xcreate_vec3, xempty_vec3, xcopy_vec3
from ..vector.vector3.math import sub_vec_vec3, cross_vec3, len_vec3, \
                                    truediv_scl_vec3
from ..transform.vector3 import Vector3DTransform


class Face3D:
    def __init__(self, vectors=None):
        self._vectors = Triangle3DFactory.copy(vectors) if vectors else Triangle3DFactory.unita_z0()
        self._transformed = Triangle3DFactory.copy(self._vectors)

    transformed = lambda self: self._transformed

    def update(self, matrices):
        Triangle3DFactory.icopy(self._vectors, self._transformed)
        [Vector3DTransform.xitransforms(vec, matrices) for vec in self._transformed]
        return self

    def copy(self):
        face = self.__class__(self._vectors)
        face._transformed = Triangle3DFactory.copy(self._transformed)
        return face


class Triangle3DMath:
    def normal(tri):
        norm_vec = cross_vec3(
            sub_vec_vec3(tri[1], tri[0]),
            sub_vec_vec3(tri[2], tri[0])
            )
        norm_vec = truediv_scl_vec3(norm_vec, len_vec3(norm_vec))
        return xcreate_vec3(norm_vec[0], norm_vec[1], norm_vec[2])

    center =lambda tri: xcreate_vec3(
        (tri[0][0] + tri[1][0] + tri[2][0]) / 3,
        (tri[0][1] + tri[1][1] + tri[2][1]) / 3,
        (tri[0][2] + tri[1][2] + tri[2][2]) / 3
        )

class Triangle3DFactory:
    from_vecs = lambda veca, vecb, vecc: [veca, vecb, vecc]
    @classmethod
    def from_coords(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        return cls.from_vecs(
            xcreate_vec3(x1, y1, z1),
            xcreate_vec3(x2, y2, z2),
            xcreate_vec3(x3, y3, z3)
            )

    @classmethod
    def copy(cls, tri):
        return cls.from_vecs(
            xcopy_vec3(tri[0]),
            xcopy_vec3(tri[1]),
            xcopy_vec3(tri[2])
            )
    def icopy(tri, other):
        other[0] = xcopy_vec3(tri[0])
        other[1] = xcopy_vec3(tri[1])
        other[2] = xcopy_vec3(tri[2])
        return other


    @classmethod
    def unita_x0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(0.0, 1.0, 1.0)
            )
    @classmethod
    def unitb_x0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(0.0, 1.0, 0.0)
            )
    @classmethod
    def unitc_x0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(0.0, 1.0, 0.0)
            )
    @classmethod
    def unitd_x0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(0.0, 0.0, 0.0)
            )
    @classmethod
    def unita_x1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(1.0, 1.0, 1.0)
            )
    @classmethod
    def unitb_x1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(1.0, 0.0, 1.0)
            )
    @classmethod
    def unitc_x1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(1.0, 0.0, 1.0)
            )
    @classmethod
    def unitd_x1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(1.0, 0.0, 0.0)
            )

    @classmethod
    def unita_y0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(1.0, 0.0, 1.0)
            )
    @classmethod
    def unitb_y0(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(0.0, 0.0, 1.0)
            )
    @classmethod
    def unitc_y0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(0.0, 0.0, 1.0)
            )
    @classmethod
    def unitd_y0(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(0.0, 0.0, 0.0)
            )
    @classmethod
    def unita_y1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(1.0, 1.0, 1.0)
            )
    @classmethod
    def unitb_y1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(1.0, 1.0, 0.0)
            )
    @classmethod
    def unitc_y1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(1.0, 1.0, 0.0)
            )
    @classmethod
    def unitd_y1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(0.0, 1.0, 0.0)
            )

    @classmethod
    def unita_z0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(1.0, 1.0, 0.0)
            )
    @classmethod
    def unitb_z0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(1.0, 0.0, 0.0)
            )
    @classmethod
    def unitc_z0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 0.0),
            xcreate_vec3(1.0, 1.0, 0.0),
            xcreate_vec3(1.0, 0.0, 0.0)
            )
    @classmethod
    def unitd_z0(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 1.0, 0.0),
            xcreate_vec3(1.0, 0.0, 0.0),
            xcreate_vec3(0.0, 0.0, 0.0)
            )
    @classmethod
    def unita_z1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(1.0, 1.0, 1.0)
            )
    @classmethod
    def unitb_z1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(0.0, 1.0, 1.0)
            )
    @classmethod
    def unitc_z1(cls):
        return cls.from_vecs(
            xcreate_vec3(0.0, 0.0, 1.0),
            xcreate_vec3(1.0, 1.0, 1.0),
            xcreate_vec3(0.0, 1.0, 1.0)
            )
    @classmethod
    def unitd_z1(cls):
        return cls.from_vecs(
            xcreate_vec3(1.0, 0.0, 1.0),
            xcreate_vec3(0.0, 1.0, 1.0),
            xcreate_vec3(0.0, 0.0, 1.0)
            )

    unit = unita = unita_z0
    unitb = unitb_z0
    unitc = unitc_z0
    unitd = unitd_z0


class Rectangle3DFactory:
    from_tris = lambda tria, trib: [tria, trib]
    @classmethod
    def from_vecs(cls, veca, vecb, vecc, vecd):
        return cls.from_tris(
            Triangle3DFactory.from_vec(veca, vecb, vecc),
            Triangle3DFactory.from_vec(xcopy_vec3(veca), xcopy_vec3(vecc), vec4d)
            )
    @classmethod
    def from_coords(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
        return cls.from_vecs(
            xcreate_vec3(x1, y1, z1),
            xcreate_vec3(x2, y2, z2),
            xcreate_vec3(x3, y3, z3),
            xcreate_vec3(x4, y4, z4)
            )

    @classmethod
    def unit_ac_x0(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_x0(),
            Triangle3DFactory.unitc_x0()
            )
    @classmethod
    def unit_bd_x0(cls):
        return cls.from_tris(
        Triangle3DFactory.unitb_x0(),
        Triangle3DFactory.unitd_x0()
        )
    @classmethod
    def unit_ac_x1(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_x1(),
            Triangle3DFactory.unitc_x1()
            )
    @classmethod
    def unit_bd_x1(cls):
        return cls.from_tris(
            Triangle3DFactory.unitb_x1(),
            Triangle3DFactory.unitd_x1()
            )
    unit_x0 = unit_ac_x0
    unit_x1 = unit_ac_x1

    @classmethod
    def unit_ac_y0(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_y0(),
            Triangle3DFactory.unitc_y0()
            )
    @classmethod
    def unit_bd_y0(cls):
        return cls.from_tris(
        Triangle3DFactory.unitb_y0(),
        Triangle3DFactory.unitd_y0()
        )
    @classmethod
    def unit_ac_y1(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_y1(),
            Triangle3DFactory.unitc_y1()
            )
    @classmethod
    def unit_bd_y1(cls):
        return cls.from_tris(
            Triangle3DFactory.unitb_y1(),
            Triangle3DFactory.unitd_y1()
            )
    unit_y0 = unit_ac_y0
    unit_y1 = unit_ac_y1

    @classmethod
    def unit_ac_z0(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_z0(),
            Triangle3DFactory.unitc_z0()
            )
    @classmethod
    def unit_bd_z0(cls):
        return cls.from_tris(
        Triangle3DFactory.unitb_z0(),
        Triangle3DFactory.unitd_z0()
        )
    @classmethod
    def unit_ac_z1(cls):
        return cls.from_tris(
            Triangle3DFactory.unita_z1(),
            Triangle3DFactory.unitc_z1()
            )
    @classmethod
    def unit_bd_z1(cls):
        return cls.from_tris(
            Triangle3DFactory.unitb_z1(),
            Triangle3DFactory.unitd_z1()
            )
    unit = unit_z0 = unit_ac_z0
    unit_z1 = unit_ac_z1


class Polygon3DFactory:
    from_tris = lambda *tris: [*tris]
    from_vecs = lambda *vecs: [
        Triangle3DFactory.from_vecs(*vecs[i : i + 3]) for i in range(0, vecs, 3)
        ]
    from_coords = lambda: None
