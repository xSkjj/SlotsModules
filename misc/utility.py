from misc import gui, ConfigParser
from tkinter import colorchooser


def show_settings():
    gui.amtInput.unbind("<Return>")
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def hide_settings():
    gui.amtInput.bind("<Return>", gui.spin.try_spin)
    gui.settingsFrame.place_forget()


def change_color(btn, key):
    _, color = colorchooser.askcolor()
    if color is None:
        return
    btn["bg"] = color

    config = ConfigParser()
    config.read("settings.ini")
    config["customisation"][key] = color
    with open("settings.ini", 'w') as settings:
        config.write(settings)


def to_rgb(hx):
    return [int(hx[i] + hx[i + 1], 16) for i in range(1, 7, 2)]


def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


def light_value(hx, percent):
    rgb_list = to_rgb(hx)
    for i, c in enumerate(rgb_list):
        rgb_list[i] = min(max(round(c*percent), 0), 255)
    r, g, b = rgb_list
    return rgb(r, g, b)
