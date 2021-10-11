from re import compile, findall
from random import randint


ISHEXCODE_PATTERN = compile("[0-9,a-f,A-F]{2}")

class RGBAUtility:
    def set(rgba, r=None, g=None, b=None, a=None):
        if r != None:
            rgba[0] = 255 if r > 255 else 0 if r < 0 else r // 1
        if g != None:
            rgba[1] = 255 if g > 255 else 0 if g < 0 else g // 1
        if b != None:
            rgba[2] = 255 if b > 255 else 0 if b < 0 else b // 1
        if a != None:
            rgba[3] = 1.0 if a > 1 else 0.0 if a < 0 else a / 1
        return rgba

    is_rgba = lambda rgba: isinstance(rgba, list) \
        and 3 <= len(rgb) <= 4 \
        and 0 <= rgba[0] <= 255 \
        and 0 <= rgba[1] <= 255 \
        and 0 <= rgba[2] <= 255 \
        and ((0 <= rgba[3] <= 1) if len(rgba) == 4 else True)
    is_hexcode1 = lambda string: isinstance(string, str) \
        and len(findall("[0-9,a-f,A-F]{2}", string[-6:])) == 3
    is_hexcode2 = lambda string: isinstance(string, str) \
        and len(ISHEXCODE_PATTERN.findall(string[-6:])) == 3
    is_hexcode = is_hexcode2

    to_hexcode = lambda rgba: ("#" \
        + hex(int(rgba[0]))[2:].rjust(2, "0")[-2:] \
        + hex(int(rgba[1]))[2:].rjust(2, "0")[-2:] \
        + hex(int(rgba[2]))[2:].rjust(2, "0")[-2:]
        ).upper()


class RGBAFactory:
    def create1(r, g, b, alpha=1.0):
        r = r // 1
        g = g // 1
        b = b // 1
        a = alpha / 1
        return [
            255 if r > 255 else 0 if r < 0 else r,
            255 if g > 255 else 0 if g < 0 else g,
            255 if b > 255 else 0 if b < 0 else b,
            1.0 if a > 1 else 0.0 if a < 0 else a,
            ]
    def create2(r, g, b, alpha=1.0):
        r //= 1
        g //= 1
        b //= 1
        alpha /= 1
        return [
            255 if r > 255 else 0 if r < 0 else r,
            255 if g > 255 else 0 if g < 0 else g,
            255 if b > 255 else 0 if b < 0 else b,
            1.0 if alpha > 1 else 0.0 if alpha < 0 else alpha,
            ]
    create = create2

    def random(alpha=1.0, scale=1, function=(lambda: randint(0, 255))):
        r = function() * scale
        g = function() * scale
        b = function() * scale
        return [
            255 if r > 255 else 0 if r < 0 else r,
            255 if g > 255 else 0 if g < 0 else g,
            255 if b > 255 else 0 if b < 0 else b,
            1.0 if alpha > 1 else 0.0 if alpha < 0 else alpha,
            ]

    copy = lambda rgba: rgba.copy()
    def icopy1(rgba, other):
        r = rgba[0] // 1
        g = rgba[1] // 1
        b = rgba[2] // 1
        a = rgba[3] / 1
        other[0] = 255 if r > 255 else 0 if r < 0 else r
        other[1] = 255 if g > 255 else 0 if g < 0 else g
        other[2] = 255 if b > 255 else 0 if b < 0 else b
        other[3] = 1.0 if a > 1 else 0.0 if a < 0 else a
        return other
    def icopy2(rgba, other):
        r, g, b, a = rgba
        r //= 1
        g //= 1
        b //= 1
        a /= 1
        other[0] = 255 if r > 255 else 0 if r < 0 else r
        other[1] = 255 if g > 255 else 0 if g < 0 else g
        other[2] = 255 if b > 255 else 0 if b < 0 else b
        other[3] = 1.0 if a > 1 else 0.0 if a < 0 else a
        return other
    def icopy3(rgba, other):
        r, g, b, a = rgba
        r = r // 1
        g = g // 1
        b = b // 1
        a = a / 1
        other[0] = 255 if r > 255 else 0 if r < 0 else r
        other[1] = 255 if g > 255 else 0 if g < 0 else g
        other[2] = 255 if b > 255 else 0 if b < 0 else b
        other[3] = 1.0 if a > 1 else 0.0 if a < 0 else a
        return other
    icopy = icopy2

    def from_hexcode(hexcode, alpha=1.0):
        hexstring = hexcode[-6:]
        r = int(hexstring[:2], 16)
        g = int(hexstring[2:4], 16)
        b = int(hexstring[4:6], 16)
        alpha /= 1
        return [
            255 if r > 255 else 0 if r < 0 else r,
            255 if g > 255 else 0 if g < 0 else g,
            255 if b > 255 else 0 if b < 0 else b,
            1.0 if alpha > 1 else 0.0 if alpha < 0 else alpha,
            ]


class RGBAMath:
    def normalize1(rgba):
        r = rgba[0]
        g = rgba[1]
        b = rgba[2]
        a = rgba[3]
        return [
            (255 if r > 255 else 0 if r < 0 else r) / 255,
            (255 if g > 255 else 0 if g < 0 else g) / 255,
            (255 if b > 255 else 0 if b < 0 else b) / 255,
            (1.0 if a > 1 else 0.0 if a < 0 else a),
            ]
    def normalize2(rgba):
        r, g, b, a = rgba
        return [
            (255 if r > 255 else 0 if r < 0 else r) / 255,
            (255 if g > 255 else 0 if g < 0 else g) / 255,
            (255 if b > 255 else 0 if b < 0 else b) / 255,
            (1.0 if a > 1 else 0.0 if a < 0 else a),
            ]

    normalize = normalize2

    max = lambda rgba: max(rgba[:3])
    min = lambda rgba: min(rgba[:3])

    def most_significant1(rgba):
        rgb = rgba[:3]
        return rgb.index(max(rgb))

    def most_significant2(rgba):
        return rgba.index(max(rgba[:3]))
    most_significant3 = lambda rgba: rgba.index(max(rgba[:3]))
    most_significant = most_significant2

    def least_significant(rgba):
        rgb = rgba[:3]
        return rgb.index(min(rgb))

    def level(rgba, level):
        level = 1.0 if level > 1 else 0.0 if level < 0 else level
        r = rgba[0] / 255
        g = rgba[1] / 255
        b = rgba[2] / 255

        r = 2 * r * level if level <= 0.5 else 2 * (level - 0.5) * (1 - r) + r
        g = 2 * g * level if level <= 0.5 else 2 * (level - 0.5) * (1 - g) + g
        b = 2 * b * level if level <= 0.5 else 2 * (level - 0.5) * (1 - b) + b
        return [
            (255 * (1 if r > 1 else 0 if r < 0 else r)) // 1,
            (255 * (1 if g > 1 else 0 if g < 0 else g)) // 1,
            (255 * (1 if b > 1 else 0 if b < 0 else b)) // 1,
            1.0
            ]

    def overlay1(rgba, target, level=None):
        level = target[3] if level == None else 1.0 if level > 1 else 0.0 if level < 0 else level
        r = rgba[0] / 255
        g = rgba[1] / 255
        b = rgba[2] / 255

        r += (target[0] / 255 - r) * level
        g += (target[1] / 255 - g) * level
        b += (target[2] / 255 - b) * level
        return [
            (255 * (1 if r > 1 else 0 if r < 0 else r)) // 1,
            (255 * (1 if g > 1 else 0 if g < 0 else g)) // 1,
            (255 * (1 if b > 1 else 0 if b < 0 else b)) // 1,
            1.0
            ]
    def overlay2(rgba, target, level=None):
        r, g, b, _ = rgba
        target_r, target_g, target_b, target_a = target
        level = target_a if level == None else 1.0 if level > 1 else 0.0 if level < 0 else level
        r /= 255
        g /= 255
        b /= 255

        r += (target_r / 255 - r) * level
        g += (target_g / 255 - g) * level
        b += (target_b / 255 - b) * level
        return [
            (255 * (1 if r > 1 else 0 if r < 0 else r)) // 1,
            (255 * (1 if g > 1 else 0 if g < 0 else g)) // 1,
            (255 * (1 if b > 1 else 0 if b < 0 else b)) // 1,
            1.0
            ]
    def overlay3(rgba, target, level=None):
        r, g, b, _ = rgba
        target_r, target_g, target_b, target_a = target
        level = target_a if level == None else 1.0 if level > 1 else 0.0 if level < 0 else level
        r /= 255
        g /= 255
        b /= 255

        target_r /= 255
        target_g /= 255
        target_b /= 255
        target_r -= r
        target_g -= g
        target_b -= b
        target_r *= level
        target_g *= level
        target_b *= level

        r += target_r
        g += target_g
        b += target_b
        return [
            (255 * (1 if r > 1 else 0 if r < 0 else r)) // 1,
            (255 * (1 if g > 1 else 0 if g < 0 else g)) // 1,
            (255 * (1 if b > 1 else 0 if b < 0 else b)) // 1,
            1.0
            ]
    overlay = overlay2

    def inverse(rgba):
        r = rgba[0]
        g = rgba[1]
        b = rgba[2]
        return [
            255 - (255 if r > 255 else 0 if r < 0 else r),
            255 - (255 if g > 255 else 0 if g < 0 else g),
            255 - (255 if b > 255 else 0 if b < 0 else b),
            1.0
            ]

    def invert(rgba):
        r = rgba[0]
        g = rgba[1]
        b = rgba[2]
        rgba[0] = 255 - (255 if r > 255 else 0 if r < 0 else r)
        rgba[1] = 255 - (255 if g > 255 else 0 if g < 0 else g)
        rgba[2] = 255 - (255 if b > 255 else 0 if b < 0 else b)
        return rgba

    def add_values(rgba, r=0, g=0, b=0, a=0):
        r += rgba[0]
        g += rgba[1]
        b += rgba[2]
        a += rgba[3]
        return [
            255 if r > 255 else 0 if r < 0 else r // 1,
            255 if g > 255 else 0 if g < 0 else g // 1,
            255 if b > 255 else 0 if b < 0 else b // 1,
            1.0 if a > 1 else 0.0 if a < 0 else a / 1,
            ]
    def sub_values(rgba, r=0, g=0, b=0, a=0):
        r = rgba[0] - r
        g = rgba[1] - g
        b = rgba[2] - b
        a = rgba[3] - a
        return [
            255 if r > 255 else 0 if r < 0 else r // 1,
            255 if g > 255 else 0 if g < 0 else g // 1,
            255 if b > 255 else 0 if b < 0 else b // 1,
            1.0 if a > 1 else 0.0 if a < 0 else a / 1,
            ]
    def mul_values(rgba, r=0, g=0, b=0, a=0):
        r *= rgba[0]
        g *= rgba[1]
        b *= rgba[2]
        a *= rgba[3]
        return [
            255 if r > 255 else 0 if r < 0 else r // 1,
            255 if g > 255 else 0 if g < 0 else g // 1,
            255 if b > 255 else 0 if b < 0 else b // 1,
            1.0 if a > 1 else 0.0 if a < 0 else a / 1,
            ]
    def truediv_values(rgba, r=0, g=0, b=0, a=0):
        r = rgba[0] / r
        g = rgba[1] / g
        b = rgba[2] / b
        a = rgba[3] / a
        return [
            255 if r > 255 else 0 if r < 0 else r // 1,
            255 if g > 255 else 0 if g < 0 else g // 1,
            255 if b > 255 else 0 if b < 0 else b // 1,
            1.0 if a > 1 else 0.0 if a < 0 else a / 1,
            ]

    def iadd_values(rgba, r=0, g=0, b=0, a=0):
        r += rgba[0]
        g += rgba[1]
        b += rgba[2]
        a += rgba[3]
        rgba[0] = 255 if r > 255 else 0 if r < 0 else r // 1
        rgba[1] = 255 if g > 255 else 0 if g < 0 else g // 1
        rgba[2] = 255 if b > 255 else 0 if b < 0 else b // 1
        rgba[3] = 1.0 if a > 1 else 0.0 if a < 0 else a / 1
        return rgba

    def isub_values(rgba, r=0, g=0, b=0, a=0):
        r = rgba[0] - r
        g = rgba[1] - g
        b = rgba[2] - b
        a = rgba[3] - a
        rgba[0] = 255 if r > 255 else 0 if r < 0 else r // 1
        rgba[1] = 255 if g > 255 else 0 if g < 0 else g // 1
        rgba[2] = 255 if b > 255 else 0 if b < 0 else b // 1
        rgba[3] = 1.0 if a > 1 else 0.0 if a < 0 else a / 1
        return rgba

    def imul_values(rgba, r=0, g=0, b=0, a=0):
        r *= rgba[0]
        g *= rgba[1]
        b *= rgba[2]
        a *= rgba[3]
        rgba[0] = 255 if r > 255 else 0 if r < 0 else r // 1
        rgba[1] = 255 if g > 255 else 0 if g < 0 else g // 1
        rgba[2] = 255 if b > 255 else 0 if b < 0 else b // 1
        rgba[3] = 1.0 if a > 1 else 0.0 if a < 0 else a / 1
        return rgba

    def itruediv_values(rgba, r=0, g=0, b=0, a=0):
        r = rgba[0] / r
        g = rgba[1] / g
        b = rgba[2] / b
        a = rgba[3] / a
        rgba[0] = 255 if r > 255 else 0 if r < 0 else r // 1
        rgba[1] = 255 if g > 255 else 0 if g < 0 else g // 1
        rgba[2] = 255 if b > 255 else 0 if b < 0 else b // 1
        rgba[3] = 1.0 if a > 1 else 0.0 if a < 0 else a / 1
        return rgba
