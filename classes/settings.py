import tkinter as tk
from modules import bgColor
from classes import colorbutton


class Section(tk.Frame):
    def __init__(self, master, text=None, grid=False, pack=True, **kwargs):
        super().__init__(master,
                         bg=bgColor,
                         **kwargs)
        self.label = tk.Label(self,
                              text=text,
                              font="Consolas 12 bold" if grid else "Impact 24",
                              fg="white",
                              bg=bgColor)
        self.label.grid(column=0, row=0, padx=4, sticky='w') if grid else self.label.pack()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.pack(padx=20, pady=8, fill='x') if pack else None


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
                                  width=6)
        self.rightSlider = colorbutton.ColorButton(self, "grey",
                                                   text=">",
                                                   font=font,
                                                   width=4)
        self["bg"] = self.leftSlider.bg

        self.leftSlider.grid(column=0, row=0)
        self.textLabel.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def slide(self):
        pass
