import tkinter as tk


class Button(tk.Button):
    """
    Custom tkinter Button Widget
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._init_colors()

    def _init_colors(self):
        pass
