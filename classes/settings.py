import tkinter as tk
from modules import bgColor
from classes import colorbutton


class Section(tk.Frame):
    def __init__(self, master, grid=False, **kwargs):
        super().__init__(master,
                         bg=bgColor)
        self.label = tk.Label(self,
                              font="Consolas 12 bold" if grid else "Impact 24",
                              fg="white",
                              bg=bgColor,
                              **kwargs)
        self.label.grid(column=0, row=0, padx=4) if grid else self.label.pack()
        self.pack(padx=4, pady=8)


class TextSlider(tk.Frame):
    def __init__(self, master, default, **kwargs):
        super().__init__(master, **kwargs)
        self.leftSlider = colorbutton.ColorButton(self, "grey",
                                                  font="Arial 10 bold")
        self.textLabel = tk.Label(self,
                                  text=default)

    def slide(self):
        pass
