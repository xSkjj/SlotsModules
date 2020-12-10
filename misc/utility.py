from misc import gui, ConfigParser


def show_settings():
    gui.amtInput.unbind("<Return>")
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def hide_settings():
    gui.amtInput.bind("<Return>", gui.spin.try_spin)
    gui.settingsFrame.place_forget()


def change_setting(sect, key, value):
    config = ConfigParser()
    config.read("settings.ini")
    config[sect][key] = value
    with open("settings.ini", 'w') as settings:
        config.write(settings)


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
