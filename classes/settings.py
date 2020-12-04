import tkinter as tk
from modules import bgColor


class Section(tk.Frame):
    def __init__(self, master, grid=False, **kwargs):
        tk.Frame.__init__(self, master,
                          bg=bgColor)
        self.label = tk.Label(self,
                              font="Arial 12 bold" if grid else "Impact 24",
                              fg="white",
                              bg=bgColor,
                              **kwargs)
        self.label.grid(column=0, row=0) if grid else self.label.pack()
        self.pack()
