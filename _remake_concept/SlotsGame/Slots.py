import tkinter as tk
from gui import mainframes as mf


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mainMenu = mf.MainMenu(self)
        self.game = mf.SlotsGame(self)
        self.settings = mf.Settings(self)

        self.mainMenu.pack()


if __name__ == '__main__':
    App().mainloop()
