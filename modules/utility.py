from modules import gui
from tkinter import colorchooser
from configparser import ConfigParser


def on_close():
    # insert something that kills still running threads
    gui.root.destroy()


def show_settings():
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def change_color(entry, key):
    _, color = colorchooser.askcolor()
    entry.delete(0, "end")
    entry.insert(0, color)

    config = ConfigParser()
    config.read("settings.ini")
    config["customisation"][key] = color
    with open("settings.ini", 'w') as settings:
        config.write(settings)


def hide_settings():
    gui.settingsFrame.place_forget()
