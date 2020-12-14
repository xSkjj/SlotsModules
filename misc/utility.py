from misc import gui, ConfigParser


def show_settings():
    gui.amtInput.unbind("<Return>")
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def hide_settings():
    gui.amtInput.bind("<Return>", gui.spin.try_spin)
    gui.settingsFrame.place_forget()


def change_setting(sect, key, value):
    config = ConfigParser()
    config.read("settings.ini")
    config[sect][key] = value
    with open("settings.ini", 'w') as settings:
        config.write(settings)
