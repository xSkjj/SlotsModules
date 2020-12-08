import tkinter as tk


class ColorButton(tk.Button):
    def __init__(self, master, color=None, **kwargs):
        colors = {
            "grey": {
                "fg": "#808080",
                "active_fg": "#505050",
                "bg": "#404040",
                "active_bg": "#202020",
            },
            "green": {
                "fg": "#005500",
                "active_fg": "#003300",
                "bg": "#77cc77",
                "active_bg": "#55aa55",
            },
        }

        fg = colors[color]["fg"]
        active_fg = colors[color]["active_fg"]
        bg = colors[color]["bg"]
        active_bg = colors[color]["active_bg"]

        super().__init__(master,
                         fg=fg,
                         activeforeground=active_fg,
                         bg=bg,
                         activebackground=active_bg,
                         relief="flat",
                         **kwargs)
