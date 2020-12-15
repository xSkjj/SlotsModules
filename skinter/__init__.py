import tkinter as tk
from tkinter import colorchooser
from skinter import colortools as ct


class Button(tk.Button):
    """
    Custom tkinter Button Widget
    """

    def __init__(self, master, color="#484848", **kwargs):
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
        _diff = 128 if ct.is_dark(color) else -128
        self.bg = color
        self.fg = ct.color_math(color, _diff)
        self.abg = ct.color_math(color, -16)
        self.afg = ct.color_math(color, _diff - 16)

    def _on_enter(self, _):
        """
        you shall not use this!
        """
        if self["state"] != "disabled":
            self["bg"] = ct.color_math(self.bg, 20)
            self["fg"] = ct.color_math(self.fg, 20)

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
                         text="choose color",
                         width=16,
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
        super().__init__(master, bg=master["bg"], **kwargs)
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
    """
    A Widget for switching through an array
    """

    def __init__(self, master, default_value, slides, callback=None, font="Arial 10 bold", **kwargs):
        self._index = slides.index(default_value) if slides.count(default_value) else 0
        super().__init__(master, **kwargs)
        self.leftSlider = Button(self, master["bg"],
                                 command=lambda: self._slide(slides, 0, callback),
                                 text="<",
                                 font=font,
                                 width=4)
        self.currentSlide = tk.Label(self,
                                     text=default_value,
                                     font=font,
                                     bg=master["bg"],
                                     fg="white",
                                     width=8)
        self.rightSlider = Button(self, master["bg"],
                                  command=lambda: self._slide(slides, 1, callback),
                                  text=">",
                                  font=font,
                                  width=4)
        self["bg"] = master["bg"]

        self._check_slides(slides)

        self.leftSlider.grid(column=0, row=0)
        self.currentSlide.grid(column=1, row=0)
        self.rightSlider.grid(column=2, row=0)

    def _check_slides(self, slides):
        if not self._index:
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
        self.currentSlide["text"] = slides[self._index]
        self._check_slides(slides)
        callback(slides[self._index]) if callback else None


class OkCancelApply(tk.Frame):
    """
    "Ok"-button, "cancel"-button and "apply"-button for settings
    """

    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(master, bg=master["bg"], **kwargs)
        self.ok = Button(self, "#404040",
                         command=self._ok,
                         font="Consolas 12",
                         text="OK")
        self.cancel = Button(self, "#404040",
                             command=self._cancel,
                             font="Consolas 12",
                             text="Cancel")
        self.apply = Button(self, "#404040",
                            command=self._apply,
                            font="Consolas 12",
                            text="Apply")

        self.ok.grid(column=0, row=0, padx=2)
        self.cancel.grid(column=1, row=0, padx=2)
        self.apply.grid(column=2, row=0, padx=2)

    def _ok(self):
        self.master.applySettings()
        self.master.place_forget()

    def _cancel(self):
        self.master.resetSettings()
        self.master.place_forget()

    def _apply(self):
        self.master.applySettings()
