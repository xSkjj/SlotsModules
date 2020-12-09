import tkinter as tk

from misc import utility, bgColor


class Button(tk.Button):
    def __init__(self, master, color, **kwargs):
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
            self["bg"] = utility.light_value(self.bg, 1.2)
            self["fg"] = utility.light_value(self.fg, 1.2)

    def on_leave(self, _):
        self["bg"] = self.bg
        self["fg"] = self.fg


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
        self.leftSlider = Button(self, "grey",
                                 text="<",
                                 font=font,
                                 width=4)
        self.textLabel = tk.Label(self,
                                  font=font,
                                  bg=self.leftSlider["bg"],
                                  width=6)
        self.rightSlider = Button(self, "grey",
                                  text=">",
                                  font=font,
                                  width=4)
        self["bg"] = self.leftSlider["bg"]

        self.leftSlider.grid(column=0, row=0)
        self.textLabel.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def slide(self):
        pass  # TODO
