

class RGBMath:
    normalize_rgb = lambda r, g, b: (
        (abs(int(r)) % 255) / 255,
        (abs(int(g)) % 255) / 255,
        (abs(int(b)) % 255) / 255
        )
    normalize = normalize_vec = lambda vec: (
        (abs(int(vec[0])) % 255) / 255,
        (abs(int(vec[1])) % 255) / 255,
        (abs(int(vec[2])) % 255) / 255
        )


class RGBFactory:
    create = from_rgb = lambda r, g, b: [
        abs(int(r)) % 255,
        abs(int(g)) % 255,
        abs(int(b)) % 255
        ]
    empty = lambda: [0, 0, 0]
    copy = from_vec = lambda vec: [
        abs(int(vec[0])) % 255,
        abs(int(vec[1])) % 255,
        abs(int(vec[2])) % 255
        ]


class RGBHexString:
    from_rgb = lambda r, g, b: "#" \
        + hex(int(abs(r) % 255))[2:4].rjust(2, "0") \
        + hex(int(abs(g) % 255))[2:4].rjust(2, "0") \
        + hex(int(abs(b) % 255))[2:4].rjust(2, "0")

    from_vec = lambda vec: "#" \
        + hex(int(abs(vec[0]) % 255))[2:4].rjust(2, "0") \
        + hex(int(abs(vec[1]) % 255))[2:4].rjust(2, "0") \
        + hex(int(abs(vec[2]) % 255))[2:4].rjust(2, "0")
