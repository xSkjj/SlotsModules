from modules import gui, ConfigParser
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


def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)
