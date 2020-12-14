import tkinter as tk


class Button(tk.Button):
    """
    Custom tkinter Button Widget
    """

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self._init_colors()
        self.config(**kwargs)

    def _init_colors(self):
        pass
