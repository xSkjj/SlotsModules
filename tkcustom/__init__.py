import tkinter as tk
from misc import utility, bgColor


class Button(tk.Button):
    def __init__(self, master, color, **kwargs):
        self._diff = -80 if utility.is_bright(color) else 80
        self.bg = color
        self.fg = utility.set_brightness(color, self._diff)
        self.abg = utility.set_brightness(color, -16)
        self.afg = utility.set_brightness(color, self._diff - 16)
        super().__init__(master,
                         bg=color,
                         fg=self.fg,
                         activebackground=self.abg,
                         activeforeground=self.afg,
                         relief="flat",
                         **kwargs)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, _):
        if self["state"] != "disabled":
            self["bg"] = utility.set_brightness(self.bg, 20)
            self["fg"] = utility.set_brightness(self.fg, 20)

    def on_leave(self, _):
        self["bg"] = self.bg
        self["fg"] = self.fg


class ColorPicker(Button):
    def __init__(self, master, color, **kwargs):
        super().__init__(master, color,
                         text="pick",
                         font="Consolas 12 bold",
                         **kwargs)


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
        self.leftSlider = Button(self, "#404040",
                                 text="<",
                                 font=font,
                                 width=4)
        self.textLabel = tk.Label(self,
                                  font=font,
                                  bg=self.leftSlider["bg"],
                                  width=6)
        self.rightSlider = Button(self, "#404040",
                                  text=">",
                                  font=font,
                                  width=4)
        self["bg"] = self.leftSlider["bg"]

        self.leftSlider.grid(column=0, row=0)
        self.textLabel.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def slide(self):
        pass  # TODO
