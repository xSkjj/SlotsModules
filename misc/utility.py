import misc
import misc.gui


def show_settings():
    misc.gui.amtInput.unbind("<Return>")
    misc.gui.settingsFrame.place(height=misc.gui.root.winfo_height(), width=misc.gui.root.winfo_width())


def hide_settings():
    misc.gui.amtInput.bind("<Return>", misc.gui.spin.try_spin)
    misc.gui.settingsFrame.place_forget()


def reset_settings():
    misc.configQ = misc.config


def q_setting(sect, key, value):
    misc.configQ[sect][key] = value


def apply_settings():
    misc.config = misc.configQ
    with open("settings.ini", 'w') as settings:
        misc.config.write(settings)
