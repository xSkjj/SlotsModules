from modules import gui

# display the elements
gui.header.pack(pady=4)
gui.settingsBtn.place(x=4, y=4, width=40, height=40)
gui.slotCanvas.pack(padx=10, pady=(20, 40))
gui.output.pack(fill='x', padx=20, pady=25)
gui.amtInputLabel.grid(column=0, row=0, padx=5)
gui.amtInput.grid(column=0, row=1, padx=5)
gui.spinBtn.grid(column=1, row=0, rowspan=2, padx=5, sticky='s')
gui.userInputs.pack()
gui.balLabel.pack(pady=10)

gui.closeSettingsBtn.place(width=40, height=40)
gui.bgColorPicker.grid(column=1, row=0, sticky="ew")
gui.bgSlotsPicker.grid(column=1, row=0, sticky="ew")
gui.slotAmtSlider.grid(column=1, row=0, sticky="ew")
gui.fastSpinCheck.grid(column=1, row=0, sticky="ew")

# May do:
#
# can change all settings while still running
# Save and exit, cancel, apply buttons
# main menu and stuff
# class App(tk.Frame)
# improve performance of spin animation
#
# TODO: add remaining settings functionality
#

# bind functions to events
gui.amtInput.bind("<Return>", gui.spin.try_spin)  # same as clicking the spin button

# keep the window open
gui.root.mainloop()
