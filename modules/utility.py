from modules import gui
from tkinter import colorchooser


def on_close():
    # insert something that kills still running threads
    gui.root.destroy()


def show_settings():
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def change_color(entry):
    _, color = colorchooser.askcolor()
    entry.delete(0, "end")
    entry.insert(0, color)
