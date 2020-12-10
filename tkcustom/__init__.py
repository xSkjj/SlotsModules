import tkinter as tk
from tkinter import colorchooser
from misc import utility, gui


class Button(tk.Button):
    """
    Custom tkinter Button Widget
    """

    def __init__(self, master, color, **kwargs):
        self._init_colors(color)
        super().__init__(master,
                         bg=self.bg,
                         fg=self.fg,
                         activebackground=self.abg,
                         activeforeground=self.afg,
                         relief="flat",
                         **kwargs)

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _init_colors(self, color):
        """
        forbidden, unless...
        """
        _diff = -80 if utility.is_bright(color) else 80
        self.bg = color
        self.fg = utility.set_brightness(color, _diff)
        self.abg = utility.set_brightness(color, -16)
        self.afg = utility.set_brightness(color, _diff - 16)

    def _on_enter(self, _):
        """
        you shall not use this!
        """
        if self["state"] != "disabled":
            self["bg"] = utility.set_brightness(self.bg, 20)
            self["fg"] = utility.set_brightness(self.fg, 20)

    def _on_leave(self, _):
        """
        access denied
        """
        self["bg"] = self.bg
        self["fg"] = self.fg

    def change_color(self, color):
        """
        Change the button color,
        along with the following variables:
        .bg, .fg, .abg, .afg
        """
        self._init_colors(color)
        self.config(bg=self.bg,
                    fg=self.fg,
                    activebackground=self.abg,
                    activeforeground=self.afg)


class ColorChooser(Button):
    """
    Custom Tkinter Button that
    opens a color chooser window and
    changes its color to the chosen color
    with a callback function to use the
    selected color value in external stuff
    """

    def __init__(self, master, color, callback=None, **kwargs):
        super().__init__(master, color,
                         text="pick",
                         font="Consolas 12 bold",
                         command=lambda: self.askcolor(callback),
                         **kwargs)

    def askcolor(self, callback=None):
        """
        Opens a color chooser window and
        changes the button color to the chosen color,
        along with the following variables:
        .bg, .fg, .abg, .afg
        and calls a callback with the color as a parameter
        """
        rgb, color = colorchooser.askcolor()
        super().change_color(color) if color else None
        callback(color) if callback and color else None


class Section(tk.Frame):
    """
    Custom Tkinter Frame with a Label
    """

    def __init__(self, master, text=None, grid=False, pack=True, **kwargs):
        super().__init__(master, bg=gui.rootBG, **kwargs)
        self.label = tk.Label(self,
                              text=text,
                              font="Consolas 12 bold" if grid else "Impact 24",
                              fg="white",
                              bg=self["bg"])
        self.label.grid(column=0, row=0, padx=4, sticky='w') if grid else self.label.pack()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.pack(padx=20, pady=8, fill='x') if pack else None


class TextSlider(tk.Frame):
    def __init__(self, master, slides=' ', default_index=0, callback=None, font="Arial 10 bold"):
        self._index = default_index
        super().__init__(master)
        self.leftSlider = Button(self, "#404040",
                                 command=lambda: self._slide(slides, 0, callback),
                                 text="<",
                                 font=font,
                                 width=4)
        self.textLabel = tk.Label(self,
                                  text=slides[self._index],
                                  font=font,
                                  bg=self.leftSlider["bg"],
                                  fg="white",
                                  width=6)
        self.rightSlider = Button(self, "#404040",
                                  command=lambda: self._slide(slides, 1, callback),
                                  text=">",
                                  font=font,
                                  width=4)
        self["bg"] = self.leftSlider["bg"]

        self._check_slides(slides)

        self.leftSlider.grid(column=0, row=0)
        self.textLabel.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def _check_slides(self, slides):
        if self._index == 0:
            self.leftSlider["state"] = "disabled"
            self.leftSlider["bg"] = self.leftSlider.bg
        else:
            self.leftSlider["state"] = "normal"

        if self._index == len(slides) - 1:
            self.rightSlider["state"] = "disabled"
            self.rightSlider["bg"] = self.rightSlider.bg
        else:
            self.rightSlider["state"] = "normal"

    def _slide(self, slides, direction, callback=None):
        self._index += 1 if direction else -1
        self.textLabel["text"] = slides[self._index]
        self._check_slides(slides)
        callback(slides[self._index]) if callback else None
