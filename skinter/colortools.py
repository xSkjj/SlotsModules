def to_rgb(hx):
    """
    Turn a hex color into a list with the rgb values
    """
    return [int(hx[i] + hx[i + 1], 16) for i in range(1, 7, 2)]


def rgb(r, g=None, b=None):
    """
    Returns a hex code from an rgb value
    rgb(tuple or list) or rgb(red, green, blue)
    """
    r, g, b = r if type(r) == tuple else (r, g, b)
    return "#%02x%02x%02x" % (r, g, b)


def is_dark(color):
    """
    Returns True if the color average is < 128
    """
    li = to_rgb(color) if type(color) == str else color
    return 128 > (sum(li) / 3)


def color_math(hx, value):
    """
    Add or subtract a value from a hex color
    """
    rgb_list = to_rgb(hx)
    for i, c in enumerate(rgb_list):
        rgb_list[i] = min(max(round(c + value), 0), 255)
    r, g, b = rgb_list
    return rgb(r, g, b)
