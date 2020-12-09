import tkinter as tk
from misc.utility import light_value as lv


class ColorButton(tk.Button):
    def __init__(self, master, color=None, **kwargs):
        colors = {
            "grey": {
                "bg": "#404040",
                "fg": "#808080",
                "active_bg": "#202020",
                "active_fg": "#505050",
            },
            "green": {
                "bg": "#77cc77",
                "fg": "#005500",
                "active_bg": "#55aa55",
                "active_fg": "#003300",
            },
        }

        self.bg = colors[color]["bg"]
        self.fg = colors[color]["fg"]
        self.active_bg = colors[color]["active_bg"]
        self.active_fg = colors[color]["active_fg"]

        super().__init__(master,
                         fg=self.fg,
                         activeforeground=self.active_fg,
                         bg=self.bg,
                         activebackground=self.active_bg,
                         relief="flat",
                         **kwargs)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, _):
        if self["state"] != "disabled":
            self["bg"] = lv(self.bg, 1.2)
            self["fg"] = lv(self.fg, 1.2)

    def on_leave(self, _):
        self["bg"] = self.bg
        self["fg"] = self.fg
