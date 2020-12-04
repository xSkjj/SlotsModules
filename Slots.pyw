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

# bind functions to events
gui.root.bind("<Return>", gui.spin.try_spin)
gui.root.protocol("WM_DELETE_WINDOW", gui.utility.on_close)

# keep the window open
gui.root.mainloop()
