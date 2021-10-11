from ..face.face3 import Rectangle3DFactory


class Cube3DFactory:
    unit = unit_ac = lambda: [
        *Rectangle3DFactory.unit_ac_x0(),
        *Rectangle3DFactory.unit_ac_y0(),
        *Rectangle3DFactory.unit_ac_z0(),
        *Rectangle3DFactory.unit_ac_x1(),
        *Rectangle3DFactory.unit_ac_y1(),
        *Rectangle3DFactory.unit_ac_z1()
        ]
    unit_bd = lambda: [
        *Rectangle3DFactory.unit_bd_x0(),
        *Rectangle3DFactory.unit_bd_y0(),
        *Rectangle3DFactory.unit_bd_z0(),
        *Rectangle3DFactory.unit_bd_x1(),
        *Rectangle3DFactory.unit_bd_y1(),
        *Rectangle3DFactory.unit_bd_z1()
        ]


class Shape3DFactory:
    pass
