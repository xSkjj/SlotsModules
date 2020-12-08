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
        self.label.grid(column=0, row=0, padx=4, sticky="ew") if grid else self.label.pack()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.pack(padx=4, pady=8, fill='x')


class TextSlider(tk.Frame):
    def __init__(self, master, font="Arial 10 bold"):
        super().__init__(master)
        self.leftSlider = colorbutton.ColorButton(self, "grey",
                                                  text="<",
                                                  font=font,
                                                  width=4)
        self.textLabel = tk.Label(self,
                                  font=font,
                                  bg=self.leftSlider.bg,
                                  width=11)
        self.rightSlider = colorbutton.ColorButton(self, "grey",
                                                   text=">",
                                                   font=font,
                                                   width=4)
        self["bg"] = self.leftSlider.bg

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.leftSlider.grid(column=0, row=0)
        self.textLabel.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def slide(self):
        pass
