def to_rgb(hx):
    return [int(hx[i] + hx[i + 1], 16) for i in range(1, 7, 2)]


def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


def is_bright(color):
    """
    Returns True if the color average is > 127 -> a bright color
    """
    li = to_rgb(color) if type(color) == str else color
    return 128 <= sum(li) / 3


def set_brightness(hx, value):
    rgb_list = to_rgb(hx)
    for i, c in enumerate(rgb_list):
        rgb_list[i] = min(max(round(c + value), 0), 255)
    r, g, b = rgb_list
    return rgb(r, g, b)


def switch(key, cases: dict):
    call = cases.get(key, cases.get("default"))
    if call is not None:
        call()
