import tkinter as tk
from modules import bgColor, utility
from classes import colorbutton


class Section(tk.Frame):
    def __init__(self, master, grid=False, **kwargs):
        tk.Frame.__init__(self, master,
                          bg=bgColor)
        self.label = tk.Label(self,
                              font="Consolas 12 bold" if grid else "Impact 24",
                              fg="white",
                              bg=bgColor,
                              **kwargs)
        self.label.grid(column=0, row=0, padx=4) if grid else self.label.pack()
        self.pack(padx=4, pady=8)


class ColorPicker(tk.Frame):
    def __init__(self, master, key, default_value=0):
        tk.Frame.__init__(self, master, bg=bgColor)
        self.entry = tk.Entry(self,
                              textvariable=tk.StringVar(value=default_value),
                              font="Consolas 16",
                              fg="white",
                              bg="#404040",
                              insertbackground="white",
                              relief="flat",
                              width=7)
        self.entry.grid(column=0, row=0)
        self.button = colorbutton.ColorButton(self, "grey",
                                              command=lambda: utility.change_color(self.entry, key),
                                              text="pick",
                                              font="Arial 10 bold")
        self.button.grid(column=1, row=0)
        self.grid(column=1, row=0)
