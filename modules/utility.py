from modules import gui


def on_close():
    # insert something that kills still running threads
    gui.root.destroy()


def show_settings():
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())
