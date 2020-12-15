import tkinter as tk
import skinter as sk
import gui


class MainMenu(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.lbl_header = tk.Label(self, gui.cnf_header)
        self.btn_play = sk.Button(self, cnf=gui.cnf_button, text="Play", command=self.show_game)
        self.btn_settings = sk.Button(self, cnf=gui.cnf_button, text="Settings", command=self.show_settings)
        self.btn_exit = sk.Button(self, cnf=gui.cnf_button, text="Quit", command=master.destroy)

        self.lbl_header.pack()
        self.btn_play.pack()
        self.btn_settings.pack()
        self.btn_exit.pack(fill='x')

    def show_settings(self):
        self.pack_forget()
        self.master.settings.pack()

    def show_game(self):
        self.pack_forget()
        self.master.game.pack()


class SlotsGame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.lbl_header = tk.Label(self, gui.cnf_header)
        self.canv_slotsDisplay = tk.Canvas(self)

        self.lbl_header.pack()
        self.canv_slotsDisplay.pack()


class Settings(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.lbl_header = tk.Label(self, gui.cnf_header, text="SETTINGS")

        self.lbl_header.pack()
