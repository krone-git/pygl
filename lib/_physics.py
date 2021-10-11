from math import sin, cos, pi


arch_linear = lambda time, height=1.0, duration=1.0: (
    height * (1 - ((1 - 2 * time / duration) ** 2) ** 0.5)
    )

arch_square = lambda time, height=1.0, duration=1.0: (
    height * (1 - (2 * time / duration - 1) ** 2)
    )

arch_sinoid = lambda time, height=1.0, duration=1.0: (
    height * sin(time * pi / duration)
    )

arch_sinsquare = lambda time, height=1.0, duration=1.0: (
    height * sin(time * pi / duration) ** 2
    )
