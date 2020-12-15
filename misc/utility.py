from misc import gui, config


def show_settings():
    gui.amtInput.unbind("<Return>")
    gui.settingsFrame.place(height=gui.root.winfo_height(), width=gui.root.winfo_width())


def hide_settings():
    gui.amtInput.bind("<Return>", gui.spin.try_spin)
    gui.settingsFrame.place_forget()


def reset_settings():
    gui.slotAmtSlider.currentSlide["text"] = str(gui.misc.slotAmt)
    gui.fastSpinSlider.currentSlide["text"] = ["Off", "On"][gui.misc.fastSpin]


def change_setting(sect, key, value):
    config[sect][key] = value
    with open("settings.ini", 'w') as settings:
        config.write(settings)
